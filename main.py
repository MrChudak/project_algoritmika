# # from PyQt5.QtCore import Qt

# # from PyQt5.QtWidgets import QApplication, QWidget

# # app = QApplication([])


# # class My_widget(QWidget):
# #     def __init__(self):
# #         super().__init__()

# import matplotlib as mlp

# import matplotlib.pyplot as plt

# import numpy as np



# # list_x = []
# # list_y = []
# # x = -10
# # for i in range(20):
    
# #     list_x.append(x)
# #     y = ((x + 3) ** 2) - 12
# #     list_y.append(y)
# #     x += 1
# # fig, ax = plt.subplots()
# # ax.plot(list_x, list_y)


# # ax.set_xlabel('текст под абсцисой')
# # ax.set_ylabel('текст у ординаты')
# # ax.set_title('заголовок')
# # ax.legend(9)

# fig = plt.figure()

# fig.suptitle(r'$\alpha^1 > \beta_i$')

# plt.show()
# print('start')





# print('end')



from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMenuBar, QMenu, QToolBar
import sys





class Window(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setWindowTitle('Изменение менюшки')
        self.resize(700, 500)
        self.central_Label = QLabel('hello world!')
        self.central_Label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.central_Label)


        self._createMenuBar()
        self._createToolBars()


    def _createMenuBar(self):
        menuBar = self.menuBar()

        fileMenu = QMenu("File", self) # ! "&amp" - не работает
        menuBar.addMenu(fileMenu)

        editMenu = menuBar.addMenu('Edit')
        helpMenu = menuBar.addMenu('Help')


    def _createToolBars(self):

        # using Title
        fileToolBar = self.addToolBar('File')

        # using a ToolBar object
        editToolBar = QToolBar('Edit', self)
        self.addToolBar(editToolBar)

        # using a QToolBar object and a ToolBar Area
        helpToolBar = QToolBar('Help', self)
        self.addToolBar(Qt.LeftToolBarArea, helpToolBar)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = Window()
    mw.show()
    sys.exit(app.exec_())



















































































