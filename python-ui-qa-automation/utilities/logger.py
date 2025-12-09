import logging
import os
from datetime import datetime

def get_logger():

    # Create logs folder if not exists
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Generate timestamp log file
    log_file = os.path.join(logs_dir, f"test_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

    # Create logger
    logger = logging.getLogger(log_file)
    logger.setLevel(logging.INFO)

    # File Handler
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    # Console Handler (optional)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Attach handlers if not already added
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
