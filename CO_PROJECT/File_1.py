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

op_type={"A":['add','sub','mul','xor','or','and'],
         "B":['mov','rs','ls'],
         "C":['mov','div','not','cmp'],
         "D":['ld','st'],
         "E":['jmp','jlt','jgt','je'],
         "F":['hlt']}

reg={'R0':'000',
     'R1':'001',
     'R2':'010',
     'R3':'011',
     'R4':'100',
     'R5':'101',
     'R6':'110'}

#global error_counter
error_counter=0

def hlt_checker():
    if "hlt" not in all_instructions:
        global error_counter
        error_counter += 1
        print("Missing hlt instruction")
    else:
        if (all_instructions[-1] != "hlt"):
            error_counter += 1
            print("Error as hlt is not being used as the last instruction")
        for instruction in all_instructions[0:-2]:
            if instruction == "hlt":
                error_counter += 1
                print("ERROR: General syntax error.") # hlt occurs before last instruction
                return False

def check_imm(n):
    if 0<=int(n)<=127:
        return True
    else:
        print("Illegal immediate value")
        global error_counter
        error_counter+=1
        return False

def imm_to_bin(n):
    return "{0:07b}".format(int(n))
    
def type_A(lst):
    if len(lst)==4:
        if lst[0] in op_type.get("A"):
            if (lst[1] in reg.keys()) & (lst[2] in reg.keys()) & (lst[3] in reg.keys()):
                opcode, r1, r2, r3 = lst[0], lst[1], lst[2], lst[3]
                return op_code.get(opcode) + '00' + reg.get(r1) + reg.get(r2) + reg.get(r3)+'\n'
            else:
                global error_counter
                error_counter += 1
                print("ERROR: Typos in register name")
        else:
            error_counter += 1
            if lst[0] in op_code.keys():
                print("ERROR: instruction not supported in type A instruction.")
            else:
                print("ERROR: Typos in instruction name")
    else:
        error_counter+=1
        print("ERROR: Syntax error")

def type_B(lst):
    if len(lst)==3:
        if lst[0] in op_type.get('B'):
            if (lst[1] in reg.keys()):
                opcode, r1, imm = lst[0], lst[1], lst[2]
                return op_code.get(opcode) + '0' +  reg.get(r1) + imm_to_bin(imm[1:]) + '\n'
            else:
                global error_counter
                error_counter += 1
                print("ERROR: Typos in register name")
        else:
            error_counter += 1
            if lst[0] in op_code.keys():
                print("ERROR: instruction not supported in type B instruction.")
            else:
                print("ERROR: Typos in instruction name")
    else:
        error_counter+=1
        print("ERROR: Syntax error")

def type_C(lst):
    if len(lst)==3:
        if lst[0] in op_type.get('C'):
            if (lst[1] in reg.keys()) & (lst[2] in reg.keys()):
                opcode, r1, r2 = lst[0], lst[1], lst[2]
                return op_code.get(opcode) + '00000' + reg.get(r1) + reg.get(r2) + '\n'
            else:
                global error_counter
                error_counter += 1
                print("ERROR: Typos in register name")
        else:
            error_counter += 1
            if lst[0] in op_code.keys():
                print("ERROR: instruction not supported in type C instruction.")
            else:
                print("ERROR: Typos in instruction name")
    else:
        error_counter+=1
        print("ERROR: Syntax error")

def type_D(lst):
    if len(lst)==3:
        if lst[0] in op_type.get("D"):
            if lst[1] in reg.keys():
                # modify to handle m_add error
                if (1):  #replace with condition if m_add is correct
                    opcode, r1, m_add = lst[0], lst[1], lst[2]
                    return op_code.get(opcode) + '0' + reg.get(
                        r1) + m_add  # correct to get memory add and handle error here
                else:
                    global error_counter
                    error_counter += 1
                    print("ERROR: in m_add")
            else:
                error_counter += 1
                print("ERROR: Typos in register name")

        else:
            error_counter += 1
            if lst[0] in op_code.keys():
                print("ERROR: instruction not supported in type E instruction.")
            else:
                print("ERROR: Typos in instruction name")

    else:
        error_counter+=1
        print("ERROR: Syntax error")

def type_E(lst):
    if len(lst)==2:
        if lst[0] in op_type.get("E"):
            # modify to handle m_add error
            if (1):  #replace with condition if m_add is correct
                opcode, m_add = lst[0], lst[1]
                return op_code.get(opcode) + '0000' + m_add
            else:
                global error_counter
                error_counter += 1
                print("ERROR: in m_add")
        else:
            error_counter += 1
            if lst[0] in op_code.keys():
                print("ERROR: instruction not supported in type E instruction.")
            else:
                print("ERROR: Typos in instruction name")

    else:
        error_counter+=1
        print("ERROR: Syntax error")

def type_F(lst):
    opcode= lst[0]
    return op_code.get(opcode) + '00000000000'

def identify_type(lst):
    if len(lst)==4:
        print("a")
        print(type_A(lst))
    elif len(lst)==2:
        print("e")
        print(type_E(lst))
    elif len(lst)==1:
        print(type_F(lst))
    else:
        if '$' in lst[-1]:
            print("b")
            print(type_B(lst))
        elif 'R' in lst[-1]:
            print("c")
            print(type_C(lst))
        elif lst[0] == 'ld' or lst[0] == 'st':
            print("d")
            print(type_D(lst))

def var_not_declared(lst):
    declared={}
    for i in lst:
        if i.startswith('var'):
            var_name=line.split()[1]
            declared[var_name]="declared"
    for i in lst:
        word=i.split()
        for w in word:
            if 'var' in w:
                var_name=word[-1]
                if var_name not in declared:
                    print(f"ERROR: variable {var_name} is not declared")
           

f = open('input.txt','r')
page = f.read()
all_instructions=[x for x in page.split('\n') if x!=""]
print(all_instructions)
hlt_checker()
var_not_declared(all_instructions)

for line in all_instructions:
    if "$" in line:
        k=line.split()
        print("k=",k)
        imm=k[-1]
        check_imm(imm[1:])
c=all_instructions[3]
print(c)
identify_type(c)
if error_counter==0:
    for line in all_instructions:
        words = line.split() 
        identify_type(words) 
   
print(error_counter)
