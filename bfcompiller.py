from sys import argv

bf_file_name, prog_name, mem_size = argv[1:]

syntax = {
	'>':'i++;\n',
	'<':'i--;\n',
	'+':'arr[i]++;\n',
	'-':'arr[i]--;\n',
	'.':'putchar(arr[i]);\n',
	',':'arr[i] = getchar();\n',
	'[':'while(arr[i]){\n',
	']':'}\n',
	'\n':'\n',
	' ':'\n'}

tab = 1

head = f'''#include <stdio.h>
#include <string.h>
void main(){'{'}
    int i = 0;
    char arr[{mem_size}];
    memset(arr, 0, sizeof(arr));
'''

with open(bf_file_name, 'r') as bf_file, open(prog_name, 'w') as prog:
	prog.write(head)
	for char in bf_file.read().strip():
		if char == '[':
			tab += 1
		prog.write(tab * '\t' + syntax[char])
		if char == ']':
			tab -= 1
	prog.write('}\n')
