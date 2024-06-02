import logging
import os

from api.core_server import create_core_server

from dotenv import load_dotenv

logging.info("Loading env...")
load_dotenv()

if os.environ.get("env") == "prod":
    if not os.environ.get("SUCCESSFUL_DOTENV_LOAD") == "prod_env":
        raise Exception("CRITICAL ERROR: environment variables not successfully loaded")