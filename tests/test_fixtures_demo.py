from validators.trace_checker import check_trace

def test_nominal_clean(trace_paths):
    assert check_trace(trace_paths["nominal"]) == []
