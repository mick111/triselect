from PyQt6.QtWidgets import QApplication
from . import TriSelect
import sys


def main():
    """
    Main function to run the TriSelect application.
    """

    app = QApplication(sys.argv)
    window = TriSelect()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
