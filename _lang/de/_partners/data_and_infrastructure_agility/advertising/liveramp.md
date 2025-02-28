---
nav_title: LiveRamp
article_title: LiveRamp
description: "Erfahren Sie, wie Sie LiveRamp, Snowflake und Braze miteinander verbinden können, damit Sie hochgradig personalisierte und relevante Marketingkampagnen erstellen können."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# LiveRamp, Snowflake und Braze miteinander verbinden

> Erfahren Sie, wie Sie LiveRamp, Snowflake und Braze miteinander verbinden können, damit Sie hochgradig personalisierte und relevante Marketingkampagnen erstellen können, indem Sie die Zeit bis zur Gewinnung von Erkenntnissen verkürzen, Datensilos aufbrechen und die Kundenbindung optimieren. Diese Integration verbessert das datengesteuerte Marketing, indem sie verwertbare personenbezogene Erkenntnisse liefert und die Berührungspunkte mit den Verbrauchern konsolidiert, um eine bessere Segmentierung der Zielgruppe und zeitnahe Kampagnen zu ermöglichen. Außerdem können Sie mit Hilfe von Snowflake Benchmarks Ihre Marketingstrategien im Vergleich zu den Industriestandards verfeinern.

{% alert important %}
Die [sichere Datenfreigabe](https://docs.snowflake.com/en/user-guide/data-sharing-intro) von Snowflake überträgt keine Daten zwischen LiveRamp, Snowflake und Braze. Die Daten werden nur über die Dienste und den Metadatenspeicher von Snowflake ausgetauscht, d.h. es werden keine Daten kopiert und es fallen keine zusätzlichen Speichergebühren an. Der Zugriff auf gemeinsam genutzte Daten wird über die Zugriffskontrollen Ihres Snowflake-Kontos gesteuert und geregelt.
{% endalert %}

## Anwendungsfälle

- **Datenminimierung:** Die Aktivierungs-App von LiveRamp nutzt die Funktion Secure Data Share von Snowflake, um die Tabellen direkt aus Ihrer Instanz zu lesen. Bis zur Übergabe an den nachgelagerten Partner werden keine Daten von Snowflake verschoben.
- **Sichere 1st-Party-Aktivierung:** Wenn Sie die oben beschriebene Anwendung zur Identitätsauflösung verwenden, nutzt die Aktivierungsanwendung von LiveRamp nur die RampID-basierten Tabellen in Ihrer Snowflake-Instanz, so dass die PII niemals Ihre Wände verlassen müssen.
- **Beschleunigen Sie die Zeit zum Leben:** Da die Daten direkt in Ihrer Umgebung in RampID aufgelöst werden, kann die Zustellung an ein Endziel innerhalb weniger Stunden erfolgen, im Vergleich zu mehreren Tagen bei der Verwendung des traditionellen dateibasierten Ansatzes von LiveRamp. So können Sie die Kampagnenleistung rechtzeitig optimieren.
- **Operative Einsparungen:** Ähnlich wie oben beschrieben, sparen Kunden durch die Verwendung der Snowflake-Funktion für die sichere Datenfreigabe Zeit und Geld im Vergleich zur Koordinierung der Übertragung von Dateien an LiveRamp oder direkt an ein beliebiges Endziel.

## Voraussetzungen

| Voraussetzung       | Beschreibung                                                                                                                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Schneeflocken-Konto | Sie benötigen ein Snowflake-Konto mit Admin-Rechten.                                                                                                                                      |
| LiveRamp Konto  | Wenden Sie sich an Ihr LiveRamp-Kundenteam oder an [snowflake@liveramp.com](mailto:snowflake@liveramp.com), um die erforderlichen LiveRamp-Anwendungen in Snowflake zu besprechen.                              |
{: .reset-td-br-1 .reset-td-br-2 }

## Einrichten der Integration

### Schritt 1: Beantragen Sie eine Datenfreigabe von Braze

Wenden Sie sich zunächst an Ihren Braze Account Manager oder Customer Success Manager, um einen Snowflake Data Share Connector für Ihr Braze-Konto zu erwerben. Wenn Sie eine Datenfreigabe anfordern, wird Braze die Freigabe von dem/den Arbeitsbereich(en) aus bereitstellen, für den/die die Freigabe erworben wurde. Nachdem die Freigabe bereitgestellt wurde, sind alle Daten sofort von Ihrer Snowflake-Instanz aus in Form einer eingehenden Datenfreigabe zugänglich. Sobald die Freigabe in Ihrer Instanz sichtbar ist, erstellen Sie eine Datenbank aus der Freigabe, damit Sie die Tabellen sehen und abfragen können.

Eine vollständige Anleitung finden Sie im [Snowflake Integrationsleitfaden mit Braze]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/).

### Schritt 2: Einrichten der LiveRamp App in Snowflake 

Die Funktionen zur Übersetzung und Identitätsauflösung sind in Snowflake über die native App LiveRamp Identity Resolution and Translation verfügbar, die eine Freigabe für Ihr Konto erstellt und eine Ansicht zur Abfrage des Referenzdatensatzes in Ihrer eigenen Snowflake-Umgebung öffnet.

Um die native App einzurichten, folgen Sie diesen Schritten in den LiveRamp-Dokumenten: [Einrichten der LiveRamp Native App in Snowflake](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html). Wenn Sie fertig sind, fahren Sie mit dem nächsten Schritt fort.

### Schritt 3: Erstellen Sie eine Datentabelle

{% alert warning %}
Bevor Sie PII-basierte Tabellen vorbereiten, sollten Sie den [Datenschutzfilter von LiveRamp](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html) kennen, der während der Aufträge ausgeführt wird, um sicherzustellen, dass die Attributspalten (Nicht-Identifikatoren) in Ihren Eingabetabellen keine zu eindeutigen Werte enthalten. Dies ist wichtig, um die Privatsphäre der Verbraucher zu schützen und eine erneute Identifizierung zu vermeiden.
{% endalert %}

Als Nächstes erstellen Sie eine Datentabelle mit dem [gewünschten Format](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html), die in der nativen LiveRamp-App aufgerufen wird. Anhand der folgenden Kategorien können Sie feststellen, welche Ihrer Identifikatoren für die Auflösung in Frage kommen:

| Identifikator Typ | Beschreibung  |
|-----------------|--------------|
| Vollständige PII        | Zu den persönlich identifizierbaren Informationen (PII) gehören der Name, die Postanschrift, die E-Mail-Adresse und die Telefonnummer des Benutzers. **Hinweis:** Nicht alle Identifikatoren sind für jeden Datensatz erforderlich. |
| Nur E-Mail      | Die E-Mail-Adressen der Benutzer, wie `alex-lee@email.com`. |
| Gerät          | Dazu gehören Cookies von Drittanbietern, Mobile Advertising IDs (MAIDs), Connected TV IDs (CTV IDs) und RampIDs (aufgelöst in eine Household RampID). |
| CIDs            | Dies sind Kennungen von einem Plattformpartner oder eine mit LiveRamp synchronisierte Identität, wie z.B. Ihre interne Kunden-ID. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Hartlöt-Identifikatoren

Die Ereignisprotokolle von Braze enthalten Kennungen, die Sie in der nativen LiveRamp-App verwenden können. Eine vollständige Liste der verfügbaren Bezeichner für jeden Ereignistyp finden Sie in den [Braze Ereignisschemata und Bezeichnern](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt).

| Identifikator Typ | Beschreibung  |
|-----------------|--------------|
| `AD_ID` | Werbe-IDs, wie z.B. `ios_idfa`, `google_ad_id`, `roku_ad_id`, die innerhalb bestimmter Ereignistypen erfasst wurden und die in Verbindung mit den LiveRamp-Diensten zur Geräteauflösung verwendet werden können. Standardmäßig werden die Werbe-IDs nicht erfasst. Sie können das Tracking jedoch aktivieren, indem Sie die [Dokumentation von Braze]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default) befolgen. |
| `EMAIL_ADDRESS`   | E-Mail-Adresse, die in Verbindung mit LiveRamp's Email Only Resolution Services verwendet werden kann |
| `TO_PHONE_NUMBER` | Telefonnummer, die in Verbindung mit den PII-Auflösungsdiensten von LiveRamp verwendet werden kann. |
| `EXTERNAL_USER_ID` | Die einem Benutzer zugeordnete externe ID, die in Verbindung mit den Geräteauflösungsdiensten (CID) von LiveRamp verwendet werden kann. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Die Verwendung von kunden- oder markenspezifischen Identifikatoren innerhalb der LiveRamp-Anwendung erfordert eine [Identitätssynchronisierung mit LiveRamp](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html).
{% endalert %}

### Schritt 4: Setzen Sie Ihre Variablen

Als nächstes legen Sie Ihre Variablen für den Auftrag im Arbeitsblatt Ausführungsschritte fest, das in der App enthalten ist. Dazu gehören Details wie die Zieldatenbank, zugehörige Tabellen (Eingabedaten, Metriken, Protokollierung) und die Definition des Namens der Ausgabetabelle. Einen vollständigen Überblick finden Sie unter [LiveRamp: Geben Sie die Variablen](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727) an.

### Schritt 5: Erstellen Sie die Metadatentabelle für die Auflösung der PII

Da Ihre Variablen nun festgelegt sind, erstellen Sie die Metadaten-Tabelle für die PII-Auflösung. Hier finden Sie Einzelheiten über die Art des auszuführenden Auftrags, basierend auf der Kategorie der beteiligten Identifikatoren. Einen vollständigen Überblick finden Sie unter [LiveRamp: Erstellen Sie die Metadatentabelle](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43).

### Schritt 6: Führen Sie den Vorgang der Identitätsauflösung durch

Führen Sie schließlich den Vorgang der Identitätsauflösung durch. Einen vollständigen Überblick finden Sie unter [LiveRamp: Führen Sie den Vorgang der Identitätsauflösung durch](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation).

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

{% tab example output %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### Nächste Schritte

Da Ihre Daten nun pseudonymisiert und mit Ihrer eigenen RampID-Kodierung versehen sind, haben Sie die Möglichkeit, die RampID-basierten Tabellen an die Managed Activation Application von LiveRamp weiterzugeben, um die Abwicklung mit Ihren wichtigsten Werbeplattformpartnern zu optimieren. Die Aktivierungsanwendung enthält eine benutzerfreundliche Oberfläche für die zusätzliche Segmentierung und Auswahl/Konfiguration von nachgeschalteten Zielpartnern. Für weitere Details zur Anwendung wenden Sie sich bitte an Ihr LiveRamp-Kundenteam oder an [snowflake@liveramp.com](mailto:snowflake@liveramp.com).

## Fehlersuche

{% alert note %}
Wenn Sie spezielle Probleme oder Fragen haben, wenden Sie sich an [martech@liveramp.com](mailto:martech@liveramp.com).
{% endalert %}

### Schneeflocken-Regionen

Derzeit ist diese Anwendung nur für die folgenden Regionen in den USA verfügbar:

  - aws-us-east-1: POA18931
  - aws-us-west-2: FAA28932
  - azure-east-us-2: BL60425

### Datenschutz & Spaltenwerte

Der Prozess wertet die Kombination aller Spaltenwerte für jede Zeile auf eindeutige Werte aus. Wenn eine bestimmte Kombination von Spaltenwerten 3 Mal oder weniger vorkommt, sind die Zeilen, die diese Spaltenwerte enthalten, nicht übereinstimmend und werden in der Ausgabetabelle nicht angezeigt. Um den Datenschutz zu gewährleisten, prüft der LiveRamp-Dienst auch die Einzigartigkeit von Kombinationen von Spaltenwerten und stellt sicher, dass der Auftrag fehlschlägt, wenn mehr als 5 % der Zeilen der Datei aufgrund seltener Kombinationen nicht mehr zugeordnet werden können.

### Historische Daten

Die historischen Daten in Snowflake reichen bis April 2019 zurück. Aufgrund von Produktänderungen kann es jedoch zu leichten Abweichungen bei den Daten von vor August 2019 kommen.

### Geschwindigkeit, Leistung, Kosten

Die Geschwindigkeit und die Kosten der Abfragen hängen von der Größe des verwendeten Lagers ab. Berücksichtigen Sie Ihre Anforderungen an den Datenzugriff, wenn Sie die Größe des Warehouse auswählen.

### Braze Benchmarks

Benchmarks ermöglichen Ihnen den Vergleich Ihrer Kennzahlen mit Branchenstandards, die direkt im Snowflake Data Exchange verfügbar sind.

### Breaking vs. Nicht-brechende Änderungen

Achten Sie auf Änderungen, die sich auf Ihre Integration auswirken können. Einschneidenden Änderungen werden eine Ankündigung und eine Umstellungsphase vorausgehen.
