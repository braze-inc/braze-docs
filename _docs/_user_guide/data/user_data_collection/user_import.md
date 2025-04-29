---
nav_title: User Import
article_title: User Import
page_order: 4
page_type: reference
description: "This reference article covers how to import users into your Braze dashboard using the REST API, Cloud Data Ingestion, CSV, and importing best practices."

---
# User import

> Braze offers a variety of ways to import user data into the platform: SDKs, APIs, Cloud Data Ingestion, technology partner integrations, and CSV files.

Before proceeding, note that Braze does not sanitize (validate or properly format) HTML data during import. This means that script tags must be stripped for all import data meant for web personalization.

When importing data into Braze that is specifically meant for personalization usage in a web browser, ensure that it is stripped of HTML, JavaScript, or any other script tag that potentially could be leveraged maliciously when rendered in a web browser.  

Alternatively, for HTML, you can use Braze Liquid filters (`strip_html`) to HTML-escape rendered text. For example:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}

## REST API

Use the [`/users/track` endpoint][12] to record custom events, user attributes, and purchases for users.

## Cloud Data Ingestion

Use Braze [Cloud Data Ingestion][14] to import and maintain user attributes. 

## CSV import

You can upload and update user profiles though CSV files from **Audience** > **Import Users**.

CSV import supports recording and updating user attributes such as first name and email, in addition to custom attributes such as shoe size. You can import a CSV by specifying one of two unique user identifiers: an `external_id` or a user alias.

{% alert note %}
If you're uploading a mix of users with an `external_id` and users without, you need to create one CSV for each import. One CSV can't contain both `external_ids` and user aliases.
{% endalert %}

### Constructing your CSV

There are several data types in Braze. When importing or updating user profiles with a CSV file, you can create or update default user attributes or custom attributes.

- Default user attributes are reserved keys in Braze. For example, `first_name` or `email`.
- Custom attributes are custom to your business. For example, a travel booking app may have a custom attribute called `last_destination_searched`.

{% alert important %}
When importing customer data, the column headers you use must exactly match the spelling and capitalization of default user attributes. Otherwise, Braze will automatically create a custom attribute on that user's profile.
{% endalert %}

Braze accepts user data in the standard CSV format from files up to 500&nbsp;MB in size. Refer to the preceding sections on importing for downloadable CSV templates.

#### Data point considerations

Each piece of customer data imported from a CSV file will overwrite the existing value on user profiles and count as a data point, except for external IDs and blank values. 

- External IDs uploaded from a CSV file will not consume data points. If you are uploading a CSV to segment existing Braze users by uploading only external IDs, this can be done without consuming data points. If you were to add additional data like user emails or phone numbers in your import, that would overwrite existing user data, consuming your data points.
  - CSV imports for segmentation purposes (imports made with `external_id`, `braze_id`, or `user_alias_name` as the only field) will not consume data points.
- Blank values will not overwrite existing values on the user profile, and you do not need to include all existing user attributes in your CSV file.
- Updating `email_subscribe`, `push_subscribe`, `subscription_group_id`, or `subscription_state` will not count toward data point consumption.

{% alert important %}
Setting `language` or `country` on a user through CSV import or API will prevent Braze from automatically capturing this information through the SDK.
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
| `date_of_first_session` <br><br> `date_of_last_session`| String | May be passed in one of the following ISO 8601 formats: {::nomarkdown} <ul> <li> "YYYY-MM-DD" </li> <li> "YYYY-MM-DDTHH:MM:SS+00:00" </li> <li> "YYYY-MM-DDTHH:MM:SSZ" </li> <li> "YYYY-MM-DDTHH:MM:SS" (for example, 2019-11-20T18:38:57) </li> </ul> {:/} | No |
| `subscription_group_id` | String | The `id` of your subscription group. This identifier can be found on the subscription group page of your dashboard. | No |
| `subscription_state` | String | The subscription state for the subscription group specified by `subscription_group_id`. Allowed values are `unsubscribed` (not in subscription group) or `subscribed` (in subscription group). | No, but strongly recommended if `subscription_group_id` is used |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
While `external_id` itself is not mandatory, you **must** include one of these fields:
- `external_id`: A unique user identifier for your customer <br> - OR -
- `braze_id`: A unique user identifier pulled for existing Braze users <br> - OR -
- `user_alias_name`: A unique user identifier for an anonymous user
{% endalert %}

### Importing a CSV

To import your CSV file, go to **Audiences** > **User Import**. Here, you'll find a table that lists the most recent imports, which includes details such as the upload date, the uploader's name, file name, targeting availability, number of imported rows, and status of each import.

![The 'Import Users' page in the Braze dashboard.][3]

Select **Browse Files** and your file. Braze will upload your file and check the column headers and the data types of each column.

To download a CSV template, refer to the sections [Importing with external ID](#importing-with-external-id) or [Importing with user alias](#importing-with-user-alias) on this page.

{% alert important %}
CSV imports are case sensitive. This means capital letters in CSV imports will write the field as a custom attribute instead of a standard one. For example, "email" is correct, but "Email" would be written as a custom attribute.
{% endalert %}

After the upload is completed, you'll see a modal with a preview of the contents of your file. All the information in this table is based on the values in the top few rows of your CSV file. For column headers, standard attributes are written in normal text, while custom attributes are italicized and have their type noted in parentheses. There is also a summary of your file at the top of the pop-up.

You can import more than one CSV at the same time. CSV imports run concurrently, so the order of updates is not guaranteed to be serial. If you require CSV imports to run one after another, wait until a CSV import has finished before uploading a second one.

If Braze notices something malformed in your file during the upload, these errors will show with the summary. For example, if your file includes a malformed row, that error is noted in the preview when you import the file. So, a file can be imported with errors, but an import can't be canceled or rolled-back after it's started. Review the preview, and if you find any errors, cancel the import and modify your file. 

{% alert important %}
Examine the full CSV file before upload, as Braze doesn't scan every row of the input file for the preview. This means errors can exist that Braze doesn't catch while generating this preview.
{% endalert %}

Malformed rows and rows lacking an external ID will not be imported. All other errors can be imported, but may interfere with filtering when creating a segment. For more information, skip to the [Troubleshooting](#troubleshooting) section.

![CSV upload completed with errors involving mixed data types in a single column][4]{: style="max-width:70%"}

{% alert warning %}
Errors are based solely on data type and file structure. For example, a poorly formatted email address would still be imported as it can still be parsed as a string.
{% endalert %}

When you're satisfied with the upload, start the import. The pop-up will close and the import will begin in the background. You can track its progress on the **User Import** page, which will refresh every five seconds, or at the press of the refresh button in the **Recent Imports** box.

Under **Lines Processed** is the progress of the import; the status will change to **Complete** when finished. You can still use the rest of the Braze dashboard during the import, and you'll receive notifications when the import begins and ends.

If the import process runs into an error, a yellow warning icon will display next to the total number of lines in the file. You can hover over the icon to see details about why certain lines failed. After the import is completed, all data will be added to existing profiles, or new profiles will be created.

### Importing with external ID

When importing your customer data, you'll need to specify each customer's unique identifier (`external_id`). Before starting your CSV import, it's important to understand from your engineering team how users will be identified in Braze. Typically, this is an internal database ID. This should align with how users will be identified by the Braze SDK on mobile and web and is designed for each customer to have a single user profile within Braze across their devices. Read more about the Braze [user profile lifecycle][13].

When you provide an `external_id` in your import, Braze will update any existing user with the same `external_id` or create a newly identified user with that `external_id` set if one is not found.

**Download:** [CSV Import Template][template]

### Importing with user alias

To target users who don't have an `external_id`, you can import a list of users with user aliases. An alias serves as an alternative unique user identifier, and can be helpful if you are trying to market to anonymous users who haven't signed up or made an account with your app.

If you are uploading or updating user profiles that are alias only, you must have the following two columns in your CSV:

- `user_alias_name`: A unique user identifier; an alternative to the `external_id`
- `user_alias_label`: A common label by which to group user aliases

| user_alias_name | user_alias_label | last_name | email | sample_attribute |
| --- | --- | --- | --- | --- |
| 182736485 | my_alt_identifier | Smith | smith@user.com | TRUE |
| 182736486 | my_alt_identifier | Nguyen | nguyen@user.com | FALSE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

When you provide both a `user_alias_name` and `user_alias_label` in your import, Braze will update any existing user with the same `user_alias_name` and `user_alias_label`. If a user isn't found, Braze will create a newly identified user with that `user_alias_name` set.

{% alert important %}
You can't use a CSV import to update an existing user with a `user_alias_name` if they already have an `external_id`. Instead, this will create a new user profile with the associated `user_alias_name`. To associate an alias-only user with an `external_id`, use the [Identify users endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).
{% endalert %}

**Download:** [CSV Alias Import Template][template_alias]

### Importing with Braze ID

To update existing user profiles in Braze by using an internal Braze ID value instead of an `external_id` or `user_alias_name` and `user_alias_label` value, specify `braze_id` as a column header.

This can be helpful if you exported user data from Braze through our CSV export option within segmentation and want to add a new custom attribute to those existing users.

{% alert important %}
You can't use a CSV import to create a new user using `braze_id`. This method can only be used to update pre-existing users within the Braze platform.
{% endalert %}

{% alert tip %}
The `braze_id` value might be labeled as `Appboy ID` in CSV exports from the Braze dashboard. This ID will be the same as the `braze_id` for a user, so you can rename this column to `braze_id` when you re-import the CSV.
{% endalert %}

### Importing with email addresses and phone numbers

You can omit an external ID or user alias and use either an email address or phone number to import users. Before importing a CSV file with email addresses or phone numbers, check for the following:

- Verify that you don’t have any external IDs or user aliases for these profiles in your CSV file. If you do, Braze will prioritize using the external ID or user alias before the email address to identify profiles.
- Confirm that your CSV file is formatted properly.

{% alert note %}
If you include both email addresses and phone numbers in your CSV file, the email address is prioritized over the phone number when looking up profiles.
{% endalert %}

If an existing profile has that email address or phone number, that profile will be updated, and Braze will not create a new profile. If there are multiple profiles with that same email address, Braze will use the same logic as the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) where the most recently updated profile will be updated.

If a profile with that email address or phone number doesn't exist, Braze will create a new profile with that identifier. You can use the [`/users/identify` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) to identify this profile later. To delete a user profile, you can also use the [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) endpoint.

### Importing custom data

Any headers that don't exactly match default user data will create a custom attribute within Braze.

The following data types are accepted in user import:
- **Datetime:** Must be stored in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format
- **Boolean:** `true` or `false`
- **Number:** Integer or float with no spaces or commas, floats must use a period (`.`) as the decimal separator
- **String:** Can contain commas if there are double-quotation marks (`""`) surrounding the column value
- **Blank:** Blank values won't overwrite existing values on the user profile, and you don't need to include all existing user attributes in your CSV file

{% alert important %}
Arrays, push tokens, and custom event data types aren't supported in user import.
Especially for arrays, commas in your CSV file will be interpreted as a column separator, so any commas in values will cause errors in parsing the file.<br><br>To upload these kinds of values, use the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) or [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/).
{% endalert %}

### Lambda user CSV import

You can use our serverless S3 Lambda CSV import script to upload user attributes to the platform. This solution works as a CSV uploader where you drop your CSVs into an S3 bucket, and the scripts upload it through our API.

Estimated execution times for a file with 1,000,000 rows should be around five minutes. See [User attribute CSV to Braze import]({{site.baseurl}}/user_guide/data/cloud_ingestion/) for more information.

### Updating subscription group status

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

## Creating a retargeting filter from a user import

User import can be used to turn the CSV file into a retargeting filter by selecting **Import users in this CSV and make it possible to retarget this specific batch of users as a group**. To filter by the file in a segment or wherever filtering is an option, select the **Updated/Imported from CSV** filter and then search for the file's exact name.

![A filter group with the "Updated/Imported from CSV" filter including a CSV file titled "Halloween season fun".][5]

## Creating segments from a user import

User import can also be used to create segments by selecting **Import users in this CSV and make it possible to retarget this specific batch of users as a group** and checking **Automatically generate a segment from the users who are imported from this CSV** before starting the import.

You can set the name of the segment or accept the default, which is the name of your file. Files that were used to create a segment will have a link to view the segment after the import has been completed.

The filter used to create the segment selects users who were created or updated in a selected import and is available with all other filters in the edit segment page.

## Considerations

{% multi_lang_include email-via-sms-warning.md %}

## Troubleshooting

###  Upload completed with errors

#### Malformed row

There must be a header row to properly import data. Each row must have the same number of cells as the header row. Rows with a length of more or fewer values than the header row will be excluded from the import. Commas in a value will be interpreted as a separator and can lead to this error. Additionally, all data must be UTF-8 encoded.

If your CSV file has blank rows and imports less rows than the total lines in the CSV file, this may not indicate a problem with the import since the blank rows wouldn't need to be imported. Check the number of lines that were correctly imported and make sure it matches the number of users you're attempting to import.

#### Invalid email addresses

Braze detected invalid encrypted email addresses. Confirm that all email addresses are encrypted properly before importing them into Braze.

- **When [updating or importing email address]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)** in Braze, use the hashed email value wherever an email is included. These hash email values are provided by your internal team. 
- **When creating a new user**, you must add `email_encrypted` with the user’s encrypted email value. Otherwise, the user will not be created. Similarly, if you’re adding an email address to an existing user who doesn’t have an email, you must add `email_encrypted`. Otherwise, the user won't be updated.

### Missing rows

There are a few reasons why the number of users imported might not match the total rows in your CSV file:

- **Duplicate external IDs, user aliases, Braze IDs, email addresses, or phone numbers:** If there are duplicate external ID columns, this may cause malformed or unimported rows even if the rows are correctly formatted. In some cases, this may not report a specific error. Check if there are any duplicate external IDs in your CSV. If so, remove the duplicates and try uploading again.
- **Accented characters:** Your CSV may have names or attributes that include accents. Ensure your file is UTF-8 encoded to prevent any issues.
- **Braze ID belongs to an orphaned user:** When a user is orphaned, the remaining user with whom the orphan was merged may still not associate the orphaned user's Braze ID with the profile. In this case, Braze won't find a user to update, so the row won't count as imported.
- **Empty row:** There is a blank row in the CSV file. This can be checked if you open the CSV in a text editor program (don't use Excel or Sheets). If you upload the CSV with an empty row, there will be an error message saying there are rows with malformed data.
- **Including double quotation marks (`"`):** This character isn't valid and will make the row malformed. Instead, use single quotation marks (`'`).
- **Inconsistent line breaks:** For example, if the CSV file uses `\n` for the first line and `\r\n` for each subsequent line, the first row of data will be processed as part of the header, and that data won't be imported as expected. You can check this in a hex editor or a specialized text editor that distinguishes whitespace characters.
- **Incorrectly encoded file:** The CSV file can include names or attributes that have accents, but the file must be encoded to UTF-8 to properly import them. Other character encodings may work in some instances, but only UTF-8 is fully compatible.

### Incorrectly formatted dates

Dates not in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format won't be read as `datetimes` on import.

### String quotation

Values encapsulated in single (`''`) or double (`""`) quotation marks will be read as strings on import.

### Data imported as custom attribute

If a piece of default user data (such as `email` or `first_name`) is imported as a custom attribute, check the case and spacing of your CSV file. For example, `First_name` would be imported as a custom attribute, while `first_name` would be correctly imported into the "first name" field on a user's profile.

### Multiple data types

Braze expects each value in a column to be of the same data type. Values that don't match their attribute's data type will cause errors in segmenting.

Additionally, beginning a number attribute with zero will cause issues because numbers starting with zeros are considered strings. When Braze converts that string, it may be treated like an octal value (which uses digits from zero to seven), meaning it will be converted to its corresponding decimal value. For example, if the value in the CSV file is 0130, the Braze profile will show 88. To prevent this issue, use attributes with string datatypes. However, this data type isn't available in the segmentation number comparison.

### Default attribute types

Some default attributes may only accept certain values as valid for user updates. For guidance, refer to [Constructing your CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Trailing spaces and differences in capitalization can cause a value to be interpreted as invalid. For example, in the following CSV file, only the user in the first row (`brazetest1`) will have their email and push statuses updated successfully because the accepted values are `unsubscribed`, `subscribed`, and `opted_in`. 

```
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

### "Select CSV File" button doesn't work

There are several reasons the **Select CSV File** button may not work:

- **Pop-up blocker:** This may prevent the page from displaying. Confirm that your browser is allowing pop-ups on the Braze dashboard website. 
- **Outdated browser:** Make sure your browser is up to date; if not, update it to the latest version.
- **Background processes:** Close every browser instance, then restart your computer.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/language_codes/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[3]: {% image_buster /assets/img/importcsv5.png %}
[4]: {% image_buster /assets/img/importcsv2.png %}
[5]: {% image_buster /assets/img/csvfilter.png %}
[7]: {% image_buster /assets/img/segment-imported-users.png %}
[8]: {% image_buster /assets/img_archive/user_alias_import_1.png %}
[9]: {% image_buster /assets/img/subscription_group_import.png %}
[12]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[13]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[14]: {{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/
[errors]:#common-errors
[template]: {% image_buster /assets/download_file/braze-user-import-template-csv.xlsx %}
[template_alias]: {% image_buster /assets/download_file/braze-user-import-alias-template-csv.xlsx %}
