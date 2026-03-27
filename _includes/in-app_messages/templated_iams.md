In-app messages are delivered as templated in-app messages when **Re-evaluate campaign eligibility before displaying** is selected or if any of the following Liquid tags exist in the message:

- `canvas_entry_properties`
- `connected_content`
- SMS variables such as {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

This means that during session start, the device will receive the trigger of that in-app message instead of the entire message. When the user triggers the in-app message, the user's device will make a network request to fetch the actual message.

{% alert note %}
The message will not be delivered if the device doesn't have access to the internet. The message might not be delivered if the Liquid logic takes too long to resolve.
{% endalert %}