# Computer Organisation Project

Course: CSE112
Course Title: Computer Organisation

Palak Bhardwaj(2022344)
Suhani Kalyani(2022511)
Vanshika Pal(2022560)
Nandini Jain(2022316)


### Path To Run Assembler
 - CO-project -> CO_A_P1 -> Simple-Assembler -> Assembler.py


#### HOW TO EVALUATE

In terminal, go to automatedTesting directory and enter `./run``. A complete report sheet will be generated in the terminal

For Only Assembler
In terminal, go to automatedTesting directory and enter `./run --no-sim`. A complete report sheet will be generated in the terminal

#### To view all changes and history view Old_Assembler 

 ### ASSUMPTIONS:
  
  - Label type instruction: only 1 label declaration per line i.e, ":"occurs only once.
  
  - `Mov R1 FLAGS` is taken to be a valid command since FLAGS doesn't represent a variable but instead represents a valid register name , where 
  - MOV can be used with two types of instructions , type1- mov register value , mov reg1 reg2 , hence we have taken to be a valid name
  - Use of FLAG register:
    - `FLAGS` is a valid register name
    - `mov reg1 FLAGS` is the only valid  instruction involving FLAG register.





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

## License

This code is provided under the [MIT License](LICENSE).

