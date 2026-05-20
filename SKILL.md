# YouTube Publisher

> **Agent**: `depositback-agent-youtube-publisher`  
> **Group**: Distribution  
> **Product**: DepositBack — Security Deposit Demand Letter Service

## Purpose

Cross-posts TikToks as Shorts (5%+ engagement target) and publishes 2-3 long-form videos/month: state law deep-dives, walkthroughs, and comparison content.

## DepositBack Context

DepositBack is a single-page, no-signup transactional product for US renters seeking to recover security deposits. The entire customer journey fits on one URL: landing page → 6-question form → Revolut payment → PDF emailed. Conversion rate target: **4% visitor-to-purchase minimum**.

## Inputs

- Short scripts from social-content-creator
- State blog posts from geo-content-generator

## Outputs

- Published video URLs → analytics/funnel-analyst inbox

## Human Escalation Points 🛑

- DMCA claims
- Comment moderation for legal advice
- Monetization policy issues

## Skills

| Skill | Description | Status |
|-------|-------------|--------|
| `noop` | Health check / pipeline verification | ✅ Active |
| `execute` | Primary function for this agent | 🔧 Planned |

## Workflow

1. Poll `data/inbox/` for task manifests from upstream agents.
2. Resolve required skills (local `skills/` or ClawHub fallback).
3. Execute workflow.
4. Write artifacts to `data/outbox/`.
5. Update `data/state.json`.

## Runtime

```bash
pip install -r requirements.txt
python runtime/main.py
```
