---
nav_title: User Archival
article_title: User Archival
page_order: 0
page_type: reference
description: "This reference article covers user archival definitions and how to customize your user archival policy."

---
# User archival

Each week, Braze runs a process to remove inactive users and dormant users from the Braze Services.

This process ensures that Braze provides accurate statistics regarding campaign reachable audiences. It also serves in accordance with two key concepts of [GDPR][1]:

1. The storage limitation principle - personal data processed and stored should be kept for no longer than is necessary
2. Having a legitimate business purpose to process personal data.

That is, personal data processed and stored should be kept for no longer than is necessary and personal data should only be processed for legitimate business purposes. Archived users will also have their unsubscribe status deleted in compliance with GDPR.

If you have a user profile in danger of being archived under these policies which needs to be retained, then register a single data point through our REST API for that user profile at least once every six months.

## Customizing your user archival policy

Braze provides data orchestrations features that make it quick and easy to customize your user archival policy. Create a user archival policy that gives you the best of both worlds with the Canvas [User Update]({{site.baseurl}}/user_update/) component.

This allows you to:

- Adhere to GDPR and privacy best practices by deleting user profiles that are no longer valuable.
- Retain any user profile that you have a legitimate business need for.

### Steps

1. Target users that meet archival criteria and that you'd like to retain.<br><br>
      ![Target users that last received any message more than 23 weeks ago, have never received a message from a campaign or Canvas step, last used these apps more than 23 weeks ago, and have used these apps exactly zero times.][2]<br><br>
2. Set re-eligibility to be a little less than 6 months long.<br><br>
      ![Entry controls with re-eligibility turned on and the re-eligibility window set to 23 weeks.][3]<br><br>
3. Configure the User Update step to add an attribute to each profile.<br><br>
      ![User Update step that adds the attribute "do_not_archive": true to the user's profile.][4]
{% details Sample User Update object %}
```json
{
    "attributes": [ 
        {
            "do_not_archive": true
        }
    ]
}
```
{% enddetails %}

## User archival definitions

### Active users

Braze defines an “active user” for a given period of time as any user who has a session in that time period. 

If a user loses connectivity, we will cache the session data locally and upload it when the user regains a network connection. These sessions will also be applied to the active user count. Additionally, if your app has a registration process, Braze will count all users as active—registered or unregistered.

If you set user IDs to identify users when a new user logs in they will be counted as a separate active user. Users who are updated via the API will also be counted as an active user in the time period that they are updated.

### Inactive users

"Inactive users" are users that are unreachable and have likely churned. Inactive users are those that meet all of these criteria:

- Can't receive email. For example, they do not have an email address or they are unsubscribed from all email lists.
- Can't receive SMS. For example, they do not have a valid phone number or they are unsubscribed from all SMS subscription groups.
- Can't receive push. For example, they have uninstalled the app or disabled push permissions.
- Haven't used any mobile app or visited a website in an app group in more than six months.
- Haven't received any messages from an app group in more than six months.
- Braze hasn't processed any data points for this user profile in more than six months.

In this case, these users cannot be messaged and are not engaging with your brand. These users have effectively churned.

### Dormant users

"Dormant users" are users who have had no activity in the last twelve months and:

- Haven't used any mobile app or visited a website in an app group in more than 12 months.
- Haven't received any messages from an app group in more than 12 months.
- Braze hasn't processed any data points for this user profile in more than 12 months.

## Spam blocking

Braze blocks individual users with over 5 million sessions ("dummy users"), and no longer ingests their SDK events, because they are usually the result of an incorrect integration. If you find that this has happened for a legitimate user, file a ticket with Braze [support]({{site.baseurl}}/braze_support/).

To find your dashboard's dummy users, perform the following steps:

1. Create a [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).
2. Select the filter `Session Count` and set it to `more than 5,000,000`.
3. Export the segment via CSV.

If necessary, you can delete the users via the [Users Delete]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) API endpoint.

[1]: {{site.baseurl}}/dp-technical-assistance/#the-right-to-erasure
[2]: {% image_buster /assets/img_archive/user_archival_policy1.png %}
[3]: {% image_buster /assets/img_archive/user_archival_policy2.png %}
[4]: {% image_buster /assets/img_archive/user_archival_policy3.png %}
