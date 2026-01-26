---  
nav_title: DOTS.ECO  
article_title: DOTS.ECO  
description: "This reference article outlines the partnership between Braze and DOTS.ECO."  
alias: /partners/dots.eco/  
page_type: partner  
search_tag: Partner  
---

# DOTS.ECO  

> [DOTS.ECO](https://dots.eco) enables brands to reward users with real-world environmental impact through trackable digital certificates. Each certificate can include key metadata like a shareable certificate URL and image URL, making it easy to deliver a proof-of-impact experience that users can view and revisit.

_This integration is maintained by DOTS.ECO_

## About this integration

Braze and DOTS.ECO work together to connect customer engagement journeys to real-world impact rewards. From a Braze Canvas or Campaign step, you can trigger a DOTS.ECO certificate creation request using connected content. DOTS.ECO returns certificate metadata (such as certificate URL and image URL), which can be stored on the Braze user profile as custom attributes and reused across channels like in-app messages, content cards, and push notifications

## Use cases

- Trigger a reward (impact certificate) when a user completes a key event (purchase, level completion, subscription, referral).  
- Show a personalized certificate image in an in-app message after the connected content step succeeds.  
- Add a “View your certificate” content card containing the certificate URL for later access.  
- Store certificate metadata (certificate_url, certificate_image_url, certificate_header, greeting) as Braze custom attributes for reuse in future messaging.  
- Assign certificates using a remote user ID, allowing users to claim and view their impact at a later time.  
- Run A/B tests on impact messaging (different copy/images) while keeping the same DOTS.ECO user update flow.


## Prerequisites

Before you start, you need the following:

| Prerequisite       | Description |                          
|-----------------------|-----------------|  
| A DOTS.ECO account   | A DOTS.ECO account is required to take advantage of this partnership.  |  
| A DOTS.ECO Authorisation Key   | The Connected Content request below requires a DOTS.ECO App Token, API Key and Allocation ID. To retrieve these, please reach out to your DOTS.ECO CSM.  |  
| A Braze REST API key  | A Braze REST API key with `users.track` permissions. Create this key in the Braze dashboard from **Settings** > **API Keys**. |  
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance.  |

## Integrating DOTS.ECO

### Step 1: Create a Canvas and add a User Update step

In the Braze dashboard, create a new Canvas that will trigger when a user completes a key event (such as a purchase, subscription, or milestone).

Add a User Update step right after the entry step. This step will be used to call the DOTS.ECO API via Connected Content and store the returned certificate data on the user profile.

### Step 2: Compose Advanced Json - A POST request to DOTS.ECO using Connected Content

Inside the **User Update** step, switch to the **Advanced JSON Editor** and use Braze Connected Content to make a POST request to the DOTS.ECO certificate API.

The "capture" tag and a connected content request are used to make a POST request to DOTS.ECO's certificate endpoint. It will then capture the response, and allow this data to be saved to a user profile as custom attributes.

**Connected Content + User Update example**  
```  
{% capture post_body %} 
{  
  "remote_user_email": "{{${email_address} | default: 'braze+nadav@dots.eco'}}",  
  "app_token": "YOUR_DOTS.ECO_APP_TOKEN",  
  "impact_qty": 1,  
  "remote_user_id": "{{${user_id} | default: ${braze_id}}}",  
  "allocation_id": YOUR_DOTS.ECO_ALLOCATION_ID  
}  
{% endcapture %}

{% connected_content https://impact.dots.eco/api/v1/certificate/add?format=sdk  
  :method post  
  :headers { "auth-token": "YOUR_DOTS.ECO_AUTH_TOKEN" }  
  :body {{post_body}}  
  :content_type application/json  
  :save result  
%}

{  
  "attributes": [  
    {  
      "certificate_image_url": "{{result.certificate_image_url}}",  
      "certificate_url": "{{result.certificate_url}}",  
      "certificate_id": "{{result.certificate_id}}"  
    }  
  ]  
}  
```

The request should be sent to:

`https://impact.dots.eco/api/v1/certificate/add?format=sdk`

![Dots.eco – User Update Step ]({% image_buster assets/img/dots_eco/dotseco_user_update.png %})  

{% alert important %}  
This integration uses Braze Connected Content inside a Canvas **User Update** step to call the DOTS.ECO API. Test requests with an API client (e.g., Postman) first to validate your token and payload.  
{% endalert %}

### Step 3: Display the certificate in messages

Once the certificate attributes are stored on the user profile, they can be referenced in downstream Canvas message steps.

![Dots.eco Flow]({% image_buster assets/img/dots_eco/dots.eco_flow %})  

![Dots.eco Messages Step]({% image_buster assets/img/dots_eco/dotseco_messages.png %})  

![Dots.eco Messages – Compose Section]({% image_buster assets/img/dots_eco/dotseco_messages_compose.png %})  

For example:  
- Show the certificate image in an in-app message using `{{custom_attribute.certificate_image_url}}`  
- Link to the hosted certificate using `{{custom_attribute.certificate_url}}`

![Dots.eco Messages – On-click Behavior]({% image_buster assets/img/dots_eco/dotseco_messages_compose_onclickbehavior.png %})


This allows teams to personalize in-app messages, content cards, or push notifications with real-world impact confirmation.

## Troubleshooting

Connected Content errors can be reviewed in the Braze Dashboard under Settings > Message Activity Log 

* **Connected Content returns empty**: Verify that the *“:save result*” is set and references all relevant fields  
* **Attributes not showing in the “messages” step**:   
  * Confirm that the attributes created in Braze UI have the exact same name as the ones created within the Connected Content  
    * In the User Update step, you can use the “*Preview and test*” tab to see if the attributes are populated. Then, send this test to a user and view them to make sure they are stored properly  
* **422 Error (Unprocessable entity)**: App Token, Impact quantity is invalid  
* **401 Error**: Auth token is wrong or missing  
* **No image preview in Messages step**: Please validate the attributes by clicking “Send Test to User” in the User Update step. Then test the preview with the same user




