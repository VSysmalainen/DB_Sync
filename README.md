Скрипт внесения направивших врачей из базы данных lis Новосибирска  
в dp-main и mcc-main.  
Подключить впн NSB и впн лабы  
Указать через ENV переменные параметры баз данных (LIS NSB, DP, MCC).  
Пример:  
LIS_NSB_POSTGRES_USER  
LIS_NSB_POSTGRES_PASSWORD  
LIS_NSB_POSTGRES_HOST  
LIS_NSB_POSTGRES_PORT  
LIS_NSB_POSTGRES_DB  
Запуск локально:  
1) создать виртуальное окружение  
2) в корне проекта выполнить команду pip install -r -requirements.txt для установки зависимостей
3) выполнить команду python 01.py
4) дождаться окончания выполнения скрипта
5) после выполнения скрипта логи будут доступны в папке logs
