---
nav_title: Slideups
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 2
---
# Slideup In-App Messages

Our slideups typically appear at the top or bottom of the app screen (you can set this when you create your message). These are great for alerting your users about new terms of service, cookies, and other snippets of information. These are non-obtrusive and allow your end users to continue to interact with your app while the message displays.

<br>

![Slideup Specs][2a]{: style="max-width: 50%; border: none;"}

<br>

| Element | Specification | Details |
|---|---|---|
| Slideup Size | 450px Maximum Width | 3-Line maximum height, at which point the message is truncated with an ellipsis. |
| Image/Icon Size | 50px by 50px | These images are optional, but always appear on the left side of the message. |
| Copy | 14px - Bolded | Three lines of text will appear before being truncated with an ellipsis. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Slideup Viewport

On a tablet or desktop browser, a slideup in-app message will sit in the corner of the app screen as shown below (unless designated otherwise when creating the in-app message).

<br>
![Slideup Viewport][2b]{: style="max-width: 80%; border: none;"}

<br>

## Image and Copy Behavior

Slideup messages can contain up to three lines of copy before truncation with ellipses. Images in slideups will never be cropped or clipped - they will always scale down to fit within the 50X50 image container.

- __All images must be less than 5MB.__
- We only accept `PNG`, `JPG`, and `GIF` file types.
- We recommend that your images be 500KB.

You should __always__ [preview and test your messages]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/testing/) on a variety of devices to ensure that the most important areas of your image and message appear as expected.

[2a]: {% image_buster /assets/img/slideup-spec.png %}
[2b]: {% image_buster /assets/img/slideup-large-viewport2.png %}
