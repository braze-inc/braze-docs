---
nav_title: Stripo
alias: /partners/stripo
---

# Stripo

[Stripo](https://stripo.email/) is a Drag-n-Drop email template builder that helps create sophisticated emails in no time due to workflow automation. Design responsive emails, setting which elements to display/hide on various devices, add interactive elements to emails right in the Stripo editor. The HTML code editor allows working with pure code to design unique emails.

Create emails with Stripo faster with its comprehensive Drag-n-Drop editor and set of basic blocks. Embed custom HTML code with interactive elements. Then export those emails to Braze in 2 clicks, where you finalize them — personalize, add contact information prior to running email campaigns, and track conversions after. Combine the tools for easy, productive communication with clients.

# Requirements

Requirement   | Source | Description
--------------|--------| -----
Braze API Key | [Braze Platform](https://dashboard.braze.com/sign_in) | The API key must have the *Template's* permission enabled before use.

# Integration Usage

The export functionality from Stripo to Braze will allow users to send the HTML as a new template within the Braze platform.

## Step 1
Once you have finished editing your email, click **export** located at the top next to the name field.
![Stripo Export]({% image_buster /assets/img_archive/stripo_export.png %})

## Step 2
Select **Braze** as your method of export.

## Step 3
Enter your `account name` (i.e `Appgroup name`), `API key`, and your `cluster instance`.
![Stripo Form]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
This is a one-time setup and any exports in the future will automatically utilize this API key.
{% endalert %}

# Usage
To use this integration, look for your new email template in [Templates & Media > Email Templates][1] in your Braze account, or begin to create your email and choose your template from those presented.  

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
