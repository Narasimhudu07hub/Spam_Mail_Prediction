import pickle
import streamlit as st
model = pickle.load(open("spam.pkl", "rb"))
cv=pickle.load(open("vectorizer.pkl", "rb"))

def main():
    st.title("Email/sms Spam Classifier")
    st.subheader("Build")
    msg=st.text_area("Enter a message")
    if st.button("predict"):
        data = [msg]
        vect = cv.transform(data).toarray()
        prediction = model.predict(vect)
        result = prediction[0]
        if result == 1:
            st.error("This is a Spam mail")
        else:
            st.success("Ham mail")

main()