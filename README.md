# Basic-Language-Analyser

A basic language analyser to investigate the linguistic characteristics of children with some form of language disorders. The analyser is able to perform basic statistical analysis on a number of linguistic features and also analysis results is presented using visualisation.

There are two datasets. The dataset is known as ENNI [https://childes.talkbank.org/access/Clinical-MOR/ ENNI.html] which is a collection of narrative transcripts gathered for a clinical study carried out in Alberta, Canada, to study children with language disorders. Two sets of data were collected: the first set is from children diagnosed with Specific Language Impairment (SLI) — one form of language disorders; and the second set is from children with the typical development (TD). A subset of the original corpus is used in this assignment with 10 selected transcripts for each group of children.

A more deatiled description of the assignment is available [here](https://github.com/AshwaniKuSingh/Basic-Language-Analyser/blob/master/FIT9133-Assign-02%20.pdf)

## The assignment consists of three tasks

**Task 1: Handling with File Contents and Preprocessing**

This task required to conduct a number of pre-processing or filtering tasks to extract only the relevant contents or texts needed for analysis in the subsequent tasks.

The notebook for task one [Task 1](https://github.com/AshwaniKuSingh/Basic-Language-Analyser/blob/master/task1_29968550.py)

**Task 2: Building a class for Daa Analysis**

The second task is about collating the required data for analysis. The main task is to produce a number of statistics for the two groups of children transcripts. These statistics are those that might serve as good indicators for distinguishing between the children with SLI and the typically developed (TD) children.

The statistics for each of child transcript that we are interested in are:

• Length of the transcript — indicated by the number of statements<br>
• Size of the vocabulary — indicated by the number of unique words<br>
• Number of repetition for certain words or phrases — indicated by the CHAT symbol [/] <br>
• Number of retracing for certain words or phrases — indicated by the CHAT symbol [//]<br>
• Number of grammatical errors detected — indicated by the CHAT symbol [*]<br>
• Number of pauses made — indicated by the CHAT symbol (.)<br>

The notebook for task one [Task 2](https://github.com/AshwaniKuSingh/Basic-Language-Analyser/blob/master/task2_29968550.py)

**Task 3: Building a class for Data Visualisation**

The last task is about implementing a class to visualise the statistics collected in Section Task 2 as some form of graphs. The visualiser class is implemented using some of the external Python packages, such as **NumPy**, **SciPy**, **Pandas**, and/or **Matplotlib** in order to create the suitable graphs for comparing the statistics collected for the two groups of children transcripts. 

The notebook for task one [Task 3](https://github.com/AshwaniKuSingh/Basic-Language-Analyser/blob/master/task3_29968550.py)
