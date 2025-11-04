---
nav_title: MetaRouter
article_title: MetaRouter
description: "Verbessern Sie Ihr Kundendaten-Management in Braze, mit MetaRouter. Diese leistungsstarke, serverseitige Lösung zur Verwaltung von Tags bietet ein Höchstmaß an Konformität und Kontrolle mit nahtlosen Bereitstellungsoptionen, ob in einer von MetaRouter gehosteten privaten Cloud oder in Ihrer eigenen Infrastruktur."
alias: /partners/metarouter/
page_type: partner
search_tag: Partner
---

# MetaRouter

> [MetaRouter](https://www.metarouter.io/) steigert Ihr Braze-Erlebnis durch nahtlose Integration als leistungsstarke Server-seitige Tag-Management-Plattform. Es ermöglicht Ihnen die Orchestrierung einer kompletten Customer Journey innerhalb von Braze, von der zuverlässigen Datenerfassung von First-Party-Daten mit einer Anreicherung von bis zu 30% bis hin zur Aktivierung von Event-Streams in Echtzeit für personalisierte Journeys. Darüber hinaus vereinfacht MetaRouter die Implementierung, da keine Tags von Braze oder anderen Drittanbietern mehr benötigt werden. So können Sie die Daten, die in Braze einfließen, genauestens kontrollieren, Parameter für Parameter.

_Diese Integration wird von Metarouter gepflegt._

## Unterstützte Funktionen

- Wiederholungen können eingebaut werden.
- Anfragen werden gebündelt.
- Rate-Limiting-Probleme werden mit einem erneuten Versuch behandelt.
- Externe ID und PII werden unterstützt. MetaRouter gibt ihre anonyme ID und alle von den Clients gewünschten PII (E-Mail, Telefonnummer, Name) weiter.
- Sie können Braze Daten zu Käufen und angepassten Events senden.
  - Event-Eigenschaften werden unterstützt.
  - Verschachtelte Event-Eigenschaften werden nicht unterstützt.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Anforderung           | Beschreibung                                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ein MetaRouter-Konto  | Ein [MetaRouter Enterprise-Konto](https://enterprise.metarouter.io/).                                                                                |
| Braze REST API-Schlüssel    | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. Um einen zu erstellen, gehen Sie zu **Einstellungen** > **API-Schlüssel**.                                                |
| Ein Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## MetaRouter einrichten

So richten Sie MetaRouter für Ihre Integration in Braze ein:

1. Gehen Sie zu MetaRouter und erstellen Sie einen neuen Cluster.
2. Wählen Sie die Ereignisse, die Sie tracken möchten.
3. Installieren Sie ein MetaRouter SDK und integrieren Sie Ereignisse in Ihre Website.
4. Verbinden Sie Ihr Cluster mit dem UI Ihrer Website.
5. Erstellen Sie eine neue Pipeline.
6. Überprüfen Sie, ob Ihre Website Ereignisse an MetaRouter sendet.

## Integration von Braze

### Schritt 1: Fügen Sie die Integration von Braze hinzu

Wählen Sie in Enterprise MetaRouter **Integrationen** > **Neue Integration** > **Braze** und benennen Sie Ihre Integration. Geben Sie als nächstes Ihre Instanz-URL und Ihren API-Schlüssel ein und wählen Sie dann **Änderungen übernehmen**.

![Hinzufügen von Braze als Integration in MetaRouter.]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### Schritt 2: Abbildung der Ereignisse hinzufügen

Fügen Sie für jeden Identitätsausgang eine Abbildung der Ereignisse hinzu und konfigurieren Sie dann die Ereignisse, die Sie an Braze senden möchten. Wenn Sie fertig sind, wählen Sie **Als neue Revision speichern** aus.

![Fügen Sie für jeden der Identitätsausgänge eine Abbildung der Ereignisse hinzu.]({% image_buster /assets/img/metarouter/img2.png %})

