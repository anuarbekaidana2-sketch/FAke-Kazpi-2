from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle

class RoundedButton(Button):
    def __init__(self, button_color=(0.662, 0.662, 0.662, 1), **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)  # Прозрачный фон кнопки
        with self.canvas.before:
            Color(*button_color)  # Используемый цвет для фона кнопки
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class WhiteBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(WhiteBoxLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)  # Белый цвет (RGBA)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[0])
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class WhiteBackgroundApp(App):
    def build(self):
        # Создаем основной вертикальный макет, который будет содержать верхнюю и нижнюю части
        main_layout = WhiteBoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Создаем верхнюю часть макета для кнопок "Документы" и "Реквизиты"
        top_layout = BoxLayout(orientation='horizontal', size_hint_y=0.005, padding=10, spacing=10)
        
        # Создаем серые кнопки для верхней части
        btn1 = RoundedButton(
            text="Документы", 
            size_hint=(0.5, 0.9), 
            font_size=18,
            button_color=(0.662, 0.662, 0.662, 1)  # Серый цвет
        )
        btn2 = RoundedButton(
            text="Реквизиты",
            size_hint=(0.5, 0.9), 
            font_size=18,
            button_color=(0.662, 0.662, 0.662, 1)  # Серый цвет
        )
        
        # Добавляем кнопки в верхний макет
        top_layout.add_widget(btn1)
        top_layout.add_widget(btn2)
        
        # Создаем нижнюю часть макета для кнопок "Предъявить документ" и "Отправить документ"
        bottom_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1, padding=10, spacing=10)
        
        # Создаем голубые кнопки для нижней части
        btn3 = RoundedButton(
            text="Предъявить документ", 
            size_hint=(0.5, 0.05), 
            font_size=18,
            button_color=(0.4, 0.7, 1, 1)  # Голубой цвет
        )
        btn4 = RoundedButton(
            text="Отправить документ", 
            size_hint=(0.5, 0.05), 
            font_size=18,
            button_color=(0.4, 0.7, 1, 1)  # Голубой цвет
        )
        
        # Добавляем кнопки в нижний макет
        bottom_layout.add_widget(btn3)
        bottom_layout.add_widget(btn4)
        
        # Добавляем верхний и нижний макеты в основной макет
        main_layout.add_widget(top_layout)
        main_layout.add_widget(bottom_layout)
        
        return main_layout

if __name__ == "__main__":
    WhiteBackgroundApp().run()
