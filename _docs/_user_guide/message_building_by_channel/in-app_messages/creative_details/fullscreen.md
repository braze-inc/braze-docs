---
nav_title: Full-Screen
platform: Message_Building_and_Personalization
subplatform: In-App Messages
page_order: 0
---
# Full-Screen In-App Messages

Full-screen messages take up the whole screen of the device! This message type is great when you really need your user's attention, like for mandatory app updates.

<br>

![Full-Screen Specs][3a]{: style="max-width: 80%; border: none;"}

<br>

| Element | Specification | Details |
|---|---|---|
| Text & Image - Image Size | 5:4 Aspect Ratio <br> 450px by 360px Image Container | Accepts high resolution, PNG, JPEG, GIF. |
| Image Only - Image Size | 10:16 Aspect Ratio <br> 450px by 720px Image Container | Accepts high resolution, PNG, JPEG, GIF. |
| Copy | 20px Header Text - Bolded <br> 14px Message Text - Regular Weight | We cannot recommend character or word limits.|
| Primary & Secondary Action Buttons | Secondary on the Left <br> Primary on the Right | We recommend contrasting your buttons to present the desired choice to the user with the right button, designating it as the Primary Action. |

## Full-Screen Viewport

On a tablet or desktop browser, a full-screen in-app message will sit in the center of the app screen as shown below.

<br>
![Full-Screen Viewport][3b]{: style="max-width: 80%; border: none;"}
<br>

## Image Behavior

Full-screen in-app messages (with text) will fill the entire height of a device and stay true to aspect ratio. Image only full-screen messages will fill the entire height of a device and crop horizontally (left and right sides) as needed.

- __All images must be less than 5MB.__
- We only accept `PNG`, `JPG`, and `GIF` file types.
- We recommend that your images be 500KB.

You should __always__ [preview and test your messages]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/testing/) on a variety of devices to ensure that the most important areas of your image and message appear as expected.

### Notch Support

Notched mobile devices, where parts of the screen are blocked to hold camera or speaker ports, often distort the look and expansion of in-app messages. This can result in odd overlays or distortion from status bars situated on either side of the notch.

In August 2019, Braze introduced improved support for notched devices. With this new behavior, our in-app messages will consider notches when expanding and filling a device. Where some fullscreen in-app messages will stop at the bottom limit of the notch and allow view of the status bar, our fullscreen messages will fill the notched negative spaces, including the status bar, and provide a fully immersive experience in your message.

[3a]: {% image_buster /assets/img/full-screen-spec-notched.png %}
[3b]: {% image_buster /assets/img/full-screen-large-viewport.png %}
