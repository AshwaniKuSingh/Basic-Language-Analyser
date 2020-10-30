import re
class analyser:
    #this is a class which contains methods to analyse the data obtained from cleaning transcripts from the ENNI dataset

    def __init__(self):
        self.datastats = {}
        self.datastats['Length'] = 0
        self.datastats["Vocab"] = 0
        self.datastats["Repeats"] = 0
        self.datastats["Retraces"] = 0
        self.datastats['g-errors'] = 0
        self.datastats['pauses'] = 0

    def __str__(self):
        if self.datastats["Length"] == 0:
            return "Transcript has not been analysed yet. Please select a transcript to be analysed."

        else:
            lenstr = "The length of the transcript is: "+str(self.datastats["Length"])
            vocabstr = "The size of vocabulary used: "+str(self.datastats["Vocab"])
            repeatstr = "The number of words or phrases repeated done: "+str(self.datastats["Repeats"])
            retracestr = "The number of words or phrases retraced: "+str(self.datastats["Retraces"])
            gerror = "The number of grammatical errors made: "+str(self.datastats["g-errors"])
            pausestr = "The number of pauses made: "+str(self.datastats["pauses"])

            return lenstr+"\n"+vocabstr+"\n"+repeatstr+"\n"+retracestr+"\n"+ gerror+"\n"+pausestr



    def analyse_script(self, cleaned_file):
        #cleaned_file = "SLI-1-Cleaned.txt"
        fileObj_analyse = open(cleaned_file,"r")
        fileReader = fileObj_analyse.readlines()
        numLines = []
        vocabSet = set()

        for lines in fileReader:
            lines = lines.rstrip()
            if lines.endswith("!") or lines.endswith("?") or lines.endswith("."):
                numLines.append(lines)
        #print(len(numLines))

        self.datastats['Length'] = len(numLines)

        for lines in fileReader:
            lines = lines.rstrip()
            #lines = lines.replace(".","")
            #lines = lines.replace("!","")
            #lines = lines.replace("?","")
            words = lines.split()
            for word in words:
                #print(word)
                pattern = re.compile(r"[':]")
                word = re.sub(pattern,'',word)
                if word.isalpha() and (len(word)>1 or word == "i" or word == "a"):
                    vocabSet.add(word)

        self.datastats["Vocab"] = len(vocabSet)

        fileObj_analyse = open(cleaned_file,"r")
        fileReader = fileObj_analyse.readlines()
        pattern = "[/]"
        rep_count = 0
        for lines in fileReader:
            rep_count += lines.count(pattern)

        self.datastats["Repeats"] = rep_count
        #print("Total word repetitions: ", rep_count)

        fileObj_analyse = open(cleaned_file,"r")
        fileReader = fileObj_analyse.readlines()
        pattern = "[//]"
        retr_count = 0
        for lines in fileReader:
            retr_count += lines.count(pattern)

        self.datastats["Retraces"] = retr_count
        #print("Total word retraces: ", retr_count)


        fileObj_analyse = open(cleaned_file,"r")
        fileReader = fileObj_analyse.readlines()
        pattern = "[*]"
        gerr_count = 0
        for lines in fileReader:
            gerr_count += lines.count(pattern)

        self.datastats["g-errors"] = gerr_count

        fileObj_analyse = open(cleaned_file,"r")
        fileReader = fileObj_analyse.readlines()
        pattern = "(.)"
        pause_count = 0
        for lines in fileReader:
            pause_count += lines.count(pattern)

        self.datastats["pauses"] = pause_count

        fileObj_analyse.close()

#while True:
#    opt = int(input('''
#            1. Select a transcript to analyse
#            2. Show Statistics
#            3. Exit
#            '''))
#    if opt == 1:
#        script = input("Enter the name of the file: ")
#        analObj = analyser()
#        analObj.analyse_script(script)
#    elif opt == 2:
#        print(analObj)
#        continue
#    else:
#        break
