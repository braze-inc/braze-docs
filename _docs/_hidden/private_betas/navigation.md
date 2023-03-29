---
nav_title: Navigation
permalink: /navigation/
hidden: true
---

# Braze navigation

> We're updating the Braze navigation to help you create and access your content more quickly and efficiently. To make this transition easier for you and your team, this guide covers what has changed and what you can expect next.

The new Braze navigation features a completely redesigned information architecture (how information is organized, grouped, and presented) to make each part of Braze more findable and understandable. 

Features are now organized into intuitive categories that are familiar and relevant to a marketer's workflow in Braze. Top-level categories are collapsed by default so you can get a better view of each section at a glance. Some pages have been renamed to better represent their contents.

Early access participants can turn on the new navigation at any time by selecting **Switch to new nav** in the global header.

![Global header of Braze with a button to switch to the new navigation.]({% image_buster /assets/img/navigation/global_header_switch.png %}){: style="max-width:70%"}

{% alert important %}
The new navigation is currently in early access and is being tested with a select group of customers. During the early access period, we'll be collecting feedback regularly. You can share feedback directly from the dashboard: when in the new navigation view, expand the **Tour new navigation** button and select **Send feedback**.
{% endalert %}

## What to expect next

The new navigation will be released to all Braze customers in **April 2023**, and will include an updated look and feel that is different from the early access version.

## What's changed

### App group rename

As part of our navigation and information architecture changes, we have renamed "App Group" to "Workspace". We recognize that the language "App Group" doesn't reflect the way many users onboard, approach, and use the Braze platform. To better reflect the many use cases of Braze, "App Group" is now "Workspace".

If you're using our updated navigation, this change will appear throughout the platform.

### Global header

{% tabs %}
{% tab New navigation %}

![]({% image_buster /assets/img/navigation/global_header_new.png %}){: style="border:0"}

1. **Braze logo** - Select to go to your Braze home page.
2. **Page name** - The name of the page you are currently on.
3. **Tour new navigation** - Retake the navigation tour or expand the dropdown to access options for documentation or to send us feedback on the new navigation.
4. **Community** - Access links to the Braze Bonfire community, our blog, case studies, and the product roadmap.
5. **Support** - Check our system status and access links to Braze documentation, Braze Learning, or get help from support.
6. **Language selector** - Select the language you want to use for Braze.
7. **Your profile** - View your profile, company settings, billing, company users, or sign out.
8. **Administrator icon** - Appears next to your profile if you are an administrator for your company.

{% endtab %}
{% tab Old navigation %}

![]({% image_buster /assets/img/navigation/global_header_old.png %}){: style="border:0"}

1. **Braze logo** - Select to go to your Braze home page.
2. **Page name** - The name of the page you are currently on.
3. **Switch to new nav** - Switch your view to the new navigation experience or expand the dropdown to access the documentation.
3. **Resources** - Access links to Braze Learning, documentation, Braze Bonfire community, our blog, case studies, and the product roadmap.
4. **Get Help** - Check our system status, visit help articles, or get help from support.
5. **Language selector** - Select the language you want to use for Braze.
6. **Your profile** - View your profile, company settings, subscriptions and usage, company users, or sign out.
7. **Administrator icon** - Appears next to your profile if you are an administrator for your company.

{% endtab %}
{% tab Changes %}

![]({% image_buster /assets/img/navigation/global_header_compare.png %}){: style="border:0"}

- Community
   - **Resources** is now **Community**
- Support
   - **Get Help** is now **Support** 
   - **Braze Learning** and **Documentation** are now located here
   - **Braze Support** is now **Get Help** 
- Your profile
   - **Account Settings** is now **Manage Your Profile**
   - **Subscriptions and Usage** is now **Billing**
   - **Manage Users** is now **Company Users**

{% endtab %}
{% endtabs %}

### Sidebar

<style>
#navigation td {
    word-break: break-word;
    width: 50%;
    font-size: 16px;
}
</style>

{% tabs %}
{% tab New navigation %}

<table id="navigation">
<tbody>
  <tr>
    <td><img src="{% image_buster /assets/img/navigation/sidebar_new.png %}"></td>
    <td><b>1. Workspace selector</b> - See what workspace you're currently in or switch between workspaces.<br><br><b>2. Home</b> - Braze home page. After your initial setup, this is your <b>Overview</b> dashboard.<br><br><b>3. Messaging</b> - Create and manage your campaigns and Canvases, and access a calendar view of your upcoming scheduled messages.<br><br><b>4. Audience</b> - Contains everything related to your users, such as searching or importing users, managing your segments, Global Control Group, subscription groups, and more.<br><br><b>5. Templates</b> - Contains your message templates, Content Blocks, and Media Library.<br><br><b>6. Analytics</b> - Contains your reports, analytics dashboard, and Predictions.<br><br><b>7. Partner Integrations</b> - Contains our technology partner integrations, solutions partners, and data export (Currents).<br><br><b>8. Data Settings</b> - Contains settings related to user data, such as custom user attributes, custom user events, catalogs, products, and more.<br><br><b>9. Settings</b> - Manage your workspace integration, workspace settings, company settings, billing, and more.<br></td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Old navigation %}

<table id="navigation">
<tbody>
  <tr>
    <td><img src="{% image_buster /assets/img/navigation/sidebar_old.png %}"></td>
    <td><b>1. App Group selector</b> - See what app group you're currently in or switch between app groups.<br><br><b>2. Data</b> - Contains various reports, dashboards, and settings related to user data in Braze.<br><br><b>3. Engagement</b> - Contains pages related to messaging, such as your segments campaigns, Canvases, message templates, and more.<br><br><b>4. Users</b> - Search or import users, or manage your subscription groups.<br><br><b>5. Integrations</b> - Contains integrations including our technology partners, Currents, and promotion codes.<br><br><b>6. Settings</b> - Contains app group settings, various data settings, logs, and more.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Changes %}

Top-level categories are now collapsed by default so you can get a better view of each section at a glance.

The following table lists where each page is located in the new navigation. Some pages have been renamed, and the new name is referenced in the "New location" column.

| Page name                     | New location                                                          |
| ----------------------------- | --------------------------------------------------------------------- |
| API Settings                  | **Settings** > **Workspace Setup and Testing** > **API Keys**         |
| Approval Workflow             | **Settings** > **Workspace Settings** > **Approval Workflow**         |
| Campaigns                     | **Messaging** > **Campaigns**                                         |
| Calendar                      | **Messaging** > **Content Calendar**                                  |
| Canvas                        | **Messaging** > **Canvas**                                            |
| Catalogs                      | **Data Settings** > **Catalogs**                                      |
| Connected Content             | **Settings** > **Workspace Settings** > **Connected Content**         |
| Content Blocks Library        | **Templates** > **Content Blocks**                                    |
| Conversions                   | **Analytics** > **Analytics Dashboards** > **Conversions**            |
| Currents                      | **Partner Integrations** > **Data Export (Currents)**                 |
| Custom Attributes             | **Data Settings** > **Custom User Attributes**                        |
| Custom Events (report)        | **Analytics** > **Reports** > **Custom Events Reports**               |
| Custom Events                 | **Data Settings** > **Custom User Events**                            |
| Data Feeds                    | **Data Settings** > **Data Feeds**                                    |
| Developer Console             | **Settings** > **Workspace Setup and Testing**                        |
| Email Performance             | **Analytics** > **Analytics Dashboards** > **Email Performance**      |
| Email Settings                | **Settings** > **Workspace Settings** > **Email Preferences**         |
| Email Templates               | **Templates** > **Email Templates**                                   |
| Engagement Reports            | **Analytics** > **Reports** > **Engagement**                          |
| Event User Log                | **Settings** > **Workspace Setup and Testing** > **Event User Log**   |
| Feature Flags                 | **Audience** > **Feature Flags**                                      |
| Global Control (report)       | **Analytics** > **Reports** > **Global Control**                      |
| Global Control Group Settings | **Audience** > **Global Control Group**                               |
| In-App Message Templates      | **Templates** > **In-App Message Templates**                          |
| Internal Groups               | **Settings** > **Workspace Setup and Testing** > **Internal Groups**  |
| Link Templates                | **Templates** > **Email Link Templates**                              |
| Locations                     | **Audience** > **Locations**                                          |
| Manage Settings               | **Settings** > **Workspace Settings**                                 |
| Manage Teams                  | **Settings** > **Workspace Settings** > **Internal Teams**            |
| Media Library                 | **Templates** > **Media Library**                                     |
| Message Activity Log          | **Settings** > **Workspace Setup and Testing** > **Message Activity** |
| News Feed                     | **Messaging** > **News Feed**                                         |
| Overview                      | **Home**                                                              |
| Predictions                   | **Analytics** > **Predictions**                                       |
| Products                      | **Data Settings** > **Products**                                      |
| Promotion Codes               | **Data Settings** > **Promotion Codes**                               |
| Push TTL Settings             | **Settings** > **Workspace Settings** > **Push Time-To-Live (TTL)**   |
| Report Builder                | **Analytics** > **Reports** > **Report Builder**                      |
| Revenue                       | **Analytics** > **Reports** > **Revenue**                             |
| Segments                      | **Audience** > **Segments**                                           |
| Segment Extensions            | **Audience** > **Segment Extensions**                                 |
| Segment Insights              | **Analytics** > **Reports** > **Segment Insights**                    |
| Global Message Settings       | **Settings** > **Workspace Settings** > **Message Frequency**         |
| SMS Performance               | **Analytics** > **Analytics Dashboards** > **SMS Performance**        |
| Subscription Group Management | **Audience** > **Subscription** > **Subscription Groups**             |
| Subscription Groups           | **Audience** > **Subscription** > **Subscription Groups**             |
| Tags                          | **Settings** > **Workspace Settings** > **Tag Management**            |
| Technology Partners           | **Partner Integrations** > **Technology Partner Integrations**        |
| User Import                   | **Audience** > **Import Users**                                       |
| User Search                   | **Audience** > **Search Users**                                       |
| Webhook Templates             | **Templates** > **Webhook Templates**                                 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}