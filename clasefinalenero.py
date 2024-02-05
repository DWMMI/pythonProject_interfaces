import os

from DI_U04_A02_01 import CronometroUI
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMessageBox, QSystemTrayIcon, QMenu

import DI_U04_A03_03

@Slot()
def mostrar_ocultar():
    if cronometro.isHidden():
        cronometro.show()
    else:
        cronometro.hide()

@Slot()
def mostrar_aviso(mensaje):
    QMessageBox.information(cronometro, "Cronómetro PySide6", mensaje)

if __name__ == "__main__":

    app = QApplication([])

    # Asignamos el icono de la ventana
    app.setWindowIcon(QIcon("icons/cronometro.png"))

    # Agregamos la aplicacion al tray
    icon = QIcon("icons/cronometro.png")
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    tray.activated.connect(mostrar_ocultar)

    # Creamos un componente cronómetro
    cronometro = CronometroUI()

    # Cambiamos las propiedades del componente
    cronometro.setWindowTitle("Cronómetro PySide6")

    # Para que sea siempre visible
    cronometro.setWindowFlags(Qt.WindowStaysOnTopHint)

    # Creamos un QAction y lo conectamos al slot quit, para cerrar la aplicación
    accion_salir = QAction("Salir", cronometro)
    accion_salir.triggered.connect(app.quit)

    # Creamos un menú y añadimos la accion
    menu = QMenu()
    menu.addAction(accion_salir)

    # Añadimos la señal del componente
    cronometro.mensaje.connect(mostrar_aviso)

    cronometro.show()
    app.exec()
