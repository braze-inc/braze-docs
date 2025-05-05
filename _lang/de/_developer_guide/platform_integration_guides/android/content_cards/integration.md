---
nav_title: Integration
article_title: Content-Card Integration für Android und FireOS
page_order: 0
platform: 
  - Android
  - FireOS
description: "Dieser referenzierte Artikel behandelt die Content-Card Integration und die verschiedenen Datenmodelle und kartenspezifischen Eigenschaften, die für Ihre Android- oder FireOS-Anwendung zur Verfügung stehen."
channel:
  - content cards
search_rank: 1
---

# Integration von Content Cards

> Dieser referenzierte Artikel behandelt die Content-Card Integration und die verschiedenen Datenmodelle und kartenspezifischen Eigenschaften, die für Ihre Android- oder FireOS-Anwendung zur Verfügung stehen.

{% alert note %}
Ziehen Sie den [Anpassungsleitfaden für Content-Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards) zurate, um mit der Implementierung und Anpassung zu beginnen.
{% endalert %}

In Android ist der Content-Card-Feed als [Fragment](https://developer.android.com/guide/components/fragments.html) implementiert, das im Braze Android UI-Projekt verfügbar ist. Sehen Sie sich die [ von Google](https://developer.android.com/guide/fragments#Adding "Android-Dokumentation: Fragments") für Informationen zum Hinzufügen eines Fragments zu einer Aktivitäten an.

Die Klasse [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) wird automatisch aktualisiert, zeigt den Inhalt der Content-Cards an und protokolliert die Nutzungs-Analytics. Die Karten, die im `ContentCards` eines Nutzers erscheinen können, werden auf dem Braze-Dashboard erstellt.

## Datenmodell der Inhaltskarte {#card-types-for-android}

Das Content-Cards-Datenmodell ist im Android SDK verfügbar. Eine vollständige Referenz des Content-Card-Datenmodells finden Sie in der [Dokumentation zum SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

Braze verfügt über vier eindeutige Content-Cards-Kartentypen, die sich ein Basismodell teilen: [nur Bild](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html), [Bild mit Untertitel](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html), [klassisch (Textankündigung)](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) und [klassisch (Kurznachrichten)](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html). Jeder Typ erbt gemeinsame Eigenschaften von einem Basismodell und hat die folgenden zusätzlichen Eigenschaften.

Informationen zum Abonnieren von Kartendaten finden Sie unter [Logging-Analysen]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics).

### Eigenschaften des Basis-Content-Card-Modells {#base-card-for-android}

Das [Basiskartenmodell](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) bietet grundlegende Verhaltensweisen für alle Karten.  

|Eigenschaft | Beschreibung |
|---|---|
|`getId()` | Gibt die von Braze eingestellte ID der Karte zurück.|
|`getViewed()` | Gibt einen booleschen Wert zurück, der angibt, ob die Karte vom Nutzer:in gelesen oder ungelesen ist.|
|`getExtras()` | Gibt eine Karte mit Schlüssel-Wert-Extras für diese Karte zurück.|
|`getCreated()`  | Gibt den Unix-Zeitstempel der Erstellungszeit der Karte aus Braze zurück.|
|`getIsPinned` | Gibt einen booleschen Wert zurück, der angibt, ob die Karte gepinnt ist.|
|`getOpenUriInWebView()`  | Gibt einen booleschen Wert zurück, der angibt, ob die URI für diese Karte geöffnet werden soll. <br> in Braze WebView oder nicht.|
|`getExpiredAt()` | Ruft das Verfallsdatum der Karte ab.|
|`getIsRemoved()` | Gibt einen booleschen Wert zurück, der angibt, ob der Endnutzer:in diese Karte gekündigt hat.|
|`getIsDismissible()`  | Gibt einen booleschen Wert zurück, der angibt, ob die Karte gepinnt ist.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Eigenschaften der Bildkarte "Nur Bild"{#banner-image-card-for-android}

[Nur-Bild-Karten](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) sind anklickbare Bilder in voller Größe.

|Eigenschaft | Beschreibung |
|---|---|
|`getImageUrl()` | Gibt die URL des Bildes der Karte zurück.|
|`getUrl()` | Gibt die URL zurück, die geöffnet wird, nachdem die Karte angeklickt wurde. Kann eine HTTP(s)-URL oder eine Protokoll-URL sein.|
|`getDomain()` | Gibt den Linktext für die URL der Eigenschaft zurück.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Eigenschaften der Bildkarte mit Beschriftung {#captioned-image-card-for-android}

[Bildunterschriftenkarten](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) sind anklickbare Bilder in voller Größe mit begleitendem beschreibendem Text.

|Eigenschaft | Beschreibung |
|---|---|
|`getImageUrl()` | Gibt die URL des Bildes der Karte zurück.|
|`getTitle()` | Gibt den Titeltext für die Karte zurück.|
|`getDescription()` | Gibt den Text für die Karte zurück.|
|`getUrl()` | Gibt die URL zurück, die geöffnet wird, nachdem die Karte angeklickt wurde. Kann eine HTTP(s)-URL oder eine Protokoll-URL sein.|
|`getDomain()` | Gibt den Linktext für die URL der Eigenschaft zurück. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Klassische Eigenschaften der Karte {#text-Announcement-card-for-android}

Bei einer klassischen Karte ohne Bild handelt es sich um eine [Textankündigungskarte](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Wenn ein Bild enthalten ist, erhalten Sie eine [kurze Benachrichtigung](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

|Eigenschaft | Beschreibung |
|---|---|
|`getTitle()` | Gibt den Titeltext für die Karte zurück. |
|`getDescription()` | Gibt den Text für die Karte zurück. |
|`getUrl()` | Gibt die URL zurück, die geöffnet wird, nachdem die Karte angeklickt wurde. Kann eine HTTP(s)-URL oder eine Protokoll-URL sein. | 
|`getDomain()` | Gibt den Linktext für die URL der Eigenschaft zurück. |
|`getImageUrl()` | Gibt die URL des Bildes der Karte zurück, gilt nur für die klassische Kurznachrichtenkarte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Karten-Methoden

Alle [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) Datenmodellobjekte bieten die folgenden Analytics-Methoden für die Protokollierung von Nutzer:innen-Ereignissen auf Braze Servern.

|Methode | Beschreibung |
|---|---|
|`logImpression()` | Protokollieren Sie manuell einen Abdruck in Braze für eine bestimmte Karte. |
|`logClick()` | Protokollieren Sie manuell einen Klick auf Braze für eine bestimmte Karte. |
|`setIsDismissed()` | Protokollieren Sie manuell eine Kündigung in Braze für eine bestimmte Karte. Wenn eine Karte bereits als abgelehnt markiert ist, kann sie nicht erneut als abgelehnt markiert werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

