@echo off

REM Выполнение скриптов по порядку
echo Running data_creation.py
python data_creation.py

echo Running model_preprocessing.py
python model_preprocessing.py

echo Running model_preparation.py
python model_preparation.py

echo Running model_testing.py
python model_testing.py

echo Pipeline execution completed.