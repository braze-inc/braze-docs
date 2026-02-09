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

### Company permission strings {#company}

| As displayed in UI | SCIM API string |
| --- | --- |
| Administrator | `admin` |
| Can Manage Company Settings | `manage_company_settings` |
| Can Add/Remove Workspaces| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Workspace permission strings {#workspace-strings}

| Permission name | SCIM API string |
| --- | --- |
| Admin | `admin` |
| Access Campaigns, Canvases, Cards, Segments, Media Library | `basic_access` |
| Approve and Deny Canvases | `approve_deny_campaigns` |
| Send Campaigns, Canvases | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit Segments | `edit_segments` |
| Export User Data | `export_user_data` |
| View PII | `view_pii` |
| View User Profiles PII Compliant | `view_user_profile` |
| Manage Dashboard Users | `manage_dashboard_users` |
| Manage Media Library Assets | `manage_media_library` |
| View Usage Data | `view_usage_data` |
| Import and Update User Data | `import_update_user_data` |
| View Billing Details | `view_billing_details` |
| Access Dev Console | `dev_console` |
| Launch Content Blocks | `launch_content_blocks` |
| Manage External Integrations | `manage_external_integrations` |
| Manage Apps | `manage_apps` |
| Manage Teams | `manage_teams` |
| Manage Events, Attributes, Purchases | `manage_events_attributes_purchases` |
| Manage Tags | `manage_tags` |
| Manage Email Settings | `manage_email_settings` |
| Manage Subscription Groups | `manage_subscription_groups` |
| Manage Approval Settings | `manage_approval_settings` |
| Manage Catalogs Dashboard Permission | `manage_catalogs_dashboard_permission` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Team permission strings {#team}

| Permission name | SCIM API string |
| --- | --- |
| Admin | `admin` |
| Access Campaigns, Canvases, Cards, Segments, Media Library | `basic_access` |
| Approve and Deny Canvases | `approve_deny_campaigns` |
| Send Campaigns, Canvases | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit Segments | `edit_segments` |
| Export User Data | `export_user_data` |
| View User Profile | `view_user_profile` |
| Manage Dashboard Users | `manage_dashboard_users` |
| Manage Media Library Assets | `manage_media_library` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Department strings

| As displayed in UI | SCIM API string |
| --- | --- |
| Agency / Third Party | `agency` |
| BI / Analytics | `bi` |
| C-Suite | `c_suite` |
| Engineering | `engineering` |
| Finance | `finance` |
| Marketing / Editorial | `marketing` |
| Product Management | `pm` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
