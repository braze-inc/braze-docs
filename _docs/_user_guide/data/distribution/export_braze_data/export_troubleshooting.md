---
nav_title: Export troubleshooting
article_title: Export Troubleshooting
page_order: 10
page_type: reference
description: "This reference article covers some common troubleshooting scenarios for API and CSV exports."

---

# Export troubleshooting

> This page lists error messages you may encounter while exporting data through CSV or API from Braze.

## Common errors

### 'AccessDenied' 

#### When using your own S3 bucket

If you're using **your own S3 bucket**, this could happen because:

- The expected object is no longer in the S3 bucket; check with your engineers.
- The configured S3 credentials within the Braze dashboard don't have the correct permissions; confirm the proper credentials with your team.

#### When using a Braze S3 bucket

If you're using a **Braze S3 bucket**, this could happen because:

- The object is no longer there. This could occur if you clicked on a link for an export that expired, as files are automatically deleted from S3 when the download link expires. Unless otherwise noted, files are removed after four hours. If this is the case, re-run your export.
- You selected the download link right away, before the S3 was ready to serve the object. Wait a few minutes and try again. Larger reports will generally take longer. 
- The export is too big, so our server ran out of memory trying to create this zip file. We'll automatically email the user attempting this export if this occurs. If you consistently run into this issue, we recommend that you use your own S3 buckets in the future.

### 'ExpiredToken'

This happens if the email was sent long enough ago that the S3 file has expired. Unless otherwise noted, files are removed after four hours. Re-run the export and download it before the file expires.

This could also be caused by Braze no longer having access to the S3 bucket you are downloading the data to. Make sure you've updated your S3 credentials using these steps.

### "Looks like the file doesn't exist anymore, please check to make sure nothing is deleting objects from your bucket"

There may be a slight lag between when Braze's email with the export gets sent, and when S3 is actually ready to serve the object. If you see this error, wait a few minutes before trying again.

### Apostrophes added to fields

Braze will automatically prepend an apostrophe to a field in the CSV export if the field begins with any of the following characters:

- -
- =
- +
- @

For example, the field "-1943" will export as "'-1943". This doesn't apply to JSON exports, such as those returned by the [`/users/export/segment` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).