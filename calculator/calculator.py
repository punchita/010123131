############################################################

#refbyrsp
#refbychanakanblog22011999.wordpress.com

############################################################

from PySimpleGUI import *
import PySimpleGUI as sg

#color
maroon = '#800000'
green = '#5ae03a'
Teal = '#008080'
darkred = '#8B0000'
firebrick = '#B22222'
pastelyellow = '#ffff77'
darksalmon = '#E9967A'
WHITE = "#F8F8F8" 
LIGHTGREEN = "#90EE90" 

#set button position, color, font, font size 
layout = [[sg.Input(size=(30,2), do_not_clear=True, justification='right', key='input', background_color=maroon,text_color=darksalmon, font='Arial')],
            [sg.Text("0.0000", size=(25,2),justification='right', font=('Franklin Gothic Book', 20), text_color=darkred ,background_color=darksalmon, key='out')],
            [sg.Button('+', button_color=(LIGHTGREEN,green), font='Arial'), sg.Button('-', button_color=(LIGHTGREEN,green), font='Arial'), sg.Button('*', button_color=(LIGHTGREEN,green), font='Arial'), sg.Button('/', button_color=(LIGHTGREEN,green), font='Arial')],
            [sg.Button('7', button_color=(LIGHTGREEN,Teal), font='Arial'), sg.Button('8', button_color=(LIGHTGREEN,Teal), font='Arial'), sg.Button('9', button_color=(LIGHTGREEN,Teal), font='Arial'), sg.Button('C', button_color=(LIGHTGREEN,green), font='Arial')],
            [sg.Button('4', button_color=(LIGHTGREEN,Teal), font='Arial'), sg.Button('5', button_color=(LIGHTGREEN,Teal), font='Arial'), sg.Button('6', button_color=(LIGHTGREEN,Teal), font='Arial'), sg.Button('Del', button_color=(LIGHTGREEN,green), font='Arial')],
            [sg.Button('1', button_color=(LIGHTGREEN,Teal), font='Arial'), sg.Button('2', button_color=(LIGHTGREEN,Teal), font='Arial'), sg.Button('3', button_color=(LIGHTGREEN,Teal), font='Arial'), sg.Button('.', button_color=(LIGHTGREEN,green), font='Arial')],
            [sg.Button('(', button_color=(LIGHTGREEN,green), font='Arial'), sg.Button('0', button_color=(LIGHTGREEN,Teal), font='Arial'), sg.Button(')', button_color=(LIGHTGREEN,green), font='Arial'), sg.Button('=', button_color=(LIGHTGREEN,firebrick), font='Arial')],
            ]

# set screen and button size
window = sg.FlexForm('Calculator', default_button_element_size=(6,3), auto_size_buttons=False, grab_anywhere=False, background_color=maroon)
window.Layout(layout)

in_put= " "
answer = " "
while True:
    button,values = window.Read()                # read input
    # if button is None:
    #     break
    if len(in_put) >= 30:                      # set input range
        in_put = in_put[:-1]
    if button is 'C':                          # if click button C then show nothing
        in_put = " "
        answer = " "
    elif button is 'Del':                      # if click button Del then delete
        in_put = in_put[:-1]
    elif button in '1234567890':               # if click number pad then in_put add number and show number
        in_put = values['input']
        in_put += button
    elif button in  '+-*/.()':                 # if click operand pad then in_put add operand and show operand
        in_put = values['input']
        in_put += button
    elif button is '=':
        if in_put[0] == '+' or in_put[0] == '-' or in_put[0] == '*' or in_put[0] == '/':  # if at first is operand then show error
            answer = 'ERROR! Please try again..'
        elif in_put[-1] == '+' or in_put[-1] == '-' or in_put[-1] == '*' or in_put[-1] == '/': #if at last is operand then show error
            answer = 'ERROR! at the last one'
        elif '/0' in in_put:                   # if input divide by zero then shoe error
            answer = "ERROR! Can't divide by 0"
        elif '++' in in_put or '–' in in_put or '**' in in_put or '//' in in_put:  #if has operand more than 1 then show error
            answer = "Operation Error"
        elif in_put == ' ':                    # if input is blank then pass
            pass 
        else:
            in_put = values['input']
            answer = eval(in_put)
    # update input and answer on screen
    window.FindElement('out').Update(answer)
    window.FindElement('input').Update(in_put)