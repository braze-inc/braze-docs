---
nav_title: Handling Unknown Phone Numbers
article_title: Non-Native SMS Unknown Phone Number Handling
page_order: 1
description: "This refernence article covers how Braze will go about handling unknown phone numbers for non-native SMS users."
page_type: reference
channel:
  - SMS

---

# Handling unknown phone numbers - new users

You may find that once you get SMS up and running with Braze that you receive messages from unknown users. Noted below are the steps through which an unidentified user and number get processed.

Braze can automatically create a user when a user with a new phone number responds with a `START` or `STOP` (or any other variation of these keywords).  When creating the user, Braze will set their phone field with the [E.164][e.164] number provided by our SMS provider.  In addition, the [User Alias][ualink] ('phone') will be set with the same value.<br><br>Customers can use the [User Attributes Object][uaolink] in tandem with the [Track Endpoint][telink] to find users based on their alias and set an `external_id`.

## Opt-In/Out and Custom Keyword Workflow for Unknown Numbers

Braze automatically addresses an unknown number in one of three ways:
1. If an opt-in keyword is texted:
  * Braze creates an anonymous profile
  * Our system sets the phone attribute
  * Subscribes the user to the corresponding subscription group based on what opt-in keyword was received by Braze.<br><br>
2. If an opt-out keyword is texted:
  * Braze creates an anonymous profile
  * Our system sets the phone attribute
  * Unsubscribes the user from the corresponding subscription group based on what opt-out keyword was received by Braze.<br><br>
3. If any other custom keyword is texted:
  * Braze ignores the text message and does nothing.

{% alert important %}
If you would like to enable this functionality, please contact your Onboarding Manager or Customer Success Manager.
{% endalert %}

[ualink]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[telink]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[uaolink]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[e.164]: https://en.wikipedia.org/wiki/E.164
