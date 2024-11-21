---
nav_title: Data Tracking
article_title: Data Tracking
description: "This article covers the data that is tracked on landing pages, and how landing page data collection affects user tracking and cookie consent."
page_order: 3
alias: /landing_pages/data_tracking/
---

# Data tracking

> Braze landing pages use a version of the Braze web SDK to track user data only when a landing page form is submitted. Information that isn't associated with a specific user, including page views and button click aggregate counts, is collected without the web SDK.<br><br>This page covers the data that is tracked on landing pages, and how landing page data collection affects user tracking and cookie consent.

## Tracking methods

### Web SDK

The Braze web SDK is initialized only when a user submits a form on the landing page. Prior to form submission, no personal data is collected and the SDK doesn't actively track users. After initialization is completed, the SDK doesn't store any data in the browser (such as cookies, local storage, or others).

When a form is submitted, the SDK will collect the following data:

- Form submission event (name of event and time of submission)
- Data specified by your team in the form (such as name, email, and phone number)
- Session start time
- Device ID (a unique ID that is generated, but not stored, for the device)
- Country determined by IP address

### Anonymized data

Before a user submits a form, the data tracked on a landing page consists only of anonymized, non-identifiable information. This includes standard website tracking metrics like the number of page views (impressions) and clicks that a landing page receives.

Because this data isn't linked to identifiable users, it can't be used to retarget or track individual user behavior.

## Impact on user tracking and cookie consent

Landing pages were built to adhere to privacy regulations, but we still recommend reviewing the above information with your legal team to determine if there are any consent collection mechanisms required for your company and use cases.

Braze landing pages rely on local storage and anonymized data collection, so they can operate without requiring explicit cookie consent from users prior to form submission. 