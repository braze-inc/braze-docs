---
nav_title: MetaRouter
article_title: MetaRouter
description: "Verbessern Sie Ihr Kundendatenmanagement in Braze mit MetaRouter. Diese leistungsstarke, serverseitige Tag-Management-Lösung bietet ein Höchstmaß an Konformität und Kontrolle mit nahtlosen Bereitstellungsoptionen, ob auf einer von MetaRouter gehosteten privaten Cloud oder Ihrer eigenen Infrastruktur."
alias: /partners/MetaRouter/
page_type: partner
search_tag: Partner
---

# MetaRouter

> [MetaRouter](https://www.metarouter.io/) verbessert Ihr Braze-Erlebnis durch die nahtlose Integration als leistungsstarke serverseitige Tag-Management-Plattform. Mit Braze können Sie eine komplette Customer Data Journey orchestrieren, von der zuverlässigen Sammlung von First-Party-Daten, die um bis zu 30% angereichert sind, bis hin zur Aktivierung von Ereignisströmen in Echtzeit für personalisierte Journeys. Darüber hinaus vereinfacht MetaRouter die Implementierung, da keine Braze-Tags oder Tags von Drittanbietern mehr erforderlich sind und Sie die Daten, die in Braze einfließen, Parameter für Parameter genau kontrollieren können.

## Unterstützte Funktionen

- Wiederholungen können eingebaut werden.
- Anfragen werden gebündelt.
- Probleme mit der Ratenbegrenzung werden mit einem erneuten Versuch behandelt.
- Externe ID und PII werden unterstützt. MetaRouter gibt ihre anonyme ID und alle PII (E-Mail, Telefonnummer, Name) weiter, die die Kunden wünschen.
- Sie können Braze-Käufe und benutzerdefinierte Ereignisdaten senden.
  - Ereigniseigenschaften werden unterstützt.
  - Verschachtelte Ereigniseigenschaften werden nicht unterstützt.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Anforderung           | Beschreibung                                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ein MetaRouter-Konto  | Ein [MetaRouter Enterprise-Konto](https://enterprise.metarouter.io/).                                                                                |
| Braze REST API Schlüssel    | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. Um einen zu erstellen, gehen Sie zu **Einstellungen** > **API-Schlüssel**.                                                |
| Ein Braze REST Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, können Sie einen API-Schlüssel unter **Entwicklerkonsole** > **API-Einstellungen** erstellen.
{% endalert %}

## MetaRouter einrichten

So richten Sie MetaRouter für Ihre Braze-Integration ein:

1. Gehen Sie zu MetaRouter und erstellen Sie einen neuen Cluster.
2. Wählen Sie die Ereignisse, die Sie verfolgen möchten.
3. Installieren Sie ein MetaRouter SDK und integrieren Sie Ereignisse in Ihre Website.
4. Verbinden Sie Ihr Cluster mit der Benutzeroberfläche Ihrer Website.
5. Erstellen Sie eine neue Pipeline.
6. Überprüfen Sie, ob Ihre Website Ereignisse an MetaRouter sendet.

## Integration von Braze

### Schritt 1: Fügen Sie die Braze-Integration hinzu

Wählen Sie in Enterprise MetaRouter **Integrationen** > **Neue Integration** > **Braze** und benennen Sie dann Ihre Integration. Geben Sie als nächstes Ihre Instanz-URL und Ihren API-Schlüssel ein und wählen Sie dann **Änderungen übernehmen**.

![Hinzufügen von Braze als eine Integration in MetaRouter.]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### Schritt 2: Ereigniszuordnung hinzufügen

Fügen Sie die Ereigniszuordnung für jeden Identitätsausgang hinzu und konfigurieren Sie dann die Ereignisse, die Sie an Braze senden möchten. Wenn Sie fertig sind, wählen Sie **Als neue Revision speichern**.

![Fügen Sie für jeden der Identitätsausgänge eine Ereigniszuordnung hinzu.]({% image_buster /assets/img/metarouter/img2.png %})
