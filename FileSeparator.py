### import important work module....

import os ,shutil
import tkinter as tk
from tkinter import _Color, ttk
from tkinter import filedialog
from tkinter import messagebox as m_box

### Defining the main working in the function..



def mainfunc(folder_path):
    dict_extensions = {
    
#######  Popular extension present in realworld environment in the form of dict and contain tuple for all types of extension

    'Audio_files' : ('.pcm','.wav','.aiff','.mp3','.aac','.ogg','.wma','.flac','.alac','.m4a'),
    'Video_files' : ('.webm','.mkv','.flv','.flv','.vob','.ogv','.ogg','.drc','.gif','.gifv','.mng','.avi','.MTS','.M2TS','.TS','.mov','.qt','.wmv','.yuv','.rm','.rmvb','.viv','.asf','.amv','.mp4','.m4p','.m4v','.mpg','.mp2','.mpeg','.mpe','.mpv','.mpg','.mpeg','.m2v','.svi','.3gp','.3g2','.mxf','.roq','.nsv','.flv','.f4v','.f4p','.f4a','.f4b'),
    'Image_files' : ('.jpg','.jpeg','.jpe','.jif','.jfif','.jfi','.png','.gif','.webp','.tiff','.tif','.psd','.raw','.arw','.cr2','.nrw','.k25','.bmp','.dib','.heif','.heic','.ind','.indd','.indt','.jp2','.j2k','.jpf','.jpx','.jpm','.mj2','.svg','.svgz'),
    'Compressed_files' : ('.7z','.arj','.deb','.pkg','.rar','.rpm','.tar','.gz','.z','.zip'),
    'Disc_media_files' : ('.bin','.dmg','.iso','.toast','.vcd'),
    'Data_database_files' : ('.csv','.dat','.db','.dbf','.log','.mdb','.sav','.sql','.tar','.xml'),
    'Email_files' : ('.email','.eml','.emlx','.msg','.oft','.ost','.pst','.vcf'),
    'Executable_files' : ('.apk','.bat','.bin','.cgi','.pl','.com','.exe','.gadget','.jar','.msi','.wsf'),
    'Font_files' : ('.fnt','.fon','.otf','.ttf'),
    'Internet_files' : ('.asp','.aspx','.cer','.cfm','.cgi','.pl','.css','.htm','.html','.js','.jsp','.part','.php','.rss','.xhtml'),
    'Presentation_files' : ('.key','.odp','.pps','.ppt','.pptx'),
    'Coding_files' : ('.c','.c++','.cgi','.pl','.class','.cpp','.cs','.h','.java','.php','.py','.sh','.swift','.vb'),
    'Text_files' : ('.doc','.docx','.odt','.pdf','.rtf','.tex','.txt','.wpd')

    }


    ##### Defining the sub function for search and filter the path we given through the GUI app..

    def file_finder(folder_path,file_extensions):
        files = []
        for file in os.listdir(folder_path):
            for extension in file_extensions:
                if  file.endswith(extension):
                    files.append(file)
        return files

    for extension_type , extension_tuple in dict_extensions.items():    ##loop for checking each file for all present
        # print("calling file finder: ")                                ## extension and then pass it to sub function.
        # print(file_finder(folder_path,extension_tuple))
        try:
            if len(file_finder(folder_path,extension_tuple))>0:             ##condition for checking a file is present of any extension.
                folder_name = extension_type.split('_')[0] + '_Files'
                folderpath = os.path.join(folder_path,folder_name)
                if os.path.exists(folderpath)==False:                       ## condition for checking if path folder is already exist or not
                    os.mkdir(folderpath)
            for item in (file_finder(folder_path,extension_tuple)):
                item_path = os.path.join(folder_path,item)
                item_new_path = os.path.join(folderpath,item)
                shutil.move(item_path,item_new_path)
        except:
            m_box.showerror("Path Error..","You entered a wrong path..")
            break
    m_box.showinfo("Operation Status...","Opertion done sucessfully..")
        

####................................................ Working on gui window...........................................................####



win = tk.Tk()

#### ................................................set the gui application title.................................................####

win.title('File - Filter')

####..........................................changing the gui window background color..............................................####

win.configure(background='#41BFBF')

####....................................create a gui labelframe on gui application window..............................................####

labels=tk.LabelFrame(win,text="")
labels.pack(pady = 200)
labels.configure(background="#FFFFFF")

####..........................................creating a gui label on default label frame..............................................####

lab=ttk.Label(labels,text = '                     Enter The Folder Path :                             ',font=('times','16','bold'))
lab.pack(pady= 10)
lab.configure(background="#FFA500")
path_var = tk.StringVar()

####..................................................create a entry box for path entry.................................................####

entry_box = tk.Entry(labels,width = 52,textvariable=path_var,background="#FFFF00")
entry_box.pack(pady=10)

####..........................................creating a submit button and defining its process..............................................####

def click():
    folder_path = path_var.get()
    mainfunc(folder_path)
    entry_box.delete(0,tk.END)

ttk.Button(labels,text = "Filter",command=click).pack()
op = ttk.Label(labels,text = "OR",font = ('times','14','bold','italic'))
op.pack(pady=10)
op.configure(background="#FFA500")
ttk.Label(labels,text = "Select The Folder Path From System: ",background="#FFA500",font = ('times','16','bold')).pack(pady = 10)
folder_path = str()
def action():
    folder_path = filedialog.askdirectory()
    mainfunc(folder_path)

ttk.Button(labels,text = "Browse",command=action).pack()



win.mainloop()


