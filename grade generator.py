print("Exam Grade Calculator")
name=input("Name of the exam:")
mark=int(input("Max. Possible Score:"))
score=int(input("Your Score:"))
percentage=(score/mark)*100
percentage=round(percentage,2)
if percentage>=90:
  print("You got",percentage,"% which is a A+")
elif percentage>=80:
  print("You got",percentage,"% which is a A-")
elif percentage>=70:
  print("You got",percentage,"% which is a B")
elif percentage>=60:
  print("You got",percentage,"% which is a C")
elif percentage>=50:
  print("You got",percentage,"% which is a D")
elif percentage>=40:
  print("You got",percentage,"% which is a U")
else:
  print("you got failed")