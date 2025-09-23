---
nav_title: Using a CSV
article_title: "CSV Import"
description: "Learn how to record and update user attributes and custom events using CSV import."
page_order: 1.2
---

# CSV import

> Learn how to record and update user attributes and custom events using CSV import.

## About CSV import

You can use CSV import to record and update the following user attributes and custom events.

|Type|Definition|Example|Maximum file size|
|---|---|---|---|
|Default Attributes|Reserved user attributes recognized by Braze.|`first_name`, `email`|500 MB|
|Custom Attributes|User attributes unique to your business.|`last_destination_searched`|500 MB|
|Custom Events|Events unique to your business that represent user actions.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## Using CSV import

### Step 1: Download a CSV template

To open CSV import, go to **Audiences** > **Import Users**. Here, you'll find a table that lists details about the most recent imports, such as the upload date, uploader's name, file name, targeting availability, number of imported rows, and status of the import.

To get you started with your CSV, download a template for attributes or events.

![The 'Import Users' page in the Braze dashboard.]({% image_buster /assets/img/csv_import/import_users_page.png %})

### Step 2: Choose an identifier {#choose-an-identifier}

The CSV you import will need a dedicated identifier. You can choose from the following:

{% tabs local %}
<!-- TAB -->
{% tab external id %}
When importing your customer data, you can use an `external_id` to serve as each customer’s unique identifier. When you provide an `external_id` in your import, Braze will update any existing user with the same `external_id` or create a newly identified user with that `external_id` set if one is not found.

- Download: [CSV Attributes Import Template: External ID]({{site.baseurl}}/assets/download_file/braze-user-import-template-csv.xlsx?3aafd0c03634ac03f248b3055fbc3126)
- Download: [CSV Events Import Template: External ID](https://braze.com/unlisted_docs/assets/download_file/braze-csv-events-import-template.csv?3b64ea284baa9a21cfe0a7ab4b46fce4)

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

| `user_alias_name` | `user_alias_label` | `last_name` | `email` | sample_attribute |
| :---- | :---- | :---- | :---- | :---- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

When you provide both a `user_alias_name` and `user_alias_label` in your import, Braze will update any existing user with the same `user_alias_name` and `user_alias_label`. If a user isn’t found, Braze will create a newly identified user with that `user_alias_name` set.

{% alert important %}
You can’t use a CSV import to update an existing user with a `user_alias_name` if they already have an `external_id`. Instead, this will create a new user profile with the associated `user_alias_name`. To associate an alias-only user with an `external_id`, use the [Identify users endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

Download: [CSV Attributes Import Template: User Alias]({{site.baseurl}}/assets/download_file/braze-user-import-alias-template-csv.xlsx?c0ce6c0aa1e901395161d87c5ba17747)
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

{% alert note %}
If you include both email addresses and phone numbers in your CSV file, the email address is prioritized over the phone number when looking up profiles.
{% endalert %}

If an existing profile has that email address or phone number, that profile will be updated, and Braze will not create a new profile. If there are multiple profiles with that same email address, Braze will use the same logic as the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) where the most recently updated profile will be updated.

If a profile with that email address or phone number doesn’t exist, Braze will create a new profile with that identifier. You can use the [`/users/identify` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) to identify this profile later. To delete a user profile, you can also use the [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) endpoint.
{% endtab %}
{% endtabs %}

### Step 3: Build your CSV file

You can upload either of the following data types as a single CSV file. To upload more than one data types, upload multiple CSV files.

- **User Attributes:** This includes both default and custom user attributes. Default user attributes are reserved keys in Braze (such as `first_name` or `email`) and custom attributes are user attributes unique to your business (such as `last_destination_searched`).  
- **Custom Events:** These are unique to your business and reflect actions a user has taken, such as `trip_booked` for a travel booking app.

When you're ready to start building your CSV file, refer to the following information:

{% tabs local %}
<!-- TAB -->
{% tab user attributes %}
#### Required identifiers {#required-identifiers-attributes}

While `external_id` is not required, you **must** include **one** of the following identifiers as a header in your CSV file. For details about each one, review [Choose an identifier](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **and** `user_alias_label`
- `email`
- `phone`

#### Custom attributes

The following data types can be used as custom attributes for CSV import. Column headers that don't exactly match a [default attribute](#default-attributes) will be given a custom attribute in Braze.

| Data Type | Description |
|---|---|
| Datetime | Must be stored in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| Boolean | Accepts `true` or `false`. |
| Number | Must be an integer or float with no spaces or commas. Floats must use a period (`.`) as the decimal separator. |
| String | Can contain commas if the value is wrapped in double quotation marks (`""`). |
| Blank | Blank values won’t overwrite existing values on the user profile, and you don’t need to include all existing user attributes in your CSV file. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Arrays, push tokens, and custom event data types aren’t supported in user import, as commas in your CSV file will be interpreted as a column separator and cause errors while parsing your file.<br><br>To upload these kinds of values, use the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) or [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/) instead.
{% endalert %} 

#### Default attributes

{% alert important %}
When importing default attributes, the column headers you use must exactly match the spelling and capitalization of default user attributes. Otherwise, Braze will detect these as [custom attributes](#custom-attributes) instead.
{% endalert %}

| User Profile Field | Data Type | Description | Required? |
| :---- | :---- | :---- | :---- |
| `external_id` | String | A unique user identifier for your customer. | Conditionally. See [Required Identifiers](#required-identifiers-attributes). |
| `user_alias_name` | String | A unique user identifier for anonymous users that's an alternative to `external_id`. Must be used with `user_alias_label`. | Conditionally. See [Required Identifiers](#required-identifiers-attributes). |
| `user_alias_label` | String | A common label by which to group user aliases. Must be used with `user_alias_name`. | Conditionally. See [Required Identifiers](#required-identifiers-attributes). |
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

#### Updating subscription group status (optional)

Additionally, you can add users to email or SMS subscription groups through user import. This is particularly useful for SMS, because a user must be enrolled into an SMS subscription group to be messaged with the SMS channel. For more information, refer to [SMS subscription groups](https://www.braze.com/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement).

If you are updating subscription group statuses, you must have the following two columns in your CSV:

- `subscription_group_id`: The `id` of the [subscription group](https://www.braze.com/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups).  
- `subscription_state`: Available values are `unsubscribed` (not in the subscription group) or `subscribed` (in the subscription group).

| external_id | first_name | subscription_group_id | subscription_state |
| :---- | :---- | :---- | :---- |
| A8i3mkd99 | Colby | 6ff593d7-cf69-448b-aca9-abf7d7b8c273 | subscribed |
| k2LNhj8Ks | Tom | aea02307-a91e-4bc0-abad-1c0bee817dfa | subscribed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert note %}
Only a single `subscription_group_id` can be set per row in the user import. Different rows can have different `subscription_group_id` values. However, if you need to enroll the same users into multiple subscription groups, you’ll need to do multiple imports.
{% endalert %}
{% endtab %}

<!-- TAB -->
{% tab custom events %}
#### Required identifiers {#required-identifiers-custom-events}

While `external_id` is not required, you **must** include **one** of the following identifiers as a header in your CSV file. For details about each one, review [Choose an identifier](#choose-an-identifier).

- `external_id`
- `braze_id`
- `user_alias_name` **and** `user_alias_label`
- `email`
- `phone`

#### Custom event fields

In addition to the following, your CSV may also contain additional column headers for event properties. These properties should have a column header of `<event_name>.properties.<property name>.`

For example, the custom event `trip_booked` may have the properties `destination` and `duration`. These can be imported by having the column headers `trip_booked.properties.destination` and `trip_booked.properties.duration`.

| User Profile Field | Data Type | Information | Required? |
| :---- | :---- | :---- | :---- |
| `external_id` | String | A unique user identifier for your user. | Conditionally. See [Required identifiers](#required-identifiers-custom-events). |
| `braze_id` | String | A Braze assigned identifier for your user. | Conditionally. See [Required identifiers](#required-identifiers-custom-events). |
| `user_alias_name` | String | A unique user identifier for anonymous users, that's an alternative to `external_id`. Must be used with `user_alias_label`. | Conditionally. See [Required identifiers](#required-identifiers-custom-events). |
| `user_alias_label` | String | A common label by which to group user aliases. Must be used with `user_alias_name`. | Conditionally. See [Required identifiers](#required-identifiers-custom-events). |
| `email` | String | The email of your users as they have indicated (for example, `jane.doe@braze.com`). | No, and can only be used in the absence of other identifiers. See the following note. |
| `phone` | String | A telephone number as indicated by your users, in `E.164` format (for example, `+442071838750`). Refer to [User Phone Numbers]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/) for formatting guidance. | No, and can only be used in the absence of other identifiers. See the following note. |
| `name` | String | A custom event of your users. | Yes |
| `time` | String | The time of the event. May be passed in one of the following ISO-8601 formats: "YYYY-MM-DD" "YYYY-MM-DDTHH:MM:SS+00:00" "YYYY-MM-DDTHH:MM:SSZ" "YYYY-MM-DDTHH:MM:SS" (for example, 2019-11-20T18:38:57) | Yes |
| `<event name>.properties.<property name>` | Multiple | An event property associated with a custom event. An example is `trip_booked.properties.destination` | No |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endtab %}
{% endtabs %}

### Step 4: Upload and preview your data

Before Braze processes your CSV, it will generate a preview of the first few rows so you can check for any issues. To generate your preview, choose **Attributes** or **Events**, then select **Browse Files**, and upload your CSV. 

<!-- old image -->
![CSV upload completed with errors involving mixed data types in a single column]({% image_buster /assets/img/csv_import/upload_csv.png %}){: style="max-width:70%"}

{% alert important %}
User Import preview doesn’t scan every row of the input file. Errors after the top few rows may not be caught, so consider examining the CSV file in full.
{% endalert %}

### Step 5: Choose targeting preferences

You can also choose from the following targeting preferences. If you don't need to create a new targeting filter or segment from your import, select **Do not make this list available as a targeting filter**.

| Option | Description |
|---|---|
| Targeting filter | To convert your CSV file into a retargeting option when building user segments, choose your file from the **Updated/Imported from CSV** dropdown, then select **Create targeting filter**. |
| New segments | To also create a new segment from your new targeting filter, select **Create targeting filter and add to new segment** . |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

![A filter group with the "Updated/Imported from CSV" filter including a CSV file titled "Halloween season fun".]({% image_buster /assets/img/csv_import/add_filter_group.png %}){: style="max-width:85%;"}

### Step 6: Start your CSV import

When you're ready, select **Start import**. You can track the current progress on the **User Import** page, which automatically refreshes every five seconds.

If there's no issues, the status will update to **Complete** and the number of rows processed will be displayed. All data from processed rows will either be added to existing profiles or to newly created profiles.

{% alert note %}
You can import more than one CSV at the same time. CSV imports run concurrently, so the order of updates is not guaranteed to be serial. If you require CSV imports to run one after another, wait until a CSV import has finished before uploading a second one.
{% endalert %}

## Data point considerations

Each piece of customer data imported from a CSV file will overwrite the existing value on user profiles and log a data point, except for external IDs and blank values. If you have any questions about the nuances of Braze data points, your Braze account manager can answer them.

| Consideration | Details |
|---|---|
| External IDs | Uploading a CSV with only `external_id` will not log data points. This allows you to segment existing Braze users without impacting data limits. However, including fields like `email` or `phone` will overwrite existing user data and **will** log data points. <br><br>CSV imports used only for segmentation do not log data points, such as those containing just `external_id`, `braze_id`, or `user_alias_name`. |
| Blank values | Blank values in your CSV won't overwrite existing user profile data. You don't need to include all user attributes or custom events when importing. |
| Subscription states | Updating `email_subscribe`, `push_subscribe`, `subscription_group_id`, or `subscription_state` does **not** count toward data point usage. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Setting `language` or `country` on a user through CSV import or API will prevent Braze from automatically capturing this information through the SDK.
{% endalert %}

## Troubleshooting

Review these common issues if you’re having trouble with CSV import. Still need help? Reach out to [support@braze.com](mailto:support@braze.com).

### File formatting issues

#### Malformed row

If your upload completed with errors, there may be a malformed row in your CSV file. 

To properly import data, there must be a header row. Each row must have the same number of cells as the header row. Rows with a length of more or fewer values than the header row will be excluded from the import. Commas in a value will be interpreted as a separator and can lead to this error. Additionally, all data must be UTF-8 encoded.

If your CSV file has blank rows and imports less rows than the total lines in the CSV file, this may not indicate a problem with the import since the blank rows wouldn't need to be imported. Check the number of lines that were correctly imported and make sure it matches the number of users you're attempting to import.

#### Missing row

There are a few reasons why the number of users imported might not match the total rows in your CSV file:

| Issue | Resolution |
|---|---|
| Duplicate external IDs, user aliases, Braze IDs, email addresses, or phone numbers | If there are duplicate external ID columns, this may cause malformed or unimported rows even if the rows are correctly formatted. In some cases, this may not report a specific error. Check for duplicates and remove them before re-uploading. |
| Accented characters | Your CSV may include names or attributes with accents. Ensure the file is UTF-8 encoded to prevent import issues. |
| Braze ID belongs to an orphaned user | If a user was merged into another and Braze cannot associate the Braze ID with the remaining profile, the row won't be imported. |
| Empty row | Blank rows in the CSV can cause malformed data errors. Check using a plain text editor, not Excel or Sheets. |
| Including double quotation marks (`"` ) | This character is invalid and will cause a malformed row. Use single quotation marks (`'`) instead. |
| Inconsistent line breaks | Mixed line breaks (e.g., `\n` and `\r\n`) may cause the first row of data to be treated as part of the header. Use a hex or advanced text editor to inspect and fix. |
| Incorrectly encoded file | Even if accents are allowed, the file must be UTF-8 encoded. Other encodings may work partially but are not fully supported. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### String quotation

Values encapsulated in single (`''`) or double (`""`) quotation marks will be read as strings on import.

#### Incorrectly formatted dates

Dates not in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format won't be read as `datetimes` on import.

### Data structure issues

#### Invalid email addresses

If your upload completed with errors, there may be one or more invalid encrypted email addresses. Confirm that all email addresses are encrypted properly before importing them into Braze.

- **When [updating or importing email address]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)** in Braze, use the hashed email value wherever an email is included. These hash email values are provided by your internal team. 
- **When creating a new user**, you must add `email_encrypted` with the user’s encrypted email value. Otherwise, the user will not be created. Similarly, if you’re adding an email address to an existing user who doesn’t have an email, you must add `email_encrypted`. Otherwise, the user won't be updated.

#### Data imported as custom attribute

If a piece of default user data (such as `email` or `first_name`) is imported as a custom attribute, check the case and spacing of your CSV file. For example, `First_name` would be imported as a custom attribute, while `first_name` would be correctly imported into the "first name" field on a user's profile.

#### Multiple data types

Braze expects each value in a column to be of the same data type. Values that don't match their attribute's data type will cause errors in segmenting.

Additionally, beginning a number attribute with zero will cause issues because numbers starting with zeros are considered strings. When Braze converts that string, it may be treated like an octal value (which uses digits from zero to seven), meaning it will be converted to its corresponding decimal value. For example, if the value in the CSV file is 0130, the Braze profile will show 88. To prevent this issue, use attributes with string datatypes. However, this data type isn't available in the segmentation number comparison.

#### Default attribute types

Some default attributes may only accept certain values as valid for user updates. For guidance, refer to [Constructing your CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Trailing spaces and differences in capitalization can cause a value to be interpreted as invalid. For example, in the following CSV file, only the user in the first row (`brazetest1`) will have their email and push statuses updated successfully because the accepted values are `unsubscribed`, `subscribed`, and `opted_in`. 

```plaintext
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### "Select CSV File" is not working

There are several reasons the **Select CSV File** button may not work:

| Issue | Resolution |
|---|---|
| Pop-up blocker | This may prevent the page from displaying. Confirm that your browser is allowing pop-ups on the Braze dashboard website. |
| Outdated browser | Make sure your browser is up to date; if not, update it to the latest version. |
| Background processes | Close every browser instance, then restart your computer. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
