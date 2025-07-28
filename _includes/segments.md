{% if include.section == "Differing audience size" %}

The target population size that displayed in a campaign or Canvas may differ from the [reachable audience size for a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size#segment-membership-calculation), even if you're directly adding that segment into your campaign or Canvas without additional filters. 
This may happen for several reasons:

- When a Global Control Group applies to a campaign or Canvas, users in that Global Control Group are excluded in the reachable users count.
- The target population size on a campaign or Canvas excludes users that aren't contactable through various message channels; the behavior differs from channel to channel. For example, the reachable audience for a campaign or Canvas excludes users who are unsubscribed, marked as spam (for emails), or soft bounced (for emails). The segment itself, however, only excludes opt-outs when showing the estimated number of email reachable users. 
- Braze only sends SMS messages to users within the selected subscription group, so the SMS target population for a campaign or Canvas will also exclude any users who aren't part of your selected subscription group.

{% endif %}

{% if include.section == "Refresh settings" %}

If you don't need your extension to refresh on a regular schedule, you can save it without using refresh settings, and Braze will default to generating your Segment Extension based on your user membership at that moment. Use the default behavior if you only want to generate the audience once and then target it with a one-off campaign.

Your segment will always begin processing after the initial save. Whenever your segment refreshes, Braze will re-run the segment and update segment membership to reflect the users in your segment at the time of refresh. This can help your recurring campaigns reach the most relevant users.

#### Setting up a recurring refresh

To set up a recurring schedule by designating refresh settings, select **Enable refresh**. The option to designate refresh settings is available for all types of Segment Extensions, including SQL segments, CDI Segment Extensions, and simple form-based Segment Extensions.

{% alert important %}
To optimize your data management, refresh settings are automatically turned off for unused Segment Extensions. Segment Extension are considered unused when they're:

- Not used in any active or inactive (draft, stopped, archived) campaigns, Canvases, or segments; or
- Have not been modified in over 7 days

Braze will notify the company contact and creator of the extension if this setting is turned off. The option to regenerate extensions daily can be turned on again at any time.
{% endalert %}

#### Selecting your refresh settings

![Refresh Interval Settings with a weekly refresh frequency, start time of 10 am, and Monday selected as a day.]({% image_buster /assets/img/segment/segment_interval_settings.png %}){: style="max-width:50%;"}

Within the **Refresh Interval Settings** panel, you can select the frequency at which this segment extension will refresh: hourly, daily, weekly, or monthly. You’ll also be required to select the specific time (which is in your company’s time zone) the refresh would occur, such as:

- If you have an email campaign that is sent every Monday at 11 am company time, and you want to ensure your segment is refreshed right before it's sent, you should choose a refresh schedule of weekly at 10 am on Mondays.
- If you’d like your segment to refresh every day, select the daily refresh frequency and then choose the time of day to refresh.

{% alert note %}
The ability to set an hourly refresh schedule isn't available for form-based Segment Extensions (but you can set daily, weekly, or monthly schedules). 
{% endalert %}

#### Credit consumption and additional costs

Because refreshes re-run your segment’s query, each refresh for SQL segments will consume SQL segment credits, and each refresh for CDI Segment Extensions will incur a cost within your third-party data warehouse.

{% alert note %}
Segments could require up to 60 minutes to refresh because of data processing times. Segments that are currently in the process of refreshing will have a “Processing” status within your Segment Extensions list. This has a couple of implications:

- To finish processing your segment before a specific time, choose a refresh time that is 60 minutes earlier. 
- Only one refresh can occur at a time for a specific Segment Extension. If there is a conflict where a new refresh is initiated when an existing refresh has already begun processing, Braze will cancel the new refresh request and continue the in-progress processing. 
{% endalert %}

#### Criteria to automatically disable stale extensions

Scheduled refreshes are automatically disabled once a Segment Extension is stale. A Segment Extension is stale if it meets the following criteria:

- Not used in any active campaigns or Canvases
- Not used in any segment that is in an active campaign or Canvas
- Not used in any segment that has [analytics tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) turned on
- Hasn't been modified in over seven days
- Hasn't been added to a campaign or Canvas (including drafts), or segment in over seven days

If the scheduled refresh is disabled for a Segment Extension, that extension will have a notification that says so.

![A notification stating that "Scheduled refreshes have been turned off for this extension because it's not used in any active campaigns, Canvases, or segments. The segment extension was disabled February 23, 2025 at 12:00 AM."]({% image_buster /assets/img/segment/segment_extension_disabled.png %})

When you're ready to use a stale Segment Extension, review the refresh settings, select the refresh schedule that matches your use case, and then save any modifications.

{% endif %}