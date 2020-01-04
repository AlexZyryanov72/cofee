import sqlite3, sys
from PyQt5.Qt import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QMessageBox
from main1 import Ui_MainWindow
from addEditCoffeeForm import Ui_Dialog


class Correct(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        con = sqlite3.connect("data\coffee.db")
        cur = con.cursor()
        result = cur.execute("SELECT name FROM type").fetchall()
        con.close()
        self.id = -1
        self.comboBox_ground.addItems([item[0] for item in result])
        self.pushButton_ok.clicked.connect(self.save_results)
        self.pushButton_no_ok.clicked.connect(self.back)

    def back(self):
        self.hide()
        ex.run()

    def save_results(self):
        if (not(self.lineEdit_description.text() == '' or self.lineEdit_price.text() == '' or
                self.lineEdit_volume.text() == '' or self.lineEdit_frying.text() == ''
                or self.lineEdit_sort.text() == '')) and (self.lineEdit_price.text().isdigit()
                                                          and self.lineEdit_volume.text().isdigit()):
            con = sqlite3.connect("data\coffee.db")
            sp = [self.lineEdit_sort.text(), self.lineEdit_frying.text(),
                  str(self.comboBox_ground.currentIndex() + 1),
                  self.lineEdit_description.text(), self.lineEdit_price.text(),
                  self.lineEdit_volume.text()]
            cur = con.cursor()
            result = cur.execute("SELECT * FROM cof").fetchall()
            if self.id == -1:
                result_2 = cur.execute("INSERT INTO cof(" + ", ".join([col[0] for col in cur.description][1:])
                                       + ") VALUES(" + '"' + '", "'.join(sp) + '"' + ")")
            else:
                for i, item in enumerate([col[0] for col in cur.description][1:]):
                    result_2 = cur.execute('UPDATE cof SET ' + item + ' = "' + sp[i] + '" WHERE ID="' + self.id + '"')
            con.commit()
            con.close()
            self.hide()
            ex.run()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setWindowTitle("Error")
            msg.exec_()


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.cor = Correct()
        super().__init__()
        self._correct = False
        self.setupUi(self)
        self.run()
        self.pushButton.clicked.connect(self.add)
        self.tableWidget.cellDoubleClicked.connect(self.redact)

    def get_stroka(self):
        return self._stroka

    def redact(self, row, col):
        self._stroka = 'SELECT ID FROM cof WHERE '
        self.cor.lineEdit_volume.setText(self.tableWidget.item(row, 6).text())
        self.cor.lineEdit_price.setText(self.tableWidget.item(row, 5).text())
        self.cor.lineEdit_description.setText(self.tableWidget.item(row, 4).text())
        self.cor.lineEdit_frying.setText(self.tableWidget.item(row, 2).text())
        self.cor.lineEdit_sort.setText(self.tableWidget.item(row, 1).text())
        self.cor.comboBox_ground.setCurrentText(self.tableWidget.item(row, 3).text())
        self.cor.id = self.tableWidget.item(row, 0).text()
        self._flag2 = True
        self._row = row
        self.cor.show()

    def add(self):
        self.cor.id = -1
        self.cor.lineEdit_sort.setText('')
        self.cor.lineEdit_frying.setText('')
        self.cor.lineEdit_description.setText('')
        self.cor.lineEdit_price.setText('')
        self.cor.lineEdit_volume.setText('')
        self.cor.comboBox_ground.setCurrentIndex(0)
        self.cor.show()
        self._correct = True

    def run(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        con = sqlite3.connect("data\coffee.db")
        con.commit()
        cur = con.cursor()
        result = cur.execute("SELECT cof.ID, cof.sort, cof.frying, type.name, cof.description, cof.price, cof.volume"
                             " FROM cof, type WHERE type.ID == cof.ground").fetchall()
        if result != []:
            self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnWidth(0, 0)
            for i in range(len(result)):
                for j in range(len(result[0])):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(result[i][j])))
            for t in range(len(result[0])):
                self.tableWidget.setHorizontalHeaderItem(t, QTableWidgetItem(cur.description[t][0]))
        con.commit()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())