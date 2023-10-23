# Import Secrets into Azure Key Vault
This Python script allows you to import secrets from a file into an Azure Key Vault. It's a convenient way to manage sensitive information securely. Below are the steps to use this script:

## Prerequisites
Python 3.x
Azure CLI installed and configured
You have logged in using the Azure CLI (`az login`)
Azure Resource Group has been created

## Instructions
1. Clone the Repository
   git clone <repository_url>
   cd <repository_directory>
2. Configure the Script
   1. Open the Python script in a code editor.
   2. Modify the following variables:
     - resource_group_name: Set it to your desired Azure Resource Group name.
     - key_vault_name: Set it to your desired Azure Key Vault name.
     - secrets_file_path: Set the path to the file containing secrets. The file should have secrets in the format "SECRET_NAME = SECRET_VALUE".
3. Run the Script
   Execute the script using the following command:
         - python script_name.py
   Replace script_name.py with the name of the Python script you want to run.
