# pataddress
![image](https://user-images.githubusercontent.com/70379302/191047720-24826764-8b76-45e2-bfb0-2156b5851079.png)

Global address in four words

https://altilunium.github.io/pataddress


## Build your own word database by using word frequency analysis
1. Copy a document to `nya`
2. Delete `nya.pickle`
3. Execute `nya.py`
4. Repeat this step until you reach at least 10.000 unique words
5. Execute `nyo.py`, configure the parameter (line 10 : maximum word length, or you can setup your own custom parameter)
6. Copy the list from `nyo.py` output to `index.html` line 132

The default word database is derived from Project Gutenberg's "The Adventures of Sherlock Holmes", "Alice's Adventures in Wonderland", and "Dracula", sorted by most frequent word.