import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

path = "dataset_phishing.csv"

data = pd.read_csv(path)

data.head()

'ip'
'nb_www', 'nb_com','nb_dslash', 'http_in_path', 
'https_token', 'punycode', 'port'
'ratio_digits_url', 'ratio_digits_host'