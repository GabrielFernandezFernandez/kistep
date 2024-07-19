import os
from pathlib import Path
from steproids.data import create_track_2_dataset

os.umask(7)  # Allow other users in the same computer to access and edit the created files

data_path = Path("/media/scratrch_data/nanoninjas/data/raw")
dataset_name = "medium_49"

n_exps_per_model = 2000  # 10 takes about 8-9min to make

create_track_2_dataset(data_path/dataset_name, n_exps_per_model)