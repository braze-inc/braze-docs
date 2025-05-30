---
nav_title: SDK Übersicht
article_title: "SDK Übersicht für Entwickler:in"
description: "Dieser Onboarding-Referenzartikel enthält eine technische Übersicht für Entwickler des Braze SDK. Er behandelt die Standarddaten, die vom SDK getrackt werden, die Sperrung der automatischen Datenerfassung und die aktive SDK-Version Ihrer App."
page_order: 0
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}SDK-Übersicht für Entwickler

> Bevor Sie mit der Integration der Braze SDKs beginnen, werden Sie sich vielleicht fragen, was genau Sie da eigentlich entwickeln und integrieren. Vielleicht sind Sie neugierig, wie Sie das SDK weiter an Ihre Bedürfnisse anpassen können. Dieser Artikel hilft Ihnen, alle Ihre Fragen zum SDK zu beantworten. 

Sind Sie ein Marketer, der einen grundlegenden Überblick über das SDK benötigt? Sehen Sie sich stattdessen unsere [Übersicht für Marketer]({{site.baseurl}}/user_guide/getting_started/web_sdk/) an.

Kurz gesagt, das Braze SDK:
* Sammelt und synchronisiert Benutzerdaten in einem konsolidierten Benutzerprofil
* Sammelt automatisch Sitzungsdaten, Geräteinformationen und Push-Tokens
* Erfasst Marketingdaten und angepasste Daten speziell für Ihr Unternehmen
* Unterstützt Push-Benachrichtigungen, In-App-Nachrichten und Content-Card-Nachrichtenkanäle

## App-Performance

Braze sollte keine negativen Auswirkungen auf die Performance Ihrer App haben.

Die SDKs von Braze haben einen sehr geringen Platzbedarf. Wir ändern die Flush-Rate der Nutzerdaten automatisch in Abhängigkeit von der Qualität des Netzwerks und ermöglichen darüber hinaus eine manuelle Netzwerksteuerung. Wir stapeln API-Anfragen aus dem SDK automatisch, um sicherzustellen, dass die Daten schnell erfasst werden und gleichzeitig die maximale Netzwerkeffizienz erhalten bleibt. Und schließlich ist die Menge der Daten, die bei jedem API-Aufruf vom Client an Braze gesendet wird, äußerst gering.

## SDK-Kompatibilität

Das Braze SDK ist so konzipiert, dass es andere SDKs in Ihrer App nicht beeinträchtigt. Wenn Sie Probleme haben, die Ihrer Meinung nach auf eine Inkompatibilität mit einem anderen SDK zurückzuführen sind, wenden Sie sich an den Braze Support.

## Standard Analytics und Sitzungsbehandlung

Bestimmte Nutzerdaten werden von unserem SDK automatisch erfasst, z. B. die zuerst verwendete App, die zuletzt verwendete App, die Gesamtzahl der Sitzungen, das Betriebssystem des Geräts usw. Wenn Sie unseren Integrationsleitfäden folgen, um unsere SDKs zu implementieren, können Sie die Vorteile dieser [Standard Datenerfassung]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/) nutzen. Wenn Sie diese Liste überprüfen, können Sie vermeiden, die gleichen Informationen über Nutzer mehrfach zu speichern. Mit Ausnahme des Sitzungsbeginns und des Sitzungsendes werden alle anderen automatisch getrackten Daten nicht auf Ihr Datenpunkt-Kontingent angerechnet.

{% alert note %}
Alle unsere Features sind konfigurierbar, aber es empfiehlt sich, das Standardmodell für die Datenerfassung vollständig zu implementieren.

<br>Falls erforderlich können Sie nach Abschluss der Integration [die Erfassung bestimmter Daten beschränken](#blocking-data-collection).
{% endalert %}

## Daten hoch- und herunterladen

Das Braze SDK speichert Daten (Sitzungen, angepasste Events usw.) im Cache und lädt sie in regelmäßigen Abständen hoch. Erst nachdem die Daten hochgeladen wurden, werden die Werte im Dashboard aktualisiert. Das Upload-Intervall berücksichtigt den Zustand des Geräts und richtet sich nach der Qualität der Netzwerkverbindung:

|Qualität der Netzwerkverbindung |    Data-Flush-Intervall|
|---|---|
|Großartig    |10 Sekunden|
|Gut    |30 Sekunden|
|Schlecht    |60 Sekunden|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Wenn keine Netzwerkverbindung besteht, werden die Daten lokal auf dem Gerät zwischengespeichert, bis die Netzwerkverbindung wiederhergestellt ist. Wenn die Verbindung wiederhergestellt ist, werden die Daten auf Braze hochgeladen.

Braze sendet zu Beginn einer Sitzung Daten an das SDK, die darauf basieren, in welche Segmente der Nutzer zum Zeitpunkt der Sitzung fällt. Die neuen In-App-Nachrichten werden während der Sitzung nicht aktualisiert. Allerdings werden die Nutzerdaten während der Sitzung kontinuierlich verarbeitet, wenn sie vom Client gesendet werden. Abgelaufene Nutzer (die die App das letzte Mal vor mehr als 7 Tagen genutzt haben) erhalten zum Beispiel bei ihrer ersten Sitzung in der App immer noch gezielte Inhalte.

## Sperrung der Datenerfassung

Es ist möglich (wird aber nicht empfohlen), die automatische Erfassung bestimmter Daten aus Ihrer SDK-Integration zu blockieren bzw. Prozesse, die dies tun, zuzulassen. 

Die Sperrung der Datenerfassung ist nicht empfehlenswert, da die Entfernung von analytischen Daten die Kapazität Ihrer Plattform für Personalisierung und Targeting verringert. Zum Beispiel:

- Wenn keine vollständige Integration für den Standort auf einem der SDKs vorzunehmen, können Sie Ihre Nachrichten nicht anhand von Sprache oder Standort personalisieren. 
- Wenn Sie die Integration für die Zeitzone nicht wählen, können Sie möglicherweise keine Nachrichten innerhalb der Zeitzone eines Nutzers versenden. 
- Wenn Sie sich dafür entscheiden, keine visuellen Informationen für bestimmte Geräte zu integrieren, wird der Inhalt der Nachrichten möglicherweise nicht für dieses Gerät optimiert.

Wir empfehlen Ihnen dringend, die SDKs vollständig zu integrieren, um dessen Möglichkeiten voll auszuschöpfen.

{% tabs %}
{% tab Internet SDK %}

Sie können entweder bestimmte Teile des SDK einfach nicht integrieren oder verwenden [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) für spezifische Nutzer. Diese Methode synchronisiert die Daten, die vor dem Aufruf von `disableSDK()` aufgezeichnet wurden, und führt dazu, dass alle nachfolgenden Aufrufe des Braze Web SDK für diese Seite und zukünftige Seitenladungen ignoriert werden. Wenn Sie die Datenerfassung zu einem späteren Zeitpunkt wieder aufnehmen möchten, können Sie mit der Methode [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) die Datenerfassung fortsetzen. Mehr dazu erfahren Sie in unserem Artikel [Deaktivieren von Internet-Tracking]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=web).

{% endtab %}
{% tab Android SDK %}

Sie können mit [`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder) das SDK so konfigurieren, dass es nur eine Teilmenge der Schlüssel oder Werte des Geräteobjekts gemäß einer festgelegten Allowlist  sendet. Dies muss aktiviert werden über [`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder).

{% alert important %}
Eine leere Allowlist führt dazu, dass **keine** Gerätedaten an Braze gesendet werden.
{% endalert %}

{% endtab %}
{% tab Swift SDK %}

Sie können die zulässigen Felder zu [`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) in Ihrer `Braze.Configuration` zuweisen, um eine Allowlist für Gerätefelder anzulegen, die vom SDK erfasst werden. Die vollständige Liste der Felder ist definiert in [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty). Um die Erfassung aller Felder des Geräts zu deaktivieren, lassen Sie den Wert dieser Eigenschaft leer (`[]`).

{% alert important %}
Standardmäßig werden alle Felder durch das Braze Swift SDK erfasst. Das Entfernen einiger Eigenschaften des Geräts kann SDK Features deaktivieren.
{% endalert %}

Weitere Einzelheiten zur Verwendung dieser Methode finden Sie unter [Speicherung]({{site.baseurl}}/developer_guide/storage/?tab=swift) in der Dokumentation zum Swift SDK.

{% endtab %}
{% endtabs %}

## Welche Version des SDK verwende ich?

Sie können die SDK-Version einer bestimmten App im Dashboard unter **Einstellungen > App-Einstellungen** sehen. Unter **Live SDK Version** finden Sie die höchste Braze SDK Version, die von Ihrer letzten Live-App für mindestens 5 % Ihrer Nutzer verwendet wurde.

![Eine App namens Swifty in einem Workspace. Die Live SDK Version ist 6.6.0.]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"} 

{% alert tip %}
Wenn Sie eine iOS App haben, können Sie sich vergewissern, dass Sie das [Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) anstelle des alten [Objective-C iOS SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/) verwenden, wenn Ihre **Live SDK Version** gleich oder höher als 5.0.0 ist, was die erste veröffentlichte Version des Swift SDK war.
{% endalert %}

