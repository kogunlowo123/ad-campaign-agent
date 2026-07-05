"""Ad Campaign Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_create_ad_copy():
    """Test Create ad copy optimized for a specific platform and objective."""
    tools = AgentTools()
    result = await tools.create_ad_copy(platform="test", objective="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_manage_budget():
    """Test Allocate and optimize budget across campaigns and ad sets."""
    tools = AgentTools()
    result = await tools.manage_budget(total_budget="test", campaigns="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_optimize_targeting():
    """Test Optimize audience targeting based on performance data."""
    tools = AgentTools()
    result = await tools.optimize_targeting(campaign_id="test", performance_data="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_performance():
    """Test Analyze campaign performance metrics (CTR, CPC, ROAS)."""
    tools = AgentTools()
    result = await tools.analyze_performance(campaign_id="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.ad_campaign_agent_agent import AdCampaignAgentAgent
    agent = AdCampaignAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
