import sys
from PyQt6.QtWidgets import QApplication
from ui.command_bar import CommandBar

app = QApplication(sys.argv)

window = CommandBar()
window.show()

sys.exit(app.exec())