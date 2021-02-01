## Introduction
A fun little password manager I've made for fun. It is also functional!

The main program to run is manager.py. Using it should be pretty self explanatory; it uses a basic text menu UI for use of the manager. Simply enter the number of the item you want to use and it should run the correct code selected.

## passwordLib.py
---
**requires btecKey.py**

* **generate()**

_params: none_

returns a random set of characters based of settings in *genSettings.txt*.

* **settingsChange**
_params: none_

Gives a text UI menu for all the possible edits to *genSettings.txt*.
