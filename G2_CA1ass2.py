# A company decided to give bonus to employee according to following criteria
# Time period of services     Bonus

# more than 10 years           10%
# >=6 and <=10 years           8%
# less than 6 years            5%
# ask user for thier salary and years of services and print the net bonus amount

salary=int(input("Enter your salary::"))
year=int(input("Enter the year of service::"))

if(year<6):
    print("Your bonus amount is::",((salary*5)/100))
    print("Total salary now::",((salary*5)/100)+salary)
elif(year>=6 & year <=10):
    print("Your bonus amount is::",((salary*8)/100))
    print("Total salary now::",((salary*8)/100)+salary)
elif(year>10):
    print("Your bonus amount is::",((salary*10)/100))
    print("Total salary now::",((salary*10)/100)+salary)


    
    