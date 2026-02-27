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

## Step 1: Create a landing page and link to it from a message

First, [create a Braze landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/). Then, create a message (such as an email) that links users to the landing page.

{% raw %}
To automatically associate landing page activity with the recipient's user profile, use the `{% landing_page_url %}` Liquid tag when linking to the page from a Braze message. For example:

```html
<a href="{% landing_page_url your-page-url-handle %}">Sign up for reminders</a>
```
{% endraw %}

When a user clicks this link, Braze automatically identifies them, so any preferences they submit are written to their existing profile — no manual URL parameters needed. For a full walkthrough, see [Track users through a form]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users/).

{% alert tip %}
If you're linking to the landing page from an external channel (outside of Braze), you'll need to pass a user identifier in the URL manually and decode it in your custom code block. Use a URL-safe encoding approach (such as Base64url, or standard Base64 with URL-encoding) to avoid corruption — standard Base64 characters like `+` are treated as spaces by URL query parsers. See [Track users through a form]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users/) for your landing page's unique URL.
{% endalert %}

## Step 2: Use a custom code block to capture preferences

After creating your landing page, insert a custom code block that captures user preferences and writes them to Braze. When users arrive through the {% raw %}`{% landing_page_url %}`{% endraw %} Liquid tag, Braze already knows who they are, so your script only needs to:

1. Listen for the form submission button click.
2. Use the `lpBridge` API to set custom attributes and flush the data to Braze.

### Example script

The following example script disables the default button behavior and executes custom methods on button click. Replace the element IDs and attribute values with your own.

```html
<script async="true">
  // Set IDs (as found by inspecting your landing page preview) and success message
  const registerButtonId = "YOUR_BUTTON_ID";
  const messageDivId = "YOUR_MESSAGE_DIV_ID";
  const successMessage = "You're all set! We'll send your reminder.";

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
