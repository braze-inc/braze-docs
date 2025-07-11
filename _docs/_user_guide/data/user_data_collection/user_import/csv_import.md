---
nav_title: CSV Import
article_title: "ARTICLE_TITLE"
description: "SHORT_DESCRIPTION."
page_order: 1.2
---

# CSV import

> Learn how to...

## About CSV import

You can use CSV import to record and update both user attributes and custom events.

|Type|Definition|Example|Maximum file size|
|---|---|---|---|
|Default Attributes|Reserved user attributes recognized by Braze.|`first_name`, `email`|500 MB|
|Custom Attributes|User attributes unique to your business.|`last_destination_searched`|500 MB|
|Custom Events|Events unique to your business that represent user actions.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Data point considerations

Each piece of customer data imported from a CSV file will overwrite the existing value on user profiles and count as a data point, except for external IDs and blank values.

- External IDs uploaded from a CSV file will not consume data points. If you are uploading a CSV to segment existing Braze users by uploading only external IDs, this can be done without consuming data points. If you were to add additional data like user emails or phone numbers in your import, that would overwrite existing user data, consuming your data points.  
  - CSV imports for segmentation purposes (imports made with `external_id`, `braze_id`, or `user_alias_name` as the only field) will not consume data points.  
- Blank values will not overwrite existing values on the user profile, and you do not need to include all existing user attributes or custom events in your CSV file.  
- Updating `email_subscribe`, `push_subscribe`, `subscription_group_id`, or `subscription_state` will not count toward data point consumption.

{% alert important %}
Setting `language` or `country` on a user through CSV import or API will prevent Braze from automatically capturing this information through the SDK.
{% endalert %}

## Using CSV import

### Step 1: Open CSV import

To open CSV import, go to **Audiences** > **User Import**. Here, you'll find a table that lists the most recent imports, which includes details such as the upload date, the uploader's name, file name, targeting availability, number of imported rows, and status of each import.

![The 'Import Users' page in the Braze dashboard.]({% image_buster /assets/img/importcsv5.png %})

### Step 2: Choose an identifier

To import your CSV, you'll need to choose a user identifier for identifying which user profile each row will update. You can use the following identifiers:

external_id, 
braze_id, 
user alias, 
email address, 
or phone number.

{% tabs local %}
<!-- TAB -->
{% tab external id %}
When importing your customer data, you can use an `external_id` to serve as each customer’s unique identifier. When you provide an `external_id` in your import, Braze will update any existing user with the same `external_id` or create a newly identified user with that `external_id` set if one is not found.

Download: [CSV Attributes Import Template \- External ID]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)

Download: [CSV Events Import Template](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4) \- External ID

{% alert note %} 
If you’re uploading a mix of users with an `external_id` and users without, you need to create one CSV for each import. One CSV can’t contain both `external_ids` and user aliases.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab user alias %}
To target users who don’t have an `external_id`, you can import a list of users with user aliases. An alias serves as an alternative unique user identifier, and can be helpful if you are trying to market to anonymous users who haven’t signed up or made an account with your app.

If you are uploading or updating user profiles that are alias only, you must have the following two columns in your CSV:

- `user_alias_name`: A unique user identifier; an alternative to the `external_id`  
- `user_alias_label`: A common label by which to group user aliases

| user\_alias\_name | user\_alias\_label | last\_name | email | sample\_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my\_alt\_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my\_alt\_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

When you provide both a `user_alias_name` and `user_alias_label` in your import, Braze will update any existing user with the same `user_alias_name` and `user_alias_label`. If a user isn’t found, Braze will create a newly identified user with that `user_alias_name` set.

{% alert important %}
You can’t use a CSV import to update an existing user with a `user_alias_name` if they already have an `external_id`. Instead, this will create a new user profile with the associated `user_alias_name`. To associate an alias-only user with an `external_id`, use the [Identify users endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

Download: [CSV Attributes Import Template]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747) \- User Alias
{% endtab %}

<!-- TAB -->
{% tab braze id %}
To update existing user profiles in Braze by using an internal Braze ID value instead of an `external_id` or `user_alias_name` and `user_alias_label` value, specify `braze_id` as a column header.

This can be helpful if you exported user data from Braze through our CSV export option within segmentation and want to add a new custom attribute to those existing users.

{% alert important %}
You can’t use a CSV import to create a new user using `braze_id`. This method can only be used to update pre-existing users within the Braze platform.  
{% endalert %}

{% alert tip %}
The `braze_id` value might be labeled as `Appboy ID` in CSV exports from the Braze dashboard. This ID will be the same as the `braze_id` for a user, so you can rename this column to `braze_id` when you re-import the CSV.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab email address and phone numbers %}
You can omit an external ID or user alias and use either an email address or phone number to import users. Before importing a CSV file with email addresses or phone numbers, check for the following:

- Verify that you don’t have any external IDs or user aliases for these profiles in your CSV file. If you do, Braze will prioritize using the external ID or user alias before the email address to identify profiles.  
- Confirm that your CSV file is formatted properly.  
  note:  
  If you include both email addresses and phone numbers in your CSV file, the email address is prioritized over the phone number when looking up profiles.

If an existing profile has that email address or phone number, that profile will be updated, and Braze will not create a new profile. If there are multiple profiles with that same email address, Braze will use the same logic as the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) where the most recently updated profile will be updated.

If a profile with that email address or phone number doesn’t exist, Braze will create a new profile with that identifier. You can use the [`/users/identify` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) to identify this profile later. To delete a user profile, you can also use the [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) endpoint.
{% endtab %}
{% endtabs %}

### Step 3: Choose which data to import

You can upload either of the following data in a single CSV file. Upload additional CSV files to import multiple data types.

- **User Attributes:** This includes both default and custom user attributes. Default user attributes are reserved keys in Braze (such as `first_name` or `email`) and custom attributes are user attributes unique to your business (such as `last_destination_searched`).  
- **Custom Events:** These are unique to your business and reflect actions a user has taken, such as `trip_booked` for a travel booking app.

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
You can import a CSV with custom user attributes, default user attributes, or a combination of both. Your CSV must include the following column headers:

- 1 header to serve as your identifier (2 in the case of using user aliases as your identifier).  
- Additional headers for each default or custom attribute. These headers will dictate whether you are updating a default attribute or a custom attribute.

#### Custom attributes

Any column headers that don’t exactly match default attributes will create a custom attribute within Braze.

The following data types are accepted in user import:

- Datetime: Must be stored in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)  format  
- Boolean: `true` or `false`  
- Number: Integer or float with no spaces or commas, floats must use a period (`.`) as the decimal separator  
- String: Can contain commas if there are double-quotation marks (`""`) surrounding the column value  
- Blank: Blank values won’t overwrite existing values on the user profile, and you don’t need to include all existing user attributes in your CSV file  

{% alert important %}
Arrays, push tokens, and custom event data types aren’t supported in user import. Especially for arrays, commas in your CSV file will be interpreted as a column separator, so any commas in values will cause errors in parsing the file. 
{% endalert %} 
    
To upload these kinds of values, use the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) or [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/).

#### Default attributes

{% alert important %}
When importing default attributes, the column headers you use must exactly match the spelling and capitalization of default user attributes. Otherwise, Braze will detect these as custom attributes instead.
{% endalert %}

| USER PROFILE FIELD | DATA TYPE | INFORMATION | REQUIRED |
| :---- | :---- | :---- | :---- |
| `external_id` | String | A unique user identifier for your customer. | Yes, see the following note |
| `user_alias_name` | String | A unique user identifier for anonymous users. An alternative to the `external_id`. | No, see the following note |
| `user_alias_label` | String | A common label by which to group user aliases. | Yes if `user_alias_name` is used |
| `first_name` | String | The first name of your users as they have indicated (for example, `Jane`). | No |
| `last_name` | String | The last name of your users as they have indicated (for example, `Doe`). | No |
| `email` | String | The email of your users as they have indicated (for example, `jane.doe@braze.com`). | No |
| `country` | String | Country codes must be passed to Braze in the ISO-3166-1 alpha-2 standard (for example, `GB`). | No |
| `dob` | String | Must be passed in the format “YYYY-MM-DD” (for example, `1980-12-21`). This will import your user’s Date of Birth and enable you to target users whose birthday is “today”. | No |
| `gender` | String | “M”, “F”, “O” (other), “N” (not applicable), “P” (prefer not to say), or nil (unknown). | No |
| `home_city` | String | The home city of your users as they have indicated (for example, `London`). | No |
| `language` | String | Language must be passed to Braze in the ISO-639-1 standard (for example, `en`). Refer to our [list of accepted languages]({{site.baseurl}}/user_guide/data/user_data_collection/language_codes/). | No |
| `phone` | String | A telephone number as indicated by your users, in `E.164` format (for example, `+442071838750`). Refer to [User Phone Numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) for formatting guidance. | No |
| `email_open_tracking_disabled` | Boolean | true or false accepted. Set to true to disable the open tracking pixel from being added to all future emails sent to this user. Available for SparkPost and SendGrid only. | No |
| `email_click_tracking_disabled` | Boolean | true or false accepted. Set to true to disable the click tracking for all links within a future email, sent to this user. Available for SparkPost and SendGrid only. | No |
| `email_subscribe` | String | Available values are `opted_in` (explicitly registered to receive email messages), `unsubscribed` (explicitly opted out of email messages), and `subscribed` (neither opted in nor out). | No |
| `push_subscribe` | String | Available values are `opted_in` (explicitly registered to receive push messages), `unsubscribed` (explicitly opted out of push messages), and `subscribed` (neither opted in nor out). | No |
| `time_zone` | String | Time zone must be passed to Braze in the same format as the IANA Time Zone Database (for example, `America/New_York` or `Eastern Time (US & Canada)`). | No |
| `date_of_first_session`  `date_of_last_session` | String | May be passed in one of the following ISO 8601 formats: "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS" (for example, 2019-11-20T18:38:57) | No |
| `subscription_group_id` | String | The `id` of your subscription group. This identifier can be found on the subscription group page of your dashboard. | No |
| `subscription_state` | String | The subscription state for the subscription group specified by `subscription_group_id`. Allowed values are `unsubscribed` (not in subscription group) or `subscribed` (in subscription group). | No, but strongly recommended if `subscription_group_id` is used |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

note:  
While `external_id` itself is not mandatory, you must include one of these fields to serve as your identifier:

- `external_id`: A unique user identifier for your customer  
  \- OR \-  
- `braze_id`: A unique user identifier pulled for existing Braze users  
  \- OR \-  
- `user_alias_name` : A unique user identifier for an anonymous user. This requires the additional use of the `user_alias_label` field.  
- \- OR \-  
  - `email`  
    - \- OR \-  
    - `phone`
{% endtab %}

<!-- TAB -->
{% tab custom events %}
You can import a CSV with custom events. Your CSV must include the following column headers:

- 1 header to serve as your identifier (2 in the case of using user aliases as your identifier).  
- `name` \- This is the name of the custom event  
- `time` \- This is the time that the custom event occurred

Additionally, your CSV may also have additional column headers for event properties. These properties should have a column header of `<event_name>.properties.<property name>.`

For example, the custom event `trip_booked` may have the properties `destination` and `duration`. These can be imported by having the column headers `trip_booked.properties.destination` and `trip_booked.properties.duration`.

| USER PROFILE FIELD | DATA TYPE | INFORMATION | REQUIRED |
| :---- | :---- | :---- | :---- |
| `external_id` | String | A unique user identifier for your user. | Yes, see the following note |
| `braze_id` | String | A Braze assigned identifier for your user. | Yes, one of `external_id`, `braze_id`, or `user_alias_name` and `user_alias_label` is required. |
| `user_alias_name` | String | A unique user identifier for anonymous users. An alternative to the external\_id. | No, see the following note |
| `user_alias_label` | String | A common label by which to group user aliases. | Yes if `user_alias_name` is used |
| `email` | String | The email of your users as they have indicated (for example, `jane.doe@braze.com`). | No, and can only be used in the absence of other identifiers. See the following note. |
| `phone` | String | A telephone number as indicated by your users, in `E.164` format (for example, `+442071838750`). Refer to [User Phone Numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) for formatting guidance. | No, and can only be used in the absence of other identifiers. See the following note. |
| `name` | String | A custom event of your users. | Yes |
| `time` | String | The time of the event. May be passed in one of the following ISO-8601 formats: "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS" (for example, 2019-11-20T18:38:57) | Yes |
| `<event name>.properties.<property name>` | Multiple | An event property associated with a custom event. An example is `trip_booked.properties.destination` | No |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

note:  
While `external_id` itself is not mandatory, you must include one of these fields to serve as your identifier:

- `external_id`: A unique user identifier for your customer  
  \- OR \-  
- `braze_id`: A unique user identifier pulled for existing Braze users  
  \- OR \-  
- `user_alias_name` : A unique user identifier for an anonymous user. This requires the additional use of the `user_alias_label` field.  
- \- OR \-  
  - `email`  
    - \- OR \-  
    - `phone`
{% endtab %}
{% endtabs %}

### Step 4: Review the upload preview

Select Attributes or Events, then select Browse Files and upload your file. Braze will upload your file and preview the top few rows for potential issues.

Note that although a file can be imported with errors, processed rows cannot be undone. it can’t be canceled or undone. As such, review the preview and consider canceling the import and modifying your file if there are issues.

<!-- old image -->
![CSV upload completed with errors involving mixed data types in a single column]({% image_buster /assets/img/importcsv2.png %}){: style="max-width:70%"}

{% alert important %}
User Import preview doesn’t scan every row of the input file. Errors after the top few rows may not be caught, so consider examining the CSV file in full.
{% endalert %}

### Step 5: Upload your CSV

When you’re satisfied with the upload, start the import and select targeting preferences. You can track its progress on the User Import page, which will refresh every five seconds, or at the press of the refresh button in the Recent Imports box.

{% details More on targeting preferences %}
Choosing “Create targeting filter” turns the CSV file into a retargeting option when building user segments. To filter all users from the CSV in a segment or wherever filtering is an option, select the Updated/Imported from CSV filter and then search for the file’s exact name.

![A filter group with the "Updated/Imported from CSV" filter including a CSV file titled "Halloween season fun".]()

Choosing “Create targeting filter and add to new segment” builds on this by automatically creating a new segment containing all users imported from your CSV file.
{% enddetails %}

When the import is completed, the status will change to Complete and the number of rows processed is displayed. All data from processed rows will either be added to existing profiles or to newly created profiles.

{% alert note %}
You can import more than one CSV at the same time. CSV imports run concurrently, so the order of updates is not guaranteed to be serial. If you require CSV imports to run one after another, wait until a CSV import has finished before uploading a second one.
{% endalert %}

## Updating subscription group status

You can add users to email or SMS subscription groups through user import. This is particularly useful for SMS, because a user must be enrolled into an SMS subscription group to be messaged with the SMS channel. For more information, refer to [SMS subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

If you are updating subscription group statuses, you must have the following two columns in your CSV:

- `subscription_group_id`: The `id` of the [subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).
- `subscription_state`: Available values are `unsubscribed` (not in the subscription group) or `subscribed` (in the subscription group).

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">external_id</th>
    <th class="tg-0pky">first_name</th>
    <th class="tg-0pky">subscription_group_id</th>
    <th class="tg-0pky">subscription_state</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">A8i3mkd99</td>
    <td class="tg-0pky">Colby</td>
    <td class="tg-0pky">6ff593d7-cf69-448b-aca9-abf7d7b8c273</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
  <tr>
    <td class="tg-0pky">k2LNhj8Ks</td>
    <td class="tg-0pky">Tom</td>
    <td class="tg-0pky">aea02307-a91e-4bc0-abad-1c0bee817dfa</td>
    <td class="tg-0pky">subscribed</td>
  </tr>
</tbody>
</table>

{% alert important %}
Only a single `subscription_group_id` can be set per row in the user import. Different rows can have different `subscription_group_id` values. However, if you need to enroll the same users into multiple subscription groups, you'll need to do multiple imports.
{% endalert %}

## Lambda user CSV import

You can use our serverless S3 Lambda CSV import script to upload user attributes to Braze. This solution works as a CSV uploader where you drop your CSVs into an S3 bucket, and the scripts upload it through our API.

Estimated execution times for a file with 1,000,000 rows should be around five minutes. See [User attribute CSV to Braze import](https://www.braze.com/docs/user_guide/data/cloud_ingestion/) for more information.
