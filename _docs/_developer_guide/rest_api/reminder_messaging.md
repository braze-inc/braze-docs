---
nav_title: User-selected reminder messaging
article_title: User-selected reminder messaging
page_order: 5
page_type: reference
description: "This reference article walks through how to use Braze landing pages, custom attributes, and campaigns to let users sign up for personalized reminder messages about upcoming events or appointments."
---

# User-selected reminder messaging

> Use Braze [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/), custom attributes, and campaigns to let users choose when they want to receive reminder messages about upcoming events or appointments. This approach lets non-technical Braze users create and edit the content for reminder sign-up pages, while the preferences users select can drive segmentation, targeting, and personalization across all of your Braze-powered messaging.

With this approach, you can:

- Let users self-select the date of their reminder message relative to an upcoming event.
- Capture preferences directly from users using a Braze landing page and write them to user profiles — no extra backend needed.
- Send messages on the dates users choose, so messaging stays relevant and permission-based.
- Extend the use case with additional Braze features, such as message delays, follow-up retargeting, and A/B testing.

## Prerequisites

To complete this guide, you need:

| Requirement | Description |
| --- | --- |
| Landing page access | Access and permissions to create [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) in Braze. |
| HTML and JavaScript knowledge | Basic familiarity with HTML and JavaScript to customize your landing page. |
| Liquid knowledge | Basic familiarity with [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) for templating personalized variables. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Step 1: Create a landing page and associate it with a user profile

First, [create a Braze landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/). Then, create an email that shares the landing page link with your users.

To associate landing page activity with a specific user profile, append a query string parameter to the link that identifies the recipient. This lets Braze write the user's responses back to their profile.

{% raw %}
For example, include a link in your email that appends the user ID as a Base64-encoded value:

```
https://your-landing-page-url.com?q={{${user_id} | base64_encode}}
```
{% endraw %}

When a user clicks this link, the landing page can decode the parameter and identify the user, so any preferences they select are written to their Braze profile.

## Step 2: Use a custom code block to capture preferences

After creating your landing page, insert a custom code block that identifies users and writes their preferences to Braze. The script should:

1. Decode the user identifier from the URL query string.
2. Listen for the form submission button click.
3. Use the `lpBridge` API to identify the user, set custom attributes, and flush the data to Braze.

### Example script

The following example script disables the default button behavior and executes custom methods on button click. Replace the element IDs and attribute values with your own.

```html
<script async="true">
  // Set IDs (as found by inspecting your landing page preview) and success message
  const registerButtonId = "YOUR_BUTTON_ID";
  const messageDivId = "YOUR_MESSAGE_DIV_ID";
  const successMessage = "You're all set! We'll send your reminder.";

  // Retrieve and decode the 'q' parameter from the URL
  const qParam = new URLSearchParams(window.location.search).get("q");
  if (!qParam) {
    console.error("Missing 'q' parameter in URL. Cannot identify user.");
    return;
  }
  const external_id = atob(qParam);

  // Wait for page content to load
  document.addEventListener("DOMContentLoaded", () => {
    // Remove the default redirect event from the Braze Message Handler Script
    props[registerButtonId].onclickContract[0].brazeEvents =
      props[registerButtonId].onclickContract[0].brazeEvents.filter(
        (event) => event.eventType !== "REDIRECT"
      );

    const registerButton = document.getElementById(registerButtonId);
    if (registerButton) {
      registerButton.addEventListener("click", async (event) => {
        event.preventDefault();

        // Identify the user
        await window.lpBridge.changeUser(external_id);

        // Set the custom attribute (replace with your actual key/value)
        await window.lpBridge.setCustomUserAttribute("key", "value");

        // Flush data to Braze
        await window.lpBridge.requestImmediateDataFlush();

        // Remove the button and update the message
        registerButton.remove();
        const messageDiv = document.getElementById(messageDivId);
        if (messageDiv) {
          messageDiv.innerHTML = successMessage;
        }
      });
    }
  });
</script>
```

To find the element IDs for your landing page components, preview your page, right-click, and select **Inspect** in your browser. Locate the IDs for the button and message components in the HTML.

In the script above, replace the `setCustomUserAttribute` call with the actual attributes you want to store. How you present options to your users depends on whether you're collecting shared dates or personal dates.

### Option A: Shared dates

For events where many users share the same date (such as holidays or sporting events), use checkboxes on the landing page that map to boolean custom attributes on the user profile.

For example, if a user signs up for Super Bowl 2026 reminders, set:

```
super_bowl_2026_reminder = true
```

These boolean attributes can then be used directly in [segment filters]({{site.baseurl}}/user_guide/engagement_tools/segments/) to build your target audience.

### Option B: Personal dates

For dates unique to each user (such as birthdays or anniversaries), use a date picker input in a custom code block (for example, `<input type="date">`).

Store these preferences using a [nested custom attribute array of objects]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/array_of_objects/). This structure lets you store multiple reminders per user and add derived fields later, such as `next_reminder_name` or `last_reminder_date`.

## Step 3: Set up and trigger reminder messages

After collecting custom attributes through the landing page, create campaigns to message users about upcoming events.

### Option A: Shared dates {#step-3-option-a-shared-dates}

If you used boolean custom attributes (Option A in [Step 2](#option-a-shared-dates)), use that attribute as a segment filter to build the audience for your reminder message. Then create a new campaign, scheduled before the event, to target this group with your chosen content.

### Option B: Personal dates {#step-3-option-b-personal-dates}

If you used nested custom attributes (Option B in [Step 2](#option-b-personal-dates)), use the **Nested Custom Attribute** audience filter to select all users who have a reminder date within a specific window — for example, two days from now.

To send reminders on an ongoing basis, set up a daily recurring campaign so that each day, users with upcoming reminders that fall within your window receive their messages.

## Step 4: Verify your integration

After completing the setup, verify your integration:

1. Send yourself a link to the landing page and complete the form.
2. Navigate to your user profile in the Braze dashboard and confirm the custom attribute appears.
3. Send a test reminder message to your profile and verify that any personalized details render correctly.
4. Monitor results closely as you launch your campaign.

## Considerations

- For a detailed example of how to send messages based on date-based custom attributes, see the email use case in the [REST API messaging guide]({{site.baseurl}}/developer_guide/rest_api/messaging/).
- If you duplicate a landing page or replace any fields, the component IDs change. Update your custom code block to reflect the new IDs.
- Nested custom attributes consume [data points]({{site.baseurl}}/user_guide/data/data_points/) for each key in the array of objects. Updating a custom attribute object to null also consumes a data point.
- The code presented in this guide is intended as an illustrative example. Thoroughly test all code and components within your environment before deploying to production.
