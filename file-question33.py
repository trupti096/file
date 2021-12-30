banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
a=open("file-question3.txt","w")
i=0
while i<len(banks_list):
    a.write (banks_list[i])
    a.write("\n")
    i=i+1
    print(a)
