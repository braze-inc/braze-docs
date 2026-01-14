---
nav_title: Oracle Crowdtwist
article_title: Crowdtwist
description: "This article outlines the partnership between Braze and Oracle Crowdtwist, by way of specially-created Braze Data-Transformation templates and Crowdtwist's Data Push Objects."
page_type: partner
search_tag: Partner

---

# Oracle Crowdtwist

> [Oracle Crowdtwist](https://www.oracle.com/uk/cx/marketing/customer-loyalty/) is a leading cloud-native customer loyalty solution to empower brands to offer personalized customer experiences. Their solution offers over 100 out-of-the-box engagement paths, providing rapid time-to-value for marketers to develop a more complete view of the customer.

Oracle Crowdtwist's Data Push feature allows user or event metadata to be passed whenever an update occurs in Crowdtwist's platform.

This guide outlines how to integrate Oracle Crowdtwist’s User Profile, User Activity, and User Redemption Live Push feeds into your Braze environment. Two additional Data Push types are available that are not explicitly covered in this documentation, but their setup follows the same principles outlined below. 

* [Live Push User Profile](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/PushUserProfile-withTiersv2.html): Includes creations of new profiles and updates to existing profiles.

* [Live Push User Activity](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html): Includes data on user activity completions.

* [Live Push User Redemption](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserRedemption.html): Includes data on user reward redemptions. 

By using a Braze Data Transformation template, you can filter out the elements of the Data Push that aren't relevant to Braze, and assign the values needed in Braze so that they can be leveraged by the available "destinations".

For example, use a Data Push to pass relevant custom events and attributes to Braze, like when a user changes loyalty tier or redeems a reward. You can also use it to log custom attributes in Braze as soon as that data is updated on a member's user profile, like a user's points balance. 

## Prerequisites


| Requirement | Description |
| --- | --- |
| Oracle Crowdtwist account | An [Oracle Crowdtwist Account](https://www.oracle.com/uk/cx/marketing/customer-loyalty/) is required to take advantage of this partnership. |
| Braze Data Transformation Endpoint| This integration relies on Braze's [Data Transformation Tool]({{site.baseurl}}/user_guide/data/data_transformation/overview). When you create a Data Transformation, Braze generates a unique endpoint that you can add as a destination for Crowdtwist's Data Push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Braze and Oracle Crowdtwist have created [Data Transformation templates]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation?redirected=1#step-2-create-a-transformation) to help our customers develop their own Data Transformations which leverage the User Profile, User Redemption, and User Activity events. 

## Step 1: Create Data Transformation from Oracle Crowdtwist Template

Navigate to **Data Settings > Data Transformation > Create Transformations > Use a Template** > and select the “BRAZE <> CROWDTWIST” template of your choice. 

You will find four templates—one each for transforming User Profile, User Activity, and User Redemption events, and a master template that uses conditional logic to apply to various Data Push events.

As shown in [Oracle Crowdtwist's Data Push documentation](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/DataPush.html), Data Push objects contain different metadata, so each requires its own transformation code to create appropriate Braze objects. The master template illustrates how to set up a single Data Transformation to accept each of the three types of objects and creates an appropriate output with values from each object.

## Step 2: Update and Test Template

Below, you’ll see the annotated templates. The body of these templates is designed to apply to the `/users/track` destination. Annotations are marked by the `//` line-start and green text, and you can delete them without affecting the operation of the transformation code. 

The transformation uses JavaScript, which builds an object called "brazecall". This object is where you create the request body that is sent to a Braze REST API endpoint. For guidance on the required structures of the requests to these destinations, see the links in the "destinations" section.    

{% alert note %} 
Notice that the "values" of each "key" start with `payload.`. The payload represents the data object received from Oracle Crowdtwist. Use JavaScript dot notation to choose what piece of data you want to populate the elements of your Braze object. For example, when you see `external_id: payload.thirdPartyId`, this means that the Braze external ID is set by the `third_party_id` value stored in Oracle Crowdtwist. For more information about the schema or makeup of the objects coming from Oracle Crowdtwist, see [Oracle's documentation](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html).
{% endalert %}

{% alert important %}
 Use the objects sent from Oracle Crowdtwist to create users in Braze. By including the `update_existing_only` key with the value `false`, if an attribute or event object includes an identifier that does not exist in Braze, Braze creates a user profile with the attributes included in the event or attribute object. If you prefer that Oracle Crowdtwist update only profiles that already exist in Braze, set this attribute to `true` in each attribute or event object. 
{% endalert %}

### Data Transformation Templates
{% tabs %}
{% tab User Profile Event Template%}
```javascript
let brazecall = {
 "attributes": [
   {
     //You must include an appropriate identifier for your attribute or event object from data available in Oracle Crowdtwist. This could be an external ID, Braze ID, user alias, phone, or email address for attribute or event objects.
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
   // **Important** To allow Oracle Crowdtwist events to create users in Braze, set the value of "_update_existing_only" to false. Otherwise, set this value to true in your event and attribute objects.
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
 //In this example, the "tierInfo" object from Crowdtwist is transformed into a Braze Nested Custom Attribute. Use the "_merge_objects" value to avoid duplications in a data point efficient manner.
 //The "tierinfo_current_level" attribute is a flat Braze custom attribute, while "tierInfo" below is a nested object mirroring the Crowdtwist payload; the difference in capitalization is intentional.
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{ 
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
//Below we show how to create both custom attributes and events from a single Crowdtwist User Profile object.
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
//Below we can see how to write a timestamp in your object, which is a required value for some objects, like the Event Object. 
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
// After the /users/track request is assigned to brazecall, return brazecall to create an output.
return brazecall;

```

{% endtab %}
{% tab User Activity Event Template %}
```javascript
let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
```
{% endtab %}
{% tab Redemption Event Template %}
```javascript
let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   //A user redemption event may not have a third party id, in which case you can instead provide the opportunity to include a user alias.
   "user_alias": { "alias_name" : "crowdtwist_redemption_username", "alias_label" : payload.userName},
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;

```
{%endtab%}
{% tab Master Template %}
```javascript
//The master template uses JavaScript's conditional operators to determine the output of the Data Transformation. This example shows how to apply JavaScript to your transformation to allow for a dynamic range of sources or inputs. 

 // We open the transformation with a simple "if" function. We're checking if the value "payload.tierInfo" is present. "tierInfo" is a value that is always populated in the User Profile Live Push object, but is not present in the others.

if (payload.tierInfo) {
let brazecall = {
 "attributes": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{ 
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
return brazecall;
//Now we use an "else if" operator to change the "brazecall" body if the object is a User Activity event by checking if the unique key "activityId" has been populated.
} else if (payload.activityId) {
 let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
//Finally, this conditional statement triggers if the Data Push object is a User Redemption event, based on whether a value populates in the key "rewardId".
} else if (payload.rewardId) {
 let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;
} else {
 //Include this error message to help with troubleshooting in the log if a call fails. Replace the text in the parentheses with anything that might be clearer to your team based on your Data Transformation.
 throw new Error("No appropriate Identifiers found");
}

```
{%endtab%}
{% endtabs %}

### Destinations

The templates in this guide are created to deliver to the "Track Users" destination, but you can design your template to send to any of the endpoints listed in [Braze's Data Transformation guide]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation/#step-2-create-a-transformation), with the support of the associated [REST API documentation]({{site.baseurl}}/api/home).

### Testing

After you modify the template to your liking, you must validate that it operates correctly. Click “Validate” to return a preview of your code’s output and to check if it is an acceptable request for your chosen destination. 

![Screenshot of Braze Data transformation UI]({% image_buster /assets/img/crowdtwist_tools/screenshot.png %}){: style="max-width:70%;margin-bottom:15px;border:none;"}

When you're happy with the object you see in the "output" field, click **Activate** so that the Data Transformation endpoint is ready to accept data. 

You'll find your Data Transformation's webhook URL on the left-hand side panel. Copy this and use it for configuration within Oracle Crowdtwist's Integration Hub.

{% alert important %}
The Braze Data Transformation endpoints have a rate limit of 1000 requests per minute. Consider the speed at which you want this data made available in Braze, and speak to your Braze Account Manager if you require a higher Data Transformation rate limit.
{% endalert %}

Data Transformations are a very dynamic tool and you can design them for purposes beyond what is outlined in this document with an understanding of JavaScript and with the guidance of our REST API documentation. For support or troubleshooting on complex changes to your Data Transformation templates, talk to your Customer Success Manager to learn about the guidance available to you.