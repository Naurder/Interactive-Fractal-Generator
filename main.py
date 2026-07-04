#Author: Bondek 'Naurder' Barłomiej
import FractalTreeClass
from FractalTreeClass import FractalTree as fTree

import sys
import os
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, QApplication

from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

from PyQt5.QtCore import Qt

import wave

###################generator import
import numpy as np
from scipy.io.wavfile import write

clear = lambda: os.system('cls')
import msvcrt as m
def wait():
    print("Nacisnij dowolny klawisz aby kontynuowac")
    m.getch()
    clear()

from scipy.fft import fft
import pandas as pd
###################generator import

class App(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        
        self.title = "Fractal Generator"
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 1200, 600)
        FractalTreeClass.FractalTree.alignSelfAtTheCenter(self)             #method from fractal Tree Module::class FractalTree

        self.fractal_Tree_Field = FractalTreeClass.FractalTree()

        #########               MENU Bar            ####
        save_as_SVG = QAction('Save as .SVG', self)
        save_as_SVG.triggered.connect(self.saveFractalAsSVG)

        exitProgram = QAction('Exit', self)
        exitProgram.triggered.connect(self.exit_program)

        aboutProgram = QAction('About', self)
        aboutProgram.triggered.connect(self.about_program)
        
        antialiasing = QAction('Antialiasing', self)
        antialiasing.setCheckable(True)
        antialiasing.triggered.connect(self.switch_ON__Antialiasing)

        distinguish_LeftRight_Branch = QAction('Distinguish L/R Branch', self)
        distinguish_LeftRight_Branch.setCheckable(True)
        distinguish_LeftRight_Branch.triggered.connect(self.switch_ON__Distinguish_LeftRight_Branch)

        self.position =['Top Left',    'Top Mid',      'Top Right',
                        'Middle Left', 'Center',       'Middle Right',
                        'Bottom Left', 'Bottom Mid',   'Bottom Right',]
        position_Top_Left = QAction(    self.position[0], self)
        position_Top_Mid = QAction(     self.position[1], self)
        position_Top_Right = QAction(   self.position[2], self)
        position_Middle_Left = QAction( self.position[3], self)
        position_Middle_Mid = QAction(  self.position[4], self)
        position_Middle_Right = QAction(self.position[5], self)
        position_Bottom_Left = QAction( self.position[6], self)
        position_Bottom_Mid = QAction(  self.position[7], self)
        position_Bottom_Right = QAction(self.position[8], self)

        position_Top_Left.triggered.connect(lambda: self.setFractalPosition(fTree().FRACTAL_POSITION["Top Left"]))
        position_Top_Mid.triggered.connect(lambda: self.setFractalPosition(     fTree().FRACTAL_POSITION["Top Mid"]))
        position_Top_Right.triggered.connect(lambda: self.setFractalPosition(   fTree().FRACTAL_POSITION["Top Right"]))
        position_Middle_Left.triggered.connect(lambda: self.setFractalPosition( fTree().FRACTAL_POSITION["Middle Left"]))
        position_Middle_Mid.triggered.connect(lambda: self.setFractalPosition(  fTree().FRACTAL_POSITION["Center"]))
        position_Middle_Right.triggered.connect(lambda: self.setFractalPosition(fTree().FRACTAL_POSITION["Middle Right"]))
        position_Bottom_Left.triggered.connect(lambda: self.setFractalPosition( fTree().FRACTAL_POSITION["Bottom Left"]))
        position_Bottom_Mid.triggered.connect(lambda: self.setFractalPosition(  fTree().FRACTAL_POSITION["Bottom Mid"]))
        position_Bottom_Right.triggered.connect(lambda: self.setFractalPosition(fTree().FRACTAL_POSITION["Bottom Right"]))


        shape_Line = QAction("Line", self)
        shape_Line.setCheckable(True)
        shape_Line.setChecked(True)
        shape_Rect = QAction("Rect", self)
        shape_Rect.setCheckable(True)
        shape_Circle = QAction("Circle", self)
        shape_Circle.setCheckable(True)
        shape_Triangle = QAction("Triangle", self)
        shape_Triangle.setCheckable(True)

        shape_Line.triggered.connect(lambda: self.setShape(fTree().shape_KEY_NAMES["Line"]))
        shape_Rect.triggered.connect(lambda: self.setShape(fTree().shape_KEY_NAMES["Rect"]))
        shape_Circle.triggered.connect(lambda: self.setShape(fTree().shape_KEY_NAMES["Circle"]))
        shape_Triangle.triggered.connect(lambda: self.setShape(fTree().shape_KEY_NAMES["Triangle"]))

        brush_Thickness_halfPX = QAction("0.5 px", self)
        brush_Thickness_halfPX.setCheckable(True)
        brush_Thickness_default = QAction("1 px", self)
        brush_Thickness_default.setCheckable(True)
        brush_Thickness_default.setChecked(True)
        brush_Thickness_twoPX = QAction("2 px", self)
        brush_Thickness_twoPX.setCheckable(True)
        brush_Thickness_fivePX = QAction("5 px", self)
        brush_Thickness_fivePX.setCheckable(True)
        brush_Thickness_teenPX = QAction("10 px", self)
        brush_Thickness_teenPX.setCheckable(True)
        brush_Thickness_fTeenPX = QAction("15 px", self)
        brush_Thickness_fTeenPX.setCheckable(True)

        brush_Thickness_halfPX.triggered.connect(lambda: self.setBrush_Thickness(.5))
        brush_Thickness_default.triggered.connect(lambda: self.setBrush_Thickness(1))
        brush_Thickness_twoPX.triggered.connect(lambda: self.setBrush_Thickness(2))
        brush_Thickness_fivePX.triggered.connect(lambda: self.setBrush_Thickness(5))
        brush_Thickness_teenPX.triggered.connect(lambda: self.setBrush_Thickness(10))
        brush_Thickness_fTeenPX.triggered.connect(lambda: self.setBrush_Thickness(15))

        self.brush_Color_pallete_Ratio = QAction("Color Changer", self)
        self.brush_Color_pallete_Ratio.setCheckable(True)
        self.brush_Color_pallete_Ratio.triggered.connect(self.showColorChanger)
        


        MENU_Bar = self.menuBar()
        
        Menu_file = MENU_Bar.addMenu('File')
        Menu_file.addAction(save_as_SVG)
        Menu_file.addSection('')
        Menu_file.addAction(exitProgram)

        Menu_options = MENU_Bar.addMenu('Options')
        Menu_options.addAction(antialiasing)
        Menu_options.addAction(distinguish_LeftRight_Branch)
        
        Menu_fractalPosition = MENU_Bar.addMenu('Position')
        Menu_fractalPosition.addAction(position_Top_Left)
        Menu_fractalPosition.addAction(position_Top_Mid)
        Menu_fractalPosition.addAction(position_Top_Right)
        Menu_fractalPosition.addSection('')
        Menu_fractalPosition.addAction(position_Middle_Left)
        Menu_fractalPosition.addAction(position_Middle_Mid)
        Menu_fractalPosition.addAction(position_Middle_Right)
        Menu_fractalPosition.addSection('')
        Menu_fractalPosition.addAction(position_Bottom_Left)
        Menu_fractalPosition.addAction(position_Bottom_Mid)
        Menu_fractalPosition.addAction(position_Bottom_Right)

        Menu_painterBrush = MENU_Bar.addMenu('Painter')
        Menu_painterBrush_Shapes = Menu_painterBrush.addMenu('Shapes')
        Menu_painterBrush_Shapes.addAction(shape_Line)
        Menu_painterBrush_Shapes.addAction(shape_Rect)
        Menu_painterBrush_Shapes.addAction(shape_Circle)
        Menu_painterBrush_Shapes.addAction(shape_Triangle)
        self.Menu_painterBrush_Thickness = Menu_painterBrush.addMenu('Thickness')
        self.Menu_painterBrush_Thickness.addAction(brush_Thickness_halfPX)
        self.Menu_painterBrush_Thickness.addAction(brush_Thickness_default)
        self.Menu_painterBrush_Thickness.addAction(brush_Thickness_twoPX)
        self.Menu_painterBrush_Thickness.addAction(brush_Thickness_fivePX)
        self.Menu_painterBrush_Thickness.addAction(brush_Thickness_teenPX)
        self.Menu_painterBrush_Thickness.addAction(brush_Thickness_fTeenPX)
        Menu_painterBrush.addAction(self.brush_Color_pallete_Ratio)
        
        


        Menu_help = MENU_Bar.addMenu('Help')
        Menu_help.addAction(aboutProgram)

        


        #layout right
        layout_rightSide = QVBoxLayout()
        layout_rightSide.addWidget(self.fractal_Tree_Field)
        
        
        #left layout
        layout_leftMenu = QVBoxLayout()
        layout_leftTopMenu = QHBoxLayout()
        layout_leftBottomMenu = QVBoxLayout()
        layout_leftMenu.addLayout(layout_leftTopMenu)               #TOP
        layout_leftMenu.addLayout(layout_leftBottomMenu)            #BOTTOM
        

        #TOP LEFT layouts
        layout_angle = QVBoxLayout()
        self.slider_Angle = QSlider(Qt.Vertical, self)
        self.slider_Angle.setFocusPolicy(Qt.StrongFocus)
        self.slider_Angle.setTickPosition(QSlider.TicksBothSides)   #NoTicks, TicksBothSides, TicksAbove, TicksBelow, TicksLeft, TicksRight
        self.slider_Angle.setTickInterval(1000)
        self.slider_Angle.setSingleStep(1000)
        self.slider_Angle.setRange(0*100,   180*100)
        self.slider_Angle.valueChanged.connect(lambda v: self.setAngleValue(v,self.fractal_Tree_Field))
        
        self.SpinBox_Angle = QDoubleSpinBox(self)
        self.SpinBox_Angle.setSuffix('\N{DEGREE SIGN}')
        self.SpinBox_Angle.setRange(0.00, 180)
        self.SpinBox_Angle.setSingleStep(0.01)
        self.SpinBox_Angle.valueChanged.connect(lambda v: self.setAngleValue(v*100,self.fractal_Tree_Field))
        self.SpinBox_Angle.setMaximumWidth(60)

        self.slider_Angle.setValue(4500)
        self.SpinBox_Angle.setValue(4500/100)


        layout_Initial_Branch_Length = QVBoxLayout()
        self.slider_Initial_Length = QSlider(Qt.Vertical, self)
        self.slider_Initial_Length.setFocusPolicy(Qt.StrongFocus)
        self.slider_Initial_Length.setTickPosition(QSlider.TicksBothSides) 
        self.slider_Initial_Length.setTickInterval(100)
        self.slider_Initial_Length.setSingleStep(1)
        self.slider_Initial_Length.setRange(0, 1000)
        self.slider_Initial_Length.valueChanged.connect(self.setInitialBranchLength)

        self.SpinBox_Initial_Length = QSpinBox(self)
        self.SpinBox_Initial_Length.setSuffix('h')
        self.SpinBox_Initial_Length.setSingleStep(1)
        self.SpinBox_Initial_Length.setRange(0, 1000)
        self.SpinBox_Initial_Length.valueChanged.connect(self.setInitialBranchLength)
        self.SpinBox_Initial_Length.setMaximumWidth(60)

        self.slider_Initial_Length.setValue(200)
        self.SpinBox_Initial_Length.setValue(200)



        layout_Initial_Length_Ratio = QVBoxLayout()
        self.slider_Initial_Length_Ratio = QSlider(Qt.Vertical, self)
        self.slider_Initial_Length_Ratio.setFocusPolicy(Qt.StrongFocus)
        self.slider_Initial_Length_Ratio.setTickPosition(QSlider.TicksBothSides) 
        self.slider_Initial_Length_Ratio.setTickInterval(1)
        self.slider_Initial_Length_Ratio.setSingleStep(1)
        self.slider_Initial_Length_Ratio.setRange(0, 200)
        self.slider_Initial_Length_Ratio.valueChanged.connect(lambda v: self.SpinBox_Initial_Length_Ratio.setValue(v/100))

        self.SpinBox_Initial_Length_Ratio = QDoubleSpinBox(self)
        self.SpinBox_Initial_Length_Ratio.setSuffix('r')
        self.SpinBox_Initial_Length_Ratio.setRange(0.01, 2)
        self.SpinBox_Initial_Length_Ratio.setSingleStep(0.01)
        self.SpinBox_Initial_Length_Ratio.valueChanged.connect(lambda v: self.setInitialLengthRatio(v))
        self.SpinBox_Initial_Length_Ratio.setMaximumWidth(60)

        self.SpinBox_Initial_Length_Ratio.setValue(.66)
        


        layout_singleBranch = QVBoxLayout()
        self.slider_RightBranch_Length_Ratio = QSlider(Qt.Vertical, self)
        self.slider_RightBranch_Length_Ratio.setFocusPolicy(Qt.StrongFocus)
        self.slider_RightBranch_Length_Ratio.setTickPosition(QSlider.TicksBothSides) 
        self.slider_RightBranch_Length_Ratio.setTickInterval(1)
        self.slider_RightBranch_Length_Ratio.setSingleStep(1)
        self.slider_RightBranch_Length_Ratio.setRange(0, 100)
        self.slider_RightBranch_Length_Ratio.valueChanged.connect(lambda v: self.setRightBranchLengthRatio(v))

        self.SpinBox_RightBranch_Length_Ratio = QDoubleSpinBox(self)
        self.SpinBox_RightBranch_Length_Ratio.setSuffix('right')
        self.SpinBox_RightBranch_Length_Ratio.setRange(0.00, 1)
        self.SpinBox_RightBranch_Length_Ratio.setSingleStep(0.01)
        self.SpinBox_RightBranch_Length_Ratio.valueChanged.connect(lambda v: self.setRightBranchLengthRatio(v*100))
        self.SpinBox_RightBranch_Length_Ratio.setMaximumWidth(60)

        self.slider_RightBranch_Length_Ratio.setValue(1)
        self.SpinBox_RightBranch_Length_Ratio.setValue(1.00)

        self.slider_LeftBranch_Length_Ratio = QSlider(Qt.Vertical, self)
        self.slider_LeftBranch_Length_Ratio.setFocusPolicy(Qt.StrongFocus)
        self.slider_LeftBranch_Length_Ratio.setTickPosition(QSlider.TicksBothSides) 
        self.slider_LeftBranch_Length_Ratio.setTickInterval(1)
        self.slider_LeftBranch_Length_Ratio.setSingleStep(1)
        self.slider_LeftBranch_Length_Ratio.setRange(0, 100)
        self.slider_LeftBranch_Length_Ratio.valueChanged.connect(lambda v: self.setLeftBranchLengthRatio(v))

        self.SpinBox_LeftBranch_Length_Ratio = QDoubleSpinBox(self)
        self.SpinBox_LeftBranch_Length_Ratio.setSuffix('left')
        self.SpinBox_LeftBranch_Length_Ratio.setRange(0.00, 1)
        self.SpinBox_LeftBranch_Length_Ratio.setSingleStep(0.01)
        self.SpinBox_LeftBranch_Length_Ratio.valueChanged.connect(lambda v: self.setLeftBranchLengthRatio(v*100))
        self.SpinBox_LeftBranch_Length_Ratio.setMaximumWidth(60)

        self.slider_LeftBranch_Length_Ratio.setValue(1)
        self.SpinBox_LeftBranch_Length_Ratio.setValue(1.00)



        layout_knotPosition = QVBoxLayout()
        self.slider_Knot_Position_Ratio = QSlider(Qt.Vertical, self)
        self.slider_Knot_Position_Ratio.setFocusPolicy(Qt.StrongFocus)
        self.slider_Knot_Position_Ratio.setTickPosition(QSlider.TicksBothSides) 
        self.slider_Knot_Position_Ratio.setTickInterval(1)
        self.slider_Knot_Position_Ratio.setSingleStep(1)
        self.slider_Knot_Position_Ratio.setRange(0, 3*100)
        self.slider_Knot_Position_Ratio.valueChanged.connect(lambda v: self.setKnotPositionRatio(v))

        self.SpinBox_Knot_Position_Ratio = QDoubleSpinBox(self)
        self.SpinBox_Knot_Position_Ratio.setSuffix('knot')
        self.SpinBox_Knot_Position_Ratio.setRange(0.00, 3)
        self.SpinBox_Knot_Position_Ratio.setSingleStep(0.01)
        self.SpinBox_Knot_Position_Ratio.valueChanged.connect(lambda v: self.setKnotPositionRatio(v*100))
        self.SpinBox_Knot_Position_Ratio.setMaximumWidth(60)

        self.slider_Knot_Position_Ratio.setValue(1)
        self.SpinBox_Knot_Position_Ratio.setValue(1.00)

        
        layout_colorChanger = QVBoxLayout()
        self.slider_colorChanger = QSlider(Qt.Vertical, self)
        self.slider_colorChanger.setFocusPolicy(Qt.StrongFocus)
        self.slider_colorChanger.setTickPosition(QSlider.TicksBothSides)   #NoTicks, TicksBothSides, TicksAbove, TicksBelow, TicksLeft, TicksRight
        self.slider_colorChanger.setTickInterval(1000)
        self.slider_colorChanger.setSingleStep(1000)
        self.slider_colorChanger.setRange(0*100,   360*100)
        self.slider_colorChanger.valueChanged.connect(lambda v: self.SpinBox_colorChanger.setValue(v/100))
        
        self.SpinBox_colorChanger = QDoubleSpinBox(self)
        self.SpinBox_colorChanger.setSuffix('color')
        self.SpinBox_colorChanger.setRange(0.00, 360)
        self.SpinBox_colorChanger.setSingleStep(0.01)
        self.SpinBox_colorChanger.valueChanged.connect(lambda v: self.setColor_HSV_Ratio(v))
        self.SpinBox_colorChanger.setMaximumWidth(60)

        self.slider_colorChanger.setVisible(False)
        self.SpinBox_colorChanger.setVisible(False)
        self.slider_colorChanger.setValue(1500)
        self.SpinBox_colorChanger.setValue(1500/100)






        #LEFT BOTTOM layouts

        layout_maximumIterations = QHBoxLayout()
        self.slider_max_Itterations = QSlider(Qt.Horizontal, self)
        self.slider_max_Itterations.setFocusPolicy(Qt.StrongFocus)
        self.slider_max_Itterations.setTickPosition(QSlider.TicksBothSides) 
        self.slider_max_Itterations.setTickInterval(1)
        self.slider_max_Itterations.setSingleStep(1)
        self.slider_max_Itterations.setRange(0, 25)
        self.slider_max_Itterations.valueChanged.connect(self.setMaxItterations)
        self.slider_max_Itterations.setMaximumWidth(150)

        self.SpinBox_max_Itterations = QSpinBox(self)
        self.SpinBox_max_Itterations.setSuffix('n')
        self.SpinBox_max_Itterations.setRange(0, 25)
        self.SpinBox_max_Itterations.setSingleStep(1)
        self.SpinBox_max_Itterations.valueChanged.connect(self.setMaxItterations)
        self.SpinBox_max_Itterations.setMaximumWidth(60)

        self.slider_max_Itterations.setValue(10)
        self.SpinBox_max_Itterations.setValue(10)

        
        self.Dial_Zoom_View_ChangeUP = False
        self.Dial_Zoom_View_GreenZONE = False
        layout_viewport = QHBoxLayout()
        self.Dial_Zoom_View = QDial(self)
        self.Dial_Zoom_View.setFocusPolicy(Qt.StrongFocus)
        self.Dial_Zoom_View.setSingleStep(1)
        self.Dial_Zoom_View.setRange(1,   101)
        self.Dial_Zoom_View.valueChanged.connect(lambda v: self.SpinBox_Zoom_View.setValue(v/100))
        self.Dial_Zoom_View.setMaximumSize(60, 60)

        self.SpinBox_Zoom_View = QDoubleSpinBox(self)
        self.SpinBox_Zoom_View.setSuffix('z')
        self.SpinBox_Zoom_View.setRange(0.01, 1.01)
        self.SpinBox_Zoom_View.setSingleStep(0.01)
        self.SpinBox_Zoom_View.valueChanged.connect(lambda v: self.setZoomView(v))
        self.SpinBox_Zoom_View.setMaximumWidth(60)

        self.Dial_Zoom_View.setValue(100)
        #self.SpinBox_Zoom_View.setValue(1)

        self.Dial_Fractal_Rotation = QDial(self)
        self.Dial_Fractal_Rotation.setFocusPolicy(Qt.StrongFocus)
        self.Dial_Fractal_Rotation.setWrapping(True)
        self.Dial_Fractal_Rotation.setSingleStep(1)
        self.Dial_Fractal_Rotation.setRange(-180*100,   180*100)
        self.Dial_Fractal_Rotation.valueChanged.connect(lambda v: self.SpinBox_Fractal_Rotation.setValue(v/100))
        self.Dial_Fractal_Rotation.setMaximumSize(60, 60)

        self.SpinBox_Fractal_Rotation = QDoubleSpinBox(self)
        self.SpinBox_Fractal_Rotation.setSuffix('R')
        self.SpinBox_Fractal_Rotation.setRange(-180, 180)
        self.SpinBox_Fractal_Rotation.setSingleStep(0.01)
        self.SpinBox_Fractal_Rotation.valueChanged.connect(lambda v: self.setStartingPointRotationAngle(v))
        self.SpinBox_Fractal_Rotation.setMaximumWidth(60)

        self.Dial_Fractal_Rotation.setValue(0)
        self.SpinBox_Fractal_Rotation.setValue(0)




        #adding layouts in LEFT side
        #LEFT TOP
        layout_leftTopMenu.addLayout(layout_angle)
        layout_angle.addWidget(self.slider_Angle)
        layout_angle.addWidget(self.SpinBox_Angle)

        layout_leftTopMenu.addLayout(layout_Initial_Branch_Length)
        layout_Initial_Branch_Length.addWidget(self.slider_Initial_Length)
        layout_Initial_Branch_Length.addWidget(self.SpinBox_Initial_Length)

        layout_leftTopMenu.addLayout(layout_Initial_Length_Ratio)
        layout_Initial_Length_Ratio.addWidget(self.slider_Initial_Length_Ratio)
        layout_Initial_Length_Ratio.addWidget(self.SpinBox_Initial_Length_Ratio)

        layout_leftTopMenu.addLayout(layout_singleBranch)
        layout_singleBranch.addWidget(self.slider_RightBranch_Length_Ratio)
        layout_singleBranch.addWidget(self.SpinBox_RightBranch_Length_Ratio)
        layout_singleBranch.addWidget(self.slider_LeftBranch_Length_Ratio)
        layout_singleBranch.addWidget(self.SpinBox_LeftBranch_Length_Ratio)

        layout_leftTopMenu.addLayout(layout_knotPosition)
        layout_knotPosition.addWidget(self.slider_Knot_Position_Ratio)
        layout_knotPosition.addWidget(self.SpinBox_Knot_Position_Ratio)

        layout_leftTopMenu.addLayout(layout_colorChanger)
        layout_colorChanger.addWidget(self.slider_colorChanger)
        layout_colorChanger.addWidget(self.SpinBox_colorChanger)


        #LEFT BOTTOM
        layout_leftBottomMenu.addLayout(layout_maximumIterations)
        layout_maximumIterations.addWidget(self.SpinBox_max_Itterations)
        layout_maximumIterations.addWidget(self.slider_max_Itterations)

        layout_leftBottomMenu.addLayout(layout_viewport)
        layout_viewport.addWidget(self.SpinBox_Zoom_View)
        layout_viewport.addWidget(self.Dial_Zoom_View)
        layout_viewport.addWidget(self.Dial_Fractal_Rotation)
        layout_viewport.addWidget(self.SpinBox_Fractal_Rotation)
        

        



        #main layout
        layout = QHBoxLayout()                  #MAIN        panel
        layout.addLayout(layout_leftMenu)       #LEFT   side panel
        layout.addLayout(layout_rightSide)      #RIGHT  side panel
        
        self.window = QWidget()
        self.window.setLayout(layout)
        self.setCentralWidget(self.window)
        
        self.show()
    #__init__##################################     End of constructor   ################################

    #MENU_Bar OPTIONS:
    def saveFractalAsSVG(self):
        print('Zapisywanie wav...')
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getOpenFileName()", "", options=options)
        fileName += ".svg"
        self.fractal_Tree_Field.SVG_fileName = fileName
        if(fileName != ".svg"):
            self.fractal_Tree_Field.SVG_saving = True
        
        self.update()

    def exit_program(self):
        print('Wychodzę')
        os._exit(0)
    def about_program(self):
        print('Developera nie ma w domu')
    def switch_ON__Antialiasing(self, checkBox_STATE):
        self.fractal_Tree_Field.switch_ON__Antialiasing(checkBox_STATE)

    def switch_ON__Distinguish_LeftRight_Branch(self, checkBox_STATE):
        self.fractal_Tree_Field.switch_ON__Distinguishing_By_LeftRight_Branch(checkBox_STATE)

    def setFractalPosition(self, fTree_FRACTAL_POSITION):
        self.fractal_Tree_Field.setDrawingPointPosition(fTree_FRACTAL_POSITION)

    def setShape(self, fTree_shape_KEY_NAMES):
        self.fractal_Tree_Field.setDrawingShape(fTree_shape_KEY_NAMES)

    def setBrush_Thickness(self, value):
        self.fractal_Tree_Field.setBrushThickness(value)

        for child in self.Menu_painterBrush_Thickness.actions():
            child.setChecked(False)
        self.sender().setChecked(True)

        self.update()

    def setColor_HSV_Ratio(self, value):
        self.fractal_Tree_Field.setColor_HSV_Ratio(int(value))
    def showColorChanger(self):
        if(self.brush_Color_pallete_Ratio.isChecked()):
            self.slider_colorChanger.setVisible(True)
            self.SpinBox_colorChanger.setVisible(True)
        else:
            self.slider_colorChanger.setVisible(False)
            self.SpinBox_colorChanger.setVisible(False)
        self.update()

    #handling FRACTAL TREE FIELD                            #left panel could handle multiple fractal classes,      although python isn't good for passing obj referencess
    def setAngleValue(self, value, fractal):                #it's easier to call 2 func for each QWidget            although this is more efficient and cleaner way 
        fractal.setAngleValue(value/100)

        if(type(value) == int):                             #checks from whom[spinbox/slider] recieves arguments
            self.SpinBox_Angle.setValue(value/100)
        if(type(value) == float):
            self.slider_Angle.setValue(int(value))
        self.update()

    def setMaxItterations(self, value):
        self.fractal_Tree_Field.setMaxItterations(value)
        
        if(self.slider_max_Itterations.value != value):
            self.slider_max_Itterations.setValue(value)
        if(self.SpinBox_max_Itterations.value != value):
            self.SpinBox_max_Itterations.setValue(value)
        self.update()

    def setInitialBranchLength(self, value):
        self.fractal_Tree_Field.setInitialBranchLength(value)
        
        if(self.slider_Initial_Length.value != value):
            self.slider_Initial_Length.setValue(value)
        if(self.SpinBox_Initial_Length.value != value):
            self.SpinBox_Initial_Length.setValue(value)
        self.update()
        
    def setInitialLengthRatio(self, value):
        self.fractal_Tree_Field.setInitialLengthRatio(value)

        self.slider_Initial_Length_Ratio.setValue(int(value*100))
        self.update()

    def setRightBranchLengthRatio(self, value):
        self.fractal_Tree_Field.setRightBranchLengthRatio(value/100)

        if(type(value) == int):                             #checks from whom[spinbox/slider] recieves arguments
            self.SpinBox_RightBranch_Length_Ratio.setValue(value/100)
        if(type(value) == float):
            self.slider_RightBranch_Length_Ratio.setValue(int(value))
        self.update()
    
    def setLeftBranchLengthRatio(self, value):
        self.fractal_Tree_Field.setLeftBranchLengthRatio(value/100)

        if(type(value) == int):                             #checks from whom[spinbox/slider] recieves arguments
            self.SpinBox_LeftBranch_Length_Ratio.setValue(value/100)
        if(type(value) == float):
            self.slider_LeftBranch_Length_Ratio.setValue(int(value))
        self.update()

    def setKnotPositionRatio(self, value):
        self.fractal_Tree_Field.setKnotPositionRatio(value/100)

        if(type(value) == int):                             #checks from whom[spinbox/slider] recieves arguments
            self.SpinBox_Knot_Position_Ratio.setValue(value/100)
        if(type(value) == float):
            self.slider_Knot_Position_Ratio.setValue(int(value))
        self.update()

    def setZoomView(self, value):                                                                           #this function is my masterpiece
        self.fractal_Tree_Field.setZoomView(value)

        self.Dial_Zoom_View.setValue(int(value*100))

        if(value>2 or value<0.85):
            self.Dial_Zoom_View_GreenZONE = False
        if(value>=1.01 and self.Dial_Zoom_View_ChangeUP == False and self.Dial_Zoom_View_GreenZONE==False):
            self.Dial_Zoom_View.setInvertedAppearance(True)
            self.Dial_Zoom_View.setRange(99,   1099)
            self.SpinBox_Zoom_View.setRange(0.99, 10.99)
            self.Dial_Zoom_View_ChangeUP = True
            self.Dial_Zoom_View_GreenZONE = True 
        if(value<=0.99 and self.Dial_Zoom_View_ChangeUP==True and self.Dial_Zoom_View_GreenZONE==False):        
            
            self.Dial_Zoom_View.setInvertedAppearance(False)
            self.Dial_Zoom_View.setRange(1,   101)
            self.SpinBox_Zoom_View.setRange(0.01, 1.01)
            self.Dial_Zoom_View_ChangeUP = False
            self.Dial_Zoom_View_GreenZONE = True
        self.update()
        
    def setStartingPointRotationAngle(self, value):
        self.fractal_Tree_Field.setStartingPointRotationAngle(value)

    
############################################## CLASS END ########################################################    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()