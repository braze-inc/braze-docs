---
nav_title: Handling Unknown Phone Numbers
page_order: 1
description: "This reference article covers how Braze processes certain keywords for SMS, as well as best practices."
page_type: reference
tool:
  - Dashboard
  - Docs
  - Campaigns

platform:
  - iOS
  - Android

channel:
  - SMS
---

# New Users

Braze has the ability to automatically creates a user when a user with a new phone number responds with a `START` or `STOP` (or any other variation of these keywords).  When creating the user, Braze will set their phone field with the [E.164][e.164] number provided by our SMS provider.  In addition, the [User Alias][ualink] ('phone') will be set with the same value.<br><br>Customers can use the [User Attributes Object][uaolink] in tandem with the [Track Endpoint][telink] to find users based on their alias and set an `external_id`.

{% alert important %}
If you would like to enable this functionality, please contact your Onboarding Manager or Customer Success Manager.
{% endalert %}

[ualink]: {{ site.baseurl }}/api/objects_filters/user_alias_object/
[telink]: {{ site.baseurl }}/api/endpoints/user_data/post_user_track/
[uaolink]: {{ site.baseurl }}/api/objects_filters/user_attributes_object/
[e.164]: https://en.wikipedia.org/wiki/E.164
