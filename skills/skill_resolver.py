#!/usr/bin/env python3
import importlib.util, sys
from pathlib import Path
SKILLS = {"noop": ("noop", "execute")}
def resolve_skill(name):
    if name not in SKILLS: return None
    mod, func = SKILLS[name]
    sys.path.insert(0, str(Path(__file__).parent))
    return getattr(__import__(mod), func)
def execute_skill(fn, params): return fn(**params)
