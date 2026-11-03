#!/usr/bin/env python3
"""Validate a .excalidraw file: structure, unique ids, and two-sided bindings."""
import json
import sys


def check(path):
    with open(path) as f:
        doc = json.load(f)
    errors = []
    if doc.get("type") != "excalidraw" or not isinstance(doc.get("elements"), list):
        return ["top level must have type 'excalidraw' and an 'elements' list"]

    els = [e for e in doc["elements"] if not e.get("isDeleted")]
    by_id = {}
    for e in doc["elements"]:
        if e.get("id") in by_id:
            errors.append(f"duplicate id {e.get('id')}")
        by_id[e.get("id")] = e

    def bound(owner_id, child_id):
        owner = by_id.get(owner_id) or {}
        return any(b.get("id") == child_id for b in owner.get("boundElements") or [])

    for e in els:
        eid = e.get("id")
        for field in ("type", "x", "y"):
            if field not in e:
                errors.append(f"{eid}: missing {field}")
        if e.get("type") == "text":
            if "text" not in e:
                errors.append(f"{eid}: text element without text")
            cid = e.get("containerId")
            if cid and cid not in by_id:
                errors.append(f"{eid}: containerId {cid} does not exist")
            elif cid and not bound(cid, eid):
                errors.append(f"{eid}: container {cid} does not list it in boundElements")
        if e.get("type") in ("arrow", "line"):
            if len(e.get("points") or []) < 2:
                errors.append(f"{eid}: needs at least 2 points")
            for side in ("startBinding", "endBinding"):
                b = e.get(side)
                if b:
                    tid = b.get("elementId")
                    if tid not in by_id:
                        errors.append(f"{eid}: {side} target {tid} does not exist")
                    elif not bound(tid, eid):
                        errors.append(f"{eid}: {side} target {tid} does not list it in boundElements")
        for b in e.get("boundElements") or []:
            if b.get("id") not in by_id:
                errors.append(f"{eid}: boundElements references missing {b.get('id')}")
    return errors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: check.py <file.excalidraw>")
    try:
        errs = check(sys.argv[1])
    except (OSError, json.JSONDecodeError) as exc:
        sys.exit(f"ERROR: {exc}")
    if errs:
        print("\n".join(f"ERROR: {e}" for e in errs))
        sys.exit(1)
    print("OK")
