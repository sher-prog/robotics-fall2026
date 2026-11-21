"""Complete decide() using the transition requirements in the Lab 10 guide."""


def decide(state, event):
    phase = state["phase"]
    kind = event["kind"]
    target = event["target"]
    active = ("CLARIFY", "CONFIRM", "EXECUTING", "WAIT_READY")

    if kind == "CANCEL":
        if phase in active:
            return "cancel"
        return "hold"

    if kind == "REQUEST" and phase in ("IDLE", "CLARIFY", "CONFIRM", "RECOVERY", "CANCELLED"):
        if target in ("red", "blue"):
            return "select"
        return "clarify"

    if kind == "CORRECT" and phase in active and target in ("red", "blue"):
        return "select"

    if kind == "CONFIRM" and phase == "CONFIRM":
        return "begin"

    if phase == "WAIT_READY" and kind == "READY":
        return "release"

    if kind == "TIMEOUT" and phase == "WAIT_READY":
        return "timeout"

    if kind == "TICK" and phase == "EXECUTING":
        return "advance"

    return "hold"
