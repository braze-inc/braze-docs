---
nav_title: "SCIM API Objects and Appendix"
article_title: SCIM API Objects and Appendix
page_order: 8
page_type: reference
description: "This article explains the different SCIM API objects and appendix."
hidden: true
permalink: "/scim_api_appendix/"
---

# SCIM API objects and appendix

## Permissions object

The permissions object is a field found in some of the requests and responses when interfacing with the user resource through SCIM id permissions.

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

A valid permissions object is a JSON object with the following key-value pairs:

| Key | Required | Data type | Desciption |
| --- | --- | --- | --- |
| `companyPermissions` | Required | Array | Array of company-level permission strings from the [Company permission strings](#company) table, in which the presence of the string corresponds to the user having the corresponding permission. |
| `appGroup` | Required | Array | Array of [App group permission objects](#app-group-permssions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### App group permssions object

A valid app group permission object is a JSON object with the following key-value pairs:

| Key | Required | Data type | Description |
| --- | --- | --- | --- |
| `appGroupName`| Optional | String | Name of the workspace. Used to specify which workspace the permissions contained within this object are for. | 
| `appGroupId` | Required if `appGroupName` is missing | String | ID of the workspace, serving as an alternative method of specifying the workspace. |
| `appGroupPermissions` | Required | Array | Array of workspace-level permission strings from the [App group permission strings](#app-group) table, in which the presence of the string corresponds to the user having the corresponding permission for the specified workspace. |
| `team` | Optional | Array | Array of [Team permission objects](#team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Team permissions object

A valid team permission object is a JSON object with the following key-value pairs:

| Key | Required | Data type | Description |
| --- | --- | --- | --- |
| `teamName` | Optional | String | Name of the team. Used to specify which team the permissions contained within this object are for. |
| `teamId` | Required if `teamName` is missing | String | ID of the team, serving as an alternative method of specifying the team. |
| `teamPermissions` | Required | Array | Array of team-level permission strings from the [team permission strings](#team) table, in which the presence of the string corresponds to the user having the corresponding permission for the specified team. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Appendix

### Company permission strings

| As displayed in UI | SCIM API string |
| --- | --- |
| Administrator | `admin` |
| Can Manage Company Settings | `manage_company_settings` |
| Can Add/Remove Workspaces| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2}

### App group permission strings

| Permission name | SCIM API string |
| --- | --- |
| Admin | `admin` |
| Access Campaigns, Canvases, Cards, Segments, Media Library | `basic_access` |
| Send Campaigns, Canvases | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit Segments | `edit_segments` |
| Export User Data | `export_user_data` |
| View PII | `view_pii` |
| View User Profiles PII Compliant | `view_user_profile` |
| Manage Dashboard Users | `manage_dashboard_users` |
| Manage Media Library | `manage_media_library` |
| View Usage Data | `view_usage_data` |
| Import and Update User Data | `import_update_user_data` |
| View Billing Details | `view_billing_details` |
| Access Dev Console | `dev_console` |
| Manage External Integrations | `manage_external_integrations` |
| Manage Apps | `manage_apps` |
| Manage Teams | `manage_teams` |
| Manage Events, Attributes, Purchases | `manage_events_attributes_purchases` |
| Manage Tags | `manage_tags` |
| Manage Email Settings | `manage_email_settings` |
| Manage Subscription Groups | `manage_subscription_groups` |
| Manage Approval Settings | `manage_approval_settings` |
{: .reset-td-br-1 .reset-td-br-2}

### Teams permission strings

| Permission name | SCIM API string |
| --- | --- |
| Admin | `admin` |
| Access Campaigns, Canvases, Cards, Segments, Media Library | `basic_access` |
| Send Campaigns, Canvases | `send_campaigns_canvases` |
| Publish Cards | `publish_cards` |
| Edit Segments | `edit_segments` |
| Export User Data | `export_user_data` |
| View User Profile | `view_user_profile` |
| Manage Dashboard Users | `manage_dashboard_users` |
| Manage Media Library | `manage_media_library` |
{: .reset-td-br-1 .reset-td-br-2}

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
{: .reset-td-br-1 .reset-td-br-2}
