class multipleFunctions():
    # Create a class and function, and list out the items in the list
    def Subfields():
        print("Sub-fields in AI are: ")
        list = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        for ls in list:
            print(ls)    
# Create a function that checks whether the given number is Odd or Even
    def OddEven():
        num = int(input("Enter your number: "))
        if(num % 2 == 0):
            print(num, " is Even number")
        else:
            print(num, " is Odd number")
            
# Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
    def Elegible():
        gender =input("Enter your Gender: ")
        age =int(input("Enter your Age: "))    
        if(gender == "Male"):
            if(age <= 20):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
        elif(gender == "Female"):
            if(age <= 18):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
        else:
            print("Invalid entry")

# calculate the percentage of your 10th mark
    def percentage():
            sub1 = int(input("Enter subject1 mark :"))
            sub2 = int(input("Enter subject2 mark :"))
            sub3 = int(input("Enter subject3 mark :"))
            sub4 = int(input("Enter subject4 mark :"))
            sub5 = int(input("Enter subject5 mark :"))
            total = sub1 + sub2 + sub3 + sub4 + sub5
            print("Total : ", total)
            percentage = (total/500)*100
            print("Percentage :", percentage)
        
#print area and perimeter of triangle using class and functions
    def triangle():
            height = int(input("Enter Height :"))
            breadth = int(input("Enter Breadth :"))
            areaFormula = (height*breadth)/2
            print("Area of Triangle: ", areaFormula)
            height1 = int(input("Enter Height1 :"))
            height2 = int(input("Enter Height2 :"))
            breadth1 = int(input("Enter Breadth1 :"))
            formula = height1 + height2 + breadth1
            print("Perimeter of Triangle :",formula)