# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'livre1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import mysql.connector
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets , uic
from PyQt5.QtWidgets import QLabel, QLineEdit, QSpinBox, QScrollArea, QComboBox, QPushButton, QDateTimeEdit, QWidget, QMainWindow, QTextEdit
class Ui_MainWindow(object):
    def init_database_connection(self):
        try:
            self.cnx = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='library'
            )
            self.cursor = self.cnx.cursor(dictionary=True)
        except mysql.connector.Error as err:
            print(f"Erreur de connexion à la base de données : {err}")

    def close_database_connection(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'cnx') and self.cnx.is_connected():
            self.cnx.close()
class MainWindow(QMainWindow, Ui_MainWindow):
    def closeEvent(self, event):
        self.close_database_connection()
        event.accept()
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("livre1.ui", self)
        self.init_database_connection()
        self.populate_combobox_arme()
        self.populate_combobox_disciplines()
        self.populate_chapitre_text_and_combobox()
        self.chapitre.currentIndexChanged.connect(self.update_texte_chapitre)
        self.livre.currentIndexChanged.connect(self.update_chapitres)
        self.textEdit.textChanged.connect(self.update_chapitre_from_text)
    def update_texte_chapitre(self,index):
        selected_chapitre = self.chapitre.currentText()
        query_chapitre = f"SELECT texte FROM chapitre WHERE no_chapitre = '{selected_chapitre}';"
        self.cursor.execute(query_chapitre)
        chapitre_text = self.cursor.fetchone()["texte"].decode('utf-8')
        self.textEdit.setPlainText(chapitre_text)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 822)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titrelivre = QtWidgets.QLabel(self.centralwidget)
        self.titrelivre.setGeometry(QtCore.QRect(410, 10, 251, 101))
        self.titrelivre.setObjectName("titrelivre")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 600, 341, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.champnom_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.champnom_2.setObjectName("champnom_2")
        self.verticalLayout.addWidget(self.champnom_2)
        self.nom_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.nom_2.setObjectName("nom_2")
        self.verticalLayout.addWidget(self.nom_2)
        self.champdate = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.champdate.setObjectName("champdate")
        self.verticalLayout.addWidget(self.champdate)
        self.date = QtWidgets.QDateTimeEdit(self.verticalLayoutWidget)
        self.date.setObjectName("date")
        self.verticalLayout.addWidget(self.date)
        self.sauvegarder = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sauvegarder.setObjectName("sauvegarder")
        self.sauvegarder.clicked.connect(self.on_sauvegarder_clicked)
        self.verticalLayout.addWidget(self.sauvegarder)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 80, 341, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.nouvellepartie = QtWidgets.QLabel(self.gridLayoutWidget)
        self.nouvellepartie.setObjectName("nouvellepartie")
        self.gridLayout.addWidget(self.nouvellepartie, 0, 0, 1, 2)
        self.livre = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.livre.setObjectName("livre")
        self.gridLayout.addWidget(self.livre, 1, 1, 1, 1)
        self.nom = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.nom.setObjectName("nom")
        self.gridLayout.addWidget(self.nom, 5, 1, 1, 1)
        self.champnom = QtWidgets.QLabel(self.gridLayoutWidget)
        self.champnom.setObjectName("champnom")
        self.gridLayout.addWidget(self.champnom, 5, 0, 1, 1)
        self.champlivre = QtWidgets.QLabel(self.gridLayoutWidget)
        self.champlivre.setObjectName("champlivre")
        self.gridLayout.addWidget(self.champlivre, 1, 0, 1, 1)
        self.creer = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.creer.setObjectName("creer")
        self.gridLayout.addWidget(self.creer, 6, 0, 1, 2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 310, 341, 151))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.suprimer = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.suprimer.setObjectName("suprimer")
        self.gridLayout_2.addWidget(self.suprimer, 3, 0, 1, 1)
        self.charger = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.charger.setObjectName("charger")
        self.gridLayout_2.addWidget(self.charger, 3, 1, 1, 1)
        self.selectsauvegarde = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.selectsauvegarde.setObjectName("selectsauvegarde")
        self.gridLayout_2.addWidget(self.selectsauvegarde, 2, 0, 1, 2)
        self.champsauvegarde = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.champsauvegarde.setObjectName("champsauvegarde")
        self.gridLayout_2.addWidget(self.champsauvegarde, 0, 0, 1, 2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(710, 430, 361, 241))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.discipline = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.discipline.setObjectName("discipline")
        self.verticalLayout_2.addWidget(self.discipline)
        self.disciplinmax = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.disciplinmax.setObjectName("disciplinmax")
        self.verticalLayout_2.addWidget(self.disciplinmax)
        self.discipline1 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.discipline1.setObjectName("discipline1")
        self.verticalLayout_2.addWidget(self.discipline1)
        self.discipline2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.discipline2.setObjectName("discipline2")
        self.verticalLayout_2.addWidget(self.discipline2)
        self.discipline5 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.discipline5.setObjectName("discipline5")
        self.verticalLayout_2.addWidget(self.discipline5)
        self.discipline4 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.discipline4.setObjectName("discipline4")
        self.verticalLayout_2.addWidget(self.discipline4)
        self.discipline3 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.discipline3.setObjectName("discipline3")
        self.verticalLayout_2.addWidget(self.discipline3)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(380, 660, 291, 121))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.champchapitre = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.champchapitre.setObjectName("champchapitre")
        self.verticalLayout_3.addWidget(self.champchapitre)
        self.chapitre = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.chapitre.setObjectName("chapitre")
        self.verticalLayout_3.addWidget(self.chapitre)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(710, 700, 311, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bourse = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.bourse.setObjectName("bourse")
        self.horizontalLayout.addWidget(self.bourse)
        self.montant = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.montant.setObjectName("montant")
        self.horizontalLayout.addWidget(self.montant)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(710, 270, 361, 141))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.champarme = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.champarme.setObjectName("champarme")
        self.verticalLayout_4.addWidget(self.champarme)
        self.armemax = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.armemax.setObjectName("armemax")
        self.verticalLayout_4.addWidget(self.armemax)
        self.arme2 = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.arme2.setObjectName("arme2")
        self.verticalLayout_4.addWidget(self.arme2)
        self.arme1 = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.arme1.setObjectName("arme1")
        self.verticalLayout_4.addWidget(self.arme1)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(710, 30, 361, 81))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.champsacados = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.champsacados.setObjectName("champsacados")
        self.verticalLayout_5.addWidget(self.champsacados)
        self.sacados = QtWidgets.QLineEdit(self.centralwidget)
        self.sacados.setGeometry(QtCore.QRect(710, 120, 361, 131))
        self.sacados.setObjectName("sacados")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(380, 170, 291, 431))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.livre.currentIndexChanged.connect(self.update_chapitres)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titrelivre.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Livre</span></p></body></html>"))
        self.champnom_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Nom :</span></p></body></html>"))
        self.champdate.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Date création</span></p></body></html>"))
        self.sauvegarder.setText(_translate("MainWindow", "Sauvegarder"))
        self.nouvellepartie.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Nouvelle Partie </span></p></body></html>"))
        self.champnom.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Nom :</p></body></html>"))
        self.champlivre.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">livre :</p></body></html>"))
        self.creer.setText(_translate("MainWindow", "Créer"))
        self.suprimer.setText(_translate("MainWindow", "Suprimer"))
        self.charger.setText(_translate("MainWindow", "Charger"))
        self.champsauvegarde.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Selectionner une sauvegarde</span></p></body></html>"))
        self.discipline.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Disciplines</span></p></body></html>"))
        self.disciplinmax.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic; text-decoration: underline;\">5 discipline maximum</span></p></body></html>"))
        self.champchapitre.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">CHAPITRES :</span></p></body></html>"))
        self.bourse.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">BOURSE :</span></p></body></html>"))
        self.montant.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.champarme.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">ARME</span></p></body></html>"))
        self.armemax.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic; text-decoration: underline;\">2 arme maximum</span></p></body></html>"))
        self.champsacados.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">SAC À DOS :</span></p></body></html>"))
    def populate_combobox_arme(self):
        self.arme1.clear()
        self.arme2.clear()
        query = "SELECT arme FROM arme;"
        self.cursor.execute(query)
        for ligne in self.cursor:
            arme = ligne["arme"]
            self.arme1.addItem(arme)
            self.arme2.addItem(arme)
    def populate_combobox_disciplines(self):
        self.discipline1.clear()
        self.discipline2.clear()
        self.discipline3.clear()
        self.discipline4.clear()
        self.discipline5.clear()
        query = "SELECT discipline FROM discipline;"
        self.cursor.execute(query)
        for ligne in self.cursor:
            discipline = ligne["discipline"]
            self.discipline1.addItem(discipline)
            self.discipline2.addItem(discipline)
            self.discipline3.addItem(discipline)
            self.discipline4.addItem(discipline)
            self.discipline5.addItem(discipline)
    def populate_chapitre_text_and_combobox(self):
        query_chapitre = "SELECT texte FROM chapitre WHERE no_chapitre = '1';"
        self.cursor.execute(query_chapitre)
        chapitre_text = self.cursor.fetchone()["texte"].decode('utf-8')
        self.textEdit.setPlainText(chapitre_text)
        query_lien_chapitre = "SELECT no_chapitre_destination FROM lien_chapitre WHERE no_chapitre_origine = '1';"
        self.cursor.execute(query_lien_chapitre)
        self.chapitre.addItem("Aucun")
        for ligne in self.cursor:
            no_chapitre_destination = ligne["no_chapitre_destination"]
            self.chapitre.addItem(str(no_chapitre_destination))
    def update_chapitres(self):
        selected_livre = self.livre.currentText()
        query = f"SELECT chapitre FROM chapitre WHERE livre_id = (SELECT id FROM livre WHERE nom = '{selected_livre}');"
        self.cursor.execute(query)
        chapitres = [chapitre["chapitre"] for chapitre in self.cursor.fetchall()]
        self.chapitre.clear()
        for ligne in self.cursor:
            no_chapitre_destination = ligne["no_chapitre_destination"]
            self.chapitre.addItem(str(no_chapitre_destination))
    def update_chapitre_from_text(self):
    # Récupérez le numéro du chapitre actuellement affiché dans la zone de texte
        current_chapitre = self.textEdit.toPlainText().strip()
        index = self.chapitre.findText(current_chapitre)
        if index != -1:
            self.chapitre.setCurrentIndex(index)


    def update_texte_chapitre(self, index):
        selected_chapitre = self.chapitre.currentText()
        query_chapitre = f"SELECT texte FROM chapitre WHERE no_chapitre = '{selected_chapitre}';"
        self.cursor.execute(query_chapitre)
        chapitre_text = self.cursor.fetchone()["texte"].decode('utf-8')
        self.textEdit.setPlainText(chapitre_text)
    def on_sauvegarder_clicked(self):
        nom_personnage = self.nom_2.text()
        if nom_personnage:
            livre_id = "1"
            query_insert_personnage = f"INSERT INTO personnage (id_livre, nom) VALUES ({livre_id}, '{nom_personnage}');"
            self.cursor.execute(query_insert_personnage)
            self.cnx.commit()
        else:
            QtWidgets.QMessageBox.warning(self, "Erreur", "Veuillez entrer un nom pour le personnage.")
        self.nom_2.clear()



