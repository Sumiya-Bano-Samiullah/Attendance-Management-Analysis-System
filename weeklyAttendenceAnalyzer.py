import numpy as np

section_A=np.array([[1,1,1,1,1],[1,1,1,1,0],[1,1,1,0,0],[1,1,0,0,0],[1,0,0,0,0]])
section_B=np.array([[1,0,0,0,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[1,1,0,0,1]])
section_C=np.array([[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1],[1,1,1,1,0],[1,1,1,0,0]])

#joining data
attendence=np.vstack((section_A,section_B,section_C))

total_days=np.size(attendence[0])
print(total_days)

#calculaing attendence
total=[]
avg=[] 
status=[]
for i in attendence:
    total.append(np.sum(i))
    avg.append((np.average(i))*100)

total_present_days=np.array(total)
attendence_per=np.array(avg)

for i in attendence_per:
    if(i<75.0):
        status.append("NOT ELIGIBLE")
    else:
        status.append("ELIGIBLE")

final_status=np.array(status)

print("Attendence Sheet")
print()
print("Roll_no        Days Present          Percentage                  Status")
for i in range(len(attendence)):
    print(i+1,"                 ",total_present_days[i],"                 ",attendence_per[i],"                 ",status[i])

#highest and lowes positions

print("highest 3 and lowest 3 attendents")
uiq=np.unique(total_present_days)[::-1]
if np.all(uiq==total_days):
    print("All students have 100 percent attendence no highest no lowest")
elif(np.all(uiq==0)):
    print("All students have 0 percent attendence no highest no lowest")
else:
    print("Highest three")
    print("Roll_no    Attendence")
    uiqr=uiq[0:3:1]  #top 3
    high_3=np.argsort(-total_present_days) #high --> low indexes
    high_sort=np.sort(total_present_days)[::-1] #sort array from high to low
    for i in range(len(high_sort)):
        for j in range(len(uiqr)):
            if(high_sort[i]==uiqr[j]):
                print(high_3[i]+1,"            ",high_sort[i])
    if(total_days==5):
        uiql=uiq[-2:][::-1]
        print("lowest two")
    else:
        uiql=uiq[-3:][::-1]
        print("lowest three")
    print("Roll_no    Attendence")
    for i in range(len(high_sort)):
        for j in range(len(uiql)):
            if(high_sort[i]==uiql[j]):
                print(high_3[i]+1,"            ",high_sort[i])


#highest attendence  per section
sec_att=[]
section=np.split(attendence,3,axis=0)
for i in section:
    sec_att.append(np.average(i))

att=np.array(sec_att)

if np.all(att==att[0]):
    result=0
    flag=False
else:
    result=np.max(att)
    result_idx=np.argmax(att)
    flag=True

print()
print("Section with highest average attendence")
if(flag==False):
    print("No section with highest average attendence all are same\n")
else:
    print("Section",result_idx+1,"has get the highest average attendennce of",result,"\n")




#analysis per day

#section A
print("Section A")
dayA=[]
A=np.transpose(section_A)

for i in A:
    dayA.append(np.sum(i))

dayAarr=np.array(dayA)
uiqA=np.unique(dayAarr)
if np.all(uiqA==uiqA[0]):
    print("All days have same no of absent students",total_days-uiqA[0])
else:
    minnimumA=np.min(uiqA)
    print("Day_no    Total absents")
    for i in range(len(dayAarr)):
        if(dayAarr[i]==minnimumA):
            print(i+1,"        ",total_days-minnimumA)

#section B
print("Section B")
dayB=[]
B=np.transpose(section_B)

for i in B:
    dayB.append(np.sum(i))

dayBarr=np.array(dayB)
print(dayBarr)
uiqB=np.unique(dayBarr)
if np.all(uiqB==uiqB[0]):
    print("All days have same no of absent students",total_days-uiqB[0])
else:
    minnimumB=np.min(uiqB)
    print("Day_no    Total absents")
    for i in range(len(dayBarr)):
        if(dayBarr[i]==minnimumB):
            print(i+1,"        ",total_days-minnimumB)


#section C
print("Section C")
dayC=[]
C=np.transpose(section_C)

for i in C:
    dayC.append(np.sum(i))

dayCarr=np.array(dayC)
uiqC=np.unique(dayCarr)
if np.all(uiqC==uiqC[0]):
    print("All days have same no of absent students",total_days-uiqC[0])
else:
    minnimumC=np.min(uiqC)
    print("Day_no    Total absents")
    for i in range(len(dayCarr)):
        if(dayCarr[i]==minnimumC):
            print(i+1,"        ",total_days-minnimumC)










    









    