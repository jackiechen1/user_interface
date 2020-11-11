#!/usr/bin/env python
# coding: utf-8

# 

# In[1]:


!chmod 755 ee.sh
!chmod 755 available.sh

#run as ipython user_interface.py
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import os
import pathlib

#set this path to the same path as the notebook(main workspace)
full_path = os.getcwd()
window = Tk()
window.geometry('1000x800')
window.title("Welcome to Data Visualization app")


# In[2]:


from tkinter.ttk import *
add_data_list = Combobox(window)
# the data list will add to the program

#input path and find the dataset(s6a02 for example)
def find_dataset(path):
    import os
    from os import listdir
    from os.path import isfile, join
    data_list=[]
    file = os.listdir(path)
    for x in file:
        if len(x)==5:
            data_list.append(x)
    #this function adds all string with length 5 
    #so some irrelavant string like "support" may also include in the list 
    
    add_data_list['values']= data_list
    add_data_list.current(1) #set the selected item
    add_data_list.grid(column=0, row=4)  


# In[3]:


path = full_path
data_list=[]#avaiable data list
from tkinter import filedialog 
# Function for opening the  
# file explorer window 
current_path = Label(window,text = "current path: "+path,font=("Arial Bold", 12))
def browseFiles(): 
    global path
    path = filedialog.askdirectory() 
    get_ipython().system('cd {path}')
    print("user input path: ")
    print(path)
    current_path = Label(window,text = "current path: "+path,font=("Arial Bold", 12))
    find_dataset(path)

label_file_explorer = Label(window,  
                            text = "File Explorer using Tkinter"
                            ) 
   
       
button_explore = Button(window,  
                        text = "Browse Files", 
                        command = browseFiles)  
label_file_explorer.grid(column = 0, row = 0) 

button_explore.grid(column = 0, row = 1) 
current_path.grid(column=0,row=2)


# In[4]:


#basic label and setup for data path
lbl = Label(window, text="Data Visualization User Interface 1.0", font=("Arial Bold", 12))
lbl.grid(column=1, row=0)


# In[5]:


dataset_list = Label(window,text="add new data set",font=("Arial Bold", 12))
dataset_list.grid(column=0,row=3)


# In[6]:


#here are three functions used for read/write/delete index in the file"data_list.txt"
#datalist file has following format:
#each line contain five character
get_ipython().system('touch data_list.txt')#create a list if it is the first time using it'
def readindex():
    global full_path
    change_path = full_path
    os.chdir(change_path)
    dataindex_list = open("data_list.txt","r")
    saved_list=[]
    saved_list1=[]
    for line in dataindex_list:
        saved_list.append(line)
    for x in saved_list:
        y = x.replace('\n','')
        if(len(y)==5):
            saved_list1.append(y)
    dataindex_list.close()
    #print(saved_list1)
    return saved_list1
def writeindex(data_name):#add_data_list
    global full_path
    change_path = full_path
    os.chdir(change_path)
    dataindex_list = open("data_list.txt","r")
    final_string = dataindex_list.read()+data_name+'\n'
    f = open("data_list.txt","w")
    f.write(final_string)
    f.close()
def deleteindex(data_name):
    global full_path
    change_path = full_path
    os.chdir(change_path)
    dataindex_list = open("data_list.txt","r")
    final_string = dataindex_list.read()
    #print(final_string)
    temp = data_name+'\n'
    final_string = final_string.replace(temp,'')
    final_string.strip()
    f = open("data_list.txt","w")
    f.write(final_string)
    f.close()


# In[7]:


label05 = Label(window,text = "Saved data:",font=("Arial Bold", 12))
label05.grid(column=0,row = 5)
save_data_list = Combobox(window)#saved data combobox(also in the datalist file)
save_data_list['values']= readindex()
save_data_list.current() #set the selected item
save_data_list.grid(column=0, row=6) 
label07 = Label(window,text = "Action:",font=("Arial Bold", 12))
label07.grid(column=0,row = 7)
data_list_action = Combobox(window)
data_list_action['values']= ['use','add','delete']
data_list_action.current(1) #set the selected item
data_list_action.grid(column=0, row=8) 


# In[ ]:


#given path and five character, traverse the dirctory and return 
#all availiable data index intervel
def find_intervel(path,dataname):
    import os
    from os import listdir
    from os.path import isfile, join
    file = os.listdir(path)
    prefix = dataname+"-"
    count = 0
    for i in file:
        i = i.replace(prefix,"")
        i = i.replace("-000","")
        file[count] = i
        count+=1
    count = 0

    for i in range(len(file)):
        try:
            file[i] = int(file[i])
        except:
            file[i] = -1
            
    count = 0
    file.sort()
    counting = 0
    for i in range(len(file)):
        if file[i]==-1:
            counting+=1       
    file = file[counting:len(file)]
    #print(file)
    test1 = file
    #After this loop, all the 

    

    count=1
    list1 =[]
    if file:
        list1 = [file[0]]

    for i in file:
        if count == len(file):
            list1.append(file[count-1])
            break
        if file[count] != file[count-1]+1:
            list1.append(file[count-1])
            list1.append(file[count])
        count+=1
    return [test1,list1]
        


# In[ ]:


#these three functions read/write/delete from "cvr.txt" file
#cvr.txt contain saved cvr operations
#format: e6a02-50-BE-rotation-up-60
#five character + dataindex + field + operation + direction + degree
def readcvr():
    get_ipython().system('touch cvr.txt')
    dataindex_list = open("cvr.txt","r")
    saved_list=[]
    saved_list1=[]
    for line in dataindex_list:
        saved_list.append(line)
    for x in saved_list:
        y = x.replace('\n','')
        saved_list1.append(y)
    dataindex_list.close()
    #print(saved_list1)
    return saved_list1
def writecvr(data_name):
    dataindex_list = open("cvr.txt","r")
    final_string = dataindex_list.read()+data_name+'\n'
    f = open("cvr.txt","w")
    f.write(final_string)
    f.close()
def deletecvr(data_name):
    dataindex_list = open("cvr.txt","r")
    final_string = dataindex_list.read()
    #print(final_string)
    dataindex_list.close()
    data_name = data_name+'\n'
    new_string = final_string.replace(data_name,'')
    print(new_string)
    new_string.strip()
    f = open("cvr.txt","w")
    f.write(new_string)
    f.close()
    

label022 = Label(window,text = "Add new file(input new index)",font=("Arial Bold", 12))
label022.grid(column=0,row = 22)
label028 = Label(window,text = "Action:",font=("Arial Bold", 12))
label028.grid(column=0,row = 28)
cvr_list_action = Combobox(window)
cvr_list_action['values']= ['create','open','delete']
cvr_list_action.current(0) #set the selected item
cvr_list_action.grid(column=0, row=29) 

cvr_save_list = Combobox(window,width=30)#list of saved cvr folder
cvr_save_list['values']= readcvr()
cvr_save_list.current() #set the selected item
cvr_save_list.grid(column=0, row=21) 


new_cvr_data_index = Combobox(window)#new dataindex if want to create a cvr file
new_cvr_data_index.current() #set the selected item
new_cvr_data_index.grid(column=0, row=23)
current_index=0
lbl020 = Label(window,text="Cvr mode: saved cvr file", font=("Arial Bold", 12))
lbl020.grid(column=0,row=20)
lbl024 = Label(window,text="Rotation direction: ", font=("Arial Bold", 12))
lbl024.grid(column=0,row=24)
lbl026 = Label(window,text="Rotation degree", font=("Arial Bold", 12))
lbl026.grid(column=0,row=26)
cvr_rotation_direction = Combobox(window)
cvr_rotation_direction['values']= ['up','eye','horizontal']
cvr_rotation_direction.current(0) #set the selected item
cvr_rotation_direction.grid(column=0, row=25)
degree_list=[]
for i in range(360):
    degree_list.append(i)
cvr_rotation_degree = Combobox(window)
cvr_rotation_degree['values']= degree_list #range from 0 to 360
cvr_rotation_degree.current(0) #set the selected item
cvr_rotation_degree.grid(column=0, row=27)

#update the data list when choose to create a cvr
def show023():
    global data_list
    new_cvr_data_index['values']= data_list
    new_cvr_data_index.current(0) #set the selected item
def update_cvr_list():
    cvr_save_list['values']= readcvr()
    if len(cvr_save_list['values'])!=0 :
        cvr_save_list.current(0) #set the selected item
    
def delete_cvr():#delete folder
    #directory neeed to adjust for cvr three functiosn
    #print(cvr_save_list.current())
    global full_path
    path = full_path+'/'+save_data_list['values'][save_data_list.current()]
    os.chdir(path)
    folder_name = cvr_save_list['values'][cvr_save_list.current()]
    get_ipython().system('rm -rf {folder_name}')
    deletecvr(folder_name)
    update_cvr_list()  

#this function take cvr_save_list as cvr folder name,display the figures inside this folder

def open_cvr():
    import tkinter as tk
    win = tk.Toplevel()
    win.wm_title("graph window")
    folder_name = cvr_save_list['values'][cvr_save_list.current()]
    #the folder_name format: s6a02-50-BE-rotation-up-30
    #We want to take the last 2 or 3 digit for angels
    lastindex = folder_name.rfind('-', 0, len(folder_name))+1
    angel = (int)(folder_name[lastindex:len(folder_name)])
    
    n = (int)(360/angel)
    print("value n: "+str(n))
    global full_path
    folder_path = full_path+'/'+save_data_list['values'][save_data_list.current()]+'/'+folder_name
    #get all the file name and make it an array
    imagename = os.listdir(folder_path)
    current_path = os.getcwd()
    
    global current_index
    current_index=0
    os.chdir(folder_path)
    image = Image.open(imagename[0])
    #test_image = image.resize(200,200, Image.ANTIALIAS) ## The (250, 250) is (height, width)
    test_image = ImageTk.PhotoImage(image)
    my_labelimg = Label(win,image = test_image )
    my_labelimg.image = test_image
    my_labelimg.grid(column=0,row=0,columnspan=1)
    
    
    #index problem not fixed yet, index out of bound may occur
    def next_figure():
        os.chdir(folder_path)
        global current_index
        if(current_index<n):
            current_index+=1
        print(current_index)
        image = Image.open(imagename[current_index])
        print(imagename[current_index])
        test_image = ImageTk.PhotoImage(image)
        my_labelimg = Label(win,image = test_image )
        my_labelimg.image = test_image
        my_labelimg.grid(column=0,row=0,columnspan=1)
        os.chdir(current_path)
    def previous_figure():
        os.chdir(folder_path)
        global current_index
        if(current_index>0):
            current_index-=1
        print(current_index)
        image = Image.open(imagename[current_index])
        print(imagename[current_index])
        test_image = ImageTk.PhotoImage(image)
        my_labelimg = Label(win,image = test_image )
        my_labelimg.image = test_image
        my_labelimg.grid(column=0,row=0,columnspan=1)
        os.chdir(current_path)
        
    btnwin01 = Button(win, text="next figure",command=next_figure)
    btnwin01.grid(column=0, row=1)
    btnwin02 = Button(win, text="previous figure",command=previous_figure)
    btnwin02.grid(column=0, row=2)
    os.chdir(current_path)
    
#similar to open cvr, create_cvr take all the relative combobox info
def create_cvr():
    import tkinter as tk
    win = tk.Toplevel()
    win.wm_title("graph window")
    #script_path='/home/jonestw/jian0250/interface'#or change to current path 
    global full_path
    script_path = full_path
    folder_name = save_data_list['values'][save_data_list.current()]+"-"+new_cvr_data_index['values'][new_cvr_data_index.current()]
    folder_name+='-'+combo_data110['values'][combo_data110.current()]+'-'+'rotation'
    folder_name+='-'+cvr_rotation_direction['values'][cvr_rotation_direction.current()]
    folder_name+='-'+cvr_rotation_degree['values'][cvr_rotation_degree.current()]
    get_ipython().system('mkdir {folder_name}')

    try:
        f = open("cvr.txt","r")
        f.close()
    except:
        get_ipython().system('touch cvr.txt')
    writecvr(folder_name)
    update_cvr_list()
    current_path = full_path+'/'+save_data_list['values'][save_data_list.current()]
    folder_path= current_path+'/'+folder_name
    commandname = save_data_list['values'][save_data_list.current()]+"-"
    
    #add zeros before number make it form 4 digit
    four_digit=""
    if(int(new_cvr_data_index['values'][new_cvr_data_index.current()])<10):
        four_digit+= "000"
        four_digit+= str(new_cvr_data_index['values'][new_cvr_data_index.current()])
    elif(int(new_cvr_data_index['values'][new_cvr_data_index.current()])<100):
        four_digit+= "00"
        four_digit+= str(new_cvr_data_index['values'][new_cvr_data_index.current()])
    elif(int(new_cvr_data_index['values'][new_cvr_data_index.current()])<1000):
        four_digit+= "0"
        four_digit+= str(new_cvr_data_index['values'][new_cvr_data_index.current()])
    frame=int(360/int(cvr_rotation_degree['values'][cvr_rotation_degree.current()]))

    commandname+= four_digit+"-"+combo_data110['values'][combo_data110.current()]+".cvrin>>o1r.view"
    get_ipython().system("{script_path}/ee.sh {new_cvr_data_index['values'][new_cvr_data_index.current()]} {combo_data110['values'][combo_data110.current()]} cvr save=in")
    get_ipython().system('rm -f o1r.view')
    
    get_ipython().system('touch temp.sh')
    f= open("temp.sh","w") 
    new_string="module load intel/cluster/2018\nulimit -s unlimited \nexport post_bin_path=/home/dhp/public/postproc/dev\n"
    new_string+="export PATH=$post_bin_path:$PATH\n"
    new_string+="rm -f o1r.view\n"



    if(cvr_rotation_direction.current()==0):
        new_string+="for i in center eye up fov bbox\ndo\ngrep $i "+commandname+"\ndone\n"
        new_string+="path_view2view o1r.view o1r.view i=arc1u n="+str(frame)+" o=rot1.path\n"
    elif(cvr_rotation_direction.current()==1):
        get_ipython().system('for i in center eye eye fov bbox;do;grep $i {commandname};done')
        get_ipython().system('path_view2view o1r.view o1r.view i=arcie n={frame} o=rot1.path')
    else:
        get_ipython().system('for i in center eye horizontal fov bbox;do;grep $i {commandname};done')
        get_ipython().system('path_view2view o1r.view o1r.view i=arcih n={frame} o=rot1.path')
    f.write(new_string)
    f.close()
    get_ipython().system('chmod 755 temp.sh')
    get_ipython().system('./temp.sh')
    get_ipython().system('touch GENERATE_ONLY')
    get_ipython().system("{script_path}/ee.sh {new_cvr_data_index['values'][new_cvr_data_index.current()]} {combo_data110['values'][combo_data110.current()]} cvr path=rot1.path")
    get_ipython().system('rm GENERATE_ONLY')
    get_ipython().system('ls *jpg')
    

    imagename = []#a list of generated image name
    for i in range(int(frame)):
        current_name = save_data_list['values'][save_data_list.current()]+'-'+four_digit+'-'+combo_data110['values'][combo_data110.current()]+'_'
        if (i<10):
            current_name+='00'+str(i)
        elif(i<100):
            current_name+='0'+str(i)
        current_name+=".jpg"
        imagename.append(current_name) 
    for x in imagename:
        get_ipython().system("mv {current_path+'/'+x} {folder_path+'/'}")
    os.chdir(folder_path)
    print(folder_path)
    
    global current_index
    current_index=0
    image = Image.open(imagename[0])
    #test_image = image.resize(200,200, Image.ANTIALIAS) ## The (250, 250) is (height, width)
    
    test_image = ImageTk.PhotoImage(image)
    my_labelimg = Label(win,image = test_image )
    my_labelimg.image = test_image
    my_labelimg.grid(column=0,row=0,columnspan=1)
    def next_figure():
        os.chdir(folder_path)
        global current_index
        if(current_index<frame):
            current_index+=1
        image = Image.open(imagename[current_index])
        test_image = ImageTk.PhotoImage(image)
        my_labelimg = Label(win,image = test_image )
        my_labelimg.image = test_image
        my_labelimg.grid(column=0,row=0,columnspan=1)
        os.chdir(current_path)
    def previous_figure():
        os.chdir(folder_path)
        global current_index
        if(current_index>0):
            current_index-=1
        image = Image.open(imagename[current_index])
        test_image = ImageTk.PhotoImage(image)
        my_labelimg = Label(win,image = test_image )
        my_labelimg.image = test_image
        my_labelimg.grid(column=0,row=0,columnspan=1)
        os.chdir(current_path)
        
    btnwin01 = Button(win, text="next figure",command=next_figure)
    btnwin01.grid(column=0, row=1)
    btnwin02 = Button(win, text="previous figure",command=previous_figure)
    btnwin02.grid(column=0, row=2)
    
    
    os.chdir(current_path)


# In[ ]:


def excute_cvr():
    if(cvr_list_action.current()==0):
        create_cvr()
    elif(cvr_list_action.current()==1):
        open_cvr()
    else:
        delete_cvr()
        

list_combo_box = []

#this function give user choices to choose data index they want
def update_combo_box():
    global data_list
    global list_combo_box
    for i in range(20):
        selected_data_list = Combobox(window)
        selected_data_list['values']= data_list
        selected_data_list.current() #set the selected item
        selected_data_list.grid(column=2, row=2+i)
        list_combo_box.append(selected_data_list)
    
    show023()
    btn030 = Button(window, text="confirm",command=excute_cvr)
    btn030.grid(column=0, row=30)


# In[ ]:


txt010 = Entry(window,width=25)#description when create a data
txt010.grid(column=0, row=10)
lbl09 = Label(window, text="Add a description to the data set", font=("Arial Bold", 12))
lbl09.grid(column=0,row=9)


from tkinter.ttk import *

#show avaiable data intervel
def update_range(path,dataname):
    result = find_intervel(path,dataname)
    #all_data_index = result[0]
    intervel = result[1]#get a new path then update the intervel
    global data_list
    data_list = result[0] 
    print(intervel)
    avaliable_intervel = ""
    
    for indexi in range(len(intervel)):
        if(indexi%2==0):
            avaliable_intervel+=str(intervel[indexi])
            avaliable_intervel+="-"
            avaliable_intervel+=str(intervel[indexi+1])
            avaliable_intervel+=" "
    avaliable_intervel = ""

    for indexi in range(len(intervel)):
        if(indexi%2==0):
            avaliable_intervel+=str(intervel[indexi])
            avaliable_intervel+="-"
            avaliable_intervel+=str(intervel[indexi+1])
            avaliable_intervel+=" "

    lbl21 = Label(window, text=avaliable_intervel, font=("Arial Bold", 12))
    lbl21.grid(column=1,row=5)
    update_combo_box()
def excute_action():
    #script_path='/home/jonestw/jian0250/interface'
    global full_path
    script_path = full_path
    if(save_data_list.current()==-1):# no char in save dataset
        five_chara06 = 'aaaaa'
    else:
        five_chara06=save_data_list['values'][save_data_list.current()]#current five character in "save dataset"
    if(add_data_list.current()==-1):# no char in add dataset
        five_chara04 = 'aaaaa'
    else:
        five_chara04=add_data_list['values'][add_data_list.current()]#current five character in "add new dataset"
    if(data_list_action.current()==1):#add current data into saved file
        writeindex(five_chara04)
        save_data_list['values']= readindex()
        get_ipython().system('mkdir {five_chara04}')
        global path
        newpath = path+'/'+five_chara04+'/dumps'
        print(newpath)
        os.chdir(full_path+'/'+five_chara04)
        get_ipython().system("cd {newpath};{script_path}/available.sh new {five_chara04} {'1'+txt010.get()}")
        get_ipython().system('{script_path}/available.sh {five_chara04}')
    elif(data_list_action.current()==2):#delete
        deleteindex(five_chara06)
        save_data_list['values']= readindex()
        get_ipython().system('rm -rf {five_chara06}')
    elif(data_list_action.current()==0):#use
        current = full_path
        os.chdir(current+'/'+five_chara06)
        dataindex_list = open("dataset.info","r")
        path=""
        result = 1
        for line in dataindex_list:
            result = line.find("datasetdir")
            if(result!=-1):
                path = line   
        path = path.replace("datasetdir=","")
        path = path.replace('"','')
        path = path.replace('"','')
        path = path.replace('\n','')
        print(path)
        update_range(path,five_chara06)
        update_cvr_list()
    else:
        print("error")
        print(data_list_action.current())
    
btn07 = Button(window, text="confirm",command=excute_action)
btn07.grid(column=0, row=11)


# In[ ]:


#txt for input intervel num
txt17 = Entry(window,width=10)
txt17.grid(column=1, row=12)
lbl17 = Label(window, text="Input an data intervel for general preview: ", font=("Arial Bold", 12))
lbl17.grid(column=1,row=11)
    
lbl1 = Label(window, text="Avaliable data indexing intervel: ", font=("Arial Bold", 12))
lbl1.grid(column=1,row=4)
lbl17 = Label(window, text="Select mode ", font=("Arial Bold", 12))
lbl17.grid(column=1,row=7)
combo_data18 = Combobox(window)#graph type
combo_data18['values']= ['zprof','xprof','yprof','dist','spc3v','view2d','xstrip','ystrip','zstrip','cvr']
combo_data18.current(0) #set the selected item
combo_data18.grid(column=1, row=8) 
#cvr only works for one index

lbl17 = Label(window, text="Select field ", font=("Arial Bold", 12))
lbl17.grid(column=1,row=9)
combo_data110 = Combobox(window)#field
combo_data110['values']= ['B','V','BE','KE','gBE','B1','B2','B3','V1','V2','V3','Vav','dV','dV1','dV2','dV3','gV','maggV','W','magW','W1','W2','W3']
combo_data110.current(2) #set the selected item
combo_data110.grid(column=1, row=10) 

    


# In[ ]:


save_data_list = Combobox(window)#data list saved in data_list.txt
save_data_list['values']= readindex()
save_data_list.current() #set the selected item
save_data_list.grid(column=0, row=6) 
def show_intervel():
    intervel = int(txt17.get())#intervel num
    global data_list
    new_list=data_list[::intervel]#select element based on intervel (new_list is string not int)
    print(new_list)
    command = ""
    for i in new_list:
        command+=str(i)
        command+=","
    command = command[0:len(command)-1]#remove last ','
    count=0
    for i in new_list:
        if(int(i)<10):
            new_list[count] = "000"+str(i)
        elif(int(i)>=10 and int(i)<100):
            new_list[count] = "00"+str(i)
        elif(int(i)>=100 and int(i)<1000):
            new_list[count] = "0"+str(i)
        count = count+1
    #print(new_list)
    global full_path
    script_path =full_path
    #script_path='/home/jonestw/jian0250/interface'
    get_ipython().system("{script_path}/ee.sh {command} {combo_data110['values'][combo_data110.current()]} {combo_data18['values'][combo_data18.current()]}")
    index=0 #use for count the picture index
    import tkinter as tk
    win = tk.Toplevel()
    win.wm_title("graph window")
    high = len(new_list)/5.0
    wide = 5
    if(len(new_list)<=5):
        wide = len(new_list)
    import math
    high = math.ceil(high)
    for i in range(int(wide)+1):
        for j in range(int(high)):
            if(len(new_list)<=5 and index<len(new_list)):
                imagename = save_data_list['values'][save_data_list.current()]+"-"
                imagename+= str(new_list[index])
                imagename+= "-"+combo_data110['values'][combo_data110.current()]+"."+combo_data18['values'][combo_data18.current()]+".png"
                image = Image.open(imagename)
                get_ipython().system("touch display_in_notebook")
                #test_image = image.resize((int(1920/len(new_list)), int(1920/len(new_list))), Image.ANTIALIAS) ## The (250, 250) is (height, width)
                test_image = ImageTk.PhotoImage(image)
                my_labelimg = Label(win,image = test_image)
                my_labelimg.image = test_image
                my_labelimg.grid(column=i,row=j,columnspan=1)
                index+=1
            elif(index<len(new_list)):
                imagename = save_data_list['values'][save_data_list.current()]+"-"
                imagename+= str(new_list[index])
                #print(combo_data18.current())
                if(combo_data18.current()==9):
                    imagename+= "-"+combo_data110['values'][combo_data110.current()]+"_000.jpg"
                    #print("hhh")
                else:
                    imagename+= "-"+combo_data110['values'][combo_data110.current()]+"."+combo_data18['values'][combo_data18.current()]+".png"
                image = Image.open(imagename)
                length_of_graph= int(1920/wide)
                test_image = image.resize((length_of_graph, length_of_graph), Image.ANTIALIAS) ## The (250, 250) is (height, width)
                test_image = ImageTk.PhotoImage(test_image)
                my_labelimg = Label(win,image = test_image )
                my_labelimg.image = test_image
                my_labelimg.grid(column=i,row=j,columnspan=1)
                index+=1


# In[ ]:


my_btn19 = Button(window,text="show graph with intervel",command=show_intervel)#change the command
my_btn19.grid(column=1,row=13)
#get the intervel num


# In[ ]:


def show_all_graph():
    command_line = ''
    new_list=[]
    global list_combo_box
    for i in list_combo_box:
        if(i.current()!=-1):
            command_line+=str(i['values'][i.current()])
            command_line+=','
            new_list.append(i['values'][i.current()])
    command_line = command_line[0:len(command_line)-1]#remove last ','
    count=0
    for i in new_list:#convert to 4 digit
        if(int(i)<10):
            new_list[count] = "000"+str(i)
        elif(int(i)>=10 and int(i)<100):
            new_list[count] = "00"+str(i)
        elif(int(i)>=100 and int(i)<1000):
            new_list[count] = "0"+str(i)
        count = count+1
    #print(new_list)
    global full_path
    script_path =full_path
    #script_path='/home/jonestw/jian0250/interface'
    get_ipython().system("{script_path}/ee.sh {command_line} {combo_data110['values'][combo_data110.current()]} {combo_data18['values'][combo_data18.current()]}")
    
    index=0 #use for count the picture index
    import tkinter as tk
    get_ipython().system("touch display_in_notebook")
    win = tk.Toplevel()
    win.wm_title("graph window")
    high = len(new_list)/5.0
    wide = 5
    if(len(new_list)<=5):
        wide = len(new_list)
    import math
    high = math.ceil(high)
    for i in range(int(wide)+1):
        for j in range(int(high)):
            if(len(new_list)<=5 and index<len(new_list)):
                imagename = save_data_list['values'][save_data_list.current()]+"-"
                imagename+= str(new_list[index])
                imagename+= "-"+combo_data110['values'][combo_data110.current()]+"."+combo_data18['values'][combo_data18.current()]+".png"
                image = Image.open(imagename)
                test_image = ImageTk.PhotoImage(image)
                my_labelimg = Label(win,image = test_image)
                my_labelimg.image = test_image
                my_labelimg.grid(column=i,row=j,columnspan=1)
                index+=1
            if(index<len(new_list)):
                imagename = save_data_list['values'][save_data_list.current()]+"-"
                imagename+= str(new_list[index])
                print(combo_data18.current())
                if(combo_data18.current()==9):
                    imagename+= "-"+combo_data110['values'][combo_data110.current()]+"_000.jpg"
                else:
                    imagename+= "-"+combo_data110['values'][combo_data110.current()]+"."+combo_data18['values'][combo_data18.current()]+".png"
                image = Image.open(imagename)
                test_image = image.resize((int(1920/wide), int(850/high)), Image.ANTIALIAS) ## The (250, 250) is (height, width)
                test_image = ImageTk.PhotoImage(test_image)
                my_labelimg = Label(win,image = test_image )
                my_labelimg.image = test_image
                my_labelimg.grid(column=i,row=j,columnspan=1)
                index+=1


# In[ ]:


lbl21 = Label(window, text="Select data index", font=("Arial Bold", 12))
lbl21.grid(column=2, row=1)
btn224 = Button(window, text="display",command=show_all_graph)
btn224.grid(column=2, row=24)


# In[ ]:


window.mainloop()

