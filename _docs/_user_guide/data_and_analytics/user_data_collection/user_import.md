---
nav_title: User Import
page_order: 13
---
# User Import

Braze's User Import feature allows users to upload and update user profiles via CSV files. This feature supports updating default and custom user profile attributes.

## Formatting
Braze accepts user data in the standard CSV format from files up to 100MB in size. The particulars of how to construct your file are described below.

### Column Headers

Braze expects that the first row in your CSV file will contain the headers for each column in the file. The number of columns in each row must match the number of headers.

Users imported to Braze via CSV *must* be identified -- Braze does not support creating entirely anonymous users via User Import. You must specify either a 'braze_id' or an 'external_id', but not both, allowing Braze to match an existing user.

* If you provide an `external_id`, we will update any existing user with the same `external_id` or create a new identified user with that `external_id` set if one is not found.

* If you provide a `braze_id`, we will update any existing user with the same `braze_id` but will not create a new identified user with that `braze_id` if one is not found since we do not allow entirely anonymous users via User Import.

All headers will be interpreted as custom attributes unless they match these [fields][fields] used with the user data REST API:

- braze_id
- external_id
- first_name
- last_name
- email
- dob
- country
- language
- home_city
- bio
- gender
- phone
- email_subscribe
- push_subscribe
- image_url

> All of these fields are of type String except for dob (date of birth). Take care to use the exact spelling and proper case for pre-existing user data fields.

### Values
These data types are accepted in User Import:

- Datetime (Must be stored in the [ISO 8601][date] format)
- Boolean (TRUE/FALSE)
- Number (Integer or Float with no spaces or commas, floats must use '.' as the decimal separator)
- String (no commas)
- Blank

Note that the following data types are __not supported__ in User Import:

- Arrays
- Push Tokens
- Custom Events

For uploading these kinds of values, please use our [User Data API][fields].

![GoodCSV][1]

Any value which is not formatted to match the Datetime, Boolean, Integer, or Float specifications will be read as a String. Each comma in the input will be interpreted as a column separator, therefore any commas in values will cause errors in parsing the file. In addition, all leading and trailing whitespace will be trimmed from each value. Otherwise, values will be stored exactly as stored in the input CSV file. Blank values will not overwrite existing values on the user profile, and you do not need to include all existing user attributes in your CSV file.

For segmentation, it is important that each column contains a consistent data type. Values which do not match the attribute's data type will not match the filters used to segment the attribute. In addition, for custom attributes whose data type is set as "Detect Automatically" on the dashboard, the most recently added value is used to set the data type of the attribute, so an error in your last row can interfere with proper segmentation.

During import, Braze determines the data type of each column by scanning a sample from the top rows of the file. Mixed data types in a column will not prevent you from importing your file, so we recommend exercising caution and ensuring the values in each column are consistent and match the data type you expect.

## Importing
To import your CSV file, navigate to the User Import page under the Users section on the left hand toolbar. In the lower text box, "Recent Imports", there will be a table which lists up to twenty of your most recent imports, their file names, number of lines in the file, number of lines successfully imported, total lines in each file, and the status of each import.

![User Import][3]

The upper box, "Import CSV", will contain importing directions and a button to begin your import. Press the "Select CSV File" button and select your file of interest, then press "Start Upload." Braze will upload your file and check the column headers as well as the data types of each column. Once the upload is complete, you will see a modal window with a table previewing the contents of your file. All the information in this table is based off of the values in top few rows of your CSV file. For column headers, default attributes will be written in normal text, while [custom attributes][CAO] will be italicized and have their type noted in parentheses. There will also be a short summary of your file at the top of the pop-up.

You can import more than one CSV at the same time. CSV imports will run concurrently, and as such the order of updates is not guaranteed to be serial. If you require CSV imports run in a serial fashion, you should wait until a CSV import has finished before uploading a second one.

![Errorless Import][4]

If Braze notices something malformed in your file during the upload, errors will be shown above the summary. A file can be imported with errors, but once started, an import cannot be cancelled or rolled-back. Review the preview, and if errors are found cancel the import and modify your file. It is important to examine the full file before upload as well. Braze does not scan every row of the input file at this stage; errors can exist which Braze does not catch while generating this preview. Malformed rows and rows lacking an external ID (A) will not be imported, all other [errors][errors] can be imported (B) but may interfere with filtering when [creating a segment][filtering]. Note that errors are based solely off of data type and file structure - for example, a poorly formatted email address (C) would still be imported as it can still be parsed as a string.

![Import Errors][5]

When you are satisfied with the upload, start the import. The pop-up will close and the import will begin in the background. You can track its progress on the User Import page, which will refresh every 5 seconds, or at the press of the refresh button in the Recent Imports box. Under Lines Processed, you will see the progress of the import; the status will change to Complete when finished. You can continue to navigate around other parts of the dashboard during the import, you will receive modal notifications when the import begins and ends.

When the import process runs into an error, a yellow warning icon will be displayed next to the total number of lines in the file. You can mouse over the icon to see details into why certain lines failed. Once the import is Complete, all data will have been added to existing profiles or all new profiles will have been created.

![Error Tooltip][6]

## Segmenting

User Import creates and updates user profiles, and can also be used to create segments. To create a segment, check the 'Create a segment from this CSV' box.

![Create a Segment][7]

You can set the name of the segment or accept the default, which is the name of your file. Files which were used to create a segment will have a link to view the segment once the import has completed.

![View the Segment][8]

The filter used to create the segment selects users who were created or updated in a selected import, and is available with all other filters in the edit segment page. Note that as of 4/10/2018, for each user, only the last 100 CSVs the user was imported/updated in are cached. So if you attempt to create a segment by filtering for members who were in an older import, the segment will not include users who have been in 100 or more imports since. Previous to 4/10/2018 Braze cached the last 10 CSVs that a user was imported/updated in.

![Edit the Segment][9]

## Common Errors

  - No external_id: To connect data from User Import to user profiles, Braze requires an external_id in each row. Rows without a value in the external_id column will be excluded from the import. User profiles that lack an external_id cannot be created or updated via the User Import.
  - Malformed Row: There must be a header row in order to properly import data. Each row must have the same number of cells as the header row. Rows whose length that have more or fewer values than the header row will be excluded from the import. Commas in a value will be interpreted as a separator and can lead to this error being thrown. Additionally, all data must be [UTF-8][utf8] encoded.
  - Multiple Data Types: Braze expects each value in a column to be of the same data type. Values which do not match their atttribute's data type will cause errors in segmenting.
    - Incorrectly Formatted Dates: Dates not in the [ISO 8601][date] format will not be read as datetimes on import.
    - String Quotation: Values encapsulated in single ('') or double ("") quotation marks will be read as strings on import.

[fields]:{{ site.baseurl }}/developer_guide/rest_api/user_data/#custom-attribute-data-types
[1]:{% image_buster /assets/img_archive/userimport_examplecsv_noerrors.png %}
[2]:{% image_buster /assets/img_archive/userimport_nav.png %}
[3]:{% image_buster /assets/img_archive/userimport_file_import_view.png %}
[4]:{% image_buster /assets/img_archive/userimport_Uploaded_NoErrors.png %}
[5]:{% image_buster /assets/img_archive/userimport_Uploaded_Errors.png %}
[6]:{% image_buster /assets/img_archive/userimport_Imported_Errors.png %}
[7]:{% image_buster /assets/img_archive/userimport_create_segment.png %}
[8]:{% image_buster /assets/img_archive/userimport_view_segment.png %}
[9]:{% image_buster /assets/img_archive/userimport_edit_segment.png %}
[10]:{% image_buster /assets/img_archive/userimport-import_started.png %}
[11]:{% image_buster /assets/img_archive/userimport-import_finished.png %}
[errors]:#common-errors
[date]: https://en.wikipedia.org/wiki/ISO_8601
[utf8]: https://en.wikipedia.org/wiki/UTF-8
[CAO]: {{ site.baseurl }}/user_guide/data_and_analytics/custom_data/custom_attributes/
[filtering]: {{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
