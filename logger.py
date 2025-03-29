import logging

logging.basicConfig(
    filename='app.log',  # Log filename
    level=logging.INFO,  # Logging level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)

if __name__ == "__main__":
    log_info("Hello! I am an info message.")
    log_warning("Boo! This is a warning message.")
    log_error("Sadly, I am an error message.")