# Author: 'Mathew Cunningham'
import turtle
import random

t = turtle.Turtle()
myWin = turtle.Screen()


def tree(branchLen,t):
    randBranch = random.randrange(5,15)
    if branchLen > 5:
        t.color("#53350A")
        t.width(branchLen / 4)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-randBranch,t)
        t.right(20)
        t.backward(branchLen)
        t.width(branchLen/8)
    if branchLen < 10:
        t.color("#006400")
    else:
        t.color("#53350A")


t.speed(0)
t.left(90)
t.up()
t.backward(200)
t.down()
tree(100,t)
myWin.exitonclick()