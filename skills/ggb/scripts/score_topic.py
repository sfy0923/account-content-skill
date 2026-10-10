#!/usr/bin/env python3
"""Calculate editorial topic scores; evidence and semantic review remain human/agent judgments."""

import argparse
import json
import math
import sys

DIMENSIONS = (
    ("pain_and_consequence", 5),
    ("concrete_scene", 4),
    ("viewing_reason", 2),
    ("evidence_and_simulation", 3),
    ("account_fit_and_business", 3),
    ("shootability_and_continuity", 2),
    ("clarity_and_plain_language", 1),
)


def score_topic(scores, dedup="unknown", other_gates="pending"):
    if len(scores) != len(DIMENSIONS):
        raise ValueError("exactly seven scores are required")
    if any(isinstance(value, bool) or not isinstance(value, (int, float))
           or not math.isfinite(value) or not 0 <= value <= 5 for value in scores):
        raise ValueError("each score must be a finite number between 0 and 5")
    if dedup not in ("independent", "adjacent", "duplicate", "unknown"):
        raise ValueError("invalid dedup status")
    if other_gates not in ("passed", "pending", "failed"):
        raise ValueError("invalid other-gates status")
    items = [{"dimension": name, "raw": raw, "weight": weight,
              "weighted": round(raw * weight, 4)}
             for (name, weight), raw in zip(DIMENSIONS, scores)]
    base = round(sum(item["weighted"] for item in items), 4)
    deduction = {"independent": 0, "adjacent": 5, "duplicate": 10, "unknown": 0}[dedup]
    final = round(base - deduction, 4)
    numeric_gates = {
        "pain_at_least_4": scores[0] >= 4,
        "viewing_reason_at_least_3": scores[2] >= 3,
        "clarity_at_least_4": scores[6] >= 4,
    }
    band = "candidate" if final >= 90 else "revise" if final >= 80 else "keep_direction" if final >= 70 else "pass"
    if dedup == "duplicate":
        decision = "pass_duplicate"
    elif dedup == "adjacent":
        decision = "revise_adjacent_not_selected"
    elif other_gates == "failed" or not all(numeric_gates.values()):
        decision = "hard_gate_failed_not_selected"
    elif dedup == "unknown" or other_gates == "pending":
        decision = "pending_review_not_selected"
    else:
        decision = band
    return {
        "items": items, "base_score": base, "dedup_status": dedup,
        "deduction": deduction, "final_score": final,
        "provisional_score": dedup == "unknown", "numeric_gates": numeric_gates,
        "other_gates": other_gates, "score_band": band, "decision": decision,
        "scope": "Editorial calculation only; no evidence, history, authorization, filming or performance verification.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scores", nargs=7, type=float,
                        help="pain, scene, viewing reason, evidence, account fit, shootability, clarity")
    parser.add_argument("--dedup", choices=("independent", "adjacent", "duplicate", "unknown"), default="unknown")
    parser.add_argument("--other-gates", choices=("passed", "pending", "failed"), default="pending",
                        help="use passed only after independently checking the remaining hard gates")
    args = parser.parse_args()
    try:
        result = score_topic(args.scores, args.dedup, args.other_gates)
    except ValueError as exc:
        parser.error(str(exc))
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
