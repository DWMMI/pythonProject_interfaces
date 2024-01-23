from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QIcon, QKeySequence

import DI_U04_A02_CP_03
class EditorContrasena(QLineEdit):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.mostrar=QIcon("icons/visible.png")
        self.ocultar=QIcon("icons/hidden.png")

        self.laber=self.setEchoMode(QLineEdit.Password)

        self.setPlaceholderText("Introduce tu contraseña")
        self.accion_cambiar_visibilidad = self.addAction(self.mostrar, QLineEdit.TrailingPosition)

        self.accion_cambiar_visibilidad.setShortcut(QKeySequence("Ctrl+M"))
        self.accion_cambiar_visibilidad.triggered.connect(self.cambiar_visibilidad)

        self.contraseña_visible=False
        self.setWindowIcon(QIcon('self.mostrar'))

    def cambiar_visibilidad(self):
        if not self.contraseña_visible:
            self.setEchoMode(QLineEdit.Normal)
            self.contraseña_visible=True
            self.accion_cambiar_visibilidad.setIcon(self.ocultar)
            self.setWindowIcon(QIcon('self.ocultar'))
        else:
            self.setEchoMode(QLineEdit.Password)
            self.contraseña_visible=False
            self.accion_cambiar_visibilidad.setIcon(self.mostrar)
            self.setWindowIcon(QIcon('self.mostrar'))

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    ventana = EditorContrasena()
    ventana.show()
    sys.exit(app.exec_())