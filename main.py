'''In this app, we are going to read a file that contains a series of data and
predict it using the training model.'''

# import library
import pandas as pd
import tensorflow as tf

model = tf.keras.models.load_model("")

data = pd.read_csv("")

pridiction = model.pridict(data)
