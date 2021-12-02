letter='''
Dear <|NAME|>,
Greetings from Nautanki Saala films, We are happy to tell you about 
You are selected to work at Nautanki Saala Films!!
Congratulations once again, See you soon

Have a nice Day

Date: <|DATE|>

Thanks and Regards,
Arjit Srivastava
'''
name = raw_input("Enter your Name\n")
date = raw_input("Enter the Date\n")

letter = letter.replace("<|NAME|>",name);
letter = letter.replace("<|DATE|>",date);

print(letter);
