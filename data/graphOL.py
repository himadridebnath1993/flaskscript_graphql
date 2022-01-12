import asyncio
import json

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

from data.filter import accounting_invoice, _accConstList, accounting_driver_payment, _driverPaymentList
from data.gqlQuery import GqlQuery
from data.writeExcel import export_in_excel
from querys.query_list import build_query_list


async def download_all_file():
    for e in build_query_list():
        result = await gql_query(e)
        if "accounting_invoice" in e.name:
            _data_list = await accounting_invoice(result)
            await export_in_excel(e.name, _data_list, _accConstList)
        elif "accounting_driver_payment" in e.name:
            _data_list = await accounting_driver_payment(result)
            await export_in_excel(e.name, _data_list, _driverPaymentList)


async def gql_query(_gql_query: GqlQuery) -> json:
    transport = AIOHTTPTransport(url="GRAPHQL_URL",
                                 headers={'Content-Type': 'application/json',
                                          'x-hasura-admin-secret': "SECRET_KEY"})

    # Using `async with` on the client will start a connection on the transport
    # and provide a `session` variable to execute queries on this connection
    async with Client(
            transport=transport, fetch_schema_from_transport=True,
    ) as session:
        # Execute single query
        query = gql(_gql_query.query)
        params = _gql_query.param
        result = await session.execute(query, variable_values=params)
    return result


asyncio.run(download_all_file())
