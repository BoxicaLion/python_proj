import turtle #imporing the module

turtle.setup(500,600) #seting up the window size


#setu up the turtle.
turtle.penup()
turtle.hideturtle()

#creating the variabiles for cordonates

left_shoulder_x = -70
left_shoulder_y = 200

right_shoulder_x = 80
right_shoulder_y = 180

left_bletstar_x = -40
left_bletstar_y = -20

middle_bletstar_x = 0
middle_bletstar_y = 0

right_bletstar_x = 40
right_bletstar_y = 20

left_knee_x = -90
left_knee_y = -140

right_kee_x = 120
right_kee_y = -140


turtle.goto(left_shoulder_x, left_shoulder_y)
turtle.dot()
turtle.goto(right_shoulder_x, right_shoulder_y)
turtle.dot()
turtle.goto(left_bletstar_x, left_bletstar_y)
turtle.dot()
turtle.goto(middle_bletstar_x, middle_bletstar_y)
turtle.dot()
turtle.goto(right_bletstar_x, right_bletstar_y)
turtle.dot()
turtle.goto(left_knee_x, left_knee_y)
turtle.dot()
turtle.goto(right_kee_x,right_kee_y)
turtle.dot()

turtle.goto(left_shoulder_x, left_shoulder_y)
turtle.write('Betegeuse')
turtle.goto(right_shoulder_x, right_shoulder_y)
turtle.write('meissa')
turtle.goto(left_bletstar_x, left_bletstar_y)
turtle.write('Alnitak')
turtle.goto(middle_bletstar_x, middle_bletstar_y)
turtle.write('Alnilam')
turtle.goto(right_bletstar_x, right_bletstar_y)
turtle.write('Mintaka')
turtle.goto(left_knee_x, left_knee_y)
turtle.write('Saiph')
turtle.goto(right_kee_x,right_kee_y)
turtle.write('Rigle')




turtle.goto(left_shoulder_x, left_shoulder_y)
turtle.pendown()
turtle.goto(left_bletstar_x, left_bletstar_y)
turtle.penup()

turtle.goto(right_shoulder_x, right_shoulder_y)
turtle.pendown()
turtle.goto(right_bletstar_x, right_bletstar_y)
turtle.penup()

turtle.goto(left_bletstar_x, left_bletstar_y)
turtle.pendown()
turtle.goto(middle_bletstar_x, middle_bletstar_y)
turtle.penup()

turtle.goto(middle_bletstar_x, middle_bletstar_y)
turtle.pendown()
turtle.goto(right_bletstar_x, right_bletstar_y)
turtle.pendown()

turtle.goto(left_bletstar_x, left_bletstar_y)
turtle.pendown()
turtle.goto(left_knee_x, left_knee_y)
turtle.penup()

turtle.goto(right_bletstar_x, right_bletstar_y)
turtle.pendown()
turtle.goto(right_kee_x,right_kee_y)

turtle.done()
