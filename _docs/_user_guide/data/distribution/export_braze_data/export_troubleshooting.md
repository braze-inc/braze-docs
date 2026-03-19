---
nav_title: Export troubleshooting
article_title: Export Troubleshooting
page_order: 10
page_type: reference
description: "This reference article covers common troubleshooting scenarios for exports in both CSV and API workflows."
---

# Export troubleshooting

> This page covers common troubleshooting scenarios for exports in both CSV and API workflows.  

Use the tabs to select whether you're exporting to the **default Braze S3 bucket** or to a **cloud storage partner**.

{% sdktabs %}
{% sdktab Default export %}

When you don't have a storage partner marked as your default export destination, Braze uses its own Amazon S3 bucket to hold your export files. Files in this setup are temporary and expire after four hours.  

## CSV exports  
When you export a CSV from the dashboard, Braze emails a download link to the logged-in user. That link points to a ZIP file hosted in Braze's S3 bucket. Inside the ZIP are multiple smaller files that together make up your export.  

You must be logged in to the Braze dashboard to use the link, and the file is available for only four hours. After that, the link no longer works and the data is deleted. If you run into repeated failures with very large exports (over 500,000 users), the export may fail. In that case, try splitting your export into smaller groups or fields, or consider setting up a storage partner.  

### Common errors

- If you see an `AccessDenied` error, the file may have already expired or you may have tried to open it before it was ready. Larger reports take longer to generate, so wait a few minutes and try again.  
- An `ExpiredToken` error means the four-hour window has passed. Re-run the export to generate a fresh link.  
- The message `Looks like the file doesn't exist anymore` usually appears when the email is sent but the file hasn't finished uploading to S3. Waiting a few minutes typically resolves it.  
- Apostrophes added at the start of certain fields (like `-`, `=`, `+`, or `@`) are expected. For example, `-1943` becomes `'-1943` in the CSV. Braze does this to prevent spreadsheet programs from misinterpreting the data. This doesn't apply to JSON exports, such as those returned by the [`/users/export/segment` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).  

## API exports  
When you export through the Export APIs without cloud storage, Braze writes the files to its S3 bucket. You won't receive an email—instead, the API response includes a temporary download URL. The export comes as a ZIP containing multiple JSON files, each with one user per line.  

Like CSV exports, links from the API expire after four hours. If you click the link too early, you may see errors because the file isn't ready yet. You can provide a `callback_endpoint` in your request if you want Braze to notify you when the file is available.  

Large API exports can also time out. If that happens, try making smaller requests or connect a storage partner to handle the volume.  

### Common errors  
- `AccessDenied` or `ExpiredToken` typically mean the link expired or wasn't ready yet. Run the export again or wait a bit longer.  

{% endsdktab %}

{% sdktab Cloud storage connected %}

When you connect a storage partner (such as Amazon S3, Google Cloud Storage, or Azure Blob) and mark it as your default export destination from the **Technology Partners** page in the dashboard, Braze writes your exports directly to your bucket. This setup is typically more reliable for larger exports.  

## CSV exports  
With CSV exports, Braze emails you a download link. That link expires after a short window (typically around four hours). When you have a storage partner connected and marked as your default export destination, Braze also delivers a copy of the export to your connected bucket. That copy lives in your own infrastructure, where expiration and retention follow your storage policies.  

In cloud storage, CSV exports are bundled into a ZIP file. Inside the ZIP are multiple smaller CSV files. Large exports are often split into chunks (for example, around 5,000 users each), and chunk size can vary. Smaller files don't indicate missing data. If the emailed link fails but the copy in your storage succeeds, you can always retrieve your data directly from your bucket.  

### Common errors

- `AccessDenied` means Braze couldn't write to your bucket. Double-check that your credentials and permissions are still valid.  
- `ExpiredToken` appears if Braze has lost access to your bucket. Update your credentials in the Braze dashboard.  
- If some files look smaller than expected, that's normal behavior. The export process intentionally splits files for stability.  
- Apostrophes added at the start of certain fields (like `-`, `=`, `+`, or `@`) are expected. For example, `-1943` becomes `'-1943` in the CSV. Braze does this to prevent spreadsheet programs from misinterpreting the data. This doesn't apply to JSON exports, such as those returned by the [`/users/export/segment` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).  

## API exports  
When you export data through the APIs with a storage partner connected, the export files are written to your bucket. No email is sent. The underlying objects live in your storage and follow your retention settings, even though the download URLs Braze returns may still be time-limited. Each ZIP file contains JSON objects, one per line. Large exports may be split into multiple ZIP files instead of a single ZIP, which generally makes this method more reliable for heavy exports.  

### Common errors

- `AccessDenied` happens when Braze can't write to your bucket or the objects were deleted afterward. Check permissions and confirm nothing external is clearing files.  
- `ExpiredToken` means Braze's access credentials to your bucket are outdated. Refresh them in the dashboard.  
- If files are missing or smaller than expected, first confirm that nothing outside Braze is deleting objects. Smaller file sizes themselves are expected.  

{% endsdktab %}
{% endsdktabs %}