l = input("Write a word of your choice: ")
for i in l:
    if i == "A" or i == "a":
        print("A is found in",l)
        break
    else:
        print("A is not found")