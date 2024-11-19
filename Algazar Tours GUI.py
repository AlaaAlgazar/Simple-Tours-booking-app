from tkinter import *
from tkinter import ttk,messagebox
import datetime,time,sqlite3

# ********************************
# creating data base files for clients
tourists_database_file=sqlite3.connect("Algazar_tourists_GUI.db")
cr=tourists_database_file.cursor()
cr.execute("create table if not exists tourists_data (name text, age text, country text, address text, job text, phone_number text, tour text, password text)")
cr.execute("create table if not exists tours_data (name text,place text,days int,date date,ticket_price'$' int,max_tourists int)")
# cr.execute("delete from tours_data")
# cr.execute("insert into tours_data values('Alex 101' ,'Alex libirary',1,'3/1/2024',50,35)")
# cr.execute("insert into tours_data values('Luxor 112' ,'Luxor Templete',3,'7/1/2024',150,70)")
# cr.execute("insert into tours_data values('Paris 103' ,'Eiffel Tower',5,'12/1/2024',600,50)")
# cr.execute("insert into tours_data values('London 111' ,'Tower of London',6,'16/1/2024',450,40)")
# cr.execute("insert into tours_data values('Berlin 107' ,'Brandenburg Bate',7,'22/1/2024',550,55)")

# ********************************
# cr.execute("delete from tourists_data")
# cr.execute("insert into tourists_data values ('khaled ali', '20', 'Egypt', 'Tanta - kafr el_zayat','doctor Std.', '0124268592' ,'Cairo tower','noway')")
# main program form
main_window = Tk()
main_window.configure(bg="#999")
wid=main_window.winfo_screenwidth()
hei=main_window.winfo_screenheight()
main_window.geometry(f"{wid}x{hei}")
# *******************
hello_label=Label(main_window,text="Hello to your company",font=("Arial",25,"bold"),bg="#999",fg="#ca1",bd=5)
hello_label.grid(row=0,column=0)
main_window.title("Algazar Tours")
# ******************
main_fg_label_color="#147"
main_fg_entry_color="#277"
main_label_font_size=16
main_entry_font_size=14
main_frame_font_size=12
# ********************
main_frame=Frame(main_window)
main_frame.grid(row=1,column=0,sticky="e")
# Client data frame
mypadx=20
mypady=10
first_labeled_frame=LabelFrame(main_frame,text="Client Data",font=("Arial",main_frame_font_size,"bold"),fg="brown",bd=5)
first_labeled_frame.grid(row=0,column=0,padx=20,pady=10,sticky="news")

# *******************************
registering_name=StringVar()
name_label=Label(first_labeled_frame,text="Full name",fg=main_fg_label_color,font=("Arial",main_label_font_size,"bold"))
name_label.grid(row=0,column=0,padx=mypadx)

name_entry=Entry(first_labeled_frame,textvariable=registering_name,fg=main_fg_entry_color,font=("Arial",main_entry_font_size,"bold"))
name_entry.grid(row=1,column=0,padx=mypadx,pady=5)
# *******************************
registering_age=StringVar(value="")
age_label=Label(first_labeled_frame,text="Age",fg=main_fg_label_color,font=("Arial",main_label_font_size,"bold"))
age_label.grid(row=0,column=1,padx=mypadx)

age_entry=Entry(first_labeled_frame,textvariable=registering_age,fg=main_fg_entry_color,font=("Arial",main_entry_font_size,"bold"))
age_entry.grid(row=1,column=1,padx=mypadx,pady=5)
# *******************************
registering_country=StringVar()
country_label=Label(first_labeled_frame,text="Country",fg=main_fg_label_color,font=("Arial",main_label_font_size,"bold"))
country_label.grid(row=0,column=2,padx=mypadx)

country_entry=Entry(first_labeled_frame,textvariable=registering_country,fg=main_fg_entry_color,font=("Arial",main_entry_font_size,"bold"))
country_entry.grid(row=1,column=2,padx=mypadx)

# *******************************
registering_address=StringVar()
my_column_span=10
address_label=Label(first_labeled_frame,text="Address",fg=main_fg_label_color,font=("Arial",main_label_font_size,"bold"))
address_label.grid(row=2,column=0,padx=mypadx)

address_entry=Entry(first_labeled_frame,textvariable=registering_address,fg=main_fg_entry_color,font=("Arial",main_entry_font_size,"bold"))
address_entry.grid(row=3,column=0,padx=mypadx)
# *******************************
registering_jop=StringVar()
job_label=Label(first_labeled_frame,text="Job",fg=main_fg_label_color,font=("Arial",main_label_font_size,"bold"))
job_label.grid(row=2,column=1,padx=mypadx)

job_entry=Entry(first_labeled_frame,textvariable=registering_jop,fg=main_fg_entry_color,font=("Arial",main_entry_font_size,"bold"))
job_entry.grid(row=3,column=1,padx=mypadx)
# *****************************
registering_phone_num=StringVar(value="")
Phone_num_label=Label(first_labeled_frame,text="Phone number",fg=main_fg_label_color,font=("Arial",main_label_font_size,"bold"))
Phone_num_label.grid(row=2,column=2,padx=mypadx)

Phone_num_entry=Entry(first_labeled_frame,textvariable=registering_phone_num,fg=main_fg_entry_color,font=("Arial",main_entry_font_size,"bold"))
Phone_num_entry.grid(row=3,column=2,padx=10)
# *****************************
# saving_data_button=Button(first_labeled_frame,text="Save data",fg="blue",bg="#fd4",font=("Arial",20,"bold"))
# saving_data_button.grid(row=4,column=1,padx=20,pady=10,sticky="snew")
# ********************************
# creating second labeled frame
second_labeled_frame=LabelFrame(main_frame,text="Registering way",bd=5,height=3,font=("Arial",main_frame_font_size,"bold"),fg="brown")
second_labeled_frame.grid(row=2,column=0,padx=20,pady=3,sticky="snew")
# *******************
def check_if_admin():
    # print(checking_var.get())
    pass

checking_var=StringVar()
checking_var.set(value="no")
is_admin_check=Checkbutton(second_labeled_frame,command=check_if_admin,variable=checking_var,text="Are you an admin ?                                 "
                                  ,onvalue="yes",offvalue="no",fg=main_fg_entry_color,font=("Arial",main_label_font_size,"bold"))#,state=go_next_1.get()
is_admin_check.grid(row=0,column=0,padx=20,pady=2)

def complete_as_admin():
    # print(complete_var.get())
    pass

complete_var=StringVar()
complete_var.set(value="no")
complete_check=Checkbutton(second_labeled_frame,command=complete_as_admin,variable=complete_var,text="Do you want to complete as an admin ?"
                                  ,onvalue="yes",offvalue="no",fg=main_fg_entry_color,font=("Arial",main_label_font_size,"bold"))#,state=go_next_1.get()
complete_check.grid(row=1,column=0,pady=2)

# *************************************
# the third frame will have many possibilities for the client and the admin
third_labeled_frame=LabelFrame(main_frame,fg="brown",bd=5,font=("Arial",main_frame_font_size,"bold"))
third_labeled_frame.configure(text="Tours Booking")
third_labeled_frame.grid(row=3,column=0,padx=20,pady=10)

if checking_var.get() =="yes" and complete_var.get() == "yes":
    third_labeled_frame.configure(text="Admins Registeration")
    pass
    # I will complete this later
else:
    f0=LabelFrame(third_labeled_frame,fg="brown",bd=5,font=("Arial",main_entry_font_size,"bold"))
    f0.grid(row=0,column=0,padx=10,pady=10)
    choice_tours_label=Label(f0,text="Choose a tour",fg=main_fg_label_color,font=("Arial",main_label_font_size,"bold"))
    choice_tours_label.grid(row=0,column=0)

    # ********************
    # ******************
    # ********************
    cr.execute("select name from tours_data")
    tours_names_tuple=cr.fetchall()
    tours_names_list=[]
    for element in tours_names_tuple:
        tours_names_list.append(element[0])
    # print(tours_names_list)
    # ******************
    cr.execute("select place from tours_data")
    tours_places_tuple=cr.fetchall()
    tours_places_list=[]
    for element in tours_places_tuple:
        tours_places_list.append(element[0])
    # print(tours_places_list)
    # ******************
    cr.execute("select days from tours_data")
    tours_days_tuple=cr.fetchall()
    tours_days_list=[]
    for element in tours_days_tuple:
        tours_days_list.append(element[0])
    # print(tours_days_list)
    # ******************
    cr.execute("select date from tours_data")
    tours_date_tuple=cr.fetchall()
    tours_date_list=[]
    for element in tours_date_tuple:
        tours_date_list.append(element[0])
    # print(tours_date_list)
    # ******************
    cr.execute("select ticket_price from tours_data")
    tours_ticket_price_tuple=cr.fetchall()
    tours_ticket_price_list=[]
    for element in tours_ticket_price_tuple:
        tours_ticket_price_list.append(element[0])
    # print(tours_ticket_price_list)
    # ********************
    cr.execute("select max_tourists from tours_data")
    tours_max_tourists_tuple=cr.fetchall()
    tours_max_tourists_list=[]
    for element in tours_max_tourists_tuple:
        tours_max_tourists_list.append(element[0])
    # print(tours_max_tourists_list)
    # ******************
    # ********************
    # i will change this value later using sqlite3
    tour_place=StringVar()
    tour_days=StringVar()
    tour_date=StringVar()
    ticket_price=StringVar()
    max_tourists_num=StringVar()
    # ************************
    # **************************              المشكلة
    def show_data_func(event):
        # print(tours_names_list)
        # print(tours_places_list)
        # print(tours_days_list)
        # print(tours_date_list)
        # print(tours_ticket_price_list)
        # print(tours_max_tourists_list)

        tour_place.set(value=tours_places_list[tours_names_list.index(chosed_tour.get())])
        # print (tour_place.get())
        tour_days.set(value=tours_days_list[tours_names_list.index(chosed_tour.get())])
        # print (tour_days.get())
        tour_date.set(value=tours_date_list[tours_names_list.index(chosed_tour.get())])
        # print (tour_date.get())
        ticket_price.set(value=tours_ticket_price_list[tours_names_list.index(chosed_tour.get())])
        # print (ticket_price.get())
        max_tourists_num.set(value=tours_max_tourists_list[tours_names_list.index(chosed_tour.get())])
        # print (max_tourists_num.get())
    # ************************
    # **************************

    chosed_tour=StringVar()
    existing_tours_combo=ttk.Combobox(f0,textvariable=chosed_tour,state="readonly",foreground=main_fg_entry_color,
                                      font=("Arial",main_entry_font_size,"bold"),width=18,values=tours_names_list)

    existing_tours_combo.grid(row=1,column=0,pady=10,padx=20)
    existing_tours_combo.bind ("<<ComboboxSelected>>",show_data_func)
    # ******************
    initial_value = "First, choose a trip"
    # print(tours_names_list.index('Alex 101'))
    # print(tours_places_list[tours_names_list.index('Alex 101')])
    tour_place.set(value=initial_value)

    f1=LabelFrame(third_labeled_frame,fg="brown",bd=5,font=("Arial",main_entry_font_size,"bold"))
    f1.grid(row=0,column=1,padx=10,pady=10,sticky="news")
    tour_place_label=Label(f1,text="Tour place",fg=main_fg_label_color,font=("Arial",main_label_font_size,"bold"))
    tour_place_label.grid(row=0,column=0)
    tour_place_entry=Label(f1,textvariable=tour_place,fg=main_fg_entry_color,width=20,font=("Arial",main_entry_font_size,"bold"))#,state=go_next_1.get()
    tour_place_entry.grid(row=1,column=0,padx=20)
    # ******************
    f2=LabelFrame(third_labeled_frame,fg="brown",bd=5,font=("Arial",main_entry_font_size,"bold"))
    f2.grid(row=0,column=2,padx=10,pady=10,sticky="news")
    tour_days.set(value=initial_value)
    tour_days_label=Label(f2,text="Tour days",fg=main_fg_label_color,font=("Arial",main_label_font_size,"bold"))
    tour_days_label.grid(row=0,column=0)
    tour_days_entry=Label(f2,textvariable=tour_days,fg=main_fg_entry_color,font=("Arial",main_entry_font_size,"bold"))#,state=go_next_1.get()
    tour_days_entry.grid(row=1,column=0,padx=20)

    # ********************
    f3=LabelFrame(third_labeled_frame,fg="brown",bd=5,font=("Arial",main_entry_font_size,"bold"))
    f3.grid(row=1,column=1,padx=10,pady=10,sticky="news")

    ticket_price.set(value=initial_value)
    ticket_price_label=Label(f3,text="ticket price",fg=main_fg_label_color,font=("Arial",main_label_font_size,"bold"))
    ticket_price_label.grid(row=0,column=0)
    ticket_price_entry=Label(f3,textvariable=ticket_price,fg=main_fg_entry_color,font=("Arial",main_entry_font_size,"bold"))#,state=go_next_1.get()
    ticket_price_entry.grid(row=1,column=0,padx=20,pady=10)
    # ******************
    f4=LabelFrame(third_labeled_frame,fg="brown",bd=5,font=("Arial",main_entry_font_size,"bold"))
    f4.grid(row=1,column=2,padx=10,pady=10,sticky="news")
    max_tourists_num.set(value=initial_value)
    max_tourists_label=Label(f4,text="max tourists",fg=main_fg_label_color,font=("Arial",main_label_font_size,"bold"))
    max_tourists_label.grid(row=0,column=0)
    max_tourists_entry=Label(f4,textvariable=max_tourists_num,fg=main_fg_entry_color,font=("Arial",18,"bold"))#,state=go_next_1.get()
    max_tourists_entry.grid(row=1,column=0,pady=10,sticky="news")
    # ******************
    tour_date.set(value=initial_value)
    f5=LabelFrame(third_labeled_frame,fg="brown",bd=5,font=("Arial",18,"bold"))
    f5.grid(row=1,column=0,padx=10,pady=10,sticky="news")
    tour_date_label=Label(f5,text="Tour date",fg=main_fg_label_color,font=("Arial",main_label_font_size,"bold"))
    tour_date_label.grid(row=0,column=0)
    tour_date_entry=Label(f5,textvariable=tour_date,fg=main_fg_entry_color,font=("Arial",main_entry_font_size,"bold"))#,state=go_next_1.get()
    tour_date_entry.grid(row=1,column=0,pady=10)
    # ****************** 
    entered_password_var=StringVar()
    Password_label=Label(third_labeled_frame,text="Set a Password",fg=main_fg_label_color,font=("Arial",main_label_font_size,"bold"))
    Password_label.grid(row=2,column=0,padx=20)
    entered_password=Entry(third_labeled_frame,fg=main_fg_entry_color,textvariable=entered_password_var,font=("Arial",main_entry_font_size,"bold"),width=20)#,show="*")
    entered_password.grid(row=2,column=1,padx=20,pady=10)
    # ********************
    # entered_password_var=StringVar()
    def is_show():
        pass

    #     if show_pass_var.get()=="yes":
    #         entered_password_text=Text(third_labeled_frame,fg="green",font=("Arial",18,"bold"),width=20,height=1)
    #         entered_password_text.insert("1.0",entered_password_var.get())
    #         entered_password_text.grid(row=3,column=2,padx=20,pady=10)
    #     else:
    #         entered_password=Entry(third_labeled_frame,fg="green",textvariable=entered_password_var,font=("Arial",18,"bold"),width=20,show="*")
    #         entered_password.grid(row=3,column=2,padx=20,pady=10)
    #         entered_password.configure(show="*")

    show_pass_var=StringVar(value="no")
    show_password_check=Checkbutton(third_labeled_frame,fg="#826",text="Show Password",font=("Arial",main_label_font_size,"bold"),variable=show_pass_var
                                    ,onvalue="yes",offvalue="no",command=is_show)
    show_password_check.grid(row=2,column=2)
    # *****************
    # *******************
    # ******************
    # creating the forth labeled frame
    forth_labeled_frame=LabelFrame(main_frame,text="Information about the tour",width=40,fg="brown",bd=5,font=("Arial",main_frame_font_size,"bold"))
    forth_labeled_frame.grid(row=0,column=1,sticky="news",padx=20,pady=10)

    more_information_text=Text(forth_labeled_frame,fg=main_fg_entry_color,font=("Arial",main_entry_font_size,"bold"),height=7,width=48)
    more_information_text.grid(row=0,column=0,padx=20,pady=10,sticky="news")

    # ****************
    # creating the fifth frame
    def get_policies_func():
        pass

    fifth_labeled_frame=LabelFrame(main_frame,text="Policies & Conditions",width=60,bd=5,fg="brown",font=("Arial",main_frame_font_size,"bold"))
    fifth_labeled_frame.grid(row=2,column=1,padx=20,pady=10,sticky="news")

    conditions_label=Label(fifth_labeled_frame,text="       If you don't know the policies,please    ",fg=main_fg_label_color,font=("Arial",main_label_font_size,"bold"))
    conditions_label.grid(row=0,column=0)
    conditions_button=Button(fifth_labeled_frame,width=25,bg="#fa3",text="Click here",bd=5,fg="#148",font=("Arial",3+main_label_font_size,"bold"),command=get_policies_func)
    conditions_button.grid(row=1,column=0,padx=100,columnspan=50,pady=10)


    # ******************
    # creating the sixth labeled frame
    sixth_labeled_frame=LabelFrame(main_frame,text="Accept policies",width=60,bd=5,fg="brown",font=("Arial",main_frame_font_size,"bold"))
    sixth_labeled_frame.grid(row=3,column=1,padx=20,pady=10,sticky="new")

    def policy_check_func():
        # print(initial_check_value.get())
        pass
    policy_check_var=StringVar()
    policy_check_var.set(value="no")
    button_policy_check=Checkbutton(sixth_labeled_frame,variable=policy_check_var,font=("Arial",15,"bold"),text="I read and accept the policies.   "
                                    ,onvalue="yes",offvalue="no",fg=main_fg_entry_color,command=policy_check_func)
    button_policy_check.grid(row=0,column=0,sticky="ews",padx=20)
    # ***********************
    def data_check_func():
        # print(data_check_var.get())
        pass
    data_check_var=StringVar()
    data_check_var.set(value="no")
    button_policy_check=Checkbutton(sixth_labeled_frame,variable=data_check_var,font=("Arial",15,"bold"),text="I am responsible for the truth of\nthe entered data."
                                    ,onvalue="yes",offvalue="no",fg=main_fg_entry_color,command=data_check_func)
    button_policy_check.grid(row=1,column=0,padx=20)

    # ************************


    # *******************
    


    def saving_func():
        tourists_database_file=sqlite3.connect("Algazar_tourists_GUI.db")
        cr=tourists_database_file.cursor()
                
        # # getting data

        tourist_name=registering_name.get().title()
        tourist_age=registering_age.get()
        tourist_country=registering_country.get().title()
        tourist_address=registering_address.get().title()
        tourist_jop=registering_jop.get().title()
        tourist_phone_number=registering_phone_num.get()
        tourist_tour=chosed_tour.get().title()
        tourist_password=entered_password.get()
        list_of_data=[tourist_name,tourist_age,tourist_country,tourist_address,tourist_jop,tourist_phone_number,tourist_tour,tourist_password]
        if tourist_password.find("'") != -1:
            print(tourist_password)
            print("found")
            messagebox.showerror(title="Invalid password",message="Your password mustn't have the character \" ' \".")
        elif all(list_of_data):
            cr.execute(f"insert into tourists_data values ('{tourist_name}','{tourist_age}','{tourist_country}','{tourist_address}','{tourist_jop}','{tourist_phone_number}','{tourist_tour}','{tourist_password}')")
            messagebox.showerror(title="Saving data",message="Your trip is saved.")
        else:
            messagebox.showerror(title="empty cell",message="You must enter full data.")

        # print(tourist_name)
        # print(tourist_age)
        # print(tourist_country)
        # print(tourist_address)
        # print(tourist_jop)
        # print(tourist_phone_number)
        # print(tourist_tour)
        # print(tourist_password)

        # cr.execute("delete from tourists_data")
        tourists_database_file.commit()
        tourists_database_file.close()



    # creating the seventh labeled frame
    # seventh_labeled_frame=LabelFrame(main_frame,text="Revision & Submit",bd=5,fg="brown",font=("Arial",18,"bold"))
    # seventh_labeled_frame.grid(row=3,column=1,padx=20,pady=10,sticky="news")

    # show_data_button=Button(seventh_labeled_frame,width=40,bg="#364",text="Show tour data",bd=5,fg="#cd4",font=("Arial",3+main_label_font_size,"bold"),height=2,command=show_data_func)
    # show_data_button.grid(row=0,column=0,padx=20,pady=20,sticky="news")

    ensure_button=Button(main_frame,width=25,bg="#235",text="Submit",bd=5,fg="#fa2",font=("Arial",3+main_label_font_size,"bold"),height=2,command=saving_func)
    ensure_button.grid(row=3,column=1,padx=20,pady=20,sticky="s")





tourists_database_file.commit()
tourists_database_file.close()
if __name__ =="__main__":
    main_window.mainloop()