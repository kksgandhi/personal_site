types of assembly:

 - [[RISCV]]
 - [[MIPS]]

Programmers model for [[MIPS]]

32 bit (4 byte) registers (1 word)

add $r7, $r4, $r3 | r7 = r4 + r3

dollar sign implies it is a variable, no dollar sign is a constant

special registers: [[program counter]], stack pointer (points to end of stack frame)

memory is laid out in words as well

[[memory model]]

assembly: address, immediate
C       : pointer, constant

types of registers:

 - $r0: always 0
 - $at: assembler temporary, for expanding macros
 - $v0, $v1: return 
 - $ra where to return to
 - $ao-$a3, 4 args. Any more need to be on the stack
 - $s0-$s7, $t0-$t9 local variables

[[registers]] are the only variables you can access directly

# Load and Store

to get to the RAM

assembler takes symbols and makes a symbol table mapping symbols to addresses

array[index] is backwards in assembly, assembly has x($t1) which is t1[x / word size]

.word lets you define a symbol
.space allows you to ask for space

call frame is an array off the stack pointer

jump to address, 

beq lets you branch conditionally

jal: jump and link, jumps and sets the $ra for you to pc+word

calling multiple functions, you have to store the old $ra value to prevent $ra from getting overwritten by a jal

caller saved registers can be overwritten after a call, so if you're making a call, it's your responsibility to save them if you need them later.

callee saved registers are expected to be the same after a return, so if you want to change them, you better restore them before you exit

[[MARS]] assembly simulator
