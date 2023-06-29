name = input("Enter your Name: ")
class1 = input("Enter your Class: ")
section = input("Enter your Section: ")
rollNo = input("Enter your Roll No: ")
teacherName = input("Enter your Teacher's Name: ")
reason = input("Enter the reason for leave: ")--


letter = f"""
\n\n
Date: 23-02-2023

To,
mr/ms. {teacherName},
X.Y.Z. School,

Dear Sir/Ma'am,

Subject: Application for leave

I am {name}, a student of {class1} class, {section} section and my Roll no. is {rollNo}. I want to bring to your kind attention that due to {reason}, I will be unable to come to school on 24-02-2023. So please grant me leave for one day.

Thank you.

Yours faithfully,
{name}"""

print(letter)
