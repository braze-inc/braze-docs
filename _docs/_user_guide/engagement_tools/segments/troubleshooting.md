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

## Errors

### Target audience is too complex to launch

This rare error occurs if your target audience contains too many regex values, excessively long regex values, excessively detailed filters (such as "is any of 30,000 zip codes"), or too many filters. This includes all filters in a campaign or Canvas audience, whether the filters are located within the referenced segments or added as filters in the **Target Audience** step.

![Error for a target audience that hits the complexity threshold.]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

When you add segment filters to a campaign or Canvas, those filters are translated into queries in Braze (the character count of these queries is not 1:1 to the number of characters a dashboard user sees). When Braze sends a campaign or Canvas, we run a query that combines all filters in the targeted audience. We apply a threshold limiting the number of characters in the resulting query for a target audience. For a given campaign or Canvas, we sum up the character count across all segments referenced, including all additional filters. For a given segment, we sum up the character count across all filters and filter values.

Your dashboard will display an error when a campaign, Canvas, or segment exceeds the threshold and can't be launched. If you receive this error, simplify your target audience before launching again, including:

- If your audience references multiple segments, make sure the segments don't have redundancies, such as the same filters appearing in multiple segments.
- Make sure you aren't referencing outdated data in segment filters. For example, an outdated filter might look for users who haven't received a certain Canvas step in the past week, even though the Canvas has been stopped for months.
- Segments that are just lists of user IDs or emails (which often use a regex filter) can be converted to a [CSV import]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) and be simplified into a single CSV filter.
- If you have CDI, you may be able to create a CDI segment that pulls the group directly from your data warehouse.

You can also [contact Support]({{site.baseurl}}/braze_support/) for further assistance with filter optimization.

{% alert note %}
We began limiting character counts in April 2025. Campaigns and Canvases that launched before April 2025 were grandfathered, which means they can continue exceeding the limit, whereas newly created campaigns and Canvases can't exceed the limit. If you edit or clone a grandfathered campaign or Canvas, you **will not** be able to launch it until the audience is updated to be below the limit.
{% endalert %}

### X active or stopped campaigns or Canvases exceed the audience complexity threshold

This banner displays at the top of a campaign or Canvas list whenever active or stopped campaigns or Canvases have audiences that exceed the audience complexity threshold. Select the banner to filter the list to just the campaigns or Canvases exceeding the threshold, then follow the troubleshooting steps in [Target audience is too complex to launch](#target-audience-is-too-complex-to-launch).

![Error banner that says 4 active or stopped Canvases exceed the audience complexity threshold.]({% image_buster /assets/img/segment/audience_complexity_threshold_banner.png %})

### Filter exceeds 10,000 bytes or is too long to save

Braze limits individual segment filters to a maximum of 10,000 bytes, which is equivalent to 10,000 English characters or 3,333 Japanese characters. A warning appears whenever an individual filter exceeds 10,000 bytes, whether the filter is within a segment or added directly to campaign or Canvas. 

![Error banner for a filter that has a value that exceeds 10,000 characters.]({% image_buster /assets/img/segment/filter_error.png %})

![Error for a custom attribute filter, `menu_item`, which has an attribute value that exceeds 10,000 characters.]({% image_buster /assets/img/segment/segment_filter_error.png %})


This error occurs very rarely, but when it does occur, it’s typically with regex filters that target a list of user IDs or email addresses. In that case, you can follow these steps to convert the filters to a CSV:

1. Export the users from the affected segment or the specific regex filter. 
2. Clean the CSV as needed. You need either Braze ID or Appboy ID, but you can remove all other columns if they aren't needed. We also recommend reviewing your data to confirm it’s recent (for example, remove users who you're no longer trying to target).
3. [Import]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) the CSV file again, which automatically groups the users into a single, highly efficient CSV-based filter.

## User behavior

### User is no longer in a segment

If a user isn’t available while creating a segment, their user data that determines their segment eligibility might have changed as a result of their own activity or other campaigns and Canvases they’ve interacted with previously. If re-eligibility is turned on, their user profile will show the latest data of the received campaign.

### Info displays for users of other apps when I filter for a specific app

Users can have multiple apps, so selecting a specific app in the **Apps Used** section of the segmentation page will yield results for users who at least have that app. The filter does not yield results for the users who exclusively have that app.

## Filtering

### Filter options changed

Your filter options are related to the format (data type) that you're passing to Braze for your custom attribute. To review the data type that Braze is recognizing for your custom attributes, navigate to **Data Settings** > **Custom Attributes**.

If your filter options have changed, this is an indication that your data is being passed to Braze in a different format (data type) than before. For detailed descriptions of different data types and their filtering options, refer to [custom attribute data types]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes#custom-attribute-data-types).

Keep in mind that changing the data type of a custom attribute in the dashboard will reject data that is sent to Braze in a different format.

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
