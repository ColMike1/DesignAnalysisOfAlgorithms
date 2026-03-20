def sum(a, b):
    print('ciao')
    return a + b


import dis      # Disassembler of Python byte code into mnemonics.

dis.dis(sum)    # dis.dis(...) Disassemble classes, methods, functions, and other compiled objects. 
                # In this case, the sum function

