import logging

import pytest

from flask import Flask

from mock_server.mock_model_response import create_mock_server


@pytest.fixture
def core_server():
    return create_mock_server()