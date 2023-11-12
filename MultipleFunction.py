class multifunction():
    
    def subfields():
        subfield=["Machine Learning","Neural Networks","Vision","Robotics","Speach Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for field in subfield:
            print("\n",field)
            
            
    def OddEven():
        
        Num=int(input("Enter a Number: "))
        if (Num%2 == 0):
            print(Num,"is Even Number")
        else:
            print(Num,"is Odd Number")
            
            
    def Eligible():
        
        gender=input("your Gender: ")
        age=int(input("Your Age: "))
        if (gender=="Male"):
            if(age>=21):
                eligibility="ELIGIBLE"
            else:
                eligibility="NOT ELIGIBLE"
        elif (gender=="Female"):
            if(age>=18):
                eligibility="ELIGIBLE"
            else:
                eligibility="NOT ELIGIBLE"
            
        return eligibility    


    def Percentage():
        mark1 = int(input("Subject1 = "))
        mark2 = int(input("Subject2 = "))
        mark3 = int(input("Subject3 = "))
        mark4 = int(input("Subject4 = "))
        mark5 = int(input("Subject5 = "))
        Total = mark1+mark2+mark3+mark4+mark5
        print("Total : ",Total)
        Percentage = (Total/5)
        print("Percentage:",Percentage) 
          
     
    
    
    def triangle():
        height = int(input("Height :"))
        base = int(input("Breadth :"))
        print("Area Formula: (Height*Breadth)/2")
        area = (height*base)/2
        print("Area of Triagle :",area)
        side1 = int(input("Height1 :"))
        side2 = int(input("Height2 :"))
        side3 = int(input("Braedth :")) 
        print("Perimeter Formula: Height1+height2+Braedth")
        perimeter = side1+side2+side3
        print("Perimeter of Triangle: ",perimeter)
        
                    
        