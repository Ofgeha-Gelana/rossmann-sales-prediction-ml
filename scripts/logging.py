import logging

def setup_logger(log_file: str = "exploration.log"):
    """
    Sets up a logger that logs to both a file and the console.
    
    Parameters:
    log_file (str): Name of the log file where messages will be stored.
    """
    # Set up basic configuration for logging
    logging.basicConfig(
        level=logging.DEBUG,  # Set the lowest-severity log message to capture
        format="%(asctime)s - %(levelname)s - %(message)s",  # Define the format of the logs
        handlers=[
            logging.FileHandler(log_file),  # Log messages to a file
            logging.StreamHandler()  # Also log to console
        ]
    )
    
    # Create and return a logger instance
    logger = logging.getLogger(__name__)
    return logger