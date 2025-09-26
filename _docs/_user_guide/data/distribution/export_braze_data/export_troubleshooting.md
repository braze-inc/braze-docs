---
nav_title: Export troubleshooting
article_title: Export troubleshooting
page_order: 10
page_type: reference
description: "This reference article covers common troubleshooting scenarios for exports in both CSV and API workflows."
---

# Export troubleshooting

> This page covers common troubleshooting scenarios for exports in both CSV and API workflows.  
Use the tabs to select whether you’re exporting to the **default Braze S3 bucket** or to a **cloud storage partner**.

{% sdktabs %}
{% sdktab Default export %}

When you don’t have a storage partner marked as your default export destination, Braze uses its own Amazon S3 bucket to hold your export files. Files in this setup are temporary and expire after four hours.  

## CSV exports  
When you export a CSV from the dashboard, Braze emails a download link to the logged-in user. That link points to a ZIP file hosted in Braze’s S3 bucket. Inside the ZIP are multiple smaller files that together make up your export.  

You need to be logged into the Braze dashboard to use the link, and the file will only be available for four hours. After that, the link no longer works and the data is deleted. If you run into repeated failures with very large exports (over 500,000 users), the export may fail. In that case, try splitting your export into smaller groups or fields, or consider setting up a storage partner.  

### Common errors

- If you see an `AccessDenied` error, the file may have already expired or you may have tried to open it before it was ready. Larger reports take longer to generate, so wait a few minutes and try again.  
- An `ExpiredToken` error means the four-hour window has passed. Re-run the export to generate a fresh link.  
- The message *“Looks like the file doesn’t exist anymore”* usually appears when the email is sent but the file hasn’t finished uploading to S3. Waiting a few minutes typically resolves it.  
- Apostrophes added at the start of certain fields (like `-`, `=`, `+`, or `@`) are expected. Braze does this to prevent spreadsheet programs from misinterpreting the data.  

## API exports  
When you export through the Export APIs without cloud storage, Braze writes the files to its S3 bucket. You won’t receive an email—instead, the API response includes a temporary download URL. The export comes as a ZIP containing multiple JSON files, each with one user per line.  

Like CSV exports, links from the API expire after four hours. If you click the link too early, you may see errors because the file isn’t ready yet. You can provide a `callback_endpoint` in your request if you want Braze to notify you when the file is available.  

Large API exports can also time out. If that happens, try making smaller requests or connect a storage partner to handle the volume.  

### Common errors  
- `AccessDenied` or `ExpiredToken` typically mean the link expired or wasn’t ready yet. Run the export again or wait a bit longer.  

{% endsdktab %}

{% sdktab Cloud storage connected %}

When you connect a storage partner (such as Amazon S3, Google Cloud Storage, or Azure Blob) and mark it as your default export destination from the **Technology Partners** page in the dashboard, Braze writes your exports directly to your bucket. This setup is typically more reliable for larger exports.  

## CSV exports  
With CSV exports, Braze emails you a download link. That link expires after four hours, just like with the default setup. The difference is that a duplicate copy of the export is also written to your connected bucket, where expiration and retention follow your own policies.  

In cloud storage, CSV exports aren’t bundled into a single ZIP. Instead, you’ll see multiple smaller files—typically around 5,000 users each, though sometimes fewer. That doesn’t necessarily indicate missing data. If the emailed link fails but the copy in your storage succeeds, you can always retrieve your data directly from your bucket.  

### Common errors

- `AccessDenied` means Braze couldn’t write to your bucket. Double-check that your credentials and permissions are still valid.  
- `ExpiredToken` appears if Braze has lost access to your bucket. Update your credentials in the Braze dashboard.  
- If some files look smaller than expected, that’s normal behavior. The export process intentionally splits files for stability.  

## API exports  
When you export data through the APIs with a storage partner connected, files are written directly to your bucket. No email is sent, and expiration is determined by your storage settings. Each file contains JSON objects, one per line. Large exports create multiple files instead of a single ZIP, which makes this method more reliable for heavy exports.  

### Common errors

- `AccessDenied` happens when Braze can’t write to your bucket or the objects were deleted afterward. Check permissions and confirm nothing external is clearing files.  
- `ExpiredToken` means Braze’s access credentials to your bucket are outdated. Refresh them in the dashboard.  
- If files are missing or smaller than expected, first confirm that nothing outside Braze is deleting objects. Smaller file sizes themselves are expected.  

{% endsdktab %}
{% endsdktabs %}