from datetime import datetime 

class Log():
    def __init__(self, func):
        self.func = func
        self.date = datetime.now()
        with open("Log.txt", "a") as file:
            file.write("The Test {0} success At {1}\n".format(func.upper(), self.date))
            
class PrintTime():
    def __init__(self, func_string):
        self.func_string = func_string
        
        if func_string != "":
            time = datetime.now()
            print(func_string + " Test success -{}\n".format(time))