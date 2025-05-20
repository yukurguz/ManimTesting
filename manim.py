from manim import *

class BeautifulAnimation(Scene):
    def construct(self):
        title = Text("Привет от Manim!", font_size=60, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.shift(UP*2))

        circle = Circle(color=GREEN)
        square = Square(color=RED)
        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Rotate(square, angle=2*PI))
        self.play(FadeOut(square), FadeOut(title))

if __name__ == "__main__":
    from manim import config
    config.background_color = WHITE
    BeautifulAnimation().render()
