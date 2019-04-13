## Introduction to Basic Data Types

When we first encounter problems, it is useful to use models to help us make sense about it.  
Famous models include the AD-AS Model in Macroeconomics, Quantum Physics Model, as well as the many various models of the atom that were developed over the 20th Century.  
Abstraction is similar to these models, in the way that they provide a structure for important information pertaining to the problem to be stored and solved by manipulating it.

To better explain this, imagine that we have to implement a program that allows us to play Tic-Tac-Toe.  
One of the core questions that we have to ask ourselves, is **how are we going to represent the game?**  
There are varying levels of abstraction that we can use. Beginning from the low-level, we can use native/basic data types, such as **Strings**, **Integers**, **Floats**, **Boolean**. One may choose to represent each instance of the game in a string of 'X's and 'O's, while another may choose to store the same information in a binary number.  
Or perhaps we decided that we would need something that is more intuitive to work with -- such as a nested list of lists. A tuple in this case would not make much sense since it is non-immutable.  
Or maybe there is more information besides the 'X's and 'O's that need to be stored -- what about players' names, scores and so on? In this problem, perhaps it would be more appropriate to use a high level of abstraction, like Classes to represent the game.  

Through this chapter, I will attempt to explain what are the characteristics of each type of abstraction, as well as how to manipulate them.
