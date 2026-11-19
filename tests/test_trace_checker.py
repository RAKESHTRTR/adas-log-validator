from validators.trace_checker import check_trace

def test_detects_timing_and_speed_faults():
    errors = check_trace("sample_data/vehicle_trace.csv")
    assert len(errors) == 2
    assert any("timestamp gap" in e for e in errors)
    assert any("invalid ego_speed_mps" in e for e in errors)
