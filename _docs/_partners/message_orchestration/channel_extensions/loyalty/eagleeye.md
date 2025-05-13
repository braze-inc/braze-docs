
### Eagle Eye Integration with Braze

## Overview

The Eagle Eye Connect is a bi-directional integration between Braze and AIR that enables brands to activate loyalty and promotional data directly in Braze. Clients can issue rewards in AIR to consumers entering an audience in AIR.  This allows marketers to personalize customer engagement using real-time data such as point balances, promotions, and reward activities.

## Prerequisites

| Requirement              | Description |
|--------------------------|-------------|
| Eagle Eye AIR account    | You need an active Eagle Eye AIR account to take advantage of this partnership.  
If you're interested in using Eagle Eye AIR, reach out to Eagle Eye’s Partnerships team at partnerships@eagleeye.com to get started. |
| Braze REST API key       | A Braze REST API key with `users.track` permissions.  
This can be created in the Braze dashboard from Settings > API Keys. |
| Braze REST endpoint      | [Your REST endpoint URL](https://www.braze.com/docs/api/basics/#endpoints). Your endpoint depends on the Braze URL for your instance. |

## Integration

The table below outlines the two types of integrations supported between Braze and Eagle Eye AIR. Eagle Eye Connect is the middleware that enables data exchange between AIR and partner systems like Braze. To learn more about the integration, refer to Eagle Eye’s [documentation](https://developer.eagleeye.com/docs/braze).

| Integration Type | Direction           | Initiated By | Data Flow                        | Purpose                                                                                                                                                     | Example |
|------------------|---------------------|--------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Outbound         | Eagle Eye → Braze   | Eagle Eye    | To Braze API                     | Send loyalty data into Braze user profiles as custom attributes via custom events. Within Braze, the ingested data can be used to:  
- segment users, trigger campaigns, and  
- personalize messages | - Sending loyalty points or tier status into Braze (`ee_loyalty.points.current`, `ee_loyalty.tier.tierId`)  
- Updating a user's profile when they receive or redeem a coupon. |
| Inbound          | Braze → Eagle Eye   | Braze        | To Eagle Eye API via webhook     | When a consumer enters an audience in Braze from any source, Braze can trigger a Braze webhook to EE Connect, allowing EE to issue a reward (coupon or points)  
Upon completion of the action in AIR, Braze would receive an outbound event from AIR. | - Rewards (Coupon or points) are issued to a consumer for joining the loyalty program  
- Rewards are issued to a consumer that had a late delivery  
- Birthday Rewards |

## Data Mapping

The custom data that can be sent to Braze as custom attributes or events can be found in the data model in Eagle Eye’s [documentation](https://developer.eagleeye.com/docs/braze#data-model).

## Setup Instructions

### Config Service for EE Connect

Inbound and outbound connectors can currently be set up via API with support from the Eagle Eye team. A self-serve option will soon be available directly within the AIR dashboard.

To set up the integration, you’ll work closely with your Eagle Eye team through the following steps:

1. **Provide Configuration Details**  
   a. Braze API Credentials  
   Share your Braze REST endpoint, App Identifier, and API Key securely with your Eagle Eye contact.  
   b. Confirm Identifier Matching  
   Determine and share the primary user identifier for profile updates that is common in AIR and Braze, such as External ID or Email.  
   c. Provide Auth Key for security  
   Determine and share a secret auth key for each inbound and outbound connector  
   d. Determine currency  
   Share the 3 digit currency code for display of monetary purchase amounts for e.g. USD

2. **Eagle Eye Connect Configuration**  
   Your Eagle Eye team will configure Eagle Eye Connect with the above details along with unique AIR API credentials and outbound events for the connectors

3. **Configure Social Behavioral Actions in AIR**  
   Set up one or more Social Behavioural Actions in AIR with unique action references to issue points or coupons

4. **Braze Configuration**  
   Set up Campaigns in Braze to issue rewards in AIR  
   Set up any communications to consumers when AIR events are received

5. **Test the Integration**  
   Make API calls in AIR and observe event data flow into your Braze workspace. Validate data received from AIR and confirm attributes are updating as expected.  
   Add users to audiences and confirm rewards are issued in AIR.

6. **Launch in Production**  
   Once testing is successful, the integration can go live to continuously send data to Braze. The same configuration steps are required for production environments in AIR and Braze

Reach out to your Eagle Eye Customer Success Manager to have a resource assigned to you, to set up EE Connect.

## Use Cases

- Trigger Braze campaigns based on loyalty events like point thresholds or rewards earned.
- Enrich Braze user profiles with real-time loyalty data to enable more personalized targeting.
- Track and report on campaign effectiveness tied to reward redemptions.
- Issue rewards in AIR when users enter campaigns in Braze.

## Support

For integration support or troubleshooting, please contact the Eagle Eye support team at support@eagleeye.com







