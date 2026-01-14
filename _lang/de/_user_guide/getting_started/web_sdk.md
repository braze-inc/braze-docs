---
nav_title: SDK-Übersicht
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

Um Zeit zu sparen und eine reibungslose Integration zu gewährleisten, empfehlen wir, dass Sie und Ihr Entwicklungsteam Ihre benutzerdefinierten Ereignisse, benutzerdefinierten Attribute und das SDK zur gleichen Zeit einrichten. Erfahren Sie mehr über die Schritte, die Ihre Marketing- und Technikteams gemeinsam durchdenken müssen, indem Sie unseren [Artikel zur Implementierung]({{site.baseurl}}/user_guide/getting_started/integration/) lesen. 

## Datenaggregation

Das Braze SDK erfasst automatisch riesige Datenmengen auf Nutzerebene, sodass Sie die wichtigsten Metriken für Ihre App und Ihre Nutzerbasis leicht erkennen können. Sie werden ähnliche Anwendungen in einem einzigen Arbeitsbereich auf Ihrem Dashboard gruppieren. So können Sie zum Beispiel die iOS- und Android-Versionen Ihrer App im selben Arbeitsbereich zusammenfassen, so dass Sie die gesammelten Daten von Benutzern auf beiden Plattformen sehen können. So erhalten Sie einen vollständigeren Überblick über Ihre Nutzer im Web und auf mobilen Kanälen. Weitere Informationen finden Sie in dem Artikel auf der [Startseite]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/).

## In-App-Nachrichten

Das SDK macht es einfach, In-App-Nachrichten zu verfassen und zu versenden, um direkt mit den Nutzer:innen in Kontakt zu treten. Sie können wählen, ob Sie Slideup-, Modal- oder Vollbildnachrichten senden möchten, je nach Ihrer Kampagnenstrategie. Weitere Informationen zum Verfassen einer In-App-Nachricht finden Sie auf unserer Seite zum [Erstellen einer In-App-Nachricht]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/).

![Push auf einem Webbrowser angezeigt]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Push-Benachrichtigungen

Push-Benachrichtigungen sind eine weitere großartige Möglichkeit, mit Ihren Nutzer:innen in Kontakt zu treten, und eignen sich besonders für zeitkritische Handlungsaufforderungen. Mobile Push-Benachrichtigungen erscheinen auf den Geräten Ihrer Benutzer, und Web-Push-Benachrichtigungen erscheinen auch dann, wenn Ihre Website nicht geöffnet ist. Weitere Informationen zur Verwendung von Push-Benachrichtigungen finden Sie in unserem [Artikel über Push-Benachrichtigungen]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/).

Die Nutzer Ihrer Website oder App müssen sich für den Empfang von Push-Benachrichtigungen entscheiden. Siehe [Push Priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) für weitere Einzelheiten. 

## Segmentierung und Lieferregeln

Eine Kampagne, die In-App-Nachrichten enthält, wird standardmäßig an alle Versionen der App in diesem Workspace gesendet. Zum Beispiel wird die Nachricht sowohl an Web- als auch an mobile Nutzer:innen gesendet. Um eine In-App-Nachricht ausschließlich an das Web oder das Mobiltelefon zu senden, müssen Sie Ihre Kampagne entsprechend segmentieren, was standardmäßig durch das Braze SDK unterstützt wird. 

Sie können ein Segment Ihrer Internet-Nutzer erstellen, indem Sie **Apps und Websites mit Targeting** auf **Nutzer:innen bestimmter Apps** zusammenstellen, und dann nur Ihre Website für die **spezifischen Apps** auswählen.

![Segment Detailseite mit Web App im Fokus]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

Dies ermöglicht es Ihnen, Nutzer:innen auf der Grundlage ihres Verhaltens auf intelligente Weise anzusprechen. Wenn Sie Webnutzer:innen ansprechen möchten, um sie zum Herunterladen Ihrer mobilen App zu bewegen, würden Sie dieses Segment als Ihre Zielgruppe erstellen. Wenn Sie eine Nachrichtenkampagne versenden möchten, die eine mobile In-App-Nachricht, aber keine Web-Nachricht enthält, deaktivieren Sie das Symbol für Ihre Website in Ihrem Segment.

## Unterstützte Plattformen

Braze bietet SDKs für mehrere Plattformen, wie Internet, Android und Swift. Die vollständige Liste finden Sie im [Braze Entwickler:in]({{site.baseurl}}/developer_guide/home).
