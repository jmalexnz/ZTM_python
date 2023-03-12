from imageai.Classification import ImageClassification
import os
# python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl
# pip3 install keras opencv-python
# pip3 install imageai --upgrade
# pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
# have to use nightly build or won't work with Python 3.11
exec_path = os.getcwd()
# https://imageai.readthedocs.io/en/latest/prediction/index.html
# download MobileNetV2 from there
# Load in pre-built model
prediction = ImageClassification()
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(exec_path, 'mobilenet_v2-b0353104.pth'))
prediction.loadModel()

# generate the predictions for an image
predictions, probabilities = prediction.classifyImage(os.path.join(exec_path, 'house.jpeg'), result_count=5)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(f'{eachPrediction} : {eachProbability}')
