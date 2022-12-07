---
nav_title: Braze Data Transformation
permalink: "/data_transformation/"
hidden: true
---

# Braze data transformation

Braze Data Transformation allows you to set up and automate a direct integration from various external platforms to Braze, via API-based notifications (commonly called webhooks). These webhooks usually contain valuable information and can send in real-time as events occur.

{% alert important %}
Braze data transformation is currently in early access. Contact your Braze customer success manager if you're interested in participating in the early access.
{% endalert %}

Once these webhooks are sent to Braze, they can be transformed into relevant user data, such as attributes, events, or purchases on Braze user profiles. You can then use this user data to power your marketing use cases.

The end result is a low-code solution for building integrations between your desired external platform and Braze. This may replace your team’s dependency on making manual API calls, integration tools or even customer data platform tools.

## How it works

In Braze, you will first define a transformation - this is a mapping between the expected contents of an incoming webhook and Braze attributes, events, or purchases. You have full flexibility to mix and match what the webhook provides with how you want it to appear in Braze. To help you with this, you can define the transformation side-by-side with a recently received webhook.

Once your transformation is defined, you can configure your external platform’s webhooks to send directly to Braze. Your transformation will apply to every webhook ingested, and your direct integration is now complete.

## Limitations

As of December 2022, submitted transformations will take approximately 2 to 3 days for the Data Transformation team to approve. We will be manually reviewing your submitted transformation to ensure correctness to your desired use case. In later versions of this feature, transformations can be enabled instantaneously.

## Use case

An example would be with Typeform, the online form building and survey software. Typeform can send webhooks with detailed information every time a survey is submitted, and you can direct those webhooks directly to Braze via data transformation.

This enables various use cases, such as:

- You want to sync the act of a user completing the survey as a Braze custom event, so that you can retarget users who didn’t complete the survey.
- You want to sync some of the answers submitted in the survey as custom attributes, as it’s valuable first party data that can power personalized messaging experiences in the future.

## Frequently asked questions

### What gets synced with data transformation?

Any data that the external platform makes available in a webhook can be synced to Braze. The more an external platform sends via webhooks, the more options there are for you to choose what gets synced.

### I'm a marketer. Do I need developer resources to use data transformation?

While we would love for developers to use this feature as well, you don’t need to be one to use this! We’ve seen marketers successfully set up transformations without developer resources.

### Can I still use data transformation if my external platform only gives a user's email address in their webhooks, without a matching user ID to Braze?

Yes! In your transformation, you can use a get_user_for_email function to have Braze take an email address and return a user profile for you to map to. Check out the example for advanced transformation.

### How do I check that my data transformation is correct?

Share your transformation code draft with the Braze Data Transformation team at [data-transformation@braze.com](mailto:data-transformation@braze.com). 
