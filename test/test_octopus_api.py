from src.util.octopus_api import octopus_api_get

def test_returns_dict_with_day_data():
    data = octopus_api_get("2025-03-29T00:00Z","2025-03-29T23:59Z")
    assert isinstance(data, dict)

def test_returns_dict_with_day_data_each_30_mins_so_48_results():
    data = octopus_api_get("2025-03-29T00:00Z","2025-03-29T23:59Z")
    assert len(data) == 48

def test_returns_vaild_data():
    data = octopus_api_get("2025-03-29T00:00Z","2025-03-29T00:59Z")
    first_dict = data['2025-03-29T00:00:00Z']
    assert first_dict['valid_to'] == '2025-03-29T00:30:00Z'
    assert isinstance(first_dict['value_exc_vat'], float)
    assert isinstance(first_dict['value_inc_vat'], float)