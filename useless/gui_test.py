import tkinter as wtk
import pymysql as mydb

session_number = 0

def btncmd():
    print("Clicked Button")
    
def searching_db(uid, upw) -> int:
    find_db = 'select count(*) from logset where uid = \'{myid}\' and upw = \'{mypw}\''.format(myid = uid, mypw = upw)
    
    cur.execute(find_db)
    table_elements = cur.fetchall()
    
    is_exist = -1
    
    for elem in table_elements:
        is_exist = elem[0]
        
    if(is_exist == 1):
        print("Login Success!")
    elif(is_exist == 0):
        print("Login Failed...")
    else:
        raise Exception("Error!")

    return is_exist
    
def inter_gui():
    mygui = wtk.Tk()
    mygui.title("My GUI")           # Window Title
    mygui.geometry("500x400")       # Size Setting
    mygui.resizable(False,False)    # Size Fixed
    
    # Multiple input
    # txt = wtk.Text(mygui, width = 10, height = 1)
    # txt.insert()
    # txt.pack()
    
    # One-Line Input
    ent = wtk.Entry(mygui, width = 15)
    ent.pack()
    ent.insert(0, 'Input Your ID')
    
    ent2 = wtk.Entry(mygui, width = 15)
    ent2.pack()
    ent2.insert(0, 'Input Your Password')
    
    def sss():
        global session_number
        
        logid = ent.get()
        logpw = ent2.get()
        
        session_number = searching_db(logid, logpw)
    
    btn1 = wtk.Button(mygui, text = 'Submit', command = sss)
    btn1.pack()
    
    # btn2 = wtk.Button(mygui, padx = 5, pady = 5, width = 5, height = 5, fg(font_color) = 'blue', bg(background_color) = 'yellow, text = 'button2')
    
    # photo = wtk.PhotoImage(file = [Photo Path])
    # btn3 = wtk.Button(mygui, image = photo)
    
    btn4 = wtk.Button(mygui, command = btncmd, text = "Click Button")
    btn4.pack()
    
    mygui.mainloop()
    
inter_gui()