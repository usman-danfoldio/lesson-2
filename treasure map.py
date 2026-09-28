print("welcome to the Danfoldio's treasure map")
line1=["", "0","0"]
line2=["0", "0","0"]
line3=["0", "0","0"]
map= [line1, line2, line3]
print("Hiding your treasure! X marks the spot")
position=input("Where do you want to put the treasure?")
letter=position[0].lower()
abc=["a", "b", "c"]
letter_index=abc.index(letter)
number_index= int(position[1])-1
map[number_index][letter_index]="X"

print(f"{line1}\n{line2}\n{line3}")