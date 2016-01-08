#! /usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import json

win_height = 600
win_width = 800

logo = "rslogo.gif"

def testrun():
    print("bye")
    sys.exit()
   
class Window(QMainWindow):

    main_menu = None
    gui_frame  = None
    cmd_frame = None

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.main_menu = self.menuBar()
        self.gui_frame = QWidget()
        self.cmd_frame = None

        self.setWindowIcon( QIcon(logo) )
        self.resize( win_width, win_height )
        self.setWindowTitle("Billin Application")

        # menu bar
        menufile = open('mainMenuEntries.json', 'r')
        self.__addMenuEntries__( self.main_menu, json.load(menufile) )

        # invoice page layout
        # make a layout and add the elemants to it
        gui_layout = QGridLayout()
        #create left phase
        left_phase = QGridLayout()
        invoice_label = QLabel("Tax Invoice")
        company = QHBoxLayout()
        company.addWidget( QLabel("Company:") )
        companyLine = QComboBox()
        company.addWidget( companyLine )
        companyLine.setEditable( True )
        table = QTableWidget(2, 5)
        table.setHorizontalHeaderLabels(["Item Name","Size","Qty","Rate","Total"])
        left_phase.addWidget( invoice_label, 0, 0)
        left_phase.addLayout( company, 1, 0)
        left_phase.addWidget( table, 2, 0)
        #create Right Phase
        right_phase = QGridLayout()
        right_phase.addWidget( QLabel("Date:"), 0, 0 )
        right_phase.addWidget( QLabel("Bill No:"), 1, 0 )
        right_phase.addWidget( QLabel("Total:"), 2, 0 )
        right_phase.addWidget( QLabel("Discount:"), 3, 0 )
        right_phase.addWidget( QComboBox(), 4, 0 )
        right_phase.addWidget( QLabel("Other Charges:"), 5, 0 )
        right_phase.addWidget( QLabel("Total:"), 6, 0 )
        right_phase.addWidget( QLabel("round off:"), 7, 0 )
        right_phase.addWidget( QLabel("Grand total:"), 8, 0 )
        right_phase.addWidget( QLineEdit(), 0, 1 )
        right_phase.addWidget( QLineEdit(), 1, 1 )
        right_phase.addWidget( QLineEdit(), 2, 1 )
        right_phase.addWidget( QLineEdit(), 3, 1 )
        right_phase.addWidget( QLineEdit(), 4, 1 )
        right_phase.addWidget( QLineEdit(), 5, 1 )
        right_phase.addWidget( QLineEdit(), 6, 1 )
        right_phase.addWidget( QLineEdit(), 7, 1 )
        right_phase.addWidget( QLineEdit(), 8, 1 )
        reset_btn = QPushButton("&reset")
        save_btn  = QPushButton("&save")
        right_phase.addWidget( reset_btn, 9, 0 )
        right_phase.addWidget( save_btn, 9, 1 )
        # make an empty widget set the layout in that widget
        gui_layout.addLayout( left_phase, 0, 0 )
        gui_layout.addLayout( right_phase, 0, 3, 1, 2 )
        self.gui_frame.setLayout( gui_layout )
        # set qwigdet as the centralWidget in the window
        self.setCentralWidget( self.gui_frame )

        #add cmd_frame
        #make the layout
        cmd_layout = QHBoxLayout()
        cmd_line = QLineEdit("$:~ ")
        print_select = QCheckBox("Print")
        print_copies = QLineEdit("3")
        cmd_layout.addWidget(cmd_line)
        cmd_layout.addWidget( print_select )
        cmd_layout.addWidget( print_copies )
        #make an empty widget and add the layout to the widget
        someWid = QWidget()
        someWid.setLayout( cmd_layout )
        #add the widget to the dockWidget
        some_dockWidget = QDockWidget()
        some_dockWidget.setWidget( someWid )
        
        self.addDockWidget( Qt.BottomDockWidgetArea, some_dockWidget)
        
        

    def __addMenuEntries__(self, parentObj, dictLst ):
        for dictEle in dictLst:
            if "submenu" in dictEle :
                # does contain a submenu attach it
                temp = parentObj.addMenu("&"+dictEle["tag"])
                self.__addMenuEntries__( temp, dictEle["submenu"])
            else:
                action = QAction("&"+dictEle["tag"], self)
                action.setShortcut( QKeySequence(dictEle["shortcut"]) ) #is not working, bug in ubuntu
                action.setStatusTip( dictEle["toolTip"] )
                action.triggered.connect( testrun )
                parentObj.addAction( action )


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())
