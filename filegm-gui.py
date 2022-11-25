#! /usr/bin/python3
# to start filgm_gui you have to install tkinter with -> sudo apt-get install python3-tk


from tkinter import *
from tkinter import ttk
from filegm import Filegm
import subprocess
import os







class Dict_stream:                                                                                              # class that creates a dictionary with the results
                                                                                                                # - of filegm

    def __init__(self, data_A, data_B, estensioni):
        self.data_A = data_A
        self.data_B = data_B
        self.estensioni = estensioni

    def dict_outp(self):

        data_A = self.data_A
        data_B = self.data_B
        estensioni = self.estensioni

        def inpt():
            f = Filegm(data_A, data_B, estensioni)
            f.tutte_funzioni()
            return f.__dict__

        def oupt():
            dct = inpt()
            return dct

        return oupt()







class Gui_filegm:

    def __init__(self, master):


        self.master = master

        self.master.title('Filegm')



        frm_top = Frame(self.master, bg='#404040', height=24)
        frm_top.pack(side=TOP, fill=X)

        frm_center = Frame(self.master, bg='#404040', height=200)
        frm_center.pack(fill=BOTH, expand=True)

        frm_bottom = Frame(self.master, bg='#404040', height=24)
        frm_bottom.pack(side=BOTTOM, fill=X)



        frm_lbl = Frame(frm_center, bg='#404040', width=500, height=400, padx=2)
        frm_lbl.pack(side=LEFT, fill=BOTH, expand=False)

        frm_txt = Frame(frm_center, bg='#404040', width=600, height=400, padx=2)
        frm_txt.pack(side=LEFT, fill=BOTH, expand=True)



        row_1 = Frame(frm_lbl, width=500, bg='#404040')
        row_1.pack(fill=X, expand=True)

        row_2 = Frame(frm_lbl, width=500, bg='#404040')
        row_2.pack(fill=X, expand=True)

        row_3 = Frame(frm_lbl, width=500, bg='#404040')
        row_3.pack(fill=X, expand=True)

        row_4 = Frame(frm_lbl, width=500, bg='#404040')
        row_4.pack(fill=X, expand=True)

        row_5 = Frame(frm_lbl, width=500, bg='#404040')
        row_5.pack(fill=X, expand=True)

        row_6 = Frame(frm_lbl, width=500, bg='#404040')
        row_6.pack(fill=X, expand=True)

        row_7 = Frame(frm_lbl, width=500, bg='#404040')
        row_7.pack(fill=X, expand=True)

        row_8 = Frame(frm_lbl, width=500, bg='#404040')
        row_8.pack(fill=X, expand=True)



        lbl_lst_inp = [
            "\nEnter the date from which you want to know\nthe files created in this format \"Y-M-D\": \n",
            "If you want to limit the time span to a second\nterm after the first, type the second date\nin the format \"Y-M-D\", otherwise press the enter\nkey to set the second term to today's date: ",
            "Specifies the file format, for example \".txt\".\nIf more than one format is specified, DO NOT\nuse commas or other punctuation: ",
        ]

        lbl_lst_out = [
            "Total files in the \"home\" folder and subfolders: \n",
            "Total files present in the forms specified above\nin the \"home\" folder and subfolders: ",
            "Total files present in the forms specified above\nin the \"home\" folder and subfolders\nin the date search: ",
            "The duplicate were found in the date search: "
        ]



        lbl_0 = Label(row_1, anchor=W, justify=LEFT, bg='#404040', fg='#E6E6E6', text=lbl_lst_inp[0])
        lbl_0.pack(side=LEFT, fill=BOTH, expand=True)

        lbl_1 = Label(row_2, anchor=W, justify=LEFT, bg='#404040', fg='#E6E6E6', text=lbl_lst_inp[1], pady=15)
        lbl_1.pack(side=LEFT, fill=BOTH, expand=True)

        lbl_2 = Label(row_3, anchor=W, justify=LEFT, bg='#404040', fg='#E6E6E6', text=lbl_lst_inp[2])
        lbl_2.pack(side=LEFT, fill=BOTH, expand=True)

        lbl_3 = Label(row_4, anchor=W, justify=LEFT, bg='#404040', fg='#E6E6E6', text=lbl_lst_out[0], pady=15)
        lbl_3.pack(side=LEFT, fill=BOTH, expand=True)

        lbl_4 = Label(row_5, anchor=W, justify=LEFT, bg='#404040', fg='#E6E6E6', text=lbl_lst_out[1])
        lbl_4.pack(side=LEFT, fill=BOTH, expand=True)

        lbl_5 = Label(row_6, anchor=W, justify=LEFT, bg='#404040', fg='#E6E6E6', text=lbl_lst_out[2], pady=15)
        lbl_5.pack(side=LEFT, fill=BOTH, expand=True)

        lbl_6 = Label(row_7, anchor=W, justify=LEFT, bg='#404040', fg='#E6E6E6', text=lbl_lst_out[3])
        lbl_6.pack(side=LEFT, fill=BOTH, expand=True)



        ent_ent_0 = Entry(row_1, background='#D9D9D9')                                                          # widget input, date A
        ent_ent_0.pack(side=LEFT, fill=X, pady=15, ipady=5)
        ent_ent_0.focus()

        ent_ent_1 = Entry(row_2, background='#D9D9D9')                                                          # .. date B
        ent_ent_1.pack(side=LEFT, fill=X, pady=15, ipady=6)

        ent_ent_2 = Entry(row_3, background='#D9D9D9')                                                          # .. extension(s)
        ent_ent_2.pack(side=LEFT, fill=X, pady=20, ipady=6)


        #           output  ---------

        ent_lbl_0 = Label(row_4, height=2, width=20)
        ent_lbl_0.pack(side=LEFT, fill=X, pady=2, ipady=1)

        ent_lbl_1 = Label(row_5, height=2, width=20)
        ent_lbl_1.pack(side=LEFT, fill=X, pady=1, ipady=1)

        ent_lbl_2 = Label(row_6, height=2, width=20)
        ent_lbl_2.pack(side=LEFT, fill=X, pady=9, ipady=1)

        ent_lbl_3 = Label(row_7, height=2, width=20)
        ent_lbl_3.pack(side=LEFT, fill=X, pady=14, ipady=1)



        txt = Text(frm_txt, font=('Liberation Mono', 11), background='#3D3D3D',foreground='#FBFFFF', wrap=NONE, cursor="arrow")      # 'Text()' widget declaration with native arrow
                                                                                                                # - cursor
        txt.config(state=DISABLED)                                                                              # in this way it will not be possible to write
                                                                                                                # - directly into the widget
        txt.pack(ipady=27, fill=BOTH, expand=True)

        scroll_y = Scrollbar(frm_center, background='#787878')                                                                        # vertical scroller
        scroll_y.pack(side="right", fill="y")
        scroll_y.config(command=txt.yview)
        txt.config(yscrollcommand=scroll_y.set)

        scroll_x = Scrollbar(frm_txt, background='#787878', orient=HORIZONTAL)                                                        # scroller orizzontale
        scroll_x.pack(side="bottom", fill="x")
        scroll_x.config(command=txt.xview)
        txt.config(xscrollcommand=scroll_x.set)






        def del_txt_and_entry():                                                                                # Function to clear label and text field outputs

            ent_lbl_0['text'] = ''                                                                              # delete labels
            ent_lbl_1['text'] = ''
            ent_lbl_2['text'] = ''
            ent_lbl_3['text'] = ''

            txt.config(state=NORMAL)                                                                            # delete text field
            txt.delete("1.0", "end")
            txt.update()
            txt.config(state=DISABLED)






        def output_file():

            del_txt_and_entry()

            io_dict = Dict_stream(ent_ent_0.get(), ent_ent_1.get(), ent_ent_2.get())

            allFiles = io_dict.dict_outp()

            ent_lbl_0['text'] = allFiles.get('print_totFiles')
            ent_lbl_1['text'] = allFiles.get('print_TotFiles_Est')
            ent_lbl_2['text'] = allFiles.get('print_specified_files_that_period')
            ent_lbl_3['text'] = allFiles.get('print_duplicate')


            txt.config(state=NORMAL)
            a = 0
            for i in allFiles.get('file_in_focus'):                                                  # for each element of 'file in focus'

                a += 1

                filename = 'path-' + str(a)                                                                     # 'tags' are defined, named 'filename', each with
                                                                                                                # - the respective number 'a' for each element in
                                                                                                                # - the loop.

                en_clr = '' + str(a)                                                                            # ... by precisely defining the name of tags this
                                                                                                                # - way (except for defining 'filename', for its
                                                                                                                # - functionality!), i.e., with an empty string +
                                                                                                                # - string-switching of the sequence number, it
                                                                                                                # - was seen that the blinking, i.e., the
                                                                                                                # - appearance) disappearance of the highlighting
                                                                                                                # - on mouseover (finally) works
                lv_clr = '' + str(a)
                clicked_clr = '' + str(a)

                txt.insert(END, i + '\n', (filename, en_clr, lv_clr, clicked_clr))                              # the third element ('filename') is used (I assume)
                                                                                                                # - to assign each looped element the respective
                                                                                                                # - 'filename' tag

                txt.tag_configure(filename)                                                                     # each tag has the options defined here
                txt.tag_configure(clicked_clr)
                txt.tag_configure(en_clr)
                txt.tag_configure(lv_clr)


                if i.endswith(('.jpg', '.jpeg', '.png', 'tiff', 'tif', '.bmp', '.eps', '.raw', '.cr2', '.nef', '.orf', '.sr2', '.webp')):
                    txt.tag_bind(filename, '<1>', lambda event, fn=i: subprocess.run(["xviewer", fn]))
                    txt.tag_bind(clicked_clr, '<1>', lambda event, wdg=txt, tn=clicked_clr: wdg.tag_configure(tn, foreground='#666633'))
                    txt.tag_bind(en_clr, '<Enter>', lambda event, wdg=txt, tn=en_clr: wdg.tag_configure(tn, background='#FFD162'))
                    txt.tag_bind(lv_clr, '<Leave>', lambda event, wdg=txt, tn=lv_clr: wdg.tag_configure(tn, background='#533E97'))
                elif i.endswith(('.ogv', '.webm', '.flv', '.avi', '.mov', 'wmv', '.3gp', '.yuv', '.mp4', '.asf', '.mpeg', '.mpg', '.mp3', '.mkv', '.flac', '.wav')):
                    txt.tag_bind(filename, '<1>', lambda event, fn=i: subprocess.run(["celluloid", fn]))
                    txt.tag_bind(clicked_clr, '<1>', lambda event, wdg=txt, tn=clicked_clr: wdg.tag_configure(tn, foreground='#666633'))
                    txt.tag_bind(en_clr, '<Enter>', lambda event, wdg=txt, tn=en_clr: wdg.tag_configure(tn, background='#FFD162'))
                    txt.tag_bind(lv_clr, '<Leave>', lambda event, wdg=txt, tn=lv_clr: wdg.tag_configure(tn, background='#1F508B'))
                elif i.endswith(('.txt', '.py', '.c', '.cpp')):
                    txt.tag_bind(filename, '<1>', lambda event, fn=i: subprocess.run(["gedit", fn]))
                    txt.tag_bind(clicked_clr, '<1>', lambda event, wdg=txt, tn=clicked_clr: wdg.tag_configure(tn, foreground='#666633'))
                    txt.tag_bind(en_clr, '<Enter>', lambda event, wdg=txt, tn=en_clr: wdg.tag_configure(tn, background='#FFD162'))
                    txt.tag_bind(lv_clr, '<Leave>', lambda event, wdg=txt, tn=lv_clr: wdg.tag_configure(tn, background='#506269'))
                elif i.endswith(('.odt', '.doc', '.docx', '.pptx')):
                    txt.tag_bind(filename, '<1>', lambda event, fn=i: subprocess.run(["libreoffice", fn]))
                    txt.tag_bind(clicked_clr, '<1>', lambda event, wdg=txt, tn=clicked_clr: wdg.tag_configure(tn, foreground='#666633'))
                    txt.tag_bind(en_clr, '<Enter>', lambda event, wdg=txt, tn=en_clr: wdg.tag_configure(tn, background='#FFD162'))
                    txt.tag_bind(lv_clr, '<Leave>', lambda event, wdg=txt, tn=lv_clr: wdg.tag_configure(tn, background='#0A7E8C'))
                elif i.endswith(('.gif')):
                    txt.tag_bind(filename, '<1>', lambda event, fn=i: subprocess.run(["gthumb", fn]))
                    txt.tag_bind(clicked_clr, '<1>', lambda event, wdg=txt, tn=clicked_clr: wdg.tag_configure(tn, foreground='#666633'))
                    txt.tag_bind(en_clr, '<Enter>', lambda event, wdg=txt, tn=en_clr: wdg.tag_configure(tn, background='#FFD162'))
                    txt.tag_bind(lv_clr, '<Leave>', lambda event, wdg=txt, tn=lv_clr: wdg.tag_configure(tn, background='#851852'))
                elif i.endswith(('.pdf',)):
                    txt.tag_bind(filename, '<1>', lambda event, fn=i: subprocess.run(["evince", fn]))
                    txt.tag_bind(clicked_clr, '<1>', lambda event, wdg=txt, tn=clicked_clr: wdg.tag_configure(tn, foreground='#666633'))
                    txt.tag_bind(en_clr, '<Enter>', lambda event, wdg=txt, tn=en_clr: wdg.tag_configure(tn, background='#FFD162'))
                    txt.tag_bind(lv_clr, '<Leave>', lambda event, wdg=txt, tn=lv_clr: wdg.tag_configure(tn, background='#B30B00'))
                elif i.endswith(('.html', '.php', '.xml')):
                    txt.tag_bind(filename, '<1>', lambda event, fn=i: subprocess.run(["firefox", fn]))
                    txt.tag_bind(clicked_clr, '<1>', lambda event, wdg=txt, tn=clicked_clr: wdg.tag_configure(tn, foreground='#666633'))
                    txt.tag_bind(en_clr, '<Enter>', lambda event, wdg=txt, tn=en_clr: wdg.tag_configure(tn, background='#FFD162'))
                    txt.tag_bind(lv_clr, '<Leave>', lambda event, wdg=txt, tn=lv_clr: wdg.tag_configure(tn, background='#41A2D1'))

            txt.config(state=DISABLED)


        btn_1 = Button(row_8, width=34, text='Shows the specified files from this period', fg='#404040', command=output_file)
        btn_1.grid(row=0, column=1, pady=10, padx=6)






        def output_dupl():

            del_txt_and_entry()

            io_dict = Dict_stream(ent_ent_0.get(), ent_ent_1.get(), ent_ent_2.get())

            allFiles = io_dict.dict_outp()

            ent_lbl_0['text'] = allFiles.get('print_totFiles')
            ent_lbl_1['text'] = allFiles.get('print_TotFiles_Est')
            ent_lbl_2['text'] = allFiles.get('print_specified_files_that_period')
            ent_lbl_3['text'] = allFiles.get('print_duplicate')


            txt.config(state=NORMAL)
            a = 0
            for i in io_dict.dict_outp().get('dupl_lst'):                                                       # for each element of 'file in focus'

                a += 1

                filename = 'path-' + str(a)                                                                     # 'tags' are defined, named 'filename', each with
                                                                                                                # - the respective number 'a' for each element
                                                                                                                # - in the loop.
                en_clr = '' + str(a)
                lv_clr = '' + str(a)
                clicked_clr = '' + str(a)

                txt.insert(END, i + '\n', (filename, en_clr, lv_clr, clicked_clr))                              # the third element ('filename') is used (I assume)
                                                                                                                # - to assign each looped element the respective
                                                                                                                # - 'filename' tag

                txt.tag_configure(filename)                                                                     # each tag has the options defined here
                txt.tag_configure(clicked_clr)
                txt.tag_configure(en_clr)
                txt.tag_configure(lv_clr)

                if i.endswith(('.jpg', '.jpeg', '.png', 'tiff', 'tif', '.bmp', '.eps', '.raw', '.cr2', '.nef', '.orf', '.sr2', '.webp')):
                    txt.tag_bind(filename, '<1>', lambda event, fn=i: subprocess.run(["xviewer", fn]))
                    txt.tag_bind(clicked_clr, '<1>', lambda event, wdg=txt, tn=clicked_clr: wdg.tag_configure(tn, foreground='#666633'))
                    txt.tag_bind(en_clr, '<Enter>', lambda event, wdg=txt, tn=en_clr: wdg.tag_configure(tn, background='#FFD162'))
                    txt.tag_bind(lv_clr, '<Leave>', lambda event, wdg=txt, tn=lv_clr: wdg.tag_configure(tn, background='#533E97'))
                elif i.endswith(('.ogv', '.webm', '.flv', '.avi', '.mov', 'wmv', '.3gp', '.yuv', '.mp4', '.asf', '.mpeg', '.mpg', '.mp3', '.mkv', '.flac', '.wav')):
                    txt.tag_bind(filename, '<1>', lambda event, fn=i: subprocess.run(["celluloid", fn]))
                    txt.tag_bind(clicked_clr, '<1>', lambda event, wdg=txt, tn=clicked_clr: wdg.tag_configure(tn, foreground='#666633'))
                    txt.tag_bind(en_clr, '<Enter>', lambda event, wdg=txt, tn=en_clr: wdg.tag_configure(tn, background='#FFD162'))
                    txt.tag_bind(lv_clr, '<Leave>', lambda event, wdg=txt, tn=lv_clr: wdg.tag_configure(tn, background='#1F508B'))
                elif i.endswith(('.txt', '.py', '.c', '.cpp')):
                    txt.tag_bind(filename, '<1>', lambda event, fn=i: subprocess.run(["gedit", fn]))
                    txt.tag_bind(clicked_clr, '<1>', lambda event, wdg=txt, tn=clicked_clr: wdg.tag_configure(tn, foreground='#666633'))
                    txt.tag_bind(en_clr, '<Enter>', lambda event, wdg=txt, tn=en_clr: wdg.tag_configure(tn, background='#FFD162'))
                    txt.tag_bind(lv_clr, '<Leave>', lambda event, wdg=txt, tn=lv_clr: wdg.tag_configure(tn, background='#506269'))
                elif i.endswith(('.odt', '.doc', '.docx', '.pptx')):
                    txt.tag_bind(filename, '<1>', lambda event, fn=i: subprocess.run(["libreoffice", fn]))
                    txt.tag_bind(clicked_clr, '<1>', lambda event, wdg=txt, tn=clicked_clr: wdg.tag_configure(tn, foreground='#666633'))
                    txt.tag_bind(en_clr, '<Enter>', lambda event, wdg=txt, tn=en_clr: wdg.tag_configure(tn, background='#FFD162'))
                    txt.tag_bind(lv_clr, '<Leave>', lambda event, wdg=txt, tn=lv_clr: wdg.tag_configure(tn, background='#0A7E8C'))
                elif i.endswith(('.gif')):
                    txt.tag_bind(filename, '<1>', lambda event, fn=i: subprocess.run(["gthumb", fn]))
                    txt.tag_bind(clicked_clr, '<1>', lambda event, wdg=txt, tn=clicked_clr: wdg.tag_configure(tn, foreground='#666633'))
                    txt.tag_bind(en_clr, '<Enter>', lambda event, wdg=txt, tn=en_clr: wdg.tag_configure(tn, background='#FFD162'))
                    txt.tag_bind(lv_clr, '<Leave>', lambda event, wdg=txt, tn=lv_clr: wdg.tag_configure(tn, background='#851852'))
                elif i.endswith(('.pdf',)):
                    txt.tag_bind(filename, '<1>', lambda event, fn=i: subprocess.run(["evince", fn]))
                    txt.tag_bind(clicked_clr, '<1>', lambda event, wdg=txt, tn=clicked_clr: wdg.tag_configure(tn, foreground='#666633'))
                    txt.tag_bind(en_clr, '<Enter>', lambda event, wdg=txt, tn=en_clr: wdg.tag_configure(tn, background='#FFD162'))
                    txt.tag_bind(lv_clr, '<Leave>', lambda event, wdg=txt, tn=lv_clr: wdg.tag_configure(tn, background='#B30B00'))
                elif i.endswith(('.html', '.php', '.xml')):
                    txt.tag_bind(filename, '<1>', lambda event, fn=i: subprocess.run(["firefox", fn]))
                    txt.tag_bind(clicked_clr, '<1>', lambda event, wdg=txt, tn=clicked_clr: wdg.tag_configure(tn, foreground='#666633'))
                    txt.tag_bind(en_clr, '<Enter>', lambda event, wdg=txt, tn=en_clr: wdg.tag_configure(tn, background='#FFD162'))
                    txt.tag_bind(lv_clr, '<Leave>', lambda event, wdg=txt, tn=lv_clr: wdg.tag_configure(tn, background='#41A2D1'))

            txt.config(state=DISABLED)



        btn_2 = Button(row_8, width=18, text='Show duplicates files', fg='#404040', command=output_dupl)
        btn_2.grid(row=0, column=2, pady=10, padx=6)







def main():
    root = Tk()
    app = Gui_filegm(root)
    root.mainloop()



if __name__ == '__main__':
    main()

