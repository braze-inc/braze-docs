---
nav_title: Alerts (best practices)
article_title: Alerts (best practices)
description: "Information, guidelines, and examples for alert types used in Braze documentation."
page_order: 2
noindex: true
---

# Alerts (best practices)

### Best practices for alerts {#best-practices-for-alerts}

This document contains information, general guidelines, and examples for alert types used in Braze documentation. 

### Alert types {#alert-types}

Alerts categorize information that a reader should be aware of. There are four alert types that can be used in our documentation:

* Important  
* Note  
* Tip  
* Warning

### When to use an alert {#when-to-use-an-alert}

Use alerts to draw a reader's attention to important information. Keep the content short and to the point. We want to make sure that information sticks with the reader.

Refer to the following table for definitions of each alert:

| Alert Type | Definition |
| :---- | :---- |
| Important | Includes essential information that **should** be addressed by the reader, such as: {::nomarkdown}<ul><li>Deprecated features</li><li>Impacts on billing</li><li>Information pertaining to relevant updates</li><li>Pressing feature caveats (ex: beta features)</li><li>Other important tidbits of information</li></ul>{:/} |
| Note | Includes one-off information that the reader should know, such as: {::nomarkdown}<ul><li>Feature caveats</li><li>Formatting guidance</li><li>Helpful callouts</li><li>Information that is demoted from an Important alert due to the alert's content dropping in severity (ex: a long-standing important alert shifting to a standard note)</li></ul>{:/} |
| Tip | Includes supplementary knowledge and recommendations for the reader to be aware of, such as: {::nomarkdown}<ul><li>Additional troubleshooting articles</li><li>Steps and shortcuts that help increase usability (ex: additional customization for in-app messages)</li></ul>{:/} |
| Warning | Includes essential information that a reader must address and can include: {::nomarkdown}<ul><li>Irreversible consequences (ex: Campaign and Canvas deletion)</li><li>Feature-breaking behavior</li><li>Loss of data</li><li>Other crucial warnings</li></ul>{:/} |

**Alert Best Practices**  
Here are general guidelines and best practices for alerts. 

As a general rule of thumb, avoid using alerts for content that is essential to the article structure (like feature introductions, setup instructions, and steps to use a feature.). When in doubt, consult with the team during peer review.

| Guideline | Example |
| :---- | :---- |
| Explain the information in the alert in a clear, concise statement.  | ![An alert with a clear, concise statement.]({% image_buster /assets/img/contributing/style_guide/alert_1.png %}) <br><br> [Note alert in Step 4: Add Filters to Your Segment Section]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment) |
| For alerts that apply to different sections of the same article, consider creating a new section that captures these details to avoid repetitive content. | ![Example of a new section instead of an alert.]({% image_buster /assets/img/contributing/style_guide/alert_2.png %}) <br><br> [Property Details header in Push Send Events Section]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) |
| Separate the information into short paragraphs or lists within the alert. | ![Example of separating the information into short paragraphs.]({% image_buster /assets/img/contributing/style_guide/alert_3.png %}) <br><br> [Important alert in Canvas Persistent Entry Properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/#using-entry-properties) |
| Consider any additional formatting that may impact how the alert displays (code snippets, steps, surrounding images, and more.). | ![An alert code styling.]({% image_buster /assets/img/contributing/style_guide/alert_4.png %}) <br><br> [Important alert in Step 2: Add Code Snippet to Email Body]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/#step-2-add-code-snippet-to-email-body) |
| Include a line break for alerts that begin an article. | ![Example of an alert beginning an article.]({% image_buster /assets/img/contributing/style_guide/alert_5.png %}) <br><br> [Content Card Implementation Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/) |
| When writing about beta features, include an Important alert that calls out the beta status and related Braze contact information.  Place this beta alert after the overview text and before the first main heading. | ![Example of an important alert for a beta feature.]({% image_buster /assets/img/contributing/style_guide/alert_6.png %}) <br><br> [Canvas Persistent Entry Properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/)  |
| Avoid using two or more alerts in a row if possible. Instead, reorganize or include the information as part of the text instead. | ![An example of two alerts next to each other, which you should avoid.]({% image_buster /assets/img/contributing/style_guide/alert_7.png %}) <br><br> [Setting User IDs]({{site.baseurl}}/developer_guide/platform_integration_guides/fireos/analytics/setting_user_ids/) |
| If you find your alert is lengthy, consider creating a new section that includes the information as a list. For example, instead of including troubleshooting steps in an alert, consider creating a troubleshooting section or providing a link to a related article.  | ![Example of a new section of content.]({% image_buster /assets/img/contributing/style_guide/alert_8.png %}) <br><br> [Tip alert in Canvas and Campaign Tag Differences Section]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) |

### Alert examples {#alert-examples}

Refer to the following examples for how and why each alert type is used in our documentation. 

### Important alert  {#important-alert}

{% include alerts/important_alerts.md alert='Web push private browsing' %}

* **Article:** [Push for Web]({{site.baseurl}}/user_guide/message_building_by_channel/push/web/)
* **Use Case:** Includes essential feature caveat that the reader should know as they set up their web push.
* **Alert Reasoning:** Use an Important alert as opposed to a Note alert because the content's importance is greater for a reader to know as they set up their web push.

{% include alerts/important_alerts.md alert='BCC address billable emails' %}

* **Article:** [Email Settings]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/)
* **Use Case:**
  - Provides important feature caveat about the possibility of doubling billable emails
  - Redirects reader to contact their Customer Success Manager as needed
* **Alert Reasoning:** The Important alert is used here to communicate details about the BCC addresses in their email settings. This information is best presented using an Important alert as opposed to a Warning alert because omitting this information does not impact the feature irreversibly (feature breaking, permanent data loss, etc.).

{% multi_lang_include alerts/important_alerts.md alert='Android notification priority' %}

* **Article:** [Advanced Campaign Settings]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#notification-display-priority)
* **Use Case:** Includes pressing feature caveat about the Notification Priority. Redirects the reader to new information that's available.
* **Alert Reasoning:** The Important alert is best used here to redirect the reader to current information and to highlight that the section is applicable only to certain users. It's also placed after the section header, which forces the user to address the important alert before reading the rest of the section.

### Note alert {#note-alert}

{% include alerts/note_alerts.md alert='Content Cards frequency capping' %}

* **Article:** [Create a Content Card]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)
* **Use Case:** Includes additional information that a reader should be aware of as they learn more about Content Cards.
* **Alert Reasoning:** This Note alert provides background information on how Braze cycles older Content Cards for users. This is helpful, supplemental information for the reader to be aware of and does not require the use of an Important or Tip alert.

{% include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

* **Article:** [Custom Attributes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/)
* **Use Case:** Includes general information that a reader should be aware of. Provides an article to learn more about related content (time attributes).
* **Alert Reasoning:** This information is best relayed using a Note alert as opposed to an Important alert because the content is directed to provide general information. Disregarding this information would not impact the ease of use for this feature.

{% include alerts/note_alerts.md alert='Manage custom data storage' %}

* **Article:** [Manage Custom Data]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#managing-properties)
* **Use Case:** Includes general information that a reader should be aware of. Redirects to Braze contact for further information.
* **Alert Reasoning:** This Note alert provides additional information about data storage that would be helpful for a reader to know as they manage their custom attributes. However, the content does not require a stronger indication of importance to the reader, so a Note alert is acceptable here.

### Tip alert {#tip-alert}

{% include alerts/tip_alerts.md alert='SMS segment calculator' %}

* **Article:** [SMS and RCS Billing Calculators]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/)
* **Use Case:** Includes tool for the reader to understand their message length and SMS segment count. Provides information that may be helpful for the reader in their understanding of copy limits.
* **Alert Reasoning:** This is a lengthy Tip alert because it provides a space for entering the copy to see how many segments a message dispatches. The Tip alert is the best option here because this is a helpful generator for the reader to use in the process of setting up their SMS messages.

#### Example 2
{% include alerts/tip_alerts.md alert='Export troubleshooting' %}

* **Article:** [Export KPIs for Daily App Uninstalls by Date]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
* **Use Case:** Provides troubleshooting advice when using this endpoint.
* **Alert Reasoning:** The Tip alert provides additional support for the reader. Use a Tip alert as opposed to a Note alert because the focus of the content is to assist the reader by providing the troubleshooting article.

### Warning alert {#warning-alert}

{% include alerts/warning_alerts.md alert='User profile external_id' %}

* **Article:** [User Profile Lifecycle]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
* **Use Case:** Indicates something that the reader should not do when creating their user profiles in Braze.
* **Alert Reasoning:** The Warning alert is used to caution the reader against assigning an external_id before uniquely identifying them. This information is best relayed using a Warning alert as opposed to an Important alert because it includes irreversible consequences for the user profile.

{% include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

* **Article:** [Segment for Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* **Use Case:** Cautions the reader when creating Currents connectors. Includes the consequence of incorrectly creating these connectors.
* **Alert Reasoning:** The Warning alert is best used here to describe the limitations of the Braze Segment Currents integration. Use a Warning alert as opposed to an Important alert because creating more than one of the same Currents connectors incorrectly may result in losing data.

{% include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

* **Article:** [Create a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
* **Use Case:** Lists the information that may cause the feature to not work. Details how the intended audience may not receive the campaign or enter the Canvas.
* **Alert Reasoning:** The Warning alert is used here to note how the feature may work incorrectly. This information is best relayed using a Warning alert as opposed to an Important alert because the information is critical and may result in breaking the Canvas delivery.
