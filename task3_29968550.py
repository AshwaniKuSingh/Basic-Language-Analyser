from matplotlib import pyplot as plt

import numpy as np

import pandas as pd

from task2_29819253 import analyser



SLIlist = ["SLI-"]*10

TDlist = ["TD-"]*10

targetSLIlist = ["SLI-"]*10

targetTDlist = ["TD-"]*10

sourcelist = []

targetlist = []



i=1

for item in SLIlist:

    item = item+str(i)+".txt"

    i+=1

    sourcelist.append(item)

i=1

for item in TDlist:

    item = item+str(i)+".txt"

    i+=1

    sourcelist.append(item)

i=1

for item in targetSLIlist:

    item = item+str(i)+"-Cleaned.txt"

    i+=1

    targetlist.append(item)

i=1

for item in targetTDlist:

    item = item+str(i)+"-Cleaned.txt"

    i+=1

    targetlist.append(item)

target_sli = targetlist[0:10]

target_td = targetlist[10:]

AObj = analyser()

SLI_dict_length = []

SLI_dict_vocab = []

SLI_dict_repeat = []

SLI_dict_retrace = []

SLI_dict_gerr = []

SLI_dict_pause = []

for item in target_sli:

    AObj.analyse_script(item)

    SLI_dict_length.append(AObj.datastats['Length'])

    SLI_dict_vocab.append(AObj.datastats["Vocab"])

    SLI_dict_repeat.append(AObj.datastats["Repeats"])

    SLI_dict_retrace.append(AObj.datastats["Retraces"])

    SLI_dict_gerr.append(AObj.datastats["g-errors"])

    SLI_dict_pause.append(AObj.datastats["pauses"])

#global SLI_dict

SLI_dict = {'len':SLI_dict_length,

            'voc':SLI_dict_vocab,

            'rep':SLI_dict_repeat,

            'ret':SLI_dict_retrace,

            'ger':SLI_dict_gerr,

            'pau':SLI_dict_pause}

SLI_statslist = [SLI_dict['ger'], SLI_dict['len'], SLI_dict['pau'], SLI_dict['rep'], SLI_dict['ret'], SLI_dict['voc']]

BObj = analyser()

TD_dict_length = []

TD_dict_vocab = []

TD_dict_repeat = []

TD_dict_retrace = []

TD_dict_gerr = []

TD_dict_pause = []

for item in target_td:

    BObj.analyse_script(item)

    TD_dict_length.append(BObj.datastats['Length'])

    TD_dict_vocab.append(BObj.datastats["Vocab"])

    TD_dict_repeat.append(BObj.datastats["Repeats"])

    TD_dict_retrace.append(BObj.datastats["Retraces"])

    TD_dict_gerr.append(BObj.datastats["g-errors"])

    TD_dict_pause.append(BObj.datastats["pauses"])

#global TD_dict

TD_dict = {'len':TD_dict_length,

            'voc':TD_dict_vocab,

            'rep':TD_dict_repeat,

            'ret':TD_dict_retrace,

            'ger':TD_dict_gerr,

            'pau':TD_dict_pause}

TD_statslist = [TD_dict['ger'], TD_dict['len'], TD_dict['pau'], TD_dict['rep'], TD_dict['ret'], TD_dict['voc']]

class VisData:

    #this is a class that contains methods to obtain visual representations

    #of the analysis done between the two data sets



    def __init__(self,data):

        self.data = data

        self.gerr = self.data[0]

        self.len = self.data[1]

        self.pau = self.data[2]

        self.rep = self.data[3]

        self.ret = self.data[4]

        self.voc = self.data[5]

        self.avg_gerr = 0

        self.avg_len = 0

        self.avg_pau = 0

        self.avg_ret = 0

        self.avg_rep = 0

        self.avg_voc = 0

        self.datadict = {'gerr':self.gerr, 'len':self.len, 'pau':self.pau, 'rep':self.rep, 'ret':self.ret, 'voc':self.voc}

        self.df1 = pd.DataFrame(self.datadict)

    def returnDataFrame(self):

        return self.df1

    def compute_averages(self):

        mean_arr = np.array(self.gerr)

        mean_gerr = mean_arr.mean()

        self.avg_gerr = mean_gerr
        

        mean_arr = np.array(self.len)

        mean_len = mean_arr.mean()

        self.avg_len = mean_len


        mean_arr = np.array(self.pau)

        mean_pau = mean_arr.mean()

        self.avg_pau = mean_pau


        mean_arr = np.array(self.rep)

        mean_rep = mean_arr.mean()

        self.avg_rep = mean_rep


        mean_arr = np.array(self.ret)

        mean_ret = mean_arr.mean()

        self.avg_ret = mean_ret


        mean_arr = np.array(self.voc)

        mean_voc = mean_arr.mean()

        self.avg_voc = mean_voc



        #statement = "Average length of Transcript: " + str(mean_len) + "\n" + "Average Grammatical Errors: " + str(mean_gerr) + "\n" + "Average Number of Pauses: " + str(mean_pau) + "\n" + "Average Number of Repetitions of Words/Phrases: " + str(mean_rep) + "\n" + "Average Number of Words/Phrases Retraced: " + str(mean_ret) + "\n" + "Average Size of Vocabulary: " + str(mean_voc)

        #print(statement)

    def visualise_statistics(self,other):

        #meandiff_len = self.avg_len

        #meandiff_gerr = self.avg_gerr

        #meandiff_pau = self.avg_pau

        #meandiff_rep = self.avg_rep

        #meandiff_ret = self.avg_ret

        #meandiff_voc = self.avg_voc

        #return [meandiff_len, meandiff_gerr, meandiff_pau, meandiff_rep, meandiff_ret, meandiff_voc]



        stats_labels = ["Len", "Errors", "Pau", "Rep", "Retr", "Vocab"]

        x_label = "Statistics"

        y_label = "Mean Difference"

        title = "Mean difference in the statistics of SLI vs. TD measured"

        script_stats_SLI = [self.avg_len, self.avg_gerr, self.avg_pau, self.avg_rep, self.avg_ret, self.avg_voc]

        script_stats_TD = [other.avg_len, other.avg_gerr, other.avg_pau, other.avg_rep, other.avg_ret, other.avg_voc]

        ypos_SLI = np.arange(len(script_stats_SLI))

        ypos_TD = np.arange(len(script_stats_TD))

        plt.xticks(ypos_SLI,stats_labels)

        plt.xticks(ypos_TD,stats_labels)

        plt.xlabel(x_label)

        plt.ylabel(y_label)

        plt.title(title)

        plt.bar(ypos_SLI+0,script_stats_SLI, color = 'r',label = "SLI",width=0.4)

        plt.bar(ypos_SLI+0.4,script_stats_TD, color = 'g', label = "TD", width = 0.4)

        plt.legend()

        plt.show()



visualiserObj_TD = VisData(TD_statslist)

visualiserObj_SLI = VisData(SLI_statslist)



visualiserObj_TD.compute_averages()

visualiserObj_SLI.compute_averages()



df1 = visualiserObj_TD.returnDataFrame()

df2 = visualiserObj_SLI.returnDataFrame()



print("\nTD Statistics Data Frame\n")

print(df1)

print("\nSLI Statistics Data Frame\n")

print(df2)



visualiserObj_SLI.visualise_statistics(visualiserObj_TD)

