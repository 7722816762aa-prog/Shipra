import os
import time
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

# स्क्रीन साइज़ और डार्क-प्रीमियम थीम
Window.size = (360, 640)
Window.clearcolor = (0.02, 0.02, 0.03, 1)

class LicenseScreen(Screen):
    def __init__(self, **kwargs):
        super(LicenseScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        layout.add_widget(Label(text="Trial Expired!\nBuy License from our Website (₹600)\nEnter Key: SHIPRA600", font_size=14, color=(1, 0.8, 0.2, 1), bold=True, halign='center'))
        
        self.key_input = TextInput(hint_text="Enter SHIPRA600", multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.key_input)
        
        btn = Button(text="Activate License", size_hint_y=None, height=45, background_color=(0.2, 0.8, 0.3, 1))
        btn.bind(on_press=self.check_license)
        layout.add_widget(btn)
        
        self.add_widget(layout)

    def check_license(self, instance):
        if self.key_input.text == "SHIPRA600":
            self.manager.current = 'main_screen'
        else:
            self.key_input.hint_text = "Wrong Key! Try SHIPRA600"

class MainAppScreen(Screen):
    def __init__(self, **kwargs):
        super(MainAppScreen, self).__init__(**kwargs)
        self.trial_time = 180 # 3 मिनट का ट्रायल[span_3](start_span)[span_3](end_span)
        self.timer_event = Clock.schedule_interval(self.update_trial, 1)

        layout = BoxLayout(orientation='vertical', padding=12, spacing=8)

        # 1. ऊपर का स्टेटस बार
        top_bar = BoxLayout(size_hint_y=None, height=45)
        top_bar.add_widget(Label(text="[b]Good afternoon,\nBoss[/b]", markup=True, font_size=16, color=(1, 1, 1, 1)))
        top_bar.add_widget(Label(text="⚡ Edge FX Active", font_size=13, color=(1, 0.3, 0.5, 1), halign='right'))
        layout.add_widget(top_bar)

        # 2. बीच में फोटो और मूड स्टेटस
        img_layout = BoxLayout(orientation='vertical', size_hint_y=0.40, spacing=4)
        
        self.status_sub = Label(text="🔥 Mood: Furious & Bossy", font_size=11, color=(1, 0.4, 0.4, 1), bold=True, size_hint_y=None, height=18)
        img_layout.add_widget(self.status_sub)

        if os.path.exists('Shipra.png'):
            self.img_widget = Image(source='Shipra.png', allow_stretch=True, keep_ratio=False)
        else:
            self.img_widget = Label(text="[color=ff3366]Shipra.png missing![/color]", markup=True, color=(1, 1, 1, 1))
            
        img_layout.add_widget(self.img_widget)
        layout.add_widget(img_layout)

        # 3. बीच के कार्ड्स (Weather & Battery Warning)
        cards_box = GridLayout(cols=2, size_hint_y=None, height=85, spacing=8)
        
        weather_card = BoxLayout(orientation='vertical', padding=6)
        weather_card.add_widget(Label(text="🌤️ Weather: 29°C", font_size=11, color=(0.9, 0.9, 0.9, 1)))
        weather_card.add_widget(Label(text="Stormy vibes", font_size=10, color=(0.6, 0.6, 0.6, 1)))
        cards_box.add_widget(weather_card)

        mood_card = BoxLayout(orientation='vertical', padding=6)
        mood_card.add_widget(Label(text="⚠️ Battery: 14%", font_size=11, color=(1, 0.2, 0.2, 1)))
        mood_card.add_widget(Label(text="Plug charger now!", font_size=10, color=(0.9, 0.5, 0.5, 1)))
        cards_box.add_widget(mood_card)
        
        layout.add_widget(cards_box)

        # 4. नीचे वॉयस / चैट का दबंग बार
        voice_box = BoxLayout(size_hint_y=None, height=50, spacing=10)
        self.mic_btn = Button(text="🎙️ Tap & Talk to Shipra", font_size=14, bold=True, background_color=(0.1, 0.5, 0.8, 1))
        self.mic_btn.bind(on_press=self.on_mic_pressed)
        voice_box.add_widget(self.mic_btn)
        layout.add_widget(voice_box)

        # 5. सबसे नीचे बॉटम नेविगेशन बार (वेबसाइट लिंक बटन के साथ)
        nav_bar = BoxLayout(size_hint_y=None, height=42, spacing=5)
        nav_bar.add_widget(Button(text="🏠 Home", font_size=11, background_color=(0.2, 0.2, 0.3, 1)))
        nav_bar.add_widget(Button(text="💡 Edge FX", font_size=11, background_color=(0.4, 0.1, 0.3, 1)))
        
        buy_btn = Button(text="🌐 Buy Key", font_size=11, background_color=(0.3, 0.6, 0.1, 1))
        buy_btn.bind(on_press=self.open_website)
        nav_bar.add_widget(buy_btn)
        
        nav_bar.add_widget(Button(text="💬 Chat", font_size=11, background_color=(0.2, 0.2, 0.3, 1)))
        layout.add_widget(nav_bar)

        self.add_widget(layout)

    def on_mic_pressed(self, instance):
        instance.text = "Shipra: 'ज्यादा फोन मत चलाओ, वरना ब्लॉक कर दूँगी!' 😡"
        Clock.schedule_once(lambda dt: setattr(instance, 'text', "🎙️ Tap & Talk to Shipra"), 3)

    def open_website(self, instance):
        instance.text = "Opening Website..."
        # यहाँ हमारी खुद की लाइसेंस बिक्री वाली वेबसाइट खुलेगी
        Clock.schedule_once(lambda dt: setattr(instance, 'text', "🌐 Buy Key"), 2)

    def update_trial(self, dt):
        if self.trial_time > 0:
            self.trial_time -= 1
        else:
            self.manager.current = 'license_screen'
            Clock.unschedule(self.timer_event)

class ShipraApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainAppScreen(name='main_screen'))
        sm.add_widget(LicenseScreen(name='license_screen'))
        return sm

if __name__ == '__main__':
    ShipraApp().run()
