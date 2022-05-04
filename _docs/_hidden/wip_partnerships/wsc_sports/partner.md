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

### Sending push notifications
### Sending rich media push notifications

## Integration

### Step 1: Segments and Campaigns

Set the user segements and you campaigns in the Braze developer console

### Step 2: Endpoint usage

Our actions will deliver a request to the following braze endpoints:
| Endpoint | 
| ----------- | 
| /messages/schedule/create | 
| /messages/send |

Example:
```
{
  "apple_push": {
    "alert": {
      "body": "New Video"
    },
    "asset_url": "https://wsczoominnba.prod-cdn.clipro.tv/nba-editor/9109acd0-52a2-4475-8667-210fb212cd8c.mp4",
    "asset_file_type": "mp4"
  }
}
```
### Step 3: Using Clipro

The clipro app will handle the creation of you request

### Step 4: Preview your request

At this point, your campaign should be ready to test and send. Check the Braze developer console error message logs if you run into errors. 


[1]: https://wsc-sports.com/