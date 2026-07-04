#Author: Bondek 'Naurder' Barłomiej

import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg     import *

class FractalTree(QMainWindow,QWidget):
    def __init__(self, ifImMain = False):
        self.iAmMain = ifImMain
        super().__init__()
        self.initUI()
    def initUI(self):
        
        self.setWindowTitle('Tree')             #self.title = 'Tree'
        self.resize(1200, 600)                  #self.setGeometry(100, 100, 1200, 600)

        


        #Fractal    PARAMETERs::FACTORs::RATIOs
        self.branch_Angle = 45
        
        self.initial_Branch_Length = 200
        self.initial_Length_Ratio = .66
        self.rightBranch_Length_Ratio = 1
        self.leftBranch_Length_Ratio = 1

        self.knot_Position_Ratio = 1
        
        self.current_Itteration = 0
        self.max_Itterations = 10
        
        #booleans (options):
        self.Antialiasing_ON = False
        self.Distinguishing_LeftRight_Branch = False
        
        #positioning
        self.zoom = 1
        self.FRACTAL_POSITION = {   "Top Left":     {"w": 0, "h": 0},
                                    "Top Mid":      {"w": 1, "h": 0},
                                    "Top Right":    {"w": 2, "h": 0},
                                    "Middle Left":  {"w": 0, "h": 1},
                                    "Center":       {"w": 1, "h": 1},
                                    "Middle Right": {"w": 2, "h": 1},
                                    "Bottom Left":  {"w": 0, "h": 2},
                                    "Bottom Mid":   {"w": 1, "h": 2},
                                    "Bottom Right": {"w": 2, "h": 2},}
        self.position_Vector = {"w": 1, "h": 2}
        self.startingPoint_Rotation_Angle = 0

        #brush, color, shape, etc.
        self.color_HSV_ratio = 15
        self.SVG_saving = False
        self.SVG_fileName = "test.svg"
        self.brush_Thickness = 1
        self.shape = {
            "Line":     True,
            "Rect":     False,
            "Circle":   False,
            "Triangle": False
        }
        self.shape_KEY_NAMES = {
            "Line":     "Line",
            "Rect":     "Rect",
            "Circle":   "Circle",
            "Triangle": "Triangle"
        }


        #background
        self.pal = QPalette()
        self.pal.setColor(QPalette.Background, QColor(0, 0, 0))
        self.setPalette(self.pal)

        if(self.iAmMain == False):
            self.setStyleSheet("background-color:black;")


        self.alignSelfAtTheCenter()
        if(self.iAmMain):
            self.slider()
    #__init__##################################     End of constructor   ################################
    
    #additional methods for self-Rendering
    def alignSelfAtTheCenter(self):
        windowRec = self.frameGeometry()                            #copying current APP geometry
        centerPoint = QDesktopWidget().availableGeometry().center() #finding screen center point
        windowRec.moveCenter(centerPoint)                           #setting copy of APP to the center point 
        self.move(windowRec.topLeft())                              #setting original APP
    def slider(self):
        self.slider_angle = QSlider(Qt.Vertical, self)
        self.slider_angle.setMinimum(-80*100)
        self.slider_angle.setMaximum(80*100)
        self.slider_angle.setGeometry(0, 25, 25, self.height())
        self.slider_angle.valueChanged.connect(lambda v: self.setAngleValue(v/100))
        self.slider_angle.setValue(4500)

    #OPTIONS:   
    def switch_ON__Antialiasing(self, passState):
        if(passState):
            self.Antialiasing_ON = True
        else:
            self.Antialiasing_ON = False
        self.update()
    def switch_ON__Distinguishing_By_LeftRight_Branch(self, passState):
        if(passState):
            self.Distinguishing_LeftRight_Branch = True
        else:
            self.Distinguishing_LeftRight_Branch = False
        self.update()
    #Positioning methods
    def setDrawingPointPosition(self, fractal_POSITION_OPTIONS):
        self.position_Vector = fractal_POSITION_OPTIONS
        self.update()
    def setZoomView(self, value):
        if(value>0):
            self.zoom = value
    def setStartingPointRotationAngle(sefl, value): 
        sefl.startingPoint_Rotation_Angle = value
        sefl.update()
    #outlook, appearance
    def setDrawingShape(self, shape_KEY_NAMES=["Line","Rect","Circle","Triangle"]):
        self.shape[shape_KEY_NAMES] = not self.shape[shape_KEY_NAMES]
        self.update()
    def setBrushThickness(self, value):
        self.brush_Thickness = value
        self.update()
    def setColor_HSV_Ratio(self, value):
        self.color_HSV_ratio = value
        self.update()    

    #Fractal MODIFICATION methods (setters)
    def setAngleValue(self, value):
        self.branch_Angle = value          #branch_Angle = self.slider_angle.value()/100
        self.update()              

    def setMaxItterations(self, value):
        self.max_Itterations = value

    def setInitialBranchLength(self, value):
        self.initial_Branch_Length = value
    def setInitialLengthRatio(self, value):
        self.initial_Length_Ratio = value    
    def setRightBranchLengthRatio(self, value):
        self.rightBranch_Length_Ratio = value    
    def setLeftBranchLengthRatio(self, value):
        self.leftBranch_Length_Ratio = value

    def setKnotPositionRatio(self, value):
        self.knot_Position_Ratio = value

    
    


    #   branch(self;    QPainter,   angle,  initial length)
    def branch(self,    p,          r,      length):
        self.current_Itteration += 1

        if self.current_Itteration <= self.max_Itterations:

            #color = (self.current_Itteration*60)%359
            #if(self.current_Itteration*15 <= 359):
            p.setPen(QPen(QColor.fromHsv((self.current_Itteration*self.color_HSV_ratio)%359, 255, 255, 255), self.brush_Thickness))            #!!!!!!!!!!!biggest problem took 3 hours!!!!!!!!!!!!
            
            #RED    p.setPen(QColor.fromHsv(0, 255, 255, 255))
            #BLUE   p.setPen(QColor.fromHsv(240, 255, 255, 255))


            #drawing shape
            #'Line'
            if(self.shape["Line"]):         
                p.drawLine(0, 0, 0, int(-length))
            #'Rect'
            if(self.shape["Rect"]):
                p.drawRect(int(length/2), 0, int(-length), int(-length))
            #'Circle'
            if(self.shape["Circle"]):
                p.drawEllipse(int(length/2), 0, int(-length), int(-length))
            #'Triangle'
            if(self.shape["Triangle"]):
                p.drawPolygon(QPolygon([    QPoint(int(length/2),0),    QPoint(int(-length/2),0),   QPoint(0,int(-length/2*3**(1/2)))  ]))

            
            if length > 3:
                #saving BASIC state
                p.save()
                p.translate(0, -length*self.knot_Position_Ratio)
                
                #RIGHT branch saving point
                p.save()
                p.rotate(r)
                #p.setPen(QColor.fromHsv(0, 255, 255, 255))
                self.branch(p, r, length * self.initial_Length_Ratio*self.rightBranch_Length_Ratio)
                self.current_Itteration -= 1
                #restore RIGHT branch
                p.restore()


                #LEFT branch saving point
                p.save()
                p.rotate(-r)

                if(self.Distinguishing_LeftRight_Branch):
                    r = -r
                #p.setPen(QColor.fromHsv(240, 255, 255, 255))
                self.branch(p, -r, length * self.initial_Length_Ratio*self.leftBranch_Length_Ratio)
                self.current_Itteration -= 1
                #restore LEFT branch
                p.restore()

                #restore the BASIC state
                p.restore()
    
    # Drawing ##########################################################################
    def paintEvent(self, event):
        if(self.SVG_saving):
            generator = QSvgGenerator()
            generator.setFileName(self.SVG_fileName)
            generator.setSize(QSize(4000, 4000))
            generator.setViewBox(QRect(-8000, -8000, 16000, 16000))

            self.painter = QPainter(generator)
            self.painter.fillRect(QRect(-8000, -8000, 16000, 16000), QColor(0, 0, 0))
            self.painter.setPen(QPen(Qt.red, 3))

            self.SVG_saving = False
        else:
            self.painter = QPainter(self)
            self.painter.setPen(QPen(Qt.red, 3))

        
        

        
        windowRectangle = self.painter.window()
        #print(windowRectangle.height())
        windowRectangle.setSize(QSize(int(windowRectangle.width()/self.zoom), int(windowRectangle.height()/self.zoom)))
        #windowRectangle.moveTo(QPoint(0,0))
        #print(windowRectangle.size().width())
        #windowRectangle.setX(int(windowRectangle.size().width()/2))
        #windowRectangle.setY(int(windowRectangle.size().height()/2))
        self.painter.setWindow(windowRectangle)  
            
        if(self.Antialiasing_ON):                           #<-optional smoothing
            self.painter.setRenderHint(QPainter.Antialiasing)  

        #printing angle by QPainter
        if(self.iAmMain):
            self.painter.drawText(20, 20,  str(self.branch_Angle) + '\N{DEGREE SIGN}')

        self.painter.translate(self.width()*self.position_Vector["w"]/2/self.zoom, self.height()*self.position_Vector["h"]/2/self.zoom)
        self.painter.rotate(self.startingPoint_Rotation_Angle)
        self.branch(self.painter, self.branch_Angle, self.initial_Branch_Length)
        self.current_Itteration -= 1

        self.painter.end()
        #self.update()
        
############################################## CLASS END ########################################################

if __name__ == '__main__':
    #print("i am main file")
    app = QApplication(sys.argv)
    
    window = FractalTree(True)  #window.resize(800   , 800)  
    window.show()
    
    sys.exit(app.exec_())