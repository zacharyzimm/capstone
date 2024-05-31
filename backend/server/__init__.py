import logging
import os

from dotenv import load_dotenv

logging.info("Loading env...")
load_dotenv()

if os.environ.get("env") == "prod":
    if not os.environ.get("SUCCESSFUL_DOTENV_LOAD") == "prod_env":
        raise Exception("CRITICAL ERROR: environment variables not successfully loaded")