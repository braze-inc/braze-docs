---
nav_title: LiveRamp
article_title: LiveRamp
description: "Erfahren Sie, wie Sie LiveRamp, Snowflake und Braze miteinander verbinden können, damit Sie hoch personalisierte und relevante Kampagnen erstellen können."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# Verbinden von LiveRamp, Snowflake und Braze

> Erfahren Sie, wie Sie LiveRamp, Snowflake und Braze miteinander verbinden können, um hochgradig personalisierte und relevante Kampagnen zu erstellen, indem Sie die Zeit bis zu Insights verkürzen, Datensilos aufbrechen und das Customer-Engagement optimieren. Die Integration verbessert das datengesteuerte Marketing, indem sie verwertbare personenbezogene Erkenntnisse liefert und Verbraucherkontakte konsolidiert, um eine bessere Zielgruppensegmentierung und zeitnahe Kampagnen zu ermöglichen. Außerdem nutzt es die von Snowflake bereitgestellten Benchmarks, um Ihre Marketing Strategien im Vergleich zu Branchenstandards zu verfeinern.

{% alert important %}
Die [sichere Datenfreigabe](https://docs.snowflake.com/en/user-guide/data-sharing-intro) von Snowflake überträgt keine Daten zwischen LiveRamp, Snowflake und Braze. Daten werden nur über die Dienste und den Shop von Snowflake ausgetauscht, d.h. es werden keine Daten kopiert und es fallen keine zusätzlichen Speichergebühren an. Der Zugriff auf gemeinsam genutzte Daten wird über die Zugriffskontrollen Ihres Snowflake-Kontos gesteuert und geregelt.
{% endalert %}

## Anwendungsfälle

- **Minimierung der Daten:** Die Aktivierungs-App von LiveRamp nutzt das Feature Secure Data Share von Snowflake, um die Tabellen direkt von Ihrer Instanz zu lesen. Bis zum Zeitpunkt der Zustellung an den nachgelagerten Partner werden keine Daten von Snowflake verschoben.
- **Sichere 1st-Party-Aktivierung:** Durch die Verwendung der oben genannten Anwendung zur Identitätsauflösung wird die Aktivierungsanwendung von LiveRamp nur die RampID-basierten Tabellen in Ihrer Snowflake Instanz verwenden, so dass PII niemals Ihre Wände verlassen müssen.
- **Beschleunigen Sie die Zeit zum Leben:** Da die Daten direkt in Ihrer Umgebung in RampID aufgelöst werden, kann die Zustellung an ein Ziel innerhalb weniger Stunden erfolgen - im Gegensatz zu mehreren Tagen bei der herkömmlichen dateibasierten Methode von LiveRamp. So können Sie die Performance Ihrer Kampagnen zeitnah optimieren.
- **Operative Einsparungen:** Ähnlich wie oben beschrieben, sparen Kunden durch den Einsatz des Snowflake Features für die sichere Datenfreigabe Zeit und Geld im Vergleich zur Koordinierung der Übertragung von Daten an LiveRamp oder direkt an ein beliebiges Ziel.

## Voraussetzungen

| Voraussetzung       | Beschreibung                                                                                                                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Snowflake Konto | Sie benötigen ein Snowflake-Konto mit Admin-Rechten.                                                                                                                                      |
| LiveRamp Konto  | Wenden Sie sich an Ihr LiveRamp Account Team oder an [snowflake@liveramp.com](mailto:snowflake@liveramp.com), um die erforderlichen LiveRamp-Anwendungen in Snowflake zu besprechen.                              |
{: .reset-td-br-1 .reset-td-br-2 }

## Einrichten der Integration

### Schritt 1: Anfrage zur Freigabe von Daten bei Braze

Wenden Sie sich zunächst an Ihren Braze Account Manager oder Customer-Success-Manager, um einen Snowflake Data Share Connector für Ihr Braze-Konto zu erwerben. Wenn Sie eine Datenfreigabe anfragen, wird Braze die Freigabe von dem/den Workspace(s) aus bereitstellen, in dem/denen die Freigabe erworben wurde. Nachdem die Freigabe bereitgestellt wurde, sind alle Daten sofort von Ihrer Snowflake Instanz aus in Form einer eingehenden Datenfreigabe zugänglich. Sobald die Freigabe in Ihrer Instanz sichtbar ist, erstellen Sie eine Datenbank aus der Freigabe, damit Sie die Tabellen sehen und abfragen können.

Eine vollständige Anleitung finden Sie in der [Anleitung zur Integration von Snowflake mit Braze]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/).

### Schritt 2: Einrichten der LiveRamp App in Snowflake 

Die Funktionen zur Übersetzung und Identitätsauflösung sind in Snowflake über die native App LiveRamp Identity Resolution and Translation verfügbar, die eine Freigabe für Ihr Konto erstellt und eine Ansicht zur Abfrage des referenzierten Datensatzes in Ihrer eigenen Snowflake-Umgebung öffnet.

Um die native App einzurichten, folgen Sie diesen Schritten in den LiveRamp-Dokumenten: [Einrichten der LiveRamp Native App in Snowflake](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html). Wenn Sie fertig sind, fahren Sie mit dem nächsten Schritt fort.

### Schritt 3: Erstellen Sie eine Datentabelle

{% alert warning %}
Bevor Sie PII-basierte Tabellen vorbereiten, sollten Sie sich mit [dem Datenschutzfilter von LiveRamp](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) vertraut machen, der während der Jobs ausgeführt wird, um sicherzustellen, dass die Attributspalten (Nicht-Bezeichner) in Ihren Eingabetabellen keine zu eindeutigen Werte enthalten. Dies ist entscheidend für die Wahrung der Privatsphäre der Verbraucher:in und die Vermeidung einer erneuten Identifizierung.
{% endalert %}

Als Nächstes erstellen Sie eine Datentabelle mit dem [gewünschten Format](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html), die in der nativen App von LiveRamp aufgerufen wird. Anhand der folgenden Kategorien können Sie feststellen, welche Ihrer Bezeichner für die Auflösung in Frage kommen:

| Bezeichner Typ | Beschreibung  |
|-----------------|--------------|
| Vollständige PII        | Zu den personenbezogenen Daten (PII) gehören der Name, die Postanschrift, die E-Mail und die Telefonnummer des Nutzers:innen. **Hinweis:** Nicht alle Bezeichner sind für jeden Datensatz erforderlich. |
| Nur E-Mail      | Die E-Mail-Adressen der Nutzer:innen, z. B. `alex-lee@email.com`. |
| Gerät          | Dazu gehören Cookies von Drittanbietern, Mobile Advertising IDs (MAIDs), Connected TV IDs (CTV IDs) und RampIDs (aufgelöst in eine Household RampID). |
| CIDs            | Dabei handelt es sich um Bezeichner eines Plattformpartners oder einer mit LiveRamp synchronisierten Identität, wie z.B. Ihre interne Kund:in. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Braze Bezeichner

Die Ereignisprotokolle von Braze enthalten Bezeichner, die Sie in der nativen LiveRamp App verwenden können. Eine vollständige Liste der verfügbaren Bezeichner für jeden Ereignistyp finden Sie in den [Braze Ereignisschemata und Bezeichnern]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt).

| Bezeichner Typ | Beschreibung  |
|-----------------|--------------|
| `AD_ID` | Werbe-IDs, wie `ios_idfa`, `google_ad_id`, `roku_ad_id`, die innerhalb bestimmter Ereignistypen erfasst wurden und in Verbindung mit den Diensten von LiveRamp zur Geräteauflösung verwendet werden können. Standardmäßig werden die IDs für Werbung nicht erfasst. Sie können das Tracking jedoch aktivieren, indem Sie die [Dokumentation von Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default) befolgen. |
| `EMAIL_ADDRESS`   | E-Mail-Adresse, die in Verbindung mit den Diensten von LiveRamp (nur E-Mail) verwendet werden kann |
| `TO_PHONE_NUMBER` | Telefonnummer, die in Verbindung mit den Diensten zur Auflösung von PII von LiveRamp verwendet werden kann. |
| `EXTERNAL_USER_ID` | Die einem Nutzer:innen zugeordnete externe ID, die in Verbindung mit den Diensten von LiveRamp zur Geräteauflösung (CID) verwendet werden kann. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Die Verwendung von Client- oder markenspezifischen angepassten Bezeichnern innerhalb der LiveRamp-Anwendung erfordert eine [Identitätssynchronisierung mit LiveRamp](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html).
{% endalert %}

### Schritt 4: Setzen Sie Ihre Variablen

Als nächstes legen Sie Ihre Variablen für den Auftrag im Arbeitsblatt Ausführungsschritte fest, das in der App enthalten ist. Dazu gehören Details wie die Zieldatenbank, zugehörige Tabellen (Eingabedaten, Metriken, Protokollierung) und die Definition des Namens der Ausgabetabelle. Eine vollständige Übersicht finden Sie unter [LiveRamp: Geben Sie die Variablen](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727) an.

### Schritt 5: Erstellen Sie die Metadatentabelle für die PII-Auflösung

Da Ihre Variablen nun festgelegt sind, erstellen Sie die Metadatentabelle für die PII-Auflösung. Hier finden Sie Einzelheiten zu der Art des auszuführenden Auftrags, basierend auf der Kategorie der beteiligten Bezeichner. Eine vollständige Übersicht finden Sie unter [LiveRamp: Erstellen Sie die Metadatentabelle](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43).

### Schritt 6: Führen Sie den Vorgang der Identitätsauflösung durch

Führen Sie schließlich den Vorgang der Identitätsauflösung durch. Eine vollständige Übersicht finden Sie unter [LiveRamp: Führen Sie die Operation zur Identitätsauflösung durch](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation).

{% tabs local %}
{% tab Beispieleingabe %}
```sql
call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```
{% endtab %}

{% tab Beispiel-Ausgabe %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### Nächste Schritte

Da Ihre Daten nun mit Ihrer eigenen RampID-Kodierung pseudonymisiert sind, haben Sie die Möglichkeit, die RampID-basierten Tabellen an die Managed Activation Application von LiveRamp weiterzugeben, um die Abwicklung mit Ihren wichtigsten Partnern der Werbeplattform zu optimieren. Die Aktivierungsanwendung enthält eine benutzerfreundliche Schnittstelle für die zusätzliche Segmentierung und Auswahl/Konfiguration von nachgelagerten Zielpartnern. Für weitere Details zur Anwendung wenden Sie sich bitte an Ihr LiveRamp Account Team oder an [snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Fehlersuche

{% alert note %}
Wenn Sie spezielle Probleme oder Fragen haben, wenden Sie sich an [martech@liveramp.com](mailto:martech@liveramp.com).
{% endalert %}

### Snowflake Regionen

Derzeit ist diese Anwendung nur für die folgenden Regionen in den USA verfügbar:

  - aws-us-east-1: POA18931
  - aws-us-west-2: FAA28932
  - azure-east-us-2: BL60425

### Datenschutz & Spaltenwerte

Der Prozess wertet die Kombination aller Spaltenwerte für jede Zeile auf eindeutige Werte aus. Wenn eine bestimmte Kombination von Spaltenwerten 3 Mal oder weniger vorkommt, sind die Zeilen, die diese Spaltenwerte enthalten, nicht übereinstimmend und werden in der Ausgabetabelle nicht angezeigt. Um den Datenschutz zu gewährleisten, prüft der Dienst LiveRamp die Eindeutigkeit der Kombinationen von Spaltenwerten und stellt sicher, dass der Auftrag fehlschlägt, wenn mehr als 5 % der Zeilen in der Datei aufgrund seltener Kombinationen nicht mehr zugeordnet werden können.

### Historische Daten

Die historischen Daten in Snowflake reichen bis April 2019 zurück. Aufgrund von Produktänderungen kann es jedoch zu leichten Abweichungen bei den Daten vor August 2019 kommen.

### Geschwindigkeit, Performance, Kosten

Die Geschwindigkeit und die Kosten der Abfragen hängen von der Größe des verwendeten Lagers ab. Berücksichtigen Sie beim Auswählen der Größe des Data Warehouse Ihre Anforderungen an den Datenzugriff.

### Braze Benchmarks

Benchmarks erlauben es Ihnen, Ihre Metriken mit Branchenstandards zu vergleichen, die direkt im Snowflake Data Exchange verfügbar sind.

### Breaking vs. Nicht-brechende Änderungen

Achten Sie auf Änderungen, die sich auf Ihre Integration auswirken können. Einschneidenden Änderungen gehen eine Ankündigung und eine Migrationsphase voraus.
