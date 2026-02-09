---
nav_title: User archival
article_title: User Archival
permalink: /user_archival/
page_order: 0
page_type: reference
description: "This reference article covers user archival definitions, spam blocking, and how to customize your user archival policy."

---
# User archival

> Each week on Sunday at 5:30 am EST, Braze runs a process to remove inactive users and dormant users from the Braze Services. Note that Braze does not archive users unless the number of users in the workspace hits the 250,000 threshold.

This process is intended to help Braze provide accurate statistics regarding campaign reachable audiences. It also serves in accordance with two key concepts of [GDPR][1]:

1. The storage limitation principle—personal data processed and stored should be kept for no longer than is necessary
2. Having a legitimate business purpose to process personal data.

That is, personal data processed and stored should be kept for no longer than is necessary, and personal data should only be processed for legitimate business purposes. Archived users will also have their unsubscribe status deleted in compliance with GDPR.

{% alert important %}
Archived users will be permanently deleted. <br><br>You can [customize your user archival policy](#customizing-your-user-archival-policy) using Canvas. Customers have full control over whether a user is inactive or dormant. Canvas offers the ability to do this automatically, allowing you to effectively turn off this functionality for some or all of your inactive or dormant users.
{% endalert %}

## User archival definitions

### Active users

Braze defines an "active user" for a given period of time as any user who has recorded a session in a mobile app or website, has been updated, has been sent a message, or has interacted with a message.

If you set user IDs to identify users when a new user logs in, they will be counted as a separate active user. Users who are updated via the API will also be counted as an active user in the time period that they are updated.

{% alert important %} 
Both inactive users and dormant users will be archived unless the user is excluded from archiving for the reasons listed below. 
{% endalert %}

### Inactive users

"Inactive users" are users who are unreachable and have likely churned. Inactive users are those who meet all of these criteria:

- Can't receive email. For example, they do not have an email address, or they are unsubscribed from all email lists.
- Can't receive SMS. For example, they do not have a valid phone number, or they are unsubscribed from all SMS subscription groups.
- Can't receive push. For example, they have uninstalled the app or disabled push permissions.
- Can't receive a WhatsApp message. For example, they do not have a valid phone number or are unsubscribed from all WhatsApp subscription groups.
- Can't receive a LINE message. For example, they do not have a LINE ID or are unsubscribed from all LINE subscription groups.
- Haven't used any mobile app or visited a website in a workspace in more than six months.
- Haven't received any messages from a workspace in more than six months.
- Haven't been updated in more than six months.

In this case, these users cannot be messaged and are not engaging with your brand. These users have effectively churned.

### Dormant users

"Dormant users" are users who have had no activity in the last twelve months and:

- Haven't used any mobile app or visited a website in a workspace in more than 12 months.
- Haven't received any messages from a workspace in more than 12 months.
- Haven't been updated in more than 12 months.

## Global Control Group users

Users in the Global Control Group will never be archived, even if they meet the definition of inactive or dormant users. 

### Treatment sample group

Treatment sample group users in a Global Control Group Report are excluded from archiving.

## Test users

Test users will never be archived, even if they meet the definition of inactive or dormant users.

## Spam blocking

Braze blocks individual users with over 5 million sessions ("dummy users"), and no longer ingests their SDK events, because they are usually the result of an incorrect integration. If you find that this has happened for a legitimate user, file a ticket with Braze [support]({{site.baseurl}}/braze_support/).

To find your dashboard's dummy users, perform the following steps:

1. Create a [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).
2. Select the filter `Session Count` and set it to `more than 5,000,000`.
3. Export the segment via CSV.

If necessary, you can delete the users via the [`/users/delete` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).

## Customizing your user archival policy

Braze provides data orchestration features that allow you to customize your user archival policy. Create a user archival policy that gives you the best of both worlds with the Canvas [User Update]({{site.baseurl}}/user_update/) component.

This allows you to:

- Adhere to GDPR and privacy best practices by deleting user profiles that are no longer valuable.
- Retain any user profile that you have a legitimate business need for.

### Steps

1. Target users that meet your brand's archival criteria and that you'd like to retain. For example, you might retain users who:
    - Last received a message more than 23 weeks ago or have never received a message<br>AND<br>
    - Last used your app more than 23 weeks ago or had zero sessions in your app<br><br>
      ![Target users who last received any message more than 23 weeks ago, have never received a message from a campaign or Canvas step, last used these apps more than 23 weeks ago, and have used these apps exactly zero times.][2]<br><br>
2. Set re-eligibility to be a little less than 6 months long.<br><br>
      ![Entry controls with re-eligibility turned on and the re-eligibility window set to 23 weeks.][3]<br><br>
3. Configure the User Update step to add an event to each profile.<br><br>
      ![User Update step that adds the "do_not_archive" event to the user's profile.][4]
{% details Sample User Update object %}

{% raw %}
```json
{
    "events": [
        {
            "name": "do_not_archive",
            "time": "{{ 'now' | time_zone: 'UTC' | date: '%Y-%m-%dT%H:%M:%SZ' }}"
        }
    ]
}
```
{% endraw %}

{% enddetails %}

[1]: {{site.baseurl}}/dp-technical-assistance/#the-right-to-erasure
[2]: {% image_buster /assets/img_archive/user_archival_policy1.png %}
[3]: {% image_buster /assets/img_archive/user_archival_policy2.png %}
[4]: {% image_buster /assets/img_archive/user_archival_policy3.png %}
