import numpy
from sklearn.linear_model import LogisticRegression
import streamlit

streamlit.title("Student Result Prediction")
working_hours = numpy.array([[1],[2],[3],[4],[5],[6]])
y_train = numpy.array([0,0,0,1,1,1])

object = LogisticRegression()
object.fit(working_hours,y_train)


value_input = streamlit.number_input("Enter the working hours :")
new_value = numpy.array([[value_input]])
predict_value = object.predict(new_value)

streamlit.button("Enter")
if predict_value == 1:
    streamlit.success("Pass")
else:
    streamlit.error("Fail")