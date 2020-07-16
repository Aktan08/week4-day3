# Попросить пользователя ввести текст. В результате вывести процент букв в
# верхнем
# регистре (заглавные) и в нижнем регистре (прописные).

#ldskmlkdmcdsKKK

list_= input()
string_='dcascsa'
a=len(list(filter(lambda x: x.istitle(),list_)))
b=len(list(filter(lambda x: x.islower(),list_)))

print(a/(a+b)*100)
print(b/(a+b)*100)
