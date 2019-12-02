import sys
import ComprobacionDisenoTuberias as cdt
from PyQt5 import uic,QtWidgets

qtCreatorFile = "ComprobacionDisenoTuberias.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Aqui se declaran los botones a usar :
        self.btn_calcular.clicked.connect(self.calculos_QV)

    
    # Funciòn que se ejecuta al pulsar el botòn:
    def calculos_QV(self):
        p = float(self.txt_p.text())
        u = float(self.txt_u.text())
        H = float(self.txt_H.text())
        L = float(self.txt_L.text())
        d = float(self.txt_d.text())
        ks = float(self.txt_ks.text())
        km = float(self.txt_km.text())
        z2 = float(self.txt_z2.text())
        [Q,V] = cdt.Q_ComprobacionDiseno(L,d,ks,H,km,p,u,z2)
        self.lbl_Q.setText('{:.2f}'.format(Q))
        self.lbl_V.setText('{:.2f}'.format(V))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
