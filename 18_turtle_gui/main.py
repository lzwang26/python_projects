import colorgram
import os
from drawer import DotDrawer

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sample.jpg")
  
colors = colorgram.extract(file_path, 10)
rgb_colors = []
for color in colors: 
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

drawer = DotDrawer(10, 50, 10, 10)
drawer.draw_circle_pic(rgb_colors)
