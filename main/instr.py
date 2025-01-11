from PyQt5.QtCore import QTime

window_x, window_y = 200, 100
window_widht, window_height = 1000, 600

## MainWin class
welcome_txt = 'Welcome to the Health status detection program!'

instrunction_txt = ('This application allows you to use the Rufier test to make an initial diagnosis of your health.\n'
                   'The Rufier test is a set of physical exercises designed to assess your cardiac performance during physical exertion.\n'
                   'The subject lies in the supine position for 5 minutes and has their pulse rate measured for 15 seconds; \n'
                   'then, within 45 seconds, the subject performs 30 squats.\n'
                   'When the exercise ends, the subject lies down and their pulse is measured again for the first 15 seconds\n'
                   'and then for the last 15 seconds of the first minute of the recovery period.\n'
                   'Important! If you feel unwell during the test (dizziness,\n'
                   'tinnitus, shortness of breath, etc.), stop the test and consult a physician.' )

## TestWin class

sendresult_txt = 'Send the results'
start_test_1 = 'Start first test'
start_test_2 = 'Start doing squats'
start_test_3 = 'Start the final test'

name_txt = 'Enter Your full name:'
age_txt = 'Full years:'
time = QTime(0, 0, 15)
timer_txt = time.toString("hh:mm:ss")
test_txt_1 = '''Lie on your back and take your pulse for 15 seconds. 
    Click the "Start first test" button to start the timer.\n
    Write down the result in the appropriate field.'''
test_txt_2 = '''Perform 30 squats in 45 seconds. 
    To do this, click the "Start doing squats" button\n
    to start the squat counter.'''
test_txt_3 = '''Lie on your back and take your pulse for the first 15 seconds of the minute, 
    then for the last 15 seconds of the minute.\nPress the "Start final test" button to start the timer.\n
    The seconds that should be measured are indicated in green and the seconds that should not 
    be measured are indicated in black. Write down the results in the appropriate fields.'''

hint_test_name = 'Full name'
hint_test_age = '0'
hint_test_1 = '0'
hint_test_2 = '0'
hint_test_3 = '0'



