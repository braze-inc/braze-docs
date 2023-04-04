---
nav_title: In-App Messages
article_title: In-App Messages for tvOS
platform: tvOS
page_type: reference
description: "This reference article covers in-app messaging integration guidelines for the tvOS platform."
page_order: 3
---

# In-app messages and Content Cards on tvOS

{% alert note %}
In-app message and Content Card support on tvOS is only available using our Swift SDK.
{% endalert %}

On tvOS, you can execute messaging on both in-app message and Content Card channels by integrating the [Braze Swift SDK][swift-sdk]. After adding the Braze SDK to your Xcode project for your tvOS app, note the following details during your configuration:

**1\.** Create a new iOS app under **Manage Settings** in the Braze dashboard for your tvOS app.<br>![][1]{: style="width:70%"}<br>
{% alert warning %}
Do not choose tvOS from the checkbox list; doing so will prohibit you from leveraging Content Cards or in-app messages.
{% endalert %}

**2\.** Use the API key listed in **Manage Settings** when referencing the API key during your SDK configuration in your Xcode project.<br>![][2]{: style="width:70%"}

## Customization

Braze provided user interface libraries are not available for tvOS and have to be created and managed outside of Braze.
