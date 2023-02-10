# Python Simple Turing Machine
## A Python Simple Turing Machine (STM) execution simulator
![image](https://user-images.githubusercontent.com/32172257/216613057-4b1be4fd-38d2-45cd-b7fa-5ecccbe0c133.png)

## Install
```bash
$ git clone https://github.com/DrankRock/Python-Simple-Turing-Machine.git
$ cd Python-Simple-Turing-Machine
$ python3 SimpleTuring.py -h
```

## Usage
### Arguments
#### -h, --help
```
usage: SimpleTuring.py [-h] [-b BAND] [-c COLORS [COLORS ...]] [-di] [-ds DISPLAY_SLEEP] [-es END_SYMBOLS [END_SYMBOLS ...]] [-i INT [INT ...]] [-m MACHINE] [-nb N_BANDS] [-nu N_UPLET] [-p PRINT]
                       [-ph] [-si START_INDEX] [-t TRANSITIONS [TRANSITIONS ...]]

options:
  -h, --help            show this help message and exit
  -b BAND, --band BAND  Starting band for the program
  -c COLORS [COLORS ...], --colors COLORS [COLORS ...]
                        Specify a color for a character ( -c B red ). l to list colors
  -di, --display-inline
                        Display the current line inline
  -ds DISPLAY_SLEEP, --display-sleep DISPLAY_SLEEP
                        sleep n milliseconds between each step
  -es END_SYMBOLS [END_SYMBOLS ...], --end-symbols END_SYMBOLS [END_SYMBOLS ...]
                        Specify the symbols to count after ending. Format : -es Y S
  -i INT [INT ...], --int INT [INT ...]
                        integers to add to the band
  -m MACHINE, --machine MACHINE
                        Use a custom machine previously added to the source code above, line 27 and below
  -nb N_BANDS, --n-bands N_BANDS
                        Specify the number of bands (default : 1, min : 1)
  -nu N_UPLET, --n-uplet N_UPLET
                        Specify the accepted n-uplet (default : 4, min : 4)
  -p PRINT, --print PRINT
                        Print a python version of the machine, to add it in the code, line 27 and below
  -ph, --print-human    Print the current machine as a human readable format
  -si START_INDEX, --start-index START_INDEX
                        Starting index of the machine
  -t TRANSITIONS [TRANSITIONS ...], --transitions TRANSITIONS [TRANSITIONS ...]
                        Transitions (format : '<start state> <read> <action> <end state>' Example : "0 B | 1" "0 | | 0"


```
#### -b, --band
Specify a custom band.   
`python SimpleTuring.py -m cleaner -b "BBB|||||This is a custom band"`  
![Screenshot from 2023-02-10 07-13-09](https://user-images.githubusercontent.com/32172257/218017046-89079986-14b0-493b-b0bb-6c45b2365ef0.png)

#### -c, --colors
Specify a custom color/effect/background for any character  
`python SimpleTuring.py -c l`  
![image](https://user-images.githubusercontent.com/32172257/218018586-ae725f9b-15ce-4bf2-bd11-6cb5099b18b3.png)
`python SimpleTuring.py -m cleaner -b "BBB|||||This is a custom band" -c \| yellow B red`  
![image](https://user-images.githubusercontent.com/32172257/218018816-9994f212-fbc0-40b7-b12d-4495be905d3c.png)

#### -di, --display-inline
Print every step on top of each other instead of the one after the other.   
`python SimpleTuring.py -m cleaner -i 1 2 -di`  
![image](https://user-images.githubusercontent.com/32172257/218019723-ca4291ab-993a-4acd-a24d-6393c10641c6.png)

#### -ds, --display-sleep
Set a delay in milliseconds between each step. Especially useful with `--display-inline`, to see the steps happen.  
`python SimpleTuring.py -m cleaner -i 4 3 -di -ds 500`  
![display-sleep](https://user-images.githubusercontent.com/32172257/218020849-757a871c-9bd3-4beb-82ec-3300c0652a79.gif)



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
Note : R is for Right, L is for left,
B is for blank. | is for unary
Anything else is up to you.
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
