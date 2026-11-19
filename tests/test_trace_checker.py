import pytest
from validators.trace_checker import check_trace

@pytest.mark.parametrize("csv_path, expected_errors", [
    ("sample_data/nominal_aeb.csv", 0),
    ("sample_data/vehicle_trace.csv", 2),
])
def test_trace_suite(csv_path, expected_errors):
    errors = check_trace(csv_path)
    assert len(errors) == expected_errors, f"Unexpected errors: {errors}"
