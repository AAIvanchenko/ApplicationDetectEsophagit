from pathlib import Path
import cv2

from preprocessing_img import letterbox

# нужно будет при вызове данного класса написать трансформ с данной функцией: del_area_behind_countour

VID_FORMATS = ['mp4', 'mkv']

class VideoToBatchImage:
    def __init__(self, path, img_size=640, scaleFill=False, padding=None, stride=None, transforms = None):
        p = Path(path).resolve()

        if p.is_file():
            if p.suffix[1:].lower() in VID_FORMATS:
                path_video = str(p)  # files
        else:
            raise FileNotFoundError(f'{p} does not exist')
  
        img_info = self.get_video_info(path_video)
        # Расчёт stride для каждого видео
        vid_stride = int(img_info["fps"]*stride) if stride else 1
        vid_stride_frames = vid_stride
        
        self.num_frames = img_info["frames"]
    
        if isinstance(img_size, int):
            img_size = (img_size, img_size)
        
        self.transforms = transforms
        self.path = path_video
        self.img_size = img_size
        self.vid_stride_frames = vid_stride_frames
        self.padding = padding
        self.scaleFill = scaleFill
        
    def __iter__(self):
        self.new_video(self.path)
        return self
    
    def __next__(self):
        if self.cap == None:
            raise StopIteration
        path = self.path

        # Read video
        ret_val, img0 = self.cap.read()
        assert ret_val is True, f'Error to read from file on {round(int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))/self.cap.get(cv2.CAP_PROP_FPS), 2)} sec by path:{path}'
        self.frame += 1

        # Skip Frames
        self.frame += self.vid_stride_frames - 1

        if self.frame >= self.num_frames:
            self.cap.release()
            self.cap = None
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.frame)
        
        # Convert
        img = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB) # BGR to RGB
        img = letterbox(img, self.img_size, scaleFill=self.scaleFill)
        
        if self.transforms:
            img = self.transforms(img)

        return img
    
    def get_video_info(self, path):
        cap = cv2.VideoCapture(path)
        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        # width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        res_info = {}
        res_info["frames"] = length
        res_info["fps"] = fps
        cap.release()
        return res_info
    
    def new_video(self, path):
        self.frame = 0
        self.cap = cv2.VideoCapture(path)
        self.frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        if self.padding:
            self.frame += self.padding
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.padding)
