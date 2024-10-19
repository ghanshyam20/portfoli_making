import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


#--HERO SECTION----


col1,col2=st.columns(2,gap="small",vertical_alignment="center")

with col1:
    st.image("./assets/profile image.png",width=350)


with col2:
    st.title("Ghanshyam Bhattarai",anchor=False)
    st.write(
        "Mid Level python Developer,data analyst,Power Bi"
    )
    if st.button("✉️ CONTACT ME"):
        show_contact_form()

#----EXPERIENCE AND QUALIFICATIONS---



st.write("\n")
st.subheader("Experience & Qualifications",anchor=False)
st.write(
    """
    ✅3 years experience extracting actionale insights from data\n
    ✅Strong hands-on experience and knowledge in python and Exel\n
    ✅Good understanding of statstical principles and their respective applications\n
    ✅Excellent team-player and displaying a strong sense of initiative on tasks\n
    
    
    """

        )
#---Skills---


st.write("\n")
st.subheader("Hard Skills",anchor=False)
st.write(
    """
    ✅Programming:Python(Django,Sciket-learn,Pandas),SQL\n
    ✅Data Visulization:Power BI,Ms Excel\n
    ✅Modeling:Logistics regression,linear Regressin,Descision Trees\n
    ✅Data Strucutre and Algorithm\n
    ✅Databases:Postgres,MySQL\n
    ✅Data Analysis\n
    ✅Linux\n
    ✅CMS wordpress\n
    ✅Powershell\n

    """
        )