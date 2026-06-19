from PyQt6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QCompleter
from PyQt6.QtCore import Qt
from commands.app_commands import execute_command
from config.commands import COMMANDS


class CommandBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Universal Command Bar")

        # Floating window
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )

        self.setFixedSize(600, 70)

        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                border-radius: 15px;
            }
        """)

        # Input box
        self.command_input = QLineEdit()

        self.command_input.setPlaceholderText(
            "Type a command..."
        )

        self.command_input.setStyleSheet("""
            QLineEdit {
                background-color: #1E1E1E;
                color: white;
                border: 2px solid #3A3A3A;
                border-radius: 12px;
                padding: 12px;
                font-size: 16px;
            }

            QLineEdit:focus {
                border: 2px solid #6A5ACD;
            }
        """)

        # Execute command when Enter is pressed
        self.command_input.returnPressed.connect(
            self.run_command
        )

        layout = QVBoxLayout()
        layout.addWidget(self.command_input)

        self.setLayout(layout)

        self.center_window()

        self.command_input.setFocus()
        
        self.completer = QCompleter(COMMANDS)

        self.completer.setCaseSensitivity(
            Qt.CaseSensitivity.CaseInsensitive
        )

        self.command_input.setCompleter(
            self.completer
        )
        
        self.command_history = []
        self.history_index = -1

    def center_window(self):
        screen = self.screen().availableGeometry()

        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 3

        self.move(x, y)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key.Key_Escape:
            self.close()

        elif event.key() == Qt.Key.Key_Up:

            if self.command_history:

                self.history_index = max(
                    0,
                    self.history_index - 1
                )

                self.command_input.setText(
                    self.command_history[self.history_index]
                )

        elif event.key() == Qt.Key.Key_Down:

            if self.command_history:

                self.history_index = min(
                    len(self.command_history) - 1,
                    self.history_index + 1
                )

                self.command_input.setText(
                    self.command_history[self.history_index]
                )
            
    def run_command(self):
        command = self.command_input.text().strip()

        if not command:
            return

        self.command_history.append(command)
        self.history_index = len(self.command_history)

        execute_command(command)

        self.command_input.clear()