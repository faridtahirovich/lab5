from point import *
from figure import *
from turtle import *

def drawLine(t, p1, p2):
    t.up()
    t.width(10)
    t.pencolor(0, 1, 1)
    t.goto(p1.get_x(), p1.get_y())
    t.down()
    t.goto(p2.get_x(), p2.get_y())

def drawPoint(t,p):
    t.up()
    t.width(15)
    t.pencolor(0, 0, 1)
    t.goto(p.get_x(),p.get_y())
    t.dot()

def drawFigure(t,figure):
    pts = figure.get_points()
    for i in range(0,len(pts)-1):
        drawLine(t,pts[i],pts[i+1])
    drawLine(t,pts[len(pts)-1],pts[0])

def isIntRec(p,figure):
    px = p.get_x()
    py = p.get_y()
    f_pts = figure.get_points()
    f_a_x = f_pts[0].get_x()
    f_b_x = f_pts[1].get_x()
    f_c_x = f_pts[2].get_x()
    f_d_x = f_pts[3].get_x()
    f_a_y = f_pts[0].get_y()
    f_b_y = f_pts[1].get_y()
    f_c_y = f_pts[2].get_y()
    f_d_y = f_pts[3].get_y()
    return (px <= f_b_x) and (px >= f_a_x) and (py <= f_c_y) and (py >= f_a_y)

def main():
    pA = Point(0,0)
    pB = Point(100,50)
    pC = Point(400,100)
    pD = Point(-250,50)
    pE = Point(-120, 20)
    pX = Point(-10,-10)

    rec = Figure([pA,pB,pC,pD,pE])
    print(rec)
    t1 = Turtle()

    drawFigure(t1,rec)
    drawPoint(t1,pX)
    pFlag = isIntRec(pX,rec)
    print("====================")
    print(f"A in Figure: {pFlag}")

#    drawLine(t1, pA, pB)
#    drawLine(t1, pB, pC)
#    drawLine(t1, pC, pD)
#    drawLine(t1, pD, pA)
    done()


if __name__ == "__main__":
    main()