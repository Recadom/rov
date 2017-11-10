#This is created to make or edit a file that a user might have for some interface/app. 
#It shall take parameter file and check if it is valid
import os.path
#                               """The start"""


class File_Name(object):

    def __init__(self, file, path):
        self.file = file
        self.path = path
        self.completeName = os.path.join(self.path,self.file)
		
    def create_file(self): #creates a text document
        file_1 = open(self.completeName + '.txt', 'w+')
        file_1.close()
	
    def add_data(self, data, tf): # add_data(data, True or False) True for every line. False for all data on single line.
        file_1 = open(self.completeName + '.txt', 'a')
        if tf == True: file_1.write(data + '\n')
        elif tf == False: file_1.write(data)
        file_1.close()
	
    def delete_data(self, data): #deletes data. If parameter = True, delete all!
        if data == True:  
            with open(self.completeName + '.txt', "w"):
                pass
        else:
            file_1 = open(self.completeName + '.txt', 'r')
            lines = [line.strip() for line in file_1]
            file_1.close()
            with open(self.completeName + '.txt', "w"):
                pass
            file_2 = open(self.completeName + '.txt', 'w') 
            for line in lines:
                if line != data: file_2.write(line + '\n')
            file_2.close()
            
    def delete_line(self, v):
        b = 0 #set variable for tracking lines in for loop
        info_1 = []
        lines_1 = []
        file_1 = open(self.completeName + '.txt', 'r')
       	for i in file_1:
            info_1.append(i)
            b+=1
            lines_1.append(b)
        file_1.close()
        with open(self.completeName + '.txt', "w"):
                pass
        file_1 = open(self.completeName + '.txt', 'w')
        for info, lines in zip(info_1, lines_1):
            if str(lines) != str(v):
                file_1.write(info)
        file_1.close()
    def all_data(self): #returns all data as list
        v = 2 #setting variable for use
        file_1 = open(self.completeName + '.txt', 'r')
        lines=[line.strip() for line in file_1]
        for i in lines:
            v+=1
        file_1.close()
        return lines[0:v]
                
    def line_data(self, line, line_2): # returns only one line 
        v = 2 #setting variable for use
        line -= 1
        file_1 = open(self.completeName + '.txt', 'r')
        lines= [line.strip() for line in file_1]
        file_1.close()
        return lines[int(line):int(line_2)]




#                           """TESTING AREA"""
if __name__ == "__main__":
    folder = os.path.dirname(__file__)
    user = File_Name('Tasks',folder)
    #user.add_data('Hi, my name is Dominik, welcome to the new creation!', True)
    #user.add_data('hola!', False)
    #user.delete_data('Hi, my name is Dominik, welcome to the new creation!')
    #user.delete_data(True)
    print (user.line_data(1,4))
    #user.delete_line(3)
    pass
