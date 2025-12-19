---
nav_title: Localization
article_title: Localization for Braze Swift SDK
page_order: 3.50
description: "Learn about localization for the Braze SDK."
platform:
  - Android
  - FireOS
  - Swift
---

# Localization

> Learn about localization and supported languages for the Braze SDK, so you can connect with your users across the globe.

## About localization

In addition to English, Braze supports several languages for our built-in SDK messages displayed in your app.

"Built-in SDK messages" refers to any message that comes out-of-the-box on any platform, such as the default Content Cards UI, default in-app message UI, and other SDK-provided interfaces. For example, if you have an empty Content Cards screen, the placeholder text will automatically translate to the user's chosen language.

When a user's phone language is set to one of the supported languages, built-in SDK messages will be translated to that language. For example, if your app displays a message for connectivity issues, it will be translated to their chosen language.

{% multi_lang_include supported_language_codes.md %}
