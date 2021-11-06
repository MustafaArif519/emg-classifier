# EMG-classifier
# Instructions for using virtual environment (optional)
1. python3 -m venv env
2. pip3 install -r requirements.txt
# Data Rearrangement
1. Used EMG_training_raw from the website to arrange them into different training classes
2. Running this is a bit slow. Any better ideas?
![image](https://user-images.githubusercontent.com/59846636/140615271-f7a2213a-fe3e-40a2-9b44-87474c273e57.png)
Example of 1 file
3. Only run once
# Data preprocessing
1. Change them into same dimensions (same number of time points) e.g. 1200 x 8 / 2000 x 8
2. Only run once
# Model.py
1. Define convolution, pooling, linear layers in the __init__
2. Assign starting weights
3. Combine them in forward()
