
name=input("enter name")
email=input("enter add")
mobile=input("entermobile")
city=input("enter city")

if len(name)>1:
    if"@"in email and len(email)>11:
        if len(mobile)==10 and mobile.isnumeric():
            if city in['lucknow','delhi','noida']:
                print("data galat hai")
            else:
                print("sorry")
        else:
            print("galat hai")
    else:
        print("galat")
else:
    print('enetr correct name')
