def special_keys(raw_input):
    special_keys_linux = {
        '\r': 'Enter',# Carriage return (or '\n' for newline)
        '\n': 'Enter',
        '\x1b': 'Escape',          # Escape key
        '\x1b[A': 'Arrow Up',      # Up arrow key
        '\x1b[B': 'Arrow Down',    # Down arrow key
        '\x1b[D': 'Arrow Left',    # Left arrow key
        '\x1b[C': 'Arrow Right',   # Right arrow key
        '\x1bOP': 'F1',            # Function key F1
        '\x1bOQ': 'F2',            # Function key F2
        '\x1bOR': 'F3',            # Function key F3
        '\x1bOS': 'F4',            # Function key F4
        '\x1b[15~': 'F5',          # Function key F5
        '\x1b[17~': 'F6',          # Function key F6
        '\x1b[18~': 'F7',          # Function key F7
        '\x1b[19~': 'F8',          # Function key F8
        '\x1b[20~': 'F9',          # Function key F9
        '\x1b[21~': 'F10',         # Function key F10
        '\x1b[23~': 'F11',         # Function key F11
        '\x1b[24~': 'F12',         # Function key F12
        '\x1b[H': 'Home',          # Home key
        '\x1b[F': 'End',           # End key
        '\x1b[5~': 'Page Up',      # Page Up key
        '\x1b[6~': 'Page Down',    # Page Down key
        '\x1b[2~': 'Insert',       # Insert key
        '\x1b[3~': 'Delete',       # Delete key
        '\t': 'Tab',               # Tab key
        '\x7f': 'Backspace',       # Backspace key
    }
    
    return special_keys_linux.get(raw_input, raw_input)  # Return the mapped key name or the raw input if not found
