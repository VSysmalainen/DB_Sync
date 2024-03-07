from db import db_params_dp, db_params_mcc, db_params_lis_nsb
from query import QueryExecutor


query_executor_dp = QueryExecutor(db_params_dp)
query_executor_mcc = QueryExecutor(db_params_mcc)
query_executor_lis_nsb = QueryExecutor(db_params_lis_nsb)


mcc_case_ids = f"""
SELECT id FROM cases WHERE title LIKE '%NSB%' and client_specialist_id is null and created_at > '2023-11-25 15:15:01.979 +0300'
"""


query_mcc_case_ids = query_executor_mcc.execute_query(mcc_case_ids)

result_mcc_case_ids = [str(t[0]) for t in query_mcc_case_ids]  # Создаём список айди незаполненных кейсов из мсс


dp_case_case_ids = f"""
SELECT id FROM cases WHERE title LIKE '%NSB%' and (lis_doctor is null or lis_doctor = '') and creation_date > '2023-11-25 15:15:01.979 +0300'
"""


query_dp_case_ids = query_executor_dp.execute_query(dp_case_case_ids)

result_dp_case_ids = [str(t[0]) for t in query_dp_case_ids]  # Создаём список айди незаполненных кейсов из dp


nsb_names_and_ids = f"""
select cases.id, cases.doctor_id, client_specialists."name"
from cases join client_specialists on client_specialists.id = cases.doctor_id
where dp_id > '' and cases.created_at > '2023-11-25 15:15:01.979 +0300'
"""


query_nsb_titles_doctor_ids_names = query_executor_lis_nsb.execute_query(nsb_names_and_ids)

# Создаём словарь из кейс айди и айдишников специалистов с условием, что кейс айди есть в списке незаполненных кейсов мсс
nsb_lis_case_ids_and_specialist_ids_dict_to_mcc = {}
for i in query_nsb_titles_doctor_ids_names:
    if i[0] in result_mcc_case_ids:
        nsb_lis_case_ids_and_specialist_ids_dict_to_mcc[i[0]] = i[1]

# Создаём словарь из кейс айди и имен специалистов с условием, что кейс айди есть в списке незаполненных кейсов dp
nsb_lis_case_ids_and_names_dict_to_dp = {}
for i in query_nsb_titles_doctor_ids_names:
    if i[0] in result_dp_case_ids:
        nsb_lis_case_ids_and_names_dict_to_dp[i[0]] = i[2]


for case_id, specialist_id in nsb_lis_case_ids_and_specialist_ids_dict_to_mcc.items():
    mcc_cases_update = f"""
    UPDATE public.cases
    SET client_specialist_id='{specialist_id}'::uuid
    WHERE id='{case_id}'::uuid
    RETURNING id, title, client_specialist_id
    ;
    """
    query_mcc_cases_update = query_executor_mcc.execute_query(mcc_cases_update)


for case_id, specialist_name in nsb_lis_case_ids_and_names_dict_to_dp.items():
    dp_cases_update = f"""
    UPDATE public.cases
    SET lis_doctor='{specialist_name}'
    WHERE id='{case_id}'::uuid
    RETURNING id, title, lis_doctor
    ;
    """
    query_dp_cases_update = query_executor_dp.execute_query(dp_cases_update)
