from validators.kpi_calc import min_ttc_seconds

def test_nominal_aeb_has_valid_ttc():
    ttc = min_ttc_seconds("sample_data/nominal_aeb.csv")
    assert ttc is not None and ttc > 1.0
