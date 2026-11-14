import streamlit as st
from donorView import BloodDonorManager



donor_instance = BloodDonorManager()

tab1, tab2, tab3, tab4 = st.tabs(["Add Donor", "View Donors", "Update Donor", "Delete Donor"])
blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

with tab1:
    st.header("Add New Donors...!")
    name = st.text_input("Enter Donor Name")
    phone = st.text_input("Enter Donor Phone Number")
    blood_group = st.selectbox("select Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
    city = st.text_input("Enter Donor City")
    last_donation = st.date_input("Enter Last Donation Date")
    if st.button("Submit"):
        donor_instance.post(name=name, blood_group=blood_group, phone=phone, city=city, last_donation=last_donation)
        st.success("Donor added successfully..!")

with tab2:
    st.header("View Blood Donor Details..!")
    records = donor_instance.get()
    print("-----------")
    print(records)
    if records:
        st.table(records)
    else:
        st.warning("No Donor Details Available...!")

with tab3:
    st.header("Update Donor Details")
    records = donor_instance.get()

    if records:
        donor_ids = [r[0] for r in records]
        id = st.selectbox("Select Donor ID", donor_ids, key = "update_id")
        record = donor_instance.get_object(id=id)
        name = st.text_input("Enter name", value=record[1])
        blood_group = st.selectbox("Select your blood group",
                                   blood_groups,
                                   index=blood_groups.index(record[2]),
                                   key = "update_groups"
                                   )
        phone = st.text_input("Enter Donor phone number", value=record[3])
        city = st.text_input("Enter city", value=record[4])
        last_donation = st.date_input("Enter last donation", value=record[5])

        if st.button("Update"):
            status, message = donor_instance.put(id=id,
                                                 name=name,
                                                 blood_group=blood_group,
                                                 city=city,
                                                 last_donation=last_donation)
            if status:
                st.success(message)
                
            else:
                st.error(message)
        else:
            st.warning("No donor found")

with tab4:
    st.header("Delete Donor Details")

    records = donor_instance.get()

    if records:
        donor_ids = [r[0] for r in records]

        id = st.selectbox(
            "Select Donor ID",
            donor_ids,
            key="delete_id"
        )

        record = donor_instance.get_object(id=id)

        st.write("Donor Name:", record[1])
        st.write("Blood Group:", record[2])
        st.write("Phone:", record[3])
        st.write("City:", record[4])
        st.write("Last Donation:", record[5])

        if st.button("Delete Donor"):
            status, message = donor_instance.delete(id=id)

            if status:
                st.success(message)
            else:
                st.error(message)

    else:
        st.warning("No Donor Details Available...!")