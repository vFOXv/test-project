# Преобразование типов данных

# int() - преобразование типа данных int
# float() - преобразование типа данных float
# str() - преобразование типа данных str
# bool() - преобразование типа данных bool

age = 25
height = 1.75
name = "John"
is_married = False
is_student = True

print(float(age))
print(int(height))
print(bool(name))
print(int(is_married))
print(float(is_married))
print(str(is_student))

# 0, "", None, [], (), {} - False
# все остальное - True
print(bool(0))
print(bool(""))
