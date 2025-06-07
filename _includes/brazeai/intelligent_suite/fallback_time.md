You can choose one of the following options:

- **Most popular:** This is the most popular time your app is used among all users.
- **Custom:** This is a custom fallback of your choice. The message will be delivered based on each individual user's local time zone.

{% subtabs local %}
{% subtab most popular %}
The most popular app time is determined by the average session start time for your workspace (in local time). This time is displayed in red on the preview chart.

In the unlikely event that your app doesn't have enough session data to calculate when the app is most used (a completely new app with no data), the message will send at 5 pm in the user's local time zone. If the user's local time is unknown, it will send at 5 pm in your company time zone.

It's important to be aware of the limitations of using Intelligent Timing early in a user's lifecycle when limited data is available. It can still be valuable, as even users with few recorded sessions can offer insights into their behavior. However, Braze can more effectively calculate the optimal send time later in a user's lifecycle.

{% if include.type == "campaigns" %}
{% alert note %}
For campaigns, if you specified a [delivery window](#sending-within-specific-hours) and the most popular time to use your app falls outside of that window, the message will send closest to the edge of the delivery window. For example, if your delivery window is 1 pm to 8 pm and the most popular app time is 10 pm, the message will send at 8 pm.
{% endalert %}
{% endif %}
{% endsubtab %}

{% subtab custom %}
Use the custom fallback time to choose a different time to send the message. Similar to the most popular app time, the message will send at the fallback time in the user's local time zone. If the user's local time zone is unknown, it will send in your company time zone.

For campaigns with a custom fallback time specified, if you launch the campaign within 24 hours of the send date, users whose optimal times have already passed will receive the campaign at the custom fallback time. If the custom fallback time has already passed in their time zone, the message will send immediately.
{% endsubtab %}
{% endsubtabs %}