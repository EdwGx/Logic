Logic
=====
Open Source [Logic Gate](http://en.wikipedia.org/wiki/Logic_gate) Simulator With [Pygame](http://www.pygame.org/wiki/about)

How to install?
--------------------
1.Download python from [python.org](http://www.python.org/download/) and install python 3.3 (Windows) or 2.7 (OS X).      
       
2.Download and install [pygame](http://www.pygame.org/download.shtml). 
      
3.Run the main.py in python with pygame.

Example
--------
###1-Bit Full Adder
![alt tag](http://i.imgur.com/yMtgiHK.png)    
   
Plan Features
-------------
* Drag multiple items at once
* Move items in larger map `in progress`
* Zoom in and zoom out
* ~~Save&Load menu~~
* ~~Save and Load~~
* ~~Better logic gates images~~
* ~~Labels on sidebar~~
* ~~Add logic gates freely~~   
* ~~Add wires freely~~ 
* ~~More Input Devices (Switch and Button)~~
* ~~More Output Devices  (light bulb)~~
* Make an object-c app with SpriteKit  

Save File
---------
| 0    | 1 | 2 | 3      | 4                 | ...                       | ...                     |
|:----:|:-:|:-:|:------:|:-----------------:|:-------------------------:|:-----------------------:|
| Type | X | Y | Status | Number of In Port | Connect Module (Port ...) | Connect Port (Port ...) |


The Truth Table of Logic Gates
------------------------------
###AND Gate   

| A | B | Out |
|---|---|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

###OR Gate   

| A | B | Out |
|---|---|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

###XOR Gate   

| A | B | Out |
|---|---|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

###NOT Gate   

| A | Out |
|---|:-:|
| 0 | 1 |
| 1 | 0 |

###NAND Gate   

| A | B | Out |
|---|---|:-:|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

###NOR Gate   

| A | B | Out |
|---|---|:-:|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

###XNOR Gate   

| A | B | Out |
|---|---|:-:|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |
