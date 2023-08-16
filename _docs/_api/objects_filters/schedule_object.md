---
nav_title: "Schedule Object"
article_title: API Schedule Object
page_order: 12
page_type: reference
description: "This reference article lists and explains the different scheduling object used at Braze."

---

# Schedule object

> The parameters for the campaign and Canvas schedule creation endpoints mirror those of the sending endpoint and add the `schedule` parameter, which allows you to specify when you want your targeted users to receive your message. If you include only the `time` parameter in the `schedule` object, all of your users will be messaged at that time.

If you set `in_local_time` to be `true`, you will get an error response if the time parameter has passed in all time zones. If you set `at_optimal_time` to be true, your users will receive the message at the designated date at the [optimal time][33] for them (regardless of the time you provide). When using local or optimal time sending, do not provide time zone designators in the value of the time parameter (e.g., just give us `"2015-02-20T13:14:47"` instead of `"2015-02-20T13:14:47-05:00"`).

The response will provide you with a `schedule_id` that you should save in case you later need to cancel or update the message you schedule:

## Object body

Insert this object as needed to schedule your messages.

```json
"schedule": {
  "time": (required, datetime as ISO 8601 string) time to send the message,
  "in_local_time": (optional, bool),
  "at_optimal_time": (optional, bool),
}
```

## Schedule ID response

You will receive a `schedule_id` for the scheduled message you created.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "schedule_id" : (required, string) identifier for the scheduled message that was created
}
```

Customers using the API for server-to-server calls may need to whitelist the appropriate API URL if they're behind a firewall.

Message scheduling endpoint responses will include the message's `dispatch_id` for reference back to the dispatch of the message. The `dispatch_id` is the id of the message dispatch (unique id for each 'transmission' sent from the Braze platform).

[33]: {{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_timing/
