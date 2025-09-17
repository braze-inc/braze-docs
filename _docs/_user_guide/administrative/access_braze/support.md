---
nav_title: Braze support
article_title: Support
description: "This page will help you locate the Braze support portal to submit Braze product feedback. This page will only be accessible to Braze customers."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"}Braze Support

## Access the support portal

To contact the Braze Support team, navigate to the Braze dashboard. In the dashboard, select **Support** > **Get help**.

![The "Support" dropdown with the option to get help.]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:60%;"}

Depending on your Braze permissions and if you're a designated support contact, you will either be taken to the Braze support portal, where you can submit and track cases, or our standard support form. If you're unsure if you are a Braze support contact, reach out to your company's Braze administrator, Braze success manager, or account owner.

## Adding designated support contacts

Designated support contacts can access all support cases for your company, regardless of who submitted them. You can set users as designated support contacts directly from the **Edit user** page. 

1. Go to **Settings** > **Company Users**, then search for the user by their name or email address.
2. Either select the user name or hover over the user name row to display a menu. 
3. In the menu, select **Edit** to be redirected to the **Edit user** page.
4. Check the checkbox for **Set this user as a Designated Support Contact for Braze Support Portal**.

![The checkbox for setting a user as a designated support contact.]({% image_buster /assets/img_archive/designated_support_contact.png %}){: style="max-width:70%;"}

### Gaining access

After a user is designated as a support contact, the Braze support portal will send that user a welcome email with instructions to set up their access.

## Provide developer console screenshots

When communicating with support, you may find you need to access your developer console to provide additional information:
- Chrome
  1. Right-click on the webpage and select **Inspect**.
  2. Select the **Console** tab in the window that opens.
  3. Take a screenshot of the console tab.<br><br>
- Firefox
  1. Right-click on the webpage and select **Inspect Element**.
  2. Select the **Console** tab in the window that opens.
  3. Take a screenshot of the console tab.<br><br>
- Safari
  1. Go to Safari in the menu bar at the top of your screen and then select **Preferences**.
  2. Select **Advanced** and then check the checkbox next to **Show Develop menu in menu bar**. You can then exit the window.
  3. Right-click on the webpage and select **Inspect Element**.
  4. Select the **Console** tab in the window that opens.
  5. Take a screenshot of the console tab.

## Best practices for submitting a support case

### Provide as much information as possible

The more insights you can offer, the better. Include specifics like the workspace, the URL to the campaign or segment, and any relevant external IDs. This can help us troubleshoot your issue more efficiently.

### Provide a sample of users

Share a sampling of users rather than the entire affected segment. Providing a smaller number of users helps us narrow our scope and speed up our investigations.

### Attach network logs (HAR logs)

If you contact Support, it'll be useful to have the impacted user collect network logs (HAR logs) from their browser while the issue occurs. This will display the network requests between the browser and the server for the individual components of a webpage, as well as the Braze dashboard the user is trying to open.

Have the affected user do the following:

1. Open their developer tools. If using Chrome, this can be done using the keyboard shortcut `option` + `⌘` + `J` (on macOS). If using Windows or Linux, this can be done using the shortcut `shift` + `CTRL` + `J`.
2. Select **Network** > **Fetch/XHR** or **XHR**.
3. Capture a screen recording or screenshot showing the **Name**, **Status**, **Size**, and **Time** for the elements.<br><br>![The "Fetch/XHR" tab in a Chrome browser.]({% image_buster /assets/img/network_xhr.png %}){: style="max-width:60%;"}

Then, attach the user's recording or screenshot to the Support ticket. This information can help Support's investigation.

### Clarify expected versus actual behavior

Let us know what you were expecting and what actually happened. This can help us narrow down the possible causes of the issue.

### Attach relevant images

Consider attaching a screenshot to illustrate the problem. Providing these images can significantly aid our understanding of the issue and speed up the resolution process.

### Assess the impact

Select the appropriate severity level to help us assign the right resources to address the problem. 

{% alert important %}
Marking an issue as "Critical" means your production instance is down, and all work within Braze has stopped.
{% endalert %}

## Troubleshooting access

If you receive an error when logging into the Braze Support Portal, such as `Check your entry`, make sure you followed the link in your welcome email to set a password for the portal. If you've done that or were previously able to log into the portal, create a Support ticket.