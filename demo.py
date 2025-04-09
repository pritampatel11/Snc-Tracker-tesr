import streamlit as st
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
import io

# SharePoint site and folder details
site_url = "https://oldendorff.sharepoint.com/sites/PerformanceDesk"
relative_folder_url = "/sites/PerformanceDesk/Shared Documents/Performance Evaluations/1SNC"

# Input credentials securely (for demonstration use)
username = st.secrets["sharepoint"]["username"]
password = st.secrets["sharepoint"]["password"]

st.title("Upload File to SharePoint - 1SNC Folder")

uploaded_file = st.file_uploader("Choose a file to upload", type=["xlsx", "csv", "pdf", "docx"])

if uploaded_file is not None:
    file_name = uploaded_file.name
    file_content = uploaded_file.read()

    # Authenticate and upload
    ctx_auth = AuthenticationContext(site_url)
    if ctx_auth.acquire_token_for_user(username, password):
        ctx = ClientContext(site_url, ctx_auth)
        target_folder = ctx.web.get_folder_by_server_relative_url(relative_folder_url)

        st.info("Uploading file... Please wait.")
        target_folder.upload_file(file_name, io.BytesIO(file_content)).execute_query()
        st.success(f"File '{file_name}' uploaded successfully to SharePoint!")
    else:
        st.error("Authentication failed. Please check credentials.")
