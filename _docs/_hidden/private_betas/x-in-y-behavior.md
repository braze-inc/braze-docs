---
nav_title: X in Y Filter Behavior
permalink: /x-in-y-behavior/
---

# Current X in Y Filter Behavior

Braze has a specific category of Segmentation Filters called "X in Y Filters". These filters each have similar functionality defined by the following characteristics:

- Run by setting Calendar Days (ending at midnight).
- "Days" are defined as in UTC.
- The current UTC day is defined as "1".
- There is a bug where days are sometimes defined as a a 24-hour period, rather than as Calendar Days.

## Future X in Y Filter Behavior

The behavior of these filters will remain largely the same and will be defined by the following characteristics:

- Run by setting Calendar Days (ending at midnight).
- "Days" are defined as in UTC.
- The current UTC day is defined as "0".

{% details Why has the UTC definition changed from "1" to "0"? %}
Local timezone scheduling requires that users stay in segments for 24 hours. In the case of Y = 1 day, we were in some cases evaluating less than 24 hours of the user’s history when determining who should be processed for the Campaign or Canvas.

The change will make the filter more intuitive and more consistent with the behavior of our other calendar functionality, such as our send “in 1 day” scheduling options.
{% enddetails %}

<br>

### Example

The campaign shown below sends at 9:00PM on April 16th. It's audience's segmentation is “Made More than 2 Purchases in the past 3 days”.

![Campaign Schedule][1]

9:00PM ET on April 16th is 1:00AM UTC on April 17th.

April 17th would be day "0", April 16th would be day "1", April 15th would be day "2", and April 14th would be day "3".

The history from 12:00AM UTC on April 14th through the current time (1:00AM UTC on April 17th).
This would accumulate to a window that includes 73 hours of the user’s history.

# On Calendar Days

Calendar Days are used in more capacities than in just the "X in Y" Filters:
- Message Scheduling
- Frequency Capping
- "X in Y" Filters

[1]:{% image_buster /assets/img/campaign-schuedule-example.png %}
