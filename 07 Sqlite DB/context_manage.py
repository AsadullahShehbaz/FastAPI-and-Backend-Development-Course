def gen_table():
    table = [5,10,15,20,25]
    for n in table:
        yield n 

gen = gen_table()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))