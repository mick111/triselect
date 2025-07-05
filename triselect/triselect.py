from PyQt6.QtWidgets import QMainWindow


class TriSelect(QMainWindow):
    """
    Main window for the TriSelect application.
    This class inherits from QMainWindow and serves as the main interface.
    """

    def __init__(self, parent=None):
        """
        Initialize the TriSelect main window.

        :param parent: Parent widget, defaults to None
        """
        super().__init__(parent)
        self.setWindowTitle("TriSelect Application")
        self.resize(800, 600)
        # Additional initialization code can be added here
