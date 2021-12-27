import os

os.system(f"poetry run black --check ./sensirion_sps30")
os.system(f"poetry run isort --profile black ./sensirion_sps30")
