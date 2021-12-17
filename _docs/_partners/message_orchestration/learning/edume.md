---
nav_title: EduMe
article_title: EduMe
description: "This article outlines the partnership between Braze and EduMe, a mobile-based training tool that allows you to leverage Braze Connected Content to give your users access to EduMe courses and lessons in your Braze campaigns."
alias: /partners/edume/
page_tpe: partner
search_tag: Partner

---

# EduMe

> [EduMe](https://edume.com) is a mobile-based training tool that gives your workforce the knowledge they need to succeed, when they need it, wherever they are. 

The Braze and EduMe integration leverages Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) to give your users access to EduMe courses and lessons in your Braze campaigns. Individual and group progress can then be tracked through EduMe reporting functionality.

## Prerequisites

| Requirement | Description |
|---|---|
| EduMe account | A EduMe account is required to take advantage of this partnership. |
| EduMe API key | You must request an API key from your EduMe customer success contact. This key will be used in your Braze Connected Content call. |
| EduMe link signing secret | You must request your customer success contact at EduMe to set up a link signing secret for your organization. This secret is used to enable seamless links in Connected Content. You will not have to do anything with this secret. |
| EduMe group and content IDs | These identifiers are needed to set up your Connected Content calls. Reach out to your EduMe customer service contact for help obtaining these identifiers. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Create your Connected Content call

To give a user access to a course, lesson, or eNPS survey, and to track their progress against your internal user ID in EduMe, follow the API call shown in this example:

{% raw %}
```
Welcome to my Rickshaw App platform.
Please access your onboarding course at:

{% connected_content
  https://edume-braze-connect.herokuapp.com/
  <EDUME-CONTENT-LINK-AND-CONTENT-ID>&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "X-Api-Key": "<YOUR-EDUME-API-KEY>"
  }
%}
```
{% endraw %}

1. Replace `<YOUR-EDUME-API-KEY>` with your EduMe API key.<br><br>
2. Replace the `<EDUME-CONTENT-LINK-AND-CONTENT-ID>` with the corresponding content link string and module, lesson, or survey identifier. These identifiers can be found in your EduMe account.
  - Course: `getCourseLink?moduleId=12087`
  - Lesson: `getLessonLink?lessonId=25805`
  - eNPS survey: `getSurveyLink?surveyId=654`<br><br>
3. Users who arrive at EduMe through this link will be added to an EduMe team or group of your choosing. Replace `groupId` with the relevant EduMe group or team ID.<br><br>
4. Include an appropriate field to map the `externalUserId` field to. The above example uses the `driver_id`, though your field will likely be different. This ID will be available in EduMe reports, allowing you to correlate them with your systems.<br><br>
5. Lastly, customize and test your message as needed. We recommend you send at least one test message, access the EduMe content, complete the lesson or course, and verify the EduMe analytics are being recorded. 
