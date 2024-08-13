---
nav_title: Import User Data and CSV Events
article_title: Import User Data and CSV Events
permalink: "/csv_events/"
description: "This reference article covers how to import user data and how to import custom events using CSV files."
page_type: reference
---

# Importing user data (CSV events early access)

> Braze offers a variety of ways to import user data into the platform: SDKs, APIs, cloud data ingestion, technology partner integrations, and CSV files. This article provides detailed instructions on how to import user data, including how to [import custom events via CSV files (early access)](#importing-custom-events).

{% multi_lang_include email-via-sms-warning.md %}

Before proceeding, note that Braze does not sanitize (validate or properly format) HTML data during import. This means that script tags must be stripped for all import data meant for web personalization.

## REST API

You can use the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to record custom events, user attributes, and purchases for users.

## CSV import

You can also upload and update user profiles though CSV files from **Audience** > **Import Users**.

Importing user data using CSV files supports recording and updating user attributes such as first name and email, in addition to custom attributes such as shoe size. You can import a CSV by specifying one of two unique user identifiers: an `external_id` or a user alias.

{% alert important %}
User import also supports recording and updating user custom events. Similar to user attributes, you can import with an `external_id`, `braze_id` or with `user_alias_name` with `user_alias_label`. See [Importing custom events](#importing-custom-events) for more details.
{% endalert %}

{% alert note %}
If you're uploading a mix of users with an `external_id` and users without, you need to create one CSV file for each import. One CSV file can't contain both `external_ids` and user aliases.
{% endalert %}

### Importing with external ID

When importing your customer data, you'll need to specify each customer's unique identifier, also known as `external_id`. Before starting your CSV import, it's important to understand from your engineering team how users will be identified in Braze. Typically, this is an internal database ID. This should align with how users will be identified by the Braze SDK on mobile and web and is designed for each customer to have a single user profile within Braze across their devices. Read more about the Braze [user profile lifecycle][13].

When you provide an `external_id` in your import, Braze will update any existing user with the same `external_id` or create a newly identified user with that `external_id` set if one is not found.

- **Download:** [CSV Attributes Import Template][import_template]
- **Download:** [CSV Events Import Template][events_template]

### Importing with user alias

To target users who don't have an `external_id`, you can import a list of users with user aliases. An alias serves as an alternative unique user identifier, and can be helpful if you are trying to market to anonymous users who haven't signed up or made an account with your app.

If you are uploading or updating user profiles that are alias only, you must have the following two columns in your CSV:

- `user_alias_name`: A unique user identifier; an alternative to the `external_id`
- `user_alias_label`: A common label by which to group user aliases

| user_alias_name | user_alias_label | last_name | email | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

When you provide both a `user_alias_name` and `user_alias_label` in your import, Braze will update any existing user with the same `user_alias_name` and `user_alias_label`. If a user isn't found, Braze will create a newly identified user with that `user_alias_name` set.

{% alert important %}
You can't use a CSV import to update an existing user with a `user_alias_name` if they already have an `external_id`. Instead, this will create a new user profile with the associated `user_alias_name`. To associate an alias-only user with an `external_id`, use the [Identify users endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

- **Download:** [CSV Alias Attributes Import Template][template_alias_attributes]
- **Download:** [CSV Alias Events Import Template][template_alias_events]

### Importing with Braze ID

To update existing user profiles in Braze by using an internal Braze ID value instead of an `external_id` or `user_alias_name` and `user_alias_label` value, specify `braze_id` as a column header.

This can be helpful if you exported user data from Braze through our CSV export option within segmentation and want to add a new custom attribute to those existing users.

{% alert important %}
You can't use a CSV import to create a new user using `braze_id`. This method can only be used to update pre-existing users within the Braze platform.
{% endalert %}

{% alert tip %}
The `braze_id` value might be labeled as `Appboy ID` in CSV exports from the Braze dashboard. This ID will be the same as the `braze_id` for a user, so you can rename this column to `braze_id` when you re-import the CSV.
{% endalert %}

### Importing default attributes

To import default attributes for users, go to **Import Users** > **Attributes**. Default user attributes are reserved keys in Braze. For example, `first_name` or `email`. Custom attributes are custom to your business. For example, a travel booking app may have a custom attribute called `last_destination_searched`.

{% alert important %}
When importing customer data as attributes, the column headers you use must exactly match the spelling and capitalization of default user attributes. Otherwise, Braze will automatically create a custom attribute on that user's profile.
{% endalert %}

#### Default user data column headers

| USER PROFILE FIELD | DATA TYPE | INFORMATION | REQUIRED |
|---|---|---|---|
| `external_id` | String | A unique user identifier for your customer. | Yes, see the following note |
| `user_alias_name` | String | A unique user identifier for anonymous users. An alternative to the `external_id`. | No, see the following note |
| `user_alias_label` | String | A common label by which to group user aliases. | Yes if `user_alias_name` is used |
| `first_name` | String | The first name of your users as they have indicated (for example, `Jane`). | No |
| `last_name` | String | The last name of your users as they have indicated (for example, `Doe`). | No |
| `email` | String | The email of your users as they have indicated (for example, `jane.doe@braze.com`). | No |
| `country` | String | Country codes must be passed to Braze in the ISO-3166-1 alpha-2 standard (for example, `GB`). | No |
| `dob` | String | Must be passed in the format "YYYY-MM-DD" (for example, `1980-12-21`). This will import your user's Date of Birth and enable you to target users whose birthday is "today". | No |
| `gender` | String | "M", "F", "O" (other), "N" (not applicable), "P" (prefer not to say), or nil (unknown). | No |
| `home_city` | String | The home city of your users as they have indicated (for example, `London`). | No |
| `language` | String | Language must be passed to Braze in the ISO-639-1 standard (for example, `en`). <br>Refer to our [list of accepted languages][1]. | No |
| `phone` | String | A telephone number as indicated by your users, in `E.164` format (for example, `+442071838750`). <br> Refer to [User Phone Numbers][2] for formatting guidance. | No |
| `email_open_tracking_disabled` | Boolean | true or false accepted.  Set to true to disable the open tracking pixel from being added to all future emails sent to this user.   | No |
| `email_click_tracking_disabled` | Boolean | true or false accepted.  Set to true to disable the click tracking for all links within a future email, sent to this user. | No |
| `email_subscribe` | String | Available values are `opted_in` (explicitly registered to receive email messages), `unsubscribed` (explicitly opted out of email messages), and `subscribed` (neither opted in nor out). | No |
| `push_subscribe` | String | Available values are `opted_in` (explicitly registered to receive push messages), `unsubscribed` (explicitly opted out of push messages), and `subscribed` (neither opted in nor out). | No |
| `time_zone` | String | Time zone must be passed to Braze in the same format as the IANA Time Zone Database (for example, `America/New_York` or `Eastern Time (US & Canada)`).  | No |
| `date_of_first_session` <br><br> `date_of_last_session`| String | May be passed in one of the following ISO-8601 formats: {::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (for example, 2019-11-20T18:38:57) </li> </ul> {:/} | No |
| `subscription_group_id` | String | The `id` of your subscription group. This identifier can be found on the subscription group page of your dashboard. | No |
| `subscription_state` | String | The subscription state for the subscription group specified by `subscription_group_id`. Allowed values are `unsubscribed` (not in subscription group) or `subscribed` (in subscription group). | No, but strongly recommended if `subscription_group_id` is used |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
While `external_id` itself is not mandatory, you **must** include one of these fields: <br>
- `external_id`: A unique user identifier for your customer <br> - OR -
- `braze_id`: A unique user identifier pulled for existing Braze users <br> - OR -
- `user_alias_name` and `user_alias_label` : A unique user identifier for an anonymous user
{% endalert %}

### Importing custom attributes

You can import custom attributes for users by going to **Import Users** > **Attributes**. Any headers that do not exactly match default attributes create a custom attribute within Braze.

The following data types are accepted in user import:

| Data type | Description |
| Datetime | Must be stored in ISO-8601 format |
| Boolean | TRUE or FALSE |
| Number | Integer or float with no spaces or commas, floats must use a period (.) as the decimal separator |
| String | Can contain commas as long as there are double quotation marks surrounding the column value |
| Blank | Blank values will not overwrite existing values on the user profile, and you do not need to include all existing user attributes in your CSV file |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Arrays and push tokens are not supported in user import. Especially for arrays, commas in your CSV file will be interpreted as a column separator, so any commas in values will cause errors parsing the file. <br>For uploading these kinds of values, use the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) or [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/).
{% endalert %}

### Updating subscription group status

You can add users into email or SMS subscription groups through user import. This is particularly useful for SMS, because a user must be enrolled into an SMS subscription group to be messaged with the SMS channel. For more information, refer to [SMS subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

If you are updating subscription group status, you must have the following two columns in your CSV:

- `subscription_group_id`: The `id` of the [subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).
- `subscription_state`: Available values are `unsubscribed` (not in subscription group) or `subscribed` (in the subscription group).

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
Only a single `subscription_group_id` can be set per row in the user import. Different rows can have different `subscription_group_id` values. However, if you need to enroll the same users into multiple subscription groups, you will need to do multiple imports.
{% endalert %}

### Importing custom events (early access) {#importing-custom-events}

{% alert important %}
Importing custom events is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

Go to **Import Users** > **Events** to import custom events for your users.

- Custom events are custom to your business. For example, a streaming app may have a custom event called rented_movie. Your CSV must have column headers for:
    - One of `external_id`, `braze_id` or `user_alias_name` and `user_alias_label`
    - name
    - time
- Custom events may have event properties. For example, the custom event rented_movie may have the properties title and genre. These event properties should have a column header of `<event_name>.properties.<property name>`. For example, `rented_movie.properties.title`.

| USER PROFILE FIELD                      | DATA TYPE | INFORMATION                                                                                                                                                                                                             | REQUIRED                                                                                        |
|-----------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `external_id`                           | String    | A unique user identifier for your user.                                                                                                                                                                                 | Yes, one of `external_id`, `braze_id`, or `user_alias_name` and `user_alias_label` is required. |
| `braze_id`                              | String    | A Braze assigned identifier for your user.                                                                                                                                                                              | Yes, one of `external_id`, `braze_id`, or `user_alias_name` and `user_alias_label` is required. |
| `user_alias_name`                       | String    | A unique user identifier for anonymous users. An alternative to the external_id.                                                                                                                                        | Yes, one of `external_id`, `braze_id`, or `user_alias_name` and `user_alias_label` is required. |
| `user_alias_label`                      | String    | A common label by which to group user aliases.                                                                                                                                                                          | Yes, one of `external_id`, `braze_id`, or `user_alias_name` and `user_alias_label` is required. |
| `name`                                  | String    | A custom event of your users.                                                                                                                                                                                           | Yes                                                                                             |
| `time`                                  | String    | The time of the event. May be passed in one of the following ISO-8601 formats: {::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (for example, 2019-11-20T18:38:57) </li> </ul> {:/} | Yes                                                                                             |
| `<event name>.properties.<property name>` | Multiple  | An event property associated with a custom event. An example is `rented_movie.properties.title`                                                                                                                        | No                                                                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
While external_id itself is not mandatory, you must include one of the following fields: <br>- `external_id`: A unique user identifier for your customer <br>- `braze_id`: A unique user identifier pulled for existing Braze users <br>- `user_alias_name`: A unique user identifier for an anonymous user
{% endalert %}

#### CSV size

Braze accepts user data in the standard CSV format from files up to 500 MB in size. Refer to the previous sections on importing for downloadable CSV templates.

#### Data point considerations

Each piece of customer data imported via CSV will overwrite the existing value on user profiles and will count as a data point, except external IDs and blank values.

- External IDs uploaded via CSV import will not consume data points. If you're uploading a CSV file to segment existing Braze users by uploading only external IDs, this can be done without consuming data points. If you were to add additional data like a user's email or phone number in your import, that would overwrite existing user data and consume your data points.
    - CSV imports for segmentation purposes (imports made with `external_id`, `braze_id`, or `user_alias_name` as the only field) will not consume data points.
- Blank values will not overwrite existing values on the user profile, and you don't need to include all existing user attributes or custom events in your CSV file.
- Updating `email_subscribe`, `push_subscribe`, `subscription_group_id`, or `subscription_state` will not count toward data point consumption.

{% alert important %}
Setting language or country on a user via CSV import or API will prevent Braze from automatically capturing this information via the SDK.
{% endalert %}

## Importing a CSV

To import your CSV file, do the following.
1. Go to **Audiences** > **User Import**. 
2. Select **Browse Files** and select your file of interest, then select **Start Upload**. Braze will upload your file and check the column headers as well as the data types of each column.

![The "Events" option is selected as the type of user information to import.][5]

Under **Recent Imports**, you can view up to twenty of your most recent imports, their file names, CSV type, number of lines in the file, number of lines successfully imported, total lines in each file, and the status of each import.

{% alert important %}
CSV imports are case sensitive. This means capital letters in CSV imports will write the field as a custom attribute instead of a standard one. For example, "email" is correct, but "Email" would be written as a custom attribute.
{% endalert %}

After the upload is complete, you can view a preview of the contents of your file. The information in the table is based on the values in the top rows of your CSV file.

You can import more than one CSV file at the same time. CSV imports will run concurrently, and as such the order of updates is not guaranteed to be serial. If you require CSV imports to run one after another, you should wait until a CSV import has finished before uploading a second one.

If Braze notices something malformed in the top rows of your file during the upload, these errors will be shown with the summary. For example, if your file includes a malformed row, then this error will be noted in the preview when you import the file. Although a file can be imported with errors, it is recommended that you fix such errors in your file before continuing on with your import.

Moreover, it’s important to examine the full CSV file before upload, as Braze doesn’t scan every row of the input file for the preview. This means errors can exist which Braze doesn’t catch while generating this preview.

Malformed rows and rows lacking an external ID will not be imported. All other errors can be imported, but may interfere with filtering when creating a segment. For more information, skip to the [Troubleshooting](#troubleshooting) section.

![CSV file upload completed with errors involving mixed data types in a single column][4]{: style="max-width:70%"}

{% alert warning %}
Errors are based solely on data type and file structure. For example, a poorly formatted email address would still be imported as it can still be parsed as a string.
{% endalert %}

When you're satisfied with the upload, start the import. You can track the progress on the **User Import** page, which refreshes every five seconds, or when you select the refresh button in **Recent Imports**.

Under **Lines Processed** is the progress of the import; the status will change to **Complete** when finished. You can still use the rest of the Braze dashboard during the import, and you'll receive notifications when the import begins and ends.

If the import process runs into an error, a warning icon will appear next to the total number of lines in the file. You can hover over the icon to see details about why certain lines failed. After the import is completed, all data will be added to existing profiles, or new profiles will be created.

### Lambda user CSV import

You can use our serverless S3 Lambda CSV import script to upload user attributes to the platform. This solution works as a CSV uploader where you drop your CSVs into an S3 bucket, and the scripts upload it through our API.

Estimated execution times for a file with one million rows should be around five minutes. See [User attribute CSV to Braze import]({{site.baseurl}}/user_csv_lambda/) for more information.

## Segmenting

User import creates and updates user profiles, and can also be used to create segments. To create a segment, select **Automatically generate a segment from the users who are imported from this CSV** before starting the import.

You can set the name of the segment or accept the default, which is the name of your file. Files that were used to create a segment will have a link to view the segment after the import has been completed.

The filter used to create the segment selects users who were created or updated in a selected import and is available with all other filters in the edit segment page.

## Troubleshooting {#troubleshooting}

### Missing rows

There are a few reasons why the number of users imported might not match the total rows in your CSV file:

- **Duplicate external IDs:** If there are duplicate external ID columns, then this may cause malformed or unimported rows even if the rows are correctly formatted. In some cases this may not report a specific error. Check if there are any duplicate external IDs in your CSV. If so, remove the duplicates and try uploading again.
- **Accented characters:** Your CSV file may have names or attributes that include accents. Ensure your file is UTF-8 encoded to prevent any issues.

### Malformed row

There must be a header row in order to properly import data. Each row must have the same number of cells as the header row. Rows with a length of more or fewer values than the header row will be excluded from the import. Commas in a value will be interpreted as a separator and can lead to this error being thrown. Additionally, all data must be UTF-8 encoded.

If your CSV file has blank rows and imports less rows than the total lines in the CSV file, this may not indicate a problem with the import since the blank rows wouldn't need to be imported. Check the number of lines that were correctly imported and make sure it matches the number of users you're attempting to import.

### Multiple data types

Braze expects each value in a column to be of the same data type. Values that do not match their attribute's data type will cause errors in segmenting.

### Incorrectly formatted dates

Dates not in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format will not be read as datetimes on import.

### String quotation

Values encapsulated in single ('') or double ("") quotation marks will be read as strings on import.

### Data imported as custom attribute

If you are seeing a piece of default user data (for example, `email` or `first_name`) imported as a custom attribute, check the case and spacing of your CSV file. For example, `First_name` would be imported as a custom attribute, while `first_name` would be correctly imported into the "first name" field on a user's profile.

[import_template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[events_template]: {% image_buster /assets/download_file/braze-csv-events-import-template.csv %}
[template_alias_attributes]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
[template_alias_events]: {% image_buster /assets/download_file/braze-events-csv-example-user-alias.csv %}
[errors]:#common-errors
[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[5]: {% image_buster /assets/img/importcsv3.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}