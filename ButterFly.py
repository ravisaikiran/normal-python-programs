n=input()#butterfly function
i=len(n)-1
carry=0
total=0
while i>0:
    numtoadd=10-(int(n[i])+carry)
    total=total+numtoadd
    carry=1
    i-=1
total=total+9
print(total)
#removing trailing zeroes at end
'''29953->29954 29955 29956 29957 29958 29959(7)
2996->2997 2998 2999(4)
3->4 5 6 7 8 9 1 2(9)'''
