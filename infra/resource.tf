resource "azurerm_resource_group" "rg" {
  name     = "myResourceGroup"
  location = "West Europe"
}

resource "azurerm_app_service_plan" "asp" {
  name                = "myAppServicePlan"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  sku {
    tier = "Basic"
    size = "B1"
  }
}

resource "azurerm_app_service" "app" {
  name                = "myFastAPIApp"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_app_service_plan.asp.id

  app_settings = {
    "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = "false"
    // Referenz auf Key Vault Geheimnisse hier, wenn notwendig
  }

  identity {
    type = "SystemAssigned"
  }
}

resource "azurerm_key_vault" "kv" {
  name                = "myKeyVault"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  tenant_id           = "b7d7e9a7-eb2c-4de0-a460-f7cf1d5c2b12"
  sku_name            = "standard"
  
  purge_protection_enabled = false
}

resource "azurerm_key_vault_access_policy" "app" {
  key_vault_id = azurerm_key_vault.kv.id
  tenant_id    = "b7d7e9a7-eb2c-4de0-a460-f7cf1d5c2b12"
  object_id    = "de1399f2-1bf1-42a7-b240-f0001c0c1715"

  secret_permissions = [
    "get",
    "list"
  ]
}
resource "azurerm_key_vault_secret" "example" {
  name         = "secretName"
  value        = "secretValue"
  key_vault_id = azurerm_key_vault.kv.id
}

// Update app_settings der Web App, um das Geheimnis aus Key Vault zu verwenden
resource "azurerm_app_service" "app_with_secret" {
  name                = azurerm_app_service.app.name
  location            = azurerm_app_service.app.location
  resource_group_name = azurerm_app_service.app.resource_group_name
  app_service_plan_id = azurerm_app_service.app.app_service_plan_id

  app_settings = {
    "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = "false"
    "SECRET_NAME"                         = "@Microsoft.KeyVault(SecretUri=${azurerm_key_vault_secret.example.secret_uri_with_version})"
  }

  identity {
    type = "SystemAssigned"
  }

  depends_on = [
    azurerm_key_vault_access_policy.app
  ]
}
