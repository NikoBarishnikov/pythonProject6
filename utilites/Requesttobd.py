import datetime

import psycopg2 as psql


def check_event(timestamp):
    connection = psql.connect(
        "host=176.9.23.247 dbname=discovery_dev user=discovery_dev_user password=kd034jx89JFk349F%&((($kfgf")
    cursor = connection.cursor()
    sql_statement = f"SELECT distinct (event_type) " "FROM public.analytic_service " \
                    f"WHERE " \
                    f"client_type IN ('Driver') " \
                    f" and device_model IN ('PSP7530DUO')" \
                    f"and event_timestamp >= '{timestamp}'"

    cursor.execute(sql_statement)

    raw_events = cursor.fetchall()

    return raw_events

    # for i in raw_events:
    #  print(i[0])

    # if not raw_events:
    # print('Not found events!')
    # return
    # print('All is ok!')

    #connection.close()
