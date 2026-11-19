# test_report.py
import json
import pytest
from app.reports import generate_report

@pytest.fixture(scope="session")
def report_data(tmp_path_factory):
    print("Running Fixture...")
    report_path = tmp_path_factory.mktemp("reports") / "report.json"

    generate_report(report_path)
    return json.loads(report_path.read_text(encoding="utf-8"))


def test_generate_report(report_data) -> None:
    print("Running generate_report test...")
    assert isinstance(report_data, dict)

def test_generate_report_keys(report_data)-> None:
    print("Running generate_report keys test...")
    assert "timestamp" in report_data 
    assert "status" in report_data 
