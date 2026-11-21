import pytest

@pytest.fixture(scope="session")
def trace_paths():
    return {
        "nominal": "sample_data/nominal_aeb.csv",
        "faulty": "sample_data/vehicle_trace.csv",
    }
