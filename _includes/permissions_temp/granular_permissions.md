## Creating a permission set

Use permission sets to bundle permissions related to specific subject areas or actions. They can be applied to dashboard users who need the same access across different workspaces. To create a permission set, go to **Settings** > **Permission Settings**, then select **Create permission set**. For a description of each permission, see [List of permissions](#list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Name|Permissions|
|-----------|----------------|
|Developers|"View API Keys", "Edit API Keys", "View Internal Groups", "Edit Internal Groups", "View Message Activity Log", "View Event User Log", "View API identifiers", "View API Usage Dashboard", "View API Limits", "View API Usage Alerts", "Edit API Usage Alerts", "View SDK Debugger", "Edit SDK Debugger".|
|Marketers|"View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Frequency Capping Rules", "Edit Frequency Capping Rules", "View Message Prioritization", "Edit Message Prioritization", "View Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "Edit Global Control Group", "View IAM Templates", "Edit IAM Templates", "Archive IAM Templates", "View Email Templates", "Edit Email Templates", "Archive Email Templates", "View Webhook Templates", "Edit Webhook Templates", "Archive Webhook Templates", "View Link Templates", "Edit Link Templates", "View Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers", "Edit Reports", "View Banner Templates", "View Multi Language Settings", "Use Operator", "View Decisioning Studio Agents", "View Decisioning Studio Conversion Event".|
|User Management|"View Dashboard Users", "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams".|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Creating a role

Roles allow for more structure by bundling together your individual custom permissions with workspace access controls. This is especially useful if you have many brands or regional workspaces in one dashboard. With roles, you can add dashboard users to the right workspaces and directly grant them the associated permissions. For a description of each permission, see [List of permissions](#list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Role Name    | Workspace | Permissions  
----------- | ----------- | ---------
| Marketer - Fashion Brands | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| Marketer - Skincare Brands | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} |"View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers".|
| User Management - All Brands | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "View Dashboard Users", "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams"|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## How do permission sets and roles differ from Teams?

{% multi_lang_include permissions.md content="Differences" %}

### Considerations for adding user permissions to Teams

You may encounter difficulties when trying to save permissions in the Braze dashboard, particularly when adding or removing users from a workspace, or adding them to a Team. The **Save/Update Users** button may become greyed out if the permissions for the user are identical to those they already have at the workspace level. This restriction exists because there is no benefit to having a Team if all users possess the same permissions as the entire workspace.

To successfully add a user to a Team while maintaining the same permissions, don't assign any permissions at the workspace level. Instead, assign permissions exclusively at the team level.

## Limited users

Limited users have specific permissions that allow them to manage certain aspects of the Braze dashboard while having restrictions compared to company admins and workspace admins.

| Permissions | Limited users can edit the permissions of other limited users if they have the "View Dashboard Users" and "Edit Dashboard Users" permissions. They can also create new limited users and modify their permission sets. However, they can't create or manage company admin accounts. |
| Role limitations | If a limited user has all permissions except "Workspace Admin", they will still have access to all other permissions typically granted to an workspace admin. |
| Visibility of permissions | If a limited user has "View Dashboard Users" and "Edit Dashboard Users" permissions for one workspace (such as Dev) but not for another (such as Prod), they won't see the Prod workspace permissions in their dashboard users detail page. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparing limited users

| Limited user type | Description |
| --- | --- |
| Workspace Admin | Workspace Admins have permissions specific to managing Workspaces but do not have the same authority as Company Admins. Limited Users can inherit permissions similar to those of Workspace Admins if they have the necessary permissions checked. |
| Admin (Company Admin) | Company Admins have broader permissions, including the ability to delete dashboard users. However, they cannot delete their own accounts and must contact another Company Admin for that action. |
| View-only access | To access parts of the dashboard, such as the Campaigns page, users must have view permissions assigned to them.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Limited access error

Users may encounter messages like "You need “View Landing Pages” permissions to access this page”. In such cases, the user and account admin should verify that the required permissions are granted. If they are, try resolving the issue by disabling and then re-enabling the user’s permissions. 

{% alert note %}
It isn't possible to merge or import user permissions from one dashboard user to another.
{% endalert %}

## Editing a user's permissions

To edit a user's current admin, company, or workspace permissions, go to **Settings** > **Company Users**, then select their name.

![The "Company Users" page in Braze with one user listed in the results.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %}){: style="max-width:80%;"}

{% tabs local %}
{% tab Admin %}

### Admin

Admins have access to all features and the ability to modify any company setting. They can:

- Change [approval settings]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/#turning-on-campaign-approval)
- Add, edit, delete, suspend, or unsuspend other [Braze users]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users)
- Export Braze users as a CSV

To grant or remove admin privileges, select **This user is an admin**, then select **Update user**.

![The details of the selected user with the admin checkbox in focus.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:40%;"}

{% alert warning %}
If you remove admin privileges from a user, they won't be able to access Braze until you assign them at least one [company-level](#company) or [workspace-level](#workspace) permission.
{% endalert %}

{% endtab %}
{% tab Company %}

### Company

To manage the following company-level permissions for a user, check or uncheck the box next to that permission. When you're finished, select **Update user**.

|Permission name|Description|
|----------|-----------|
|Manage company settings|Allows users to modify permission settings and sender verification. .|
|Create and delete workspaces|Allows users to create and delete workspaces.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Workspace

You can give a user different permissions for each workspace they belong to in Braze. To manage their workspace-level permissions, select **Select workspaces and permissions**, then choose their permissions manually or assign a [permission set or role](#creating-a-permission-set) you previously created. If you need to give a user different permissions for different workspaces, repeat this process as many times as needed. For a description of each permission, see [List of permissions](#list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

Under **Workspaces**, choose one or more workspaces from the dropdown. Then, under **Permissions**, choose one or more permissions from the dropdown. They will be assigned these permissions only for the workspaces you have selected. Optionally, you can select **Enable Admin Access** if you'd like to give them full permissions for this workspace instead.

When you're finished, select **Update user**.

![Workspace-level permissions being manually selected in Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

Under **Workspaces**, choose one or more workspaces from the dropdown. Then, under **Permission Sets**, choose one permission set. They will be assigned these permissions only for the workspaces you have selected.

When you're finished, select **Update user**.

![Workspace-level permissions being assigned through a permission set in Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Assign role %}

Under **Workspaces**, choose one or more workspaces from the dropdown. Then, under **Role**, choose one role. They will be assigned these permissions only for the workspaces you have selected.

When you're finished, select **Update user**.

![Workspace-level permissions being assigned through a role in Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exporting user permissions

To download a list of your users and their permissions, go to **Settings** > **Company Users**, then select **Export Users**. A CSV file will be sent to your email address shortly.

![The "Company Users" page in Braze with the "Export Users" option in focus.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## List of permissions

| Permission | Definition |
|-------------------------------------------------|---------------------|
| View Billing Details                            | View billing details |
| View Custom Attributes Marked as PII            | View custom attributes marked as PII |
| View PII                                        | View PII |
| View User Profiles PII Compliant                | Access user search and view user profiles with redacted PII |
| View Usage Data                                 | View usage data |
| Merge Duplicate Users                           | Combine duplicate users into one user. Duplicates are removed after merging. |
| Preview Duplicate Users                         | Preview which user profiles are duplicates |
| View Canvas Templates                           | View Canvas templates |
| Archive Canvas Templates                        | Move Canvas templates to archive |
| Launch Content Blocks                           | Launch Content Blocks |
| Launch Preference Centers                       | Launch preference centers |
| Export User Data                                | Download users from the dashboard |
| Edit Currents Integrations                      | Create, update, and delete Currents integrations |
| View Currents Integration                       | View Currents integrations |
| View Campaigns                                  | View campaigns |
| Edit Campaigns                                  | Create and update campaigns |
| Archive Campaigns                               | Move campaigns to archive |
| Send Campaigns                                  | Start, stop, pause, or resume campaigns | 
| Send Canvases                         		  | Start, stop, pause, or resume Canvases |
| View Frequency Capping Rules                    | View Frequency Capping Rules |
| Edit Frequency Capping Rules                    | Create and update Frequency Capping Rules |
| View Canvases                                   | View Canvases |
| Edit Canvases                                   | Create and update Canvases |
| Archive Canvases                                | Move Canvases to archive |
| View Content Blocks                             | View Content Blocks |
| Edit Content Blocks                             | Create and update Content Blocks |
| Archive Content Blocks                          | Move Content Blocks to archive |
| View Feature Flags                              | View feature flags |
| Edit Feature Flags                              | Create and update feature flags |
| Archive Feature Flags                           | Move feature flags to archive |
|  View WhatsApp Message Templates                | Allows users to view [WhatsApp message templates]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/?tab=template%20messages#step-2-compose-your-whatsapp-message). |
| Edit WhatsApp Message Templates | Allows users to create WhatsApp message templates in the template builder. This feature is currently in early access. |
| View Segments                                   | View segments . Users must have the “View Segments” permission to have the “Edit Segments” or “Archive Segments” permission. |
| Archive Segments                                | Archive and un-archive segments. Users with the “Archive Segments” permission must also be granted the “View Segments” permission. |
| Edit Segments                                   | Create and update Segments. Users with the “Edit Segments” permission must also be granted the “View Segments permission”. |
| View Global Control Group                       | View Global Control Group setup page |
| Edit Global Control Group                       | Create and save changes to the Global Control Group. Users with the “Edit Global Control Group” permission must also be granted permissions for “Edit Campaigns” and “Edit Canvases”. Users with the “Edit Global Control Group” permission are also granted the “View Global Control Group” permission. |
| View Banner Templates                           | View banner templates |
| Edit Banner Templates                           | Create and update banner templates |
| Archive Banner Templates                   	  | Move banner templates to archive |
| View Email Templates                            | View email templates |
| Edit Email Templates                            | Create and update email templates |
| Archive Email Templates                         | Move email templates to archive |
| View Link Templates   	                      | View link templates |
| Edit Link Templates	                          | Create and update link templates |
| Publish Landing Pages                           | Make a draft landing page active |
| Edit Landing Page Drafts                        | Create and save landing page drafts |
| View Landing Pages			                  | View landing pages |
| Edit Landing Page Templates	                  |  Create and update landing page templates |
| View Landing Page Templates	                  | View landing page templates |
| Archive Landing Page Template 	              | Move landing page templates to archive |
| View Media Library Assets                       | View media library assets |
| Edit Media Library Assets                       | Create and update media library assets |
| Delete Media Library Assets                     | Permanently delete media library assets |
| View Locations                                  | View locations |
| Edit Locations                                  | Create and edit locations |
| Archive Locations                               | Move locations to archive |
| View Promotion Codes                            | View promo codes |
| Edit Promotion Codes                            | Create and update promo codes |
| Export Promotion Codes                          | Download a list of promo codes from the dashboard |
| View Preference Centers                         | View preference centers  |
| Edit Preference Centers                         | Create and update preference centers |
| Launch Preference Centers	                      | Make a draft Preference Center active or update an existing one |
| View API Keys                                   | View API keys |
| Edit API Keys                                   | Create and update API keys |
| View Internal Groups                            | View internal groups |
| Edit Internal Groups                            | Create and update internal groups |
| View Message Activity Log                       | View message activity logs |
| View Event User Log                             | View event user logs |
| View API identifiers                            | View API identifiers and other identifiers |
| View API Usage Dashboard                        | View the API usage dashboard |
| View API Limits                                 | View API rate limits |
| View API Usage Alerts                           | View API usage alerts |
| Edit API Usage Alerts                           | Create and update API usage alerts |
| Edit SDK Debugger                               | Create and download SDK Debugger sessions |
| View SDK Debugger                               | View SDK Debugger  or debugging sessions |
| View App Settings                               | View App Settings page |
| Edit App Settings                               | Create, edit, and update apps within app settings |
| View Catalogs                                   | View catalogs and selections |
| Edit Catalogs                                   | Create and update catalogs and selections |
| Export Catalogs                                 | Download catalogs from the dashboard |
| Delete Catalogs                                 | Permanently delete catalogs |
| View Dashboard Users                            | View Company Users |
| Edit Dashboard Users                            | Create and update company users 
| View Email Settings                             | View Email Preferences |
| Edit Email Settings                             | Enable and update Email Preferences | 
Edit Identifier Field-Level Encryption            | Enable and update Field-Level Encryption settings |
| View Custom Attributes                          | View custom attributes and usage report |
| Edit Custom Attributes                          | Create and update custom attributes |
| Blocklist Custom Attributes                     | Add custom attributes to a blocklist that restricts use in the dashboard |
| Delete Custom Attributes                        | Permanently delete custom attributes |
| Export Custom Attributes                        | Download custom attributes from the dashboard |
| View Custom Events                              | View custom events and usage report, and add custom events to the daily analytics report email |
| Edit Custom Events                              | Create and update custom events |
| Blocklist Custom Events                         | Add custom events to a blocklist that restricts use in the dashboard |
| Delete Custom Events                            | Permanently delete custom events |
| Export Custom Events                            | Download custom events from the dashboard |
| Edit Custom Event Property Segmentation         | Enable and disable segmentation for custom event properties |
| View Products                                   | View products |
| Edit Products                                   | Create and update products |
| Blocklist Products                              | Add products to a blocklist that restricts use in the dashboard |
| Edit Purchase Property Segmentation             | Enable and disable segmentation for purchase event properties |
| Edit Technology Partners                        | Create and update technology partners |
| Edit Cloud Data Ingestion                       | Create, update, and delete sources and syncs |
| View Multi Language Settings                    | View multi-language settings |
| Create Multi Language Locale Settings           | Create and update multi-language locale settings |
| Delete Multi Language Locale Settings           | Permanently delete multi-language locale settings |
| Edit Subscriptions                              | Create and update subscription groups |
| View Tags                                       | View tags |
| Edit Tags                                       | Create and update tags |
| Delete Tags                                     | Permanently delete tags |
| View Teams                                      | View Teams |
| Edit Teams                                      | Create and update teams |
| Archive Teams                                   | Move teams to archive |
| View Data Transformation                        | View data transformations |
| Edit Data Transformation                        | Create and update data transformations |
| Launch Campaigns                                | Start, stop, pause, or resume existing campaigns |
| Launch Canvases                                 | Start, stop, pause, or resume existing Canvases |
| Edit Canvas Templates                           | Create and update Canvas templates |
| Approve Campaigns                               | Approve or deny campaigns. The [approval workflow for campaigns]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) must be turned on for this permission to apply. This setting is currently in early access. Contact your account manager if you’re interested in participating in the early access. |
| Approve Canvases                                | Approve or deny Canvases. The [approval workflow for Canvases]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) must be turned on for this permission to apply. This setting is currently in early access. Contact your account manager if you’re interested in participating in the early access. |
| View Placements                                 | View Banner placement |
| Edit Placements                                 | View Banner placements without making changes |
| Archive Placements                              | Move Banner placements to archive |
| View Push Settings                              | View Push settings |
| Edit Push Settings                              | Create and update Push settings |
| Edit Reports                                    | Create and update reports |
| View Import Users                               | View CSV user imports |
| Import Users                                    | Upload users to the dashboard |
| Edit User Data                                  | Create and update user data |
| View Merge Users                                | View a list of user merge records |
| View User Deletion Records	            	  | View user deletion records |
| Delete Users From Dashboard	                  | Permanently delete users from the dashboard individually or in bulk. |      
| View Custom AI Agents                           | Allows users to view custom AI agents. This feature is currently in beta. Contact your account manager if you’re interested in participating in the beta. |
| Create Custom AI Agents                         | Allows users to create custom AI agents. This feature is currently in beta. Contact your account manager if you’re interested in participating in the beta. |
| Edit Custom AI Agents                           | Allows users to edit custom AI agents. This feature is currently in beta. Contact your account manager if you’re interested in participating in the beta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }