student_name=input("Enter your name and surname:")
score_input=input("Enter your exams scores separated by commas:")
exam_score= [round(float(x)) for x in score_input.split(",")]

total_score= sum(exam_score)
num_exam= len(exam_score)
average_score= total_score // num_exam

bonus_awarded=input("Has bonus been awareded (yes/no):").lower()=="yes"


if bonus_awarded:
      bonus = int(input("Enter the amount of bonus:"))
      average_score += bonus
      result=average_score
else:
    result=average_score


print(f"Processing result for {student_name}")
print(f"Outcome:{result}")



if average_score >=90:
    print( " Provisional Classification : 1st Excellent!")

elif average_score >=69:
    print( "Provisional Classification :2.1 Very Good!")
elif average_score >=59:
          print("Provisional Classification :2.2 Performance at a level showing the potential to achieve at least a lower second class honours degree!")
elif average_score >=49:
         print("Provisional Classification :3rd Pass, may not be sufficient for progression to an honours programme!")
elif average_score >=39:
       print("Provisional Classification :Marginal Fail!")
elif average_score>=29:
        print("Provisional Classification :Clear Fail!")
elif average_score>=19:
        print(" Provisional Classification :Clear Fail!")
elif average_score>=9:
        print("Provisional Classification Clear Fail!")
else:
        print("Enter some data")







#membership ,Checking if record exists 
check_score=int(input("Enter your score to check if exists in record:"))

if check_score in exam_score:
        print("Your score is in record:")
else:
        print("No record found!")


#identity operator
print("For admin olny:")
backup_scores=exam_score
if backup_scores is exam_score:
        print("Both are the same data")

#bitwise
print("Just to practice bitwise :)")
a=exam_score[0]
b=exam_score[1]

print(f"\nBitwise AND of first two scores: {a & b}")
print(f"Bitwise OR of first two scores: {a | b}")
print(f"Bitwise XOR of first two scores: {a ^ b}")


        
        


         




