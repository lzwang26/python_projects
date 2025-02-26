import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
class DotDrawer:
    def __init__(self, size_input, space_input, quantity_in_row_input, quantity_row_input):
        self.size = size_input
        self.space = space_input
        self.in_row = quantity_in_row_input
        self.quantity_row = quantity_row_input
        
        
    def draw_dot(self, color):
        tim.color(color)
        tim.dot(self.size, color)
        
    
    def draw_circle_row(self, colors):
        for i in range(self.in_row):
            self.draw_dot(random.choice(colors))
            tim.forward(self.space)
    
    def draw_circle_pic(self, colors):
        for i in range(self.quantity_row):
            tim.goto(0, -self.space * i)
            self.draw_circle_row(colors)
        screen = t.Screen()
        screen.exitonclick()
