---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Infillion, die es Ihnen ermöglicht, die Relevanz Ihres Marketings mithilfe von Standortdaten zu perfektionieren."
page_type: partner
search_tag: Partner

---

# Infillion

> [Infillion](https://infillion.com/) ermöglicht es Ihnen, die Relevanz Ihres Marketings mithilfe von Standortdaten zu perfektionieren. Ihr Standort SDK gepaart mit Geofencing-Software und Beacons ermöglicht relevante, personalisierte, auf die Nähe bezogene mobile Erlebnisse.

Kombinieren Sie Ihre Beacon- oder Geofence-Unterstützung mit den Targeting- und Messaging-Features von Braze, um mehr über die physischen Aktionen Ihrer Nutzer:innen zu erfahren und ihnen entsprechende Nachrichten zu senden. Diese partnerschaftliche Integration eröffnet eine Reihe von Anwendungsfällen für:

- **Marketing:** Versenden Sie kontextuell relevante Messaging-Nachrichten und bauen Sie eine erlebnisorientierte Verbraucher:in auf.
- **Wettbewerbsanalyse:** Richten Sie Trigger an konkurrierenden Standorten ein, um Verbrauchertrends und -muster zu verstehen.
- **Audience Insights:** Verstehen Sie das Besuchsverhalten Ihrer Nutzer:innen und segmentieren Sie auf der Grundlage dieser Erkenntnisse weiter.

{% alert note %}
Diese Integration funktioniert für Infillion Beacons und Infillion Geofence Lösungen gleichermaßen.
{% endalert %}

## Voraussetzungen

| Anforderung| Beschreibung|
| ---| ---|
| [Infillion Manager:in][1] | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Infillion Manager:in-Konto. |
|[Infillion Standort SDK](https://docs.gimbal.com/index.html) | Das Infillion Location SDK ermöglicht Makro- und Mikro-Standort-basierte mobile Erlebnisse unter Verwendung von Proximity Beacons und Geoofences, die es Ihnen ermöglichen, effektiver mit Ihren Nutzer:innen zu kommunizieren. Sie müssen das SDK implementiert und GeoFences (oder Beacons) eingerichtet haben. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SDK-Integration

Um Braze und Infillion zu integrieren, müssen Sie das Infillion Location SDK implementieren und ein Infillion Manager:in-Konto erstellen. Die folgenden Integrationen für Android, FireOS und iOS erstellen ein eindeutiges angepasstes Event für jeden neuen Ort, den ein Nutzer:innen betritt. Diese Events können dann für das Triggern und Retargeting in Ihren Kampagnen und Canvase verwendet werden.

Wenn Sie voraussichtlich mehr als 50 Orte erstellen werden, empfehlen wir Ihnen, ein allgemeines `Places Entered` angepasstes Event zu erstellen und den Ortsnamen als Event-Eigenschaft hinzuzufügen. 

1. Integrieren Sie das [Infillion SDK][2] für Android und iOS in Ihre App, indem Sie die Anweisungen in der [Infillion Dokumentation][3] befolgen.
2. Verwenden Sie die [REST API][4] von Infillion, um Nutzer:innen zu erhalten `places`.
3. Verknüpfen Sie Ihr Infillion-Konto mit Braze, indem Sie den Braze [REST API-Schlüssel][5] eingeben.
4. Richten Sie [angepasste Events][6] im Braze SDK ein. Sie können Infillion mit Braze für [Android und FireOS][7] und [iOS][8] integrieren.
5. Protokollieren Sie Eigenschaften für diese Ereignisse (Ortsname, Verweildauer).
6. Verwenden Sie diese Eigenschaften und Ereignisse zum Triggern von Kampagnen und Canvase in Braze. 

[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data/custom_data/custom_attributes/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons