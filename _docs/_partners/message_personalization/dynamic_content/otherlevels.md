---
nav_title: OtherLevels
article_title: OtherLevels
description: "OtherLevels Experience Platform."
alias: /partners/OtherLevels/
page_type: partner
search_tag: Partner
---

<!-- In most cases, the ARTICLE_TITLE will be your company name. If your tool requires several separate pages on Braze Docs, you can add a relevant page descriptor to your title, such as "MyCompany Analytics." -->
# OtherLevels

<!-- The description starts with a '>' character and contains an introduction to your company, a link to your main site, and a concise overview of your integration. In a following paragraph, highlight the the relationship between your company and Braze and how this partnership helps your customers. -->
> The [OtherLevels](https://www.otherlevels.com/) Experience Platform uses GenAI to transform how sports brands, publishers and operators connect with their customers, by transforming traditional content into on-brand personalised video and rich media experiences at scale.

*This integration is maintained by OtherLevels.*

## Overview

The Braze and OtherLevels integration allows you to create custom GenAI videos via API calls from your backend to the OtherLevels Experience Platform, then serve these videos to your users as iOS App Push videos via [Braze Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call).

Give your customers a better experience with OtherLevels ground-breaking AI powered experiences. Transform existing and 3rd party content into highly scalable, video and rich media for audiences that already consume content differently, and respond more strongly, to entertaining and contextual personalised experiences.

<!-- Most partner integrations will require the following prerequisites. However, you may add additional prerequisites as needed. -->
## Prerequisites

Before you start, you'll need the following:

| Prerequisite          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| An OtherLevels account   | An OtherLevels account is required to take advantage of this partnership.                                                                     |
| A Braze REST API key  | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.                                                 |
{: .reset-td-br-1 .reset-td-br-2}

This integration requires calling the OtherLevels Experience Platform API as part of the video generation process before messages can be sent to your users from Braze. curl examples are provided as part of this documentation, however we recommend using API clients such as Postman to automate the API calls.

<!-- An optional section you can use to outline the typical or atypical use cases for your integration. -->
## Use cases

With GenAI videos created with the Experience Platform you can:
* Create better experiences for sports owners and leagues, fan engagement, sports books, iGaming and lotteries
* Amplify your customer marketing by transforming text based content, into rich media and video, creating human, engaging, experiences
* Lift outcomes from acquisition to retention by extending, not retooling, your existing Braze integration

<!-- Create step-by-step instructions for integrating your tool with Braze. It's important to be concise and only outline the minimum necessary steps. -->
## Integrating the OtherLevels Experience Platform

### Step 1: Call the OtherLevels Experience Platform API to generate a video

The first step of the integration involves calling the OtherLevels Experience Platform API to generate a new video. Please note that video generation is not instantaneous. Depending on the length and complexity of the video, the content may take up to half an hour to generate. Therefore please plan your messaging schedules and API calls accordingly, so that the API calls to generate videos are made sufficiently ahead of when your messages are scheduled to send from Braze.

{% alert important %}
The following request uses curl. For better API request management, we recommend using an API client, such as Postman.
{% endalert %}

An example API call is provided below with placeholders. For further information about customising the video specifics and how to structure this API call, refer to the section below **Customizing the GenAI Video**.

```bash
curl --request POST \
  --url 'https://exp-platform-api.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media?=' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.0' \
  --data '{
    "task": {
        "type": "tasks",
        "tasks": {
            "image_video_overlay": {
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''",
                "color": "255,255,255,0",
                "y_pos": "0",
                "x_pos": "0",
                "image_input": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_replace_bg.mp4",
                "type": "compose.ImageVideoOverlay"
            },
            "resize_image": {
                "media_input": "= tasks.bg_image.jpg ?? tasks.bg_image.png",
                "type": "compose.MediaResize",
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''"
            },
            "bg_image": {
                "type": "load",
                "url": "BACKGROUND_IMAGE_URL",
                "refresh_interval": "12h"
            },
            "talking_head": {
                "test": false,
                "title": "INSERT_TITLE",
                "caption": false,
                "templateId": "TALENT_TEMPLATE",
                "type": "TALENT_MODEL",
                "variables": {
                    "script": {
                        "name": "script",
                        "properties": {
                            "content": "= tasks.translate_text.text"
                        },
                        "type": "text"
                    }
                }
            },
            "translate_text": {
                "type": "translate_text",
                "source": "en",
                "target": "en",
                "text": "INSERT_SCRIPT"
            },
            "talking_talent_speed": {
                "type": "compose.VideoSetSpeed",
                "speed": "1.0",
                "video_input": "= tasks.talking_head.mp4"
            },
            "talking_talent_replace_bg": {
                "type": "compose.VideoReplaceBg",
                "video_background": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_speed.mp4"
            }
        },
        "output": "image_video_overlay"
    }
}'
```

Replace the following:

| Placeholder          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `OTHERLEVELS_PROJECT_KEY`   | An OtherLevels project key will be provided to you when you are provisioned with an OtherLevels Account.                                                                     |
| `BACKGROUND_IMAGE_URL`  | An HTTPS URL for the background of the video. |
| `INSERT_TITLE` | The title of the video, this is an internal reference and will not be displayed in the video.                                                 |
| `TALENT_TEMPLATE` | A Talent Template ID. OtherLevels will work with you during account provisioning to create a talent (avatar), you may be provided with one or multiple Talent IDs which can be used.                                                 |
| `TALENT_MODEL` | A Talent Model ID. OtherLevels will work with you during account provisioning to create a talent (avatar), you may be provided with one or multiple Talent Models which can be used.                                                 |
| `INSERT_SCRIPT` | The exact script that you would like the talent to say during the video.                                                 |
{: .reset-td-br-1 .reset-td-br-2}

As part of the API response, OtherLevels will return a JSON payload indicating a successful API call. The JSON will contain a unique `recipe_id` to identify the generated video, this `recipe_id` will be required in the next Step.

Here is an example response from the API:

```bash
{"$schema":"https://exp-platform-api.prod.awsotherlevels.com/schemas/GenerateMediaResBody.json","message":"success","recipe_id":"LMINHWXV2BBD6JGV5VF3ZNZV7BDDRR7FH5FJH6MMX4BVLTPRKTWQ","media_short_id":"LMINHWX","status":"triggered"}
```

<!-- Use the "Make a post request", "Default behavior," and "Rate limit" sections to outline how users can make a POST request. If this information isn't required for your integration, you can remove these sections. -->
### Step 2: Setting the recipe_id as a custom attribute against your users

The `recipe_id` you receive from Step 1 should now be set as a Braze custom attribute against the user(s) that you wish to send the videos to.

Depending on your use case, you may have generated a single video that is intended for a large audience, in which case this same `recipe_id` can be set against multiple users. Alternatively you may have generated multiple unique videos each targeting a different user, in which case each user should have their custom `recipe_id` set as Braze custom attributes.

{% alert important %}
The following request uses curl. For better API request management, we recommend using an API client, such as Postman.
{% endalert %}

```bash
curl --location --request POST 'BRAZE_API_ENDPOINT/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer BRAZE_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "USER_ID",
      "olxpmedia": "RECIPE_ID"
    }
  ]
}'
```

Replace the following:

| Placeholder             | Description                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | The Braze REST endpoint URL of your current Braze instance. For more information, see [Rest API keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys). |
| `BRAZE_API_KEY`         | Your Braze REST API key with the `users.track` permission.                                                                                                                                      |
| `USER_ID`              | The User ID who will be receiving this particular video. For further examples of the identifiers which can be used please our [/users/track documentation]({{site.baseurl}}/docs/api/endpoints/user_data/post_user_track#track-users).                                                                                                                                                  |
| `RECIPE_ID`       | The recipe_id received from the OtherLevels API response in Step 1.                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2}

### Step 3: Sending via Braze Connected Content

To send the GenAI videos as iOS App Push messages to your users. 

1. Create a Braze iOS Push Notification Campaign based on your normal marketing processes.
2. In the Compose section of the draft campaign, under the **Assets** section, paste the following connected content syntax within the **Add from URL** field.

```
{% connected_content https://exp-platform-api-external.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media/{{custom_attribute.${olxpmedia}}} %}
```

Replace `OTHERLEVELS_PROJECT_KEY` with the project key supplied to you by OtherLevels.

3. In the next field **URL file format**, select **MP4** from the dropdown
4. The remainder of the campaign such as the message content, schedule, target audience and conversions should be configured based on your desired preferences.

![Example Asset fields for Connected Content.]({% image_buster assets/img/otherlevels/1.png %})

<!-- An optional section you can use to outline additional customization steps. It's important to be concise and only outline the minimum necessary steps. -->
## Customizing the GenAI Video

### Video size and attributes

The video background can be specified within the `bg_image` key.

| Parameter             | Description                  |
|-------------------------|----------------------------|
| `url`    | HTTPS url for the background image. |
{: .reset-td-br-1 .reset-td-br-2}

The video background size can be specified within the `resize_image` key.
We recommend that the background image is sized the same as what in configured here.

| Parameter             | Description                  |
|-------------------------|----------------------------|
| `width`    | Width of the background image can be specified, with options for both portrait and landscape modes. |
| `height`     | Height of the background image can be specified, with options for both portrait and landscape modes.                              |
{: .reset-td-br-1 .reset-td-br-2}

Video Overlay Options can be specified within the `image_video_overlay` key.

| Parameter             | Description                  |
|-------------------------|----------------------------|
| `width`    | Width of the overlay can be specified, with options for both portrait and landscape modes. |
| `height`         | Height of the overlay can be specified, with options for both portrait and landscape modes.                                              |
| `color`              | Color of the overlay specified in RGB along with transparency video.                                                                   |
| `y_pos`       | Y Axis offset from center.                                                              |
| `x_pos`    | X Axis offset from center. |
{: .reset-td-br-1 .reset-td-br-2}

### Talent and script

As part of provisioning, OtherLevels will work with you to generate one or multiple Talents (sometimes referring to as avatars) for use in your videos. Depending on your use case and brand, this may be made in the form of one of your existing brand ambassadors or a unique creation.

One these are created, you will be provided with usable `TALENT_TEMPLATE` and `TALENT_MODEL` IDs to be used with our API.

The Voice model used to process input scripts works best when providing a natural script as a human would read. In most cases there is no requirement to add extra punctuation to manually guide the script. However we always recommend testing your scripts before sending to a real audience.

The speed at which the talent will read the script can be specified within the `talking_talent_speed` key.

| Parameter             | Description                  |
|-------------------------|----------------------------|
| `speed`    | Specify the speed at which the talent will read the script, for example 1.5 |
{: .reset-td-br-1 .reset-td-br-2}

## Additional Notes

* Currently only the iOS Push Notification platform natively supports video media. Android push notifications do not natively support videos so this integration can only be used with your iOS audience
* When receiving video push notifications on iOS devices, users will need to press and hold the push notification for the video to load and play. This is standardised behaviour on the iOS platform and cannot be customised.
* Soon we will be providing an option to call a simplified API call with preconfigured video attributes, whereby the only modification required is the script. This will be useful in cases where the talent and video attributes remain largely unchanged.
