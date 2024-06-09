# 資料夾結構
```
my_transformer_project/
├── src/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # Flask application entry point
│   │   ├── routes.py          # Flask routes
│   │   ├── utils.py           # Helper functions
│   │   └── models/            # Trained models and related files
│   │       └── model_name/
│   │           ├── config.json
│   │           ├── pytorch_model.bin
│   │           └── tokenizer.json
│   ├── data/
│   │   ├── raw/               # Raw data
│   │   └── processed/         # Processed data ready for training
│   ├── scripts/
│   │   ├── train.py           # Script for training the model
│   │   ├── evaluate.py        # Script for evaluating the model
│   │   └── preprocess.py      # Script for preprocessing data
│   ├── notebooks/
│   │   ├── exploration.ipynb  # Jupyter notebooks for data exploration
│   │   └── training.ipynb     # Jupyter notebooks for training experiments
│   ├── config/
│   │   ├── config.yaml        # Configuration file for the project
│   │   └── logging.conf       # Logging configuration
│   ├── tests/
│   │   ├── test_app.py        # Tests for the Flask application
│   │   ├── test_train.py      # Tests for the training scripts
│   │   └── test_utils.py      # Tests for utility functions
│   ├── __init__.py            # Makes src a package
├── .gitignore                 # Git ignore file
├── poetry.lock                # Poetry lock file
├── pyproject.toml             # Poetry configuration file
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies (if needed)
```