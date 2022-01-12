import json

_accConstList = ['unit', 'iid', 'cid', 'vehicle_no', 'total_price', 'total_extra_kms','total_base_price','total_misc_price'
    ,'total_extra_hours','total_loader_price','total_extra_packets','total_extra_weights','total_extra_day_price'
    ,'total_extra_kms_price','total_extra_droppoints','total_extra_fuel_price', 'total_extra_hours_price','total_taxable_misc_price'
    ,'total_extra_packets_price','total_extra_weights_price','total_extra_droppoints_price','total_minimum_guarantee_price']


async def accounting_invoice(_data: json) -> list:
    _array = []
    for accounting in _data['accounting_invoice']:
        for invoice in accounting['invoice_details']:
            _object = get_key_value(invoice, {})
            _array.append(_object)
    return _array


_driverPaymentList = ['cid']


async def accounting_driver_payment(_data: json) -> list:
    _array = []
    for accounting in _data['accounting_driver_payment']:
        _object = get_key_value(accounting, {})
        _array.append(_object)
    return _array


def get_key_value(_data: json, _object: dict) -> dict:
    for key, value in _data.items():
        try:
            if key in _accConstList:
                _object[key] = value
            else:
                if isinstance(value, dict):
                    print("isinstance : dict")
                    get_key_value(value, _object)
                elif isinstance(value, list):
                    print("isinstance : list")
                    if all(not isinstance(x, int) for x in value) and not not value:
                        get_key_value(value[0], _object)
        except Exception as e:
            print(e)

    return _object
