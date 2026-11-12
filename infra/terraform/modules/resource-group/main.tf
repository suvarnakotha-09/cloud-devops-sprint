variable "name" {
  description = "Name of the Azure Resource Group."
  type        = string
}

variable "location" {
  description = "Azure region for the Resource Group."
  type        = string
}

variable "tags" {
  description = "Tags applied to the Resource Group."
  type        = map(string)
  default     = {}
}

resource "azurerm_resource_group" "this" {
  name     = var.name
  location = var.location
  tags     = var.tags
}

output "id" {
  description = "Resource Group ID."
  value       = azurerm_resource_group.this.id
}

output "name" {
  description = "Resource Group name."
  value       = azurerm_resource_group.this.name
}
