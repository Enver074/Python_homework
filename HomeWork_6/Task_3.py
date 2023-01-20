# Задача 32:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def pow_a_b(a,b,res):
    if b==1:
        return res
    return pow_a_b(a, b-1, res*a)

a = int(input())
b = int(input())
res = a
print(pow_a_b(a,b,res))