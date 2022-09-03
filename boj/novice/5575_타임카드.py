# students = []
# a = list(map(int,input().split()))
# students.append(a)
# b = list(map(int,input().split()))
# students.append(b)
# c = list(map(int,input().split()))
# students.append(c)

# result = []
# for student in students:
#     start_time = student[0]*3600 + student[1]*60 + student[2]
#     end_time = student[3]*3600 + student[4]*60 + student[5]
#     work_time = end_time - start_time

#     wh = work_time // 3600
#     work_time %= 3600
#     wm = work_time // 60
#     ws = work_time % 60

#     result.append(wh)
#     result.append(wm)
#     result.append(ws)


# for i in range(len(result)):
#     if i%3 == 0 :
#         print()
#     print(result[i], end=' ')
    
ah1,am1,as1,ah2,am2,as2 = map(int,input().split())
bh1,bm1,bs1,bh2,bm2,bs2 = map(int,input().split())
ch1,cm1,cs1,ch2,cm2,cs2 = map(int,input().split())

#a
a_start_time = ah1*3600 + am1*60 + as1
a_end_time = ah2*3600 + am2*60 + as2
a_work_time = a_end_time - a_start_time

awh = a_work_time // 3600
a_work_time %= 3600
awm = a_work_time // 60
aws = a_work_time % 60

#b
b_start_time = bh1*3600 + bm1*60 + bs1
b_end_time = bh2*3600 + bm2*60 + bs2
b_work_time = b_end_time - b_start_time

bwh = b_work_time // 3600
b_work_time %= 3600
bwm = b_work_time // 60
bws = b_work_time % 60

#c
c_start_time = ch1*3600 + cm1*60 + cs1
c_end_time = ch2*3600 + cm2*60 + cs2
c_work_time = c_end_time - c_start_time

cwh = c_work_time // 3600
c_work_time %= 3600
cwm = c_work_time // 60
cws = c_work_time % 60

print(awh,awm,aws)
print(bwh,bwm,bws)
print(cwh,cwm,cws)

## answer
# for k in [0]*3:
#     a,b,c,d,e,f=[int(k)for k in input().split()]
#     t=(d-a)*3600+(e-b)*60+f-c
#     print(t//3600,t//60%60,t%60)