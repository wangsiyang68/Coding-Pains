## 1.1.1 Basic Data Types: Strings

Overview:
There are *four* main basic data types in python: String, Integer, Float, Boolean

 **Strings**

- Assignment: ` string = "Doggo" `

- Operations:

  | Operation      | Valid? | Example               | Output            |
  | -------------- | ------ | --------------------- | ----------------- |
  | Addition       | Yes    | `string + string`     | `DoggoDoggo`      |
  | Subtraction    | No     | -                     | -                 |
  | Multiplication | Yes    | `string * 3`          | `DoggoDoggoDoggo` |
  | Division       | No     | -                     | -                 |
  | Equality       | Yes    | `"Doggo" = "Doggo"`   | True              |
  |                |        | `"Doggo" > "Cat"`     | True              |
  |                |        | `"Doggo" > "cat"`     | False             |
  |                |        | `"Doggo" > "Diglett"` | True              |

  **NOTE!** When comparing strings, do note that they will be compared based on the ASCII value of the first letter. Since lower case letters have a higher ASCII value than upper case letters, this results in the example shown in the 7th row in the above table.

- Methods:

  | Methods                 | Example                                   | Output            |
  | ----------------------- | ----------------------------------------- | ----------------- |
  | .upper()                | `string.upper()`                          | `"DOGGO"`         |
  | .lower()                | `string.lower()`                          | `"doggo"`         |
  | .format()               | To be elaborated further in a table below |                   |
  | **Useful for file I/O** |                                           |                   |
  | .strip()                | `" Cute Doggo ".strip()`                  | "Cute Doggo"      |
  | .split()                | `"Cute Doggo".split()`                    | ["Cute", "Doggo"] |

  .format() is a very useful method but with very unintuitive syntax. Here's a table that shows you what .format can do:

  _With Strings:_

  .format() is useful for padding strings when writing code to create a user-friendly table as output. The syntax is as follows:

  "{ index **:** padding_character align_direction maximum_number_of_padding_characters}".format(string)

  Note that none of the fields in the curly brackets are compulsory. However, given that the maximum number of padding is given and the direction is not, the interpreter will read it as aligning left, returning output such as that in the 1st row below

  | Purpose                           | Example                    | Output         |
  | --------------------------------- | -------------------------- | -------------- |
  | Align left                        | `"{:<10}".format(string)`  | `"Doggo     "` |
  | Align right                       | `"{:<10}".format(string)`  | `"     Doggo"` |
  | Align center                      | `"{:<10}".format(string)`  | `"  Doggo   "` |
  | Padding with different characters | `"{:*<10}".format(string)` | `"Doggo*****"` |

  .format() is also useful for formatting numbers!

  | Purpose                       | Example                      | Output          |
  | ----------------------------- | ---------------------------- | --------------- |
  | Rounding floats up            | `'{:.2f}'.format(3.14159)`   | `"3.14"`        |
  | Enter commas every 3 integers | `'${0:,.2f}'.format(123456)` | `"$123,456.00"` |

  Note that the '.2f' in the second row is not compulsory!

- Indexing

  Indexing (or slicing) is a key feature used in manipulation of strings. 

  The indexing of a string can be described as such:

  | 0      | 1      | 2      | 3      | 4      |
  | ------ | ------ | ------ | ------ | ------ |
  | D      | o      | g      | g      | o      |
  | **-5** | **-4** | **-3** | **-2** | **-1** |

  The syntax to slice a string is as follows:

  string[first:last:step]

  **first** refers to the first index chosen. It is inclusive of it. If not given, the string will start from the start, inclusive of the first character.

  **last** refers to the last index chosen.  It is not inclusive of it. If not given, the string will run to the end, inclusive of the last character.

  **step** refers to the increase in the pointer value. If step = 2, the pointer will select every alternate character. If step = -1, the pointer will move backwards. If not explicitly stated, step will have a value of 1

  | Purpose                                          | Example        | Output   |
  | ------------------------------------------------ | -------------- | -------- |
  | Select a character                               | `string[0]`    | `"D"`    |
  | Select a set of characters                       | `string[1:4]`  | `"ogg"`  |
  |                                                  | `string[:4]`   | `"Dogg"` |
  |                                                  | `string[1:]`   | `"oggo"` |
  | Select a character every n shifts of the pointer | `string[:2:]`  | `"dgo"`  |
  | Iterate backwards                                | `string[::-1]` | `oggoD`  |
