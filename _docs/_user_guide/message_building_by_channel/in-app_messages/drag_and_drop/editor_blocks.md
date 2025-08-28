---
nav_title: Editor blocks
article_title: "In-App Message Editor Blocks"
description: "This reference article describes the editor blocks available in the drag-and-drop editor for in-app messages."
alias: "/editor_blocks_dnd_iam/"
page_order: 5
---

# In-app message editor blocks

> Editor blocks are the various blocks available in the **Drag-And-Drop Editor** under the **Build** section. This section includes a series of tiles that represent the different kinds of content you can use in your message.

## How to use editor blocks

To use them, drag an editor block inside a column. It will auto-adjust to the column width. Each editor block has its own settings, such as granular control on padding. The right-side panel automatically switches to a property panel for the selected content element.

### Types

The following table describes how you can use each editor block type.

| Name | Description |
| --- | --- |
| Title | Enters a title text into the message. |
| Paragraph | Enters a paragraph text into the message. |
| Button | Adds a standard button. Properties for this block allow for editing, setting links, and logging analytics. |
| Radio Button | Adds a list of options from which users can select one. When submitted, the user profile logs the associated custom attribute. |
| Image | Inserts an image from the media library. |
| Link | Inserts a hyperlink that users can click to navigate to a specified URL. Can be embedded within text or standalone. |
| Spacer | Adds space or padding between other blocks. |
| Custom Code | Inserts and runs custom HTML, CSS, or JavaScript for advanced customization.  |
| Phone Capture | Inserts a form field for phone numbers. When submitted, the user is subscribed to the SMS or WhatsApp subscription group. |
| Email Capture | Inserts a form field for email addresses. When submitted, the email address is added to that user's profile in Braze. |
| Dropdown      | Inserts a dropdown with a pre-defined list of items from which users can select one. You can add any custom attribute strings to the list. |
| Checkbox      | Inserts a checkbox. If the user checks the box, the block's attribute is set to `true`. If left unchecked, its attribute is set to `false`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Actions

Details for each editor block's actions are provided in the following tables.

### Button

| Action | Description |
| --- | --- |
| Submit form when button is clicked | Submits the form and performs the selected on-click behavior. Turn this off to only perform the on-click behavior. |
| Set separate behaviors for each platform | Customizes the behavior of the button for each platform separately. |
| On-click behavior | Determines the action when the user clicks the button, such as closing the message, opening the web URL, deeplinking into a specific page of the app, going to another page, or requesting push permission. |
| Log custom attributes or events | Determines if clicking the button will update the user's profile with custom data. You can also select the identifier for reporting. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image

| Action | Description |
| --- | --- |
| Alt text | The written copy that appears in place of an image if the image fails to load. Screen readers announce alt text to explain images, so use plain language to provide key information about an image. |
| Submit form when image is clicked | Submits the form and performs the selected on-click behavior. Turn this off to only perform the on-click behavior. |
| Set separate behaviors for each platform | Customizes the behavior of the image for each platform separately. |
| On-click behavior | Determines the action when the user clicks the image, such as closing the message, opening the web URL, deeplinking into a specific page of the app, going to another page, or requesting push permission. |
| Log custom attributes or events | Determines if clicking the image will update the user's profile with custom data. You can also select the identifier for reporting. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Action | Description |
| --- | --- |
| URL | The hyperlink to navigate to
| Identifier for Reporting | Determines what identifier is used for reporting. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Properties

Details for each editor block's properties are provided in the following tables.

### Title and Paragraph

| Property | Description |
| --- | --- |
| Font family | The font style for the text |
| Font weight | Determines the thickness of the text |
| Font size | Determines the size of the text |
| Line height | Modifies the distance between lines of text |
| Letter spacing | Modifies the distance in between each character |
| Text alignment | Moves the text to be aligned left, center, right, or justified |
| Text color | Modifies the color of the text |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Button

| Property | Description |
| --- | --- |
| Button width | Modifies the width of the button to be automatic or manual |
| Font family | This is the font style for the text |
| Font weight | Determines the thickness of the text |
| Font size | Determines the size of the text |
| Letter spacing | Modifies the distance in between each character |
| Button alignment | Moves the button to be left, center, or right-oriented |
| Button text color | Modifies the color of the text on the button |
| Background color | Modifies the color of the button's background |
| Border style | Determines the style of the button's border of the button | 
| Border radius | Determines how round you would like the corners |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image

| Property | Description |
| --- | --- |
| URL | The hosted address for the image |
| Alignment | Moves the image to be left, center, or right-oriented |
| Background color | Modifies the color of the image's background |
| Border style | Determines the style of the image's border | 
| Border radius | Determines how round you would like the corners of the image |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link

| Property | Description |
| --- | --- |
| Font family | This is the font style for the text |
| Font weight | Determines the thickness of the text |
| Letter spacing | Modifies the distance in between each character |
| Text color | Modifies the color of the text |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Spacer

| Property | Description |
| --- | --- |
| Background color | Modifies the background color of the spacer |
| Height | Modifies the height of the spacer. You can also modify this by using the resize handles on the spacer. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Custom code

| Property | Description |
| --- | --- |
| Custom Code | Allows you to add, edit, or delete HTML, CSS, and JavaScript for an in-app message. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Phone capture

| Property | Description |
| --- | --- |
| Subscription group | The SMS or WhatsApp subscription group that the user will be subscribed to by collecting their phone number, with an option to collect numbers from all countries |
| Text alignment | Moves the text to be aligned left, center, right, or justified |
| Placeholder text | A placeholder phone number to display |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Email capture

| Property | Description |
| --- | --- |
| Font family | The font style for the text |
| Font weight | Determines the thickness of the text |
| Font size | Determines the size of the text |
| Line height | Modifies the distance between lines of text |
| Text color | Modifies the color of the text |
| Letter spacing | Modifies the distance in between each character |
| Text alignment | Moves the text to be aligned left, center, right, or justified |
| Placeholder text | A placeholder email address to display |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
