from stransi import Ansi
from ochre import RGB, Hex
import stransi
from stransi.ansi import Text
from stransi.color import Color

global line, ansi_code_stage, code_start, parsing_flags, fg

line = ""
# 0: not a ansi code
# 1: ESC code found
# 2: [ Found
# 3: m Found
ansi_code_stage = 0
code_start = -1
send_char = True
parsing_flags = []
def clear_flags():
    flags = []

DEFAULT_COLOR = Hex("FFFFFF")

fg = DEFAULT_COLOR

def new_char(char):
    global line, ansi_code_stage, code_start, send_char, parsing_flags
    global fg
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
        assert len(list(parsed_code.escapes())) == 1 # there should only be one escape
        print(list(parsed_code.instructions()))
        for i in parsed_code.instructions():
            if type(i) == Text:
                break
            match type(i):
                case stransi.SetColor:
                    if i.role == stransi.color.ColorRole.FOREGROUND:
                        fg = i.color.rgb
                case stransi.SetAttribute:
                    match i.attribute:
                        case stransi.attribute.Attribute.NORMAL:
                            fg = DEFAULT_COLOR
        print(fg)

        ansi_code_stage = 0
        send_char = True
        raw_hex = fg.hex.hex_code
        if type(raw_hex) == int:
            hexcode = "{:06x}".format(fg.hex.hex_code)
        else:
            hexcode = raw_hex
        return f"<color=#{hexcode}>"
    
    if char == "\n":
        line = ""
    if send_char:
        return char
    return ""
    
