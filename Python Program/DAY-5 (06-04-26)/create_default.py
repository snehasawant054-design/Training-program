class Demo:
    def _init_(self):
        print("I am Constructor :")

    def msg(self):
        print("Hello Class !")

obj1 = Demo()                                   
print(obj1)                                    

obj2 = Demo()                                   

obj1.msg()

# Output:
# <__main__.Demo object at 0x00000174EA42F110>
# Hello Class !
