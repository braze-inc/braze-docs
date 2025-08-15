---
nav_title: X in y filter behavior
permalink: /x-in-y-behavior/
---

# Current X in Y Filter Behavior

The behavior of these filters will remain largely the same and will be defined by the following characteristics:

- Run by setting Calendar Days (ending at midnight).
- "Days" are defined as in UTC.
- The current UTC day is defined as "0".

## Use case

The following campaign shown sends at 9 pm on April 16. The audience's segmentation is "Made More than 2 Purchases in the past 3 days".

![Campaign Schedule]({% image_buster /assets/img/campaign-schuedule-example.png %})

9 pm ET on April 16 is 1 am UTC on April 17.

April 17 would be day "0", April 16 would be day "1", April 15 would be day "2", and April 14 would be day "3".

The history from 12 am UTC on April 14 through the current time (1 am UTC on April 17).
This would accumulate to a window that includes 73 hours of the user's history.

## On Calendar Days

Calendar Days are used in more capacities than in just the "X in Y" Filters:

- Message Scheduling
- Frequency Capping
- "X in Y" Filters

`Calendar Days` refer to the period of time within a numbered day, beginning at 12:00AM and ending at 11:59PM that same day (12:00AM June 8th through 11:59PM June 8th would be a single calendar day.)

### Frequency Capping

Calendar Days are used when you select "days" or "weeks" under `Frequency Capping`.

- `Every 1 day` will limit the capping to the current calendar day in your user's local time (ending at midnight local time).
- `Every 2 days` will limit the capping to the previous and current calendar days in your user's local time (ending at midnight local time on the current calendar day).

### Company & Local Time

The current Calendar Day in the company time zone counts as day `0`.

`Send in 1 Calendar days at 11:05 am company time` or `send in 1 Calendar days at 11:05 am local time` would add `1` day to the current calendar day in the company time zone or local time zone, respectively, then schedule the message at the next upcoming 11:05 am Company Time.

If the Company or Local time is Pacific Time, and the user enters the Canvas step at 8:00PM PT on 4/13, Braze will schedule this Canvas step for 11:05 am PT on 4/14.

## Previous X in Y Filter Behavior

Braze has a specific category of Segmentation Filters called "X in Y Filters". These filters each have similar functionality defined by the following characteristics:

- Run by setting Calendar Days (ending at midnight).
- "Days" are defined as in UTC.
- The current UTC day is defined as "1".



