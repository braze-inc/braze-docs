---
nav_title: WSC Sports
article_title: WSC Sports
page_order: 1

description: "WSC Sports' platform generates personalized sports videos for every digital platform and every sports fan - automatically and in real-time."
alias: /partners/wsc_sports/

page_type: partner
search_tag: Partner
hidden: true

---

# WSC Sports

> [WSC Sports'][1] platform generates personalized sports videos for every digital platform and every sports fan - automatically and in real-time. 

WSC Sports uses Braze integration to deliver rich and robust media to customers via push notifications.

## Prerequisites


| Requirement | Description |
| ----------- | ----------- |
| WSC account | A WSC account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |

## Use cases

- Sending push notifications
- Sending rich media push notifications
- Sending scheduled push notifications

## Usage

### Setting user segments and campaigns

Setting user segmentations and campaigns allows for large scaling messaging to specific groups of users or during specific time periods.
Set up the segments and campaigns through the Braze developer console.


### Braze integration

Our app handles the end-to-end process, from the selection of the video to the arrival of the push notification on the end users' device.
After selecting and setting the appropriate options available on our platform:

![braze_integration.jpg][2]

Our internal processes will deliver the video as a push notification to the selected user segments, 
using the following Braze endpoints, according to the options selected:

| Endpoint | 
| ----------- | 
| /messages/schedule/create | 
| /messages/send |


### End result

The resulting body of the message is as follows: 
```
{
  "apple_push": {
    "alert": {
      "body": "Push Message Title"
    },
    "asset_url": "internalURI.mp4",
    "asset_file_type": "mp4"
  }
}
```

### Step 4: Preview your request

At this point, your campaign should be ready to test and send. Check the Braze developer console error message logs if you run into errors. 


[1]: https://wsc-sports.com/
[2]: {% image_buster /assets/img/wsc-sports/braze_integration.jpg %} "braze_integration.jpg"