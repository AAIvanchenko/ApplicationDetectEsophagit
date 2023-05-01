import numpy as np
from PySide6.QtCore import Slot, QSize, Qt, Signal
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QLabel, QSizePolicy, QVBoxLayout

from ui.ip_cam_worker import CaptureIpCameraFramesWorker
import data.resourse_rc

class CamWidget(QLabel):
    imageReturned = Signal(np.ndarray)
    _returnImageFromCam = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()
        self.ipCamFramesWorker = None
        self.cam_url = None

        # Create an instance of CaptureIpCameraFramesWorker
        self._pixmap = QPixmap(u":image/image/novideo.png")
        self.setPixmap(self._pixmap.scaled(
            self.width(), self.height(),
            Qt.KeepAspectRatio)
        )

    def connect_camera(self, cam_url):
        self.cam_url = cam_url
        if cam_url is not None:
            if self.ipCamFramesWorker:
                self.close()
                self.wait()
            self.ipCamFramesWorker = CaptureIpCameraFramesWorker(self.cam_url)
            self.ipCamFramesWorker.imageUpdated.connect(self.showCamFrame)
            self.ipCamFramesWorker.numpyImageReturned.connect(self._redirectImageReturnedFromCam)
            self.ipCamFramesWorker.start()
            self._returnImageFromCam.connect(self.ipCamFramesWorker.screenshot)


    def setupUI(self):
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(QSize(320, 180))
        self.setAlignment(Qt.AlignCenter)
        # self.setScaledContents(True)
        # self.installEventFilter(self)
        self.setObjectName("camLabel")
        # self.camLabel.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed))
        self.cam_state = "Normal"

    def resizeEvent(self, event):
        self.setPixmap(self._pixmap.scaled(
            self.width(), self.height(),
            Qt.KeepAspectRatio))

    @Slot()
    def returnImage(self):
        if self.ipCamFramesWorker is not None:
            self._returnImageFromCam.emit()

    @Slot()
    def _redirectImageReturnedFromCam(self, image):
        self.imageReturned.emit(image)

    def isRunning(self):
        return self.ipCamFramesWorker.isRunning()

    def wait(self):
        if self.ipCamFramesWorker is not None:
            self.ipCamFramesWorker.wait()

    @Slot(QImage)
    def showCamFrame(self, frame: QImage) -> None:
        self._pixmap = QPixmap.fromImage(frame)
        self.setPixmap(self._pixmap.scaled(
            self.width(), self.height(),
            Qt.KeepAspectRatio))

    @Slot()
    def close(self):
        if self.ipCamFramesWorker is not None and self.ipCamFramesWorker.isRunning():
            self.ipCamFramesWorker.stop()


