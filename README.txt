PATHFINDER AI - Science, Commerce and Humanities (14 questions, 10 fields each)

EASY START (Windows): double-click run.bat
  -> installs requirements, trains all 3 models, launches the app.

MANUAL (run from inside this folder):
  py -m pip install -r requirements.txt
  py train_model.py
  py -m streamlit run app.py

FILES
  app.py                       Streamlit app. Sidebar: choose Science / Commerce / Humanities,
                               then Career Finder or Model Evaluation.
  streams.py                   All fields, questions and scoring rubrics for the 3 streams
                               (edit this file to change a question or field).
  train_model.py               Trains one model per stream -> models/ folder (created automatically).
  generate_dataset.py          Regenerates datasets/*.csv from the rubric in streams.py.
  datasets/science_data.csv
  datasets/commerce_data.csv
  datasets/humanities_data.csv 3000 synthetic students each: 14 answers (1-5) + 10 scores (0-100).

If you change streams.py or a CSV: run generate_dataset.py (optional) then train_model.py again.
