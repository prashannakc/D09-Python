
#CA - Student Result Analyzer
def analyze_result(student_name, maths_marks, science_marks, english_marks, attend_perc):
    avg_marks = (maths_marks+science_marks+english_marks)/3
    grade = ['A', 'B', 'C', 'D']
    if avg_marks>=80:
        i = 0
        gradee = grade[i]
    elif 60<=avg_marks<80:
        i = 1
        gradee = grade[i]
    elif 40<=avg_marks<60:
        i = 2
        gradee = grade[i]
    else:
        i = 3
        gradee = grade[i]
    if attend_perc<75:
        gradee = grade[i+1]
    result = {"student name": student_name, "average marks": avg_marks, "final grade": gradee}
    return result
print(analyze_result("Prashanna", 70, 80, 90, 69))

#g=9.8 is default - changeable
def force(m, g=9.8):
    f = m*g
    return f

#earth 
force(10)
force(20)
force(30)

#moon
force(10, 15)

def userinfo(fname, lname = "sharma"):
    return f"My name is {fname} {lname}"

print(userinfo("sudan"))
print(userinfo("Hari", "KC"))




    
