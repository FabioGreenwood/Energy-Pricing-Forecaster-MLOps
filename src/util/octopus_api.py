import requests
from pprint import pprint

def octopus_api_get(date_start, date_end):
    # dates in format of '2020-03-29T00:00Z' '2020-03-29T02:29Z'
    # Z is zulu time
    # should return data every 30 mins
    # tarrif is currently hard coded to AGILE-24-10-01
    # region currently hard coded using tarrif_url
    
    base_url = f'https://api.octopus.energy/v1/products/'
    tarrif_url = f'AGILE-24-10-01'
    region_url = f'/electricity-tariffs/E-1R-{tarrif_url}-A/standard-unit-rates/'
    period_url = f'?period_from={date_start}&period_to={date_end}'
    full_url = base_url + tarrif_url + region_url + period_url
    
    # print(full_url)

    requested_data = requests.get(full_url)
    output_dict = requested_data.json()

    # pprint(output_dict)

    time_data_dict = {}

    for each_time in output_dict['results']:
        each_time.pop('payment_method', None)
        time_data_dict[each_time['valid_from']] = each_time

    # pprint(time_data_dict)
    return time_data_dict