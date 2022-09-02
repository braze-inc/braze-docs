---
nav_title: Testing Canvases
article_title: Testing Canvases
page_order: 1
description: "This reference article covers how to test a Canvas before launch."
page_type: reference
tool: Canvas
---

# Testing Canvases

After [creating your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), there are several checks you may want to perform before launching, depending on details such as your audience size or number of segmentation filters.

## Creating your test plan

When possible, Braze recommends testing a Canvas before launching. This test will typically take place in your Braze environment. Testing your Canvas can involve duplicating it, taking test users through the user journey, and checking if the user behavior aligns with what you have outlined in your Canvas. 

When you're testing a Canvas with multiple branches that target users based on different attributes and events, follow this testing plan:

1. For each branch, identify the attributes and events that the user must have to be included in the Canvas journey.
2. Build those into JSON payload to be posted using the [User Track endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

As you create your testing plan, consider the following questions:
- Has at least one user been created for each Canvas branch and path?
- Are any segments being used in your Canvas? 
	- If segments are used, there may be prerequisites for a user to fall into the Canvas before they're eligible for a user journey.
- Do the messages in the test Canvas have any Liquid in the message titles that pull into the user ID or email address to ensure they are easy to identify both the message and user for testing purposes?

Once the test plan has been completed, duplicate the Canvas, and when ready, launch the test Canvas. Once the test Canvas is live, the JSON payloads can be sent to Braze from Postman so users start moving through the relevant Canvas branches. 

## Creating a test user

## Reducing time delays

To run tests effectively, we suggest reducing time delays to minutes or seconds for testing purposes so you can view messages in a timely manner. 

**Payload examples**

```json
{
        ""attributes"": [ 
         {
           ""external_id"":""test_user_123A"",
    ""email_address"":""test_user_123@company.com"",
      ""L1_category_browsed"": ""shoes""
    }
    ],
    ""events"": [
    {
      ""external_id"": ""test_user_123A"",
      ""name"": ""browsed_category"",
      ""time"": ""2021-08-10T18:20:30+0:00""
    }  
   ]
}
```

```json
{
        ""attributes"": [ 
         {
           ""external_id"":""test_user_123B"",
    ""email_address"":""test_user_123B@company.com"",
      ""L1_category_browsed"": ""shoes""
    }
    ],
    ""events"": [
    {
      ""external_id"": ""test_user_123B"",
      ""name"": ""browsed_category"",
      ""time"": ""2021-08-10T18:20:30+0:00""
    }  
   ]
}
```

