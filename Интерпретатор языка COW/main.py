import numpy as np
import re

def file_read(name):
     file = open(name, 'r').read()
     str = re.sub(r'\n', r' ', file).split(' ')
     return str

def get_obj(name):
     arr = []
     obj = {}
     index = 0
     for i in file_read(name):
          if i == 'MOO':
               arr.append(index)
          if i == 'moo':
               obj[index]=arr[len(arr)-1]
               obj[arr.pop()]=index
          index+=1
     return obj

def result(name):
     result = np.zeros(1000)
     index = 0
     i = 0
     str = file_read(name)
     while(i != len(str)):
          match str[i]:
               case 'MoO':
                    result[index] += 1
               case 'MOo':
                    result[index] -= 1
               case 'mOO':
                    result[index] = i
               case 'moO':
                    index += 1
               case 'mOo':
                    index -= 1
               case 'OOM':
                    print(int(result[index]),end='')
               case 'oom':
                    result[index] = input()
               case 'Moo':
                    if str[index] != 0:
                         print(chr(int(result[index])), end=" ")
                    else:
                         input("Введите свое значение")
               case 'OOO':
                    str[index] = 0
               case 'moo':
                    i = get_obj(name)[i]-1
               case 'MOO':
                    if result[index] == 0:
                         i = get_obj(name)[i]
          if str[i] == '':
               pass
          else:
               i += 1
               continue
          i += 1


result("fib.cow")
result("hello.cow")