import logging
import os
from datetime import datetime, timedelta
from logging.handlers import BaseRotatingHandler

class DailyRotatingFileHandler(BaseRotatingHandler):
    def __init__(self, directory, filename_prefix):
        self.directory = directory
        self.filename_prefix = filename_prefix
        self.baseFilename = self._get_new_filename()
        super().__init__(self.baseFilename, 'a', encoding='utf-8', delay=False)
        self.rollover_at = self._compute_next_rollover()

    def _get_new_filename(self):
        current_time = datetime.now().strftime("%Y-%m-%d")
        return os.path.join(self.directory, f"{self.filename_prefix}_{current_time}.log")

    def _compute_next_rollover(self):
        now = datetime.now()
        tomorrow = now + timedelta(days=1)
        midnight = datetime.combine(tomorrow, datetime.min.time())
        return midnight.timestamp()

    def shouldRollover(self, record):
        current_time = datetime.now().timestamp()
        if current_time >= self.rollover_at:
            return 1
        return 0

    def doRollover(self):
        self.stream.close()
        self.baseFilename = self._get_new_filename()
        self.stream = self._open()
        self.rollover_at = self._compute_next_rollover()

# 로그 디렉토리 설정
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# 핸들러 설정
log_handler = DailyRotatingFileHandler(
    directory=log_directory,
    filename_prefix="app"
)

# 로그 포맷 설정
log_format = logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
)
log_handler.setFormatter(log_format)

# 루트 로거 설정
logging.basicConfig(
    level=logging.INFO,
    handlers=[log_handler]
)
