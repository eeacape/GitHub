import random
import sys
'''
import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
'''

'''
class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        self.title = ("My Pong App")
        return PongGame()
'''
'''
class LoginScreen(GridLayout):
    
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Customer Name:'))
        self.cname = TextInput(multiline=False)
        self.add_widget(self.cname)
        self.add_widget(Label(text='Account Name (Salesforce format):'))
        self.accid = TextInput(multiline=False)
        self.add_widget(self.accid)
        self.add_widget(Label(text='Contact Id (Salesforce format):'))
        self.contid = TextInput(multiline=False)
        self.add_widget(self.contid)
'''     
        
'''
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.add_widget(Label(text='Domain Name'))
        self.domain = TextInput(multiline=False)
        self.add_widget(self.domain)
'''
'''
class MyApp(App):

    def build(self):
        self.title = 'My Wonderful App'
        #return LoginScreen()
        #self.title = 'My Wonderful App'
        #self.icon = 'myicon.gif'
        return(Label(text="Hello World!"))
'''
'''
def generate_numbers(games):
    for game in range(games):
        numbers = [random.randint(1,45) for x in range(6)]
        print("{}  {} {} {} {} {} {}".format(game+1, numbers[0],numbers[1],numbers[2],numbers[3],numbers[4],numbers[5]))

'''
'''
class MyWidget(Widget):
    pass


class Hello2App(App):
    def build(self):
        #return Label()
        return MyWidget()
'''

def generate_numbers(game_name,games):
    if game_name == 'lot':
        for game in range(games):
            numbers = [random.randint(1,45) for x in range(6)]
            print("{}  {} {} {} {} {} {}".format(game+1, numbers[0],numbers[1],numbers[2],numbers[3],numbers[4],numbers[5]))
    elif game_name == 'sfl':
        for game in range(games):
            numbers = [random.randint(1,44) for x in range(7)]
            print("{}  {} {} {} {} {} {} {}".format(game+1, numbers[0],numbers[1],numbers[2],numbers[3],numbers[4],numbers[5],numbers[6]))
    else:
        print("Unknown Game of {}".format(game_name))
        sys.exit()

if __name__ == '__main__':
    pass
    #panel_of_numbers = generate_numbers('sfl', 10)
    #print(panel_of_numbers)
    #print("{}  {} {} {} {} {} {} {}".format(game+1, numbers[0],numbers[1],numbers[2],numbers[3],numbers[4],numbers[5],numbers[6]))
    #Hello2App().run()
    #MyApp().run()
    #PongApp().run()