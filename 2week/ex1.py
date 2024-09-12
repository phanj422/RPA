import pandas as pd
#col_names = ['과목번호', '과목명', '강의실', '시간수']
#list1 = list([['C1', '인공지능개론', 'R1', 3], ['C2', '웃음치료', 'R2', 2], ['C3', '경영학', 'R3',3], ['C4', '3D디자인', 'R4', 4], ['C5', '스포츠경영', 'R2', 2], ['C6', '예술의 세계', 'R3', 1]])
#df = pd.DataFrame(list1, columns=col_names)
#print(df)
data = {
    '과목번호' : ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'],
    '과목명' : ['인공지능개론', '웃음치료', '경영학', '3D디자인', '스포츠경영', '예술의 세계'],
    '시간수' : [3, 2, 3, 4, 2, 1]
}
df = pd.DataFrame(data)
print(df, end='\n\n')
sr_no = df.loc[2]
print(sr_no, end='\n\n')
cell_name = df.loc[2]['과목명']
print(cell_name)
df.to_csv('fle.csv', index=False)