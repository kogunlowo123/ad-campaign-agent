"""Test configuration for Ad Campaign Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "ad-campaign-agent", "category": "Marketing"}
