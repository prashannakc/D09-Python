#file handling 
# f = open('start.txt', 'w')
# f.write("b=10") 
# f.close() 


#CA (without function)
def handle_error(message): 
    with open('error.txt', 'a') as f:
        f.write(str(message)+"\n")
        f.close()
try:
    print(10+"b")
except Exception as e:
    handle_error(e)


 


