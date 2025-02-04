import streamlit as st
import requests
import re


API_URL = "http://localhost:8000/resolve-contact"

def is_valid_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone):
    """Validate phone number format - allows digits and optional +"""
    pattern = r'^\+?\d{10,15}$'
    return bool(re.match(pattern, phone))

st.title("Customer Identity Resolution Service")

st.markdown("""
    Use this application to resolve customer identities based on email and phone number.
    The service will consolidate data under a single primary contact, linking all related secondary records.
""")

st.header("Enter Customer Details")
email = st.text_input("Email Address", help="Enter a valid email address (e.g., example@domain.com)")
phone = st.text_input("Phone Number", help="Enter a valid phone number (10-15 digits, optionally starting with +)")

if st.button("Resolve Contact"):
    if not email or not phone:
        st.error("Error: Either Email or Phone number is undefined. Please check.")
    elif not is_valid_email(email):
        st.error("Invalid Email: Please enter a valid email (e.g., example@domain.com).")
    elif not is_valid_phone(phone):
        st.error("Invalid Phone: Enter a valid phone number (10-15 digits, optionally starting with +).")
    else:
        try:
            phone_number_int = int(re.sub(r'\D', '', phone))

            payload = {
                "email": email,
                "phone": phone_number_int  
            }

            with st.spinner("Resolving contact..."):
                response = requests.post(API_URL, json=payload)

                if response.status_code == 200:
                    result = response.json()
                    st.success("✅ Contact Resolved Successfully!")

                    st.subheader("📌 Consolidated Contact Information")
                    
                    st.markdown("""
                    <style>
                        .info-table {
                            width: 100%;
                            border-collapse: collapse;
                        }
                        .info-table th {
                            background-color: #4CAF50 !important;  /* Green background */
                            color: white !important; /* White text for visibility */
                            padding: 10px;
                        }
                        .info-table td {
                            border: 1px solid #ddd;
                            padding: 10px;
                            text-align: left;
                        }
                    </style>
                    """, unsafe_allow_html=True)

                    contact_ids = ", ".join(map(str, result.get("contactIds", [])))
                    emails = ", ".join(result.get("emails", []))
                    phones = ", ".join(map(str, result.get("phones", [])))

                    st.markdown(f"""
                    <table class="info-table">
                        <tr><th>Contact IDs</th><td>{contact_ids}</td></tr>
                        <tr><th>Emails</th><td>{emails}</td></tr>
                        <tr><th>Phones</th><td>{phones}</td></tr>
                    </table>
                    """, unsafe_allow_html=True)    
        except Exception as e:
            st.error(f"⚠️ An unexpected error occurred: {str(e)}")

st.sidebar.title("About")
st.sidebar.info("This app helps consolidate customer data based on matching emails or phone numbers, resolving identities across multiple purchases.")
