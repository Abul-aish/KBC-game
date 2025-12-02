print("Welcome to KBC!")
questions=[
    ["What is the the capital of pakistan?","Lahore","Islamabad","karachi","Peshawar",2],
    ["What is factorial of 5?","110","100","120","130",3],
    ["How many alphabets are there in English language ?","20","26","24","22",2],
    ["Which planet is known as the Red Planet ?","Earth","Jupiter","Mars","Saturn",3],
    ["What is the largest ocean on Earth ?","Indian Ocean","Arctic Ocean","Atlantic Ocean","Pacific Ocean",4],
    ["What is the square root of 64 ?","Six","Ten","Eight","Four",3],
    ["Who is known as the father of computers ?","Alan Turing","Abulaish","Charles Babbage","Bill Gates",3],
    ["Who wrote 'Hamlet' ?","Charles Dickens","William Shakespears","Jane Austen","Leo Tolstoy",2],
    ["Which language is used to create Facebook ?","Python","C++","Java","Jupiter",2],
    ["Which company owns YouTube ?","Apple","Microsoft","Meta","Google",4],
    ["When is Windows 10 end of support by Microsoft ?","November-2025","October-2025","November-2024","October-2024",2],
    ["What does VPN protect ?","Ads","Speed","Viruses","User",2],
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1280000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    
    print(f"Question for Rs. {levels[i]}")
    print(question[0])
    print(f"1. {question[1]}           2. {question[2]}")
    print(f"3. {question[3]}           4.{question[4]}")
    reply=int(input("Enter your answer (1-4):"))
    if (reply==questions[i][5]):
        print(f"Correct answer! You won Rs.{levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==11):
            money=1280000
    else:
            print(f"Wrong answers!")
            break
print(f"The money you are taking home is Rs.{money}")
    
         