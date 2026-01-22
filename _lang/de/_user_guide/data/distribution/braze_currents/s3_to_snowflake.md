---
nav_title: Übertragen von Daten von Amazon S3 zu Snowflake
article_title: Übertragen von Daten von Amazon S3 zu Snowflake
page_order: 7
page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie mit Hilfe des ETL-Prozesses (Extrahieren, Transformieren, Laden) Daten aus einem Cloud-Speicher (z.B. Amazon S3) in ein Warehouse (z.B. Snowflake) übertragen."
tool: Currents

---

# Übertragen von Daten von Amazon S3 zu Snowflake

> Wenn sich Ihre Daten derzeit in Amazon S3 befinden, können Sie sie mit dem Prozess Extrahieren, Laden, Transformieren (ELT) in Snowflake oder ein anderes relationales Data Warehouse übertragen. Auf dieser Seite erfahren Sie, wie Sie das tun können.

{% alert note %}
Wenn Sie spezifischere Anwendungsfälle haben und möchten, dass Braze für Ihre Currents-Instanz Serviceleistungen erbringt, wenden Sie sich an Ihren Account Manager:in und fragen Sie ihn nach den Braze Data Professional Serviceleistungen; Dienste.
{% endalert %}

## Funktionsweise

Der Prozess Extrahieren, Laden, Transformieren (ELT) ist ein automatisierter Prozess, der Daten in [Snowflake](https://www.snowflake.com/) überträgt, so dass Sie die [Braze Looker Blocks](https://marketplace.looker.com/marketplace/directory) verwenden können, um diese Daten in Looker zu visualisieren und so Einblicke und Feedback für Ihre Kampagnen, Canvases und Segmente zu gewinnen.

Nachdem Sie einen Export von Currents nach S3 eingerichtet haben und Live-Ereignisdaten empfangen, können Sie Ihre Live-ELT-Pipeline in Snowflake konfigurieren, indem Sie die folgenden Komponenten konfigurieren:

-   [AWS SQS-Warteschlangen](#aws-sqs-queues)
-   [Auto-Ingest Snowpipes](#auto-ingest-snowpipes)

## Konfigurieren von AWS SQS-Warteschlangen

**Auto-ingest Snowpipes** verlassen sich auf SQS Warteschlangen, um Benachrichtigungen von S3 an Snowpipe zu senden. Dieser Prozess wird von Snowflake nach der Konfiguration von SQS verwaltet.

### Schritt 1: Konfigurieren Sie die externe S3-Stufe

{% alert note %}
In dieser Phase werden die Tabellen in Ihrer Datenbank erstellt.
{% endalert %}

1. Wenn Sie Currents in Braze einrichten, geben Sie einen Ordnerpfad an, dem Ihre Currents-Dateien in Ihr S3-Bucket folgen sollen. Hier verwenden wir ```currents```, den Standardordnerpfad.

2. Erstellen Sie die folgenden Dateien in der angegebenen Reihenfolge:
  2.1 Erstellen Sie in AWS ein neues **Public-Private-Key-Paar** für das gewünschte S3-Bucket, mit Berechtigungen gemäß den Sicherheitsanforderungen Ihres Unternehmens.
  2.2. Erstellen Sie in Snowflake eine Datenbank und ein Schema Ihrer Wahl (im folgenden Beispiel ```currents``` und ```public``` genannt).
  2.3. Erstellen Sie eine Snowflake S3 Stage (genannt `braze_data`):

```sql
CREATE OR REPLACE STAGE
    currents.public.braze_data
    url='s3://snowpipe-demo/'
    credentials = (AWS_KEY_ID = '...' AWS_SECRET_KEY = '...' );
show stages;
```

{: start="3"}
3\. Definieren Sie das AVRO-Dateiformat für Ihre Bühne.

```sql
CREATE FILE FORMAT
    currents.public.currents_avro
    type = 'avro'
    compression = 'auto';
```

```sql
ALTER STAGE
    currents.public.braze_data
SET
    file_format = currents.public.currents_avro;
```

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_pushnotification_open
    auto_ingest=true AS

COPY INTO
  users_messages_pushnotification_open
          FROM
           (SELECT
             $1:id::STRING,
             $1:user_id::STRING,
             $1:external_user_id::STRING,
              $1:time::INT,
              $1:timezone::STRING,
              $1:app_id::STRING,
              $1:campaign_id::STRING,
              $1:campaign_name::STRING,
              $1:message_variation_id::STRING,
              $1:canvas_id::STRING,
              $1:canvas_name::STRING,
              $1:canvas_variation_id::STRING,
              $1:canvas_step_id::STRING,
              $1:canvas_step_message_variation_id::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING,
              $1:send_id::STRING,
              $1:device_id::STRING,
              $1:button_action_type::STRING,
              $1:button_string::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
```

{: start="4"}
4\. Verwenden Sie schließlich den Befehl `show pipes;`, um Ihre SQS-Informationen anzuzeigen. Der Name der SQS-Warteschlange wird in einer neuen Spalte mit der Bezeichnung `NOTIFICATION_CHANNEL` angezeigt, da diese Pipe als Auto-Test-Pipe erstellt wurde.

### Schritt 2: Bucket-Ereignisse erstellen

1. Navigieren Sie in AWS zu dem entsprechenden Bucket der neuen Snowflake-Stufe. Gehen Sie dann auf der Registerkarte **Eigenschaften** auf **Ereignisse**.

![AWS Eigenschaften Tab]({% image_buster /assets/img/aws-properties.png %}){: height="50%" width="50%"}

{: start="2"}
2\. Erstellen Sie je nach Bedarf neue Ereignisse für jeden Satz von Currents-Daten[(Messaging]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), [Nutzer:innen]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)) oder für beide.

![Erstellen eines neuen Ereignisses in AWS]({% image_buster /assets/img/aws-events.png %}){: height="50%" width="50%"}

{: start="3"}
3\. Markieren Sie das entsprechende Kästchen für das Objekt, das die Benachrichtigungen erstellen soll, sowie den ARN am unteren Rand des Formulars (aus der Spalte Benachrichtigungskanal in Snowflake).

## Konfigurieren des automatischen Tests von Snowpipes {#auto-ingest-snowpipes}

Damit die AWS SQS-Konfiguration die richtigen Tabellen erzeugt, müssen Sie die Struktur der eingehenden Daten richtig definieren, indem Sie die folgenden Beispiele und Schemata verwenden, die in unserer Currents-Dokumentation für [Message Engagement oder Messaging Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), [User oder Customer Behavior Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) oder beides festgelegt sind.

Es ist wichtig, dass Sie Ihre Tabellen in Übereinstimmung mit den Schemata von Braze Currents strukturieren, da Braze Currents kontinuierlich Daten über bestimmte Felder mit bestimmten Datentypen in diese Tabellen lädt. Zum Beispiel wird eine `user_id` als String geladen und in Currents Daten als `user_id` bezeichnet.

{% alert note %}
  Je nach Currents-Integration gibt es verschiedene Events, die Sie einrichten müssen (z.B. [Nachrichten-Engagement oder Messaging-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) und [Nutzer:innen- oder Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)). Sie können auch ein Skript für einige oder alle dieser Vorgänge schreiben.
{% endalert %}

{% tabs %}
  {% tab User Behavior Events %}

1. Erstellen Sie eine Tabelle `INTO`, die wir kontinuierlich mit der folgenden Struktur aus dem Currents-Schema laden werden:

```sql
CREATE TABLE
  users_behaviors_app_firstsession (
        id               STRING,
        user_id          STRING,
        external_user_id STRING,
        app_id           STRING,
        time             INT,
        session_id       STRING,
        gender           STRING,
        country          STRING,
        timezone         STRING,
        language         STRING,
        device_id        STRING,
        sdk_version      STRING,
        platform         STRING,
        os_version       STRING,
        device_model     STRING
    );
```

{: start="2"}
2\. Erstellen Sie die Pipe `auto_ingest` und geben Sie an:
  2.1. Welcher Tisch geladen werden soll
  2.2 Wie Sie die folgende Tabelle laden

```sql
CREATE OR REPLACE PIPE
  pipe_users_behaviors_app_firstsession
    auto_ingest=true AS

COPY INTO
  users_behaviors_app_firstsession
          FROM
            (SELECT
              $1:id::STRING,
              $1:user_id::STRING,
              $1:external_user_id::STRING,
              $1:app_id::STRING,
              $1:time::INT,
              $1:session_id::STRING,
              $1:gender::STRING,
              $1:country::STRING,
              $1:timezone::STRING,
              $1:language::STRING,
              $1:device_id::STRING,
              $1:sdk_version::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.behaviors.app.FirstSession/);
```

{% alert warning %}
Sie müssen die Befehle `CREATE TABLE` und `CREATE PIPE` für jeden Ereignistyp wiederholen.
{% endalert %}

 {% endtab %}
 {% tab Messaging Events %}

1. Erstellen Sie eine Tabelle `INTO`, die wir kontinuierlich mit der folgenden Struktur aus dem Currents-Schema laden werden:

```sql
CREATE TABLE
    public_users_messages_pushnotification_open (
        id STRING,
        user_id STRING,
        external_user_id STRING,
        time INT,
        timezone STRING,
        app_id STRING,
        campaign_id STRING,
        campaign_name STRING,
        message_variation_id STRING,
        canvas_id STRING,
        canvas_name STRING,
        canvas_variation_id STRING,
        canvas_step_id STRING,
        canvas_step_message_variation_id STRING,
        platform STRING,
        os_version STRING,
        device_model STRING,
        send_id STRING,
        device_id STRING,
        button_action_type STRING,
        button_string STRING
        );
```

{: start="2"}
2\. Erstellen Sie die AUTO-Dauerlastleitung und geben Sie an:
  2.1. Welcher Tisch geladen werden soll
  2.2 Wie Sie die folgende Tabelle laden

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_pushnotification_open
    auto_ingest=true AS

COPY INTO
  users_messages_pushnotification_open
          FROM
           (SELECT
             $1:id::STRING,
             $1:user_id::STRING,
             $1:external_user_id::STRING,
              $1:time::INT,
              $1:timezone::STRING,
              $1:app_id::STRING,
              $1:campaign_id::STRING,
              $1:campaign_name::STRING,
              $1:message_variation_id::STRING,
              $1:canvas_id::STRING,
              $1:canvas_name::STRING,
              $1:canvas_variation_id::STRING,
              $1:canvas_step_id::STRING,
              $1:canvas_step_message_variation_id::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING,
              $1:send_id::STRING,
              $1:device_id::STRING,
              $1:button_action_type::STRING,
              $1:button_string::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
```

{% alert warning %}
Sie müssen die Befehle `CREATE TABLE` und `CREATE PIPE` für jeden Ereignistyp wiederholen.
{% endalert %}

  {% endtab %}
{% endtabs %}

Um zu sehen, welche Arten von Analytics Sie mit Braze-Currents durchführen können, konsultieren Sie unsere [Looker Blocks](https://github.com/llooker?q=braze).

{% alert note %}
Wenden Sie sich an Ihren Braze-Kundenbetreuer, wenn Sie Fragen haben oder wenn Sie daran interessiert sind, dass Braze Sie durch diesen Prozess begleitet.
{% endalert %}

