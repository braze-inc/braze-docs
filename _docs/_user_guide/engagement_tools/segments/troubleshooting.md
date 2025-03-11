---
nav_title: Troubleshooting
article_title: Troubleshooting Segments
page_order: 10
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