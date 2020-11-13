def mod_checker(x, mod=0):
    return lambda y: y % x == mod


mod_3 = mod_checker(3)

print(mod_3(3))
print(mod_3(4))