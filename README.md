This is a framework for text classification by deep learning.

This branch is for tuning on Relation Extraction Attention-Based BiLSTM.
### Datasets
- Relation Extraction - Att-BiLSTM (69.85; if new format: 55.46%)

```bash
python train.py \
-lower \
-data_dir data/pubmed
-data_dir ~/proj/1908_prac_toxic/data/yelp/ \

-data_sizes 5 5 5 -batch_size 4 -verbose \
-data_dir data/pubmed -train_fname data.csv

```


### Step 1. Take a deep breath.

Do look into the data. At least read through 100 examples. Run python look_into_data.py.

- Understand the Input and Output.
- Find some signals for negative and positive samples.
- When programming, don't bother to look back at the data format again.

### Dataloading
```
python data/re_semeval/reader.py
python preprocess.py
```

### Train and Tune
```bash
python train.py \
-data_dir data/webnlg \
```
- 20190909 run: 71.2% on semeval

### Evaluate
```bash
python train.py -load_model 'tmp/model' \
-data_dir data/webnlg \

```


