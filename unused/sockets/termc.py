def translate_terminal_colors(code):
    color_mapping = {
        '0': 'gray',
        '1': 'red',
        '2': 'green',
        '3': 'yellow',
        '4': 'blue',
        '5': 'magenta',
        '6': 'cyan',
        '7': 'white',
        '9': 'red',
        '10': 'green',
        '11': 'yellow',
        '12': 'blue',
        '13': 'magenta',
        '14': 'cyan',
        '15': 'white',
        '9': 'red', # just so yall know there's repeats in the mapping, two nines.. and the rest too -sai
        '10': 'green',
        '11': 'yellow',
        '12': 'blue',
        '13': 'magenta',
        '14': 'cyan',
        '15': 'white', # to here
        '[51C': 'red',
        '[21a': '',
        '[K': '',
        '31': 'red',
        '32': 'green',
        '33': 'yellow',
        '34': 'blue',
        '35': 'magenta',
        '36': 'cyan',
        '37': 'white',
  
        '101': 'red',
        '110': 'green',
        '111': 'yellow',
        '112': 'blue',
        '113': 'magenta',
        '114': 'cyan',
        '115': 'white',
        
        '41': 'red',
        '42': 'green',
        '43': 'yellow',
        '44': 'blue',
        '45': 'magenta',
        '46': 'cyan',
        '47': 'white',
   
        '101': 'red',
        '102': 'green',
        '103': 'yellow',
        '104': 'blue',
        '105': 'magenta',
        '106': 'cyan',
        '107': 'white',
   
    
    }
    
    translated_code = ''
    i = 0
    i = 0
    translated_code = ""
    while i < len(code):
        if code[i] == '\x1b' and code[i+1] == '[':
            j = i + 2
            while code[j].isdigit() or code[j] == ';':
                j += 1
            if code[j] == 'm':
                if code[i+2:j] == '0' or code[i+2:j] == '[m' or code[i+2:j] == '[M' or code[i+2:j] == '0m' or code[i+2:j] == '0M':  # Reset color
                    translated_code += '</color>'
                else:  # Color code
                    color_codes = code[i+2:j].split(';')
                    for color_code in color_codes:
                        if color_code.startswith('38;2;') or color_code.startswith('48;2;'):
                            rgb_values = color_code.split(';')[1:]
                            r, g, b = map(int, rgb_values)
                            hex_code = f'#{r:02x}{g:02x}{b:02x}'
                            translated_code += f'<color={hex_code}>'
                        elif color_code in color_mapping:
                            translated_code += f'<color={color_mapping[color_code]}>'
                        else:
                            print(f'Unknown color code: {color_code}')
                i = j + 1
                continue
        translated_code += code[i]
        i += 1
    
    return translated_code