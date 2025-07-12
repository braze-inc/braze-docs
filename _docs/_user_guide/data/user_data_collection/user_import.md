---
nav_title: User Import
article_title: User Import
page_order: 4
page_type: reference
description: "This reference article covers how to import users into your Braze dashboard using the REST API, Cloud Data Ingestion, CSV, and importing best practices."

---
# User import

> Braze offers a variety of ways to import user data into the platform: SDKs, APIs, Cloud Data Ingestion, technology partner integrations, and CSV files.

## About HTML validation

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

## Options for importing users

### REST API

Use the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to record custom events, user attributes, and purchases for users.

### Cloud Data Ingestion

Use Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/) to import and maintain user attributes. 

### Braze CSV import

You can upload and update user profiles though CSV files from **Audience** > **Import Users**.

CSV import supports recording and updating user attributes such as first name and email, in addition to custom attributes such as shoe size. You can import a CSV by specifying one of two unique user identifiers: an `external_id` or a user alias.

{% alert note %}
If you're uploading a mix of users with an `external_id` and users without, you need to create one CSV for each import. One CSV can't contain both `external_ids` and user aliases.
{% endalert %}

### Lambda user CSV import

You can use our serverless S3 Lambda CSV import script to upload user attributes to Braze. This solution works as a CSV uploader where you drop your CSVs into an S3 bucket, and the scripts upload it through our API.

Estimated execution times for a file with 1,000,000 rows should be around five minutes. See [User attribute CSV to Braze import](https://www.braze.com/docs/user_guide/data/cloud_ingestion/) for more information.

## Creating a retargeting filter from a user import

User import can be used to turn the CSV file into a retargeting filter by selecting **Import users in this CSV and make it possible to retarget this specific batch of users as a group**. To filter by the file in a segment or wherever filtering is an option, select the **Updated/Imported from CSV** filter and then search for the file's exact name.

![A filter group with the "Updated/Imported from CSV" filter including a CSV file titled "Halloween season fun".]({% image_buster /assets/img/csvfilter.png %})

## Creating segments from a user import

User import can also be used to create segments by selecting **Import users in this CSV and make it possible to retarget this specific batch of users as a group** and checking **Automatically generate a segment from the users who are imported from this CSV** before starting the import.

You can set the name of the segment or accept the default, which is the name of your file. Files that were used to create a segment will have a link to view the segment after the import has been completed.

The filter used to create the segment selects users who were created or updated in a selected import and is available with all other filters in the edit segment page.

## About legally required transactional emails

{% multi_lang_include email-via-sms-warning.md %}
