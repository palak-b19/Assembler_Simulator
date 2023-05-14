"""                            ASUMPTIONS:
  label type instruction: only 1 label declaration per line i.e, ":"occurs only once.
"""

op_code = {
  'add': '00000',
  'sub': '00001',
  'mov': {'00010', '00011'},  #B,C
  'ld': '00100',
  'st': '00101',
  'mul': '00110',
  'div': '00111',
  'rs': '01000',
  'ls': '01001',
  'xor': '01010',
  'or': '01011',
  'and': '01100',
  'not': '01101',
  'cmp': '01110',
  'jmp': '01111',
  'jlt': '11100',
  'jgt': '11101',
  'je': '11111',
  'hlt': '11010'
}
op_type = {
  "A": ['add', 'sub', 'mul', 'xor', 'or', 'and'],
  "B": ['mov', 'rs', 'ls'],
  "C": ['mov', 'div', 'not', 'cmp'],
  "D": ['ld', 'st'],
  "E": ['jmp', 'jlt', 'jgt', 'je'],
  "F": ['hlt']
}
reg = {
  'R0': '000',
  'r0': '000',
  'R1': '001',
  'r1': '001',
  'R2': '010',
  'r2': '010',
  'R3': '011',
  'r3': '011',
  'R4': '100',
  'r4': '100',
  'R5': '101',
  'r5': '101',
  'R6': '110',
  'r6': '110',
  'FLAGS': '111'
}


def error_lno2(lno):
  for i in range(len(empty_lines)):
    if empty_lines[i] == all_instructions[lno]:
      return i + 1


def error_lno(lno):
  for i in range(len(all_with_elines)):
    if all_with_elines[i] == all_instructions[lno]:
      return i + 1


def error_inst(l):
  for i in range(len(all_with_elines)):
    if all_with_elines[i][0] == l and all_with_elines[i][1] == False:
      all_with_elines[i][1] = True
      return (i + 1)


def error_1(lst, lno):
  lst_str = []
  for i in lst:
    i_str = " ".join(i)
    lst_str.append(i_str)
  for i in range(len(empty_lines)):
    if empty_lines[i] == lst_str[lno]:
      return i + 1


def hlt_checker(list, tmp_words):
  flag = 1
  tmp_flag = 0
  for word in tmp_words:
    word_index = tmp_words.index(word)
    if "hlt" in word:
      tmp_flag |= 1
  if not (tmp_flag):
    flag = 0
    error_output.append("Missing hlt instruction.")
  else:
    if (tmp_words[-1][-1] != "hlt"):
      flag = 0
      s = "Error as hlt is not being used as the last instruction.Error in line " + str(
        word_index + 1)
      error_output.append(s)
    for instruction in tmp_words[0:-1]:
      if instruction[-1] == "hlt":
        flag = 0
        s = "ERROR_in_hlt: General syntax error.Error in line " + str(
          word_index + 1)
        error_output.append(s)
  return flag


def check_imm(n, tmp_ins):
  if 0 <= int(n) <= 127:
    return True
  else:
    for it in empty_lines:
      if tmp_ins in it:
        lab_add = empty_lines.index(it) + 1
    s = "Illegal immediate value. Error in line" + str(lab_add)
    error_output.append(s)
    return False


def imm_to_bin(n):
  return "{0:07b}".format(int(n))


def check_labels(list1):
  flag = 1
  for word in list1:
    if word[0] in op_type["E"]:
      label = word[1]
      if label not in labels_list:
        word = " ".join(word)
        indx = empty_lines.index(word) + 1
        s = "ERROR: Use of undefined label.Error in line " + str(indx)
        error_output.append(s)
        flag = 0
  return flag


def flags():
  flag = 1
  for k in range(0, len(inst)):
    i = inst[k]
    if "FLAGS" in i:
      if not (i[0] == "mov" and i[-1] == "FLAGS" and len(i) == 3):
        flag = 0
        s = "ERROR: Illegal use of FLAGS register. Error in line " + str(error_inst(i))
        error_output.append(s)
  return flag


def typos(list):
  flag = 1
  countf = 0
  for words in list:
    countf += 1
    flag &= identify_error_type(words)
  return flag


def var_not_dec(inst, var):
  flag = 1
  for i, ins in enumerate(inst):
    if (ins[0] in op_type.get("D")) and (ins[-1] not in var) and len(ins) == 2:
      s = f"ERROR: variable {ins[-1]} is not declared. Error in line " + str(
        error_1(inst, i))
      error_output.append(s)
      flag = 0
    """elif ins[0] in op_type.get("E") and ins[-1] not in labels_list:
      s = f"ERROR: variable {ins[-1]} is not declared. Error in line " + str(
        error_1(inst, i))
      error_output.append(s)
      flag = 0"""
  return flag


def not_defined_at_beginning(list1):
  flag = 1
  for i, line in enumerate(list1):
    if line[0] == "var" and len(line) == 2:
      if line[-1] in op_code.keys():
        s = "Opcode cannot be used as variable name. Error in line " + str(
          error_1(list1, i))
        error_output.append(s)
        flag = 0
  functions = [line[0] for line in tmp_words]
  j = 0
  while functions[j] == 'var':
    j += 1
  for i in range(j, len(functions)):
    if functions[i] == 'var' and len(tmp_words[i]) == 2:
      s = "ERROR:Variables not declared at the beginning. Error in line " + str(
        error_inst(tmp_words[i]))
      error_output.append(s)
      flag = 0
  return flag


def immediate():
  flag = 1
  for line in all_instructions:
    if "$" in line:
      k = line.split()
      imm = k[-1]
      if imm[1:].isdigit():
        imm = int(imm[1:])
        if not check_imm(imm, line):
          flag = 0
      else:
        s = "Immediate is not a numeric value. Error in line " + str(
          error_lno2(all_instructions.index(line)))
        error_output.append(s)
        flag = 0
  return flag


def error_type_A(lst):
  flag = 1
  if len(lst) == 4:
    if not (lst[1] in reg.keys()) & (lst[2] in reg.keys()) & (lst[3]
                                                              in reg.keys()):
      s = "ERROR:Typos in register name. Error in line " + str(error_inst(lst))
      error_output.append(s)
      flag = 0
  else:
    s = "ERROR: General Syntax error. Error in line " + str(error_inst(lst))
    error_output.append(s)
    flag = 0
  return flag


def error_type_B(lst):
  flag = 1
  if len(lst) == 3:
    if not (lst[1] in reg.keys()):
      s = "ERROR:Typos in register name. Error in line " + str(error_inst(lst))
      error_output.append(s)
      flag = 0
  else:
    s = "ERROR: General Syntax error. Error in line " + str(error_inst(lst))
    error_output.append(s)
    flag = 0
  return flag


def error_type_C(lst):
  flag = 1
  if len(lst) == 3:
    if not (lst[1] in reg.keys()) & (lst[2] in reg.keys()):
      indx = empty_lines.index(" ".join(lst)) + 1
      s = "ERROR:Typos in register name. Error in line " + str(indx)
      error_output.append(s)
      flag = 0
  else:
    s = "ERROR: General Syntax error. Error in line " + str(
      empty_lines.index(" ".join(lst)) + 1)
    error_output.append(s)
    flag = 0
  return flag


def error_type_D(lst, labl, varl):
  flag = 1
  if len(lst) == 3:
    if lst[1] in reg.keys():
      if lst[-1] in labl:
        flag = 0
        print("ERROR: Use of label as variable.\nError in line ",
              error_inst(lst))
        s = "ERROR: Use of label as variable.\nError in line " + str(
          error_inst(lst))
        error_output.append(s)
      elif (not (lst[2] in varl)):
        flag = 0
        s = "ERROR: only variables can be used as m_add. Error in line " + str(
          error_inst(lst))
        error_output.append(s)
    else:
      flag = 0
      s = "ERROR: Typos in register name. Error in line " + str(
        error_inst(lst))
      error_output.append(s)
      if lst[-1] + ":" in labl:
        s = "ERROR: Use of label as variable. Error in line " + str(
          error_inst(lst))
        error_output.append(s)
  else:
    s = "ERROR: General Syntax error. Error in line " + str(error_inst(lst))
    error_output.append(s)
    flag = 0
  return flag


def error_type_E(lst, varl):
  flag = 1
  if len(lst) == 2:
    if lst[-1] in varl:
      flag = 0
      s = "ERROR: Use of variable as label. Error in line " + str(error_inst(lst))
      error_output.append(s)
    elif not (lst[-1] in labels_list):
      flag = 0
      s = "ERROR: in m_add Error in line " + str(error_inst(lst))
      error_output.append(s)
  else:
    flag = 0
    s = "ERROR: General Syntax error.Error in line " + str(error_inst(lst))
    error_output.append(s)
    if lst[-1] in varl:
      s = "ERROR: Use of variable as label. Error in line " + str(error_inst(lst))
  return flag


def identify_error_type(lst):
  flag = 1
  if lst[0] in ['mov']:
    if lst[-1][0] == '$':
      inst_type.append("b")
      flag = error_type_B(lst)
    else:
      flag = error_type_C(lst)
      inst_type.append("c")
  elif lst[0] in op_type.get("A"):
    inst_type.append("a")
    flag = error_type_A(lst)
  elif lst[0] in op_type.get("B"):
    inst_type.append("b")
    flag = error_type_B(lst)
  elif lst[0] in op_type.get("C"):
    inst_type.append("c")
    flag = error_type_C(lst)
  elif lst[0] in op_type.get("D"):
    inst_type.append("d")
    flag = error_type_D(lst, labels_list, var)
  elif lst[0] in op_type.get("E"):
    inst_type.append("e")
    flag = error_type_E(lst, var)
  elif lst[0] in op_type.get("F"):
    inst_type.append("f")
  else:
    s = "ERROR:Typos in instruction name. Error in line " + str(
      error_inst(lst))
    error_output.append(s)
    flag = 0
  return flag


def check_empty():
  flag = 1
  if tmp_words == []:
    flag = 0
    f = open('output.txt', 'w')
    f.write("ERROR: File empty.")
  return flag


# checking all errors
def check_all_errors():
  flag = 1
  if check_empty() == 0:
    flag = 0
    return flag
  if var_not_dec(inst, var) != 1:
    flag = 0
  if not_defined_at_beginning(tmp_words) != 1:
    flag = 0
  if hlt_checker(all_instructions, tmp_words) != 1:
    flag = 0
  if immediate() != 1:
    flag = 0
  if check_labels(tmp_words) != 1:
    flag = 0
  if flags() != 1:
    flag = 0
  if typos(inst) != 1:
    flag = 0
  return (flag and empty_label and flag_out)


#main
#reading input file.
f = open('input1.txt', 'r')
page = f.read()
all_instructions = [x.lstrip().rstrip() for x in page.split('\n') if x != ""]
empty_lines = [x.lstrip().rstrip() for x in page.split('\n')]

all_with_elines, tmp_words, =[], []
for lin in empty_lines:
  lin = lin.split()
  if lin == []:
    all_with_elines.append([[], False])
  elif lin[0][-1] == ":":
    if len(lin) == 1:
      all_with_elines.append([lin, False])
    else:
      all_with_elines.append([lin[1::], False])
  else:
    all_with_elines.append([lin, False])
for line in all_instructions:
  words = line.split()
  tmp_words.append(words)

# classification of labels, var dec & instructions.
inst, inst_type = [], []
labels_list = []
var , var_dic = [], {}
error_output , labels_with_inst =[], []
labels = {}
empty_label ,flag_out = 1, 1
for i in range(0, len(tmp_words)):
  line = tmp_words[i]
  if line[0] == "var":
    if len(line) == 2:
      var.append(line[1])
    else:
      pe = "ERROR: General Syntax error. Error in line " + str(error_inst(line))
      error_output.append(pe)
      flag_out &= 0

  elif line[0][-1] == ":":
    labels_list.append(line[0][0:-1])
    if len(line) == 1:
      pe= "ERROR: empty label encountered. Error in line "+ str(error_inst(line))
      error_output.append(pe)
      empty_label = 0
    else:
      l = " ".join(line)
      labels_with_inst.append(l)
      inst.append(
        line[1:])  # adding the instruction only not the name in the inst list

  elif (line[0] in op_code.keys() and len(line) < 2
        and "hlt" not in line) or line[0] not in op_code.keys():
    pe = "ERROR: General Syntax error. Error in line " + str(error_inst(line))
    error_output.append(pe)
    flag_out &= 0

  else:
    inst.append(line)


#functions to print binary of the specific type of instructions
def type_A(lst):
  opcode, r1, r2, r3 = lst[0], lst[1], lst[2], lst[3]
  return op_code.get(opcode) + '00' + reg.get(r1) + reg.get(r2) + reg.get(
    r3) + '\n'


def type_B(lst):
  opcode, r1, imm = lst[0], lst[1], lst[2]
  if opcode == 'mov':
    return '00010' + '0' + reg.get(r1) + imm_to_bin(imm[1:]) + '\n'
  return op_code.get(opcode) + '0' + reg.get(r1) + imm_to_bin(imm[1:]) + '\n'


def type_C(lst):
  opcode, r1, r2 = lst[0], lst[1], lst[2]
  if opcode == 'mov':
    return '00011' + '00000' + reg.get(r1) + reg.get(r2) + '\n'
  return op_code.get(opcode) + '00000' + reg.get(r1) + reg.get(r2) + '\n'


def type_D(lst):
  opcode, r1, m_add = lst[0], lst[1], str(imm_to_bin(var_dic.get(lst[2])))
  return op_code.get(opcode) + '0' + reg.get(
    r1) + m_add + '\n'


def type_E(lst):
  tmp_label = lst[-1] + ":"
  for i in tmp_words:
    if tmp_label in i:
      tmp_label = i[1::]
  lab_add = inst.index(tmp_label)
  opcode = lst[0]
  return op_code.get(opcode) + '0000' + str(imm_to_bin(lab_add)) + '\n'


def type_F(lst):
  opcode = lst[0]
  return op_code.get(opcode) + '00000000000'


def print_binary():
  out = ""
  for i in range(0, len(inst_type)):
    type = inst_type[i]
    if type == "a":
      out += type_A(inst[i])
    elif type == "b":
      out += type_B(inst[i])
    elif type == "c":
      out += type_C(inst[i])
    elif type == "d":
      out += type_D(inst[i])
    elif type == "e":
      out += type_E(inst[i])
    elif type == "f":
      out += type_F(inst[i])
  f = open('output.txt', 'w')
  f.write(out)

def print_errors():
  out = ""
  for error in error_output:
    out += error
    out += "\n"
  f.write(out)

var_counter = len(all_instructions) - len(var)


for variable in var:
  var_dic[variable] = var_counter
  var_counter = var_counter + 1


if check_empty():
  f = open('output.txt', 'w')
  if check_all_errors() and flag_out:
    print_binary()
  else:
    error_output=sorted(error_output, key=lambda x: x[-2])
    print_errors()
