---
nav_title: Message-Level One-Click List-Unsubscribe Settings
article_title: Message-Level One-Click List-Unsubscribe Settings
permalink: "/one-click_unsubscribe/"
hidden: true
description: "This article provides an overview of the one-click list-unsubscribe header settings that are applied at a message level."
---

# Message-level one-click list-unsubscribe settings

> Using one-click unsubscribe for the list-unsubscribe header ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) focuses on providing an easy way for recipients to opt-out from emails. You can adjust this header setting to be applied at a message level in your emails.

{% alert important %}
The message-level one-click list-unsubscribe setting is currently in early access. Contact your account manager if you're interested in participating in this early access.
{% endalert %}

In your email editor, go to **Sending Settings** > **Sending Info**. Select from the following options:

* **Use workspace default**: Uses the **Email Unsubscribe Header** settings set in **Email Preferences**. Any changes made to this setting will apply to all messages.
* **Unsubscribe globally from all emails**: Uses the Braze default one-click unsubscribe header. Users who click the unsubscribe button will have their global email subscription state set to "Unsubscribed."
* **Unsubscribe from specific subscription group**: Uses the specified subscription group. Users who click the unsubscribe button will be unsubscribed from the selected subscription group
* **Exclude unsubscribe**

Adjusting this setting will override the default behavior for one-click list unsubscribe in this email.

![]({% image_buster /assets/img/email_settings/one-click_unsubscribe_to_email_header.png %})

### Frequently asked questions

#### If I add the email headers for one-click manually and I have email unsubscribe header turned on, what is the expected behavior?

Select **Exclude unsubscribe** as the **One-click list-unsubscribe setting**. The email headers added for one-click list-unsubscribe will be applied to all future sends of this campaign.

#### Why do subscription groups have to match across message variants in order to launch?

For a campaign with A/B testing, Braze will randomly send a user one of the variants. If you have two different subscription groups set on the same campaign (Variant A is set to Subscription Group A, and Variant B is set to Subscription Group B), we cannot guarantee that users who are only subscribed to Subscription Group B will get Variant B. There can be a scenario where users are unsubscribing from a subscription group they're already opted out of.

#### The email unsubscribe header setting is turned off in Email Preferences, but in my campaign's sending info, the one-click list-unsubscribe setting is set to "Use workspace default". Is this a bug?

No. If the workspace setting is turned off and the message setting is set to **Use workspace default**, then Braze will follow what's configured in **Email Preferences**. This means, we will not add the one-click unsubscribe header for the campaign.

#### What happens if a subscription group is archived? Will this break the one-click unsubscribe on emails sent?

If a subscription group referenced in **Sending Info** for one-click is archived, Braze will still process unsubscribes from one-click. The subscription group will no longer be displayed on the dashboard (segment filter, user profile, and similar areas).

#### Is the one-click unsubscribe setting be available for email templates?

No, we currently do not have plans to add this for email templates as these templates aren't assigned to a sending domain. If you're interested in this feature for email templates, submit [product feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

#### Does this feature check that the one-click unsubscribe URL added to the custom option is valid?

No, we do not check or validate any links in the Braze dashboard.  

![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %})