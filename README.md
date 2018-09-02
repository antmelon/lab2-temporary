#### CS 110 - Fall 2018
# Lab 2 - Python Data
## Due Date: 5:00 p.m., September 6th, 2018

*All programs will be tested on the machines in the LNG103 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files

* lab2.py

### Grading Rubric

**_TOTAL: 15 points_**
* **Part A: 10 points**
   * prints value and type of each variable as specified (2 pts)
   * requests input from user rather than hard coded values (3 pts)
   * adds request for how many classes per week (3 pts)
   * correctly calculates cost per class (2 pts)
* **Part B: 4 points**
   * os module imported correctly (2 pts)
   * each commands man page is displayed (2 pts)
* **Part C: 1 point**
    * Follows requested project structure and submission format

### Guidelines

This is an individual lab assignment. You must do the vast majority of the work on your own. It is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically *to* solve the problem you have been given, and you may not have anyone else help you write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

***

_In this lab, you will learn to_:

* Use python data
* Use python modules

| | Meaning |
|:----:|---------|
| :bulb: | Tips and useful information |
| :warning: | Caution! This could cause you problems. |
| :no_entry_sign: | Danger! Don't do this! |

## Part A: User Input

For this lab we are going to work with python data and user input. A few notes before we get started. In our class:
* Complete programs will always be written in Python scripts
* Complete programs will have a **main()** function
* Complete programs will include an invocation of the **main()** function
* Each complete program will be saved in a separate file given a **camelCaseName** followed by a **.py** extension (e.g., **computeAverageProfit.py**)
    * :no_entry_sign: *Note that file names should NEVER contain spaces*

If you are not already familiar with a linux editor, please use gedit, which has several nice features for Python code development.

:warning: Beware that gedit is a linux editor, and will not work on other OS's (Windows, Mac, etc.).

You can use gedit to open a file by typing, for example, the following into a linux command shell:

`gedit lab2.py &`

If there is no file in the current folder named *lab2.py*, then gedit will create a new empty one for you (remember, you can check your current folder location with `pwd`). If the file does exist, it will edit the existing file.

:bulb: The ampersand at the end of the command says to run this application in the background. This will allows you to write some code, save it, then run it in the shell without quitting gedit.

After making changes to a file, you can save it by clicking "Save" at the top of the gedit window, or with the hot key command `<ctrl-s>`. Note that if you have made changes to an open file, and those changes have not been saved, the file name across the top of the window will be preceded by an asterisk (for example, "\*lab2.py"). To exit from gedit, make sure your modifications are saved, and then type `<ctrl-q>` in the gedit window, or simply close the gedit window by clicking the “x” in the upper right hand corner.

Open the accompanying *lab2.py* simple program with gedit. You must keep the format, indentation, and capitalization EXACTLY as it is!

* First run the program by typing the following command into the terminal: `python3 lab2.py`
* Next, using the code I have given you as an example, make the following changes to the code:
    * The `main()` function starts with the line `def main():`. After each variable assigned to inside the `main()` function, insert a print statement that prints both the value *and* the type of the variable __in a single print statement__
        * :bulb: You should use spaces, not tabs, to indent when writing your own code. Spaces are more cross platform compatible when switching between linux and Windows. To make thing easier, most editors have an option in preferences to convert tabs into spaces.
    * Alter the code to ask for user input for the 3 variables (_weeks, classes, tuition_) rather than using **hard coded numbers**
        * A *hard coded number* is when you write a value in your code rather than calculating it or reading it from input.
        * :warning: Don’t forget to convert the input from the user to an `int`. Notice that you will always have to convert input from text to a number to perform arithmetic operations with it. Ensure you make this conversion by following the example provided in class.
    * Add code that asks the user to input how many times per week a class meets and save that in a variable called `classes_per_week`.
        * For example, our class meets 2 days a week
    * Calculate the cost per class by dividing the `cost_per_week` by the `classes_per_week` and save the result in a variable called `cost_per_class`
    * Print the `cost_per_class` to the console with a nice message
        * :bulb: try to figure out the syntax of this based on the syntax and behavior of the rest of your program
* Save your program, run it, and debug if necessary

__Show the CA your code.__

__--END OF IN LAB REQUIRED WORK--__

_You may continue to work on the remainder of the lab on your own time or in lab_

## Part B: Modules
Before we continue writing code for this lab, we need to introduce Python modules.
Modules allow us to use additional Python library code to quickly accomplish complex tasks.
There are lots of different modules we will be using over the course of the semester. One module that
you will find useful is called `os`. The [Operating System](https://docs.python.org/3/library/os.html)
module allows python to execute operating system level commands. Add the following
to the top of your _lab2.py_ script:
```python
import os
```
You can now run terminal commands from within Python scripts with the command:
```python
    os.system("<command>")
```
For example, if I wanted to print out the folder contents, I could call:
```python
    os.system("ls").
```
Write code to print out the man page for each of the commands you looked up in lab 1:
* man
* cat
* pwd
* mkdir
* rm
* cd
* ls
* mv
* cp
* python3

:warning: Remember, you are not just executing these commands, but displaying the man pages for them

:bulb: When you run the code for testing, you will have to type ‘q’ after each command to move onto the next one

:bulb: If you get ‘no manual entry’ for some of the commands, that’s okay

:no_entry_sign: These commands will not work on a Windows machine

## Part C : Code Organization and Submission
* Required code organization:
   * lab2.py

Below is just a reminder of the commands you should use to submit your code. If you cannot remember the exact process, please review Lab 1.

*These commands all presume that your current working directory is within the directory tracked by `git`.*

You will need to do the following when your submission is ready for grading.

```shell
git commit --allow-empty -m "final commit"
git push
```

To complete your submission, you must copy and paste the commit hash into MyCourses. Go to MyCourses, select CS110, and then assignments. Select Lab 2, and where it says text submission, paste your commit hash. You can get your latest commit hash with the following command:

```shell
git rev-parse HEAD
```    

:warning: Remember, you __MUST__ make a submission on mycourses before the deadline to be considered on time.
# lab2-temporary
