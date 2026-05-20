#!/usr/bin/env python3
import json, os, sys, shutil
from datetime import datetime, timezone
from pathlib import Path

AGENT_NAME = os.getenv("AGENT_NAME", "unknown")
AGENT_ID = os.getenv("AGENT_ID", "0")
INBOX = Path("data/inbox")
OUTBOX = Path("data/outbox")
ARCHIVE = Path("data/archive")
STATE_FILE = Path("data/state.json")

sys.path.insert(0, str(Path(__file__).parent.parent / "skills"))
from skill_resolver import resolve_skill, execute_skill

def write_artifact(name, payload):
    OUTBOX.mkdir(parents=True, exist_ok=True)
    path = OUTBOX / f"{int(datetime.now(timezone.utc).timestamp())}_{name}.json"
    path.write_text(json.dumps(payload, indent=2))
    print(f"  📤 Artifact: {path}")
    return str(path)

def save_state(status="idle", extra=None):
    state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}
    state["status"] = status
    state["last_run"] = datetime.now(timezone.utc).isoformat()
    state["runs"] = state.get("runs", 0) + 1
    if extra: state.update(extra)
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))

def run():
    print(f"🚀 {AGENT_NAME} ({AGENT_ID}) — {datetime.now(timezone.utc).isoformat()}")
    for d in [INBOX, OUTBOX, ARCHIVE]: d.mkdir(parents=True, exist_ok=True)
    manifests = sorted(INBOX.glob("*.json"))
    if not manifests:
        print("  ℹ️  No manifests in inbox")
        save_state("idle")
        return
    manifest = manifests[-1]
    print(f"  Processing latest: {manifest.name}")
    save_state("running")
    data = json.loads(manifest.read_text())
    results = []
    for idx, step in enumerate(data.get("steps", [])):
        fn = resolve_skill(step.get("skill"))
        if fn is None:
            results.append({"step": step.get("id", idx), "status": "skipped"})
            continue
        try:
            out = execute_skill(fn, step.get("params", {}))
            results.append({"step": step.get("id", idx), "status": "success", "output": out})
        except Exception as e:
            results.append({"step": step.get("id", idx), "status": "error", "error": str(e)})
    artifact = {"agent": AGENT_NAME, "agent_id": AGENT_ID, "manifest_id": data.get("workflow_id", "unknown"), "timestamp": datetime.now(timezone.utc).isoformat(), "results": results}
    write_artifact("output", artifact)
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    shutil.move(str(manifest), str(ARCHIVE / manifest.name))
    save_state("idle")
    print("  ✅ Complete")

if __name__ == "__main__": run()
