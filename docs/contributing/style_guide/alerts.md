
# Alerts best practices

> This document contains information, general guidelines, and examples for alert types used in Braze documentation. 

## Alert types

Alerts categorize information that a reader should be aware of. There are four alert types that can be used in our documentation:

* Important  
* Note  
* Tip  
* Warning

## When to use an alert

Use alerts to draw a reader's attention to important information. Keep the content short and to the point. We want to make sure that information sticks with the reader.

Refer to the following table for definitions of each alert:

<table>
<thead>
<tr><th>Alert Type</th><th>Definition</th></tr>
</thead>
<tbody>
<tr><td>Important</td><td>Includes essential information that <strong>should</strong> be addressed by the reader, such as: <ul><li>Deprecated features</li><li>Impacts on billing</li><li>Information pertaining to relevant updates</li><li>Pressing feature caveats (ex: beta features)</li><li>Other important tidbits of information</li></ul></td></tr>
<tr><td>Note</td><td>Includes one-off information that the reader should know, such as: <ul><li>Feature caveats</li><li>Formatting guidance</li><li>Helpful callouts</li><li>Information that is demoted from an Important alert due to the alert's content dropping in severity (ex: a long-standing important alert shifting to a standard note)</li></ul></td></tr>
<tr><td>Tip</td><td>Includes supplementary knowledge and recommendations for the reader to be aware of, such as: <ul><li>Additional troubleshooting articles</li><li>Steps and shortcuts that help increase usability (ex: additional customization for in-app messages)</li></ul></td></tr>
<tr><td>Warning</td><td>Includes essential information that a reader must address and can include: <ul><li>Irreversible consequences (ex: Campaign and Canvas deletion)</li><li>Feature-breaking behavior</li><li>Loss of data</li><li>Other crucial warnings</li></ul></td></tr>
</tbody>
</table>


**Alert Best Practices**  
Here are general guidelines and best practices for alerts. 

As a general rule of thumb, avoid using alerts for content that is essential to the article structure (like feature introductions, setup instructions, and steps to use a feature.). When in doubt, consult with the team during peer review.


<table>
<thead>
<tr><th>Guideline</th><th>Example</th></tr>
</thead>
<tbody>
<tr><td>Explain the information in the alert in a clear, concise statement.</td><td>File in GitHub: [`note_alerts.md`](../../../_includes/alerts/note_alerts.md)<br><br> <a href="https://www.braze.com/docs/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment">Note alert in Step 4: Add Filters to Your Segment Section</a></td></tr>
<tr><td>For alerts that apply to different sections of the same article, consider creating a new section that captures these details to avoid repetitive content.</td><td>File in GitHub: [`property_details_dispatch_state_source.md`](../../../_includes/currents/property_details_dispatch_state_source.md)<br><br> <a href="https://www.braze.com/docs/user_guide/data/braze_currents/event_glossary/message_engagement_events/#subscription-group-state-change-events">Property details in Message Engagement Events</a></td></tr>
<tr><td>Separate the information into short paragraphs or lists within the alert.</td><td>File in GitHub: [`important_alerts.md`](../../../_includes/alerts/important_alerts.md)<br><br> <a href="https://www.braze.com/docs/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/">Important alert in Import your email list</a></td></tr>
<tr><td>Consider any additional formatting that may impact how the alert displays (code snippets, steps, surrounding images, and more).</td><td>File in GitHub: [`tip_alerts.md`](../../../_includes/alerts/tip_alerts.md)<br><br> <a href="https://www.braze.com/docs/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/#considerations">Tip alert with code snippet in Price drop notifications</a></td></tr>
<tr><td>Include a line break for alerts that begin an article.</td><td><img src="../../../assets/img/contributing/style_guide/alert_5.png" alt="Example of an alert beginning an article."><br><br> <a href="https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/">Content Card Implementation Guide</a></td></tr>
<tr><td>When writing about beta features, include an Important alert that calls out the beta status and related Braze contact information. Place this beta alert after the overview text and before the first main heading.</td><td><img src="../../../assets/img/contributing/style_guide/alert_6.png" alt="Example of an important alert for a beta feature."></td></tr>
<tr><td>Avoid using two or more alerts in a row if possible. Instead, reorganize or include the information as part of the text.</td><td><img src="../../../assets/img/contributing/style_guide/alert_7.png" alt="An example of two alerts next to each other, which you should avoid."></td></tr>
<tr><td>If you find your alert is lengthy, consider creating a new section that includes the information as a list. For example, instead of including troubleshooting steps in an alert, consider creating a troubleshooting section or providing a link to a related article.</td><td><img src="../../../assets/img/contributing/style_guide/alert_8.png" alt="Example of a new section of content."></td></tr>
</tbody>
</table>


## Alert examples

Refer to the following examples for how and why each alert type is used in our documentation. 

### Important alert

File in GitHub: [`important_alerts.md`](../../../_includes/alerts/important_alerts.md)

* **Article:** [Push for Web](https://www.braze.com/docs/user_guide/message_building_by_channel/push/web/)
* **Use case:** Includes essential feature caveat that the reader should know as they set up their web push.
* **Alert reasoning:** Use an Important alert as opposed to a Note alert because the content's importance is greater for a reader to know as they set up their web push.

File in GitHub: [`important_alerts.md`](../../../_includes/alerts/important_alerts.md)

* **Article:** [Email Settings](https://www.braze.com/docs/user_guide/administrative/app_settings/email_settings/)
* **Use case:**
  - Provides important feature caveat about the possibility of doubling billable emails
  - Redirects reader to contact their customer success manager as needed
* **Alert reasoning:** The Important alert is used here to communicate details about the BCC addresses in their email settings. This information is best presented using an Important alert as opposed to a Warning alert because omitting this information does not impact the feature irreversibly (such as feature breaking, permanent data loss).

File in GitHub: [`important_alerts.md`](../../../_includes/alerts/important_alerts.md)

* **Article:** [Advanced Campaign Settings](https://www.braze.com/docs/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#notification-display-priority)
* **Use case:** Includes pressing feature caveat about the Notification Priority. Redirects the reader to new information that's available.
* **Alert reasoning:** The Important alert is best used here to redirect the reader to current information and to highlight that the section is applicable only to certain users. It's also placed after the section header, which forces the user to address the important alert before reading the rest of the section.

### Note alert

File in GitHub: [`note_alerts.md`](../../../_includes/alerts/note_alerts.md)

* **Article:** [Create a Content Card](https://www.braze.com/docs/user_guide/message_building_by_channel/content_cards/create/)
* **Use case:** Includes additional information that a reader should be aware of as they learn more about Content Cards.
* **Alert reasoning:** This Note alert provides background information on how Braze cycles older Content Cards for users. This is helpful, supplemental information for the reader to be aware of and does not require the use of an Important or Tip alert.

File in GitHub: [`note_alerts.md`](../../../_includes/alerts/note_alerts.md)

* **Article:** [Custom Attributes](https://www.braze.com/docs/user_guide/data/activation/custom_data/custom_attributes/)
* **Use case:** Includes general information that a reader should be aware of. Provides an article to learn more about related content (time attributes).
* **Alert reasoning:** This information is best relayed using a Note alert as opposed to an Important alert because the content is directed to provide general information. Disregarding this information would not impact the ease of use for this feature.

File in GitHub: [`note_alerts.md`](../../../_includes/alerts/note_alerts.md)

* **Article:** [Manage Custom Data](https://www.braze.com/docs/user_guide/data/activation/custom_data/managing_custom_data/#managing-properties)
* **Use case:** Includes general information that a reader should be aware of. Redirects to Braze contact for further information.
* **Alert reasoning:** This Note alert provides additional information about data storage that would be helpful for a reader to know as they manage their custom attributes. However, the content does not require a stronger indication of importance to the reader, so a Note alert is acceptable here.

### Tip alert

File in GitHub: [`tip_alerts.md`](../../../_includes/alerts/tip_alerts.md)

* **Article:** [SMS and RCS Billing Calculators](https://www.braze.com/docs/user_guide/message_building_by_channel/sms_mms_rcs/segments/)
* **Use case:** Includes tool for the reader to understand their message length and SMS segment count. Provides information that may be helpful for the reader in their understanding of copy limits.
* **Alert reasoning:** This is a lengthy Tip alert because it provides a space for entering the copy to see how many segments a message dispatches. The Tip alert is the best option here because this is a helpful generator for the reader to use in the process of setting up their SMS messages.

File in GitHub: [`tip_alerts.md`](../../../_includes/alerts/tip_alerts.md)

* **Article:** [Export KPIs for Daily App Uninstalls by Date](https://www.braze.com/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
* **Use case:** Provides troubleshooting advice when using this endpoint.
* **Alert reasoning:** The Tip alert provides additional support for the reader. Use a Tip alert as opposed to a Note alert because the focus of the content is to assist the reader by providing the troubleshooting article.

### Warning alert

File in GitHub: [`warning_alerts.md`](../../../_includes/alerts/warning_alerts.md)

* **Article:** [User Profile Lifecycle](https://www.braze.com/docs/user_guide/data/unification/user_data/user_profile_lifecycle/)
* **Use case:** Indicates something that the reader should not do when creating their user profiles in Braze.
* **Alert reasoning:** The Warning alert is used to caution the reader against assigning an external_id before uniquely identifying them. This information is best relayed using a Warning alert as opposed to an Important alert because it includes irreversible consequences for the user profile.

File in GitHub: [`warning_alerts.md`](../../../_includes/alerts/warning_alerts.md)

* **Article:** [Segment for Currents](https://www.braze.com/docs/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* **Use case:** Cautions the reader when creating Currents connectors. Includes the consequence of incorrectly creating these connectors.
* **Alert reasoning:** The Warning alert is best used here to describe the limitations of the Braze Segment Currents integration. Use a Warning alert as opposed to an Important alert because creating more than one of the same Currents connectors incorrectly may result in losing data.

File in GitHub: [`warning_alerts.md`](../../../_includes/alerts/warning_alerts.md)

* **Article:** [Create a Canvas](https://www.braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
* **Use case:** Lists the information that may cause the feature to not work. Details how the intended audience may not receive the campaign or enter the Canvas.
* **Alert reasoning:** The Warning alert is used here to note how the feature may work incorrectly. This information is best relayed using a Warning alert as opposed to an Important alert because the information is critical and may result in breaking the Canvas delivery.
