---
nav_title: Preference Center 
permalink: /preference_center/
description: "This article describes how to create and edit a preference center using the Preference Center Braze endpoints."
hidden: true
---

# Creating a preference center via API

Setting up a preference center provides a one-stop shop for your users' notification preferences with your email messaging. Using the preference center Braze endpoints, you can directly edit the HTML of your preference center to align with your branding and to understand your users' preferences.

{% alert important %}
The Braze endpoints used to create a preference center are currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

| Requirement | Description |
|---|---|
| Enabled preference center | Your Braze dashboard has permissions to use the preference center feature. |
| Valid app group with an email subscription group | A working app group with valid users and an email subscription group. |
| Valid user | A user with an email address and an external ID. |
| Generated API key with preference center permissions | In the Braze dashboard, go to **Developer Console** > **API Settings**. |
{: .reset-td-br-1 .reset-td-br-2}

## Step 1: Create the preference center via API

Let's begin building a preference center using the Create a preference center Braze endpoint. 

Here's an request body example that includes HTML.

This confirms that your preference center has been created.  

## Step 3: Update preference center details 

Next, edit your preference center using the PUT endpoint by passing through the following parameters:

If your update is successful, you'll see the following response:

## Step 4: Create a preference center URL

To create a preference center URL, include this Liquid: ```{{preference_center.${preference_center_name}}}}``` in an email campaign that's ready to be launched. For example, you can include this HTML combined with the Liquid tag at the bottom of your email to allow your users to edit their preferences.

```<a href="{{preference_center.${preference_center_name_example}}}">Edit your preferences</a>```


### General tips


### Troubleshooting


