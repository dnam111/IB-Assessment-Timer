# IB-Assessment-Timer
Introduction to the Assessment Timer
This program is a timer application built using Python, specifically an application of the Tkinter library. It provides a graphical user interface (GUI) for setting up and running a timer for various assessments or tests. Various features are included in this program. The root feature – timer – requires the user to enter the timer's duration in hours, minutes, and seconds. Simply, when the "Start Timer" button is clicked, the timer runs.

Inspiration
Since high school, I have embarked on the journey of learning various programming languages, such as Python and Java. As a sophomore at present, I intended to continue mastering Python and engage in a project that could contribute to my school. While contemplating the kind of project I wanted to undertake, a graduate friend of mine suggested the idea of developing an assessment timer. This reminded me of my own experience taking a final exam, where the school utilized a primary timer with limited functionality. I believed that there was room for improvement, which inspired the initiation of this project. Although my school has not officially endorsed the timer I created, it proved valuable and distinctive, allowing me to delve deeper into programming.

How to Use
When the timer starts, the user will see different boxes which have labels – small descriptions at the top of them. There are some boxes that are required to fill, including the three boxes under "Hour:", "Minutes:", and "Seconds:". For these boxes, the user has to input the length of the assessment: the number of hours, minutes, and seconds. The next required box is the starting timer of the assessment. This time can differ from the "Current Time" presented at the program's top. For these boxes, if the user enters nothing, the program will automatically detect the value of 0. After these inputs, the other boxes would be automatically filled through the program's calculation.

Features
The current time is shown at the top
5 minutes/10 minutes warnings are provided for friendly reminders to students
The time that the warnings would appear is included so that students can effectively distribute time on assessments questions
The test end time is automatically calculated
When the timer gets to 0, the message box pops up (all the code would stop functioning)
Details + Reminders
When the user enters nothing on the "Hour:". "Minutes:", "Seconds:", and "Test Starts at:" boxes, the program would automatically count as 0, increasing efficiency and reducing pointless user typing time
Colors are intentionally chosen as black & white so that they would not interrupt students
The total seconds can't be negative
Improvements
As a Python learner, I have discovered various modifications that can be implemented to enhance my progress. Reflecting on my journey, I identified specific areas that could benefit from improvement and implementation. First and foremost, integrating data validations into the program can significantly boost its overall performance. Considering that users might input incorrect values such as floats, negatives, strings, or non-integers, incorporating code to prevent these errors would be highly advantageous. Despite the existence of mistakes and areas for enhancement, I firmly believe this program has provided me with invaluable opportunities to enhance my Python skills. Throughout this process, I have acquired knowledge about several Python features and functions, such as applying GUI, utilizing the time library function, and working with functions within GUI, among others. Furthermore, I have also leveraged and strengthened my pre-existing Python skills. Nonetheless, I am fully aware of the program's imperfections and remain dedicated to refining it further.

Side Note
The second file uploaded is a small guide about GUI, which I learned through research. Another uploaded file is named "Timer Base" which solely includes the timer. When the user runs this file, the current time and the timer would be the only features.

To run "Timer Base", the user has to change the setting of run configuration.

In Edit Configuration menu, choose "Edit configuration templates..." at the left down corner of the menu.
Another tab would be opened.
Please choose "Python" from the side bar
Scroll down (if needed) to find the "Execution" settings.
Check the "Emulate terminal in output console"
All Set
