


# with open('test.txt','r') as my_file:
#     data =  my_file.read()
    
    
# print(data)


with open('test.txt', mode = 'r+') as my_file:
    res = my_file.write("DONE")
    print(res) 