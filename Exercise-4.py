sum=0;
for i in range(5):
    num = (input('Enter int '+ "#" +str(i+1) + ": "))
    #i faced difficulty at the start as my code was not running for 
    # negative integers then i came across lstrip on w3schools 
    # then applied it to get the desired output
    while num.lstrip("-").isdigit()==False:
        print("Invalid input. Please enter an int.")
        num = (input('Enter int '+ "#" +str(i+1) + ": "))
    if num.lstrip("-").isdigit()==True:
        sum = sum+int(num)
    
print("Your sum is " + str(sum))