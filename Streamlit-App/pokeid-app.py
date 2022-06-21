import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import Resizing

@st.cache(allow_output_mutation=True)
def load_type():
    return tf.keras.models.load_model('Models/type_select_model')

@st.cache(allow_output_mutation=True)
def load_ind():   
    model_dict = {}
    for name in type_names:
        model_dict[name] = tf.keras.models.load_model(f'Models/{name}_model')
    return model_dict

@st.cache
def load_stats():
    poke_stats = pd.read_csv('Data/pokestats_gen7_rev2.csv', header=[0], index_col=0)
    poke_stats.columns.name = 'Pokedex Number'
    poke_stats.fillna('', inplace=True)
    return poke_stats

type_model = load_type()
type_names =['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting', 'Fire', 'Ghost', 'Grass', 
            'Ground', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock', 'Steel', 'Water']

ind_dict = load_ind()
poke_stats_df = load_stats()

pokemon_dict= pd.read_csv('Data/pokemon_class_dict.csv', header=None, index_col=0, squeeze=True).to_dict()

st.title('Welcome to the Pokemon ID Project') 

# Prompt user to upload an image and convert that file into an array/batch the models can use to predict
user_pic_file = st.file_uploader(label='Please upload your picture to identify what pokemon it is.',
                    type=['png', 'jpg', 'jpeg'])

if user_pic_file is not None:
    st.subheader("Your image")
    user_img = image.load_img(user_pic_file, target_size=(128, 128))
    st.image(user_img)
    user_array = image.img_to_array(user_img)
    user_batch = np.expand_dims(user_array, axis=0)

    # Use converted image to predict type of pokemon
    user_pred = type_model.predict(user_batch)
    user_type = type_names[np.argmax(user_pred)]
    st.write(f"Your Pokemon's type is {user_type}!")

    # Based on type, use appropriate model to ID individual pokemon
    ind_model = ind_dict[user_type]
    ind_pred = ind_model.predict(user_batch)
    ind_list = pokemon_dict[user_type].split(',')
    ind_pokemon = ind_list[np.argmax(ind_pred)]
    ind_pokemon = ind_pokemon.replace("'", "")
    ind_num = ind_pokemon.split('-')[0]
    ind_name = ind_pokemon.split('-')[1]

    st.write(f"Your Pokemon is number{ind_num}, {ind_name}!")

    # Display Stats
    st.write("It's stats are:")
    display_df = poke_stats_df.loc[poke_stats_df.index == int(ind_num)]
    display_df = display_df.iloc[0, 3:]
    st.write(display_df.astype(str))