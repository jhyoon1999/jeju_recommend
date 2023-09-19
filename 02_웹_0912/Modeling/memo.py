from libreco.data import DataInfo
from libreco.algorithms import DeepFM
import pandas as pd

loaded_data_info = DataInfo.load("model_path", model_name='DeepFM')
loaded_model = DeepFM.load("model_path", model_name='DeepFM', data_info=loaded_data_info)

len(loaded_data_info.user2id)