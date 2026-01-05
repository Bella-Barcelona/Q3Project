from pyscript import display, document

def GET_GRADES(e):
    F_Name = str(document.getElementById("First_Name").value) #getting all that we need in the html page thru get element by id
    L_Name = str(document.getElementById("Last_Name").value)
    Sci_Grade = float(document.getElementById("Science").value)
    Math_Grade = float(document.getElementById("Math").value)
    Eng_Grade = float(document.getElementById("English").value)
    Flp_Grade = float(document.getElementById("Filipino").value)
    ICT_Grade = float(document.getElementById("ICT").value)
    PE_Grade = float(document.getElementById("PE").value)

    units = (5,3,2,1) #using tuples to identify the ynits per subject better

    F_AVG = (Sci_Grade * 5 + Math_Grade * 5 + Eng_Grade * 5 + Flp_Grade * 3 + ICT_Grade * 2 + PE_Grade * 1)/21 #finding the weighed average for all the grades through adding them then dividing by the number of items

    subj = ["Science", "Math", "English", "Filipino", "ICT", "PE"] # a list so we can navigate through the subject names easier

    Summary = f"""{subj[0]}: {Sci_Grade:.0f} 
    {subj[1]}: {Math_Grade:.0f}
    {subj[2]}: {Eng_Grade:.0f}
    {subj[3]}: {Flp_Grade:.0f}
    {subj[4]}: {ICT_Grade:.0f}
    {subj[5]}: {PE_Grade:.0f}
    """ #f funcions allows us to print variables/ display, three qoutations means multiline, .0f meaning to round off at 0th place

    display(f"Name: {F_Name}, {L_Name}", target = "student_info")
    display(Summary, target="summary")
    display(f"Your final average is: {F_AVG:.2f}", target="f_ave") #displaying all the info