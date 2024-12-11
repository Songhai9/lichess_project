import kagglehub

# Download latest version
path = kagglehub.dataset_download("noobiedatascientist/lichess-september-2020-data")

print("Path to dataset files:", path)