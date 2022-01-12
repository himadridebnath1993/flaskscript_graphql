import json

from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

from app.model.gqlQuery import GqlQuery


async def gql_query(_gql_query: GqlQuery) -> json:
    transport = AIOHTTPTransport(url="GRAPH_QL_URL",
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


