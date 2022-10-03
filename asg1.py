def maxMarks(k):
    maxNo = 0
    for i in k:
        if i > maxNo:
            maxNo = i
    return maxNo

def sumOfMarks(r):
    sum = 0
    for i in r:
        if i == 'a':
            pass
        else:
            sum +=i
    return sum



def MinMarks(k):
    minNo = 10000000
    r = []
    for i in k:
        if i == -1:
            pass
        else:
            r.append(i)

    for i in r:
        if i < minNo:
            minNo = i
    return minNo


def highFreq(k):
    max = 0
    res = k[0]
    for i in k:
        freq = k.count(i)
        if freq > max:
            max = freq
            res = i
    return res

def mostRepeated(k):
    most = 0
    for i in k:
        for j in range(len(k)):
            if k[j] == i:
                most = i
    return most


def absentStudent(k):
    count = 0
    for i in k:
        if i == 'a':
            count += 1
    return count


def cleanedList(k):
    r = []
    for i in k:
        if i == '':
            r.append("a")
        else:
            r.append(i)
    return  r

def sumList(k):
    r = []
    for i in k:
        if i == '':
            pass
        else:
            i = int(i)
            r.append(((i)))
    return  r





studentList = []


absent = 0
k = int(input("How many students' data do you want to enter : "))



student = 1
for i in range(k):
    a = input(f"Enter mark of the student {student} : ")

    studentList.append(a)
    student += 1


sumMarks = sumOfMarks(sumList(studentList))
mean = (sumMarks + absent)/len(studentList)
minimum = MinMarks(sumList(studentList))
maximum = maxMarks(sumList(studentList))
mode = highFreq(sumList(studentList))
most = mostRepeated(sumList(studentList))
absent = absentStudent(cleanedList(studentList))
data = cleanedList(studentList)






print(f"Marks of students = {data}")
print(f"Maximum marks of student is : {maximum}")
print(f"Minimum marks of student is : {minimum}")
print(f"Mean marks of student is : {mean}")

print(f"The marks most repeated is : {most}")
print(f"Number of absent student is : {absent}")










