variable "resource_group_name" {
  description = "Name of the sandbox Resource Group."
  type        = string
  default     = "rg-cloud-devops-sprint-sandbox"
}

variable "location" {
  description = "Azure region for sandbox resources."
  type        = string
  default     = "swedencentral"
}

variable "tags" {
  description = "Additional tags for sandbox resources."
  type        = map(string)
  default     = {}
}
