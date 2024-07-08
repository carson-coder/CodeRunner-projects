from stransi import Ansi
import stransi

global line, ansi_code_stage, code_start

line = ""
# 0: not a ansi code
# 1: ESC code found
# 2: [ Found
# 3: m Found
ansi_code_stage = 0
code_start = -1
send_char = True

def new_char(char):
    global line, ansi_code_stage, code_start, send_char
    line+=char
    
    if ansi_code_stage == 0 and char == "\x1b":
        code_start = len(line) -1 
        ansi_code_stage = 1
        send_char = False
    elif ansi_code_stage == 1 and char == "[":
        ansi_code_stage = 2
    elif ansi_code_stage == 2 and char == "m":
        ansi_code_stage = 3
    elif char not in "0123456789;" or ansi_code_stage != 2: # reset if invalid code
        ansi_code_stage = 0
        send_char = True
        
    if ansi_code_stage == 3: # Found a valid ansi code:
        code = line[code_start:]
        
        parsed_code = Ansi(code)
        assert len(list(Ansi.escapes())) == 1 # there should only be one escape
        
        for i in parsed_code.instructions:
            match type(i):
                case stransi.SetColor:
                    pass
        
        ansi_code_stage = 0
        send_char = True
    
    if char == "\n":
        line = ""
    if send_char:
        return char
    return ""
    