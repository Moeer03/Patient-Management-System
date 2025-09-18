import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Patient Management System", page_icon="🩺", layout="centered")
st.title("🩺 Patient Management System")

# Sidebar navigation
choice = st.sidebar.radio("Choose Action", ["View All", "Search Patient", "Sort Patients", "Create Patient", "Update Patient", "Delete Patient"])

if choice == "View All":
    st.header("All Patients")
    res = requests.get(f"{API_URL}/view")
    if res.status_code == 200:
        st.json(res.json())
    else:
        st.error("Failed to load patients")

elif choice == "Search Patient":
    st.header("Search Patient")
    patient_id = st.text_input("Enter Patient ID (e.g., P001)")
    if st.button("Search"):
        res = requests.get(f"{API_URL}/patient/{patient_id}")
        if res.status_code == 200:
            st.json(res.json())
        else:
            st.error("Patient not found")

elif choice == "Sort Patients":
    st.header("Sort Patients")
    sort_by = st.selectbox("Sort by", ["height", "weight", "bmi"])
    order = st.radio("Order", ["asc", "desc"])
    if st.button("Sort"):
        res = requests.get(f"{API_URL}/sort", params={"sort_by": sort_by, "order": order})
        if res.status_code == 200:
            st.json(res.json())
        else:
            st.error(res.json().get("detail", "Error sorting patients"))

elif choice == "Create Patient":
    st.header("Create Patient")
    with st.form("create_form"):
        patient_id = st.text_input("Patient ID")
        name = st.text_input("Name")
        city = st.text_input("City")
        age = st.number_input("Age", min_value=1, max_value=120)
        gender = st.selectbox("Gender", ["male", "female", "others"])
        height = st.number_input("Height (in meters)", min_value=0.1)
        weight = st.number_input("Weight (in kg)", min_value=0.1)
        submitted = st.form_submit_button("Create")
        if submitted:
            data = {
                "id": patient_id.upper(),
                "name": name,
                "city": city,
                "age": age,
                "gender": gender,
                "height": height,
                "weight": weight
            }
            res = requests.post(f"{API_URL}/create", json=data)
            if res.status_code == 201:
                st.success("Patient created successfully!")
            else:
                st.error(res.json().get("detail", "Error creating patient"))

elif choice == "Update Patient":
    st.header("Update Patient")
    with st.form("update_form"):
        patient_id = st.text_input("Patient ID")
        name = st.text_input("New Name (optional)")
        city = st.text_input("New City (optional)")
        age = st.number_input("New Age", min_value=0, max_value=120, value=0)
        gender = st.selectbox("New Gender (optional)", ["", "male", "female", "others"])
        height = st.number_input("New Height (in meters)", min_value=0.0, value=0.0)
        weight = st.number_input("New Weight (in kg)", min_value=0.0, value=0.0)
        submitted = st.form_submit_button("Update")
        if submitted:
            payload = {}
            if name: payload["name"] = name
            if city: payload["city"] = city
            if age > 0: payload["age"] = age
            if gender: payload["gender"] = gender
            if height > 0: payload["height"] = height
            if weight > 0: payload["weight"] = weight

            res = requests.put(f"{API_URL}/edit/{patient_id}", json=payload)
            if res.status_code == 200:
                st.success("Patient updated successfully!")
            else:
                st.error(res.json().get("detail", "Error updating patient"))

elif choice == "Delete Patient":
    st.header("Delete Patient")
    patient_id = st.text_input("Enter Patient ID to delete")
    if st.button("Delete"):
        res = requests.delete(f"{API_URL}/delete/{patient_id}")
        if res.status_code == 200:
            st.success("Patient deleted")
        else:
            st.error("Patient not found")
