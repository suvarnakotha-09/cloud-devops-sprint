output "resource_group_id" {
  description = "ID of the sandbox Resource Group."
  value       = module.resource_group.id
}

output "resource_group_name" {
  description = "Name of the sandbox Resource Group."
  value       = module.resource_group.name
}
