# 參考資源
- [官方訓練ipynb](https://github.com/NielsRogge/Transformers-Tutorials/blob/master/LayoutLMv3/Fine_tune_LayoutLMv3_on_FUNSD_(HuggingFace_Trainer).ipynb)
- [How to Train LayoutLM on a Custom Dataset with Hugging Face](https://github.com/NielsRogge/Transformers-Tutorials/blob/master/LayoutLMv3/Fine_tune_LayoutLMv3_on_FUNSD_(HuggingFace_Trainer).ipynb)
- [yuyijiong/layoutlmv3-base-chinese-xfund](https://huggingface.co/yuyijiong/layoutlmv3-base-chinese-xfund/tree/main)
- [xfund-dataset](https://github.com/doc-analysis/XFUND)

# XFUND site
```
@inproceedings{xu-etal-2022-xfund,
    title = "{XFUND}: A Benchmark Dataset for Multilingual Visually Rich Form Understanding",
    author = "Xu, Yiheng  and
      Lv, Tengchao  and
      Cui, Lei  and
      Wang, Guoxin  and
      Lu, Yijuan  and
      Florencio, Dinei  and
      Zhang, Cha  and
      Wei, Furu",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2022",
    month = may,
    year = "2022",
    address = "Dublin, Ireland",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.findings-acl.253",
    doi = "10.18653/v1/2022.findings-acl.253",
    pages = "3214--3224",
    abstract = "Multimodal pre-training with text, layout, and image has achieved SOTA performance for visually rich document understanding tasks recently, which demonstrates the great potential for joint learning across different modalities. However, the existed research work has focused only on the English domain while neglecting the importance of multilingual generalization. In this paper, we introduce a human-annotated multilingual form understanding benchmark dataset named XFUND, which includes form understanding samples in 7 languages (Chinese, Japanese, Spanish, French, Italian, German, Portuguese). Meanwhile, we present LayoutXLM, a multimodal pre-trained model for multilingual document understanding, which aims to bridge the language barriers for visually rich document understanding. Experimental results show that the LayoutXLM model has significantly outperformed the existing SOTA cross-lingual pre-trained models on the XFUND dataset. The XFUND dataset and the pre-trained LayoutXLM model have been publicly available at https://aka.ms/layoutxlm.",
}
```

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