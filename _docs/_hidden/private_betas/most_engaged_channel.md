---
nav_title: Most Engaged Channel
permalink: /most_engaged_channel/
---

# Most Engaged Channel Filter
The Most Engaged Channel filter allows you to select users for whom the selected messaging channel is their "best" channel ("best" meaning "has the highest likelihood of engagement, given the user's history"). You can select Email, Web Push, or Mobile Push (which includes any available mobile OS or device) as a channel.

![most_engaged_channel_filter][1]{: height="50%" width="50%"}

The Most Engaged Channel computes the engagement rate for each user for each of the three channels by taking the ratio of # of opens or interactions to the number of messages received over the last 3 months of activity. The available channels are ranked according to their respective engagement ratios, and the channel with the highest ratio is the "Most Engaged" for that user.

{% alert note %}
If you have requested access to the Channel Optimization (Most Engaged Channel) beta feature, Braze agrees to grant you access to this Beta feature, and by your use of this Beta feature, you agree that such use shall be subject in full to the language in the MSA between you and Braze relating to Beta features.
{% endalert %}

## The "Not Enough Data" Option

For Braze to determine which channel is "best", there needs to be adequate data. This means that you should have sent at least three (3) or more messages on at least two (2) of the three (3) available channels (these messages need not necessarily be opened). 

So, if a user only has data for one (1) channel, or less than three (3) messages received on two (2) or three (3) channels, that user will then fall under the "Not Enough Data" option of this filter. This will allow you to choose to use whichever messaging channel you wish for the users that do not have a "Most Engaged Channel" reliably calculated.

For example, if you want users who prefer _push messages_ to receive a push, as well as users for whom there is not enough data to receive the same push message, you could set the "Most Engaged Channel" filter as "Mobile" and use __OR__ to add a second "Most Engaged Channel" filter set to "Not Enough Data".

## The "Mobile Push" Option

Mobile Push incorporates Android, iOS, Windows, Kindle, and all other mobile device channels available on Braze. When computing the Most Engaged Channel, Braze looks at each kind of mobile device separately, but then chooses the highest engagement rate among them to represent the "Mobile Push" category when comparing against Email and Web Push. So a user with an iPhone, Android phone, and iPad with engagement rates of 0.1, 0.2, and 0.45, respectively would have their Mobile Push engagement rate calculated as the best of all those devices: 0.45. This would not, however, force that user to receive Push notifications on the iPad— they can still be considered as preferring “Mobile Push” even when using the filter on an Android push message.

## Best Practices & Effective Use Strategy

### Tie-Breaking

Because some users will have low numbers of messages received, it is not unusual to have "ties" in engagement rates across the available channels for a single given user (a single user has a 0.2 engagement rate for __both__ Email and Mobile Push). In such cases, ties will be broken by prioritizing (giving a higher ranking to) the channel with the most recent open events.

### Unreachable Channels

When the user has sufficient data for a ranking to be determined, but becomes unreachable on their "Most Engaged Channel", the user will "fall out" and not receive any messages. Braze plans to modify this behavior so that the user will be considered "Most Engaged" on the next most engaged (and reachable) channel.

[1]: {% image_buster /assets/img/most_engaged_channel.png %} "Most Engaged Channel Filter"
