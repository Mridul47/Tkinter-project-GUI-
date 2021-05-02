# Building a simple Calculator
Calculator related project:

First of all, I designed the layout using tkinter for the design of my calculator. I imported tkinter using tkinter import.
Then I made a root window then, I placed some configuration and for that I placed the required size using root geometry
and kept the value according to my preferences. Then to prevent the resizable I kept root.resizable(0,0) so that my calculator 
app neither get full screned or the size could be changed by the user. Then I kept the main loop.
Then I started working on simple customization for my calculator app by keeping name as "Galactico's Calculator"

And now I placed a frame(to place all the button required in a calculator and in the correct order).
Here I'm going to make four rows and 4 columns for my calculator. And for making that, I firstly used
"buttonrow1" as my first frame. Then i stored frame for the root and also placed a colour based on my preference.
 Then i used pack geometry manager where I passed the parameters in that pack to expand and fill. Then i did the same for the
 remaining rows.(i.e. upto buttonrow4). Now for an individual buttonrow I have created four buttons and will do thwe same for the rest of 
 the buttonrows. And while creating the button in buttonrow1. For that i named a button as button1. And now the parent element isnt a root window now
 it will be inside buttonrow1. Then I gave a simple text as "1" then i gave a font as "Yu Gothic UI Semibold".(you can keep any font you want). Then i kept the required font size.
 Then I concenterated on the placement. And for that I used button1.pack and stored left side and then I wanted button to expand and for that i used expand=true the i want the button to be filled 
 from both sides so i did fill=both. And did same for the all the button (i.e.upto button4).
 
 And for now on the top of the buttonrows, I kept label as lbl. where its parent element is root.
 Then I kept the text as "Label". Then i placed anchor property. Anchor explains where the text should be placed.
 and I placed the text "Label" in southwest and denoted as "SE". Then I used label pack where I stored the expand and fill command.
 As I want it to expand and fill from both sides and for that I kept expand=True and fill=Both.
 Now we already have four button rows for the buttons. And I copied the buttons of buttonrow 1 and pasted 3 more times and edited a bit by changing the buttonrow and the name of the buttons and also the text required inside the button manually.
 Then I did the further customization and to remove the border to make it more appealing, I just inserted 
 Relief command and kept "GROOVE" inside it and keot "Border = 0". Then I did same for every buttons present in
 every buttonrow that I created. And by doing this I completed the perfect layout for my calculator.
 
 And now its time for my calculator to actually work and respond the every command our user enters in my calculator.
And for that I firstly started with my label to give it some more properties, and for that firstly I have to give my label a Text variable
and I kept data as the variable name which will work as a string variable. Then our text variable will be equal to the data.
Then I made my background full white and foreground as a black and now our calculator distinguishes label and button colours differently.
Now I want my calculator screen to respond the user's input(i.e. if user clicks 1 then 1 should be displayed on the screen)
And to make it function well, I used def function as "def button_1_isclicked():".And I kept value which connects to older value and also concaginated with 1.
And then I again use def function and this time as "def button_2_isclicked():".Then this time i kept value which connects to older value and also concaginated with 2.
And I did same on remaining buttons from 3 to 0. Since the calculator only takes one keyword (i.e. 1,2 or any one num). And to make calculator to take multiple number at same time,
we take a value and we taken it as globally where it contain empty strings(i.e. "") To ensure that our data has been contagneted either its 1 or 2 or any numbers that should be done in this specific variable. WE also have to say
our function that that value is a "global value". Now for setting the value we use (data.set(val)) and should be kept in all "button_isclicked()) portion. And for that we also have tell every individual buttons that the command "Button_isclicked()) function according to the button numbers.


Now to make the operants like "+", "-", "/" and "*" work. We take random value as A an we place "0" inside A so that A becomes integer and also it initialises A with 0 so that we dont get 
some random values in it. Lets keep any one of the operator lets say we keep "+" and then i again used def funcyion as button_plus_clicked(): then storing global A,global operator and global variable. Then, putting integer value and storing it in A. and using the "+" operator sign where value= value + "+"
then setting data in data.set(val). And doing same in "-" , "/" and "*" and just changing the operator sign and doing in same way while keeping integers and global value.
then letting buttonplus, buttonminus, buttonmul and buttondiv know about the command we just entered and editing the way according to the operator.


Now again using def function for C(clear key) as def button_c_isclicked then storing the required global values like we did in operants like "+", "-", "/" and "*"
and the data in value be null.(i.e. val = "") and A=0 and operator also is empty. then setting the data value as data.set(val)
and now letting button nc be  known by running the command function.

Lastly for result(i.e. =) to work. we have to use def function as def result(): and putting the global A, operator and value.
taling another value as val 2 then storing val 1 in val 2 as val2=val. and now using if operator =="+". WE got every data in val2 from label.
So we split the data of val2 in the respected + opearnt where we want 1st index storing as an integer naming as x.
Now we will take third variable as "C" which work for this function and storing the A and X value in it.
now setting the result of C as data.set(C). Now letting buttonequal know by putting command=result.
Now when we perform twice input result then it shows error so to fix that error. We put value in string(c) inside def result. Now doing same in if operator of -,/,* just putting required sign in split.
but for / we have to put second value as "if x ==0:" so that, it shows error while user mistakely divides something with 0. And the error message that i kept is
messagebox.showerror("Error","Division by 0 is not supported"). And for that we should blank A,val variable, data.set(val) and if the user doesnt do such mistakes then 
by keeping else where integer(A/x) is stored in C. and putting data.set(C) and putting value as an string.
And to let user know about error message I again went at the beginning line then i imported messagebox from tkinter.
Then, I kept logo from my calculator using root.iconbitmap command below my calculator name.

And in this way i completed my calculator programming using tkinter.
