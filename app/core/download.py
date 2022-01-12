import asyncio

from app.core.filter import accounting_invoice, accounting_driver_payment, _driverPaymentList, _accConstList
from app.querys.query_list import build_query_list
from app.service.graph_ql import gql_query
from app.service.writeExcel import export_in_excel

async def download_all_file():
    for e in build_query_list():
        result = await gql_query(e)
        if "accounting_invoice" in e.name:
            _data_list = await accounting_invoice(result)
            await export_in_excel(e.name, _data_list, _accConstList)
        elif "accounting_driver_payment" in e.name:
            _data_list = await accounting_driver_payment(result)
            await export_in_excel(e.name, _data_list, _driverPaymentList)


#asyncio.run(download_all_file())