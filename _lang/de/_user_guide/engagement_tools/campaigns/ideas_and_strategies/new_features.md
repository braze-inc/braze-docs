---
nav_title: Bekanntheit von Funktionen und neue App-Version
article_title: Feature Awareness und neue App-Version
page_order: 9
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie Ihre Nutzer:innen auf dem Laufenden halten, wenn Sie neue Funktionen oder Versionen veröffentlichen."
tool: Campaigns

---

# Bekanntheit von Funktionen und neue App-Version

> In diesem Referenzartikel erfahren Sie, wie Sie die Braze-Plattform nutzen können, um Ihre Kunden über neue Funktionen und Versionen Ihrer App auf dem Laufenden zu halten. 

Sie arbeiten hart daran, Ihre App ständig zu aktualisieren und zu verbessern, und Sie möchten, dass Ihre Benutzer diese aufregenden neuen Funktionen und neuen App-Versionen erleben können. Lernen Sie, wie Sie Ihren Benutzern die neuen Funktionen, die sie noch nicht kennen, näher bringen können, und ermutigen Sie sie, die App zu erkunden, um das Beste aus Ihrem Angebot herauszuholen.

Kampagnen zum Feature-Bewusstsein sind eine großartige Möglichkeit, um Nutzer:innen zu ermutigen, mit Ihrer App in Kontakt zu bleiben, während Sie die Funktionalität Ihrer App weiter verbessern.  Wenn Sie Ihre Nutzer auf dem Laufenden halten, können Sie sie aktiv halten, die Bewertungen steigern und das Engagement der Nutzer sicherstellen.

## Filtern nach den neuesten App-Versionen

Braze SDKs verfolgen automatisch die letzte App-Version eines Benutzers. Diese Versionen können in Filtern und Segmenten verwendet werden, um zu bestimmen, welche Benutzer eine Nachricht oder Kampagne erhalten sollen.

\![Das Panel Targeting-Optionen im Schritt Nutzer:innen anvisieren im Workflow zur Erstellung der Kampagne. Der Abschnitt Zusätzliche Filter enthält den folgenden Filter "Neueste App-Versionsnummer für Android Stopwatch (Android) liegt unter 3.7.0 (134.0.0.0)".]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

{% alert note %}
Es kann einige Zeit dauern, bis die aktuellen Versionen der Apps angezeigt werden. Die App-Version im Nutzerprofil wird aktualisiert, wenn die Informationen vom SDK erfasst werden, das sich darauf verlässt, wann Nutzer:innen ihre Apps öffnen. Wenn der Nutzer:innen die App nicht öffnet, wird die aktuelle Version nicht aktualisiert. <br><br> Diese Filter können auch nicht rückwirkend angewendet werden. Es ist gut, "größer als" oder "gleich" für aktuelle und zukünftige Versionen zu verwenden, aber die Verwendung von Filtern für frühere Versionen kann zu unerwartetem Verhalten führen.
{% endalert %}

### Versionsnummer der App

Verwenden Sie den Filter **App-Versionsnummer**, um Benutzer nach der Versions- und Build-Nummer der App zu segmentieren. 

Dieser Filter unterstützt numerische Vergleiche, um eine Reihe von App-Versionen zu erfassen. So können Sie zum Beispiel Nutzer ansprechen, deren App-Version "unter", "über" und "gleich" der App-Version "1.2.3" ist. Das könnte nützlich sein, um eine neue Funktion zu bewerben, die ein App-Upgrade erfordert.

Dieser neue Filter kann den alten Filter "Name der App-Version" ersetzen, der eine explizite Auflistung jeder älteren Version oder die Verwendung eines regulären Ausdrucks erfordern würde.

**Funktionsweise**

* Jeder Teil der `major.minor.patch`-Version, der in der App-Version Ihrer App gesendet wird, wird als Ganzzahl verglichen
* Wenn die Hauptzahlen gleich sind, werden die Nebenzahlen verglichen, usw.

**Wichtig**

* Android Apps haben sowohl eine von Menschen lesbare [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) als auch eine interne [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()). Der Filter für die App-Versionsnummer verwendet `versionCode`, da diese garantiert bei jeder Veröffentlichung im App Store erhöht wird.
* Dies kann zu Verwirrung führen, wenn `versionName` und `versionCode` nicht mehr synchronisiert sind, insbesondere da beide Felder im Braze-Dashboard angezeigt werden können. Überprüfen Sie am besten, ob `versionName` und `versionCode` Ihrer App gemeinsam inkrementiert werden.
* Wenn Sie stattdessen nach dem für Menschen lesbaren Feld `versionName` filtern müssen (was selten vorkommt), verwenden Sie den Filter App Version Name.

#### SDK-Anforderungen

Werte für diesen Filter werden ab Braze Android SDK v3.6.0+ und iOS SDK v3.21.0+ erfasst. Auch wenn dieser Filter SDK-Voraussetzungen hat, können Sie mit dieser Funktion auch Nutzer:innen ansprechen, die eine niedrigere (ältere) Version Ihrer App verwenden!

Bei Android basiert diese Versionsnummer auf dem [Package Long Version Code](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) für die App.

Bei iOS basiert diese Versionsnummer auf dem [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) für die App.

{% alert tip %}
Dieser Filter füllt Werte auf, nachdem Nutzer:innen ihre Apps auf die unterstützten Braze-SDK-Versionen aktualisiert haben. Bis dahin zeigt der Filter bei Auswahl keine Versionen an.
{% endalert %}

#### Anwendungsfall

Im folgenden Szenario nehmen wir an, dass Sie zuerst auf die Braze-SDKs aktualisiert haben, die diesen Filter in der Version `2.0.0` Ihrer App unterstützen.

Sobald Braze die Daten von Version 2.0.0 Ihrer App erhält, können Sie Benutzer mit früheren oder späteren Versionen ansprechen.

| Filter  | Version der Benutzer-App  | Ergebnis |
:------------- | :----------- | :---------|
| Weniger als 2.0.0 | 1.0.0 | Der oder die Nutzer:in befindet sich in dem Segment, obwohl sein oder ihr Braze-SDK den Filter „App-Versionsnummer“ nicht unterstützte. |
| Größer als 2.0.0 | 2.5.1 | Der Benutzer und alle zukünftigen Installationen werden in dem Segment enthalten sein. |
| Größer als 2.0.0 | 1.9.9 | Der Benutzer befindet sich nicht in dem Segment. |
| Kleiner als oder gleich 2.0.0 | 3.0.1 | Der Benutzer befindet sich nicht in dem Segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### App-Versionsname

Verwenden Sie den Filter „App-Versionsname“, um Nutzer:innen nach dem „Build-Namen“ der App zu segmentieren, der für die Nutzer:innen sichtbar ist. 

Dieser Filter unterstützt den Abgleich mit "ist", "ist nicht" und regulären Ausdrücken. Sie können zum Beispiel Nutzer:innen ansprechen, die eine App haben, die nicht die Version „1.2.3-test-build“ hat.

Bei Android basiert dieser Versionsname auf dem [Paketversionsnamen](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) für die App. Bei iOS basiert dieser Versionsname auf dem [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) für die App.

### Habe die Funktion nicht verwendet

Wenn Sie eine neue App-Version herausgeben und neue Funktionen einführen, bemerken die Benutzer die neuen Inhalte möglicherweise nicht. Eine Kampagne zur Sensibilisierung für neue Funktionen ist eine gute Möglichkeit, Benutzern neue oder noch nie genutzte Funktionen vorzustellen. Dazu müssen Sie ein [angepasstes Attribut]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data) erstellen, das Nutzern:innen zugewiesen wird, die eine bestimmte Aktion innerhalb Ihrer App nie abgeschlossen haben, oder ein [angepasstes Event]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data) verwenden, um eine bestimmte Aktion zu tracken. Sie können dieses Attribut (oder Event) verwenden, um die Nutzer:innen zu segmentieren, an die Sie die Kampagne senden möchten.

{% alert tip %}
Möchten Sie einen bestimmten Teil Ihrer Zielgruppe erneut ansprechen? Sehen Sie sich [Retargeting-Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/) an, um zu erfahren, wie Sie Kampagnen neu ausrichten können, indem Sie die früheren Aktionen Ihrer Nutzer nutzen.
{% endalert %}


