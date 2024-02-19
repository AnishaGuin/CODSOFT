#importing modules
import tkinter as tk                   
from tkinter import messagebox                 
from tkinter import ttk          
import sqlite3 as sql                  
#defining function to add in the list    
def task_add():  
    task_str = task_field.get()   
    if len(task_str) == 0:   
        messagebox.showinfo( 'Eror: No entry')  
    else:  
        tasks.append(task_str)   
        cursor_t.execute('insert into tasks values (?)', (task_str ,))   
        list_update()  
        task_field.delete(0, 'end')  
#function to upudate the list 
def list_update():   
    clear_list()   
    for task in tasks:  
        task_listbox.insert('end', task)  
  
# function to delete a task from list  
def delete():  
    try: 
        the_value = task_listbox.get(task_listbox.curselection())   
        if the_value in tasks:  
            tasks.remove(the_value)  
            list_update()  
            cursor_t.execute('delete from tasks where title = ?', (the_value,))  
    except:    
        messagebox.showinfo('Error', 'Select a sinngle task')        
    
# function to clear the list  
def clear_list():  
    task_listbox.delete(0, 'end')  
  
# function to close the application  
def close():  
    print(tasks)   
    guiWindow.destroy()  
  
# function to retrieve data from the database  
def retrieve_database():  
    while(len(tasks) != 0):  
        tasks.pop()  
    for row in cursor_t.execute('select title from tasks'):  
        tasks.append(row[0])  
    
if __name__ == "__main__":  
    guiWindow = tk.Tk()  
    guiWindow.title("To-Do List")  
    guiWindow.geometry("500x450+750+250")
    guiWindow.resizable(0, 0)   
    guiWindow.configure(bg = "#f7dc6f")  
   
    the_connection = sql.connect('listOfTasks.db')   
    cursor_t = the_connection.cursor()  
    cursor_t.execute('create table if not exists tasks (title text)')  
  
    # defining an empty list  
    tasks = []  
      
    # defining frames 
    header = tk.Frame(guiWindow, bg = "#7fb3d5")  
    functions = tk.Frame(guiWindow, bg = "#7fb3d5")  
    listbox= tk.Frame(guiWindow, bg = "#7fb3d5")  
  
    #place the frames in the application  
    header.pack(fill = "both")  
    functions.pack(side = "left", expand = True, fill = "both")  
    listbox.pack(side = "right", expand = True, fill = "both")  
      
    # defining a label using the ttk.Label() widget  
    header_label = ttk.Label(  
        header,  
        text = "To-Do List",  
        font = ("Old Century", "30"),  
        background = "#FAEBD7",  
        foreground = "#8B4513"  
    )  
    # using the pack() method to place the label in the application  
    header_label.pack(padx = 40, pady = 40)  
  
    # defining another label using the ttk.Label() widget  
    task_label = ttk.Label(  
        functions,  
        text = "Enter your Task:",  
        font = ("Times New Roman", "12", "bold"),  
        background = "#dc7633",  
        foreground = "#eaeded"  
    )   
    task_label.place(x = 40, y = 40)  
      
    task_field = ttk.Entry(  
        functions,  
        font = ("Times New Roman", "12"),  
        width = 20,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )  
    task_field.place(x = 30, y = 80)  
  
    button_1 = ttk.Button(  
        functions,  
        text = "Add",  
        width = 25,  
        command = task_add  
    )  
    button_2 = ttk.Button(  
        functions,  
        text = "Delete",  
        width = 25,  
        command = delete  
    )  
    button_3 = ttk.Button(  
        functions,  
        text = "Exit",  
        width = 25,  
        command = close  
    )    
    button_1.place(x = 30, y = 120)  
    button_2.place(x = 30, y = 160)  
    button_3.place(x = 30, y = 240)  
    
    task_listbox = tk.Listbox(  
        listbox,  
        width = 26,  
        height = 13,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#CD853F",  
        selectforeground = "#FFFFFF"  
    )  
    task_listbox.place(x = 10, y = 20)  
  
    # calling some functions  
    retrieve_database()  
    list_update()  
    guiWindow.mainloop()  
    the_connection.commit()  
    cursor_t.close()
