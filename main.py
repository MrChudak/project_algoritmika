
# Источник кода: https://dev-gang.ru/article/python-i-pyqt-sozdanie-menu-panelei-instrumentov-i-strok-sostojanija-l7ubf6mm7n/
from PyQt5.QtCore import Qt, QUrl
# from PyQt5.QtWebKitWidgets import QWebView
# from PyQt5.QtWebKit import QWebView
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMenuBar, QMenu, QToolBar, QAction, QTextEdit, QDockWidget
import sys
import markdown




class Window(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setWindowTitle('School Helper')
        self.resize(700, 500)
        self.central_Label = QLabel('Welcome!') #! central_Label
        self.central_Label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.central_Label)


        self._createAction()
        self._createMenuBar()
        self._createToolBars()
        self._connectActions()
        self._init_web()


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
        helpMenu.addAction(self.graph_action)
        helpMenu.addAction(self.txt_action)
        

        geometryMenu = helpMenu.addMenu('Фигура')
        geometryMenu.addAction(self.two_d_figure_action) 
        geometryMenu.addAction(self.three_d_figure_action)


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

        self.open_action = QAction(self)
        self.open_action.setText('Open') # openAction

        self.close_action = QAction('Close', self) # closeAction
        self.save_action = QAction('Save', self) # saveAction
        self.exit_action = QAction('Exit', self) # exitAction
        self.copy_action = QAction('Copy', self) # copyAction 
        self.paste_action = QAction('Paste', self) # pasteAction 
        self.cut_action = QAction('Cut', self) # cutAction 
        self.two_d_figure_action = QAction('2D фигура', self)
        self.three_d_figure_action = QAction('3D фигура', self)
        self.graph_action = QAction('График', self) # graph_Action
        self.txt_action = QAction('Текст', self) # aboutAction
        # self.geometryAction = QAction('Фигура', self)


    def _init_web(self):
        
        self.web = QWebEngineView()
        







    def click_text(self):
        # menuBar = self.menuBar()
        fileMenu = QMenu("Текст", self)
        fileMenu.addAction(self.open_action)
        fileMenu.addAction(self.save_action)
        # self.menuBar().removeMenu(helpMenu)
        self.menuBar().addMenu(fileMenu)

    
    def click_graph(self):
        graficMenu = QMenu('График', self)
        
        self.menuBar().addMenu(graficMenu)
    

    def click_open(self):
        self.central_Label.hide()
        # self.left_Text_Edit = QTextEdit('Текст')
        self.right_result = QTextEdit()
        # self.right_result = QLabel("лол")
        # self.left_Text_Edit.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        # self.right_result.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # self.setCentralWidget(self.left_Text_Edit)
        
        self.setCentralWidget(self.right_result)
        
    
    def click_save(self):
        self.update()

    
    def click_2d_figure(self):
        print('click...')

    def click_3d_figure(self):
        print('click...')





    def update(self):
        text = self.right_result.toPlainText()
        with open("test.md", 'w', encoding = "UTF-8") as f_md:
            f_md.write(text)
        with open("test.md", 'r', encoding = "UTF-8") as f_md:
            text_md = f_md.read()
            text_html = markdown.markdown(text_md, extensions = ['extra'])
            # print(text_html)
        with open('test.html', 'w', encoding = 'UTF-8') as f_html:
            f_html.write(text_html)
        
        
        with open('test.html', 'r', encoding = 'UTF-8') as f_html:
            text_html = f_html.read() 
            self.web.setHtml(text_html)

        self.right_result.hide()
        self.setCentralWidget(self.web)
        
        



    def _connectActions(self):
        self.txt_action.triggered.connect(self.click_text)
        self.graph_action.triggered.connect(self.click_graph)
        self.two_d_figure_action.triggered.connect(self.click_2d_figure)
        self.three_d_figure_action.triggered.connect(self.click_3d_figure)
        

        # TODO: Тестовый сопособ под запись кнопки open и save внутри меню "текст" для проверки работы с .md и .html файлами
        self.open_action.triggered.connect(self.click_open)
        self.save_action.triggered.connect(self.click_save)
        



    





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = Window()
    mw.show()
    # mw.helpMenu.clicked.connect(mw.test_god())
    sys.exit(app.exec_())



















































































