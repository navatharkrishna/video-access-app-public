from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.video import Video

class VideoAppLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.label = Label(text="📺 Welcome to Video Access App", font_size=20, size_hint=(1, 0.2))
        self.add_widget(self.label)

        self.video = Video(source="", state="stop", options={'allow_stretch': True}, size_hint=(1, 0.6))
        self.add_widget(self.video)

        self.play_btn = Button(text="▶ Play Sample Video", size_hint=(1, 0.2))
        self.play_btn.bind(on_press=self.play_sample_video)
        self.add_widget(self.play_btn)

    def play_sample_video(self, instance):
        # Example video — replace with your hosted video
        self.video.source = "https://archive.org/download/ElephantsDream/ed_1024_512kb.mp4"
        self.video.state = "play"

class MyKivyApp(App):
    def build(self):
        return VideoAppLayout()

if __name__ == "__main__":
    MyKivyApp().run()
