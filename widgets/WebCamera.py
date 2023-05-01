from PySide6.QtMultimedia import (QCamera, QCameraDevice,
                                  QImageCapture, QMediaCaptureSession,
                                  QMediaDevices,
                                  QMediaRecorder)
from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtGui import QActionGroup
from PySide6.QtCore import Slot


class CamWidget(QWidget):
    def __init__(self):
        super().__init__()

        self._video_devices_group = None

        self.m_devices = QMediaDevices()
        self.m_imageCapture = None
        self.m_captureSession = QMediaCaptureSession()
        self.m_camera = None

        # try to actually initialize camera & mic

        self._video_devices_group = QActionGroup(self)
        self._video_devices_group.setExclusive(True)

        self.setCamera(QMediaDevices.defaultVideoInput())

    @Slot(QCameraDevice)
    def setCamera(self, cameraDevice):
        self.m_camera = QCamera(cameraDevice)
        self.m_captureSession.setCamera(self.m_camera)

        self.m_camera.start()

    @Slot()
    def record(self):
        self.m_mediaRecorder.record()
        self.updateRecordTime()

    @Slot()
    def pause(self):
        self.m_mediaRecorder.pause()

    @Slot()
    def stop(self):
        self.m_mediaRecorder.stop()