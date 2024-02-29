# Azure Infrastructure Deployment Guide

This guide outlines the steps to deploy a basic web application infrastructure on Azure using Terraform, including the creation of a Service Principal for secure access to Azure Key Vault.

## Prerequisites

- An Azure subscription
- Azure CLI installed
- Terraform installed

## Step 1: Set Up Azure Authentication

Before deploying your infrastructure with Terraform, authenticate with Azure to ensure you have the necessary permissions.

```bash
az login
```

## Step 2: Create a Service Principal

Create a Service Principal that Terraform will use to manage resources in your Azure subscription securely.

```bash
az ad sp create-for-rbac --name "<YourAppName>-sp" --skip-assignment
```

Note the output from this command, as it contains important information (`appId`, `password`, `tenant`) that you'll need in the next steps.

## Step 3: Configure Terraform Provider

Create a file named `main.tf` with the following content to configure the Azure provider. Replace `<appId>`, `<password>`, and `<tenant>` with the values obtained from the previous step.

```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
  client_id       = "<appId>"
  client_secret   = "<password>"
  subscription_id = "<YourSubscriptionId>"
  tenant_id       = "<tenant>"
}
```

## Step 4: Define Your Infrastructure

Create a file named `resources.tf` and define your infrastructure as code. Refer to the Terraform configuration provided in the earlier conversation for specific resource definitions, including the Azure Resource Group, App Service, App Service Plan, and Key Vault.

## Step 5: Initialize Terraform

Run the following command in your project directory to initialize Terraform.

```bash
terraform init
```

## Step 6: Plan and Apply the Configuration

Plan your deployment to review the changes Terraform will make to your infrastructure.

```bash
terraform plan
```

If everything looks correct, apply the configuration to create your resources on Azure.

```bash
terraform apply
```

## Step 7: Configure Key Vault Access

Grant the created Service Principal access to the Key Vault using the Azure CLI.

```bash
az keyvault set-policy --name "<YourKeyVaultName>" --spn "<appId>" --secret-permissions get list set delete
```

## Conclusion

You've now deployed a basic web application infrastructure on Azure using Terraform and configured a Service Principal for secure access to Azure services. Ensure to replace placeholder values with actual data relevant to your Azure subscription and infrastructure requirements.
