---
nav_title: Manuelles Verarbeiten von Klicks
article_title: Manuelle Handhabung von News-Feed-Klicks für Android und FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Dieser Referenzartikel beschreibt, wie Sie Klicks auf News Feeds in Ihrer Android- oder FireOS-Anwendung manuell verarbeiten können."
channel:
  - news feed
  
---

# Manuelles Verarbeiten von Klicks

> Dieser Referenzartikel beschreibt, wie Sie Klicks auf News Feeds in Ihrer Android- oder FireOS-Anwendung manuell verarbeiten können.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Sie können Klicks auf Newsfeeds manuell verarbeiten, indem Sie einen angepassten Klick-Listener für Newsfeeds einrichten. Dadurch werden Anwendungsfälle wie die selektive Verwendung des nativen Webbrowsers zum Öffnen von Weblinks ermöglicht.

## Schritt 1: Klick-Listener für Newsfeeds implementieren

Erstellen Sie eine Klasse, die [`IFeedClickActionListener`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/feed/listeners/IFeedClickActionListener.java) implementiert. Implementieren Sie die Methode `onFeedCardClicked()`, die aufgerufen wird, wenn auf eine Newsfeed-Card geklickt wird.

## Schritt 2: Weisen Sie Braze an, Ihren News Feed-Klickzuhörer zu verwenden

Nach dem Erstellen von `IFeedClickActionListener` rufen Sie `BrazeFeedManager.getInstance().setFeedCardClickActionListener()` auf, um `BrazeFeedManager` anzuweisen, den angepassten `IFeedClickActionListener` zu verwenden.

