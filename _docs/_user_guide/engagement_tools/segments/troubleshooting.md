---
nav_title: Troubleshooting
article_title: Troubleshooting Segments
page_order: 12
page_type: reference
tool: 
  - Segments
description: "This reference article covers troubleshooting steps and considerations to keep in mind while using segments."
---

# Troubleshooting segments

## User behavior

### User is no longer in a segment

If a user isn’t available while creating a segment, their user data that determines their segment eligibility might have changed as a result of their own activity or other campaigns and Canvases they’ve interacted with previously. If re-eligibility is turned on, their user profile will show the latest data of the received campaign.

### Info displays for users of other apps when I filter for a specific app

Users can have multiple apps, so selecting a specific app in the **Apps Used** section of the segmentation page will yield results for users who at least have that app. The filter does not yield results for the users who exclusively have that app.

## Analytics and reporting

### *Message Sent* or *Unique Recipients* in Campaign Analytics doesn't match segment count 

If your campaign analytics count for *Message Sent* or *Unique Recipients* doesn't match the number of users in the segment filter `Has received message from campaign X`, there could be two possible reasons why:

1. **Users may have been archived, orphaned, or deleted since the campaign launch**<br><br>For example, let’s say 1,000 users receive a campaign and you make a CSV export the same day. You’ll see 1,000 users reported. Over the next month, 50 of those 1,000 users are deleted (for example, by the `users/delete` endpoint). When you make another CSV export, you’ll see 950 users reported while the *Unique Recipient* count in **Campaign Analytics** is still 1,000.<br><br>In other words, the *Unique Recipients* metric is an incremented count, while the segmenter and CSV export provide a count of currently existing users.<br><br>

2. **The campaign has re-eligibility set, so users can re-enter the campaign multiple times**<br><br>For example, let’s say an email campaign has re-eligibility set to zero minutes (users can re-enter the campaign as long as they meet the audience segment requirements), and the campaign has been running for over a month. The *Messages Sent* number in **Campaign Analytics** wouldn’t match the number in the segment because this field would include messages sent to duplicate users.<br><br>This is because Braze counts unique users as *Unique Daily Recipients*, or the number of users who received a particular message in a day. This means that re-eligible users will be counted more than once as a unique recipient because the "unique” window only lasts a day. This can result in the number of *Unique Daily Recipients* being higher than the number of user profiles in the CSV export. The user profiles in the CSV file will be truly unique.

### User is assigned to two apps despite logging a session in only one app

When creating a segment, you can target users that have [used specific apps]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform). A user needs to have had a session in a specific app to be assigned to that app; however, there are two scenarios where a user can still be assigned to a specific app without having logged sessions in the app. 

The first scenario is if the `app_id` field is populated when using the `/users/track` endpoint—specifically when using an [event]({{site.baseurl}}/api/objects_filters/event_object/) or [purchase object]({{site.baseurl}}/api/objects_filters/purchase_object/), such as in this example:

```json
{
    "events": [
    {
      "external_id": "john_doe123",
      "app_id": "my_web_app_id",
      "name": "Custom Event",
      "time": "2025-08-17T19:20:30+1:00"
    }
  ]
}
```

The second scenario is if the `app_id` field is populated when using the `/users/track` endpoint to migrate push tickets, such as in this example: 

```json
"app_group_id": "{YOUR_APP_GROUP_ID}",
"attributes": [
{
      "push_token_import": false,
      "external_id": "external_id1",
      "country": "US",
      "language": "en",
      "{YOUR_CUSTOM_ATTRIBUTE}": "{YOUR_VALUE}",
      "push_tokens": [
        {"app_id": "{APP_ID_OF_OS}", "token": "{PUSH_TOKEN_STRING}"}
      ]
  }
]
```
## Errors

### Target audience is too complex to launch

This rare error occurs if your target audience contains too many regex values, excessively long regex values, or too many filters. This includes all filters in a campaign or Canvas audience, whether the filters are located within the referenced segments or added as filters in the **Target Audience** step.

If you receive this error, simplify your target audience before launching again, including:

- If your audience references multiple segments, make sure the segments don't have redundancies, such as the same filters appearing in multiple segments.
- Make sure you aren't referencing outdated data in segment filters. For example, an outdated filter might look for users who haven't received a certain Canvas step in the past week, even though the Canvas has been stopped for months.

You can also [contact Support]({{site.baseurl}}/braze_support/) for further assistance with filter optimization.
