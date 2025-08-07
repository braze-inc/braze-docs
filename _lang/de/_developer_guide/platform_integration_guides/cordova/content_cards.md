---
nav_title: Content-Cards
article_title: Integration von Content Cards
page_order: 2
---

# Integration von Content Cards

> Erfahren Sie, wie Sie Content-Cards für das Cordova Braze SDK integrieren.

{% multi_lang_include cordova/prerequisites.md %}

## Kartenzuführungen

Das Braze SDK enthält eine Standard-Kartenzuführung. Sie können den Standard-Kartenfeed mit der Methode `launchContentCards()` anzeigen. Diese Methode verarbeitet das gesamte Analytics-Tracking, Ausblendungen und die Darstellung der Content-Cards eines Nutzers.

## Content-Cards

Mit diesen zusätzlichen Methoden können Sie einen angepassten Content-Card-Feed in Ihrer App erstellen:

|Methode | Beschreibung |
|---|---|
|`requestContentCardsRefresh()`|Sendet eine Anfrage im Hintergrund, um die neuesten Content-Cards vom Braze SDK-Server anzufordern.|
|`getContentCardsFromServer(successCallback, errorCallback)`|Ruft Inhaltskarten aus dem Braze SDK ab. Diese Funktion fragt die neuesten Content-Cards vom Server ab und gibt abschließend die Liste der Karten zurück.|
|`getContentCardsFromCache(successCallback, errorCallback)`|Ruft Inhaltskarten aus dem Braze SDK ab. Dies gibt die neueste Liste der Karten aus dem lokalen Cache zurück, die bei der letzten Aktualisierung aktualisiert wurde.|
|`logContentCardClicked(cardId)`|Protokolliert einen Klick für die angegebene Content Card ID.|
|`logContentCardImpression(cardId)`|Protokolliert einen Abdruck für die angegebene Content Card ID.|
|`logContentCardDismissed(cardId)`|Protokolliert eine Ausblendung für die angegebene Content-Card-ID.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## GIF-Unterstützung

{% multi_lang_include wrappers/gif_support/content_cards.md %}
