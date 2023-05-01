from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, QPropertyAnimation, QEasingCurve

class CustomSlideMenu(QWidget):
    def __init__(self, parent=True) -> None:
        QWidget.__init__(self, parent)
        self._width_size = self.width()
        self.setMaximumWidth(0)

    @Slot()
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = self._width_size 
            # self.show()
        # If maximized
        else:
            # Restore menu
            newWidth = 0


        # Animate the transition
        self.animation = QPropertyAnimation(self, b"maximumWidth")#Animate minimumWidht
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()