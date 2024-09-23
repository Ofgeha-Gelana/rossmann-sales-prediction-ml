import logging
import pandas as pd


def load_datasets(train_file: str, store_file: str, logger: logging.Logger):
    """
    Loads the train and store datasets and logs the process.

    Parameters:
    train_file (str): Path to the training dataset file.
    store_file (str): Path to the store dataset file.
    logger (logging.Logger): Logger instance for logging the process.

    Returns:
    tuple: Loaded train and store DataFrames.
    """
    logger.info("Loading datasets.")
    try:
        # Load datasets
        train_df = pd.read_csv(train_file)
        store_df = pd.read_csv(store_file)

        logger.info("Datasets loaded successfully.")
        return train_df, store_df
    except FileNotFoundError as e:
        logger.error(f"Files not found: {e}")
        raise
    except Exception as e:
        logger.error(f"An error occurred while loading datasets: {e}")
        raise

# Example usage:
# logger = setup_logger()


