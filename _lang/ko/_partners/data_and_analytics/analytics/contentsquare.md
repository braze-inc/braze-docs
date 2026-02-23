---
nav_title: Contentsquare
article_title: Contentsquare
description: "This reference article outlines the partnership between Braze and Contentsquare, a digital experience analytics platform that allows you to improve the relevance and conversion rates of your campaigns by targeting messages based on your customers' digital experience."
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# Contentsquare

> [Contentsquare](https://contentsquare.com/) is a digital experience analytics platform that enables an unprecedented understanding of the customer experience.

_This integration is maintained by Contentsquare._

## About the integration

The Braze and Contentsquare integration allows you to send Live Signals (fraud, frustration signals, etc.) as custom events in Braze. Leverage Contentsquare experience insights to improve your campaigns' relevance and conversion rates by targeting messages based on your customers' digital experience and body language.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Contentsquare account | A Contentsquare account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. To create a new key in the Braze dashboard, go to **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL]({% image_buster /assets/img/contentsquare_custom_events.png %}). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

Some common Braze and Contentsquare use cases include:
- Hyper-personalize messages based on customer intent by surfacing customer experience data within Braze.
- Retarget customers based on their digital behavior, hesitations, frustration, and intent.
- Identify poor experiences within Contentsquare and recover customers with targeted messages and retention offers.
- Recover at-risk customers by sending more relevant and empathetic messages at the right time and place.

## Integration

To integrate Contentsquare into Braze, you must request the installation of a "Live Signals" integration from the Contentsquare integration catalog:

1. In Contentsquare, click **Console** in the **Settings** menu. This will redirect you to the project you are currently working on. 
2. On the **Projects** page, go to the **Integrations** tab and click the  **\+ Add integration** button.
3. In the integrations catalog, locate the **Live Signals** integration and click **Add**. 그러면 콘텐츠스퀘어 팀에서 연락하여 Braze에 실시간 신호를 전송하기 위한 코드 스니펫을 구성할 것입니다.
4. Contentsquare will now process your integration. The indicator text will update after the integration has been completed.

For more information, refer to [Request a Contentsquare integration](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186).

## Using this integration

Once the integration is complete, Contentsquare custom events will be available to use in your campaigns and Canvases. You can check which events are being sent to Braze from **Data Settings** > **Custom Events**.

![Braze 커스텀 이벤트 탭의 Contentsquare 실시간 신호 데이터]({% image_buster /assets/img/contentsquare_custom_events.png %})


