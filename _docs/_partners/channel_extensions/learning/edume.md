---
nav_title: EduMe

description: "EduMe is a mobile-based training tool that gives your workforce the knowledge they need to succeed. When they need it, wherever they are."
alias: /partners/edume/

---

# EduMe

[EduMe](https://edume.com) is a mobile-based training tool that gives your workforce the knowledge they need to succeed. When they need it, wherever they are.

Use [connected content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) in Braze to give your workforce or your customers access to lessons and courses in EduMe. They will be able to access this content seamlessly in their browser, and you will be able to follow their progress as a group or as individuals using EduMe reporting functionality.

## Pre-Requisites

In order to use the connected content, you will need to set up a few things with your EduMe customer success contact.

| Requirement | Origin | Access | Description |
|---|---|---|---|
| EduMe API Key | EduMe | You will need to request an API Key from your customer success contact at EduMe | Use the EduMe API key when setting up EduMe connected content as described below |
| EduMe link signing secret | EduMe | You will need to request your customer success contact at EduMe to set up a link signing secret for your organisation | This secret is used behind the scenes to enable the seamless links we use in the connected content. You don't have to find this key or do anything with it directly. |
| Knowledge of group and content IDs in EduMe | EduMe | Your customer success contact at EduMe will work with you to help you know the IDs for the relevant content and the relevant user groups in EduMe for your use case | You will use these IDs when setting up the connected content snippets following the instructions below. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Connected Content Integration

Using this integration you are able to give your users access to courses and lessons you've published in EduMe.

### Access to a course

To give a user access to a course, and to track their progress against your internal user ID in EduMe, follow the patters shown in this simple example:

```
Welcome to my Rickshaw App platform.

Please access your onboarding course at:

{% raw %}
{% connected_content
  https://edume-braze-connect.herokuapp.com/getCourseLink?moduleId=12087&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "X-Api-Key": "YOUR-EDUME-API-KEY"
 	}
%}
{% endraw %}
```

### Adapting the Example to Your Own Use Case

To go from an example to your own use case, change the following:
1. Include your EduMe API key where shown in the message
2. Include the appropriate Edume `module ID` in the connected content API call as the `moduleId` parameter
3. Users who arrive to EduMe through this link will be added to a team or group of your choosing in EduMe. Find the `ID` for the relevant group or team in EduMe and include it as the `groupId` parameter in the API call.
4. Include an appropriate field from your user data in Braze as the `externalUserId` parameter in the API call. The example assumes this would be found as `driver_id` where you're making the call. You will most likely have an appropriate ID in a different variable. This ID will be available in EduMe reports, allowing you to correlate them with your own systems.
5. Customize the message and include it in the appropriate place in your canvas
6. Test the flow: Send a test message to yourself, access the EduMe content through the link you receive, complete the lesson or course, and verify that you can find the record of your completion in EduMe reports.

### Access to a Lesson

Similarly, a link to a particular lesson can be created by using the following URL in the same way: `https://edume-braze-connect.herokuapp.com/getLessonLink?lessonId=25805&groupId=4719&externalUserId={{${driver_id}}}`. The differences are the API endpoint `getLessonLink`, and providing a lesson ID in the `lessonId` parameter instead of a module ID. Otherwise everything works the same as for courses.
