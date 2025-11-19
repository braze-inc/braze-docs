{% if include.content == "Differences" %}

You can use [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), [permission sets]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set), and [user roles]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) to manage dashboard user access and responsibilities within Braze. Each feature encompasses a different collection of permissions and access-controls.

### Key differences

At a high level, each feature has a different scope:
- Permission sets control what dashboard users can do across all workspaces.
- Roles control what dashboard users can do in specific workspaces.
- Teams control the audiences that dashboard users can reach with their messages.

| Feature | What you can do | Scope&nbsp;of&nbsp;access |
| - | - | - |
| [Permission sets]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) | Bundle permissions related to specific subject areas or actions (such as for “Developers” and “Marketers”), then apply them to dashboard users who need the same permissions across different workspaces. | Company wide |
| [Roles]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) | Bundle individual custom permissions and workspace-access controls (such as "Marketer - Fashion Brands", where the user has certain permissions associated with their role as a marketer and is limited to the "Fashion Brands" workspaces). Then assign a role to dashboard users to directly grant them the associated permissions and workspace access. <br><br>Users with this level of access are typically managers in more tightly controlled setups with many brands or regional workspaces in one dashboard. | Specific workspaces |
| [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/#creating-teams) | Limit dashboard user access to resources based on the audience (such as customer base location, language, and custom attributes). <br><br>Users with this level of access typically are responsible for a specific scope within the brand that they’re working on, such as building language-specific content for a multilingual brand. | Specific dashboard |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endif %}