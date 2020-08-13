from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json, glob, random
from hoverable import HoverBehavior
from pathlib import Path
from datetime import datetime

Builder.load_file('design.kv')

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login(self, uname, pword):
        with open("users.json", 'r') as file:
            users = json.load(file)
            if uname in users and users[uname]['password'] == pword:
                self.manager.transition.direction = "right"
                self.manager.current = "login_success"
            else:
                self.ids.login_wrong.text = "Invalid credentials. Please try again!"

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)

        users[uname] = {'username': uname, 'password': pword, 
        'created':datetime.now().strftime('%Y-%m-%d %H-%M-%S')}

        with open("users.json", 'w') as file:
            json.dump(users, file)
      
        self.manager.current = "sign_up_success"

class SignUpSuccess(Screen):
    def back_to_login(self):
        self.manager.transition.direction = "right"     
        self.manager.current = "login_screen"

class LoginSuccess(Screen):
    def logout(self):
        self.manager.transition.direction = "left" 
        self.manager.current = "login_screen"
           
    def get_quote(self, feeling):
        feeling = feeling.lower()
        available_feelings = glob.glob("mobile_app/quotes/*txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]
                     
        if feeling in available_feelings:
            print(available_feelings)
            with open(f"mobile_app/quotes/{feeling}.txt") as file:
                quotes = file.readlines()
            self.ids.msg.text = random.choice(quotes)

        else:
            self.ids.msg.text = "Please try some other feeling!"    

class ImageButton(ButtonBehavior,Image,HoverBehavior):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()
   