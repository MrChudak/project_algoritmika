
# Источник кода: https://dev-gang.ru/article/python-i-pyqt-sozdanie-menu-panelei-instrumentov-i-strok-sostojanija-l7ubf6mm7n/
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMenuBar, QMenu, QToolBar, QAction, QTextEdit, QDockWidget
import sys
import markdown




class Window(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setWindowTitle('School Helper')
        self.resize(700, 500)
        self.central_Label = QLabel('hello world!')
        self.central_Label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.central_Label)


        self._createAction()
        self._createMenuBar()
        self._createToolBars()
        self._connectActions()


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
        helpMenu.addAction(self.graph_Action)
        helpMenu.addAction(self.aboutAction)
        

        geometryMenu = helpMenu.addMenu('Фигура')
        geometryMenu.addAction('3D фигура')
        geometryMenu.addAction('2D фигура')


    def _createToolBars(self):
        pass
        # # using Title
        # fileToolBar = self.addToolBar('File')

        # # using a ToolBar object
        # editToolBar = QToolBar('Edit', self)
        # self.addToolBar(editToolBar)

        # # using a QToolBar object and a ToolBar Area
        # helpToolBar = QToolBar('Help', self)
        # self.addToolBar(Qt.LeftToolBarArea, helpToolBar)

    
    def _createAction(self):

        self.openAction = QAction(self)

        self.openAction.setText('Open')
        self.closeAction = QAction('Close', self)
        self.saveAction = QAction('save', self)
        self.exitAction = QAction('exit', self)
        self.copyAction = QAction('copy', self)
        self.pasteAction = QAction('paste', self)
        self.cutAction = QAction('cut', self)
        self.graph_Action = QAction('График', self)
        self.aboutAction = QAction('Текст', self)
        # self.geometryAction = QAction('Фигура', self)






    def click_text(self):
        # menuBar = self.menuBar()
        fileMenu = QMenu("Текст", self)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        # self.menuBar().removeMenu(helpMenu)
        self.menuBar().addMenu(fileMenu)

    
    def click_graph(self):
        graficMenu = QMenu('График', self)
        
        self.menuBar().addMenu(graficMenu)
    

    def click_open(self):
        self.central_Label.hide()
        # self.left_Text_Edit = QTextEdit('Текст')
        self.right_result = QLabel("```python\n'жизнь':{\n    'животные': ['кот', 'собака', 'жираф'],\n    'растения': {\n      'не хищные': ['алое', 'кактус', 'хлорофитум'],\n      'хищные': ['непентос раджа', 'жирянка', 'мухоловка', 'сарацения']\n    }\n  }\n```")
        # self.right_result = QLabel("лол")
        # self.left_Text_Edit.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.right_result.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # self.setCentralWidget(self.left_Text_Edit)
        self.setCentralWidget(self.right_result)
        
    
    def click_save(self):
        self.update()





    def update(self):
        # text = self.right_result.text()
        # with open("test.md", 'w', encoding = "UTF-8") as f_md:
        #     f_md.write(text)
        with open("test.md", 'r', encoding = "UTF-8") as f_md:
            text_md = f_md.read()
            text_html = markdown.markdown(text_md, extendions = ['extra'])
            # print(text_html)
        with open('test.html', 'w', encoding = 'UTF-8') as f_html:
            f_html.write(text_html)
        
        with open('test.html', 'r', encoding = "UTF-8") as f_html:
            text_html = f_html.read()

        self.right_result.setText(text_html)


    def _connectActions(self):
        self.aboutAction.triggered.connect(self.click_text)
        self.graph_Action.triggered.connect(self.click_graph)
        

        # TODO: Тестовый сопособ под запись кнопки open и save внутри меню "текст" для проверки работы с .md и .html файлами
        self.openAction.triggered.connect(self.click_open)
        self.saveAction.triggered.connect(self.click_save)
        



    





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = Window()
    mw.show()
    # mw.helpMenu.clicked.connect(mw.test_god())
    sys.exit(app.exec_())



















































































