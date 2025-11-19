---
nav_title: Verbundene Quellen
article_title: Verbundene Quellen
description: "Auf dieser Seite erfahren Sie, wie Sie Braze Cloud Data Ingestion verwenden, um relevante Daten mit Ihrer Snowflake-, Redshift-, BigQuery- und Databricks-Integration zu synchronisieren."
page_order: 2
page_type: reference

---

# Verbundene Quellen

> Verbundene Quellen sind eine Null-Kopie-Alternative zur direkten Synchronisierung von Daten mit dem Feature Cloud Data Ingestion (CDI) von Braze. Eine verbundene Datenquelle fragt direkt Ihr Data Warehouse ab, um neue Segmente zu erstellen, ohne die zugrunde liegenden Daten nach Braze zu kopieren. 

Nachdem Sie eine verbundene Quelle zu Ihrem Braze Workspace hinzugefügt haben, können Sie ein CDI-Segment innerhalb der Segment-Erweiterungen erstellen. Mit CDI Segment-Erweiterungen können Sie SQL-Anfragen direkt an Ihr Data Warehouse stellen (unter Verwendung von Daten, die dort über Ihre CDI Connected Source zur Verfügung gestellt werden) und eine Gruppe von Nutzer:innen erstellen und pflegen, die innerhalb von Braze gezielt angesprochen werden können. 

Weitere Informationen zur Erstellung eines Segments mit dieser Quelle finden Sie unter [CDI Segment-Erweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

{% alert warning %}
Da die angeschlossenen Quellen direkt auf Ihrem Data Warehouse laufen, entstehen Ihnen alle Kosten, die mit der Ausführung dieser Abfragen in Ihrem Data Warehouse verbunden sind. Verbundene Quellen protokollieren keine Datenpunkte, und CDI Segment-Erweiterungen verbrauchen keine SQL-Segmentierungen.
{% endalert %}

## Integration von verbundenen Quellen

### Schritt 1: Verbinden Sie Ihre Ressourcen

Mit der Cloud-Datenaufnahme verbundene Datenquellen erfordern einige Einstellungen auf Braze und in Ihrer Instanz. Folgen Sie diesen Schritten, um die Integration einzurichten - einige Schritte werden in Ihrem Data Warehouse und einige Schritte in Ihrem Braze Dashboard durchgeführt.

{% tabs %}
{% tab Snowflake %}
**In Ihrem Data Warehouse**
1. Erstellen Sie eine Rolle und erteilen Sie die Berechtigung zum Abfragen und Erstellen von Tabellen in einem Schema.
2. Richten Sie Ihr Lagerhaus ein und geben Sie dieser Rolle Zugriff.
3. Erstellen Sie einen Nutzer:in für diese Rolle.
4. Je nach Ihrer Konfiguration müssen Sie Braze IPs in Ihrer Snowflake Netzwerkrichtlinie zulassen.

**Im Braze-Dashboard**

{: start="5"}
5\. Erstellen Sie eine neue verbundene Quelle im Braze Dashboard.
6\. Konfigurieren Sie die Synchronisierungsdetails für die verbundene Quelle.
7\. Rufen Sie den öffentlichen Schlüssel ab, der im Braze-Dashboard bereitgestellt wird.

**In Ihrem Data Warehouse**

{: start="8"}
8\. Hängen Sie den öffentlichen Schlüssel aus dem Braze-Dashboard [zur Authentifizierung an die Nutzer:innen von Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html) an. Wenn Sie fertig sind, können Sie die verbundene Quelle verwenden, um eine oder mehrere CDI Segment-Erweiterungen zu erstellen.
{% endtab %}

{% tab Redshift %}
1. Richten Sie die Quelldaten und die erforderlichen Ressourcen in Ihrer Redshift-Umgebung ein.
2. Erstellen Sie eine neue verbundene Quelle im Braze Dashboard.
4. Testen Sie die Integration.
5. Verwenden Sie die verbundene Quelle, um eine oder mehrere CDI Segment-Erweiterungen zu erstellen.
{% endtab %}

{% tab BigQuery %}
1. Richten Sie die Quelldaten und die erforderlichen Ressourcen in Ihrer BigQuery-Umgebung ein.
2. Erstellen Sie ein Dienstkonto und erlauben Sie den Zugriff auf das/die BigQuery-Projekt(e) und den/die Datensatz(e), die die zu synchronisierenden Daten enthalten.  
3. Erstellen Sie eine neue verbundene Quelle im Braze Dashboard.
4. Testen Sie die Integration.
5. Verwenden Sie die verbundene Quelle, um eine oder mehrere CDI Segment-Erweiterungen zu erstellen.
{% endtab %}

{% tab Databricks %}
1. Richten Sie die Quelldaten und die erforderlichen Ressourcen in Ihrer Databricks-Umgebung ein.
2. Erstellen Sie ein Dienst-Konto und erlauben Sie den Zugriff auf das/die Databricks-Projekt(e) und den/die Datensatz(e), die die zu synchronisierenden Daten enthalten.  
3. Erstellen Sie eine neue verbundene Quelle im Braze Dashboard.
4. Testen Sie die Integration.
5. Verwenden Sie die verbundene Quelle, um eine oder mehrere CDI Segment-Erweiterungen zu erstellen.

{% alert important %}
Es kann zu einer Aufwärmzeit von zwei bis fünf Minuten kommen, wenn Braze eine Verbindung zu Classic- und Pro-SQL-Instanzen herstellt, was zu Verzögerungen beim Verbindungsaufbau und beim Testen sowie bei der Erstellung und Aktualisierung von CDI Segment-Erweiterungen führt. Die Verwendung einer serverlosen SQL-Instanz minimiert die Aufwärmzeit und verbessert den Abfragedurchsatz, kann aber zu etwas höheren Integrationskosten führen.
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. Erstellen Sie einen Dienst-Prinzipal und erlauben Sie den Zugriff auf den Fabric Workspace, der für Ihre Integration verwendet werden soll.   
2. Richten Sie in Ihrem Fabric Workspace die Quelldaten ein und erteilen Sie Ihrem Dienst-Principal Berechtigungen 
3. Erstellen Sie eine neue verbundene Quelle im Braze Dashboard.
4. Testen Sie die Integration.
5. Verwenden Sie die verbundene Quelle, um eine oder mehrere CDI Segment-Erweiterungen zu erstellen.
{% endtab %}

{% endtabs %}

### Schritt 2: Richten Sie Ihr Data Warehouse ein

Richten Sie die Quelldaten und die erforderlichen Ressourcen in Ihrer Data Warehouse-Umgebung ein. Die verbundene Quelle kann auf eine oder mehrere Tabellen verweisen. Vergewissern Sie sich also, dass Ihr Braze-Benutzer die Berechtigung hat, auf alle Tabellen zuzugreifen, die Sie in der verbundenen Quelle haben möchten.

{% tabs %}
{% tab Snowflake %}
#### Schritt 2.1: Eine Rolle erstellen und Berechtigungen erteilen

Erstellen Sie eine Rolle, die Ihre verbundene Quelle verwenden soll. Diese Rolle wird verwendet, um die Liste der in Ihren CDI Segment-Erweiterungen verfügbaren Tabellen zu generieren und um Quelltabellen abzufragen, um neue Segmente zu erstellen. Nachdem die verbundene Quelle erstellt wurde, ermittelt Braze die Namen und Beschreibungen aller Tabellen, die dem Nutzer:innen im Quellschema zur Verfügung stehen.

Sie können wählen, ob Sie Zugriff auf alle Tabellen in einem Schema gewähren oder nur auf bestimmte Tabellen. Die Tabellen, auf die die Braze-Rolle Zugriff hat, stehen für die Abfrage in der CDI Segment-Erweiterung zur Verfügung.

Die Berechtigung `create table` ist erforderlich, damit Braze eine Tabelle mit den Abfrageergebnissen Ihrer CDI Segment-Erweiterung erstellen kann, bevor das Segment in Braze aktualisiert wird. Braze erstellt eine temporäre Tabelle pro Segment, die nur persistent ist, solange Braze das Segment aktualisiert.

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT CREATE TABLE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to all current and future tables or views in the schema
GRANT SELECT ON ALL TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to specific tables or views in the schema
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;

```

#### Schritt 2.2: Richten Sie das Lager ein und geben Sie der Rolle Braze Zugriff

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
Das Lagerhaus muss die Option zur **automatischen Wiederaufnahme** aktiviert haben. Wenn dies nicht der Fall ist, müssen Sie Braze zusätzliche `OPERATE` Privilegien für das Warehouse erteilen, damit Braze es aktiviert, wenn es Zeit ist, die Abfrage auszuführen.
{% endalert %}

#### Schritt 2.3: Einrichten der Nutzer:in
```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Sie teilen die Verbindungsinformationen mit Braze und erhalten einen öffentlichen Schlüssel, den Sie in einem späteren Schritt an die Nutzer:innen anhängen.

{% alert note %}
Wenn Sie verschiedene Arbeitsbereiche mit demselben Snowflake-Konto verbinden, müssen Sie für jeden Braze-Arbeitsbereich, in dem Sie eine Integration erstellen, einen eigenen Benutzer anlegen. Innerhalb eines Arbeitsbereichs können Sie denselben Benutzer für verschiedene Integrationen wiederverwenden. Die Erstellung einer Integration schlägt jedoch fehl, wenn ein Benutzer mit demselben Snowflake-Konto in verschiedenen Arbeitsbereichen dupliziert wird.
{% endalert %}

#### Schritt 2.4: Zulassen von Braze IPs in Ihrer Snowflake Netzwerkrichtlinie (optional)

Je nach Konfiguration Ihres Snowflake-Kontos müssen Sie die folgenden IP-Adressen in Ihrer Snowflake-Netzwerkrichtlinie zulassen. Weitere Informationen hierzu finden Sie in der entsprechenden Snowflake Dokumentation zur [Änderung einer Netzwerkrichtlinie](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies).

{% multi_lang_include data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### Schritt 2.1: Nutzer:in anlegen und Berechtigungen erteilen 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Erstellen Sie einen Nutzer:in für Ihre verbundene Quelle, die Sie verwenden möchten. Dieser Nutzer:innen wird verwendet, um die Liste der in Ihren CDI Segment-Erweiterungen verfügbaren Tabellen zu generieren und die Quelltabellen abzufragen, um neue Segmente zu erstellen. Nachdem die verbundene Quelle erstellt wurde, ermittelt Braze die Namen und Beschreibungen aller Tabellen, die dem Nutzer:innen im Quellschema zur Verfügung stehen. Wenn Sie mehrere CDI-Integrationen erstellen, möchten Sie möglicherweise Berechtigungen für ein Schema erteilen oder Berechtigungen über eine Gruppe verwalten. 

Sie können wählen, ob Sie Zugriff auf alle Tabellen in einem Schema gewähren oder nur auf bestimmte Tabellen. Die Tabellen, auf die die Braze-Rolle Zugriff hat, stehen für die Abfrage in der CDI Segment-Erweiterung zur Verfügung. Stellen Sie sicher, dass Sie dem Benutzer bei der Erstellung neuer Tabellen Zugriff auf diese gewähren, oder legen Sie Standardberechtigungen für den Benutzer fest. 

Die Berechtigung `create table` ist erforderlich, damit Braze eine Tabelle mit den Abfrageergebnissen Ihrer CDI Segment-Erweiterung erstellen kann, bevor das Segment in Braze aktualisiert wird. Braze erstellt eine temporäre Tabelle pro Segment, die nur persistent ist, solange Braze das Segment aktualisiert.


#### Schritt 2.2: Zugriff auf Braze-IPs zulassen    

Wenn Sie eine Firewall oder andere Netzwerkrichtlinien haben, müssen Sie Braze Netzwerkzugriff auf Ihre Redshift-Instanz gewähren. Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze Dashboards entsprechen. 

Möglicherweise müssen Sie auch Ihre Sicherheitsgruppen ändern, um Braze den Zugriff auf Ihre Daten in Redshift zu ermöglichen. Stellen Sie sicher, dass Sie eingehenden Datenverkehr auf den unten aufgeführten IPs und auf dem Port, der für die Abfrage Ihres Redshift-Clusters verwendet wird (Standard ist 5439), ausdrücklich zulassen. Sie sollten Redshift TCP-Konnektivität auf diesem Port explizit erlauben, auch wenn die eingehenden Regeln auf "alles erlauben" eingestellt sind. Darüber hinaus ist es wichtig, dass der Endpunkt für den Redshift-Cluster öffentlich zugänglich ist, damit Braze eine Verbindung zu Ihrem Cluster herstellen kann.

Wenn Sie nicht möchten, dass Ihr Redshift-Cluster öffentlich zugänglich ist, können Sie eine VPC und eine EC2-Instanz einrichten, die einen ssh-Tunnel für den Zugriff auf die Redshift-Daten verwenden. Weitere Informationen finden Sie unter [AWS: Wie greife ich von meinem lokalen Rechner aus auf einen privaten Amazon Redshift-Cluster zu?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### Schritt 2.1: Dienstkonto erstellen und Berechtigungen erteilen 

Erstellen Sie ein Service-Konto in GCP, über das Braze eine Verbindung herstellen und Daten aus Ihrer(n) Tabelle(n) lesen kann. Das Konto für den Dienst sollte über die folgenden Berechtigungen verfügen: 

- **Nutzer:in der BigQuery-Verbindung:** Ermöglicht es Braze, Verbindungen herzustellen.
- **BigQuery-Nutzer:innen:** Ermöglicht den Zugriff auf Braze, um Abfragen auszuführen, Metadaten von Datensätzen zu lesen und Tabellen aufzulisten.
- **BigQuery Daten Betrachter:** Ermöglicht den Zugriff auf Braze, um Datensätze und deren Inhalte anzuzeigen.
- **Nutzer:in von BigQuery-Jobs:** Ermöglicht den Zugriff auf Braze zur Ausführung von Aufträgen.
- **bigquery.tables.create** Ermöglicht den Zugriff auf Braze, um temporäre Tabellen während der Segmentierung zu erstellen.

Erstellen Sie ein Dienst-Konto für die Nutzung Ihrer verbundenen Quelle. Dieser Nutzer:innen wird verwendet, um die Liste der in Ihren CDI Segment-Erweiterungen verfügbaren Tabellen zu generieren und die Quelltabellen abzufragen, um neue Segmente zu erstellen. Nachdem die verbundene Quelle erstellt wurde, ermittelt Braze die Namen und Beschreibungen aller Tabellen, die dem Nutzer:innen im Quellschema zur Verfügung stehen. 

Sie können wählen, ob Sie den Zugriff auf alle Tabellen in einem Datensatz gewähren wollen oder ob Sie nur für bestimmte Tabellen Zugriffsrechte gewähren wollen. Die Tabellen, auf die die Braze-Rolle Zugriff hat, stehen für die Abfrage in der CDI Segment-Erweiterung zur Verfügung. 

Die Berechtigung `create table` ist erforderlich, damit Braze eine Tabelle mit den Abfrageergebnissen Ihrer CDI Segment-Erweiterung erstellen kann, bevor das Segment in Braze aktualisiert wird. Braze erstellt eine temporäre Tabelle pro Segment, die nur persistent ist, solange Braze das Segment aktualisiert. 

Wenn Sie das Dienstkonto erstellt und die Berechtigungen erteilt haben, erzeugen Sie einen JSON-Schlüssel. Weitere Informationen finden Sie unter [Google Cloud: Schlüssel für Dienstkonten erstellen und löschen](https://cloud.google.com/iam/docs/keys-create-delete). Sie laden dies später auf das Braze Dashboard hoch.

#### Schritt 2.2: Zugriff auf Braze-IPs zulassen    

Wenn Sie über Netzwerkrichtlinien verfügen, müssen Sie Braze Netzwerkzugriff auf Ihre Big Query-Instanz gewähren. Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze Dashboards entsprechen.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### Schritt 2.1: Erstellen Sie ein Token für den Zugriff  

Damit Braze auf Databricks zugreifen kann, muss ein persönliches Token für den Zugriff erstellt werden.

1. Wählen Sie in Ihrem Databricks Workspace Ihren Databricks-Benutzernamen in der oberen Leiste aus und wählen Sie dann **Benutzer:in** aus dem Dropdown-Menü.
2. Vergewissern Sie sich, dass das Konto des Dienstes über die Rechte `CREATE TABLE` für das Schema verfügt, das für die verbundene Quelle verwendet wird. 
3. Wählen Sie auf der Registerkarte **Zugriffstoken** die Option **Neues Token generieren**.
4. Geben Sie einen Kommentar ein, der Ihnen hilft, dieses Token zu identifizieren, z. B. „Braze-CDI“, und ändern Sie die Lebensdauer des Tokens auf „keine Lebensdauer“, indem Sie das Feld „Lebensdauer (Tage)“ leer lassen.
5. Wählen Sie **Erzeugen**.
6. Kopieren Sie das angezeigte Token, und wählen Sie dann **Fertig**.

Dieses Token wird verwendet, um die Liste der Tabellen zu generieren, die in Ihren CDI Segment-Erweiterungen verfügbar sind, und um Quelltabellen abzufragen, um neue Segmente zu erstellen. Nachdem die verbundene Quelle erstellt wurde, ermittelt Braze die Namen und Beschreibungen aller Tabellen, die dem Nutzer:innen im Quellschema zur Verfügung stehen. 

Sie können wählen, ob Sie Zugriff auf alle Tabellen in einem Schema gewähren oder nur auf bestimmte Tabellen. Die Tabellen, auf die die Braze-Rolle Zugriff hat, stehen für die Abfrage in der CDI Segment-Erweiterung zur Verfügung.

Die Berechtigung `create table` ist erforderlich, damit Braze eine Tabelle mit den Abfrageergebnissen Ihrer CDI Segment-Erweiterung erstellen kann, bevor das Segment in Braze aktualisiert wird. Braze erstellt eine temporäre Tabelle pro Segment, die nur persistent ist, solange Braze das Segment aktualisiert. 

Bewahren Sie das Token an einem sicheren Ort auf, bis Sie es im Braze-Dashboard während des Schritts zur Erstellung der Zugangsdaten eingeben müssen.

#### Schritt 2.2: Zugriff auf Braze-IPs zulassen    

Wenn Sie Netzwerkrichtlinien aufgestellt haben, müssen Sie Braze Netzwerkzugriff auf Ihre Databricks-Instanz gewähren. Erlauben Sie den Zugriff von den folgenden IPs, die der Region Ihres Braze Dashboards entsprechen.  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### Schritt 2.1: Zugang zu Fabric-Ressourcen gewähren 
Braze stellt die Verbindung zu Ihrem Fabric-Warehouse über einen Dienstprinzipal mit Entra ID-Authentifizierung her. Sie erstellen einen neuen Dienstprinzipal, den Braze verwenden kann, und gewähren bei Bedarf Zugriff auf Fabric-Ressourcen. Braze benötigt für die Verbindung die folgenden Angaben:    

* Tenant ID (auch Verzeichnis genannt) für Ihr Azure-Konto 
* Principal ID (auch Anwendungs-ID genannt) für den Auftraggeber des Dienstes 
* Client-Geheimnis für Braze zur Authentifizierung

1. Navigieren Sie im Azure-Portal zum Microsoft Entra Admin Center und dann zu **App-Registrierungen**.
2. Wählen Sie **\+ Neue Registrierung** unter **Identität > Anwendungen > App-Registrierungen** 
3. Geben Sie einen Namen ein und wählen Sie `Accounts in this organizational directory only` als unterstützten Kontotyp aus. Wählen Sie dann **Registrieren**. 
4. Wählen Sie die Anwendung (Dienstprinzipal) aus, die Sie gerade erstellt haben, und navigieren Sie dann zu **Zertifikate & secrets > + New client secret**
5. Geben Sie eine Beschreibung für das Geheimnis ein und legen Sie einen Ablauf für das Geheimnis fest. Wählen Sie dann **Hinzufügen**. 
6. Notieren Sie sich das Client-Geheimnis, das Sie bei der Einrichtung von Braze verwenden. 

{% alert note %}
Azure erlaubt keinen unbegrenzten Ablauf von Dienst-Prinzipalgeheimnissen. Denken Sie daran, die Zugangsdaten zu aktualisieren, bevor sie ablaufen, damit der Datenfluss zu Braze aufrechterhalten wird.
{% endalert %}

#### Schritt 2.2: Zugang zu Fabric-Ressourcen gewähren 
Sie werden Braze den Zugang zu Ihrer Fabric-Instanz ermöglichen. Navigieren Sie in Ihrem Fabric-Administrationsportal zu **Einstellungen** > **Governance und Insights** > **Admin-Portal** > **Tenant-Einstellungen**.    

* Aktivieren Sie in den **Einstellungen für Entwickler:innen** die Option „Dienstprinzipale können Fabric-APIs verwenden“, damit Braze sich über die Microsoft Entra-ID verbinden kann.
* Aktivieren Sie in den **OneLake-Einstellungen** "Nutzer:innen können mit Apps außerhalb von Fabric auf in OneLake gespeicherte Daten zugreifen", damit der Dienstherr auf Daten aus einer externen App zugreifen kann.

#### Schritt 2.3: Warehouse Connection String abrufen 

Sie benötigen den SQL-Endpunkt für Ihr Warehouse, damit Braze eine Verbindung herstellen kann. Um den SQL-Endpunkt abzurufen, rufen Sie den **Arbeitsbereich** in Fabric auf. Bewegen Sie den Mauszeiger in der Liste der Elemente auf den Namen des Warehouse und wählen Sie **SQL-Verbindungszeichenfolge kopieren**.

![Die Seite "Fabric Console" in Microsoft Azure, auf der Nutzer:innen den SQL Connection String abrufen sollten.]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})

#### Schritt 2.4: Zulassen von Braze IPs in der Firewall (Optional)

Je nach Konfiguration Ihres Microsoft Fabric-Kontos müssen Sie möglicherweise die folgenden IP-Adressen in Ihrer Firewall zulassen, um den Datenverkehr von Braze zuzulassen. Weitere Informationen zum Enablement finden Sie in der entsprechenden Dokumentation zu [Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access).

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### Schritt 3: Erstellen Sie eine verbundene Quelle im Braze Dashboard

{% tabs %}
{% tab Snowflake %}
#### Schritt 3.1: Snowflake-Verbindungsinformationen und Quelltabelle hinzufügen

Erstellen Sie eine verbundene Quelle im Braze Dashboard. Gehen Sie zu **Dateneinstellungen** > **Cloud Data Ingestion** > **Verbundene Quellen** und wählen Sie dann **Neue Datensynchronisation erstellen** > **Snowflake Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Geben Sie die Informationen für Ihr Snowflake Data Warehouse und das Quellschema ein und fahren Sie dann mit dem nächsten Schritt fort.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### Schritt 3.2: Synchronisierungsdetails konfigurieren

Wählen Sie einen Namen für die verbundene Quelle. Dieser Name wird in der Liste der verfügbaren Quellen verwendet, wenn Sie eine neue CDI Segment-Erweiterung erstellen. 

Legen Sie eine maximale Laufzeit für diese Quelle fest. Braze bricht automatisch alle Abfragen ab, die die maximale Laufzeit überschreiten, wenn es ein Segment erstellt oder aktualisiert. Die maximal zulässige Laufzeit beträgt 60 Minuten; eine geringere Laufzeit reduziert die Kosten für Ihr Snowflake-Konto. 

{% alert note %}
Wenn Abfragen immer wieder ins Stocken geraten und Sie eine maximale Laufzeit von 60 Minuten festgelegt haben, sollten Sie versuchen, die Ausführungszeit Ihrer Abfragen zu optimieren oder dem Braze-Benutzer ein größeres Warehouse zuzuweisen.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### Schritt 3.3: Notieren Sie sich den Public Key  

Notieren Sie sich im Schritt **Verbindung testen** den öffentlichen RSA-Schlüssel. Sie benötigen sie, um die Integration in Snowflake abzuschließen.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% tab Redshift %}
#### Schritt 3.1: Redshift-Verbindungsinformationen und Quelltabelle hinzufügen

Erstellen Sie eine verbundene Quelle im Braze Dashboard. Gehen Sie zu **Dateneinstellungen** > **Cloud Data Ingestion** > **Verbundene Quellen**, und wählen Sie dann **Datenverbindung erstellen** > **Amazon Redshift Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Geben Sie die Informationen für Ihr Redshift Data Warehouse und das Quellschema ein und fahren Sie dann mit dem nächsten Schritt fort.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_1.png %})

#### Schritt 3.2: Synchronisierungsdetails konfigurieren

Wählen Sie einen Namen für die verbundene Quelle. Dieser Name wird in der Liste der verfügbaren Quellen verwendet, wenn Sie eine neue CDI Segment-Erweiterung erstellen. 

Legen Sie eine maximale Laufzeit für diese Quelle fest. Braze bricht automatisch alle Abfragen ab, die die maximale Laufzeit überschreiten, wenn es ein Segment erstellt oder aktualisiert. Die maximal zulässige Laufzeit beträgt 60 Minuten. Eine geringere Laufzeit reduziert die Kosten, die für Ihr Redshift-Konto anfallen. 

{% alert note %}
Wenn Abfragen immer wieder ins Stocken geraten und Sie eine maximale Laufzeit von 60 Minuten festgelegt haben, sollten Sie versuchen, die Ausführungszeit Ihrer Abfragen zu optimieren oder dem Braze-Benutzer ein größeres Warehouse zuzuweisen.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_2.png %})

#### Schritt 3.3: Notieren Sie sich den Public Key (optional)

Wenn in Ihren Anmeldeinformationen die Option **Mit SSH-Tunnel verbinden** ausgewählt ist, beachten Sie den öffentlichen RSA-Schlüssel im Schritt **Verbindung testen**. Sie benötigen sie, um die Integration in Redshift abzuschließen.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_3.png %})

{% endtab %}
{% tab BigQuery %}
#### Schritt 3.1: BigQuery-Verbindungsinformationen und Quelltabelle hinzufügen

Erstellen Sie eine verbundene Quelle im Braze Dashboard. Gehen Sie zu **Dateneinstellungen** > **Cloud Data Ingestion** > **Verbundene Quellen** und wählen Sie dann **Neue Datensynchronisation erstellen** > **Google BigQuery Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Geben Sie die Informationen für Ihr BigQuery-Projekt und Ihren Datensatz ein und fahren Sie dann mit dem nächsten Schritt fort.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_1.png %})

#### Schritt 3.2: Synchronisierungsdetails konfigurieren

Wählen Sie einen Namen für die verbundene Quelle. Dieser Name wird in der Liste der verfügbaren Quellen verwendet, wenn Sie eine neue CDI Segment-Erweiterung erstellen. 

Legen Sie eine maximale Laufzeit für diese Quelle fest. Braze bricht automatisch alle Abfragen ab, die die maximale Laufzeit überschreiten, wenn es ein Segment erstellt oder aktualisiert. Die maximal zulässige Laufzeit beträgt 60 Minuten; eine geringere Laufzeit reduziert die Kosten, die für Ihr BigQuery-Konto anfallen. 

{% alert note %}
Wenn Abfragen immer wieder ins Stocken geraten und Sie eine maximale Laufzeit von 60 Minuten festgelegt haben, sollten Sie versuchen, die Ausführungszeit Ihrer Abfragen zu optimieren oder dem Braze-Benutzer ein größeres Warehouse zuzuweisen.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_2.png %})

#### Schritt 3.3: Testen Sie die Verbindung

Wählen Sie **Verbindung testen**, um zu überprüfen, ob die Liste der für den Benutzer sichtbaren Tabellen Ihren Erwartungen entspricht, und wählen Sie dann **Fertig**. Ihre verbundene Quelle ist nun erstellt und kann in CDI Segment-Erweiterungen verwendet werden.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Databricks %}
#### Schritt 3.1: Databricks-Verbindungsinformationen und Quelltabelle hinzufügen

Erstellen Sie eine verbundene Quelle im Braze Dashboard. Gehen Sie zu **Dateneinstellungen** > **Cloud Data Ingestion** > **Verbundene Quellen** und wählen Sie dann **Neue Datensynchronisation erstellen** > **Databricks Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Geben Sie die Informationen für Ihre Databricks-Zugangsdaten und, optional, den Katalog und das Quellschema ein und fahren Sie dann mit dem nächsten Schritt fort.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_databricks_1.png %})

#### Schritt 3.2: Synchronisierungsdetails konfigurieren

Wählen Sie einen Namen für die verbundene Quelle. Dieser Name wird in der Liste der verfügbaren Quellen verwendet, wenn Sie eine neue CDI Segment-Erweiterung erstellen. 

Legen Sie eine maximale Laufzeit für diese Quelle fest. Braze bricht automatisch alle Abfragen ab, die die maximale Laufzeit überschreiten, wenn es ein Segment erstellt oder aktualisiert. Die maximal zulässige Laufzeit beträgt 60 Minuten; eine geringere Laufzeit reduziert die Kosten, die für Ihr Databricks-Konto anfallen. 

{% alert note %}
Wenn Abfragen immer wieder ins Stocken geraten und Sie eine maximale Laufzeit von 60 Minuten festgelegt haben, sollten Sie versuchen, die Ausführungszeit Ihrer Abfragen zu optimieren oder dem Braze-Benutzer ein größeres Warehouse zuzuweisen.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_db_2.png %})

#### Schritt 3.3: Testen Sie die Verbindung

Wählen Sie **Verbindung testen**, um zu überprüfen, ob die Liste der für den Benutzer sichtbaren Tabellen Ihren Erwartungen entspricht, und wählen Sie dann **Fertig**. Ihre verbundene Quelle ist nun erstellt und kann in CDI Segment-Erweiterungen verwendet werden.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Microsoft Fabric %}
#### Schritt 3.1: Microsoft Fabric-Verbindungsinformationen und Quelltabelle hinzufügen

Erstellen Sie eine verbundene Quelle im Braze Dashboard. Gehen Sie zu **Dateneinstellungen** > **Cloud Data Ingestion** > **Verbundene Quellen** und wählen Sie dann **Neue Datensynchronisation erstellen** > **Microsoft Fabric Import**.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Geben Sie die Informationen für Ihre Microsoft Fabric Zugangsdaten sowie das Quell-Warehouse und das Schema ein und fahren Sie mit dem nächsten Schritt fort.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_1.png %})

#### Schritt 3.2: Synchronisierungsdetails konfigurieren

Wählen Sie einen Namen für die verbundene Quelle. Dieser Name wird in der Liste der verfügbaren Quellen verwendet, wenn Sie eine neue CDI Segment-Erweiterung erstellen. 

Legen Sie eine maximale Laufzeit für diese Quelle fest. Braze bricht automatisch alle Abfragen ab, die die maximale Laufzeit überschreiten, wenn es ein Segment erstellt oder aktualisiert. Die maximal zulässige Laufzeit beträgt 60 Minuten; eine geringere Laufzeit reduziert die Kosten, die für Ihr Microsoft Fabric-Konto anfallen. 

{% alert note %}
Wenn Abfragen immer wieder zeitlich begrenzt sind und Sie eine maximale Laufzeit von 60 Minuten festgelegt haben, sollten Sie versuchen, die Ausführungszeit der Abfrage zu optimieren oder die Kapazität der Fabric zu skalieren.
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_2.png %})

#### Schritt 3.3: Testen Sie die Verbindung

Wählen Sie **Verbindung testen**, um zu überprüfen, ob die Liste der für den Benutzer sichtbaren Tabellen Ihren Erwartungen entspricht, und wählen Sie dann **Fertig**. Ihre verbundene Quelle ist nun erstellt und kann in CDI Segment-Erweiterungen verwendet werden.

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% endtabs %}

### Schritt 4: Schließen Sie die Konfiguration des Data Warehouse ab

{% tabs %}
{% tab Snowflake %}
Fügen Sie den Public Key, den Sie im letzten Schritt notiert haben, zu Ihren Nutzer:innen in Snowflake hinzu. Dadurch kann Braze eine Verbindung zu Snowflake herstellen. Einzelheiten dazu finden Sie in der [Snowflake-Dokumentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). 

Wenn Sie die Schlüssel irgendwann wechseln möchten, können Sie einen neuen öffentlichen Schlüssel erstellen, indem Sie in der **Datenzugriffsverwaltung** von **Cloud Data Ingestion** die Option **Neuen Schlüssel generieren** für das jeweilige Konto wählen.

![Data Access Management für Snowflake Zugangsdaten, mit einem Button zur Generierung eines neuen Schlüssels.]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_4.png %})

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Nachdem Sie dem Benutzer in Snowflake den Schlüssel hinzugefügt haben, wählen Sie in Braze **Verbindung testen** und dann **Fertig**. Ihre verbundene Quelle ist nun erstellt und kann in CDI Segment-Erweiterungen verwendet werden.
{% endtab %}

{% tab Redshift %}
Wenn Sie eine Verbindung über einen SSH-Tunnel herstellen, fügen Sie den öffentlichen Schlüssel, den Sie im letzten Schritt notiert haben, dem Nutzer:in des SSH-Tunnels hinzu. 

Nachdem Sie dem Benutzer den Schlüssel hinzugefügt haben, wählen Sie in Braze **Verbindung testen** und dann **Fertig**. Ihre verbundene Quelle ist nun erstellt und kann in CDI Segment-Erweiterungen verwendet werden.

{% endtab %}
{% tab BigQuery %}
Dies gilt nicht für BigQuery.

{% endtab %}
{% tab Databricks %}
Dies gilt nicht für Databricks.

{% endtab %}
{% tab Microsoft Fabric %}
Dies gilt nicht für Microsoft Fabric.

{% endtab %}
{% endtabs %}

{% alert note %}
Sie müssen eine Quelle erfolgreich testen, bevor sie vom Status "Entwurf" in den Status "aktiv" übergehen kann. Wenn Sie die Erstellungsseite verlassen müssen, wird Ihre Integration gespeichert, und Sie können die Detailseite erneut aufrufen, um Änderungen vorzunehmen und zu testen.  
{% endalert %}

## Einrichten zusätzlicher Integrationen oder Benutzer (optional)

{% tabs %}
{% tab Snowflake %}
Sie können mehrere Integrationen mit Braze einrichten, aber jede Integration sollte so konfiguriert werden, dass sie ein anderes Schema verbindet. Wenn Sie zusätzliche Verbindungen erstellen, können Sie vorhandene Anmeldedaten wiederverwenden, wenn Sie sich mit demselben Snowflake-Konto verbinden.

Wenn Sie denselben Nutzer:innen und dieselbe Rolle bei verschiedenen Integrationen wiederverwenden, müssen Sie den öffentlichen Schlüssel nicht erneut hinzufügen.
{% endtab %}

{% tab Redshift %}
Sie können mit Braze mehrere Quellen einrichten, aber jede Quelle sollte so konfiguriert werden, dass sie ein anderes Schema verbindet. Wenn Sie zusätzliche Quellen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Redshift-Konto verbinden.
{% endtab %}

{% tab BigQuery %}
Sie können mit Braze mehrere Quellen einrichten, aber jede Quelle sollte so konfiguriert werden, dass sie einen anderen Datensatz verbindet. Wenn Sie zusätzliche Quellen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben BigQuery-Konto verbinden.
{% endtab %}

{% tab Databricks %}
Sie können mit Braze mehrere Quellen einrichten, aber jede Quelle sollte so konfiguriert werden, dass sie ein anderes Schema verbindet. Wenn Sie zusätzliche Quellen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Databricks-Konto verbinden.
{% endtab %}

{% tab Microsoft Fabric %}
Sie können mit Braze mehrere Quellen einrichten, aber jede Quelle sollte so konfiguriert werden, dass sie ein anderes Schema verbindet. Wenn Sie zusätzliche Quellen erstellen, können Sie vorhandene Zugangsdaten wiederverwenden, wenn Sie sich mit demselben Azure-Konto verbinden.
{% endtab %}
{% endtabs %}

## Verwendung der angeschlossenen Quelle

Nachdem die Quelle erstellt wurde, können Sie damit eine oder mehrere CDI Segment-Erweiterungen erstellen. Weitere Informationen zur Erstellung eines Segments mit dieser Quelle finden Sie in der [Dokumentation zu CDI Segment-Erweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

{% alert note %}
Wenn Abfragen immer wieder zu Zeitüberschreitungen führen und Sie eine maximale Laufzeit von 60 Minuten festgelegt haben, sollten Sie versuchen, die Ausführungszeit Ihrer Abfragen zu optimieren oder dem Braze-Benutzer mehr Rechenressourcen (z. B. ein größeres Warehouse) zuzuweisen.
{% endalert %}
