from PyQt6.QtWidgets import  QHBoxLayout, QGroupBox, QLineEdit, QWidget, QPushButton
from PyQt6.QtCore import QCoreApplication

class RotateUI(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.rotate_groupbox = QGroupBox(parent)
        self.rotate_groupbox.setTitle("Rotate")
        self.rotate_groupbox.setMaximumWidth(150)
        self.rotate_groupbox.setMaximumHeight(80)
        self.hor_layout = QHBoxLayout(self.rotate_groupbox)
        self.rotate_components_layout = QHBoxLayout()
        self.rotate_line_edit = QLineEdit()
        self.rotate_line_edit.setMinimumWidth(50)
        self.rotate_confirm = QPushButton()
        self.rotate_confirm.setText("Ok")
        self.rotate_confirm.setMinimumWidth(30)
        self.rotate_components_layout.addWidget(self.rotate_line_edit)
        self.rotate_components_layout.addWidget(self.rotate_confirm)
        self.rotate_components_layout.setSpacing(0)
        self.hor_layout.addLayout(self.rotate_components_layout)

        self.__retranslateUI()

    def __retranslateUI(self):
        _translate = QCoreApplication.translate
        self.rotate_line_edit.setToolTip(_translate("MainWindow", "Enter degrees of rotation"))

