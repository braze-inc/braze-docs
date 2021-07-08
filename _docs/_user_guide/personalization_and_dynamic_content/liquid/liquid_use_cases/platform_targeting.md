---
nav_title: Platform Targeting
page_order: 8

page_type: reference
description: "This reference article lists Liquid use cases based on platform, such as Web, iOS, Android, or device version."
---

# Platform Targeting

Here are some examples of how you can use Liquid to target users when they're on a specific platform:

## Differentiate In-App Message Copy by Device OS

This use case checks what platform a user is on, and depending on their platform, will display specific messaging.

For example, you may want to show mobile users shorter versions of message copy, while showing other users the regular, longer version of copy. You could also show mobile users certain messaging that is relevant to them, but wouldn’t be relevant to Web users. For example, iOS messaging might talk about Apple Pay, but Android messaging should mention Google Pay.

{% raw %}

```liquid
{% if targeted_device.${platform} == "ios" or targeted_device.${platform} == "android" %}
This is a shorter copy.

{% else % %}
This is the regular copy and much longer than the short version. 
{% endif %}
```

{% endraw %}

{% alert note %} Liquid is case-sensitive, `targeted_device.${platform}` returns the value in all lowercase. {% endalert %}

## Target Only a Specific Platform

This use case will capture the users device platform, and depending on the platform, will display a message.

For example, you may want to only send a message to Android users. This can be used as an alternative to selecting an app within the Segmentation tool.

{% raw %}

```liquid
{% if {{targeted_device.${platform}}} == 'android' %} 

This is a message for an Android user! 

{% else %}  
{% abort_message %] 
{% endif %}
```

{% endraw %}

## Target Only iOS Devices with a Specific OS Version

This use case checks if a user's OS version falls within a certain set, and if so, will display a specific message.

The example used sends a warning to users on iOS 10.0 or below that they are phasing out support for the user’s device OS.

{% raw %}

```liquid
{% if {{targeted_device.${os}}} == "10.0" or {{targeted_device.${os}}} == "10.0.1" or {{targeted_device.${os}}} == "10.0.2" or {{targeted_device.${os}}} == “10.0.3” or {{targeted_device.${os}}} == “10.1” or {{targeted_device.${os}}} == “10.2” or {{targeted_device.${os}}} == “10.2.1” or {{targeted_device.${os}}} == “10.3” or {{targeted_device.${os}}} == “10.3.1” or {{targeted_device.${os}}} == “10.3.2” or {{targeted_device.${os}}} == “10.3.3” or {{targeted_device.${os}}} == “10.3.4” or {{targeted_device.${os}}} == “9.3.1” or {{targeted_device.${os}}} == “9.3.2” or {{targeted_device.${os}}} == “9.3.3” or {{targeted_device.${os}}} == “9.3.4” or {{targeted_device.${os}}} == "9.3.5" %}

We are phasing out support for your device's operating system. Be sure to update to the latest software for the best app experience.

{% else%}
{% abort_message%}
{% endif %}
```

{% endraw %}

## Target Only Web Browsers

This use case checks if a user's target device runs on Mac or Windows, and if so, will display a specific message.

{% raw %}

```liquid
{% if {{targeted_device.${os}}} == 'Mac' OR {{targeted_device.${os}}} == 'Windows' %}

This message will display on your desktop web browser.

{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

## Target a Specific Mobile Carrier

This use case checks if a user's device carrier is Verizon, and if so, will display a specific message.

For push notifications and in-app message channels, you can specify the device carrier in your message body using Liquid. If the recipient’s device carrier doesn’t match, the message won’t be sent.

{% raw %}

```liquid
{%if {targeted_device.${carrier}} contains "verizon" or {targeted_device.${carrier}} contains "Verizon" %}

This is a message for Verizon users!

{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}
