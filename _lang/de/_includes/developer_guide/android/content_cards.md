## Voraussetzungen

Bevor Sie Braze Content-Cards verwenden können, müssen Sie das [Braze Android SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) in Ihre App integrieren. Es ist jedoch keine zusätzliche Einrichtung erforderlich.

## Google-Fragmente

In Android ist der Content-Card-Feed als [Fragment](https://developer.android.com/guide/components/fragments.html) implementiert, das im Braze Android UI-Projekt verfügbar ist. Die Klasse [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) wird automatisch aktualisiert, zeigt den Inhalt der Content-Cards an und protokolliert die Nutzungs-Analytics. Die Karten, die im Dashboard eines Nutzers angezeigt werden`ContentCards` können, werden im Braze-Dashboard erstellt.

Informationen zum Hinzufügen eines Fragments zu einer Aktivität finden Sie in [der Dokumentation zu Fragmenten von Google](https://developer.android.com/guide/fragments#Adding).

## Kartentypen und Eigenschaften

Das Datenmodell für Content-Cards ist im Android SDK verfügbar und bietet die folgenden eindeutigen Content-Card-Typen. Jeder Typ verfügt über ein Basismodell, wodurch sie neben ihren eigenen eindeutigen Eigenschaften auch gemeinsame Eigenschaften vom Basismodell übernehmen können. Die vollständige Dokumentation finden Sie unter[`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) .

### Basiskartenmodell {#base-card-for-android}

Das [Basiskartenmodell](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) bietet grundlegende Verhaltensweisen für alle Karten.  

|Eigenschaft | Beschreibung |
|---|---|
|`getId()` | Gibt die von Braze eingestellte ID der Karte zurück.|
|`getViewed()` | Gibt einen booleschen Wert zurück, der angibt, ob die Karte vom Nutzer:in gelesen oder ungelesen ist.|
|`getExtras()` | Gibt eine Karte mit Schlüssel-Wert-Extras für diese Karte zurück.|
|`getCreated()`  | Gibt den Unix-Zeitstempel des Erstellungszeitpunkts der Karte aus Braze zurück.|
|`isPinned` | Gibt einen booleschen Wert zurück, der angibt, ob die Karte angeheftet ist.|
|`getOpenUriInWebView()`  | Gibt einen booleschen Wert zurück, der angibt, ob die URIs für diese Karte für die Öffnung vorgesehen sind. <br> in Braze WebView oder nicht.|
|`getExpiredAt()` | Ruft das Ablaufdatum der Karte ab.|
|`isRemoved()` | Gibt einen booleschen Wert zurück, der angibt, ob der Endnutzer:in diese Karte geschlossen hat.|
|`isDismissibleByUser()`  | Gibt einen booleschen Wert zurück, der angibt, ob die Karte von den Nutzer:innen geschlossen werden kann.|
|`isClicked()` | Gibt einen booleschen Wert zurück, der den Status nach einem Klick auf diese Karte widerspiegelt.|
|`isDismissed` | Gibt einen booleschen Wert zurück, der angibt, ob die Karte durch Karten-Ausblendung entfernt wurde. Bitte setzen Sie die Karte auf „Abgehandelt“, um `true`sie als erledigt zu kennzeichnen. Wenn eine Karte bereits als abgelehnt markiert ist, kann sie nicht erneut als abgelehnt markiert werden.|
|`isControl()` | Gibt einen booleschen Wert zurück, wenn diese Karte eine Kontrollkarte ist und nicht gerendert werden sollte.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Nur Bild {#banner-image-card-for-android}

[Karten, die nur aus Bildern](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) bestehen, sind anklickbare Bilder in voller Größe.

|Eigenschaft | Beschreibung |
|---|---|
|`getImageUrl()` | Gibt die URL des Bildes der Karte zurück.|
|`getUrl()` | Gibt die URL zurück, die nach dem Klick auf die Karte zur Öffnung führt. Kann eine HTTP(s)-URL oder eine Protokoll-URL sein.|
|`getDomain()` | Gibt den Linktext für die URL der Eigenschaft zurück.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Bildunterschrift {#captioned-image-card-for-android}

[Bildkarten mit Bildunterschriften](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) sind anklickbare Bilder in voller Größe mit begleitendem Beschreibungstext.

|Eigenschaft | Beschreibung |
|---|---|
|`getImageUrl()` | Gibt die URL des Bildes der Karte zurück.|
|`getTitle()` | Gibt den Titeltext für die Karte zurück.|
|`getDescription()` | Gibt den Text für die Karte zurück.|
|`getUrl()` | Gibt die URL zurück, die nach dem Klick auf die Karte zur Öffnung führt. Kann eine HTTP(s)-URL oder eine Protokoll-URL sein.|
|`getDomain()` | Gibt den Linktext für die URL der Eigenschaft zurück. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Klassisch {#text-Announcement-card-for-android}

Eine klassische Karte ohne Bild wird zu einer [Textankündigungskarte](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Wenn ein Bild enthalten ist, erhalten Sie eine [kurze Nachrichtenkarte](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

|Eigenschaft | Beschreibung |
|---|---|
|`getTitle()` | Gibt den Titeltext für die Karte zurück. |
|`getDescription()` | Gibt den Text für die Karte zurück. |
|`getUrl()` | Gibt die URL zurück, die nach dem Klick auf die Karte zur Öffnung führt. Kann eine HTTP(s)-URL oder eine Protokoll-URL sein. | 
|`getDomain()` | Gibt den Linktext für die URL der Eigenschaft zurück. |
|`getImageUrl()` | Gibt die URL des Kartenbildes zurück, gilt nur für die klassische Short News Card. |
|`isDismissed` | Gibt einen booleschen Wert zurück, der angibt, ob die Karte durch Karten-Ausblendung entfernt wurde. Bitte setzen Sie die Karte auf „Abgehandelt“, um `true`sie als erledigt zu kennzeichnen. Wenn eine Karte bereits als abgelehnt markiert ist, kann sie nicht erneut als abgelehnt markiert werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Karten-Methoden

Alle[`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)Datenmodellobjekte bieten die folgenden Analytics-Methoden für die Protokollierung von Benutzerereignissen auf Braze-Servern.

|Methode | Beschreibung |
|---|---|
|`logImpression()` | Protokollieren Sie manuell einen Abdruck in Braze für eine bestimmte Karte. |
|`logClick()` | Protokollieren Sie manuell einen Klick auf Braze für eine bestimmte Karte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
