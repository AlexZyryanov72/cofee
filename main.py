import sqlite3, sys
from PyQt5.Qt import QApplication, QMainWindow, QTableWidgetItem
from main1 import Ui_MainWindow

class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.flag = False
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = cur.execute("SELECT * FROM cof").fetchall()
        if result != []:
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setRowCount(len(result))
            for i in range(len(result)):
                for j in range(len(result[0])):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
            for t in range(len(result[0])):
                self.tableWidget.setHorizontalHeaderItem(t, QTableWidgetItem(cur.description[t][0]))
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())