                                         UPGRADED ISA:
Includes 5 additional opcodes:
                            - Swaps reg1 reg2: swaps value stored in both registers
                            - Incr reg1      : Increments value stored in register, in case current value is 127 it updates to 0.
                            - Decr reg1      : Decrements value stored in register, in case current value is 0 it updates to 127.
                            - Clear reg 1    : Clears value stored in reg1, value updates to 0.
                            - Set $i         : Sets FLAG reg bit at ith index. #(0<=i>=11)
Uses:
    * Incr and Decr can be used for iterating within a loop or as a circular buffer.
    * Clear and Set can be used to reset a flag or to initial variables in nested loops.

Sample test case:
mov R1 $0
mov R2 $3
incr R1
incr R2
decr R3
swap R3 R1

set R5
hlt