import time, sys
indent = 0 #How many spaces to indent
indentInc = True # Whether indent is increasing or not

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.5) # Pause for half a second

        if indentInc:
            # Increase the number of spaces
            indent += 1
            if indent == 20:
                #CHange direction
                indentInc = False
            else:
                # Decrease the number of spaces
                indent -= 1
                if indent == 0:
                    # Change direction again
                    indentInc = True
except KeyboardInterrupt:
    sys.exit()