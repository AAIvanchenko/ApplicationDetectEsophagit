import cv2
import numpy as np

from PySide6.QtGui import QImage
from PySide6.QtCore import QThread, Signal, Qt, Slot


class CaptureIpCameraFramesWorker(QThread):
    """
    Based on https://github.com/god233012yamil/Streaming-IP-Cameras-Using-PyQt-and-OpenCV/blob/main/Streaming_IP_Camera_Using_PyQt_OpenCV.py
    """
    # Signal emitted when a new image or a new frame is ready.
    imageUpdated = Signal(QImage)
    numpyImageReturned = Signal(np.ndarray)

    def __init__(self, url) -> None:
        super().__init__()
        # Declare and initialize instance variables.
        self.url = url
        self.fps = 0
        self.cap = None

        self.__thread_pause = False
        self.__thread_active = True
        self.__return_image = False

    def run(self) -> None:
        # Capture video from a network stream.
        self.cap = cv2.VideoCapture(self.url)
        # Get default video FPS.
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        # If video capturing has been initialized already.q
        if self.cap.isOpened():
            # print(f"Cam {self.url} open; fps: {self.fps}")
            # While the thread is active.
            while self.__thread_active:
                #
                if not self.__thread_pause:
                    # Grabs, decodes and returns the next video frame.
                    ret, frame = self.cap.read()
                    # If frame is read correctly.
                    if ret:
                        # Get the frame height, width and channels.
                        height, width, channels = frame.shape
                        # Calculate the number of bytes per line.
                        bytes_per_line = width * channels
                        # Convert image from BGR (cv2 default color format) to RGB (Qt default color format).
                        cv_rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        # Return image
                        if self.__return_image:
                            self.numpyImageReturned.emit(cv_rgb_image)
                            self.__return_image = False
                        # Convert the image to Qt format.
                        qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
                        # Scale the image.
                        # NOTE: consider removing the flag Qt.KeepAspectRatio as it will crash Python on older Windows machines
                        # If this is the case, call instead: qt_rgb_image.scaled(1280, 720)
                        qt_rgb_image_scaled = qt_rgb_image.scaled(1280, 720, Qt.KeepAspectRatio)  # 720p
                        # qt_rgb_image_scaled = qt_rgb_image.scaled(1920, 1080, Qt.KeepAspectRatio)
                        # Emit this signal to notify that a new image or frame is available.
                        self.imageUpdated.emit(qt_rgb_image_scaled)
                    else:
                        break
        # print(f"Cam {self.url} close; fps: {self.fps}")
        # When everything done, release the video capture object.
        if self.cap:
            self.cap.release()
        # Tells the thread's event loop to exit with return code 0 (success).
        self.quit()

    @Slot()
    def stop(self) -> None:
        self.__thread_active = False
        if self.cap:
            self.cap.release()
        self.terminate()

    @Slot()
    def pause(self) -> None:
        self.__thread_pause = True

    @Slot()
    def unpause(self) -> None:
        self.__thread_pause = False

    @Slot()
    def screenshot(self):
        self.__return_image = True