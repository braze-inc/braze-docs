---
nav_title: Creating Custom Opt-In Prompts
page_order: 2

page_type: reference
description: "This article covers best practices for creating custom opt-in prompts that clearly list and demonstrate the benefits of push messaging."
channel: push
no_index: true
---

# Creating Custom Opt-In Prompts

Even if you keep best practices in mind when designing and sending push messages, some users may turn them off before realizing any of the benefits that they would provide. Users may have had previous negative experiences with spammy, irrelevant push messages from other apps and now will decline any request to receive push messages from any app.

Furthermore, the legal environment surrounding electronic messaging in some locales is becoming increasingly strict. For example, [Canada's Anti-Spam Legislation][13] requires explicit consent from users to send them marketing-related messages. Other countries may make similar legislative moves, so acquiring that explicit consent from your users should be a priority. Not having a double opt-in system in place now may leave you with time-consuming migration to a compliant system in the future.

Creating an opt-in prompt that clearly lists and demonstrates the benefits of push can only help you, given the evolving attitudes of both consumers and governments toward push messaging. Instead of ambushing your users with a permission request when they open the app for the first time, explain the benefits of your push messages and THEN ask for permission.

![Breaking News 1][16]

![Breaking News 2][17]

Adding a simple pop-up to prompt user action can allow you to effectively request permission from your users more than once, if needed. Relying on iOS's permission request alone means that most users will never think twice about enabling your push messages.

For example, the Fandango app has a pop-up that states the benefits of enabling push notifications in a clear and concise manner. After receiving this notification, users have enough information to decide if they will find Fandango's pushes valuable and can act accordingly.

![fandango_prompt][37]

Another example of an app that does a great job with custom opt-in prompts is textPlus. Upon downloading textPlus, a user receives a pop-up prompt that explains the benefits of push notifications and walks the user through the process of enabling them.

![textplus_prompt][24]

After the user clicks "Next," the user receives the real iOS push prompt. If the user doesn't enable push notifications at this stage, then he will have to enable them in Settings. textPlus makes this easier for users to do by featuring a reminder on their Inbox page.

![textplus_reminder][25]

If users click "Turn on," they are presented with detailed steps for how to enable push notifications. This removes some of the effort involved in turning on push notifications

![textplus_directions][26]

Another app that does a wonderful job of priming its' users to accept push notifications is Hopper. See their [Medium article][49] on how to best onboard when it comes to push.

> If you've implemented a custom push prompt as described above in an iOS app, make sure that you're [reregistering with APNs][44] every time the app runs after they grant push permissions to your app. Apple advises this as [device tokens can change arbitrarily][45].

Additional information on managing user subscriptions is available [here][36].

[13]: {{site.baseurl}}/help/best_practices/spam_regulations/#can-spam
[16]: {% image_buster /assets/img_archive/bn_push1.png %}
[17]: {% image_buster /assets/img_archive/bn_push2.png %}
[24]: {% image_buster /assets/img_archive/textplus_prompt.png %}
[25]: {% image_buster /assets/img_archive/textplus_reminder.png %}
[26]: {% image_buster /assets/img_archive/textplus_directions.png %}
[36]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[37]: {% image_buster /assets/img_archive/PushPrimeFandango.png %}
[44]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/
[45]: https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html
[46]:{% image_buster /assets/img_archive/Push_Window8_Toast.png %}
[47]:{% image_buster /assets/img_archive/Push_Windows_Universal_Toast.png %}
[49]: https://medium.com/@hopper_travel/the-notification-problem-50267cbabad2#.auax13q52
