---
nav_title: Übersicht
article_title: In-App-Nachricht Übersicht für Roku
platform: Roku
channel: in-app messages
page_order: 0
page_type: reference
description: "Dieser Artikel enthält eine Übersicht über das In-App-Nachrichtentool von Roku, einschließlich bewährter Verfahren und Anwendungsfälle."

---

# Übersicht über In-App-Nachrichten

> Mit [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) können Sie Inhalte an Ihre Nutzer übermitteln, ohne sie mit einer Push-Benachrichtigung zu unterbrechen. Angepasste und maßgeschneiderte In-App-Nachrichten verbessern das Nutzererlebnis und helfen Ihrer Zielgruppe, den größten Nutzen aus Ihrer App zu ziehen. Mit einer Vielzahl von Layouts und Anpassungswerkzeugen, aus denen Sie wählen können, binden In-App-Nachrichten Ihre Nutzer mehr als je zuvor.

In unseren [Fallstudien](https://www.braze.com/customers) finden Sie Beispiele für In-App-Nachrichten.

![Drei Bilder von möglichen In-App-Nachrichten von Roku, die ein Nutzer:innen erstellen könnte. Zu diesen Beispielen gehören "Fullscreen Takeover", "Homepage-Banner" und "Corner Notifier".]({% image_buster /assets/img/roku/Docs-Imagery.png %})

## Arten von In-App-Nachrichten

Erstellen Sie eine In-App-Nachricht für Roku, indem Sie **Roku-Geräte** als In-App-Nachrichten-Plattform auswählen.

![]({% image_buster /assets/img/roku/1-Platform-Selector.png %})

## Technische Dokumentation

Besuchen Sie unsere [Integrationsanleitung]({{ site.baseurl }}/developer_guide/platform_integration_guides/roku/in-app_messaging/integration) für Anweisungen zur Anzeige von In-App-Nachrichten und zur Protokollierung von Impressionen und Click Analytics.

![Ein Beispiel für ein "Homepage-Banner", das die verschiedenen Komponenten zeigt, die zur Erstellung eines angepassten Banners benötigt werden. Zu den aufgelisteten Komponenten gehören die Komponente für die Nachrichtenzusammenstellung (die den Textkörper, den Button-Text, das Bild, das zugewiesene Button-Verhalten (Deeplink) und die Schlüssel-Wert-Paare anzeigt), die Backend-Details (die Zielgruppe, die als "Nutzer, die Staffel 1 gesehen haben" aufgeführt ist, die beabsichtigten Interaktionen (der Button setzt Deeplinks zur App, das Schließen der Nachricht entlässt die Nachricht und die automatische Entlassung nach 10 Sekunden), der Trigger (Sitzungsstart) und das Schlüssel-Wert-Paar (Template = homepage_banner)).]({% image_buster /assets/img/roku/Roku-In-App-Messages-Example.png %})

## Prüfung und QA

Das Feature Test senden wird für In-App-Nachrichten von Roku nicht unterstützt. Um eine Nachricht zu testen, starten Sie die Kampagne und filtern Sie nur nach Ihrer Nutzer-ID.

