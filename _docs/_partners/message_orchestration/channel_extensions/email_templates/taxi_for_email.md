---
nav_title: Taxi for Email
article_title: Taxi for Email
alias: /partners/taxi_for_email
description: "This article outlines the partnership between Braze and Taxi for Email, an online email marketing tool that allows Braze customers to create intelligent email templates using their drag and drop interface along with their simple yet powerful syntax."
page_type: partner
search_tag: Partner

---

# Taxi for Email

[Taxi For Email](http://taxiforemail.com/) is an online email marketing tool that encourages teams to easily collaborate on email campaigns. It allows teams to produce accurate and on-brand emails at a large scale in less time.

Taxi For Email can help Braze customers create intelligent email templates using our simple yet powerful syntax. With our easy-to-use drag and drop visual editor, copywriters and editors can build emails without needing to know HTML code. Using Taxi can help empower teams to do their best work by assigning access and setting permissions for team members. Once emails are ready to go Braze customers can export send-ready code from Taxi and upload it into Braze.


# Requirements

Requirement   | Source | Notes
--------------|--------| -----
Braze API Key | [Braze Platform](https://dashboard.braze.com/sign_in) | The API key must have the *Template's* permission enabled before use.

# Integration

The export functionality from Taxi For Email to Braze will allow users to send the HTML as a new template within the Braze platform.

To set up the Braze connector, you'll need to be logged into both your Braze and Taxi accounts.

## Step 1
In Taxi, navigate to your **Organization Settings** and select the **ESP Connectors** tab.

## Step 2
Click the **Add New** button and select "Braze" from the dropdown.

{% alert important %}
This will need to be enabled by Taxi. You will also need to name your new connector - we recommend titling the connector `Braze`.
{% endalert %}

## Step 3
Click **Braze** to edit the Connector Settings.

## Step 4
Select the **Endpoint** to send the template to. This can be found in the URL of your Braze account **e.g dashboard-03**.

## Step 5
Lastly, add your *templates enabled* Braze API key. This can be found under the **Developer Console** in your Braze account.
The field should now turn green if the details are accepted.

{% alert important %}
If the field is not green, please make sure that the **Templates** section checkboxes are all checked for your API Key, and verify that the specified **API Key** and **Endpoint** are both correct.
{% endalert %}

# Usage
To use this integration, look for your new email template in [Templates & Media > Email Templates][1] in your Braze account, or begin to create your email and choose your template from those presented.  

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
