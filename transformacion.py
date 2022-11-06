import  Render
from vector import *
import random
import extras as ex
from textures import *
from Object import *
from gl import *
from numpy import *

r = Render.Render(1024,1024)
r.set_color(Render.color(round(255), round(255), round(255)))

center = (300,300)

points = [(200,200),(400,200),(400,400),(200,400)]

a=pi/6

# scale_matrix = matrix([[3/2,0],[0,3/2]])
rotation_matrix = matrix([[cos(a),-sin(a)],[sin(a),cos(a)]])
translation_matrix = matrix([[1,0,-100],[0,1,0],[0,0,1]])
scale_matrix = matrix([[0.5,0,0],[0,0.5,0],[0,0,1]])

transformed_points = []
for point in points:
    transformed_point = scale_matrix @ translation_matrix @ [point[0],point[1],1]
    transformed_points.append(V3(*transformed_point.tolist()[0]))


prev_point = transformed_points[-1]
for point in transformed_points:
    r.line(prev_point,point)
    prev_point = point

# r.line(V3(200,200),V3(200,400))

r.write('tramsformation.bmp')