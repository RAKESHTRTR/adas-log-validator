from validators.kpi_calc import min_ttc_seconds

def test_ttc_positive_on_closing_target():
    ttc = min_ttc_seconds("sample_data/nominal_aeb.csv")
    assert ttc is not None and ttc > 0.5
    
def test_ttc_none_when_lead_pulling_away(tmp_path):
    p = tmp_path / "pulling_away.csv"
    p.write_text(
        "timestamp_ms,ego_speed_mps,lead_dist_m,aeb_active\n"
        "100,15.0,20.0,0\n"
        "120,15.0,25.0,0\n"
    )
    assert min_ttc_seconds(str(p)) is None

def test_ttc_guards_duplicate_timestamp_zero_dt(tmp_path):
    p = tmp_path / "dup_ts.csv"
    p.write_text(
        "timestamp_ms,ego_speed_mps,lead_dist_m,aeb_active\n"
        "100,20.0,30.0,0\n"
        "100,20.0,29.5,0\n"
        "120,20.0,29.0,0\n"
    )
    ttc = min_ttc_seconds(str(p))
    assert ttc is not None and ttc > 0.0