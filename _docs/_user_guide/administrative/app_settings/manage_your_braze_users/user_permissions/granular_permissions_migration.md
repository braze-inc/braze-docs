---
nav_title: Granular permissions migration
article_title: Migrating to granular permissions
page_order: 3
page_type: reference
alias: /granular_permissions_migration/
description: "This reference article covers how to prepare for the migration to granular user permissions in Braze."
tool: Dashboard
---

# Migrating to granular permissions

> Managing who can access your account and perform specific actions is critical for both security and operational efficiency. To give you more control, Braze is introducing granular permissions, a more flexible and precise way to manage user access across your account.

The migration includes these benefits:

- **More precise control:** Granular permissions offer more control, better security, and clearer oversight. Users get only the access they need.
- **Automatic mapping:** All current permissions are mapped automatically to their [granular equivalents](#legacy-to-granular-permissions-mapping). Your users keep the same access level unless you change it.

## What to review

When migration is planned for your company, your Braze admins will receive emails and in-dashboard banners notifying them of the granular permission migration. To prepare for the migration, we recommend that a Braze admin do the following.

1. Identify users, roles, or permission sets that may need to be updated for more tailored access after you migrate to the new permission framework. 
2. If your company has automated user provisioning using SCIM or compliance tools that rely on permission strings, update them to match the new granular structure. 
3. Inform your Braze users of any upcoming changes to prevent confusion.
4. At the scheduled migration date and time, your company will automatically migrate to granular permissions. No further action is required from company admins.

{% alert important %}
The ability to update permissions will lock within 15 minutes of the scheduled migration time. This means you can’t change any permissions until the migration is over, which we anticipate taking up to 15 minutes.
{% endalert %}

## Legacy to granular permissions mapping

| | Legacy permissions | Granular permissions |
|---------------|---------------|---------------|
| **Level** | **Name** | **Name** |
| Admin | Admin | Admin |
| Workspace | Workspace Admin | Workspace Admin |
| Company | Create and delete workspaces | Create and delete workspaces |
| Company | Manage company settings | Manage company settings |
| Workspace | Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers | View Campaigns<br>Edit Campaigns<br>Archive Campaigns<br>View Canvases<br>Edit Canvases<br>Archive Canvases<br>View Frequency Capping Rules<br>Edit Frequency Capping Rules<br>View Message Prioritization<br>Edit Message Prioritization<br>View Content Blocks<br>View Feature Flags<br>Edit Feature Flags<br>Archive Feature Flags<br>View Segments<br>Edit Segments<br>Edit Global Control Group<br>View IAM Templates<br>Edit IAM Templates<br>Archive IAM Templates<br>View Email Templates<br>Edit Email Templates<br>Archive Email Templates<br>View Webhook Templates<br>Edit Webhook Templates<br>Archive Webhook Templates<br>View Link Templates<br>Edit Link Templates<br>View Media Library Assets<br>View Locations<br>Edit Locations<br>Archive Locations<br>View Promotion Codes<br>Edit Promotion Codes<br>Export Promotion Codes<br>View Preference Centers<br>Edit Preference Centers<br>Edit Reports<br>View Banner Templates<br>View Multi Language Settings<br>Use Operator<br>View Decisioning Studio Agents<br>View Decisioning Studio Conversion Event |
| Workspace | Access Dev Console | View API Keys<br>Edit API Keys<br>View Internal Groups<br>Edit Internal Groups<br>Delete Internal Groups<br>View Message Activity Log<br>View Event User Log<br>View API Identifiers<br>View API Usage Dashboard<br>View API Limits<br>View API Usage Alerts<br>Edit API Usage Alerts<br>View SDK Debugger<br>Edit SDK Debugger |
| Workspace | Approve and Deny Campaigns | Approve Campaigns |
| Workspace | Approve and Deny Canvases | Approve Canvases |
| Workspace | Export User Data | Export User Data |
| Workspace | Import and Update User Data | View Import Users<br>Import Users<br>Edit User Data |
| Workspace | Edit Segments | Archive Segments |
| Workspace | Launch and Manage Content Blocks | Edit Content Blocks<br>Archive Content Blocks<br>Launch Content Blocks |
| Workspace | Manage Media Library | Edit Media Library Assets<br>Delete Media Library Assets |
| Workspace | Launch Preference Centers | Launch Preference Centers |
| Workspace | Manage Apps | View App Settings<br>Edit App Settings<br>View Push Settings<br>Edit Push Settings<br>Edit Banner Templates<br>Archive Banner Templates |
| Workspace | Manage Catalogs Dashboard Permission | View Catalogs<br>Edit Catalogs<br>Export Catalogs<br>Delete Catalogs |
| Workspace | Manage Dashboard Users | Edit Dashboard Users |
| Workspace | Manage Email Settings | View Email Settings<br>Edit Email Settings |
| Workspace | Manage Events, Attributes, Purchases | View Custom Attributes<br>Edit Custom Attributes<br>Blocklist Custom Attributes<br>Delete Custom Attributes<br>Export Custom Attributes<br>View Custom Events<br>Edit Custom Events<br>Blocklist Custom Events<br>Delete Custom Events<br>Export Custom Events<br>Edit Custom Event Property Segmentation<br>View Products<br>Edit Products<br>Blocklist Products<br>Edit Purchase Property Segmentation |
| Workspace | Manage External Integrations | Edit Technology Partners<br>Edit Cloud Data Ingestion |
| Workspace | Manage Multi Language Settings | Edit Localization Settings<br>Delete Localization Settings |
| Workspace | Manage Subscription Groups | Edit Subscriptions |
| Workspace | Manage Tags | View Tags<br>Edit Tags<br>Delete Tags |
| Workspace | Manage Teams | View Teams<br>Edit Teams<br>Archive Teams |
| Workspace | View Data Transformations | View Data Transformation |
| Workspace | Edit Data Transformations | Edit Data Transformation |
| Workspace | Manage User Data Encryption | Edit Identifier Field-Level Encryption |
| Workspace | Send Campaigns, Canvases | Launch Campaigns<br>Launch Canvases |
| Workspace | View Billing Details | View Billing Details |
| Workspace | View Currents Integrations | View Currents Integrations |
| Workspace | Edit Currents Integrations | Edit Currents Integrations |
| Workspace | View Custom Attributes Marked as PII | View Custom Attributes Marked as PII |
| Workspace | View PII | View PII |
| Workspace | View User Profiles PII Compliant | View User Profiles PII Compliant |
| Workspace | View Usage Data | View Usage Data |
| Workspace | Merge Duplicate Users | Merge Duplicate Users |
| Workspace | Preview Duplicate Users | Preview Duplicate Users |
| Workspace | Create and Edit Canvas Templates | Edit Canvas Templates |
| Workspace | View Canvas Templates | View Canvas Templates |
| Workspace | Archive Canvas Templates | Archive Canvas Templates |
| Workspace | Publish Landing Pages | Publish Landing Pages |
| Workspace | Create Landing Page Drafts | Edit Landing Page Drafts |
| Workspace | Access Landing Pages | View Landing Pages |
| Workspace | Create and Edit Landing Page Templates | Edit Landing Page Templates |
| Workspace | View Landing Page Templates | View Landing Page Templates |
| Workspace | Archive Landing Page Templates | Archive Landing Page Templates |
| Workspace | View Custom AI Agents | View Custom AI Agents |
| Workspace | Edit Custom AI Agents | Edit Custom AI Agents<br> Archive Custom AI Agents |
| Workspace | View Placements | View Placements |
| Workspace | Edit Placements | Edit Placements |
| Workspace | Archive Placements | Archive Placements |
| Workspace | New | View Merge Users |
| Workspace | New | View User Deletion Records |
| Workspace | New | Delete Users From Dashboard |
| Workspace | New | View Banner Templates |
| Workspace | New | Edit Banner Templates |
| Workspace | New | Archive Banner Templates |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Frequently asked questions

### Can I opt out of or revert the migration?

Braze does not support reverting the migration. We will support you through the migration and monitor the migration closely to quickly address any issues.

### Will existing users lose access to Braze during the migration?

No, there will be no downtime to Braze during the migration. However, updates to permissions will be locked during the migration. We anticipate the migration taking up to 15 minutes for completion.