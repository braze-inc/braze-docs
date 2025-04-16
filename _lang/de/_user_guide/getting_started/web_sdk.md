---
nav_title: SDK Übersicht 
article_title: SDK Übersicht 
page_order: 9
page_type: reference
description: "Dieser Referenzartikel behandelt die Grundlagen des Braze SDK."
---

# SDK-Übersicht 

> Mit dem Braze SDK ist es ganz einfach, Sitzungsdaten zu sammeln, Nutzer:innen zu identifizieren und Käufe und angepasste Events über Ihre Website oder App aufzuzeichnen. Sie können das SDK auch verwenden, um mit Ihren Nutzer:innen in Kontakt zu treten, indem Sie In-App-Nachrichten und Push-Benachrichtigungen direkt vom Braze-Dashboard aus versenden.

Kurz gesagt, das Braze SDK:
* Sammelt und synchronisiert Benutzerdaten in einem konsolidierten Benutzerprofil
* Erfasst Marketingdaten und angepasste Daten speziell für Ihr Unternehmen
* Unterstützt Push-Benachrichtigungen, In-App-Nachrichten und Content-Card-Nachrichtenkanäle

## Was ist ein SDK?
Ein Software Development Kit (SDK) ist ein Satz vorgefertigter Tools – nur kleine Code-Blöcke –, die digitalen Anwendungen hinzugefügt werden können, um neue Funktionen zu unterstützen. Das Braze SDK wird zum Senden und Abrufen von Informationen zu und von Ihrer App oder Website verwendet. Es ist so konzipiert, dass es von Anfang an wichtige Funktionen bietet: Erstellen von Benutzerprofilen, Protokollieren von benutzerdefinierten Ereignissen, Auslösen von Push-Benachrichtigungen usw. 

Da diese Funktionen standardmäßig von Braze bereitgestellt wird, können sich Ihre Entwickler:innen auf Ihr Kerngeschäft konzentrieren. Ohne ein SDK müsste jeder Braze-Kunde die gesamte Infrastruktur und die Tools für die Datenverarbeitung, die Segmentierungslogik, die Zustelloptionen, die Behandlung anonymer Benutzer, die Kampagnenanalyse und vieles mehr von Grund auf neu erstellen. Das würde viel länger dauern und wäre viel mühsamer als die Stunde, die es dauert, unser SDK einzubinden.

## Implementierung

Um ein SDK in Ihre Anwendung oder Website einzubinden, müssen Sie den Code des SDKs in die allgemeine Codebasis der Anwendung einfügen. Das bedeutet, dass Ihr Entwicklungsteam daran beteiligt sein wird, unsere Apps miteinander zu verbinden, damit Informationen und Aktionen zwischen ihnen fließen. Doch obwohl Ihre Entwickler:innen daran beteiligt sind, ist das SDK so konzipiert, dass es schlank und nutzerfreundlich zu integrieren ist. 

Um Zeit zu sparen und eine reibungslose Integration zu gewährleisten, empfehlen wir, dass Sie und Ihr Entwicklungsteam Ihre benutzerdefinierten Ereignisse, benutzerdefinierten Attribute und das SDK zur gleichen Zeit einrichten. Erfahren Sie mehr über die Schritte, die Ihre Marketing- und Technikteams gemeinsam durchdenken müssen, indem Sie unseren [Artikel zur Implementierung][4] lesen. 

## Datenaggregation

Das Braze SDK erfasst automatisch riesige Datenmengen auf Nutzerebene, sodass Sie die wichtigsten Metriken für Ihre App und Ihre Nutzerbasis leicht erkennen können. Sie werden ähnliche Anwendungen in einem einzigen Arbeitsbereich auf Ihrem Dashboard gruppieren. So können Sie zum Beispiel die iOS- und Android-Versionen Ihrer App im selben Arbeitsbereich zusammenfassen, so dass Sie die gesammelten Daten von Benutzern auf beiden Plattformen sehen können. So erhalten Sie einen vollständigeren Überblick über Ihre Nutzer im Web und auf mobilen Kanälen. Weitere Informationen finden Sie in dem Artikel auf der [Startseite][3].

## In-App-Nachrichten

Das SDK macht es einfach, In-App-Nachrichten zu verfassen und zu versenden, um direkt mit den Nutzer:innen in Kontakt zu treten. Sie können wählen, ob Sie Slideup-, Modal- oder Vollbildnachrichten senden möchten, je nach Ihrer Kampagnenstrategie. Weitere Informationen zum Verfassen einer In-App-Nachricht finden Sie auf unserer Seite [Erstellen einer In-App-Nachricht][8]].

![Push-Benachrichtigung in einem Webbrowser][11]{: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Push-Benachrichtigungen

Push-Benachrichtigungen sind eine weitere großartige Möglichkeit, mit Ihren Nutzer:innen in Kontakt zu treten, und eignen sich besonders für zeitkritische Handlungsaufforderungen. Mobile Push-Benachrichtigungen erscheinen auf den Geräten Ihrer Benutzer, und Web-Push-Benachrichtigungen erscheinen auch dann, wenn Ihre Website nicht geöffnet ist. Weitere Informationen zur Verwendung von Push-Benachrichtigungen finden Sie in unserem [Artikel über Push-Benachrichtigungen][5].

Die Nutzer Ihrer Website oder App müssen sich für den Empfang von Push-Benachrichtigungen entscheiden. Weitere Einzelheiten finden Sie unter [Push-Priming][13]. 

## Segmentierung und Lieferregeln

Eine Kampagne, die In-App-Nachrichten enthält, wird standardmäßig an alle Versionen der App in diesem Workspace gesendet. Zum Beispiel wird die Nachricht sowohl an Web- als auch an mobile Nutzer:innen gesendet. Um eine In-App-Nachricht ausschließlich an das Web oder das Mobiltelefon zu senden, müssen Sie Ihre Kampagne entsprechend segmentieren, was standardmäßig durch das Braze SDK unterstützt wird. 

Sie können ein Segment Ihrer Webnutzer erstellen, indem Sie im Abschnitt **Verwendete Apps** eines Segments nur das App-Symbol Ihrer Website auswählen.

![Seite Segmentdetails mit ausgewählter Web-App][10]

Dies ermöglicht es Ihnen, Nutzer:innen auf der Grundlage ihres Verhaltens auf intelligente Weise anzusprechen. Wenn Sie Webnutzer:innen ansprechen möchten, um sie zum Herunterladen Ihrer mobilen App zu bewegen, würden Sie dieses Segment als Ihre Zielgruppe erstellen. Wenn Sie eine Nachrichtenkampagne versenden möchten, die eine mobile In-App-Nachricht, aber keine Web-Nachricht enthält, deaktivieren Sie das Symbol für Ihre Website in Ihrem Segment.

## Welche Integrationen gibt es bei Braze?
Braze bietet eine Version unseres SDK für viele Plattformen an (Web, Android, iOS, Flutter, React Native und mehr), aber sie funktionieren alle im Wesentlichen auf die gleiche Weise. Wenn Sie also einen Verweis auf das „Web-SDK“ sehen, handelt es sich lediglich um die Version des Braze SDK, die für Ihre Website vorgesehen ist.

<style>
table th:nth-child(1) {
width: 33%;
}
table th:nth-child(2) {
width: 33%;
}
table th:nth-child(3) {
width: 33%;
}
table td {
word-break: break-word;
text-align: center;
}
</style>
Ausgewählte Integrationen   |    |   
----------- |---------------- | --------------------
[![Android]({% image_buster /assets/img/braze_icons/android.svg %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) |[![iOS]({% image_buster /assets/img/braze_icons/apple.svg %})]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift){: style="max-width:20%;margin-right:15px;border:0" class="noimgborder"} [iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) |[![Web]({% image_buster /assets/img/braze_icons/globe-02.png %})]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web){: style="max-width:25%;margin-right:15px;border:0" class="noimgborder"} [Web]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)  

Alle Integrationen   |    |   
----------- |---------------- | --------------------
[![Cordova Android]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=android){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=android) | [![Cordova iOS]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=ios){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=ios) | [![Flutter Android und iOS]({% image_buster /assets/img/flutter_icon.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=flutter){: style="max-width:20%;margin-top:5%;border:0" class="noimgborder"}  [Flutter Android und iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=flutter)
[![React Native]({% image_buster /assets/img/reactnative_icon.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [React Native]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native) | [![tvOS]({% image_buster /assets/img/tvos_icon.png %})]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/tvos/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [tvOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/tvos/initial_sdk_setup/) | [![MacOS]({% image_buster /assets/img/macOS_icon.png %})]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/macOS/initial_sdk_setup/){: style="max-width:40%;margin-top:15%;border:0" class="noimgborder"}  [MacOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/macOS/initial_sdk_setup/)
[![Unity Android]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity) | [![Unity iOS]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity) | [![Xamarin]({% image_buster /assets/img/xamarin.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=xamarin){: style="max-width:35%;margin-top:5%;border:0" class="noimgborder"}  [Xamarin]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=xamarin) 
[![Roku]({% image_buster /assets/img/roku.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=roku){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [Roku]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=roku) | [![Unreal Engine]({% image_buster /assets/img/unreal.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unreal%20engine){: style="max-width:30%;margin-right:15px;border:0" class="noimgborder"}  [Unreal-Engine]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unreal%20engine)

[3]: {{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/
[4]: {{site.baseurl}}/user_guide/getting_started/integration/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push/about/
[7]: {% image_buster /assets/img_archive/app_group_list.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/
[10]: {% image_buster /assets/img_archive/web-users-segment.png %}
[11]: {% image_buster /assets/img_archive/web_push_macbook.png %}
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
