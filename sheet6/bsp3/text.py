
with open('hello.txt','r') as readfile , open('hello_out.txt','w') as write_file :
        for el in readfile:
        
            write_file.write("new" +str(el))

            write_file.write("old" + str(el))

with open('hello_out.txt','r') as write_file :
            print(write_file.read(),end='')



file_input =input('place your file')

with open(file_input, "r") as readfile , open(f'{file_input}.out.txt', "w") as write_file:
         for el in readfile:
         
                write_file.write("new" +str(el))

                write_file.write("old" + str(el))

with open('hello_out.txt','r') as write_file :
                print(write_file.read(),end='')