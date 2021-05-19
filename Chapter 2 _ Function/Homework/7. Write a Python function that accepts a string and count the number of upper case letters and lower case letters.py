def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0,"SPACE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        elif c.isspace():
           d["SPACE"]+=1
        else:
            pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
    print ("No. of Space                 : ", d["SPACE"])
s=input("Enter String:")
string_test(s)