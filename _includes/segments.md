{% if include.section == "Differing audience size" %}
The target population size that displayed in a campaign or Canvas may differ from the [reachable audience size for a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size#segment-membership-calculation), even if you're directly adding that segment into your campaign or Canvas without additional filters. 
This may happen for several reasons:

- When a Global Control Group applies to a campaign or Canvas, users in that Global Control Group are excluded in the reachable users count.
- The target population size on a campaign or Canvas excludes users that aren't contactable through various message channels; the behavior differs from channel to channel. For example, the reachable audience for a campaign or Canvas excludes users who are unsubscribed, marked as spam (for emails), or soft bounced (for emails). The segment itself, however, only excludes opt-outs when showing the estimated number of email reachable users. 
- Braze only sends SMS messages to users within the selected subscription group, so the SMS target population for a campaign or Canvas will also exclude any users who aren't part of your selected subscription group.
{% endif %}