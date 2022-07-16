# WAP to enter the marks of 10 students and display it.
marksheet = {}
for i in range(10):
    s_id = input('Enter student ID: ')
    marks = float(input('Enter student marks: '))
    marksheet[s_id] = marks

print('sid', ' '*5, 'marks')
for s_id, marks in marksheet.items():
    print(s_id, '-->', marks)