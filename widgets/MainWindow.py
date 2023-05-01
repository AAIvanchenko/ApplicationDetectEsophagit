import os
from platform import system


from PySide6.QtWidgets import QFileDialog, QMenu
from PySide6.QtCore import Slot
from ui.ui_MainWindow import QMainWindow, Ui_MainWindow
from PySide6.QtMultimedia import QMediaDevices



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.path_video = None
        self.image_directory = self.take_home_path()
        # self.index_camera = 0
        #отображение меню
        self._menu_is_collapsed = False
        self.menuButton.clicked.connect(self.menu.slideLeftMenu)

        self.video.clicked.connect(self._load_image_by_dialog)
        #нажатие на кнопки
        self.camera.clicked.connect(lambda: self.change_page(1))
        self.predict.clicked.connect(lambda: self.change_page(2))
 
        self.settings.setMenu(self.create_menu())
        
        #show window
        self.show()

        # print(cv2.CAP_DSHOW)
        # print([cam.description() for cam in QMediaDevices.videoInputs()])
   
    # настройки
    def create_menu(self):
        impMenu = QMenu(self)
        impMenu.addAction('Выбор камеры').setMenu(self.create_menu_camera())
        impMenu.addAction('Выход', self.close)
        # impMenu.triggered.connect(self.connect_camera(1))
        # print(impMenu)
        return impMenu
    
    def create_menu_camera(self):
        name_camers = [cam.description() for cam in QMediaDevices.videoInputs()]
        camera_menu = QMenu(self)

        def connect_camera_action(idx):
            return lambda: self.connect_camera(idx)
        
        for i, name in enumerate(name_camers):
            camera_menu.addAction(name, connect_camera_action(i))
        
        return camera_menu
    
    @Slot(int)
    def connect_camera(self, index_camera):
        # print(index_camera)
        self.webcamera.close()
        self.webcamera.wait()
        self.webcamera.connect_camera(index_camera)
        # print(index_camera)
      
    # будет это Slot
    def change_page(self, index_page):
        if index_page == 1:
            self.connect_camera(0)
        if index_page != 1:
            self.webcamera.close()
            self.webcamera.wait()
        self.stackedWidget.setCurrentIndex(index_page)

    
    # будет это Slot
    def menuCollapsed(self):
        self.menu.setVisible(self._menu_is_collapsed)
        self._menu_is_collapsed = not self._menu_is_collapsed

    def _load_image_by_dialog(self):
        """
        Метод, вызывающий диалоговое окно для загрузки изображения.

        Вызвает стандартное диалоговое окно каталога.
        Старотовый каталог берётся из переменной 'self.image_directory'.
        Выбранное изображение сохраняется в 'self.row_image'.
        Изменяет 'self.image_directory' на директорию, в котором было
        изображение.
        """
        file_path = QFileDialog.getOpenFileName(self,
                                                "Выбрать деталь",
                                                self.image_directory,
                                                "Video Files (*.mp4 *.mkv)"
                                                )[0]
        # Если пользователь не выбрал файл
        if not file_path:
            return
        # Запоминание выбранной директории
        self.image_directory = os.path.dirname(file_path)
        self.path_video = file_path
        # print(self.image_directory)
        # print(file_path)

    
    def take_home_path(self) -> str:
        """
        Метод, возвращающий домашнюю директорию пользователя.
        Для Windows директория берётся из переменной окружения HOMEPATH
        (в виде C:/User/<username>).
        """
        home_path = ""
        system_name = system()
        if system_name == "Windows":
            home_path = os.environ['HOMEPATH']

        return home_path


    def closeEvent(self, event) -> None:
            self.webcamera.close()
            self.webcamera.wait()
            # Accept the event
            event.accept()

