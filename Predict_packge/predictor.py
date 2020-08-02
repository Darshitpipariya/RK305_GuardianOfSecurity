from lib.load_model import *
from keras.preprocessing import sequence
from string import printable
import warnings

warnings.filterwarnings("ignore")

LSTM = load_model_LSTM()


def Vector(url):
    max_len = 75
    url_int_tokens = [[printable.index(x) + 1 for x in url if x in printable]]
    X = sequence.pad_sequences(url_int_tokens, maxlen=max_len)
    return X


def predictor(url):
    feature = Vector(url)
    prediction_LSTM = LSTM.predict(feature, batch_size=1)
    if prediction_LSTM < 0.65:
        prediction_LSTM = 0
    else:
        prediction_LSTM = 1
    return prediction_LSTM
