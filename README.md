# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

It is a simple Python program to print stats about a book. For Mary Shelley's _Frankenstein_, the output looks like this:

```
--- Begin report of books/frankenstein.txt ---
75767 words found in the document


The 'e' was found 44538 times
The 't' was found 29493 times
The 'a' was found 25894 times
The 'o' was found 24494 times
The 'i' was found 23927 times
The 'n' was found 23643 times
The 's' was found 20360 times
The 'r' was found 20079 times
The 'h' was found 19176 times
The 'd' was found 16318 times
The 'l' was found 12306 times
The 'm' was found 10206 times
The 'u' was found 10111 times
The 'c' was found 9011 times
The 'f' was found 8451 times
The 'y' was found 7756 times
The 'w' was found 7450 times
The 'p' was found 5952 times
The 'g' was found 5795 times
The 'b' was found 4868 times
The 'v' was found 3737 times
The 'k' was found 1661 times
The 'x' was found 691 times
The 'j' was found 497 times
The 'q' was found 325 times
The 'z' was found 235 times
The 'æ' was found 28 times
The 'â' was found 8 times
The 'ê' was found 7 times
The 'ë' was found 2 times
The 'ô' was found 1 times
--- End report ---
```

To use it, create a `books` directory in the root of the project and add a book in a text file in that folder. You can get books from [Project Gutenberg](https://www.gutenberg.org/) for example. 
Then, run 

```bash
python3 main.py
```