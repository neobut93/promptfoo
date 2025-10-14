from typing import Any, Dict, Optional, Union

def calculate_score(named_scores: Dict[str, float],
                    context: Optional[Dict[str, Any]] = None
) -> Dict[str, Union[bool, float, str]]:
    """
    Zero-on-fail scoring:
    - If a metric has its own threshold, and score < that threshold, we use 0 for that metric.
    - We keep the original weights (denominator unchanged).
    - Falls back to 0.6 as the test-level threshold unless provided in context.
    """

    context = context or {}

    # 1) Expected inputs (provide these via your config or bake them here)
    #    Per-metric weights must match your YAML:
    weights = context.get("weights", {
        "Correctness": 2,
        "Tone": 1,
        "Topicality": 1,
        "Greeting": 1,
        "Performance": 2,
    })

    #    Per-metric thresholds from your YAML (only where specified):
    metric_thresholds = context.get("metric_thresholds", {
        # contains: no per-assert threshold in your snippet -> treat as 0.0
        "Correctness": 0.0,
        # llm-rubric (Tone): no per-assert threshold in your snippet -> 0.0
        "Tone": 0.0,
        # answer-relevance with threshold: 0.8
        "Topicality": 0.8,
        # llm-rubric (Greeting) with threshold: 0.8
        "Greeting": 0.8,
        # assert-set with threshold: 0.6
        "Performance": 0.6,
    })

    test_threshold = context.get("threshold", 0.6)

    # 2) Zero-on-fail transform
    effective_scores: Dict[str, float] = {}
    details = []
    for metric, w in weights.items():
        raw = float(named_scores.get(metric, 0.0))
        mth = float(metric_thresholds.get(metric, 0.0))
        eff = raw if raw >= mth else 0.0
        effective_scores[metric] = eff
        details.append(f"{metric}: raw={raw:.2f}, thr={mth:.2f}, used={eff:.2f}, w={w}")

    # 3) Weighted average with original weights
    numerator = sum(effective_scores[m] * weights[m] for m in weights)
    denom = float(sum(weights.values())) or 1.0
    aggregate = numerator / denom

    return {
        "pass": aggregate >= test_threshold,
        "score": aggregate,
        "reason": "Zero-on-fail; " + " | ".join(details),
    }