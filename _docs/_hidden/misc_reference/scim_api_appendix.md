---
nav_title: "SCIM API objects and appendix"
article_title: SCIM API Objects and Appendix
page_order: 8
page_type: reference
description: "This article explains the different SCIM API objects and appendix."
hidden: true
permalink: "/scim_api_appendix/"
---

# SCIM API objects and appendix

## Permissions object

The permissions object is a field found in some of the requests and responses when interfacing with the user resource through SCIM ID permissions.

{% alert note %}
App groups have been renamed to workspaces in Braze, but the keys on this page still reference the old terminology (for example, `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

A valid permissions object is a JSON object with the following key-value pairs:

| Key | Required | Data type | Description |
| --- | --- | --- | --- |
| `companyPermissions` | Optional | Array | Array of company-level permission strings from the [Company permission strings](#company) table, in which the presence of the string corresponds to the user having the corresponding permission. |
| `roles` | Optional | Array | Array of [role objects](#role-object). |
| `appGroup` | Required | Array | Array of [workspace permission objects](#workspace-permission-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Workspace permissions object {#workspace-permission-object}

A valid app group permission object is a JSON object with the following key-value pairs:

| Key | Required | Data type | Description |
| --- | --- | --- | --- |
| `appGroupName`| Optional | String | Name of the workspace. Used to specify which workspace the permissions contained within this object are for. | 
| `appGroupId` | Required if `appGroupName` is missing | String | ID of the workspace, serving as an alternative method of specifying the workspace. |
| `appGroupPermissionSets` | Optional | Array | Array with a single [workspace permissions set object](#workspace-permissions-set-object). |
| `appGroupPermissions` | Required | Array | Array of workspace-level permission strings from the [workspace permission strings](#workspace-strings) table, in which the presence of the string corresponds to the user having the corresponding permission for the specified workspace. |
| `team` | Optional | Array | Array of [Team permission objects](#team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Workspace permissions set object {#workspace-permissions-set-object}

A valid workspace permissions set object is a JSON object with the following key-value pairs:

| Key | Required | Data type | Description |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Optional | String | Name of the workspace permission set that is being assigned to the user for this workspace. |
| `appGroupPermissionSetID` | Required if `appGroupPermissionSetName` is missing | String | ID of the workspace, serving as an alternative method of specifying the workspace permission set assigned to the user for this workspace. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Team permissions object

A valid team permission object is a JSON object with the following key-value pairs:

| Key | Required | Data type | Description |
| --- | --- | --- | --- |
| `teamName` | Optional | String | Name of the team, which can be used to specify which team the permissions within this object are for. |
| `teamId` | Required if `teamName` is missing | String | ID of the team, serving as an alternative method of specifying the team. |
| `teamPermissions` | Required | Array | Array of team-level permission strings from the [teams permission strings](#team) table, in which the presence of the string corresponds to the user having the corresponding permission for the specified team. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Role object

A valid role object is a JSON object with the following key value pairs:

| Key | Required | Data type | Description |
| --- | --- | --- | --- |
| `roleName` | Optional | String | Name of the role that is being assigned to the user. |
| `roleId` | Required if `roleName` is missing | String | ID of the role, serving as an alternative method of specifying the role. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Appendix

### Workspace permission strings {#workspace-strings}

| Permission name | SCIM API string |
| --- | --- |
| View Campaigns | `view_campaigns` |
| Edit Campaigns | `edit_campaigns` |
| Archive Campaigns | `archive_campaigns` |
| View Canvases | `view_canvases` |
| Edit Canvases | `edit_canvases` |
| Archive Canvases | `archive_canvases` |
| View Frequency Capping Rules | `view_frequency_caps` |
| Edit Frequency Capping Rules | `edit_frequency_caps` |
| View Message Prioritization | `view_message_prioritization` |
| Edit Message Prioritization | `edit_message_prioritization` |
| View Content Blocks | `view_content_blocks` |
| View Feature Flags | `view_feature_flags` |
| Edit Feature Flags | edit_feature_flags |
| Archive Feature Flags | archive_feature_flags |
| View Segments | view_segments |
| Edit Segments | edit_segments |
| Edit Global Control Group | edit_global_control_group |
| View IAM Templates | view_iam_templates |
| Edit IAM Templates | edit_iam_templates |
| Archive IAM Templates | archive_iam_templates |
| View Email Templates | view_email_templates |
| Edit Email Templates | edit_email_templates |
| Archive Email Templates | archive_email_templates |
| View Webhook Templates | view_webhook_templates |
| Edit Webhook Templates | edit_webhook_templates |
| Archive Webhook Templates | archive_webhook_templates |
| View Link Templates | view_link_templates |
| Edit Link Templates | edit_link_templates |
| View Media Library Assets | view_media_library_assets |
| View Locations | view_locations |
| Edit Locations | edit_locations |
| Archive Locations | archive_locations |
| View Promotion Codes | view_promotion_codes |
| Edit Promotion Codes | edit_promotion_codes |
| Export Promotion Codes | export_promotion_codes |
| View Preference Centers | view_preference_centers |
| Edit Preference Centers | edit_preference_centers |
| Edit Reports | edit_reports |
| View Banner Templates | view_banner_templates |
| View Multi Language Settings | view_multi_language_settings |
| Use Operator | use_operator |
| View Decisioning Studio Agents | view_decisioning_studio_agents |
| View Decisioning Studio Conversion Event | view_decisioning_studio_conversion_event |
| Launch Campaigns | `launch_campaigns` |
| Launch Canvases | `launch_canvases` |
| Edit Dashboard Users | `edit_dashboard_users` |
| Edit Media Library Assets | `edit_media_library_assets` |
| Delete Media Library Assets | `delete_media_library_asset` |
| View Import Users | `view_import_users` |
| Import Users	| `import_users` |
| Edit User Data | `edit_user_data` |
| View API Keys | `view_api_keys` |
| Edit API Keys | `edit_api_keys` |
| View Internal Groups | `view_internal_user_groups` |
| Edit Internal Groups | `edit_internal_user_groups` |
| View Message Activity Log | `view_message_activity_log` |
| View Event User Log | `view_event_user_log` |
| View API Identifiers | `view_api_identifiers` |
| View API Usage Dashboard | `view_api_usage_dashboard` |
| View API Limits | `view_api_limits` |
| View API Usage Alerts | `view_api_usage_alerts` |
| Edit API Usage Alerts | `edit_api_usage_alerts` |
| View SDK Debugger | `view_sdk_debugger` |
| Edit SDK Debugger | `edit_sdk_debugger` |
| Launch Content Blocks | `launch_content_blocks` |
| Edit Cloud Data Ingestion | `edit_cloud_data_ingestion` |
| Edit App Settings | `edit_app_settings` |
| View Push Settings | `view_push_settings` |
| Edit Push Settings | `edit_push_settings` |
| View Teams | `view_teams` |
| Edit Teams | `edit_teams` |
| Archive Teams | `archive_teams` |
| View Custom Attributes | `view_custom_attributes` |
| Edit Custom Attributes | `edit_custom_attributes` |
| Blocklist Custom Attributes | `blocklist_custom_attributes` |
| Delete Custom Attributes | `delete_custom_attributes` |
| Export Custom Attributes | `export_custom_attributes` |
| View Custom Events	 | `view_custom_events` |
| Edit Custom Events | `edit_custom_events` |
| Blocklist Custom Events | `blocklist_custom_events` |
| Delete Custom Events | `delete_custom_events` |
| Export Custom Events | `export_custom_events` |
| Edit Custom Event Property Segmentation | `edit_custom_event_property_segmentation` |
| View Products | `view_products` |
| Edit Products	 | `edit_products` |
| Blocklist Products | `blocklist_products` |
| Edit Purchase Property Segmentation | `edit_purchase_property_segmentation` |
| View Tags | `view_tags` |
| Edit Tags | `edit_tags` |
| Delete Tags | `delete_tags` |
| View Email Settings	| `view_email_settings` |
| Edit Email Settings | `edit_email_settings` |
| View Catalogs | `view_catalogs` |
| Edit Catalogs	 | `edit_catalogs` |
| Export Catalogs | `export_catalogs` |
| Delete Catalogs | `delete_catalogs` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Team permission strings {#team}

| Permission name | SCIM API string |
| --- | --- |
| View Campaigns | `view_campaigns` |
| Edit Campaigns | `edit_campaigns` |
| Archive Campaigns | `archive_campaigns` |
| View Canvases | `view_canvases` |
| Edit Canvases | `edit_canvases` |
| Archive Canvases | `archive_canvases` |
| View Frequency Capping Rules | `view_frequency_caps` |
| Edit Frequency Capping Rules | `edit_frequency_caps` |
| View Message Prioritization | `view_message_prioritization` |
| Edit Message Prioritization | `edit_message_prioritization` |
| View Content Blocks | `view_content_blocks` |
| View Feature Flags | `view_feature_flags` |
| Edit Feature Flags | `edit_feature_flags` |
| Archive Feature Flags | archive_feature_flags |
| View Segments | view_segments |
| Edit Segments | edit_segments |
| Edit Global Control Group | edit_global_control_group |
| View IAM Templates | view_iam_templates |
| Edit IAM Templates | edit_iam_templates |
| Archive IAM Templates | archive_iam_templates |
| View Email Templates | view_email_templates |
| Edit Email Templates | edit_email_templates |
| Archive Email Templates | archive_email_templates |
| View Webhook Templates | view_webhook_templates |
| Edit Webhook Templates | edit_webhook_templates |
| Archive Webhook Templates | archive_webhook_templates |
| View Link Templates | view_link_templates |
| Edit Link Templates | edit_link_templates |
| View Media Library Assets | view_media_library_assets |
| View Locations | view_locations |
| Edit Locations | edit_locations |
| Archive Locations | archive_locations |
| View Promotion Codes | view_promotion_codes |
| Edit Promotion Codes | edit_promotion_codes |
| Export Promotion Codes | export_promotion_codes |
| View Preference Centers | view_preference_centers |
| Edit Preference Centers | edit_preference_centers |
| View Reports | view_reports |
| Create Reports | create_reports |
| Edit Reports | edit_reports |
| View Banner Templates | view_banner_templates |
| View Multi Language Settings | view_multi_language_settings |
| Use Operator | use_operator |
| View Decisioning Studio Agents | view_decisioning_studio_agents |
| View Decisioning Studio Conversion Event | view_decisioning_studio_conversion_event |
| Launch Campaigns | `launch_campaigns` |
| Launch Canvases | `launch_canvases` |
| Edit Dashboard Users | `edit_dashboard_users` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }