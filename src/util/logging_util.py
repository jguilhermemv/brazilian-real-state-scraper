import logging
from datetime import datetime

def get_logger():
    timestamp = datetime.now().strftime("%Y%m%d")
    
    # Create a logger instance
    logger = logging.getLogger(__name__)

    # Create a file handler
    handler = logging.FileHandler(f'{timestamp}-error.log')

    # Configure the handler to only log messages with severity of ERROR or higher
    handler.setLevel(logging.ERROR)

    # Create a formatter to format the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Attach the formatter to the handler
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    
    return logger

