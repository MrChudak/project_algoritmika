
# Источник кода: https://dev-gang.ru/article/python-i-pyqt-sozdanie-menu-panelei-instrumentov-i-strok-sostojanija-l7ubf6mm7n/
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMenuBar, QMenu, QToolBar, QAction
import sys





class Window(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setWindowTitle('Изменение менюшки')
        self.resize(700, 500)
        self.central_Label = QLabel('hello world!')
        self.central_Label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.central_Label)


        self._createAction()
        self._createMenuBar()
        self._createToolBars()


    def _createMenuBar(self):
        menuBar = self.menuBar()

        # fileMenu = QMenu("File", self) # ! "&amp" - не работает
        # menuBar.addMenu(fileMenu)
        # fileMenu.addAction(self.NewAction)
        # fileMenu.addAction(self.openAction)
        # fileMenu.addAction(self.saveAction)
        # fileMenu.addAction(self.exitAction)

        # editMenu = menuBar.addMenu('Edit')
        # editMenu.addAction(self.copyAction)
        # editMenu.addAction(self.pasteAction)
        # editMenu.addAction(self.cutAction)


        helpMenu = menuBar.addMenu('+')
        helpMenu.addAction(self.helpcontent)
        helpMenu.addAction(self.aboutAction)
        

        geometryMenu = helpMenu.addMenu('Фигура')
        geometryMenu.addAction('3D фигура')
        geometryMenu.addAction('2D фигура')


    def _createToolBars(self):

        # using Title
        fileToolBar = self.addToolBar('File')

        # using a ToolBar object
        editToolBar = QToolBar('Edit', self)
        self.addToolBar(editToolBar)

        # using a QToolBar object and a ToolBar Area
        helpToolBar = QToolBar('Help', self)
        self.addToolBar(Qt.LeftToolBarArea, helpToolBar)

    
    def _createAction(self):

        self.NewAction = QAction(self)

        self.NewAction.setText('New')
        self.openAction = QAction('open', self)
        self.saveAction = QAction('save', self)
        self.exitAction = QAction('exit', self)
        self.copyAction = QAction('copy', self)
        self.pasteAction = QAction('paste', self)
        self.cutAction = QAction('cut', self)
        self.helpcontent = QAction('График', self)
        self.aboutAction = QAction('Текст', self)
        # self.geometryAction = QAction('Фигура', self)





    def test_god(self):
        menuBar = self.menuBar()
        fileMenu = QMenu("File", self)
        menuBar.addMenu(fileMenu)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = Window()
    mw.show()
    # mw.helpMenu.clicked.connect(mw.test_god())
    sys.exit(app.exec_())



















































































