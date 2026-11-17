"""Run the data-quality monitoring demo from the repository root."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent / "src"))

from quality_monitor import assess_records


def main() -> None:
    records = json.loads((Path(__file__).parent / "data" / "sample_orders.json").read_text())
    print(json.dumps(assess_records(records), indent=2))


if __name__ == "__main__":
    main()
