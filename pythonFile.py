# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution
#student ID:w1998771
#Data: 21/04/2023
Continue="y"
Output_list=[]
ALL_input_list=[]
Student_IDS=[]
TXTfile_list=[]
marks_list=[0,20,40,60,80,100,120]
Bigset=set(marks_list)
choose= True
Data_base=dict()

def Count_1():
    from collections import Counter
    Count=Counter(Output_list)
    C_total=Count.total()
    Count1=dict(Count)
    for new_s, new_val in Count1.items():
        print(new_s, new_val , ":", new_val*"*")
    print(C_total,"outcomes in total.\n")
def STUDENT_AND_TEACHER():
            output=""
            display_list=["Please enter your credits at PASS: " ,"Please enter your credit at DEFER: ","Please enter your credit at FAIL:  "]
            List_lenbgth3=len(display_list)
            S_ID=True
            marks=True
            while S_ID== True:
                student_id=input("Enter student id :").lower()
                if (len(student_id))!=8:
                    print("Enter correct sutdent id ")
                else:
                    for elements in range (1,len(student_id)):
                        if (student_id[0])!="w":
                            print("Enter correct sutdent id ")
                            break
                        elif (student_id[0])=="w":
                            try:
                               int(student_id[elements])                           
                               S_ID=False
                            except:
                                print("Enter correct sutdent id.. \n ")
                                break
                    Student_IDS.append(student_id)         
            while marks==True:
                input_list=[]
                check=False
                for k in range (0,List_lenbgth3):
                    num1=input(display_list[k])
                    try:
                        int(num1)
                        input_list.append(int(num1))
                        check=True      
                    except :
                        print("Please enter your correct credits.. \n")
                        check=False
                        break
                while check==True:
                    Marks=set(input_list).issubset(Bigset)#https://stackoverflow.com/questions/3847386/how-to-test-if-a-list-contains-another-list-as-a-contiguous-subsequence
                    if Marks== False:
                        print("Please enter your correct credits.. \n")
                        check=False
                    else:        
                        Sum=sum(input_list)
                        if Sum != 120:
                            print("Please enter your correct credits.. \n")
                            check=False
                            break
                        else:
                            check=False
                            marks=False                
            count=0
            ALL_input_list.append(input_list)
            def MAIN(count,List_length1,List_length2):
                if input_list[2] >= 80:
                    output="Exclude"   
                else:
                    while count<=(List_length1-3):
                        for i in range(0,List_length2-2):
                            if input_list[count]==marks_list[i]:
                                output="Do not progress – module retriever"
                                break
                            elif input_list[count]==120:
                                output="Progress"   
                            else :
                                input_list[count]==100
                                output="Progress (module trailer)"                                
                        count=count+1
                Output_list.append(output)
                print("\n",output)
                print("-"*80)
            count=0
            List_length1=len(input_list)
            List_length2=len(marks_list)
            MAIN(count,List_length1,List_length2)
            All_list=[Output_list,input_list]

print("PROGRESSION OUTCOME".center(80))
while choose==True:
    category=input("please enter whether you are a student(1) or a teacher(2) to begin:")
    try:
        category=int(category)
        choose= False 
    except:
        print("please enter correct number")
        choose==True

if category==1:
    STUDENT_AND_TEACHER()
else:
    while Continue=="y":
        STUDENT_AND_TEACHER()
        Continue="q"
        print("\nWould you like to enter another set of data?")
        Continue=input("\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
    print("_"*35,"Histogram","_"*35,"\n")
    Count_1()

    Round=0
    List_length3=len(Output_list)
    List_length4=len(ALL_input_list)
    print("_"*80)
    print("PART_2")
    for o in range(0,List_length3): 
        while Round<=(List_length4-1):
            print(Output_list[Round],"-" ,ALL_input_list[o])
            TXT_elements= Output_list[Round],"-" ," ".join(str(x) for x in ALL_input_list[o])#PART_3  
            with open('CW.txt', 'a') as file:
                line = ''.join (str(x)for x in TXT_elements)
                file.write(line+ "\n")
                TXTfile_list.append(line)
            break
        Round=Round+1
    print("_"*80)
    print("PART_4")
    #PART_3  
    for key in Student_IDS:
        for value in TXTfile_list:
            Data_base[key] = value
            TXTfile_list.remove(value)
            break
        for Data_s, TXT_val in Data_base.items():
            print(Data_s,":", TXT_val,end=" | " )

