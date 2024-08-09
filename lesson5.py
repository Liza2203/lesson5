#1
immutable_var=(1, 22, False, 'hello')
print(immutable_var)
#2
print(immutable_var.replace(1, 3))
print(immutable_var[2]=1)
#заменить элемнты в картеже нельзя, потому что он неизменяемый

#3
mutable_list=[1, 3, True, 'good']
mutable_list[1]=1
print(mutable_list)