# Ad Campaign Agent

[![CI](https://github.com/kogunlowo123/ad-campaign-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/ad-campaign-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Marketing | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Advertising campaign agent that creates ad copy, manages campaign budgets, optimizes targeting, analyzes campaign performance, and provides ROI reports across ad platforms.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `create_ad_copy` | Create ad copy optimized for a specific platform and objective |
| `manage_budget` | Allocate and optimize budget across campaigns and ad sets |
| `optimize_targeting` | Optimize audience targeting based on performance data |
| `analyze_performance` | Analyze campaign performance metrics (CTR, CPC, ROAS) |
| `generate_roi_report` | Generate ROI and attribution report for campaigns |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/ad-campaign/create` | Create or generate |
| `POST` | `/api/v1/ad-campaign/analyze` | Analyze performance |
| `POST` | `/api/v1/ad-campaign/optimize` | Optimize |
| `POST` | `/api/v1/ad-campaign/schedule` | Schedule |
| `POST` | `/api/v1/ad-campaign/report` | Generate report |

## Features

- Ad
- Campaign
- Analytics
- Optimization

## Integrations

- Hubspot Marketing
- Marketo
- Mailchimp
- Google Analytics
- Meta Ads

## Architecture

```
ad-campaign-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── ad_campaign_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Marketing Platform + LLM + Analytics**

---

Built as part of the Enterprise AI Agent Platform.
