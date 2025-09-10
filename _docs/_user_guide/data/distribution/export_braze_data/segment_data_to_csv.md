---
nav_title: Export segment data to CSV
article_title: Export Segment Data to CSV
page_order: 2
page_type: reference
description: "This reference article covers how to export segment data to CSV."

---

# Exporting segment data to CSV

> This page covers how to request a CSV export of user data from a segment, and the data included in the export.

To export segment data to a CSV, select the **User Data** dropdown while editing a segment and select to export either the user data or email addresses for the segment.

![Segment Details section with User Data dropdown showing export options.]({% image_buster /assets/img_archive/csvexport.png %})

You can also request a CSV export from the main **Segments** page by selecting the <i class="fas fa-gear"></i> **Settings** dropdown for a segment:

![Settings dropdown on the main Segments page.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
To export data from all your user profiles, create a segment with no filters, and then request a CSV export.
{% endalert %}

The CSV output contains the data from each user profile captured in the segment at the time of export. You can export any segment by selecting the gear icon and CSV export. Braze will generate the report in the background and email it to the user who is currently logged in.

{% alert important %} 
Due to file size restrictions, your export may fail if the estimated size of your segment is over 500,000 users. Note that this restriction uses the estimated size of your segment, and not the exact calculation. For more details, see [Exporting large segments]({{site.baseurl}}/help/help_articles/segments/exporting_large_segments/).
{% endalert %}

If you've linked your [Amazon S3 credentials]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration) to Braze, the CSV will instead be uploaded in your S3 bucket under the key `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`. You must be logged into the dashboard to access the download link emailed to you.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## Data included in export

The following is included in your export depending on your selection.

### CSV Export User Data

| Field Name                  | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | Internal ID (cannot be changed)                           |
| country                     | Country                                    |
| created_at                  | Date and time when the user profile was created                   |
| devices                     | Device information                           |
| date_of_birth               | Date of birth                                            |
| email                       | Email address                                            |
| unsubscribed_from_emails_at | Date unsubscribed from emails                            |
| user_id                     | External ID                                              |
| first_name                  | First name                                               |
| first_session               | Date and time of first session                           |
| gender                      | Gender                                                   |
| google_ad_ids               | Google advertising IDs associated with the user                      |
| city                        | City                                     |
| IDFAs                       | Identifier for Advertising (IDFA) values                 |
| IDFVs                       | Identifier for Vendor (IDFV) values                      |
| language                    | Language in ISO-639-1 standard                                        |
| last_app_version_used       | Last version of the app used                             |
| last_name                   | Last name                                                |
| last_session                | Date and time of last session                            |
| number_of_google_ad_ids     | Count of associated Google advertising IDs               |
| number_of_IDFAs             | Count of associated IDFAs                                |
| number_of_IDFVs             | Count of associated IDFVs                                |
| number_of_push_tokens       | Count of associated push notification tokens             |
| number_of_roku_ad_ids       | Count of associated Roku advertising IDs                 |
| number_of_windows_ad_ids    | Count of associated Windows advertising IDs              |
| phone_number                | Phone number                                             |
| opted_into_push_at          | Date opted into push notifications                       |
| unsubscribed_from_push_at   | Date unsubscribed from push notifications                |
| random_bucket               | Random bucket number                                 |
| roku_ad_ids                 | Roku advertising IDs                          |
| session_count               | Total number of sessions                                 |
| timezone                    | User's time zone in the same format as the IANA Time Zone Database                                         |
| in_app_purchase_total       | Total amount spent on in-app purchases                   |
| user_aliases                | User aliases, if any                                          |
| windows_ad_ids              | Windows advertising IDs                       |
| Custom events               | Based on selection at export                             |
| Custom attributes           | Based on selection at export                             |
{: .reset-td-br-1 .reset-td-br-2 }

### CSV Export Email Addresses

| Field Name                  | Description            |
| --------------------------- | ---------------------- |
| user_id                     | User's external ID     |
| first_name                  | First name             |
| last_name                   | Last name              |
| email                       | Email                  |
| unsubscribed_from_emails_at | Email unsubscribe date |
| opted_in_to_emails_at       | Email opt-in date      |
| user_aliases                | User aliases, if any   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
For help with CSV and API exports, visit our [troubleshooting]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/) article.
{% endalert %} 

