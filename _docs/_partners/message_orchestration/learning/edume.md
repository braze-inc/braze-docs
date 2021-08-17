---
nav_title: EduMe
article_title: EduMe
description: "This article outlines the partnership between Braze and EduMe, a mobile-based training tool that allows you to give your workforce or customers access to lessons and courses created in EduMe. They will be able to access this content seamlessly in their browser, and you will be able to follow their progress as a group or as individuals using the EduMe reporting functionality."
alias: /partners/edume/
page_tpe: partner
search_tag: Partner

---

# EduMe

> [EduMe](https://edume.com) is a mobile-based training tool that gives your workforce the knowledge they need to succeed. When they need it, wherever they are. <br><br>Use [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) in Braze to give your workforce or your customers access to lessons and courses in EduMe. They will be able to access this content seamlessly in their browser, and you will be able to follow their progress as a group or as individuals using the EduMe reporting functionality.

## Prerequisites

In order to use Connected Content with EduMe, you will need to set up a few things with your EduMe customer success contact.

| Requirement | Origin | Access | Description |
|---|---|---|---|
| EduMe API Key | EduMe | You must request an API Key from your customer success contact at EduMe | Use the EduMe API key when setting up EduMe Connected Content as described below. |
| EduMe link signing secret | EduMe | You must request your customer success contact at EduMe to set up a link signing secret for your organization. | This secret is used behind the scenes to enable seamless links in Connected Content. You don't have to find this key or do anything with it directly. |
| Knowledge of group and content IDs in EduMe | EduMe | Your customer success contact at EduMe will work with you to help you know the IDs for the relevant content and user groups in EduMe for your use case. | You will use these IDs when setting up the Connected Content snippets following the instructions below. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Connected Content Integration

Use this integration to give your users access to courses and lessons you've published in EduMe.

### Access to a Course

To give a user access to a course, and to track their progress against your internal user ID in EduMe, follow the API call shown in this simple example:

{% raw %}
```
Welcome to my Rickshaw App platform.
Please access your onboarding course at:

{% connected_content
  https://edume-braze-connect.herokuapp.com/getCourseLink?moduleId=12087&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "X-Api-Key": "YOUR-EDUME-API-KEY"
 	}
%}
```
{% endraw %}

### Adapting the Example for Your Own Use Case

To go from the example to your own use case, update the following:
1. Include your EduMe API key where shown in the message.
2. Include the appropriate EduMe `module ID` in the Connected Content API call as the `moduleId` parameter.
3. Users who arrive at EduMe through this link will be added to a team or group of your choosing in EduMe. Find the `ID` for the relevant group or team in EduMe and include it as the `groupId` parameter in the API call.
4. Include an appropriate field from your user data in Braze as the `externalUserId` parameter in the API call. The example assumes this would be found as `driver_id` where you're making the call. You will most likely have an appropriate ID in a different variable. This ID will be available in EduMe reports, allowing you to correlate them with your own systems.
5. Customize the message and include it in the appropriate place in your campaign or Canvas.
6. Test the flow: Send a test message to yourself, access the EduMe content through the link you receive, complete the lesson or course, and verify that you can find the record of your completion in EduMe reports.

### Access to a Lesson

Similarly, a link to a particular lesson can be created by using the following URL in the same way:
{%raw%}
```
https://edume-braze-connect.herokuapp.com/getLessonLink?lessonId=25805&groupId=4719&externalUserId={{${driver_id}}}
```
{%endraw%}
The differences are the API endpoint `getLessonLink`, and providing a lesson ID in the `lessonId` parameter instead of a module ID. Otherwise, everything works the same as for courses.

### Access to an eNPS Survey

As for lessons, a link to a particular eNPS survey can be created by using the following URL:
{%raw%}
```
https://edume-braze-connect.herokuapp.com/getSurveyLink?surveyId=654&groupId=7961&externalUserId={{${driver_id}}}
```
{%endraw%}
Again, the differences are the API endpoint `getSurveyLink`, and providing a surveyId in the `surveyId` parameter. Otherwise it is exactly the same process as for courses.
