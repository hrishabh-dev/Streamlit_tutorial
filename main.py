import streamlit as st
import numpy as np 
import pickle 
import time

with open("model.pkl",'rb') as file: 
    model=pickle.load(file) 

target=['setosa','versicolor','virginica']

st.title("IRIS FLOWER PREDICTION")
st.subheader("Brewed with Streamlit")
if 'sepal_length' not in st.session_state:
    st.session_state['sepal_length'] = 5.0
if 'sepal_width' not in st.session_state:
    st.session_state['sepal_width'] = 3.0
if 'petal_length' not in st.session_state:
    st.session_state['petal_length'] = 1.5
if 'petal_width' not in st.session_state:
    st.session_state['petal_width'] = 0.2
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=20.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=20.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=20.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=20.0, step=0.1)



if st.button("Clear"):
    with st.spinner("Clearing...... please wait") :
        time.sleep(1)
        try:
            st.session_state['sepal_length'] = 5.0
            st.session_state['sepal_width'] = 3.0
            st.session_state['petal_length'] = 1.5
            st.session_state['petal_width'] = 0.2
            st.rerun() 
        except Exception as e :
            st.write("Some error occured")




setosas="""
        It is a type of wild iris plant.
        Native to North America.
        Has light-colored, white or pale purple flowers.
        Flowers bloom in late spring or early summer.
        Grows in moist areas like stream banks and meadows.
        The plant is a perennial, meaning it lives for many years.
        It has long, narrow leaves.
        Flowers are pretty and often used in gardens.
        Symbolizes purity and innocence.
        Not endangered, but needs natural habitat to stay healthy."""

versi="""
        It is a type of wild iris plant.
        Also called Harlequin Blue Iris.
        Native to North America.
        Has beautiful blue or purple flowers with white markings.
        Blooms in late spring to early summer.
        Grows in wet places like marshes, stream banks, and wetlands.
        Perennial plant (lives for many years).
        Has long, sword-shaped leaves.
        Used in gardens for its pretty flowers.
        Symbolizes faith and hope.
        Needs moist soil to grow well

"""

virg="""
        It is a type of wild iris plant.
        Also called Southern Blue Iris.
        Native to the southeastern United States.
        Has large, blue to purple flowers.
        Blooms in late spring to early summer.
        Grows in wet areas like swamps, marshes, and riverbanks.
        Perennial plant (lives for many years).
        Has tall, sword-shaped leaves.
        Often used in natural landscapes and gardens.
        Symbolizes purity and beauty.
        Prefers moist, rich soil to thrive.

"""

if st.button("Predict"):
    with st.spinner("Predicting...... please wait") :
        time.sleep(2)
        try:
            input_features=np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            prediction_idx=model.predict(input_features)[0]
            predicted_class=target[prediction_idx]
            st.success("Prediction completed")

            st.write(f"Iris Species :- {predicted_class.capitalize()}")
            if predicted_class=="setosa":
                st.write(setosas)
            elif predicted_class=="versicolor":
                st.write(versi)
            elif predicted_class=="virginica":
                st.write(virg)
            else:
                print("No flower found")
        except Exception  as e :
            st.error("Error occured during prediction")
                


st.caption(f"Powered by Streamlit version :- {st.__version__}")



