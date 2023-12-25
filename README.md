# Computer Organisation Project

# ASSEMBLER SIMULATOR PROJECT


| Field           | Value              |
| --------------- | ------------------ |
| Course          | CSE112             |
| Course Title    | Computer Organisation |
| Instructor      | Tammam Tillo - https://www.iiitd.ac.in/tammam  |

`PROJECT MEMBERS`

| Name             | Student ID |
|------------------|------------|
| Palak Bhardwaj   | 2022344    |
| Suhani Kalyani   | 2022511    |
| Vanshika Pal     | 2022560    |
| Nandini Jain     | 2022316    |

# Path To Run Assembler
 - CO-project -> CO_A_P1 -> Simple-Assembler -> Assembler.py


# HOW TO EVALUATE

In terminal, go to automatedTesting directory and enter `./run``. A complete report sheet will be generated in the terminal


# To view all changes and history view Old_Assembler 

 # ASSUMPTIONS:
  
  - `Label type instruction`: only 1 label declaration per line i.e, ":"occurs only once.
  
  - `Mov R1 FLAGS` is taken to be a valid command since FLAGS doesn't represent a variable but instead represents a valid register name , where 
  - MOV can be used with two types of instructions , type1- mov register value , mov reg1 reg2 , hence we have taken to be a valid name
  - Use of FLAG register:
    - `FLAGS` is a valid register name
    - `mov reg1 FLAGS` is the only valid  instruction involving FLAG register.

# Project Overview

`automatedTesting`: This folder contains

the sample test cases provided by the evaluator: tests/
the grading script: src
the run file: run

`Simple-Assembler`: This folder contains

Python programme which gives stdin and stdout and is used for automated testing:- main.py
Python programme that reads from read.txt and writes output in write.txt:- readable.py
Python programme that contains basic decimal-binary conversion functions which are used at many instances in the assembler:- CONVERTME.py

`SimpleSimulator`: This folder contains

Python program which takes the binary output from Simple-Assembler/main.py and contains the main programme for execution of each instruction in class ee (execution engine) and the flow of simulator execution and gives the required output in stdout:- main.py
MEM.py contains the class for program memory and all the memory functions required
RF.py contains the class for register data and all the register accessing function required
PC.py contains the class for program counter and all the program counter operations required
opcodes.py contains all the dictionaries for opcodes and registers and their binary address equivalents
Python programme that contains basic decimal-binary conversion functions which are used at many instances in the simulator:- CONVERTME.py

# Assembly Language Compiler

This repository contains a simple assembly language compiler that translates assembly code into binary machine code. The compiler supports various instructions and handles labels, variables, and immediate values.

## Assumptions

The compiler operates under the following assumptions:

1. **Label Type Instruction:** Only one label declaration per line is allowed. The colon (":") occurs only once in a line.

2. **MOV Instruction:** The `MOV` instruction is versatile and can be used with two types of operands:
   - `MOV register value`: Valid when the destination is a register.
   - `MOV reg1 reg2`: Valid when both operands are registers.

## Opcode and Register Mapping

The compiler uses the following opcodes and register mappings:

```python
op_code = {
    'add': '00000',
    'sub': '00001',
    'mov': {'00010', '00011'},  # B, C
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
    'hlt': '11010',
    'addf': '10000',
    'subf': '10001',
    'movf': '10010'
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
```

## Usage

1. **Input Format:**
   - The input assembly code should be provided via standard input (stdin).
   - Labels are declared with a colon (`:`) at the end of a line.
   - Variables are declared using the `var` keyword.

2. **Running the Compiler:**

   ```bash
   python compiler.py < input_code.txt
   ```

   Replace `input_code.txt` with the name of your input file.

## Error Handling

The compiler performs various error checks, including checking for undefined variables, label misuse, typos in instruction names, and more. If errors are detected, the compiler outputs detailed error messages.

## Example

```assembly
var X
mov R1 X
add R2 R1 R3
ld R4 X
hlt
```

This example code declares a variable `X`, moves its value to `R1`, adds the values in `R1` and `R3` and loads the value of `X` into `R4`, finally halting the program.

# Assembly Simulator

A simple assembly simulator that executes instructions and updates the register and memory accordingly.

## Instruction Set

### Operation Codes (op_code)
- **add:** '00000'
- **sub:** '00001'
- **movb:** '00010'
- **movc:** '00011'
- **ld:** '00100'
- **st:** '00101'
- **mul:** '00110'
- **div:** '00111'
- **rs:** '01000'
- **ls:** '01001'
- **xor:** '01010'
- **or:** '01011'
- **and:** '01100'
- **not:** '01101'
- **cmp:** '01110'
- **jmp:** '01111'
- **jlt:** '11100'
- **jgt:** '11101'
- **je:** '11111'
- **hlt:** '11010'

### Operation Types (op_type)
- **A:** add, sub, mul, xor, or, and
- **B:** movb, rs, ls
- **C:** movc, div, not, cmp
- **D:** ld, st
- **E:** jmp, jlt, jgt, je
- **F:** hlt

### Registers (reg)
- **R0:** '000'
- **R1:** '001'
- **R2:** '010'
- **R3:** '011'
- **R4:** '100'
- **R5:** '101'
- **R6:** '110'
- **FLAGS:** '111'

### Initial Register Values (initial_reg)
```python
{
    'R0': '0' * 16,
    'R1': '0' * 16,
    'R2': '0' * 16,
    'R3': '0' * 16,
    'R4': '0' * 16,
    'R5': '0' * 16,
    'R6': '0' * 16,
    'FLAGS': '0' * 16,
}
```

## Usage

1. Input your assembly code into the simulator.
2. Run the simulator to execute the instructions.
3. View the updated register and memory values after execution.

## Example

```python
# Example Assembly Code
ld 00000001 00000100
add 00000100 00000101 00000110
st 00000010 00000110
hlt
```

## Simulator Execution

```bash
$ python simulator.py
```


## License

This code is provided under the [MIT License](LICENSE).

