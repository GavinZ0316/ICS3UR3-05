# Created by: Gavin Zhou
# Created on: Oct 20 2017
# Created for: ICS3U

import ui

def calculate_touch_up_inside(sender):
    counter = 0
    count = int(view['count_textbox'].text)
    
    if count < 0:
        view['answer_label'].text = "please enter postive number!"
    elif count == 0:
        view['answer_label'].text = "1"
    else:
        factorial = counter = 1
        while (counter < count):
            counter = (counter + 1)
            factorial = counter * factorial
            view['answer_label'].text = str(factorial)

view = ui.load_view()
view.present('full_screen')

