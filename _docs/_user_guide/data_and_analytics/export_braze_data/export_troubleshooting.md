---
nav_title: Export Troubleshooting
page_order: 10

page_type: reference
description: "This reference article covers some common troubleshooting scenarios for API and CSV exports"
---

# Export Troubleshooting

Here are some error messages and FAQs you may encounter while exporting data via CSV or API from Braze.

## Common Errors
#### ‘AccessDenied’ 
If you are using __your own S3 bucket__, this could happen because:
- The expected object is no longer in the S3 bucket; check with your engineers.
- The configured S3 credentials within the Braze dashboard do not have the correct permissions; confirm the proper credentials with your team.

If you are using __Braze’s S3 bucket__, this could happen because:
- The object is no longer there. This could occur if you clicked on a link for an export that ran 4+ hours ago. If this is the case, please re-run your export.
- You clicked on the download link right away, before the S3 was ready to serve the object. Please wait a few minutes and try again. Larger reports will generally take longer. 
- The export is too big, so our server ran out of memory trying to create this zip file. We’ll automatically email the user attempting this export if this occurs. If you consistently run into this issue, we recommend that you use your own S3 buckets in the future.

#### ‘ExpiredToken’
This will happen if the email was sent 4+ hours ago. Re-run the export and download it within 4 hours.
This could also be caused by Braze no longer having access to the S3 bucket you are downloading the data to. Make sure you’ve updated your S3 credentials using these steps.

#### "Looks like the file doesn't exist anymore, please check to make sure nothing is deleting objects from your bucket"
There may be a slight lag between when Braze's email with the export gets sent, and when S3 is actually ready to serve the object. If you see this error, wait a few minutes before trying again.


## FAQs

{% details Why did I receive multiple files when exporting user profiles to S3? %}
This is expected behavior for app groups with a lot of users. We split your export into multiple files, based on the number of users in your app group. Generally, there is 1 file output per 5k users. Note that if you are exporting a small segment within a large app group, you may still receive multiple files. 
{% enddetails %}

{% details What happens if you set up S3 credentials in the dashboard, but do not check the box for "make this the default data export destination?" %}
That checkbox will impact whether exports go to S3 or Azure, assuming you've added credentials for both. 
{% enddetails %}

{% details Do I have to add S3 credentials to Braze to export data? %}
No. Customers who do not add S3 credentials will have all of their exports appear in an S3 bucket belonging to Braze
{% enddetails %}

{% details Is there a way for certain exports to appear in the customer's S3 bucket, and certain exports to not? %}
No. if you have provided S3 credentials, all your exports will appear in your S3 bucket; otherwise, if no credentials are provided, all exports will appear in an S3 bucket belonging to Braze.
{% enddetails %}

{% details Why do I see duplicates when I export users by segment via REST API? %}
This is a very rare edge case caused by the underlying architecture of the database provider. Duplicates are cleaned out every week; however, most weeks, there are no duplicates cleared. 
{% enddetails %}

