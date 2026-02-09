---
nav_title: eduMe
article_title: eduMe
description: "This reference article outlines the partnership between Braze and eduMe, a mobile-based training tool that allows you to leverage Braze Connected Content to give your users access to eduMe courses and lessons in your Braze campaigns."
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# eduMe

> [eduMe](https://edume.com) is a mobile-based training tool that gives your workforce the knowledge they need to succeed, when they need it, wherever they are. 

_This integration is maintained by eduMe._

## About the integration

The Braze and eduMe integration leverages Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) to give your users access to eduMe courses and lessons in your Braze campaigns. Individual and group progress can then be tracked through eduMe reporting functionality.

## Prerequisites

| Requirement | Description |
|---|---|
| eduMe account | An eduMe account is required to take advantage of this partnership. |
| eduMe API key | You must request an API key from your eduMe customer success contact. 이 키는 Braze 커넥티드 콘텐츠 통화에서 사용됩니다. |
| eduMe link signing secret | You must request your customer success contact at eduMe to set up a link signing secret for your organization. This secret is used to enable seamless links in Connected Content. 이 비밀을 가지고 아무것도 할 필요가 없습니다. |
| eduMe group and content IDs | These identifiers are needed to set up your Connected Content calls. 이러한 식별자를 얻는 데 도움이 필요하면 EduMe 고객 서비스 담당자에게 문의하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Create your Connected Content call

To give a user access to a course, lesson, or eNPS survey, and to track their progress against your internal user ID in eduMe, follow the API call shown in this example:

{% raw %}
```
Welcome to my Rickshaw App platform.
Access your onboarding course at:

{% connected_content
  https://connect.edume.com/
  EDUME-CONTENT-LINK-AND-CONTENT-ID&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "x-api-key": "YOUR-EDUME-API-KEY"
  }
%}
```
{% endraw %}

1. Replace `YOUR-EDUME-API-KEY` with your eduMe API key.<br><br>
2. Replace the `EDUME-CONTENT-LINK-AND-CONTENT-ID` with the corresponding content link string and module, lesson, or survey identifier. These identifiers can be found in your eduMe account.
  - Course: `getCourseLink?moduleId=12087`
  - Lesson: `getLessonLink?lessonId=25805`
  - eNPS survey: `getSurveyLink?surveyId=654`<br><br>
3. 이 링크를 통해 에듀미에 도착한 사용자는 선택한 에듀미 팀 또는 그룹에 추가됩니다. Replace `groupId` with the relevant team ID or eduMe group ID. 등록이 필요한 코스를 제외하고는 일반적으로 팀 ID를 사용하며, 이 경우 그룹 ID를 사용해야 합니다.<br><br>
4. Include an appropriate field to map the `externalUserId` field to. The example connected content call uses the `driver_id`, though your field will likely be different. 이 ID는 EduMe 보고서에서 사용할 수 있으므로 시스템과 상호 연관시킬 수 있습니다.<br><br>
5. Lastly, customize and test your message as needed. We recommend you send at least one test message, access the eduMe content, complete the lesson or course, and verify the eduMe analytics are being recorded. 

