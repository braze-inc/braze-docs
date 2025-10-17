---
nav_title: Improving Low Latency Requirements
article_title: Improving Low Latency Requirements
page_order: 10
description: "This article covers strategies to ensure low-latency requirements are met with Content Cards."
channel:
  - content cards
---

{% alert tip %}
Are you trying to display prominent, customized banners on your app or website? Try [Banners](#todo) - built to support low latency banner use cases.
{% endalert %}

# Content Cards as Banners

If you are experience latency with your Content Cards implementation for critical pages (eg: homepage banners), there are a few strategies and tips to help resolve and speed up your rendering.

## 1. Use Schedule Entry instead of Action-based Entry

Action-based cards (Campaigns or Canvas) require background processing where Braze must first receive notice of the triggering action (eg: a purchase has occured, a session start), and then create the user's content card. As a result, these cards won't be available until some time after the event is sent up.

Action-based cards will introduce added complexity to your application where you may find yourself continuously polling and refreshing to wait for the card to be available.

Instead, configure your card to be "scheduled" - which will act as an availablility window for the card to always be available to the targeted audience.

If you schedule your cards in advance, they'll be ready, waiting for the user to open you app and request cards.

## 2. Use "At First Impression" send logic

Together with scheduled sends, the "At First Impression" option will avoid latency due to the speed in which a card is created and stored in Braze. Instead of the "At Campaign Launch" - which tries to create all cards for users in advance, the "At First Impression" option will generate the cards on the fly, at the moment a user first opens your app (or refreshes cards) and is newly eligible for the message.

This means that together with Scheduled entry, cards will be available immediately, as soon as you need them, at both Session Start, or for a time-based eligibility window.

## 3. Canvas Entry is a pre-requisite for receiving cards

When using Canvas, remember that a user must first enter the canvas based on your configured entry criteria, and __then__ must also flow through your content card message step. Only then will the card be available for your app or website. Remember, there is built in latency for the card to be created once the user passes through the step and may delay when the card is available.

## 4. Don't refresh cards excessively

Content Cards are automatically refreshed by the SDK at each new session start. Your integration is able to manually request a content cards refresh at any time during the active app session.

Calling the `requestContentCardsRefresh` method too frequently may lead to rate limiting. If your app becomes temporarily rate limited, you might not be able to refresh cards when you need to or at a critical time in the user's engagement with your app.

For this reason, ensure you're only calling this refresh method at important times in the user lifecycle, for example, after a user makes a purchase, or after a user upgrades their account.

## 5. Avoid Connected Content

Connected Content helps to enrich Content Cards with 1st party or 3rd party API data. However, when included in a Content Card message, it will block the availability of the card until this network request can be completed. In some cases, this will cause SDKs to retry a few seconds later in an effort to not delay your app's rendering logic which may wait for the SDK to complete its refresh task.

If you must you Connected Content, schedule these cards in advance and use the "At Campaign Launch" option so that cards are pre-created prior to a user's upcoming session.
