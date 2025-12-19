## Voraussetzungen

Bevor Sie Braze Content-Cards verwenden können, müssen Sie das [Braze Android SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) in Ihre App integrieren. Es ist jedoch keine zusätzliche Einrichtung erforderlich.

## Google-Fragmente

In Android ist der Content-Card-Feed als [Fragment](https://developer.android.com/guide/components/fragments.html) implementiert, das im Braze Android UI-Projekt verfügbar ist. Die Klasse [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) wird automatisch aktualisiert, zeigt den Inhalt der Content-Cards an und protokolliert die Nutzungs-Analytics. Die Karten, die im `ContentCards` eines Nutzers erscheinen können, werden auf dem Braze-Dashboard erstellt.

Wie Sie ein Fragment zu einer Aktivität hinzufügen können, erfahren Sie in [der Dokumentation zu Fragmenten von Google](https://developer.android.com/guide/fragments#Adding).

## Kartentypen und Eigenschaften

Das Content-Cards-Datenmodell ist im Android SDK verfügbar und bietet die folgenden eindeutigen Content-Card-Typen. Jeder Typ hat ein gemeinsames Basismodell, das es ihnen erlaubt, gemeinsame Eigenschaften vom Basismodell zu erben und darüber hinaus ihre eigenen eindeutigen Eigenschaften zu haben. Die vollständige referenzierte Dokumentation finden Sie unter [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

### Basis-Kartenmodell {#base-card-for-android}

Das [Basiskartenmodell](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) bietet grundlegende Verhaltensweisen für alle Karten.  

|Eigenschaft | Beschreibung |
|---|---|
|`getId()` | Gibt die von Braze eingestellte ID der Karte zurück.|
|`getViewed()` | Gibt einen booleschen Wert zurück, der angibt, ob die Karte vom Nutzer:in gelesen oder ungelesen ist.|
|`getExtras()` | Gibt eine Karte mit Schlüssel-Wert-Extras für diese Karte zurück.|
|`getCreated()`  | Gibt den Unix-Zeitstempel der Erstellungszeit der Karte aus Braze zurück.|
|`isPinned` | Gibt einen booleschen Wert zurück, der angibt, ob die Karte gepinnt ist.|
|`getOpenUriInWebView()`  | Gibt einen booleschen Wert zurück, der angibt, ob die URI für diese Karte geöffnet werden soll. <br> in Braze WebView oder nicht.|
|`getExpiredAt()` | Ruft das Verfallsdatum der Karte ab.|
|`isRemoved()` | Gibt einen booleschen Wert zurück, der angibt, ob der Endnutzer:in diese Karte gekündigt hat.|
|`isDismissibleByUser()`  | Gibt einen booleschen Wert zurück, der angibt, ob die Karte vom Nutzer:in entlassen werden kann.|
|`isClicked()` | Gibt einen booleschen Wert zurück, der den angeklickten Zustand dieser Karte wiedergibt.|
|`isDismissed()` | Gibt einen booleschen Wert zurück, wenn diese Karte abgewiesen wurde.|
|`isControl()` | Gibt einen booleschen Wert zurück, wenn diese Karte eine Kontrollkarte ist und nicht gerendert werden soll.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Nur Bild {#banner-image-card-for-android}

[Nur Bildkarten](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) sind anklickbare Bilder in voller Größe.

|Eigenschaft | Beschreibung |
|---|---|
|`getImageUrl()` | Gibt die URL des Bildes der Karte zurück.|
|`getUrl()` | Gibt die URL zurück, die geöffnet wird, nachdem die Karte angeklickt wurde. Kann eine HTTP(s)-URL oder eine Protokoll-URL sein.|
|`getDomain()` | Gibt den Linktext für die URL der Eigenschaft zurück.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Bildunterschrift {#captioned-image-card-for-android}

[Bildunterschriftenkarten](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) sind anklickbare Bilder in voller Größe mit begleitendem beschreibendem Text.

|Eigenschaft | Beschreibung |
|---|---|
|`getImageUrl()` | Gibt die URL des Bildes der Karte zurück.|
|`getTitle()` | Gibt den Titeltext für die Karte zurück.|
|`getDescription()` | Gibt den Text für die Karte zurück.|
|`getUrl()` | Gibt die URL zurück, die geöffnet wird, nachdem die Karte angeklickt wurde. Kann eine HTTP(s)-URL oder eine Protokoll-URL sein.|
|`getDomain()` | Gibt den Linktext für die URL der Eigenschaft zurück. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Klassisch {#text-Announcement-card-for-android}

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
|`isDismissed` | Setzen Sie diese Eigenschaft auf `true`, um eine Karte als abgelehnt zu markieren. Wenn eine Karte bereits als abgelehnt markiert ist, kann sie nicht erneut als abgelehnt markiert werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
