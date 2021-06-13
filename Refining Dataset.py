import numpy as np
import pandas as pd 
from pandas import Series, DataFrame
from numpy.random import randn

df_left = DataFrame({'key':['X','X','Y','Z','Z'],
                     'data':range(5)})

df_right = DataFrame({'group_data':[10,30]},index=['X','Z'])

df_left_hr = DataFrame({'key1':['MB','MB','DL','DL','PU'],
                        'key2':[10,30,20,30,20],
                        'data_set':np.arange(5.)})

df_right_hr = DataFrame(np.arange(10).reshape(5,2),
                        index = [['PU','MB','MB','DL','PU'],
                        [20,30,10,10,10]],
                        columns = ['col1','col2'])

print(df_left)

print(df_right)

print(df_left_hr)

print(df_right_hr)

print(pd.merge(df_left_hr,df_right_hr,left_on=['key1','key2'],right_index= True))

df = pd.read_csv("DLD.csv")
females = pd.read_csv("Indian-Female-Names.csv")
males = pd.read_csv("Indian-Male-Names.csv")

training_df = df.loc[1:200,:].copy()

def namecorrection(string):
    s = ''
    for i in string:
        if i != '@':
            s += i
    return s

array = np.random.randint(1000,size=200)
data = []
for i in array:
    j = np.random.randint(2)
    if j == 0:
        name = males['name'][i]
    else:
        name = females['name'][i]
    if type(name) != float:
        if '@' in name:
            name = namecorrection(name)
        data.append(name)

ser1 = pd.Series(data=data, index=np.arange(200))
training_df['School'] = ser1
training_df.rename(columns={'School':'Name'},inplace=True)
print(training_df.head())

absents=[]
for i in range(200):
    absents.append(df2['Enrolled'][i] - df2['Present'][i])

df2['Absent'] = absents
del(df2['Released'])
del(df2['Date'])

#print(np.random.choice(np.arange(1,7),p=[0.1, 0.05, 0.05, 0.2, 0.4, 0.2]))

#S=[90,100] 0.1
#A=[76,89] 0.2
#B=[56,75] 0.3
#C=[40,55] 0.3
#D=[26,40] 0.05
#F=[0,25] 0.05

marks=[random.randrange(90,100),
       random.randrange(76,89),
       random.randrange(56,75),
       random.randrange(40,55),
       random.randrange(26,39),
       random.randrange(0,25)]

markrange_s=range(90,100)
markrange_a=range(76,90)
markrange_b=range(56,76)
markrange_c=range(40,56)
markrange_d=range(26,40)
markrange_e=range(0,26)

s_percentage=10
a_percentage=20
b_percentage=30
c_percentage=30
d_percentage=5
e_percentage=5

total_marks=[]

for k in range(200):
    marklist = []
    for i in range(6):
        if i > 0:
            if marklist[i-1] in markrange_s:
                s_percentage += 20
                a_percentage += 15
                b_percentage += 10
                c_percentage += 5
                d_percentage -= 1
                e_percentage -= 1        
            elif marklist[i-1] in markrange_a:
                s_percentage += 10
                a_percentage += 20
                b_percentage += 10
                c_percentage += 5
                d_percentage -= 1
                e_percentage -= 1
            elif marklist[i-1] in markrange_b:
                s_percentage += 5
                a_percentage += 10
                b_percentage += 20
                c_percentage += 10
                d_percentage += 5
                e_percentage -= 1
            elif marklist[i-1] in markrange_c:
                s_percentage -= 1
                a_percentage += 5
                b_percentage += 10
                c_percentage += 20
                d_percentage += 10
                e_percentage += 5
            elif marklist[i-1] in markrange_e:
                s_percentage -= 1
                a_percentage += 3
                b_percentage += 5
                c_percentage += 10
                d_percentage += 20
                e_percentage -= 10
            elif marklist[i-1] in markrange_e:
                s_percentage -= 1
                a_percentage -= 3
                b_percentage += 5
                c_percentage += 5
                d_percentage += 1
                e_percentage -= 1
            if s_percentage <= 0:
                s_percentage = 1
            if a_percentage <= 0:
                a_percentage = 1
            if b_percentage <= 0:
                b_percentage = 1
            if c_percentage <= 0:
                c_percentage = 1
            if d_percentage <= 0:
                d_percentage = 1
            if e_percentage <= 0:
                e_percentage = 1
            
            values = np.array([s_percentage,a_percentage,b_percentage,c_percentage,d_percentage,e_percentage])
            arr1 = values / values.sum()
            marklist.append(np.random.choice(marks,p=arr1))
        
        else:    
            marklist.append(np.random.choice(marks,p=[0.1,0.2,0.3,0.3,0.05,0.05]))
    total_marks.append(marklist)

grades_dict = {}
grade=''
subjects=['Subject_1_mark','Subject_2_mark','Subject_3_mark','Subject_4_mark','Subject_5_mark','Subject_6_mark']
subject_grades=['Subject_1_grade','Subject_2_grade','Subject_3_grade','Subject_4_grade','Subject_5_grade','Subject_6_grade']
for x in range(6):
    mark_list=[]
    grade_list=[]
    for y in range(200):
        mark = total_marks[y][x]
        if mark in markrange_s:
            grade = 'S' 
        elif mark in markrange_a:
            grade = 'A'
        elif mark in markrange_b:
            grade = 'B'
        elif mark in markrange_c:
            grade = 'C'
        elif mark in markrange_d:
            grade = 'D'
        elif mark in markrange_e:
            grade = 'E'   
        mark_list.append(mark)
        grade_list.append(grade)
    grades_dict[subjects[x]] = mark_list
    grades_dict[subject_grades[x]] = grade_list
df3 = pd.DataFrame(grades_dict)
print(df3)
result = pd.merge(df2, df3, left_index=True, right_index=True)

markrange_s=range(90,100)
markrange_a=range(76,90)
markrange_b=range(56,76)
markrange_c=range(40,56)
markrange_d=range(26,40)
markrange_e=range(0,26)

total_m_dict={}
total_marks = []
eligibility = []
att_pct=[]
for i in range(200):
    totalmarks = df2['Subject_1_mark'][i] + df2['Subject_2_mark'][i] + df2['Subject_3_mark'][i] + df2['Subject_4_mark'][i] + df2['Subject_5_mark'][i] + df2['Subject_6_mark'][i]
    attendance = (df2['Present'][i] * 100)/df2['Enrolled'][i]    
    ans = ''
    if (int(attendance) >= 75) and (int(totalmarks) >= 400):        
        ans = "Yes"
    elif (attendance >= 75.0) and (int(totalmarks) < 400):
        if totalmarks >= 400:   
            ans = 'Yes'
        else:
            ans = 'No'
    elif attendance < 75.0 and totalmarks >= 400:
        
        totalmarks -= 20 - attendance//10
        if totalmarks >= 400:
            ans = 'Yes'
        else:
            ans = 'No'
    else:
        
        ans = 'No'
    eligibility.append(ans)
    total_marks.append(totalmarks)
    att_pct.append(attendance)
total_m_dict['Total_marks'] = total_marks
total_m_dict['eligibility'] = eligibility
d3 = pd.DataFrame(total_m_dict)

final_grade = []
for j in d3['Total_marks']/6:
    if int(j) in markrange_s:
        final_grade.append('S')
    elif int(j) in markrange_a:
        final_grade.append('A')
    elif int(j) in markrange_b:
        final_grade.append('B')
    elif int(j) in markrange_c:
        final_grade.append('C')
    elif int(j) in markrange_d:
        final_grade.append('D')
    elif int(j) in markrange_e:
        final_grade.append('E')
d3['Final_grade'] = final_grade
result2 = pd.merge(df2, d3, left_index=True, right_index=True)
print(result2)
