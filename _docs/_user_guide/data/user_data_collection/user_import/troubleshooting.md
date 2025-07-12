---
nav_title: Troubleshooting
article_title: "ARTICLE_TITLE"
description: "SHORT_DESCRIPTION."
page_order: 10
---

# Troubleshooting user import

> If you’re having trouble with user import, review these common issues first. If it continues, reach out to [support@braze.com](mailto:support@braze.com).

## Malformed row

If your upload completed with errors, there may be a malformed row in your CSV file. 

To properly import data, there must be a header row. Each row must have the same number of cells as the header row. Rows with a length of more or fewer values than the header row will be excluded from the import. Commas in a value will be interpreted as a separator and can lead to this error. Additionally, all data must be UTF-8 encoded.

If your CSV file has blank rows and imports less rows than the total lines in the CSV file, this may not indicate a problem with the import since the blank rows wouldn't need to be imported. Check the number of lines that were correctly imported and make sure it matches the number of users you're attempting to import.

## Invalid email addresses

If your upload completed with errors, there may be one or more invalid encrypted email addresses. Confirm that all email addresses are encrypted properly before importing them into Braze.

- **When [updating or importing email address]({{site.baseurl}}/user_guide/analytics/field_level_encryption/#step-3-import-and-update-users)** in Braze, use the hashed email value wherever an email is included. These hash email values are provided by your internal team. 
- **When creating a new user**, you must add `email_encrypted` with the user’s encrypted email value. Otherwise, the user will not be created. Similarly, if you’re adding an email address to an existing user who doesn’t have an email, you must add `email_encrypted`. Otherwise, the user won't be updated.

## Missing rows

There are a few reasons why the number of users imported might not match the total rows in your CSV file:

- **Duplicate external IDs, user aliases, Braze IDs, email addresses, or phone numbers:** If there are duplicate external ID columns, this may cause malformed or unimported rows even if the rows are correctly formatted. In some cases, this may not report a specific error. Check if there are any duplicate external IDs in your CSV. If so, remove the duplicates and try uploading again.
- **Accented characters:** Your CSV may have names or attributes that include accents. Ensure your file is UTF-8 encoded to prevent any issues.
- **Braze ID belongs to an orphaned user:** When a user is orphaned, the remaining user with whom the orphan was merged may still not associate the orphaned user's Braze ID with the profile. In this case, Braze won't find a user to update, so the row won't count as imported.
- **Empty row:** There is a blank row in the CSV file. This can be checked if you open the CSV in a text editor program (don't use Excel or Sheets). If you upload the CSV with an empty row, there will be an error message saying there are rows with malformed data.
- **Including double quotation marks (`"`):** This character isn't valid and will make the row malformed. Instead, use single quotation marks (`'`).
- **Inconsistent line breaks:** For example, if the CSV file uses `\n` for the first line and `\r\n` for each subsequent line, the first row of data will be processed as part of the header, and that data won't be imported as expected. You can check this in a hex editor or a specialized text editor that distinguishes whitespace characters.
- **Incorrectly encoded file:** The CSV file can include names or attributes that have accents, but the file must be encoded to UTF-8 to properly import them. Other character encodings may work in some instances, but only UTF-8 is fully compatible.

## Incorrectly formatted dates

Dates not in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format won't be read as `datetimes` on import.

## String quotation

Values encapsulated in single (`''`) or double (`""`) quotation marks will be read as strings on import.

## Data imported as custom attribute

If a piece of default user data (such as `email` or `first_name`) is imported as a custom attribute, check the case and spacing of your CSV file. For example, `First_name` would be imported as a custom attribute, while `first_name` would be correctly imported into the "first name" field on a user's profile.

## Multiple data types

Braze expects each value in a column to be of the same data type. Values that don't match their attribute's data type will cause errors in segmenting.

Additionally, beginning a number attribute with zero will cause issues because numbers starting with zeros are considered strings. When Braze converts that string, it may be treated like an octal value (which uses digits from zero to seven), meaning it will be converted to its corresponding decimal value. For example, if the value in the CSV file is 0130, the Braze profile will show 88. To prevent this issue, use attributes with string datatypes. However, this data type isn't available in the segmentation number comparison.

## Default attribute types

Some default attributes may only accept certain values as valid for user updates. For guidance, refer to [Constructing your CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#constructing-your-csv).

Trailing spaces and differences in capitalization can cause a value to be interpreted as invalid. For example, in the following CSV file, only the user in the first row (`brazetest1`) will have their email and push statuses updated successfully because the accepted values are `unsubscribed`, `subscribed`, and `opted_in`. 

```
external_id,email,email_subscribe,push_subscribe
brazetest1,test1@braze.com,unsubscribed,unsubscribed
brazetest2,test2@braze.com,Unsubscribed,Unsubscribed
```

## "Select CSV File" button doesn't work

There are several reasons the **Select CSV File** button may not work:

- **Pop-up blocker:** This may prevent the page from displaying. Confirm that your browser is allowing pop-ups on the Braze dashboard website. 
- **Outdated browser:** Make sure your browser is up to date; if not, update it to the latest version.
- **Background processes:** Close every browser instance, then restart your computer.
