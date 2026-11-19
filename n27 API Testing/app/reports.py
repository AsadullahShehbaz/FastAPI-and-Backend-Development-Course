# report.py
import json
from datetime import datetime, timezone
from pathlib import Path


def generate_report(output_path: Path) -> None:
    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": "complete",
    }

    output_path.write_text(
        json.dumps(report),
        encoding="utf-8",
    )
