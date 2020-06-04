echo "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>." > example.bf
python3 bfcompiller.py example.bf example.c 30000
gcc example.c -o example.elf
./example.elf