---
nav_title: Canvas Persistent Entry Properties
title: Canvas Persistent Entry Properties
description: ""
permalink: "/persistent_entry/"
hidden: true
---

# Canvas Persistent Entry Properties

By utilizing the new persistent entry properties functionality in Canvas, customers can achieve sophisticated use cases that were previously either impossible or time-consuming, complex workarounds.

When a Canvas is triggered by a custom event or an API call, customers will now be able to use metadata from the API call or custom event for personalization in each step of the Canvas. __Prior to this change, the entry properties could only be used in the first step of Canvas.__ Being able to retain entry properties for the duration of a Canvas will allow customers to send more curated messages to their users, thereby resulting in a highly refined end-user experience.

Note: Persistent entry properties are currently only available on API-Triggered Canvases. The Beta release will support every channel except in-app messages. Support for in-app messages and Action-based campaigns will be included in future releases.

Entry properties are defined when you send a Canvas message via the API, which you can find more information about in our documentation. 

Braze will begin saving the values associated with those properties once a liquid snippet for personalization has been defined in the message.

If an active Canvas is edited to include a new entry property, the Canvas corresponding to that property will not be available for users who entered the Canvas before the entry property key was added to the Canvas. The values will only be saved for users that enter the Canvas ager the change is made. 

For example, in the case that a Canvas entry property is null or blank, you can abort messages using conditionals. The following code snippet is an example of how you may use Liquid to abort a message.

{% raw %}
```liquid
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

## Use Cases

If you have a Canvas that is triggered when a user browses an item in your e-commerce site but does not add it to their cart, the first step of the Canvas might be a push notification asking if they are interested in purchasing the item. You could reference the product name by using {{Canvas_entry_properties.$(product_name)}}

![Image][1]{: style="border:0;margin-left:15px;"}

The second step may send another push notification prompting the user to checkout if they added the item to their cart but have not purchased it yet. You can continue to reference the product_name entry property by using {{Canvas_entry_properties.$(product_name)}}.

![Image][2]{: style="border:0;margin-left:15px;"}

[1]:{% image_buster /assets/img/persistent_entry_properties/PEP1.png %}
[2]:{% image_buster /assets/img/persistent_entry_properties/PEP12.png %}
