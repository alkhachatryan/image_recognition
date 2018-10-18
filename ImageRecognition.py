from imageai.Prediction import ImagePrediction

import os
import json

project_path = os.path.dirname(os.path.realpath(__file__)) + '/'

def recognize(file):

    prediction = ImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath(project_path + "restnet.h5")
    prediction.loadModel()

    predictions, percentage_probabilities = prediction.predictImage(file, result_count=5)
    result = {}
    for index in range(len(predictions)):
        result[predictions[index]] = percentage_probabilities[index]

    os.remove(file)

    return json.dumps(result)


def upload(form_file):
    uploaded_file_path = os.path.join(project_path, os.path.basename(form_file.filename))
    with open(uploaded_file_path, 'wb') as fout:
        while True:
            chunk = form_file.file.read(100000)
            if not chunk:
                break
            fout.write(chunk)
    return uploaded_file_path
