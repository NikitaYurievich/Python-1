New_array = []
Final_array = []
Element = input(" Enter word. If you want end the array write 'stop' ")
while Element != "stop":
    New_array.append(Element)
    Element = input(" Enter word ")
for i in New_array:
    SymboLenght = len(i)
    if SymboLenght <= 3:
        Final_array.append(i)
print(Final_array)
