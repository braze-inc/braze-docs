---
title: "Movable Ink Da Vinci"
article_title: Movable Ink Da Vinci
alias: "/partners/movable_ink_da_vinci/"
description: "The Braze and Movable Ink Da Vinci integration empowers brands to deliver highly personalized messaging by leveraging Da Vinci's AI-driven content decisioning engine. Da Vinci curates the most relevant content for each user and seamlessly deploys messages through Braze."
page_type: partner
search_tag: Partner

---

# Movable Ink Da Vinci

> The Braze and Movable Ink [Da Vinci](https://movableink.com/da-vinci) integration empowers brands to deliver highly personalized messaging by leveraging Da Vinci’s AI-driven content decisioning engine. Da Vinci curates the most relevant content for each user and seamlessly deploys messages through Braze.

## Prerequisites

| 요구 사항 | 설명 |
|------------|-------------|
| Movable Ink Da Vinci | A Movable Ink Da Vinci account is required to take advantage of this partnership. |
| Braze Currents - Message Engagement Events | A Braze Custom Currents Export is required to send message engagement event data to Movable Ink. |
| Braze REST API 키 | A Braze REST API key with `messages.send`, `sends.id.create`, and `campaigns.details` permissions is required. This can be created in the Braze dashboard from **Settings**\* > **API Keys**. <br><br>Your Movable Ink account team will provide more setup instructions directly. Refer to the [Integration](#integration) section.|
| Da Vinci app instance in Braze | Create a dedicated Da Vinci app instance in Braze. A new app can be created in the Braze dashboard by going to **Settings** > **App Settings** > **\+ Add App**. Name the app "**Movable Ink - Da Vinci**" and select any platform (a platform selection is required but the type does not impact functionality). Learn more about [how to add a new app]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/#step-3-add-your-app-instances). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

To get started with the integration, contact your Movable Ink account team for assistance. Movable Ink will provide access and setup instructions accordingly. You will need to provide Movable Ink with a set of Braze API credentials to enable Da Vinci to send email deployments through Braze’s Messaging API.

When connected, Movable Ink will:

- Work with the client and Braze to set up the brand’s Da Vinci account to successfully deploy with Braze.
- Capture brand-specific configurations to align with your messaging use cases.
- Conduct comprehensive testing and quality assurance to validate that emails are delivered as intended and meet all performance and operational standards.
