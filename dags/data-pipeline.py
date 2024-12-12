from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

from datetime import datetime

# bronze data
from pipelines.get_data_to_bronze import main as get_data_to_bronze
from pipelines.transform_data_to_silver import main as transform_data_to_silver
from pipelines.present_data_in_gold import main as present_data_in_gold

with DAG(
    dag_id='data-pipeline',
    start_date=datetime(2024, 11, 12),
    schedule_interval=None
) as dag:
 
    start_task = EmptyOperator(
        task_id='start'
    )

    get_data_to_bronze = PythonOperator(
        task_id='get_data_to_bronze',
        python_callable=get_data_to_bronze
    )

    transform_data_to_silver = PythonOperator(
        task_id='transform_rates_to_silver',
        python_callable=transform_data_to_silver
    )

    present_data_in_gold = PythonOperator(
        task_id='present_data_in_gold',
        python_callable=present_data_in_gold
    )


    end_task = EmptyOperator(
        task_id='end'
    )

    start_task >> [get_data_to_bronze >> transform_data_to_silver >> present_data_in_gold ] >> end_task