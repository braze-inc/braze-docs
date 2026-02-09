---
nav_title: "Schedule object"
article_title: API Schedule Object
page_order: 12
page_type: reference
description: "This reference article lists and explains the different scheduling object used at Braze."

---

# Schedule object

> The parameters for the campaign and Canvas schedule creation endpoints mirror those of the sending endpoint and add the `schedule` parameter, which allows you to specify when you want your targeted users to receive your message. If you include only the `time` parameter in the `schedule` object, Braze messages all of your users at that time.

If you set `in_local_time` to be `true`, you get an error response if the time parameter has passed in all time zones. If you set `at_optimal_time` to be true, your users receive the message at the designated date at the optimal time (regardless of the time you provide). When using local or optimal time sending, do not provide time zone designators in the value of the time parameter (for example, use `"2015-02-20T13:14:47"` instead of `"2015-02-20T13:14:47-05:00"`).

The response provides you with a `schedule_id` that you should save in case you later need to cancel or update the message you schedule:

## Object body

Insert this object as needed to schedule your messages.

```json
"schedule": {
  "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
  "in_local_time": (optional, bool),
  "at_optimal_time": (optional, bool),
}
```

## Schedule ID response

You receive a `schedule_id` for the scheduled message you created.

```json
{
  "schedule_id" : (required, string) identifier for the scheduled message you created
}
```

If you use the API for server-to-server calls, you may need to allowlist the appropriate API URL if they're behind a firewall.

Message scheduling endpoint responses include the message's `dispatch_id` for reference back to the dispatch of the message. The `dispatch_id` is the ID of the message dispatch (unique ID for each 'transmission' sent from Braze).