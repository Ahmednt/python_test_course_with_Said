var_a = 6
var_b = 6

#if var_a == var_b:
if (var_a == var_b) and (var_a != var_b):
    print(f' {var_a} is eaqul to  {var_b}')
elif ((var_a != var_b) and (var_a > var_b)):
    print(f'{var_a} is greater than {var_b}')
elif ((var_a != var_b) and (var_a < var_b)):
    print(f'{var_a} is less  than {var_b}')
else:
    print(f' {var_a} is  eaqul to  {var_b}')

my_list = ['F','T','A','S','K']
my_list[2]='G'
print(my_list[0:2])
my_list.append('W')
my_list.append('T')
print(my_list)
#my_list.remove('T')
my_list.pop(-7)
print(my_list)