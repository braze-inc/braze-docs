---
nav_title: Gimbal
article_title: Gimbal
alias: /partners/gimbal/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Gimbal, die es Ihnen ermöglicht, Ihre Marketingrelevanz mithilfe von Standortdaten zu perfektionieren."
page_type: partner
search_tag: Partner

---

# Gimbal

> [Gimbal](https://gimbal.com/) ermöglicht es Ihnen, Ihre Marketingrelevanz mithilfe von Standortdaten zu perfektionieren. Ihr Location SDK gepaart mit Geofencing-Software und Beacons ermöglicht relevante, personalisierte, auf die Umgebung abgestimmte mobile Erlebnisse.

Kombinieren Sie Ihre Beacon- oder Geofence-Unterstützung mit den Targeting- und Messaging-Funktionen von Braze, um mehr über die physischen Aktionen Ihrer Nutzer zu erfahren und sie entsprechend zu benachrichtigen. Diese Partnerschaftsintegration eröffnet eine Reihe von Anwendungsfällen für:

- **Marketing:** Versenden Sie kontextbezogene Nachrichten und bauen Sie Erlebnisreisen für Verbraucher auf.
- **Wettbewerbsanalyse:** Richten Sie Auslöser in der Nähe von Konkurrenzstandorten ein, um Verbrauchertrends und -muster zu verstehen.
- **Publikumseinblicke:** Verstehen Sie das Besuchsverhalten Ihrer Nutzer und segmentieren Sie auf der Grundlage dieser Erkenntnisse weiter.

{% alert note %}
Diese Integration funktioniert für Gimbal Beacons und Gimbal Geofence-Lösungen gleichermaßen.
{% endalert %}

## Voraussetzungen

| Anforderung| Beschreibung|
| ---| ---|
| [Gimbal Manager Konto][1] | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Gimbal Manager-Konto. |
|[Gimbal Location SDK](https://docs.gimbal.com/index.html) | Das Gimbal Location SDK ermöglicht Makro- und Mikro-Standort-basierte mobile Erlebnisse unter Verwendung von Proximity Beacons und Geofences, mit denen Sie effektiver mit den Nutzern Ihrer App kommunizieren können. Sie müssen das SDK implementiert haben und Geofences (oder Beacons) einrichten. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SDK-Integration

Um Braze und Gimbal zu integrieren, müssen Sie das Gimbal Location SDK implementieren und ein Gimbal Manager-Konto erstellen. Die folgenden Integrationen für Android, FireOS und iOS erstellen für jeden neuen Ort, den ein Nutzer betritt, ein einzigartiges benutzerdefiniertes Ereignis. Diese Ereignisse können dann für das Triggering und Retargeting in Ihren Kampagnen und Canvases verwendet werden.

Wenn Sie mehr als 50 Orte erstellen möchten, empfehlen wir Ihnen, ein allgemeines benutzerdefiniertes Ereignis `Places Entered` zu erstellen und den Ortsnamen als Ereigniseigenschaft hinzuzufügen. 

1. Integrieren Sie das [Gimbal SDK][2] für Android und iOS in Ihre App, indem Sie den Anweisungen in der [Gimbal Dokumentation][3] folgen.
2. Verwenden Sie die [REST-API][4] von Gimbal, um Benutzer `places` zu erhalten.
3. Verknüpfen Sie Ihr Gimbal-Konto mit Braze, indem Sie den Braze [REST API-Schlüssel][5] eingeben.
4. Richten Sie [benutzerdefinierte Ereignisse][6] im Braze SDK ein. Sie können Gimbal mit Braze für [Android und FireOS][7] und [iOS][8] integrieren.
5. Protokolleigenschaften für diese Ereignisse (Ortsname, Verweildauer).
6. Verwenden Sie diese Eigenschaften und Ereignisse zum Auslösen von Kampagnen und Canvases in Braze. 

[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data_and_analytics/Custom_Data/custom_events/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons