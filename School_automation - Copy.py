import schedule
import time
import webbrowser
import keyboard

#Input your url's here for your classes
url1 = "First url"
url2 = "Second url"
url3 = "Third url"
url4 = "Fourth url"
url5 = "Fifth url"
url6 = "Sixth url"
url7 = "Seventh url"
url8 = "Eighth url"
url9 = "Ninth url"
url10 = "Tenth url"

#If the format doesn't match your schedule your going to have to manually change it
#Input the names of your classes
def first_class_A():
    webbrowser.open_new_tab(url1)

def second_class_A():
    webbrowser.open_new_tab(url2)

def third_class_A():
    webbrowser.open_new_tab(url3)

def fourth_class_A():
    webbrowser.open_new_tab(url4)

def fifth_class_A():
    webbrowser.open_new_tab(url5)

#make sure that you are on the url you want to close before the end or else it will close out of whatever tab you're on
def end_of_day():
    keyboard.press_and_release('ctrl+w')
    print("Your all done for the day")
    
def first_class_B():
    webbrowser.open_new_tab(url6)

def second_class_B():
    webbrowser.open_new_tab(url7)

def third_class_B():
    webbrowser.open_new_tab(url8)

def fourth_class_B():
    webbrowser.open_new_tab(url9)

def fifth_class_B():
    webbrowser.open_new_tab(url10)

def end_of_day():
    keyboard.press_and_release('ctrl+w')
    print("Your all done for the day")

#If your classes switch on wednesday's, copy and paste the amount of classes and match up each class to their url
#You will have to match your corresponding url number to each of the classes for wednesday

#def first_class_wednesday_A():
    #webbrowser.open_new_tab(Corresponding url)

#def second_class_wednesday_A():
#    webbrowser.open_new_tab(Corresponding url)

#def third_class_wednesday_A():
#    webbrowser.open_new_tab(Corresponding url)

#def fourth_class_wednesday_A():
#    webbrowser.open_new_tab(Corresponding url)

#def fifth_class_wednesday_A():
#    webbrowser.open_new_tab(Corresponding url)

#def end_of_day():
#    keyboard.press_and_release('ctrl+w')
#    print("Your all done for the day")

#def first_class_wednesday_B():
    #webbrowser.open_new_tab(Corresponding url)

#def second_class_wednesday_B():
#    webbrowser.open_new_tab(Corresponding url)

#def third_class_wednesday_B():
#    webbrowser.open_new_tab(Corresponding url)

#def fourth_class_wednesday_B():
#    webbrowser.open_new_tab(Corresponding url)

#def fifth_class_wednesday_B():
#    webbrowser.open_new_tab(Corresponding url)

#def end_of_day():
#    keyboard.press_and_release('ctrl+w')
#    print("Your all done for the day")


#Add in the time you would like the script to open up your link
schedule.every().monday.at('Start time').do(first_class_A)
schedule.every().monday.at('Start time').do(second_class_A)
schedule.every().monday.at('Start time').do(third_class_A)
schedule.every().monday.at('Start time').do(fourth_class_A)
schedule.every().monday.at('Start time').do(fifth_class_A)
schedule.every().monday.at('Start time').do(end_of_day)

schedule.every().tuesday.at('Start time').do(first_class_B)
schedule.every().tuesday.at('Start time').do(second_class_B)
schedule.every().tuesday.at('Start time').do(third_class_B)
schedule.every().tuesday.at('Start time').do(fourth_class_B)
schedule.every().tuesday.at('Start time').do(fifth_class_B)
schedule.every().tuesday.at('Start time').do(end_of_day)

#If your classes switch on wednesday's, then uncomment out the next section

#schedule.every().wednesday.at('Start time').do(first_class_wednesday_A)
#schedule.every().wednesday.at('Start time').do(second_class_wednesday_A)
#schedule.every().wednesday.at('Start time').do(third_class_wednesday_A)
#schedule.every().wednesday.at('Start time').do(fourth_class_wednesday_A)
#schedule.every().wednesday.at('Start time').do(fifth_class_wednesday_A)
#schedule.every().wednesday.at('Start time').do(end_of_day)

#schedule.every().wednesday.at('Start time').do(first_class_wednesday_B)
#schedule.every().wednesday.at('Start time').do(second_class_wednesday_B)
#schedule.every().wednesday.at('Start time').do(third_class_wednesday_B)
#schedule.every().wednesday.at('Start time').do(fourth_class_wednesday_B)
#schedule.every().wednesday.at('Start time').do(fifth_class_wednesday_B)
#schedule.every().wednesday.at('Start time').do(end_of_day)

schedule.every().thursday.at('Start time').do(first_class_A)
schedule.every().thursday.at('Start time').do(second_class_A)
schedule.every().thursday.at('Start time').do(third_class_A)
schedule.every().thursday.at('Start time').do(fourth_class_A)
schedule.every().thursday.at('Start time').do(fifth_class_A)
schedule.every().thursday.at('Start time').do(end_of_day)

schedule.every().friday.at('Start time').do(first_class_B)
schedule.every().friday.at('Start time').do(second_class_B)
schedule.every().friday.at('Start time').do(third_class_B)
schedule.every().friday.at('Start time').do(fourth_class_B)
schedule.every().friday.at('Start time').do(fifth_class_B)
schedule.every().friday.at('Start time').do(end_of_day)

while True:
    schedule.run_pending()
    time.sleep(1)