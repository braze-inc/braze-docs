---
nav_title: Celebrus
article_title: Celebrus-Integration
description: "Integration von Braze und Celebrus."
---

# Celebrus

> Celebrus integriert sich nahtlos in das Braze SDK über alle Kanäle im Internet und in mobilen Apps und erleichtert so die Befüllung von Braze mit Daten über die Aktivitäten der Kanäle. Dazu gehören umfassende Insights über den Besucherverkehr bei digitalen Assets über bestimmte Zeiträume. <br><br>Darüber hinaus erfasst Celebrus umfangreiche Profildaten für jeden einzelnen Kunden, die mit Braze synchronisiert werden können. So können Sie effektive Analytics- und Kommunikationsstrategien für Braze erstellen, die auf umfassenden, genauen und detaillierten First-Party-Daten basieren. Diese Fähigkeit wird durch die von maschinellem Lernen gestützten Signale von Celebrus noch verstärkt, die eine mühelose Datenerfassung ohne umfangreiche Tags zulassen. Mit einem robusten First-Party-Identitätsgraphen sind alle Daten sofort für die unmittelbare Nutzung zugänglich. 

_Diese Integration wird von Celebrus gepflegt._

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Celebrus-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Celebrus-Konto. |
| Data Warehouse (optional) | Wenn Sie den Celebrus Konnektor für angepasste Attribute von Braze verwenden, müssen Sie über ein Data Warehouse verfügen, das von der Braze Cloud Data Ingestion (CDI) Integration unterstützt wird, und CDI im Braze Dashboard konfigurieren. |
| Braze SDK Konfigurationseinstellungen (optional) | Wenn Sie den Celebrus Konnektor für Braze SDK verwenden, müssen Sie den SDK-Endpunkt und den SDK-API-Schlüssel übergeben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Implementierung
Nach der Installation Ihrer Celebrus-Implementierung verwenden Sie die Celebrus Konnektoren für Braze, um Celebrus-Daten in Braze zu integrieren. Die Celebrus-Integration für Braze besteht aus zwei Elementen: dem Braze SDK und den angepassten Attributen von Braze. Je nachdem, wie Sie Braze verwenden und welche Anwendungsfälle Sie benötigen, können Sie entweder eines oder beide einsetzen.

Wenn Sie das Braze SDK nicht bereits in Ihrem Internet-Kanal implementiert haben, können Sie Celebrus verwenden, um das Braze SDK bereitzustellen. Celebrus fügt das Braze SDK zu den Internetseiten hinzu und richtet die Braze-Identität für den Webbesucher mithilfe des Celebrus-Identitätsgraphen ein. Kunden:in-Attribute können über eine Cloud-Datenaufnahme (CDI) mit Braze synchronisiert werden. Dies erfordert ein Data Warehouse, das von Braze CDI unterstützt wird, und die Konfiguration des CDI in Braze.

### Celebrus Konnektor für Braze SDK

Der Konnektor von Celebrus für Braze SDK liefert Daten über die Kanäle von Braze im Internet und in mobilen Apps. Im Braze SDK wird der Celebrus `System Identity` aus dem Celebrus-Identitätsgraphen als Bezeichner für die Braze-Integration verwendet. Andere Bezeichner werden für die Synchronisierung angepasster Attribute über den Konnektor Braze Custom Attributes Celebrus unterstützt.

Der Konnektor setzt das Braze SDK in Ihrem Kanal ein und konfiguriert es. Daher müssen Sie einige Einstellungen im Daten-Stream von Braze SDK konfigurieren und die Werte für diese drei Einstellungen angeben:

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
Der Konnektor von Celebrus für Braze SDK fügt das Braze SDK ein und initialisiert es, um den Nutzer:innen zu identifizieren und den Bezeichner zum Identitätsgraphen von Celebrus hinzuzufügen. Dieser Konnektor protokolliert keine Daten im Nutzerprofil und triggert keine anderen Braze SDK-Methoden. <br><br>Sie können alle gewünschten Methoden direkt in Ihrer Code-Basis aufrufen, um Daten über das [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) zu protokollieren oder andere vom Braze SDK unterstützte Features zu nutzen.
{% endalert%}

### Celebrus Konnektor für angepasste Attribute von Braze

#### Schritt 1: Konfigurieren Sie Verbundene Details in Celebrus 

Der Celebrus Konnektor für angepasste Attribute von Braze sendet angepasste Attribute an eine zwischengeschaltete Datenbank, die so vorformatiert ist, wie Braze sie erwartet. In Celebrus konfigurieren Sie die Verbindungsdetails für die Datenbank, die davon abhängen, welche Art von Datenbank Sie verwenden (z. B. Snowflake oder Redshift). 

#### Schritt 2: Konfigurieren Sie die Datenaufnahme in die Cloud in Ihrem Braze-Dashboard

Diese Integration verwendet Braze Cloud Data Ingestion. Folgen Sie den Anweisungen unter [Data Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/), um die [Einstellungen für die Datenaufnahme in der Cloud]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) je nach Art des von Ihnen verwendeten Data Warehouse einzurichten und zu konfigurieren. 

#### Schritt 3: Daten von Celebrus mit Braze synchronisieren

Celebrus erfasst und weist einer Person eindeutige Bezeichner wie E-Mail, Telefon, `external_id`oder Nutzer:in zu und sendet diese über CDI an Braze. Dies ermöglicht die Synchronisierung von Daten mit Braze für dieselbe Person.

Celebrus verwendet die definierten Bezeichner, um die Kunden:in-Attribute zu senden, die im Celebrus Profil-Builder definiert sind, aber nur, wenn sich die Attributwerte ändern. Beachten Sie, dass die in der Celebrus-Profilerstellung definierten Attributnamen standardmäßig in Braze verwendet werden. Stellen Sie also sicher, dass Sie diese Namen aktualisieren, um die [Braze-Namenskonventionen]({{site.baseurl}}/api/objects_filters/user_attributes_object/) einzuhalten.

{% alert important %}
Im Moment unterstützt diese Version noch keine Ereignisse und Käufe.<br><br> Diese Integration sendet Attribute als String-Werte, so dass einige Attribute Listen sind (z.B. Signale). Im Moment können Listen noch nicht in Arrays umgewandelt werden. Es gibt keine verschachtelten Attribute.
{% endalert%}

