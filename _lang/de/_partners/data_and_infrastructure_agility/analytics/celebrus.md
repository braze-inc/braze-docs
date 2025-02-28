---
nav_title: Celebrus
article_title: Celebrus Integration
description: "Integration von Braze und Celebrus."
---

# Celebrus

> Celebrus lässt sich nahtlos mit dem Braze SDK über Web- und mobile App-Kanäle hinweg integrieren und erleichtert so die Befüllung von Braze mit Kanalaktivitätsdaten. Dazu gehören umfassende Einblicke in den Besucherverkehr über digitale Assets in bestimmten Zeiträumen. <br><br>Darüber hinaus erfasst Celebrus umfangreiche Profildaten für jeden einzelnen Kunden, die mit Braze synchronisiert werden können. So können Sie effektive Analyse- und Kommunikationsstrategien für Braze erstellen, die auf umfassenden, genauen und detaillierten First-Party-Daten basieren. Diese Fähigkeit wird durch die auf maschinellem Lernen basierenden Signale von Celebrus noch verstärkt, die eine mühelose Datenerfassung ermöglichen, ohne dass umfangreiche Markierungen erforderlich sind. Mit einem robusten First-Party-Identitätsgraphen sind alle Daten sofort für die unmittelbare Nutzung zugänglich. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Celebrus-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Celebrus-Konto. |
| Data Warehouse (optional) | Wenn Sie den Celebrus-Connector für benutzerdefinierte Attribute von Braze verwenden, müssen Sie über ein Data Warehouse verfügen, das von der Braze Cloud Data Ingestion (CDI) Integration unterstützt wird, und CDI im Braze Dashboard konfigurieren. |
| Braze SDK Konfigurationseinstellungen (optional) | Wenn Sie den Celebrus Connector für Braze SDK verwenden, müssen Sie den SDK-Endpunkt und den SDK-API-Schlüssel übergeben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Implementierung
Nachdem Sie Ihre Celebrus-Implementierung installiert haben, verwenden Sie die Celebrus-Konnektoren für Braze, um Celebrus-Daten in Braze zu integrieren. Die Celebrus-Integration für Braze besteht aus zwei Elementen: dem Braze SDK und den benutzerdefinierten Attributen von Braze. Sie können entweder eines oder beide einsetzen, je nachdem, wie Sie Braze verwenden und welche Anwendungsfälle Sie benötigen.

Wenn Sie das Braze SDK noch nicht in Ihrem Web-Channel implementiert haben, können Sie Celebrus verwenden, um das Braze SDK bereitzustellen. Celebrus fügt das Braze SDK zu Webseiten hinzu und richtet die Braze-Identität für den Webbesucher mithilfe des Celebrus-Identitätsgraphen ein. Kundenattribute können mit Braze über eine Cloud Data Ingestion (CDI) synchronisiert werden. Dies erfordert ein Data Warehouse, das von Braze CDI unterstützt wird, und die Konfiguration des CDI in Braze.

### Celebrus-Anschluss für Braze SDK

Der Celebrus-Connector für Braze SDK liefert High-Level-Web- und Mobile-App-Channel-Daten für Braze. Im Braze SDK wird die Celebrus `System Identity` aus dem Celebrus-Identitätsgraphen als Bezeichner für die Braze-Integration verwendet. Andere Bezeichner werden für die Synchronisierung benutzerdefinierter Attribute über den Braze Custom Attributes Celebrus Connector unterstützt.

Der Connector stellt das Braze SDK in Ihrem Channel bereit und konfiguriert es. Sie müssen also einige Einstellungen im Braze SDK-Datenstrom konfigurieren und die Werte für diese drei Einstellungen angeben:

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
Der Celebrus-Konnektor für Braze SDK fügt das Braze SDK ein und initialisiert es, um den Benutzer zu identifizieren und die Kennung zum Identitätsgraphen von Celebrus hinzuzufügen. Dieser Connector protokolliert keine Daten im Benutzerprofil und löst auch keine anderen Methoden des Braze SDK aus. <br><br>Sie können alle gewünschten Methoden direkt in Ihrer Codebasis aufrufen, um Daten über das [Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/) zu protokollieren oder andere vom Braze SDK unterstützte Funktionen zu nutzen.
{% endalert%}

### Celebrus-Anschluss für benutzerdefinierte Attribute von Braze

#### Schritt 1: Konfigurieren Sie Verbundene Details in Celebrus 

Der Celebrus-Konnektor für benutzerdefinierte Attribute von Braze sendet benutzerdefinierte Attribute an eine Zwischendatenbank, die so vorformatiert ist, wie Braze sie zu empfangen erwartet. In Celebrus konfigurieren Sie die Verbindungsdetails für die Datenbank, die davon abhängen, welche Art von Datenbank Sie verwenden (z.B. Snowflake oder Redshift). 

#### Schritt 2: Konfigurieren Sie Cloud Data Ingestion in Ihrem Braze Dashboard

Diese Integration verwendet Braze Cloud Data Ingestion. Folgen Sie den Anweisungen unter [Data Warehouse-Integrationen]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/), um die [Einstellungen für Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/) je nach Art des von Ihnen verwendeten Warehouses einzurichten und zu konfigurieren. 

#### Schritt 3: Daten von Celebrus mit Braze synchronisieren

Celebrus erfasst und weist einer Person eindeutige Identifikatoren zu, wie z. B. E-Mail, Telefon, `external_id`oder Benutzer-Alias, und sendet diese über CDI an Braze. Dadurch können Daten für dieselbe Person mit Braze synchronisiert werden.

Celebrus verwendet die definierten Identifikatoren, um die Kundenattribute zu senden, die im Celebrus Profil Builder definiert sind, aber nur, wenn sich die Attributwerte ändern. Beachten Sie, dass die Attributnamen wie im Celebrus-Profilersteller definiert sind, so dass die Attribute in Braze denen im Celebrus-Profil entsprechen. Diese müssen möglicherweise angepasst werden, um den Braze-Namenskonventionen zu entsprechen. Zum Beispiel die Einhaltung der [Standard-Attributbenennungskonventionen]({{site.baseurl}}/api/objects_filters/user_attributes_object/) von Braze.  

{% alert important %}
Im Moment unterstützt diese Version noch keine Ereignisse und Käufe.<br><br> Diese Integration sendet Attribute als String-Werte, so dass einige Attribute Listen sind (z. B. Signale). Im Moment können Listen noch nicht in Arrays umgewandelt werden. Es gibt keine verschachtelten Attribute.
{% endalert%}

