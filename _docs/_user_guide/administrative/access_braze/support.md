---
nav_title: Support Portal
article_title: About Braze support
description: "Learn how to access the Braze support portal, submit detailed support cases, and manage your designated support contacts."
alias: /braze_support/
search_rank: 7
---

# Braze support portal

> Learn how to access the Braze support portal, submit detailed support cases, and manage your designated support contacts.

## Accessing the Braze support portal

To contact the Braze Support team, navigate to the Braze dashboard. In the dashboard, select **Support** > **Get help**.

![The "Support" dropdown with the option to get help.]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:60%;"}

Depending on your Braze permissions and if you're a designated support contact (premium), you will either be taken to the Braze support portal, where you can submit and track cases, or our standard support form. If you're unsure if you are a Braze support contact, reach out to your company's Braze administrator, Braze success manager, or account owner.

## Submitting a support case

To help us resolve your technical issues as quickly as possible, please submit a detailed support ticket that includes information about your organization, your affected user segments, screenshots of the issue, and any error logs.

### Step 1: Complete the questionnaire

Complete the questionnaire...

![ALT_TEXT.]()

### Step 2: Compose your message

1. In the **Subject** field, enter a short description of the issue.
2. From the dropdown, choose a severity level. Only select **Critical** if your production instance is down and all work within Braze has stopped.
3. Compose your message. To get started, copy and paste this template into the body of your message.

```plaintext
Workspace details:

- Name: Enter workspace name
- Campaign: Enter the URL
- Size of segment: N/A 
- External IDs: N/A

Describe the issue here.

What was the expected behavior vs. the actual behavior?

Steps to reproduce:

1. Go to...
2. Select...
3. Choose...
```

### Step 3: Attach screenshots

Consider attaching a screenshot to illustrate the problem. Providing these images can significantly aid our understanding of the issue and speed up the resolution process. To attach screenshot...

### Step 4: Attach browser logs

If..., then attach the following logs from your web browser.

Share a sampling of users rather than the entire affected segment. Providing a smaller number of users helps us narrow our scope and speed up our investigations.

#### Step 4.1: Access the developer tools

{% tabs %}
{% tab Chrome %}
1. Go to the page in Braze where you're experiencing the issue.
2. Right-click the page, then select **Inspect**.
{% endtab %}  
  
{% tab Firefox %}
1. Go to the page in Braze where you're experiencing the issue.
2. Right-click the page, then select **Inspect Element**.
{% endtab %}

{% tab Safari %}
1. Launch Safaris, then from the menu bar at the top of your screen, select **Safari** > **Settings**.
2. In the **Advanced** tab, check **Show features for web developers**.
3. Go to the page in Braze where you're experiencing the issue, then right-click and select **Inspect Element**.
{% endtab %}
{% endtabs %}

#### Step 4.2: Get console logs

Network logs (also known as HAR logs) contain a history of network requests made between your browser and the Braze server, which helps us troubleshoot the individual components on the page causing issues.

If you contact Support, it'll be useful to have the impacted user collect network logs (HAR logs) from their browser while the issue occurs. This will display the network requests between the browser and the server for the individual components of a webpage, as well as the Braze dashboard the user is trying to open.

{% tabs %}
{% tab Chrome %}
1. From your developer tools, select the **Console** tab.
2. Take a screenshot of all messages in the log.<br><br>![The "Fetch/XHR" tab in a Chrome browser.][1]{: style="max-width:60%;"}
{% endtab %}  
  
{% tab Firefox %}
1. From your developer tools, select the **Console** tab.
2. Take a screenshot of all messages in the log.<br><br>![The "Console" tab in a Firefox browser.]()
{% endtab %}

{% tab Safari %}
1. From your developer tools, select the **Console** tab.
2. Take a screenshot of all messages in the log.<br><br>![The "Console" tab in a Safari browser.]()
{% endtab %}
{% endtabs %}

### Step 5: Submit your support case

When you're ready, select ... to submit your support case.

## Managing designated support contacts

{% alert important %}
Only users with [admin permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) can manage designated support contacts.
{% endalert %}

Designated support contacts can access and reply to any support cases submitted by members of your organization. Your maximum number of contacts is determined by your contract. To increase your limit, contact your customer success manager.

{% tabs local %}
{% tab another user %}
To make another user a designated support contact:

1. Go to **Settings** > **Company Users**.
2. Search using the user's name or email address, then select them from the list.
3. Under **Department**, select their department from the dropdown, then check **Set this user as a Designated Support Contact for Braze Support Portal**.
4. When you're finished, select **Update user**. They'll be sent an email prompting them to finish setting up their account.

![The checkbox for setting a user as a designated support contact.]()
{% endtab %}

{% tab yourself %}
To make yourself a designated support contact:

1. This.
2. This.
3. This.

![ALT_TEXT.]()
{% endtab %}
{% endtabs %}

{% alert note %}
Marking an issue as "Critical" means your production instance is down, and all work within Braze has stopped.
{% endalert %}

[1]: {% image_buster /assets/img/network_xhr.png %}

