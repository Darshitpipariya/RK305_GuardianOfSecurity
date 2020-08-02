from keras.models import model_from_json
import json


def load_model_LSTM():
    with open(r"lib\files\data1DConvLSTM.json", "r") as f:
        model_json = json.load(f)
        model = model_from_json(model_json)
    model.load_weights(r"lib\files\data1DConvLSTM.h5")
    return model
