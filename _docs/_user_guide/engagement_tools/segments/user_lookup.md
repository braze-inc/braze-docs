---
nav_title: User Lookup
article_title: User Lookup
page_order: 5.5
page_type: reference
description: "This reference article describes how to user user lookup to confirm if a user matches a specific segment or filter."
---

# User lookup

When setting up your audience for a campaign or Canvas, you can search for a specific user directly from the composer to test if your filters and segments are set up correctly. This can also be helpful when troubleshooting a campaign or Canvas that isn't sending as expected—for example, if users aren't receiving a message when they should be.

User lookup is available when:

- Creating a segment
- Setting up a campaign or Canvas audience
- Setting up an Audience Paths step

![User Lookup feature when building an audience.][1]{: style="max-width:60%"}

To check if a user matches the audience criteria, click **Lookup User** and search for a user's `external_id` or `braze_id`.

## Results

When a user matches the segment, filter, and app criteria, you see the following:

![User Lookup results that read "user007 matches all of the segments, filters, and apps."][2]{: style="max-width:60%"}

When a user doesn't match part or all of the segment, filter, or app critieria, the missing criteria is listed for troubleshooting purposes.

![User Lookup results that read "user1234 does not match the following targeting criteria" with two segments listed in a table.][3]{: style="max-width:60%"}


[1]: {% image_buster /assets/img_archive/user_lookup.png %}
[2]: {% image_buster /assets/img_archive/user_lookup_match.png %}
[3]: {% image_buster /assets/img_archive/user_lookup_nomatch.png %}