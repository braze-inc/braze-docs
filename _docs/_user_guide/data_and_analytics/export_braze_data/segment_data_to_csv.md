---
nav_title: Export Segment Data to CSV
page_order: 2

page_type: reference
description: "This reference article covers how to export segment data to CSV."
---

# Exporting to CSV

To request a CSV export of user data from a segment, click on the "User Data" button on the top-right side while editing a segment:

![csvexport][1]

You can also request a CSV export from the main Segments page by clicking the gear icon on the right side to access this dropdown menu:

![csvexport2][2]

The CSV output contains the data from each user profile captured in the segment at the time of export. You can export any segment by clicking the gear icon and CSV export. Braze will generate the report in the background and email it to the user who is currently logged in.

{% alert important %} 
Due to file size restrictions, your export may fail if your segment is too large (over 500,000 users). Consider using [random bucket numbers]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) to break your user base into multiple segments, and then combine them after export. For example, if you need to break up your segment into 2 different segments, you can do so with the following filters:

- Segment 1: Random bucket number is less than 5000 (includes 0-4999)
- Segment 2: Random bucket number is more than 4999 (includes 5000-9999)

{% endalert %}

If you have [linked your Amazon S3 credentials to Braze][26], then the CSV will instead be uploaded in your S3 bucket under the key `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`. The link emailed to you will expire after 1 day of exporting and requires that you are logged into the dashboard to access it.

Data included in the exports:

- All User Data
    - User ID
    - First Name
    - Last Name
    - Timezone
    - City
    - Gender
    - Email Address
    - Phone Number
    - Number of Push Tokens
    - Twitter Username
    - Session Count
    - First Session
    - Last Session
    - Last App Version Used
    - In-App Purchase Total
    - Email Unsubscribe Time 
    - Device Info
    - Number of IDFAs
    - Number of IDFVs
    - Custom Events
    - Custom Attributes
- Email Addresses
    - User ID
    - First Name
    - Last Name
    - Email Address
    - Email Unsubscribe Date
    - Email Opt-in Date

{% alert tip %}
For help with CSV and API exports, visit our troubleshooting article [here]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

[1]: {% image_buster /assets/img_archive/csvexport.png %}
[2]: {% image_buster /assets/img_archive/csvexport2.png %}
[26]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration
