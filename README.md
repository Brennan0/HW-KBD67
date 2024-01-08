# HW-KBD67
## Code written for this specifically handwired KBD67 Lite keyboard. This code is the complement to firmware code from KMK (https://github.com/KMKfw/kmk_firmware/tree/master/kmk). 

This code was written for a handwired keyboard. The keyboard has the same layout as the KBD 67 Lite as the case for that specific keyboard was used for this project. 

## Controller
This keyboard used a Pi Pico but other controller boards should be usable. All you really need is enough pins on the board for a full keyboard matrix to be completed.

![IMG_0543](https://github.com/Brennan0/HW-KBD67/assets/51968218/dc2555e9-d53e-4f58-932d-53a64ac9725f)

## Figuring Out the Matrix
The matrix may differ depending on how the keyboard is wired. From the following images you can see how this keyboard was wired. The diagrams show how the mapping was made depending on the matrix. You can also see there are blank spaced as the matrix will not be a square matrix. The blank spaces will need to be taken into account when writing the code for the board.

![IMG_0032](https://github.com/Brennan0/HW-KBD67/assets/51968218/bcc17750-157e-4b1e-a7f1-205f96642640)
* I couldn't use pins 16 and 17 because resin had gotten into the holes and cured

![IMG_0033](https://github.com/Brennan0/HW-KBD67/assets/51968218/f8b8e091-676d-42ae-8064-d00ac5af5ea1)

## Final Assembly
For this board, I only used a plate and the case. There was actually no space on the plate I got for plate mounted stabilizers so I just didn't use stabilizers lol. The only major key that had a noticable impact on the missing stabilizers was the space bar. So I just put a shorter modifier as a place holder. 

![IMG_0636](https://github.com/Brennan0/HW-KBD67/assets/51968218/c182adcf-fa38-44f7-8813-c445f19a9a16)

## How to use
1. handwire your keyboard and connect Pi Pico or other controller
2. figure out matrix mapping
3. download the kmk file from KMK keyboards
4. create code for keyboard mapping
