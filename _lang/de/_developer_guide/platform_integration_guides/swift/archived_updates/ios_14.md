---
nav_title: Upgrade-Leitfaden für iOS 14
article_title: Upgrade-Leitfaden für das iOS 14-SDK
page_order: 7
platform: iOS
description: "Dieser Referenzartikel beschreibt das iOS 14-SDK-Update und hebt Änderungen wie Geofences, Standort-Targeting, IDFA und mehr hervor."
hidden: true
noindex: true
---

# Upgrade-Leitfaden für das iOS 14-SDK

> Dieser Leitfaden beschreibt die für Braze relevanten Änderungen in iOS 14 sowie die erforderlichen Upgrade-Schritte für Ihre Braze iOS-SDK-Integration. Eine vollständige Liste der neuen iOS 14 Updates finden Sie auf Apples [iOS 14 Seite](https://www.apple.com/ios/ios-14/).

{% alert tip %}
Ab iOS 14.5 muss für die **IDFA-Erfassung** und für [bestimmte Datenfreigaben](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track) eine Berechtigung über den [ATT-Prompt (AppTrackingTransparency)](https://developer.apple.com/documentation/apptrackingtransparency) eingeholt werden. [(Mehr erfahren](#idfa))
{% endalert %}

#### Zusammenfassung der wichtigsten Änderungen von iOS 14

- Apps für iOS 14 / Xcode 12 müssen unser [offizielles iOS 14-Release](https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.27.0) verwenden.
- Für Nutzer, die die neue Berechtigung _Ungefährer Standort_ auswählen, werden Geofences [nicht mehr von iOS unterstützt](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization).
- Die Verwendung der Targeting-Features "Letzter bekannter Standort" erfordert ein Upgrade auf Braze iOS SDK v3.26.1+, um Kompatibilität mit der Berechtigung _Ungefährer Standort_ herzustellen. Wenn Sie Xcode 12 verwenden, müssen Sie ein Upgrade auf mindestens v3.27.0 durchführen.
- Ab iOS 14.5 muss für die IDFA-Erfassung und für [bestimmte Datenfreigaben](https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track) eine Berechtigung über den [ATT-Prompt (AppTrackingTransparency)](https://developer.apple.com/documentation/apptrackingtransparency) eingeholt werden.
- Wenn Sie das Feld "Ad-Tracking aktiviert" für das Kampagnen-Targeting oder für Analytics verwenden, müssen Sie auf Xcode 12 upgraden und das neue AppTrackingTransparency-Framework verwenden, um den Opt-in-Status der Nutzer zu melden.

## Upgrade Zusammenfassung

<style>
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    min-width:230px;
}
table td {
    word-break: break-word;
}
</style>

|Wenn Ihre App Folgendes verwendet:|Upgrade-Empfehlung|Beschreibung|
|------|--------|---|
|Xcode 12|**Upgrade auf iOS SDK v3.27 oder höher**|Kunden, die Xcode 12 verwenden, müssen aus Kompatibilitätsgründen v3.27.0+ verwenden. Wenn Sie Probleme oder Fragen im Zusammenhang mit unserer iOS 14-Kompatibilität haben, öffnen Sie einen neuen [GitHub-Problemfall](https://github.com/Appboy/appboy-ios-sdk/issues).|
|Letzter Standort| **Upgrade auf iOS SDK v3.26.1 oder höher**|Wenn Sie das Targeting-Feature "Letzter Standort" verwenden und noch Xcode 11 einsetzen, sollten Sie mindestens auf iOS SDK v3.26.1 upgraden, das das neue Feature _Ungefährer Standort_ unterstützt. Ältere SDKs sind nicht in der Lage, den Standort zuverlässig zu erfassen, wenn ein Nutzer ein Upgrade auf iOS 14 durchführt _und_ "Ungefährer Standort" auswählt.<br><br>Auch wenn Ihre App nicht auf iOS 14 abzielt, könnten Ihre Nutzer ein Upgrade auf iOS 14 durchführen und die neue Option für die Standortgenauigkeit nutzen. Apps, die nicht auf iOS SDK v3.26.1+ aktualisiert werden, sind nicht in der Lage, Standortattribute zuverlässig zu erfassen, wenn Nutzer ihren _ungefähren Standort_ auf iOS 14-Geräten angeben.|
|IDFA Anzeigenverfolgungs-ID| **Upgrade auf Xcode 12 und iOS SDK v3.27 kann erforderlich sein**|2021 hat Apple damit begonnen, einen Prompt zur Einholung einer Berechtigung für die IDFA-Erfassung zu verlangen. Das bedeutet, dass Apps auf Xcode 12 aktualisiert werden und das neue `AppTrackingTransparency` Framework verwenden müssen, um weiterhin IDFA erfassen zu können. Für die Übermittlung von IDFA an das Braze SDK ist dann ebenfalls ein Upgrade auf v3.27.0+ erforderlich.<br><br>Apps, die die neuen iOS 14-APIs nicht verwenden, können keine IDFA erfassen. Sie erfassen stattdessen eine leere ID (`00000000-0000-0000-0000-000000000000`), nachdem Apple die Änderung 2021 durchgesetzt hat. Weitere Informationen darüber, ob dies auf Ihre App zutrifft oder nicht, finden Sie unter [IDFA-Details](#idfa).|


## iOS 14 Verhaltensänderungen

### Berechtigung zur Abfrage des ungefähren Standorts

![Genauer Standort]({% image_buster /assets/img/ios/ios14-approximate-location.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

#### Übersicht

Wenn eine Berechtigung zur Standortermittlung angefordert wird, können Nutzer nun wählen, ob sie (wie bisher) ihren _genauen Standort_ oder ob sie den _ungefähren Standort_ angeben möchten. Ungefähre Position gibt einen größeren Radius zurück, in dem sich der Benutzer befindet, anstelle seiner genauen Koordinaten.

#### Geofences {#geofences}

Für Nutzer, die die neue Berechtigung _Ungefährer Standort_ auswählen, werden Geofences [nicht mehr von iOS unterstützt](https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization). Für Ihre Braze SDK-Integration sind zwar keine Updates erforderlich, aber Sie müssen möglicherweise Ihre [standortbasierte Marketingstrategie](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/) für Kampagnen anpassen, die auf Geofences basieren.

#### Standort-Targeting {#location-tracking}

Um weiterhin den _letzten bekannten Standort_ von Nutzern zu erfassen, wenn die Berechtigung für die Ermittlung des _ungefähren Standorts_ erteilt wird, muss Ihre App mindestens auf v3.26.1 des Braze iOS SDK aktualisiert werden. Denken Sie daran, dass die Ortung weniger präzise ist und nach unseren Tests bis zu 12.000 Meter (7+ Meilen) betragen hat. Wenn Sie die Optionen für den _letzten bekannten Standort_ im Braze Dashboard verwenden, sollten Sie den Radius des Standorts vergrößern, um neue _ungefähre Standorte_ zu berücksichtigen (wir empfehlen einen Radius von mindestens 1 Meile/1,6 km).

Apps, die das Braze iOS SDK nicht mindestens auf v3.26.1 aktualisieren, können das Standort-Tracking nicht mehr nutzen, wenn auf iOS 14-Geräten die Berechtigung für die Ermittlung des _ungefähren Standorts_ erteilt wird.

Benutzer, die bereits Zugriff auf ihren Standort gewährt haben, können auch nach dem Upgrade weiterhin _ihren genauen Standort_ angeben.

Wenn Sie Xcode 12 verwenden, müssen Sie ein Upgrade auf mindestens v3.27.0 durchführen.

Weitere Informationen zu Approximate Location finden Sie in Apples WWDC-Video [What's New In Location](https://developer.apple.com/videos/play/wwdc2020/10660/).

### IDFA und App Tracking Transparency {#idfa}

#### Übersicht

IDFA (Identifier for Advertisers) ist ein von Apple bereitgestellter Identifikator zur Verwendung mit Werbe- und Attributionspartnern für geräteübergreifendes Tracking und ist an die Apple ID einer Person gebunden.

Ab iOS 14.5 muss ein neuer Prompt (eingeführt vom neuen `AppTrackingTransparency` Framework) angezeigt werden, um die ausdrückliche Zustimmung des Nutzers für IDFA einzuholen. Dieser Prompt, der um die Erlaubnis bittet, "Sie über Apps und Websites anderer Unternehmen zu verfolgen", ist vergleichbar mit dem Prompt zur Standortermittlung.

Wenn ein Nutzer dem Prompt nicht zustimmt oder wenn Sie nicht auf das `AppTrackingTransparency` Framework von Xcode 12 aktualisieren, wird ein leerer IDFA-Wert (`00000000-0000-0000-0000-000000000000`) zurückgegeben und Ihre App darf den Nutzer nicht erneut auffordern.

{% alert important %}
Diese IDFA-Updates werden wirksam, nachdem die Endnutzer ihre Geräte auf iOS 14.5 aktualisiert haben. Stellen Sie sicher, dass Ihre App das neue `AppTransparencyFramework` mit Xcode 12 verwendet, wenn Sie IDFA erfassen möchten.
{% endalert %}

#### Änderungen an der Braze IDFA Kollektion
![IDFA]({% image_buster /assets/img/ios/ios14-idfa.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

1. Braze wird es Apps weiterhin ermöglichen, den IDFA-Wert eines Nutzers _an_ das Braze SDK zu übermitteln.

2. Das Kompilierungsmakro `ABK_ENABLE_IDFA_COLLECTION`, das eine optionale automatische IDFA-Erfassung bedingt kompilieren würde, funktioniert unter iOS 14 nicht mehr und wurde in 3.27.0 entfernt. 

3. Wenn Sie das Feld "Ad-Tracking aktiviert" für das Kampagnen-Targeting oder für Analysen verwenden, müssen Sie auf Xcode 12 upgraden und das neue AppTrackingTransparency-Framework verwenden, um den Opt-in-Status der Nutzer zu melden. Der Grund für diese Änderung ist, dass in iOS 14 das alte Feld [`advertisingTrackingEnabled`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-advertisingtrackingenabled) immer "Nein" zurückgibt.

4. Wenn Ihre Anwendung IDFA oder IDFV als externe Braze-ID verwendet hat, empfehlen wir Ihnen dringend, diese Bezeichner zugunsten einer UUID aufzugeben. Weitere Informationen zur Migration externer IDs finden Sie unter [API-Endpunkte für die externe ID-Migration]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

Lesen Sie mehr über Apples [Datenschutz-Updates](https://developer.apple.com/app-store/user-privacy-and-data-use/) und das neue [App-Tracking-Transparenz-Framework](https://developer.apple.com/documentation/apptrackingtransparency).

### Push-Autorisierung {#push-provisional-auth}

{% alert important %}
In iOS 14 sind keine Änderungen an der vorläufigen Push-Autorisierung enthalten. In einer früheren Beta-Version von iOS 14 führte Apple eine Änderung ein, die inzwischen wieder rückgängig gemacht wurde.
{% endalert %}

## iOS 14 neue Funktionen

### App Datenschutz und Datenerfassung im Überblick {#app-privacy}

Seit dem 8\. Dezember 2020 sind für alle Einreichungen im App Store zusätzliche Schritte erforderlich, um die [neuen App-Datenschutzstandards von Apple](https://developer.apple.com/app-store/app-privacy-details/) einzuhalten.

#### Fragebogen zum Apple Entwicklerportal

Auf dem _Apple Developer Portal_:
* Sie werden gebeten, einen Fragebogen auszufüllen, in dem Sie beschreiben, wie Ihre App oder Drittpartner Daten erfassen.
  * Es wird erwartet, dass der Fragebogen immer auf dem neuesten Stand Ihrer letzten Veröffentlichung im App Store ist.
  * Der Fragebogen kann auch ohne Einreichung einer neuen App aktualisiert werden.
* Sie müssen einen Link zur URL der Datenschutzrichtlinie Ihrer App einfügen.

Wenden Sie sich beim Ausfüllen Ihres Fragebogens an Ihr Rechtsteam und überlegen Sie, wie sich die Verwendung von Braze für die folgenden Felder auf Ihre Offenlegungspflichten auswirken könnte.

#### Braze Standard-Datenerfassung
**Bezeichner**: Eine anonyme Gerätekennung wird immer vom Braze SDK erfasst. Diese ist derzeit auf die Geräte-IDFV (Kennung für den Hersteller) eingestellt.

**Nutzungsdaten**: Hierzu können Sitzungsdaten von Braze sowie alle erfassten Events oder Attribute gehören, die Sie zur Messung der Produktinteraktion verwenden.

#### Optionale Datenerfassung
Daten, die Sie möglicherweise durch Ihre Nutzung von Braze sammeln:

**Standort**: Das Braze SDK kann optional sowohl den ungefähren Standort als auch den genauen Standort erfassen. Diese Funktion ist standardmäßig deaktiviert.

**Kontaktinformationen** \- Dies kann Ereignisse und Attribute im Zusammenhang mit der Identität des Benutzers enthalten.

**Käufe**: Hierzu können Events und Käufe gehören, die im Namen des Nutzers protokolliert wurden.

{% alert important %}
Beachten Sie, dass diese Liste nicht vollständig ist. Wenn Sie in Braze manuell weitere Informationen über Ihre Nutzer erfassen, die auf andere Kategorien im App-Datenschutzfragebogen zutreffen, müssen Sie diese ebenfalls offenlegen.
{% endalert %}

Um mehr über diese Funktion zu erfahren, lesen Sie bitte [Apples Datenschutz und Datennutzung](https://developer.apple.com/app-store/user-privacy-and-data-use/).

