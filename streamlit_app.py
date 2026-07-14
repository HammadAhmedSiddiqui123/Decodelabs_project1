"""Streamlit UI — run: streamlit run streamlit_app.py"""

import streamlit as st

from password_checker import check_password

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.title("🔐 Password Strength Checker")
st.caption("DecodeLabs · Cyber Security Project 1")

password = st.text_input("Enter password", type="password")

if password:
    r = check_password(password)
    colors = {"Weak": "🔴", "Medium": "🟡", "Strong": "🟢"}
    progress = {"Weak": 0.33, "Medium": 0.66, "Strong": 1.0}

    st.subheader(f"{colors[r['strength']]} {r['strength']}")
    st.progress(progress[r["strength"]])
    st.write(r["message"])

    st.write(
        f"Length: {r['length']} | "
        f"Upper: {'✅' if r['has_upper'] else '❌'} | "
        f"Lower: {'✅' if r['has_lower'] else '❌'} | "
        f"Digit: {'✅' if r['has_digit'] else '❌'} | "
        f"Symbol: {'✅' if r['has_symbol'] else '❌'}"
    )
else:
    st.info("Type a password to check its strength.")
