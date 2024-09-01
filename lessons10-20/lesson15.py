# Срезы строк


name = "John"

print(name[0])
print(name[1])
print(name[-2])


# [start:stop:step]
# start - начальная позиция (по умолчанию 0)
# stop - конечная позиция (по умолчанию -1)
# step - шаг (по умолчанию 1)

print(name[::])
print(name[2::])
print(name[:2:])
print(name[::2])
print(name[1:3:])
print(name[::-2])
