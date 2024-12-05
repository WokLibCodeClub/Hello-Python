# Age Calculator

In this step we'll write a simple programme to calculate someone's age if you know their year of birth. (OK, I know you don't really need a computer to do this, but it will help to show some important ways that Python carries out certain tasks.)

Have your "first ever Python code" (from step 1) open in a browser window. You will also find it useful to have the [Interactive Python Console](https://trinket.io/console) open in another tab of your browser.

## input()

Before we go on let's introduce another important Python function: ```input()``` which is used to get information from the computer user.

You can try this out in your "first ever Python code" project. Type

``` python
input("What's your name?")
```

and click on Run. In the results panel you will see it has printed **What's your name?** and after that is a flashing black rectangle. That means the code is waiting for you to type in something into the results panel. But before you start to type ***CLICK YOUR MOUSE ONCE INSIDE THE RESULTS PANEL***. This is to shift the *focus* of trinket to the results panel. If start typing without doing this, trinket will assume you are still editing your code, so whatever you type will appear in the code and will probably cause an error. You can easily remove anything you typed by accident in the code using the keys Cntl-Z, for *undo*.

The phrase inside the brackets in the ```input()``` function is called a *prompt string*.

(Did you notice the *double* quotes around the prompt string above? Python lets you use single *or* double quotes for a text string, but in this case the string includes an apostrophe in the word **What's**. If you tried to use single quotes Python would think the apostrophe was another single quote mark which would indicate the end of the string.)

When you put ```input("What's your name?")``` in your code, and then type in something in the results panel nothing much happens, as the information you typed vanishes. The usual way to save this information is to put it into a *variable*, which you would do with code like this:

``` python
myname = input("What's your name?")
```

Now, whatever you type into the results panel is saved in a variable called ```myname``` and you can print it, or use it in other ways. You could add this line:

``` python
print("Hello", myname)
```

which would print **Hello** followed by what you typed.

## A New Project

We're ready to code our *Age Calculator* programme, so start a new trinket project, following the instructions [here](../trinket_basics/using_trinket.md#starting-a-new-trinket-project). You could call your project "Age Calculator".

Don't forget to add the first line of code in your new project:

``` python
#!/bin/python3
```

If we want to calculate someone's age, we first need to know what year they were born. Write code, using the ```input()``` function and a variable to ask the user to type in the year they were born.

<details><summary>Hint</summary>

<p></p>
This is an example of code which will work:

``` python
born = input('What year were you born? ')
```

<p></p>

</details>

The next thing we need is what year it is today. We could put this in a variable called ```this_year```:

``` python
this_year = 
```

where you have to add the correct year after the *equals* sign.

Calculating someone's age is a simple subtraction sum. Add this line of code to subtract one variable from another:

``` python
age = this_year - born
```

If you didn't call your variable ```born``` then use your variable name instead.

This line is supposed to calculate the person's age, but our code won't tell us the answer unless we *print* it. So add another line

``` python
print(age)
```

Click Run and see what happens. Oh no - there's an error. You can seen that the last line you typed is highlighted in red, and at the bottom of the editing panel is a message:

![Type Error](type_error.png)

## Types of Python objects

We've run into a problem concerned with the way the ```input()``` function works.

In step 1 we mentioned that numbers and text strings are two different types of Python *object*. It is a feature of the ```input()``` function that whatever you type as your response, *even if it's a number*, the function treats it as a text string. This means that our variable ```born``` (or whatever name you used) will be a *text* type of object, even though the person typed in a number.

You can check this using another Python function called ```type()```, which simply tells you the type of whatever object you put inside the brackets.

Add a line of code just after your ```input()``` line:

``` python
print(type(born))
```

(use your own variable name) and you will see it prints

```<class 'str'>```

which tells you that this variable is of type ```'str'``` which is short for *string*.

### Conversion of an object from one type to another

Luckily there are functions which convert the type of a Python object, so to run our code we need to *convert* our "year born" variable from type ```'str'``` to be an integer. We can do this using the ```int()``` function. Put this line of code after the line with ```type()```:

``` python
born = int(born)
```

This takes the variable born, converts it to integer type and puts the result back into the variable born.

Repeat the line with the ```type()``` function after this conversion, and when you run the code you will see

- that the variable has changed from type ```<class 'str'>``` to ```<class 'int'>```

- the code now runs without an error!

## Does the code always give the right answer?

The last thing printed is the computer's calculation of the person's age. But *sometimes it gives the wrong answer!* This happens if the person hasn't yet had a birthday this year, which means the computer calculates an age which is one too large.

When you're ready, go on to [the next step](../step3/step3.md) and start learning Python graphics!

Back to [previous step](../step1/step1.md).
