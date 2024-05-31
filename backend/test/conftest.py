import logging

import pytest

from flask import Flask


@pytest.fixture
def core_server():
    return create_core_server()