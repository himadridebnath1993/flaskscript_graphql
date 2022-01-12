from typing import List

from app.model.gqlQuery import GqlQuery


def build_query_list() -> List[GqlQuery]:
    return [GqlQuery(
        "accounting_invoice",
        """ 
            query q1 {
              accounting_invoice(where: {_and: [{end_date: {_lt: "2021-12-01"}}, {end_date: {_gte: "2021-11-01"}}, {invoice_status_id: {_eq: 3}}]}, limit: 10) {
                invoice_details {
                  invoice {
                    iid
                  }
                  unit
                  vehicle_no
                  base_price
                  total_price
                  price_summary
                  contract_details
                }
              }
            }
        """,
        {}), GqlQuery(
        'accounting_driver_payment',
        """ 
            query q2 {
              accounting_driver_payment(where: {_or: [{_and: [{order_id: {_is_null: false}}, {order: {date: {_lt: "2021-12-01"}}}, {order: {date: {_gte: "2021-11-01"}}}, {paid: {_eq: true}}]}, {_and: [{order_id: {_is_null: true}}, {contract_id: {_is_null: false}}, {paid: {_eq: true}}, {created_at: {_lt: "2021-12-01"}}, {created_at: {_gte: "2021-11-01"}}]}, {_and: [{order_id: {_is_null: true}}, {contract_id: {_is_null: true}}, {payout_settlement_id: {_is_null: false}}, {paid: {_eq: true}}, {payout_settlement: {end_date: {_lt: "2021-11-01"}}}, {payout_settlement: {end_date: {_gte: "2021-10-01"}}}]}]}, limit: 10) {
                approved_amount
                order_id
                driver_payment_type {
                  name
                }
                contract_id
                contract {
                  unit {
                    name
                  }
                  cid
                }
                payout_settlement_id
                contract {
                  cid
                }
                correction_amount
                price_details
              }
            }
        """,
        {})]
