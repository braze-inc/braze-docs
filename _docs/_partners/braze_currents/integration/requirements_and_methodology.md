---
nav_title: Requirements & Methodology
page_order: 2
---

# Requirements & Methodology

Using Currents with any of our partners requires the same basic parameters and connection methodology.

Each partner requires that Braze has permission to write and send data files to them, and Braze asks for the location they should write those files to, specifically bucket names or keys.

The following requirements are the basic, minimum requirements to integrate with most of our partners. Some partners will require additional parameters, but those will be listed on those partners pages along with any nuances associate with these basic requirements.


| Requirement | Origin | Access | Description
|---|---|---|---|
| Account with Partner | Arrange account with that partner or reach out to your Braze account manager for suggestions. | Check that Partner’s site or reach out to that Partner to sign up. | Braze will not send data to a Partner if you don’t have access to that data through your company’s account.
| Partner API Key or Token | Usually the Partner’s dashboard. | Just copy and paste it into the designated Braze field. | Braze has a designated field for this in the Integrations page for that Partner. We need this to map where we are sending your data.
| Authentication Code/Key, Secret Key, Certification File | Contact a representative for your account with that Partner. May also exist in the Partner’s dashboard. | Copy and paste keys into the designated Braze field. Generate and upload `.json` or other certification files into the appropriate place in Braze. | Braze has a designated field for this in the Integrations page for that Partner. This gives Braze credentials and authorizes us to write files to your Partner account.
| Bucket, Folder Path | Some partners organize and sort data by buckets. This should be found in the Partner’s dashboard. | If this is required, be sure to copy the Bucket name or file path exactly into the designated space in Braze. We don’t want your data to get lost! | Though this is required for some Partners, it’s important to get right when you do need it. |
