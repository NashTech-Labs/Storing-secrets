import os
import subprocess
import base64
 

# Azure Resource Group and Key Vault Configuration
resource_group_name = "your-resource-group-name"  # Replace with your desired resource group name
key_vault_name = "Desire-key-vault-name"  # Replace with your desired Key Vault name
secrets_file_path = "./file.txt"

 

# Replace underscores with hyphens in the Key Vault and Resource Group names
key_vault_name = key_vault_name.replace("_", "-")
resource_group_name = resource_group_name.replace("_", "-")

 

# Read secrets from the file
secrets = {}
with open(secrets_file_path, "r") as file:
    for line in file:
        key, value = line.strip().split(" = ")
        secrets[key] = value

 

# Authenticate to Azure
try:
    # Use Azure CLI to get the access token
    access_token = subprocess.check_output(["az", "account", "get-access-token", "--query", "accessToken", "-o", "tsv"]).decode("utf-8").strip()
except subprocess.CalledProcessError:
    print("Error: Failed to obtain Azure access token. Make sure you are logged into Azure CLI.")
    exit(1)

 

# Create Azure Resource Group if it doesn't exist
try:
    subprocess.check_call(["az", "group", "create", "--name", resource_group_name, "--location", "location-name"])
    print(f"Azure Resource Group '{resource_group_name}' created successfully.")
except subprocess.CalledProcessError:
    print(f"Azure Resource Group '{resource_group_name}' already exists or encountered an error during creation.")

 

# Create Azure Key Vault in the specified Resource Group
try:
    subprocess.check_call(["az", "keyvault", "create", "--name", key_vault_name, "--resource-group", resource_group_name, "--location", "location-name"])
    print(f"Azure Key Vault '{key_vault_name}' created successfully in Resource Group '{resource_group_name}'.")
except subprocess.CalledProcessError:
    print(f"Azure Key Vault '{key_vault_name}' already exists or encountered an error during creation in Resource Group '{resource_group_name}'.")

 

# Store secrets in Azure Key Vault
for key, value in secrets.items():
    # Replace underscores with hyphens in the secret name
    key = key.replace("_", "-")
    encoded_value = base64.b64encode(value.encode("utf-8")).decode("utf-8")   
    command = f"az keyvault secret set --vault-name {key_vault_name} --name {key} --value {encoded_value} --output none --query 'value'"

 

    try:
        # Use Azure CLI to set the secret in the Key Vault
        subprocess.check_call(["bash", "-c", f'AZURE_ACCESS_TOKEN="{access_token}" {command}'])
        print(f"Secret '{key}' stored in Azure Key Vault '{key_vault_name}' successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to store secret '{key}' in Azure Key Vault '{key_vault_name}'.")
        print(e)

 

print("All secrets have been stored in Azure Key Vault.")
