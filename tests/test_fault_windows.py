from validators.fault_windows import merge_fault_windows

def test_merges_overlapping_ecu_faults():
    raw = [(140, 200), (100, 150), (300, 320)]
    assert merge_fault_windows(raw) == [(100, 200), (300, 320)]

def test_handles_empty_and_touching_windows():
    assert merge_fault_windows([]) == []
    assert merge_fault_windows([(10, 20), (20, 30)]) == [(10, 30)]