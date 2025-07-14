---
nav_title: User Import
article_title: User Import
page_order: 4
description: "Learn about Braze's various user import options, like CSV import, REST API, Cloud Data Ingestion, and more."

---
# User import

> Learn about Braze's various user import options, like CSV import, REST API, Cloud Data Ingestion, and more.

## About HTML validation

Keep in mind that Braze does not sanitize, validate, or reformat HTML data during import, meaning script tags must be removed from all import data you use for web personalization.

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

## Import options

### Braze CSV import

You can use CSV import to record and update the following user attributes and custom events. To get started, see [CSV Import]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

|Type|Definition|Example|Maximum file size|
|---|---|---|---|
|Default Attributes|Reserved user attributes recognized by Braze.|`first_name`, `email`|500 MB|
|Custom Attributes|User attributes unique to your business.|`last_destination_searched`|500 MB|
|Custom Events|Events unique to your business that represent user actions.|`trip_booked`|50 MB|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

### Lambda user CSV import

You can use our serverless S3 Lambda CSV import script to upload user attributes to Braze. This solution works as a CSV uploader where you drop your CSVs into an S3 bucket, and the scripts upload it through our API.

Estimated execution times for a file with 1,000,000 rows should be around five minutes. See [User attribute CSV to Braze import](https://www.braze.com/docs/user_guide/data/cloud_ingestion/) for more information.

### REST API

Use the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to record custom events, user attributes, and purchases for users.

### Cloud Data Ingestion

Use Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/) to import and maintain user attributes. 

## Creating a retargeting filter from a user import

User import can be used to turn the CSV file into a retargeting filter by selecting **Import users in this CSV and make it possible to retarget this specific batch of users as a group**. To filter by the file in a segment or wherever filtering is an option, select the **Updated/Imported from CSV** filter and then search for the file's exact name.

![A filter group with the "Updated/Imported from CSV" filter including a CSV file titled "Halloween season fun".]({% image_buster /assets/img/csvfilter.png %})

## Creating segments from a user import

User import can also be used to create segments by selecting **Import users in this CSV and make it possible to retarget this specific batch of users as a group** and checking **Automatically generate a segment from the users who are imported from this CSV** before starting the import.

You can set the name of the segment or accept the default, which is the name of your file. Files that were used to create a segment will have a link to view the segment after the import has been completed.

The filter used to create the segment selects users who were created or updated in a selected import and is available with all other filters in the edit segment page.

## About legally required transactional emails

{% multi_lang_include email-via-sms-warning.md %}
