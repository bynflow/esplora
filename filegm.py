#! /usr/bin/python3

import os
from datetime import datetime, timedelta
# from tkinter import *

tme_tms = ''
tme_tms_2 = ''
#lsta = []
inp_3_tpl = ()


class Filegm:

    def __init__(self, data_a, data_b, estensioni):

        self.data_a = data_a
        self.data_b = data_b
        self.estensioni = estensioni


        # self.print_paths = p_p
        self.print_totFiles = None
        self.print_TotFiles_Est = None
        self.file_in_focus = []
        self.dupl_lst = []
        self.print_specified_files_that_period = None
        self.print_duplicate = None
        self.lsta = []


        # ----------------------------------------------------------------------    Entering a 'a' start date and a 'b' end date for the search

        tme = datetime.strptime(self.data_a, "%Y-%m-%d")
        global tme_tms
        tme_tms = datetime.timestamp(tme)
        # print(tme_tms)

        if self.data_b == '':

            self.data_b = datetime.now()
            tme2 = self.data_b
            global tme_tms_2
            tme_tms_2 = datetime.timestamp(tme2)
            # print(tme_tms_2)

        elif self.data_b == self.data_a:

            tme_2 = datetime.strptime(self.data_b, "%Y-%m-%d") + timedelta(days=1)
            tme_tms_2 = datetime.timestamp(tme_2)
            # print(tme_tms_2)

        else:

            tme_2 = datetime.strptime(self.data_b, "%Y-%m-%d") + timedelta(days=1)
            tme_tms_2 = datetime.timestamp(tme_2)
            # print(tme_tms_2)


        # ----------------------------------------------------------------------    Entering one or more file extensions, for searching

        global inp_3_tpl
        inp_3_tpl = tuple([i for i in self.estensioni.split()])
        # print(inp_3_tpl)



        #                       -----------------------------------------------







    def tutte_funzioni(self):

        def pth_gen():                                                              # Generic search generator of all folders and subfolders of $HOME
            for root, dirct, filename in os.walk(os.environ['HOME']):
                for file in dirct:
                    os.path.join(root, file)
                for name in filename:
                    yield os.path.join(root, name)


        # global print_totFiles
        self.print_totFiles = len([i for i in pth_gen()])
        print('Total files in home and subfolders are: ', self.print_totFiles, type(self.print_totFiles))

        #global ttFiles
        #ttFiles = print_totFiles



        def gen_ext():                                                              # Generator of all files (file = path and filename, then of the full path, i.e.,
                                                                                    # - respectively: head and tail, enclosed in string) with the extensions entered
                                                                                    # - in the search
            for i in pth_gen():
                if i.endswith(inp_3_tpl):
                    yield i


        # global print_TotFiles_Est
        self.print_TotFiles_Est = len([i for i in gen_ext()])
        print('The total files with the specified extension present in home and subfolders are: ', self.print_TotFiles_Est, type(self.print_TotFiles_Est))

        #global ttFilesEst
        #ttFilesEst = print_TotFiles_Est




        c_time = {i: os.path.getctime(i) for i in gen_ext()}                        # dictionary of all files with the extensions entered in the search with their
                                                                                    # - respective creation dates (creation ...say)


        def gen_values():                                                           # generator of all dates etracted from the 'c_time' dictionary, of all files
                                                                                    # - with the extensions entered in the search
            for i in c_time.values():
                yield i

        def gen_values_tme():                                                       # Generator of all dates greater than (equal to) date 'a', of all files with the
                                                                                    # - extensions entered in the search
            for i in gen_values():
                if i >= tme_tms:
                    yield i


        tme_lst = [i for i in gen_values_tme()]                                     # list of all dates greater than (equal to) the date 'a', of all files with the
                                                                                    # - extensions entered in the search




        if self.data_b:
            def gen_values_tme_2():                                                 # Generator of all 'epoch' dates greater than (equal to) date 'a' but less than
                                                                                    # - date 'b', of all files with the extensions entered in the search
                for i in tme_lst:
                    if i < tme_tms_2:
                        yield i


            tme_2_lst = [i for i in gen_values_tme_2()]                             # list of all dates greater than (equal to) date 'a' but less than date 'b', of
                                                                                    # - all files with the extensions entered in the search
            # print('tme_2_lst', tme_2_lst)

            # file_in_focus = []

        if self.data_b:
            def gen_tpl_lst_a_b():                                                  # Generator of a tuple array of all files with respective 'epoch' date, taken
                                                                                    # - from the 'c_time' dictionary, with the extensions entered in the search
                for i in c_time.items():
                    yield i

            def gen_fcs_tpl_a_b():                                                  # Generator of an array of tuples (string, epoch) of all files having the date
                                                                                    # - 'epoch' present in the range date 'a' and date 'b'
                for i in gen_tpl_lst_a_b():
                    if i[1] in tme_2_lst:
                        yield i
            #lista_controllo = [i for i in gen_fcs_tpl_a_b()]
            # print('lista_controllo', lista_controllo)

            def gen_file_in_focus_a_b():                                            # Generate a list of all files having the date 'epoch' present in the range date
                                                                                    # - 'a' and date 'b'
                for i in gen_fcs_tpl_a_b():
                    yield i[0]

            self.file_in_focus = [i for i in gen_file_in_focus_a_b()]               # list of all files having the date 'epoch' present in the range date 'a' and
                                                                                    # - date 'b' (list of the entire path)
            # print('file_in_focus', file_in_focus)


        else:
            def gen_tpl_lst():                                                      # Generator of a tuple array of all files with respective 'epoch' date, extracted
                                                                                    # - from the 'c_time' dictionary, with the extensions entered in the search
                for i in c_time.items():
                    yield i

            def gen_fcs_tpl():                                                      # Generator of an array of tuples (string, epoch) of all files having dates
                                                                                    # - greater than (equal to) the date 'epoch' 'a'
                for i in gen_tpl_lst():
                    if i[1] in tme_lst:
                        yield i

            def gen_file_in_focus():                                                # Generator of a list of all files having dates greater than (equal to) the
                                                                                    # - 'epoch' date 'a'
                for i in gen_fcs_tpl():
                    yield i[0]

            self.file_in_focus = [i for i in gen_file_in_focus()]                   # list of all files having dates greater than (equal to) the 'epoch' date 'a'
                                                                                    # - ('file_in_focus' above is instead the list of all files between dates 'a'
                                                                                    # - and 'b.')

        self.print_specified_files_that_period = len(self.file_in_focus)


        def gen_split_lst():                                                        # Generator of a list of only filenames (tail) present in one of the two
                                                                                    # - 'file_in_focus'
            for i in self.file_in_focus:
                yield os.path.split(i)[1]

        split_lst = [i for i in gen_split_lst()]                                    # list of only filenames (tail) of files in either of the two
                                                                                    # - 'file_in_focus' lists
        # print('split_lst', split_lst)

        def gen_split_lst():                                                        # generatore di una eventuale lista di filename (tail) duplicati
            for i in split_lst:
                if split_lst.count(i) > 1:
                    yield i

        split_duplicates = [i for i in gen_split_lst()]                             # list of duplicate filenames (tails)

        def gen_whole_duplicate():                                                  # Generates a list of all files (entire path) in the 'split_duplicates' list
                                                                                    # - of duplicate files
            for i in self.file_in_focus:
                if os.path.split(i)[1] in split_duplicates:
                    yield i

        whole_duplicate = [i for i in gen_whole_duplicate()]                        # list of all files (entire path) in the 'split_duplicates' list of duplicate
                                                                                    # - files

        whole_duplicate.sort(key=lambda x: os.path.split(x)[1])                     # list of all files (entire path) in the 'split_duplicates' list sorted
                                                                                    # - alphabetically based on filenames only

        w_dpl_dmn = {i: os.path.getsize(i) for i in gen_whole_duplicate()}          # Generates a dictionary of all duplicate files (entire path) and their size

        w_dpl_dmn_lst = [i for i in w_dpl_dmn.items()]                              # Dictionary tuple array 'w_dpl_dmn' of all duplicate files (entire path) and
                                                                                    # - their size
        # print('w_dpl_dmn_lst', w_dpl_dmn_lst)

        w_splt_mrx = []

        for i in range(len(w_dpl_dmn_lst)):                                         # array (matrix: usually it is of lists; in this case it is of lists of lists)
                                                                                    # - [[[filename, size], [path]], ... ]]] from the tuple array 'w_dpl_dmn_lst'
            w_splt_mrx.append([])
            w_splt_mrx[i].append([os.path.split(w_dpl_dmn_lst[i][0])[1], w_dpl_dmn_lst[i][1]])
            w_splt_mrx[i].append([os.path.split(w_dpl_dmn_lst[i][0])[0]])
        # print('w_splt_mrx', w_splt_mrx)

        sp_sz_lst = []

        for i in w_splt_mrx:                                                        # Array [[filename, size], ... ] from the 'w_splt_mrx' array
            sp_sz_lst.append(i[0])
        # print('sp_sz_lst', sp_sz_lst)

        sp_sz_tp_ls = []

        for i in sp_sz_lst:                                                         # filename tuple array - size, from the 'sp_sz_lst' array
            sp_sz_tp_ls.append(tuple(i))
        # print('sp_sz_tp_ls', sp_sz_tp_ls)

        dpl_sp_sz_tpl_lst = []

        unique = set(sp_sz_tp_ls)                                                   # Set of tuple array 'sp_sz_tp_ls' with elimination of any duplicates

        for i in unique:                                                            # tuple list of single files, filename -size, that have duplicates in the
                                                                                    # - filesystem ---- -point of 'culmination' of the entire program-
            count = sp_sz_tp_ls.count(i)
            if count > 1:
                dpl_sp_sz_tpl_lst.append(i)
        # print('dpl_sp_sz_tpl_lst', dpl_sp_sz_tpl_lst)

        dpl_sp_sz_lst = []

        for i in range(len(dpl_sp_sz_tpl_lst)):                                     # Array (NOT of tuples) of single files, filename - size, that have duplicates
                                                                                    # - in the filesystem
            dpl_sp_sz_lst.append([])
            dpl_sp_sz_lst[i].append(dpl_sp_sz_tpl_lst[i][0])
            dpl_sp_sz_lst[i].append(dpl_sp_sz_tpl_lst[i][1])
        # print('dpl_sp_sz_lst', dpl_sp_sz_lst)

        join_lst = []

        for i in w_splt_mrx:                                                        # list of multiple files (entire path), thus of files and their duplicates
            if i[0] in dpl_sp_sz_lst:
                join_lst.append(os.path.join(i[1][0], i[0][0]))
        # print('join_lst', join_lst)

        join_lst.sort(key=lambda x: os.path.split(x)[1])                            # list of multiple files (whole path), thus files and their duplicates, sorted
                                                                                    # - in alphabet based on filenames (tail)
        

        for i in join_lst:
            self.dupl_lst.append(i)



        '''
        mrx_str = []
        spltxt_tpl_lst = []
        spltxt_tpl_lst_mrx = []
        spl_spltxt_lst = []
        dpl_prognumeric_lst = []

        # print('est: ', len([i for i in gen_ext()]))
        '''



        ext_lst = []

        for i in inp_3_tpl:                                                         # list of extensions entered in the search
            ext_lst.append(i)



        if len(join_lst) > 0:                                                       # if the multiple-double file list is greater than 0, then it prints the number
                                                                                    # - of files in this list
            # global print_duplicate
            self.print_duplicate = len(join_lst)
            #global dpll
            #dpll = print_duplicate


            dpl_lst = []

            for i in range(len(join_lst)):                                          # Array [[integer path, filename], [], ... ] from 'join_lst'
                dpl_lst.append([])
                dpl_lst[i].append(os.path.split(join_lst[i])[1])
                dpl_lst[i].append(join_lst[i])

                dpl_lst.sort(key=lambda x: x[1])                                    # Array [[integer path, filename], [], ... ] from 'join_lst' sorted
                                                                                    # - alphabetically based on filenames (tail)
            # print('dpl_lst', dpl_lst)


            # global lsta
            for i in dpl_lst:                                                       # Array [[integer path, filename], [], ... ] from 'dpl_lst' sorted
                                                                                    # - alphabetically based on filenames (tail) looks like a copy of 'dpl_lst'
                self.lsta.append(i)
            # print('lsta', lsta)

            '''
            # global print_paths
            print_paths = lsta
            # print('print_paths', print_paths, len(print_paths))
            '''

        else:
            self.print_duplicate = 0                                                # If the list of multiple-double files is empty (0), then print '0'
            #dpll = print_duplicate
            # print('duplicati', print_duplicate)

