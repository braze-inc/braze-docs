---
nav_title: Platform Targeting
page_order: 8
description: "Liquid use cases based on platform, such as Web, iOS, Android, or device version."
---

# Platform Targeting

Here are some examples of how you can use Liquid to target users when they're on a specific platform:

## Differentiate In-App Message Copy by Device OS

**Goal:** Show mobile users shorter versions of message copy, while showing other users the regular, longer version of copy.

{% raw %}

```liquid
{% if targeted_device.${platform} == "ios" or targeted_device.${platform} == "android" %}
This is a shorter copy.

{% else % %}
This is the regular copy and much longer than the short version. 
{% endif %}
```

{% endraw %}

## Personalize In-App Message Copy for Mobile vs Web

**Goal:** Show mobile users certain messaging that is relevant to them, but wouldn't be relevant to Web users. For example, iOS messaging might talk about Apple Pay, but Android messaging should mention Google Pay.

{% raw %}

```liquid
{% if targeted_device.${platform} == "ios" or targeted_device.${platform} == "android" %}
Take a picture with your phone

{% else %}
Grab your phone and start taking pictures
{% endif %}
```

{% endraw %}

{% alert note %} Liquid is case-sensitive, `targeted_device.${platform}` returns the value in all lowercase. {% endalert %}

## Target Only Mobile Web Users

**Goal:** Target web users only when they are on their iOS or Android device.

{% raw %}

```liquid
{% if targeted_device.${platform} == "ios" or targeted_device.${platform} == "android" %}
```

{% endraw %}

## Target Only a Specific Platform

**Goal:** Target users on a specific platform, such as only sending a message to Android users. This can be used as an alternative to selecting an app within the Segmentation tool.

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

**Goal:** Target users who have a device with a specific operating system version. The example used sends a warning to users on iOS 10.0 or below that they are phasing out support for the user's device OS.

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

**Goal:** Target users who are on a web browser through Windows or Mac OS.

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

**Goal:** Target a specific mobile carrier. For push notifications and in-app message channels, you can specify the device carrier in your message body using Liquid. If the recipient's device carrier doesn't match, the message won't send.

{% raw %}

```liquid
{%if {targeted_device.${carrier}} contains "verizon" or {targeted_device.${carrier}} contains "Verizon" %}

This is a message for Verizon users!

{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}
