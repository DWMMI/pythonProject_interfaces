from PySide6.QtWidgets import QApplication, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel
from PySide6.QtGui import QIcon, QAction

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo de uso de slot predefinido")
        self.setFixedSize(300,30)
        self.mostrar=QIcon("mostrar.png")
        self.line_edit = QLineEdit(self)

        # Fijamos el tamaño del line edit
        self.line_edit.setFixedSize(150, 30)
        self.line_edit.setMaxLength(25)

        # Crear la accion y conectarla al slor cambiar visibilidad
        self.action_cambiar_visibilidad = QAction(self.mostrar, "Mostrar", self)
        self.action_cambiar_visibilidad.triggered.connect(self.cambiar_visibilidad)

        # Agragar la accion al QLineEdit
        self.line_edit.addAction(self.action_cambiar_visibilidad, QLineEdit.TrailingPosition)

        self.etiqueta1= QLabel("self")
        self.etiqueta1.setFixedSize(150, 30) # Establecemos el mismo tamaño que el QLineEdit
        self.etiqueta1.move(150,0)

        # Conectamos el evento textChanged del QLineEdit al slot setText del Label
        self.line_edit.textChanged.connect(self.etiqueta1.setText)

    def cambiar_visibilidad(self):
        print("Hola mundo")

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()