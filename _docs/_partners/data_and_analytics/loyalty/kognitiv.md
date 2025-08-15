---
nav_title: Kognitiv inspire
article_title: Kognitiv Inspire
description: "Kognitiv Inspire is a loyalty technology system that allows you to implement and evaluate your loyalty strategy, offering innovative capabilities and tailored member communications for enhanced program efficacy."
alias: /partners/kognitiv/
page_type: partner
search_tag: Partner
---

# Kognitiv Inspire

> [Kognitiv Inspire](http://kognitiv.com) is a loyalty technology system that helps unlock unparalleled customer experiences through results-driven loyalty programs that amplify customer engagement, augment spending, and celebrate loyal behavior.

_This integration is maintained by Kognitiv Inspire._

## About the integration

The Braze and Kognitiv integration allows you to implement and evaluate your loyalty strategy, offering innovative capabilities and tailored member communications for enhanced program efficacy.

## Prerequisites

| Requirement | Description |
|---|---|
| Kognitiv account | A [Kognitiv](http://kognitiv.com) account is required to take advantage of this partnership. |
| Kognitiv API key | A Kognitiv REST API key. This can be created within the **API Security Tokens** page. |
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the Braze URL for [your instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

- **Personalized loyalty program enrollment**: Propel your members on their loyalty journey with seamless program enrollment and a customized welcome notification delivered through their preferred channel.
- **Reward issuance and engagement notification**: Keep the spark of loyalty alive by issuing rewards and notifications that celebrate each member's milestone.
- **Strategic member tiering and segmentation**: Enable a more personalized engagement by tiering and segmenting members based on spending, engagement, and simple or complex business rules tailored to your brand's specific needs.
- **Real-time promotion eligibility notification**: Make each member feel special with instant notifications of their eligibility for exclusive promotions.

## Integration

Use Kognitiv webhooks to send requests to Braze when loyalty events occur. The following examples illustrate how to use Kognitiv and Braze to issue a reward, register a Kognitiv user in Braze, and send them a welcome email.

{% raw %}
### Braze issue reward

The following Kognitiv example issues a member reward. Kognitiv Inspire will communicate that reward issuance event to Braze as a custom event via webhooks. To send a follow-up email to communicate the reward, create a campaign or Canvas that triggers off that custom event.

**Webhook URL**: `<braze-api-rest-endpoint>`
**Request Body**: `Raw Text`

- **HTTP Method**: POST
- **Request Headers**:
  - **Authorization**: Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### Request body

```json
{ 
  "events" : [ 
    { 
    "external_id" : "{{memberId}}", 
    "app_id" : "93ec5a59-3752-4a45-8559-55b61209ba38", 
    "name" : "rewards_issued", 
    "time" : "{{issuedDate}}", 
    "issued_date" : "{{issuedDate}}", 
    "issued_location_name" : "{{issuedLocationName}}", 
    "reward_type" : "{{rewardType}}" 
    } 
  ] 
}
```

### Create a user and send a welcome email

The following Kognitiv example creates a new user in Braze when they enroll in KLS. To schedule a welcome email for this user, create a campaign or Canvas in Braze that triggers based on specific custom attributes.

**Webhook URL**: `<braze-api-rest-endpoint>` <br>
**Request Body**: `Raw Text`

- **HTTP Method**: POST
- **Request Headers**:
  - **Authorization**: Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### Request body

```json
{ 
  "attributes": [ 
    { 
      "app_id": "93ec5a59-3752-4a45-855b6109ba38", 
      "bio": "Software Architect", 
      "country": "{{memberAddressCO}}", 
      "email": "{{memberEmail}}", 
      "email_subscribe": "opted_in", 
      "external_id": "{{memberId}}", 
      "first_name": "{{memberFirstName}}", 
      "home_city": "{{memberAddressCity}}", 
      "time_zone": "America/Chicago", 
      "total_points_balance": "{{memberPointsAvailable}}", 
      "CreatedKLS": "{{issuedTimestamp}}", 
      "email_contact_allowed" : "{{memberEmailContactAllowed}}", 
      "sms_contact_allowed" : "{{memberSmsContactAllowed}}", 
      "date_joined": "{{issuedDate}}" 
    } 
  ] 
}
```
{% endraw %}

## Kognitiv Inspire documentation and integration features

Once you integrate Braze with Kognitiv Inspire, Kognitiv empowers you to access its extensive API portfolio, cutting-edge webhook features, and robust data import and export capabilities for seamless bulk transfer. For more information on Kognitiv Inspire features and integration capabilities, view the Kognitiv [resource guide](https://info.kognitivloyalty.com) or contact them for a guided demonstration.

### Endpoints

**REST API authorization**
- US region: `https://app.kognitivloyalty.com/Auth/connect/token`
- CA/EMEA region: `https://ca.kognitivloyalty.com/Auth/connect/token`
- APAC region: `https://aus.kognitivloyalty.com/Auth/connect/token`

**REST API (base URL)**
- US region: `https://app.kognitivloyalty.com/api`
- CA/EMEA region: `https://ca.kognitivloyalty.com/api`
- APAC region: `https://aus.kognitivloyalty.com/api`

**Web services endpoints (base URL)**
- US region: `https://app.kognitivloyalty.com/WS`
- CA/EMEA region: `https://ca.kognitivloyalty.com/WS`
- APAC region: `https://aus.kognitivloyalty.com/WS`

For more information on configuring access tokens and SFTP endpoints, contact Kognitiv for a demonstration.


