---
nav_title: The dashboard
article_title: The Braze dashboard
page_order: 1
page_type: reference
description: "The Braze dashboard is your central workspace for building, managing, and analyzing customer engagement. It brings together messaging tools, audience insights, segmentation, and real-time performance data in one place."

---

# The Braze dashboard

> The Braze dashboard is your central workspace for building, managing, and analyzing customer engagement. Access it at [dashboard.braze.com](https://dashboard.braze.com/) or [dashboard.braze.eu](https://dashboard.braze.eu/).

Use the Braze dashboard to plan campaigns, launch and manage messages, explore audience insights, adjust segmentation, and review real-time performance and engagement metrics from a single interface.

## Dashboard overview

When you log in, the dashboard provides a centralized view of your engagement tools and data:

- **Home page:** Shows your [recently edited content](#pick-up-where-you-left-off) and key performance metrics at a glance
- **Left navigation:** Organizes tools by function (messaging, audience, analytics, settings)
- **Global header:** Provides quick access to search, support, language settings, notifications, and your account

Your dashboard experience is organized by [workspaces]({{site.baseurl}}/user_guide/getting_started/workspaces), which help you manage content for different brands, regions, or teams. You can [switch between workspaces](#workspace-switcher) at any time from the side navigation.

## Access your dashboard

To get started, [sign in to your Braze account]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account). Your access to pages within the dashboard and permission to perform certain actions are based on your assigned [user permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#list-of-permissions). If you need help with your permissions, contact your Braze administrators.

## Navigate Braze

Braze navigation is designed to help you efficiently access features and content across devices. There are two levels of navigation in the Braze dashboard: global header and side navigation.

The global header is almost always visible at the top of the screen. It provides quick access to essential tools and settings, including:

- Search
- Support and community links
- [Dashboard language]({{site.baseurl}}/user_guide/administer/personal/language_settings/)
- Notifications
- Account settings
- [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/)

### Use the side navigation

The vertical menu on the left organizes Braze tools by function and keeps your most-used items within reach. Select a main menu item to reveal its options in a stacked vertical layout. 

![Workspace switcher in Braze dashboard]({% image_buster /assets/img/workspace_switcher.png %}){: style="max-width:35%;float:right;margin-left:15px"}

#### Workspace switcher

Located at the top of the side navigation, the workspace switcher lets you move between different workspaces in your Braze instance. The active workspace is highlighted.

[Workspaces]({{site.baseurl}}/user_guide/getting_started/workspaces) help organize content by brand, region, product line, or team. Each workspace includes its own data, campaigns, and settings. Your access can vary between workspaces. For example, you might have editing access in one workspace and view-only access in another.

To switch workspaces, select the workspace dropdown at the top of the side navigation and choose the workspace you want to access. You can also [add favorite workspaces](#adding-favorite-workspaces) for faster access to the ones you use most often.

#### Minimize the side navigation

To reduce visual clutter, especially during tasks like designing a Canvas, you can minimize the side navigation panel. Press **Minimize menu** to collapse it. Even when minimized, hover over any icon to view tooltips with menu item names. This helps you move quickly between tools while keeping your workspace clean.

![Minimize and maximize menu icons]({% image_buster /assets/img/minimize_expand_menu.png %}){: style="max-width:60%;border:none"}

#### Responsive navigation

The navigation adapts seamlessly to different screen sizes. On smaller screens, the side navigation collapses automatically. Press <i class="fa-solid fa-bars" aria-label="Open navigation menu"></i> to open the menu when needed. 

![On smaller screens, the side navigation collapses automatically. Tapping the menu icon opens navigation options.]({% image_buster /assets/img/navigation/navigation_small_screens.png %}){: style="max-width: 80%;border:none"}

## Search your dashboard

The global search bar, located in the header, is the fastest way to find content across your Braze dashboard. Select to open the search interface and jump directly to what you need. 

![Global search open with no search terms entered, showing recently open pages.]({% image_buster /assets/img/navigation/search_recently_opened.png %})

Your recently opened content appears below the search bar. This includes any campaign, Canvas, template, or page you’ve recently interacted with—making it easy to return to your work.

### What can you search for?

You can search for the following items and actions:

- Campaign names
- Canvas names
- Content Blocks
- Segment names
- Email template names
- Pages within Braze (including synonyms)

{% alert tip %}
To search for exact text, put your search term in quotations (""). For example, searching for [“all users”] will return all items that contain the exact phrase “all users” in their name.
{% endalert %}

### Content type and status tags

Each result is labeled with a tag indicating its content type—such as campaign, Canvas, or segment—and its status (active, archived, stopped).

### Filter for active and draft content

By default, search includes active, draft, and archived items. Use the **Show active and draft only** toggle to narrow your results.

![The "Show active and draft only" toggle.]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### Keyboard shortcuts

You can move through search results using your keyboard.

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2), {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| Action                      | Keyboard shortcut                                                             |
| --------------------------- | ----------------------------------------------------------------------------- |
| Open the search menu        | {::nomarkdown} <ul> <li> Mac: <kbd>⌘</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> <li>Windows: <kbd>Ctrl</kbd>&nbsp;+&nbsp;<kbd>K</kbd> </li> </ul> {:/}  |
| Move between search results | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| Select a search result      | <kbd>Enter</kbd>    |
| Close the search menu       | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tips

The Braze dashboard includes several features to help you work more efficiently and quickly access the tools and content you use most.

### Pick up where you left off

On the **Home** page, the dashboard displays your recently edited or created campaigns, Canvases, and segments. This makes it easy to return to work in progress without searching. Each item includes tags showing the content type and status (such as draft, active, or stopped).

![A Canvas draft, an active segment, and a campaign draft in the "Pick up where you left off" section.]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

For more information, see [Home dashboard]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off).

### Add favorite workspaces

If you work across multiple workspaces, you can mark your most frequently used ones as favorites for faster access. To add favorite workspaces, [access your profile settings](#accessing-your-profile-settings), locate the **Favorite workspaces** field in the **Account Profile** section, and select the workspaces you want to favorite. Your favorite workspaces will appear at the top of the workspace switcher for quick access.

### Access your profile settings

To manage your account settings, notification preferences, and personal information:

1. Select your profile icon in the global header.
2. Select **Manage your account** to access your profile page.

From your profile page, you can update your email settings, configure two-factor authentication, view your API keys, and manage other account details.

## Accessibility in the dashboard

The Braze dashboard uses brand colors that meet WCAG AA standards for color contrast. This supports an inclusive experience for all users and aligns with accessibility best practices.

## Sharing feedback

Want to tell us what you think? You can share feedback about navigation, accessibility, usability, visual design, and more. Open the **Support** menu in the global header and select **Share feedback**. We review all feedback to help improve your Braze experience.

## Related resources

### Administrative tasks

- [Create and manage workspaces]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces/)
- [Manage Braze users]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/)
- [User permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)
- [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/)

### Key tasks and next steps

- **Build campaigns**: [Create a campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/)
- **Create journeys**: [Build a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- **Define audiences**: [Create a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)
- **Review performance**: [Analytics overview]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/)
- **Configure settings**: [App settings]({{site.baseurl}}/user_guide/administer/global/workspace_settings/)


