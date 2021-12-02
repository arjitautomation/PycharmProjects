def foo():
    print (5)

def bar():
    return 7

x = foo() 
y = bar()

print (x) 
# will show "None" because foo() does not return a value
print (y) 
# will show