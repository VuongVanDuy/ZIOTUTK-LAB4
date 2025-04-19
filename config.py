import sys
import os

def resource_path() -> str:
    """
    Trả về đường dẫn tuyệt đối đến một file tài nguyên,
    hoạt động bình thường cả khi chạy script và khi đóng gói PyInstaller.
    """
    if getattr(sys, "_MEIPASS", False):
        # Khi chạy từ PyInstaller --onefile, _MEIPASS trỏ đến thư mục tạm
        base = sys._MEIPASS
    else:
        # Khi chạy từ script gốc, __file__ trỏ đến module hiện tại
        base = os.path.dirname(os.path.abspath(__file__))
    return base

DIR = resource_path()
DATA_SAMPLE_DIR = DIR + '\\' + "data_samples"
GENDER = ["man_voice", "woman_voice"]
LANGUAGES = ["en", "fr", "ja", "ru"]
FREQ = 44100
DURATION = 5