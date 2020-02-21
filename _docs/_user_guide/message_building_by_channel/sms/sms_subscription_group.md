---
nav_title: "SMS Subscription Groups"
page_order: 1
description: "This is the Google Search description. Characters past 160 get truncated, keep it brief."
page_type: reference
tool:
  - Dashboard
  - Docs
  - Campaigns

platform:
  - iOS
  - Android

channel:
  - SMS
---

# SMS Subscription Groups

>  This type of article explains a concept and contains specific information about technical processes and product content (Canvas Steps, Segmentation, a specific type of Object etc.). The other type of Reference template is a Glossary. This format is not used for our API glossary or reference documentation unless there is a specific concept that needs to be explained. Be sure to outline that they will learn [this](#what-is-x-concept), [that](#topic-1-regarding-this-concept), and [the other](#topic-2-regarding-this-concept) on this page. This is a [good sample of a general reference doc](https://guide.meteor.com/code-style.html). This is a good example of a [very technical reference doc](https://www.w3schools.com/html/html_intro.asp).

## What is X Concept

Include:
- This concept's origins, if relevant.
- Links to outside resources about this concept and other names for it as needed.
- How this concept is used and applied at Braze.  
- What are the benefits of this concept


## Topic 1 Regarding this Concept

This should explain a specific aspect of this concept, like how a specific type of Canvas Step is used in combination with a channel. If you would like to see an example of how to do this thing in the wild, please check out [this link to that tutorial]({{ site.baseurl }}/home/templates/tutorial_video.md).

### Code Sample

If you're explaining a technical concept, please note that here and show a code sample.

```html
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```

Make sure you define parameters or elements that users might have to adjust from the sample above. Many users will just copy and paste.

| Variable | Description |
| -------- | ----------- |
| Page Title | You can title your page anything. You have to have this. |
| My First Heading | We recommend putting this in caps. This is also optional. |


## Topic 2 Regarding this Concept

In the event that a second topic is added, be sure to distinguish it from the first concept immediately. Then, go into explaining the concept. You should feel free to add diagrams!

~~~~~~~~~ Info Dump for DW ~~~~~~~~~

## Default Opt-In/ Opt-Out

|| Keyword | Change |
|-|-------|---|
|Opt-In| `START`<br> `YES`<br> `UNSTOP` | Any inbound request with any of these `START` keywords will result in a Subscription Group state change to `subscribed`. Additionally, the pool of numbers associated with that subscription group will now be able to send an SMS message to that customer. |
|Opt-Out| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Any inbound request with any of these `STOP` keywords will result in a Subscription Group state change to `unsubscribed`. Additionally, the pool of numbers associated with that Subscription Group will no longer be able to send an SMS message to that customer. |

- Regulations require that there are responses to all opt-in, opt-out and help/info keyword responses.
- When user responds with default keyword, Braze will automatically update the subscription status for all user profiles with that phone number.

## Double Opt-In Process

You might find that some users who might send a text to your short/long code, won't yet be opted-in to your SMS Subscription Group. Regulations require that you obtain a user’s explicit consent before you send them any promotional or informational messaging. We highly recommend implementing a Double-Opt In to ensure compliance. 

We suggest setting a triggered entry in Canvas whenever there's an incoming event `sms_response_subscriptionGroupName_custom`.

### Step 1: Create Webhook

We first suggest to create a webhook campaign that makes a request to the subscription/status/set endpoint to subscribe the user to that SMS subscription group.

### Step 2: Send a SMS campaign
Next, we recommend sending an SMS campaign a few second later, with clear call-to-actions along the lines of:

[IMAGE]

~~~~~~~~~ End Info Dump ~~~~~~~~~

