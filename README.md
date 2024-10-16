# Nand2Tetris
Building a computer, using only nand gates.
My quest to learn computer architecture!
Below are my short notes. Please note my up-to-date learnings can be tracked on Twitter: https://x.com/shreybirmiwal/status/1832816031355580427


### Project 5: Comp Arch (part C) CPU:

We put together the PC, ALU and registers together. Control bits coming from instruction enable/disable inputs, outputs, and saving of outputs. This is getting really interesting and exciting!
![GZzhn9-WYAAoPU4](https://github.com/user-attachments/assets/7de2f567-8543-49e0-bfe9-5e20bae7e53a)


### Project 5: Comp Arch (part B)

First, let's make the memory unit.
We already created the individual chips - just need to combine  RAM16k, a Screen Map section, and a register for keyboard input.

We can use the same DMUX/MUX 'fanning out' method as earlier to achieve this:
![GZqMHfnXcA42SU-](https://github.com/user-attachments/assets/97d32587-99f0-4127-bed4-2d202370b4d7)



### Project 5: Computer Architecture (part A)

Now that we have sufficient prerequest chips, let's start planning and putting together the full computer architecture. See the attached picture for plan

![GZqLxHGXsAE4H4i](https://github.com/user-attachments/assets/45429e94-5c3c-4423-bf90-e623925126fa)


### Project 4: Machine Language

Instead of making an assembler first, I jumped to making machine language programs to understand where we are heading.

In assembly, wrote programs to make the screen black on key press, multiply numbers & flip variables. My Notes:
![GZD3-TkWcAAGZbB](https://github.com/user-attachments/assets/5ff03e4b-5d95-41fd-a5ef-0ee62a686a5a)


### Project 3: RAM memory 

Starting with flip flops and dmux/mux chips made previously, we created a bit that retained memory across time!

8 bits -> 1 register -> ram8 -> ram64 -> ram256 -> ram4k -> ram16k by scaling multiple previous chips 

Notes below:
![GX9--apXoAAljtG](https://github.com/user-attachments/assets/a3239680-3391-41ee-97e1-dad23098a697)


### Project 2: Arithmetic Logic Unit

Using the XOR and AND chips from p1, I created a half adder (bit1 + bit2 = sum, carry bit)

Then, using multiple half adders, created a full adder (bit1 + bit2 + carry bit = sum, carry bit)

Addition -> multiply, divide, subtract (full ALU!)
![GXKrHbvW4AAJUs0](https://github.com/user-attachments/assets/1c7c352e-311b-4935-b7e8-07547d5f12c5)



### Project 1: Logic Gates

I created elementary logic gates from the original NAND gate. Ei: NOT was created by NAND(input, input) and AND was created by NOT NAND.
Now, we had gates like XOR, AND, OR, DMUX, MUX16, etc ready for use in future chips!
