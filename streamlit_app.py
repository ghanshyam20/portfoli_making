import streamlit as st

#---page setup----
about_page = st.Page(
    page='views/about_me.py',
    title='About me',
    icon=":material/account_circle:",
    default=True,
)

project_1_page = st.Page(
    page='views/sales_dashboard.py',
    title="Sales Dashboard",
    icon=':material/bar_chart:',
)

project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)


st.logo("assets/python-logo-only.png")

# Sidebar content
st.sidebar.text("Made with GhanShyam")

#----NAVIGATION SETUP----
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page]
    }
)

#--RUN NAVIGATION---
pg.run()
