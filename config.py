import os
import logging

# Setup basic configuration for logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config:
    """Base configuration class."""
    PORT = int(os.getenv('PORT', 5000))
    HOST = os.getenv('HOST', "0.0.0.0")
    MODEL_NAME = os.getenv('MODEL_NAME', "models/all-MiniLM-L6-v2")
    DATA_FILE = os.getenv('DATA_FILE', "data/dialogs.txt")
    EMBEDDINGS_FILE = os.getenv('EMBEDDINGS_FILE', "pickle/embeddings.pkl")
    FAQ_DATA_FILE = os.getenv('FAQ_DATA_FILE', "pickle/faq_data.pkl")

    def log_config(self):
        logger.info("Configuration Loaded: ")
        logger.info(f"PORT: {self.PORT}")
        logger.info(f"HOST: {self.HOST}")
        logger.info(f"MODEL_NAME: {self.MODEL_NAME}")
        logger.info(f"DATA_FILE: {self.DATA_FILE}")
        logger.info(f"EMBEDDINGS_FILE: {self.EMBEDDINGS_FILE}")
        logger.info(f"FAQ_DATA_FILE: {self.FAQ_DATA_FILE}")

# Example usage:
config = Config()
config.log_config()
