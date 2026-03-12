import json
from datetime import datetime

def log_route(user_input, intent, confidence):

    log = {
        "timestamp": str(datetime.now()),
        "input": user_input,
        "intent": intent,
        "confidence": confidence
    }

    with open("route_log.jsonl", "a") as f:
        f.write(json.dumps(log) + "\n")

