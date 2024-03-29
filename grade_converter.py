import tkinter as tk
 
 
# creating a new tkinter window
def main():

    master = tk.Tk()

    master.title("GRADECONVERTER")

    master.geometry("700x250") 
    
    
    # declaring objects for entering data

    object1 = tk.Entry(master)

    object2 = tk.Entry(master)

    object3 = tk.Entry(master)

    object4 = tk.Entry(master)

    object5 = tk.Entry(master)

    object6 = tk.Entry(master)

    object7 = tk.Entry(master)
    
    
    def display(subject_list):

        # subject = [name, sub-credit, grade]
        # Variable to store total marks
        total = 0
        
        for subject in subject_list:

            total_credits = get_credits( subject[2], subject[1])
            tk.Label(master, text =total_credits).grid(row=3, column=4)
            total += total_credits 

            tk.Label(master, text ="40").grid(row=4, column=4)

            total += 40

        if object5.get() == "B":

            tk.Label(master, text ="36").grid(row=4, column=4)

            total += 36

        if object5.get() == "C":

            tk.Label(master, text ="32").grid(row=4, column=4)

            total += 32

        if object5.get() == "D":

            tk.Label(master, text ="28").grid(row=4, column=4)

            total += 28

        if object5.get() == "P":

            tk.Label(master, text ="28").grid(row=4, column=4)

            total += 24

        if object5.get() == "F":

            tk.Label(master, text ="0").grid(row=4, column=4)

            total += 0

        if object5.get() == "A":

            tk.Label(master, text ="30").grid(row=5, column=4)

            total += 30

        if object6.get() == "B":

            tk.Label(master, text ="27").grid(row=5, column=4)

            total += 27

        if object6.get() == "C":

            tk.Label(master, text ="24").grid(row=5, column=4)

            total += 24

        if object6.get() == "D":

            tk.Label(master, text ="21").grid(row=5, column=4)

            total += 21

        if object6.get() == "P":

            tk.Label(master, text ="28").grid(row=5, column=4)

            total += 24

        if object6.get() == "F":

            tk.Label(master, text ="0").grid(row=5, column=4)

            total += 0

        if object7.get() == "A":

            tk.Label(master, text ="40").grid(row=6, column=4)

            total += 40

        if object7.get() == "B":

            tk.Label(master, text ="36").grid(row=6, column=4)

            total += 36

        if object7.get() == "C":

            tk.Label(master, text ="32").grid(row=6, column=4)

            total += 32

        if object7.get() == "D":

            tk.Label(master, text ="28").grid(row=6, column=4)

            total += 28

        if object7.get() == "P":

            tk.Label(master, text ="28").grid(row=6, column=4)

            total += 24

        if object7.get() == "F":

            tk.Label(master, text ="0").grid(row=6, column=4)

            total += 0
            
        # to display total credits

            tk.Label(master, text=str(total)).grid(row=7, column=4) 
        # to display SGPA

        tk.Label(master, text=str(total/15)).grid(row=8, column=4) 

    
    # label to enter name

    tk.Label(master, text="Name").grid(row=0, column=0)
    
    # label for BYUI ID number

    tk.Label(master, text="BYUI ID").grid(row=0, column=3)
    
    # label for PATHWAY IB Number

    tk.Label(master, text="PATHWAY ID").grid(row=1, column=0) 
    
    # labels for serial number

    tk.Label(master, text="Serial.No").grid(row=2, column=0) 

    tk.Label(master, text="1").grid(row=3, column=0)

    tk.Label(master, text="2").grid(row=4, column=0)

    tk.Label(master, text="3").grid(row=5, column=0)

    tk.Label(master, text="4").grid(row=6, column=0)
    
    
    # labels for subject codes

    tk.Label(master, text="Course").grid(row=2, column=1) 

    tk.Label(master, text="CSE 110").grid(row=3, column=1)

    tk.Label(master, text="CSE 111").grid(row=4, column=1)

    tk.Label(master, text="MA 101").grid(row=5, column=1)

    tk.Label(master, text="HUM 110").grid(row=6, column=1)

    

        
    # label for grades

    tk.Label(master, text="Grade").grid(row=2, column=2) 

    object4.grid(row=3, column=2)

    object5.grid(row=4, column=2)

    object6.grid(row=5, column=2)

    object7.grid(row=6, column=2)

    
    
    # labels for subject credits

    tk.Label(master, text="Sub Credit").grid(row=2, column=3) 

    tk.Label(master, text="2").grid(row=3, column=3)

    tk.Label(master, text="2").grid(row=4, column=3)

    tk.Label(master, text="3").grid(row=5, column=3)

    tk.Label(master, text="3").grid(row=6, column=3)

    

    tk.Label(master, text="Credit obtained").grid(row=2, column=4) 

    
    # taking entries of name, BYU-I, pathway ID'S respectively

    object1=tk.Entry(master) 

    object2=tk.Entry(master)

    object3=tk.Entry(master)

    
    # organizing them in the grid

    object1.grid(row=0, column=1)

    object2.grid(row=0, column=4)

    object3.grid(row=1, column=1)

    
    # button to display all the calculated credit scores and sgpa

    button1=tk.Button(master, text="submit", bg="red", command=display)

    button1.grid(row=8, column=1)

    # button2=tk.Button(master, text="Clear", bg="blue" command=delete)

    # button2.grid(row=8 column=2)
    tk.Label(master, text="Total credit").grid(row=7, column=3)

    tk.Label(master, text="SGPA").grid(row=8, column=3)


    # def clear():
    #     """Clear all the inputs and outputs."""
    #     object1.delete(0, tk.END)
    #     object2.delete(0, tk.END)
    #     object3.delete(0, tk.END)
    #     object4.delete(0, tk.END)
    #     object5.delete(0, tk.END)
    #     object6.delete(0, tk.END)
    #     object7.delete(0, tk.END)
    #     tk.Label.config(text="")
    #     # lbl_fast.config(text="")
    #     tk.Label.focus()


    master.mainloop()

def get_credits(grade, subject_credits):


    if grade == "A":
        credits = 10 * subject_credits
    elif grade == "B":
        credits = 9 * subject_credits
    elif grade == "C":
        credits = 8 * subject_credits
    elif grade == "D":
        credits = 7 * subject_credits
    elif grade == "P":
        credits = 6 * subject_credits
    else:
        credits = 0
    
    return credits
    



if __name__ == "__main__":
    main()
