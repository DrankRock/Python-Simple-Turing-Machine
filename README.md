# Python Simple Turing Machine
## A Python Simple Turing Machine (STM) execution simulator
![image](https://user-images.githubusercontent.com/32172257/216613057-4b1be4fd-38d2-45cd-b7fa-5ecccbe0c133.png)

### Install
```bash
$ git clone https://github.com/DrankRock/Python-Simple-Turing-Machine.git
$ cd Python-Simple-Turing-Machine
$ python3 SimpleTuring.py -h
```

### Usage
#### Arguments
```
  -h, --help            show this help message and exit
  -b BAND, --band BAND  Starting band for the program
  -i INT [INT ...], --int INT [INT ...]
                        integers to add to the band
  -s START_INDEX, --start-index START_INDEX
                        Starting index of the machine
  -p PRINT, --print PRINT
                        Print a python version of the machine, to add it in the code, line 27 and below
  -m MACHINE, --machine MACHINE
                        Use a custom machine previously added to the source code above, line 27 and below
  -d DICTIONARY [DICTIONARY ...], --dictionary DICTIONARY [DICTIONARY ...]
                        Define the dictionary (format : A B C | D )
  -t TRANSITIONS [TRANSITIONS ...], --transitions TRANSITIONS [TRANSITIONS ...]
                        Transitions (format : '<start state> <read> <action> <end state>' Example : "0 B | 1" "0 | | 0"
```

#### Example
`python main.py -t "0 | B 1" "1 B R 0" -p cleaner -i 2 3`
```
### COPY THIS IN THE BLOCK LINE 27 ###
cleaner = {
        0: [['|', 'B', 1]],
        1: [['B', 'R', 0]],
}
######################################
--------------------------------------
Welcome to Mat's Turing Machine !
Note : R is for Right, L is fort left,
B is for blank. Anything else is up to you.
I did almost no error management, sorry.
Text in green is the current index.
--------------------------------------
Starting with : 
[0] BBB|||B||||BBBB
Run ...
[1] BBBB||B||||BBBB
[2] BBBB||B||||BBBB
[3] BBBBB|B||||BBBB
[4] BBBBB|B||||BBBB
[5] BBBBBBB||||BBBB
[6] BBBBBBB||||BBBB
-----------------
End Reached
Return value :  4
Reached in 6 steps
Note : Ended because of unknown transition
```
-> Copy the top code in the block line 27 of the code   
-> run : `python main.py -m cleaner -i 2 3`
```
(...)
Starting with : 
[0] BBB|||B||||BBBB
Run ...
[1] BBBB||B||||BBBB
[2] BBBB||B||||BBBB
[3] BBBBB|B||||BBBB
[4] BBBBB|B||||BBBB
[5] BBBBBBB||||BBBB
[6] BBBBBBB||||BBBB
-----------------
End Reached
Return value :  4
Reached in 6 steps
Note : Ended because of unknown transition
```

### Contact
If you encounter any kind of problem, or to have a chat, you can contact me on Discord @`MattV#7337`
