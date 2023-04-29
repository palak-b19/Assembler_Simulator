op_code={'add':'00000',
         'sub':'00001',
         'mov':'00010',
         'ld':'00100',
         'st':'00101',
         'mul':'00110',
         'div':'00111',
         'rs':'01000',
         'ls':'01001',
         'xor':'01010',
         'or':'01011',
         'and':'01100',
         'not':'01101',
         'cmp':'01110',
         'jmp':'01111',
         'jlt':'11100',
         'jgt':'11101',
         'je':'11111',
         'hlt':'11010'}
reg={'R0':'000',
     'R1':'001',
     'R2':'010',
     'R3':'011',
     'R4':'100',
     'R5':'101',
     'R6':'110'}

error_counter=0

def imm_to_bin(n):
     return "{0:07b}".format(int(n))
    

def type_A(lst):
    opcode, r1, r2, r3 = lst[0], lst[1], lst[2], lst[3]
    return op_code.get(opcode) + '00' + reg.get(r1) + reg.get(r2) + reg.get(r3)+'\n'

def type_B(lst):
    opcode, r1, imm = lst[0], lst[1], lst[2]
    return op_code.get(opcode) + '0' +  reg.get(r1) + imm_to_bin(imm[1:]) + '\n'

def type_C(lst):
    opcode, r1, r2= lst[0], lst[1], lst[2]
    return op_code.get(opcode) + '00000' + reg.get(r1) + reg.get(r2) + '\n'

def type_D(lst):
    opcode, r1, m_add = lst[0], lst[1], lst[2]
    return op_code.get(opcode) + '0' + reg.get(r1) + m_add  #correct to get memory add and handle error here

def type_E(lst):
    opcode, m_add= lst[0], lst[1]
    return op_code.get(opcode) + '0000' +m_add

def type_F(lst):
    opcode= lst[0]
    return op_code.get(opcode) + '00000000000'

def identify_type(lst):
    if len(lst)==4:
        print(type_A(lst))
    elif len(lst)==2:
        print(type_E(lst))
    elif len(lst)==1:
        print(type_F(lst))
    else:
        if '$' in lst[-1]:
            print(type_B(lst))
        elif 'r' in lst[-1]:
            print(type_C(lst))
        elif lst[0] == 'ld' or lst[0] == 'st':
            print(type_D(lst))

f = open('input.txt', 'r')
page = f.read()
lines = page.split('\n')
print(lines)
all_instructions=[x for x in lines if x!=""]
print(all_instructions)

if "hlt" not in all_instructions:
    error_counter+=1
    print("Missing hlt instruction")
print(error_counter)

if "hlt" in all_instructions:
    if (all_instructions[-1]!="hlt"):
        error_counter+=1
        print("Error as hlt is not being used as the last instruction")
    print(error_counter)


if error_counter==0:
    for line in all_instructions:
        words = line.split() 
        identify_type(words)
