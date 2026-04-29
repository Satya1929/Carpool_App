
# import streamlit as st

# def main():
#     # st.title("Travel Partner Finder")
#     st.header("Seeking travel partner?🧑‍🤝‍🧑 Look no further!! (Back to College)")

#     st.write(
#         """
#         Welcome to the Travel Match App! 🚗 
        
#         Trusted by 400+ Users in Diwali along with 130+ entries !!

#         Your go-to platform for finding the perfect travel partner based on shared preferences. Just fill out a quick form and you're all set!

#         Don't miss out on this opportunity! Start now by filling out the form. 🚀 
#         """
#     )

#     # Google Form and Spreadsheet links
#     st.markdown(
#         """
#         📍Pages Available:
#         - *🏡 Home -> Form:* Enter your preferences [Here](<https://docs.google.com/forms/d/e/1FAIpQLScmQSHtkn3IhlAm7NJFA_ujO2vSKNP_lS7i4g2VQG1nWNT-2g/viewform>).
#         - *🏡 Home -> Spreadsheet:* Access traveler info to connect with potential matches [Here](<https://docs.google.com/spreadsheets/d/1fbEmtrmVu9heYMfL5P1a9qJ5q0xT3tFj3y2TFVEiGIk/edit>).
#         - *🔎 Match By Date:* Select your preferred date to match with 100+ travelers. Plus, plan your time and destination with our analysis of fellow travelers.
#         - *📊 All Dates Summary:* View the overall preferences of everyone out there!
#         """
#     )

#     st.write(
#         """
#         Start your journey and make carpooling hassle-free! 🎉

#         Got questions or feedback? Feel free to DM me anytime! 👀✌🏻 (7735416363)

#         📍 IMPORTANT: A link to edit Your Response will be emailed to you 
    
#         📍 YouTube: [Carpool Guide](https://www.youtube.com/watch?v=HJjtxDpOIow) 

#         """
#     )


# if __name__ == "__main__":
#     main()















import streamlit as st

def main():
    # st.title("Travel Partner Finder")
    st.header("Seeking travel partner?🧑‍🤝‍🧑 Look no further!! (Back to Home)")

    st.write(
        """
        Welcome to the Travel Match App! 🚗 
        
        Trusted by 1000+ Users along with 700+ entries till date !!

        Your go-to platform for finding the perfect travel partner based on shared preferences. Just fill out a quick form and you're all set!

        Don't miss out on this opportunity! Start now by filling out the form. 🚀 
        """
    )

    st.subheader("📍 Navigation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.link_button("📝 Fill the Form", "https://docs.google.com/forms/d/e/1FAIpQLScmQSHtkn3IhlAm7NJFA_ujO2vSKNP_lS7i4g2VQG1nWNT-2g/viewform", use_container_width=True)
        if st.button("🔎 Search by Date", use_container_width=True):
            st.switch_page("pages/1_🔎_Search_by_Date.py")

    with col2:
        st.link_button("📅 View Spreadsheet", "https://docs.google.com/spreadsheets/d/1fbEmtrmVu9heYMfL5P1a9qJ5q0xT3tFj3y2TFVEiGIk/edit?usp=sharing", use_container_width=True)
        if st.button("📊 All Days Summary", use_container_width=True):
            st.switch_page("pages/2_📊_All Days_Summary.py")

    if st.button("🎉 View Credits", use_container_width=True):
        st.switch_page("pages/3_🎉_Credits_Page.py")

    st.divider()

    st.write(
        """
        Start your journey and make carpooling hassle-free! 🎉

        Got questions or feedback? Feel free to DM me anytime! 👀✌🏻 (7735416363)

        📍 IMPORTANT: A link to edit Your Response will be emailed to you 
    
        📍 YouTube: [Carpool Guide](https://www.youtube.com/watch?v=HJjtxDpOIow) 

        """
    )


if __name__ == "__main__":
    main()