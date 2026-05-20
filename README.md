# depositback-agent-youtube-publisher

Schedules YouTube Shorts and long-form educational videos

## DepositBack Agent Network — Distribution

Part of the DepositBack autonomous marketing system.

## Quick Start

```bash
git clone https://github.com/kolegadev/depositback-agent-youtube-publisher.git
cd depositback-agent-youtube-publisher
pip install -r requirements.txt
python runtime/main.py
```

## Structure

```
.
├── SKILL.md, manifest.json, README.md
├── runtime/main.py
├── skills/skill_resolver.py, noop.py
├── data/inbox/, data/outbox/
└── .github/workflows/heartbeat.yml, scan.yml
```

## License

MIT — DepositBack Agent Network
