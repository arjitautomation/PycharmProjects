letter='''

Dear <|NAME|>,
You are selected
<|DATE|>

'''
name = raw_input("Enter your Name\n")
date = raw_input("Enter the Date\n")

letter = letter.replace("<|NAME|>",name);
letter = letter.replace("<|DATE|>",date);

print(letter);
