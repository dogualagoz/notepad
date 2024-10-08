import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog,QMainWindow, qApp,QAction

class Notepad(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    
    def init_ui(self):
        
        self.yazi_alani = QTextEdit()

        self.temizle = QPushButton("Temizle")
        
        self.ac = QPushButton("Aç")
        
        self.kaydet = QPushButton("Kaydet")

        h_box = QHBoxLayout()

        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("Not Defteri")
        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)
        

    def yaziyi_temizle(self):
        self.yazi_alani.clear()
    
    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("Desktop")) #Bilgisayardaki seçtiğimiz dosyayı demet olarak döndürür
        print(dosya_ismi)
        
        with open(dosya_ismi[0],"r") as file:
            self.yazi_alani.setText(file.read())
        
    def dosya_kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("Desktop"))

        with open(dosya_ismi[0],"w") as file:
            file.write(self.yazi_alani.toPlainText())

class Menu(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.pencere = Notepad()

        self.setCentralWidget(self.pencere)

        self.menuleri_olustur()

    def menuleri_olustur(self):
        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")

        dosya_ac = QAction("Dosya Aç",self)
        dosya_ac.setShortcut("CTRL+O")

        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("CTRL+S")

        temizle = QAction("Dosya Temizle",self)
        temizle.setShortcut("CTRL+D")

        cikis = QAction("Çıkış",self)
        cikis.setShortcut("CTRL+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)

        dosya.triggered.connect(self.response)

    
        
        self.setWindowTitle("Metin Editörü")

        self.show()

    def response(self,action): #Aşağıdaki işlemleri yukarda self.pencere'de tanımladığımızdan yeniden yazmamıza gerek kalmaz

        if action.text() == "Dosya Aç":
            self.pencere.dosya_ac()
        elif action.text() == "Dosya Kaydet":
            self.pencere.dosya_kaydet()
        elif action.text() == "Dosya Temizle":
            self.pencere.yaziyi_temizle()
        elif action.text() == "Çıkış":
            qApp.quit()


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())