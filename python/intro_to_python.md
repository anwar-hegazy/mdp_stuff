# An introduction to Python

*Quick reference links*

[Homebrew](http://brew.sh/)
[iPython](http://ipython.org/)
[Pip](http://pypi.python.org/pypi/pip)
[Sublime Text 2](http://www.sublimetext.com/2)
[iTerm2](http://www.iterm2.com/) (I actually prefer this to the Mac OSX Terminal, but either is fine)

## XCode

Download, and install, Xcode from the app store (this takes forever, so please do it prior to the workshop).

You also need Apple Developer Tools (in the Mac App store) and the Command Line Developer Tools (on the Apple Developer website). Go to the [Apple Developer](https://developer.apple.com/) site and register for a free account (if you do not already have one), then search for them to download both of the aforementioned plugins.

While we are at it, go to Applications>Utilities>Terminal and run the Terminal application. We are going to be using it a lot, so I would recommend adding it to your dock for quick access.

## Homebrew
Install Homebrew by entering this into the Terminal:

```
ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
```

When it is done, you can run ```brew update``` and then ```brew doctor``` in the terminal to make sure everything is working correctly (Homebrew will tell you if not).

Additionally, you need to add the Homebrew directory to your system path. In the terminal, type ```cd``` and hit enter to go to your user directory. Now type ```nano .bash_profile``` and paste this into the file:

```
export PATH=/usr/local/bin:$PATH
```

Now restart the Terminal.

<br/><i>Python</i>
You may have noticed that there are multiple versions of Python available online (2.7.something and 3). We are going to focus on version 2.7.3, which you can easily install, via Homebrew, by typing the following into the command line:
<pre>
brew install python
</pre>
<br/>This will also install Pip, which is a great package manager specifically for Python.
<br/>After installing Python, go to your .bash_profile file and add the following:
<pre>
export PATH=/usr/local/share/python:$PATH
</pre>
<br/>To confirm that everything is in order, type <pre>which python</pre> in the Terminal and hit enter. If everything is working correctly, the Terminal will return <pre>/usr/local/bin/python</pre>.
<br/><i>everything else</i>
Okay, so now we are going to install a handful of other things that will be useful when programming in Python. They are as follows: virtualenv, virtualenvwrapper,numpy, scipy, and iPython.
<br/><i>virtualenv and virtualenvwrapper</i>
<pre>
pip install virtualenv
pip install virtualenvwrapper
</pre>
<br/><i>Numpy</i>
<pre>
pip install numpy
</pre>
<br/><i>SciPy</i>
<pre>
brew install gfortran
pip install scipy
</pre>
<br/><i>Flask</i>
<pre>
pip install Flask
</pre>
<br/><i>iPython</i>
<pre>
pip install ipython
</pre>
<br/>Finally, let's install <a href="http://opencv.willowgarage.com/wiki/Mac_OS_X_OpenCV_Port">openCV</a>:
<pre>
brew install opencv
</pre>
<br/>To test to make sure everything works, run ipython from the terminal by typing the following:
<br/>ipython
<pre>
In [1]: import cv
In [2]: cv.[tab]
</pre>
<br/>If you get a long list of methods, you did it correctly. If not, review the steps above and make sure you did not actually skip anything.
<br/>Last but not least, we are going to need access to a text editor of some sort. There are lots of options, but the two I normally recommend are <a href="http://macromates.com/">TextMate</a> or <a href="http://www.sublimetext.com/">SublimeText</a>. I use SublimeText, but you can use whatever you want. Nonetheless, you will need a text editor, that frequently will be open right next to your Terminal window, for any serious programming.
<br/><i>Intro to Python</i>
Python is a general-purpose, interpreted high-level programming language. The syntax of the language has been optimized to emphasize code readability, as well as brevity. Python supports many different programming approaches, but the one to focus on, should you choose to work with this language more thoroughly in the future, is object orientation.
<br/>Object orientation is a programming philosophy/paradigm based around objects, consisting of data fields and methods, and their interactions. The common assumption for any object is that it is capable of accepting some sort of input and producing some sort of output. Generally, one object is designed to perform a generalized, abstract function, that is context independent.
<br/>For example, a car contains a computer capable of performing a complex series of calculations during its operations. Nonetheless, we do not need to understand every single thing going on inside of the car in order to be able to effectively drive it. We simply need to know that we can change the direction of the car with the steering wheel, increase the speed of the car with the gas pedal, and decrease the speed with the brake.
<br/>Another good example of object orientation: painters do not design a new (set of) paintbrush(es), from scratch, for every single painting they create. Instead, a painter has certain paint brushes usable for a general task (for example, broad brush strokes) applicable across any painting requiring such a stroke. This is a good example of abstraction and generalization, and can become a powerful way of thinking when programming.
<br/><i>Datatypes</i>
There are a handful of datatypes in Python: strings, integers, floating point numbers, and boolean.
<br/>Strings: any character surrounded by quotes. Quotes must be balanced. In other words, I could say
<pre>a = 'this'
a = “this”
#but not:
a = 'this
#See the difference there?
</pre>
<br/>Similarly, if we are going to declare a variable as a string, we have to use quotes.
<pre>a = this
#does not work because the word this is not defined.
</pre>
<br/>Python allows for numerous manipulations to strings. More specifically, if we go back to our original example:
<pre>a = 'this'</pre>
<br/>We could use various operations on it to get various information from our variable containing the string 'this'.
<br/>For example:
<pre>In [4]: len(a)
Out[4]: 4
</pre>
<br/>We could also say:
<pre>In [5]: type(a)
Out[5]: str    # str is short for string
</pre>
<br/>Lastly, we can only return part of the string by doing the following:
<pre>In [6]: a[:3]
Out[6]: 'thi'
</pre>
<br/>Similarly, we can see what other functions are possible with a by entering this into the terminal.
<pre>a.[tab]</pre>
<br/>This is a good strategy for working with iPython in general. Any time I get a new package/module, the first thing I do (after importing it) is to type its name followed by a period and then tab.
<br/>From this list, we can type out any of the functions followed by a ? to see a brief description of what it does.
<br/>For example:
<pre>In [7]: a.upper?
Type:       builtin_function_or_method
String Form:<built-in method upper of str object at 0x104488750>
Docstring:
S.upper() -> string

Return a copy of the string S converted to uppercase.
</pre>
<br/>So let's convert our string, contained in the variable a, to an entirely capitalized version of itself. Try this:
<pre>In [8]: a.upper()
Out[8]: 'THIS'
</pre>
<br/>However, if you try this:
<pre>In [9]: a
Out[9]: 'this'
</pre>
<br/>So, if we wanted to permanently change a, we could do this:
<pre>In [10]: a = a.upper()

In [11]: a
Out[11]: 'THIS'
</pre>
<br/><i>Integers/Floats</i>
There are two basic types of numbers: integers and floating point numbers (floats for short). Integers are any whole number (positive or negative), whereas floats are any number with a decimal point. Try this:
<pre>In [12]: a = 5

In [13]: type(a)
Out[13]: int
</pre>
<br/>Whereas:
<pre>In [14]: a = 4.0

In [15]: type(a)
Out[15]: float
</pre>
<br/>If you want to, you could now enter a.[tab] to see what other methods a (the variable that now stores a floating point number [4.0]) has.
<br/>Assignment operator, more variables
In Python, = does not mean what you would normally think it does. Our previous example:
<pre>In [16]: a = 4.0</pre>
<br/>Means “assign 4.0” to the variable named a. This is why we cannot say the following:
<br/>In [17]: 5 = 6
  File "<ipython-input-17-6d9c0c29354b>", line 1
    5 = 6
SyntaxError: can't assign to literal
</pre>
<br/>So a 6 can never be assigned (or put inside) a 5, so this line of code will always throw an error.
<br/>Variables must be assigned prior to their use, otherwise python throws an error because it does not understand what you want it to do.
<br/>Try this:
<pre>In [18]: x
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-18-401b30e3b8b5> in <module>()
----> 1 x

NameError: name 'x' is not defined
</pre>
<br/>Nonetheless, variables, once assigned (and therefore established as a particular type), can be converted to other data types. For example:
<pre>In [21]: a = 5

In [22]: float(a)
Out[22]: 5.0
</pre>
<br/>Or similarly:
<pre>In [23]: a = 4.9

In [24]: int(a)
Out[24]: 4
</pre>
<br/><i>Lists</i>
A compound data type used to group together other values. A list is written as a series of comma-separated values (or items) between square brackets. They do not need to be of uniform type. For example:
<pre>In [25]: a = ['spam', 'eggs', 100, 1234]

In [26]: a
Out[26]: ['spam', 'eggs', 100, 1234]</pre>
<br/>Individual items in a list are referenced by their index, or position. We can reference individual items by enter the variable and the position (counting from 0) into the interpreter.
<br/>For example:
</pre>
In [27]: a[0]
Out[27]: 'spam'
</pre>
<pre>In [28]: a[3]
Out[28]: 1234
</pre>
<pre>In [29]: a[:2]
Out[29]: ['spam', 'eggs']</pre>
<br/>Individual items/elements in a string can be rewritten as follows:
<pre>In [30]: a[1] = 2

In [31]: a
Out[31]: ['spam', 2, 100, 1234]</pre>
<br/>If we do not happen to know how long a particular string is, we can make the interpreter figure it out be calling len() on it:
<pre>In [32]: len(a)
Out[32]: 4</pre>
<br/><i>if statements</i>
Let's take a look at a nice example of a function that contains Boolean Logic (true or false datatypes)
<pre>In [34]: x = int(input('please enter an integer: ') )
please enter an integer: 42

In [35]: if x < 0:
....: x = 0
....: print 'negative changed to zero'
....: elif x == 0:
....: print 'Zero'
....: elif x == 1:
....: print 'single'
....: else:
....: print 'more'
....:
more
</pre>
<br/>Quite a bit to talk about here. Let's break it down line by line.
We called a statement that takes any input at the command line, converts it to an int, and assigns it to the variable x. After that, we start our test. If x is less than 0, set x to 0 and print the statement 'negative changed to zero'. Elif (means else if) x RETURNS 0, print zero. Else if x returns 1, print single. If none of those things are the case (the final else), print the string more.
<br/>Before you try to type this in, notice the whitespace. Python groups statements together (in functions like this one, or otherwise) via whitespace. The normal Python protocol is to use four spaces to denote the first line belonging to a previous one (the line under the first if statement), or you can use indents.
<br/>Try to enter this into your interpreter with a different input value (not 42).
<br/><i>for statements</i>
Type this into your interpreter:
<pre>In [36]: words = ['cat', 'widow', 'defenstrate']

In [37]: for w in words:
....: print w, len(w)
....:
cat 3
widow 5
defenstrate 11</pre>
<br/>Python's for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence. So, the above function declares a list called words with three items: cat, widow, and defenestrate (all strings). Then, it says for w (used as an index here) in the list words print w (the item at that position and the length of that particular item. This is why we get the sequence of words with their string length returned. Upon completion of the for loop (when the loop has iterated over each item in the list) the loop terminates.
<br/><i>range</i>
The last built in function to be concerned with, at a basic level, is the range function. Range
generates lists containing arithmatic progressions. For example:
<pre>In [33]: range(10)
Out[33]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]</pre>
<br/>and
<pre>In [34]: range(5, 10)
Out[34]: [5, 6, 7, 8, 9]</pre>
<br/><i>Defining Functions</i>
By defining a function (using def), we can call it again for later use. For example:
<pre>In [38]: def fib(n):
....: a, b = 0, 1
....: while a< n:
....: print a,
....: a, b = b, a+b
....: </pre>
<br/>Here we actually call the function and set n, so it will print the Fibonacci series up to (in this case) 2000:
<pre>In [39]: fib( 2000 )
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597</pre>
<br/><i>Intro to openCV</i>
Let's look at some OpenCV examples together, and then next week we will transition these to video. Since a lot of the time, when programming, you will be looking for resources online to use/repurpose for your own purposes, let's do just that together with the following scripts taken from <a href="opencvpython.blogspot.com">here</a>.
<br/><a href="https://github.com/abidrahmank/OpenCV2-Python/blob/master/Official_Tutorial_Python_Codes/1_introduction/display_image.py">Display an Image</a>
<a href="https://github.com/abidrahmank/OpenCV2-Python/blob/master/Official_Tutorial_Python_Codes/1_introduction/modify_image.py">Modify an Image</a>
<a href="https://github.com/abidrahmank/OpenCV2-Python/blob/master/Official_Tutorial_Python_Codes/2_core/fiter2d.py">Filtering an Image</a>
<a href="https://github.com/abidrahmank/OpenCV2-Python/blob/master/Official_Tutorial_Python_Codes/2_core/BasicLinearTransforms.py">Linear Transform</a>
<br/>Alternately, I was just alerted to the entire sample files from the Python build of openCV <a href="https://github.com/Itseez/opencv/tree/master/samples/python2">here</a>. Monkey around with any of these things and we will delve more deeply into them at the next meeting.
<br/><i>Homework</i>
Okay, so we have learned a bunch about python, and looked at a bunch of samples for OpenCV, however all of the samples dealt strictly with static images. I would like you to try to figure out, until the next time we meet, to replace the parts of the code that deal with images to video from your webcam. How does that change the behavior of the code? Is it a smooth transition? What else can you think of changing to get more interesting results? Do not worry if you do not understand every aspect of the code, tinkering with it will give you a good idea of what (and hopefully why) things work the way they do in each file.