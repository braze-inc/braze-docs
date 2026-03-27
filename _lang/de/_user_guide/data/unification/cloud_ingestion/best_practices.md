---
nav_title: Bewährte Praktiken
article_title: Bewährte Praktiken für die Cloud-Datenaufnahme
toc_headers: h2
page_order: 0
page_type: reference
description: "Diese Seite bietet eine Übersicht über die Cloud-Datenaufnahme, bewährte Praktiken und Produktbeschränkungen."

---

# Bewährte Praktiken

> Mit Braze Cloud Data Ingestion können Sie eine direkte Verbindung von Ihrem Data Warehouse oder Dateispeichersystem zu Braze einrichten, um relevante Nutzer- oder Katalogdaten zu synchronisieren. Wenn Sie diese Daten mit Braze synchronisieren, können Sie sie für Anwendungsfälle wie Personalisierung, Triggern oder Segmentierung nutzen. 

## Die Spalte `UPDATED_AT` verstehen

{% alert note %}
`UPDATED_AT` ist nur für Data-Warehouse-Integrationen relevant, nicht für S3-Synchronisierungen.
{% endalert %}

Bei einer Synchronisierung stellt Braze eine direkte Verbindung zu Ihrer Data-Warehouse-Instanz her, ruft alle neuen Daten aus der angegebenen Tabelle ab und aktualisiert die entsprechenden Daten in Ihrem Braze-Dashboard. Bei jeder Synchronisierung spiegelt Braze alle aktualisierten Daten wider.

{% alert important %}
Braze CDI synchronisiert Zeilen ausschließlich auf Grundlage des `UPDATED_AT`-Werts, unabhängig davon, ob der Inhalt der Zeile mit dem derzeit in Braze vorhandenen übereinstimmt. Daher empfehlen wir, `UPDATED_AT` korrekt zu verwenden, um nur neue oder aktualisierte Daten zu synchronisieren und so eine unnötige Datenpunkt-Nutzung zu vermeiden.
{% endalert %}

### Beispiel: Wiederkehrende Synchronisierung

Um zu veranschaulichen, wie `UPDATED_AT` in einer CDI-Synchronisierung verwendet wird, betrachten Sie dieses Beispiel einer wiederkehrenden Synchronisierung zum Update von Nutzerattributen:

- Dateispeicherquellen 
   - Amazon S3

## Unterstützte Datentypen 

Cloud Data Ingestion unterstützt die folgenden Datentypen: 
- Nutzerattribute, einschließlich:
   - Verschachtelte angepasste Attribute
   - Arrays von Objekten
   - Abo-Status
- Angepasste Events
- Kauf-Events
- Katalogartikel
- Nutzer-Löschanfragen

Sie können Nutzerdaten anhand der externen ID, des Nutzer-Alias, der Braze-ID, der E-Mail-Adresse oder der Telefonnummer aktualisieren. Sie können Nutzer:innen anhand der externen ID, des Nutzer-Alias oder der Braze-ID löschen. 

## Was wird synchronisiert?

Bei jeder Synchronisierung sucht Braze nach Zeilen, die noch nicht synchronisiert wurden. Dies wird anhand der Spalte `UPDATED_AT` in Ihrer Tabelle oder Ansicht überprüft. Braze wählt alle Zeilen aus und importiert sie, deren `UPDATED_AT`-Wert später als der zuletzt synchronisierte `UPDATED_AT`-Wert ist. Zeilen am exakten Grenz-Zeitstempel können ebenfalls erneut synchronisiert werden, wenn zwischen den Durchläufen neue Zeilen mit demselben Zeitstempel hinzugefügt werden.

{% alert important %}
CDI verfolgt die Anzahl der Zeilen beim zuletzt synchronisierten `UPDATED_AT`-Wert. Wenn zwischen den Durchläufen neue Zeilen mit demselben Zeitstempel hinzugefügt werden, wechselt CDI zu einer inklusiven Grenze (`>=`) und synchronisiert alle Zeilen mit diesem Zeitstempel erneut, einschließlich bereits verarbeiteter. Um doppelte Synchronisierungen und unnötigen Datenpunktverbrauch zu vermeiden, verwenden Sie eindeutige `UPDATED_AT`-Werte über die Synchronisierungsläufe hinweg. Weitere Informationen finden Sie unter [Erneutes Synchronisieren von Zeilen mit doppelten Zeitstempeln vermeiden](#avoid-resyncing-rows-with-duplicate-timestamps).
{% endalert %}

Fügen Sie in Ihrem Data Warehouse die folgenden Nutzer:innen und Attribute zu Ihrer Tabelle hinzu und setzen Sie den `UPDATED_AT`-Zeitpunkt auf den Zeitpunkt, zu dem Sie diese Daten hinzufügen:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Bei der nächsten geplanten Synchronisierung synchronisiert Braze alle Zeilen mit einem `UPDATED_AT`-Zeitstempel, der später als der zuletzt synchronisierte Zeitstempel ist. Braze führt Updates durch oder fügt Felder hinzu, sodass Sie nicht jedes Mal das vollständige Nutzerprofil synchronisieren müssen. Nach der Synchronisierung spiegeln die Nutzerprofile die neuen Updates wider:

**Wiederkehrende Synchronisierung, zweiter Durchlauf am 20. Juli 2022 um 12 Uhr**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

Für `customer_9012` wurde eine neue Zeile hinzugefügt, aber ihr `UPDATED_AT`-Wert (`2022-07-16 00:25:30`) liegt vor dem gespeicherten Zeitstempel (`2022-07-19 09:07:23`), sodass sie nicht synchronisiert wird. Die bestehende Zeile für `customer_5678` hat jedoch einen `UPDATED_AT`-Wert, der dem gespeicherten Zeitstempel entspricht, und wird daher aufgrund der inklusiven Grenze erneut synchronisiert. Weitere Details zu diesem Verhalten finden Sie unter [Stellen Sie sicher, dass die UPDATED_AT-Zeit nicht mit Ihrer Synchronisierungszeit übereinstimmt](#make-sure-the-updated_at-time-isnt-the-same-time-as-your-sync). Der gespeicherte `UPDATED_AT`-Wert bleibt `2022-07-19 09:07:23`.

**Wiederkehrende Synchronisierung, dritter Durchlauf am 21. Juli 2022 um 12 Uhr**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"xyz",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-21 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-20T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

In diesem dritten Durchlauf wurde eine weitere neue Zeile für `customer_1234` mit einem `UPDATED_AT`-Wert (`2022-07-21 08:30:00`) hinzugefügt, der später als der gespeicherte Zeitstempel ist. Diese neue Zeile und die bestehende Zeile für `customer_5678` (deren `UPDATED_AT`-Wert dem gespeicherten Zeitstempel entspricht) werden beide synchronisiert. Der gespeicherte `UPDATED_AT`-Wert ist nun `2022-07-21 08:30:00`.

{% alert note %}
`UPDATED_AT`-Werte dürfen sogar nach der Startzeit eines bestimmten Synchronisierungslaufs liegen. Dies wird jedoch nicht empfohlen, da dadurch der letzte `UPDATED_AT`-Zeitstempel „in die Zukunft verschoben" wird und nachfolgende Synchronisierungen frühere Werte nicht mehr synchronisieren.
{% endalert %}

## Verwenden Sie einen UTC-Zeitstempel für die Spalte `UPDATED_AT`

Die Spalte `UPDATED_AT` sollte in UTC sein, um Probleme mit der Sommerzeit zu vermeiden. Bevorzugen Sie reine UTC-Funktionen wie z. B. `SYSDATE()` anstelle von `CURRENT_DATE()`, wann immer dies möglich ist.

## Erneutes Synchronisieren von Zeilen mit doppelten Zeitstempeln vermeiden {#avoid-resyncing-rows-with-duplicate-timestamps}

CDI verfolgt die Anzahl der Zeilen beim zuletzt synchronisierten `UPDATED_AT`-Zeitstempel. Wenn CDI erkennt, dass seit dem letzten Durchlauf neue Zeilen mit demselben Zeitstempel hinzugefügt wurden, verwendet es eine inklusive Grenze (`>=`), um alle Zeilen mit diesem Zeitstempel erneut auszuwählen, einschließlich bereits verarbeiteter. Andernfalls verwendet CDI eine exklusive Grenze (`>`) und wählt nur Zeilen aus, die strikt nach dem zuletzt synchronisierten Wert liegen.

Wenn beispielsweise eine Synchronisierung fünf Zeilen mit `UPDATED_AT = 2025-04-01 00:00:00` verarbeitet und später eine sechste Zeile mit demselben Zeitstempel hinzugefügt wird, erkennt die nächste Synchronisierung die Änderung der Anzahl und synchronisiert alle sechs Zeilen erneut. Dies kann zu doppelten Daten und unnötigem Datenpunktverbrauch führen.

Um dies zu vermeiden:

- Wenn Sie eine Synchronisierung gegen eine `VIEW` einrichten, verwenden Sie nicht `CURRENT_TIMESTAMP` als Standardwert. Dies führt dazu, dass alle Daten bei jedem Synchronisierungslauf synchronisiert werden, da das `UPDATED_AT`-Feld zum Zeitpunkt der Abfrageausführung ausgewertet wird.
- Wenn Sie lang laufende Pipelines oder Abfragen haben, die Daten in Ihre Quelltabelle schreiben, vermeiden Sie es, diese gleichzeitig mit einer Synchronisierung auszuführen, oder vermeiden Sie es, denselben Zeitstempel für jede eingefügte Zeile zu verwenden.
- Verwenden Sie eine Transaktion, um alle Zeilen zu schreiben, die denselben Zeitstempel haben.
- Verwenden Sie eindeutige, monoton steigende `UPDATED_AT`-Werte, um zu verhindern, dass Zeilen nach der Verarbeitung erneut ausgewählt werden.

### Beispiel: Verwaltung nachfolgender Updates

Dieses Beispiel zeigt den allgemeinen Prozess für die erstmalige Synchronisierung von Daten und die anschließende Aktualisierung nur der geänderten Daten (Deltas) in den nachfolgenden Updates. Nehmen wir an, wir haben eine Tabelle `EXAMPLE_DATA` mit einigen Nutzerdaten. Am Tag 1 hat sie die folgenden Werte:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td>823</td>
            <td>blue</td>
            <td>380</td>
            <td>FALSE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td>28</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td>384</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>red</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td>813</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Um diese Daten in das von CDI erwartete Format zu bringen, könnten Sie die folgende Abfrage ausführen:

```sql
SELECT
    CURRENT_TIMESTAMP AS UPDATED_AT,
    EXTERNAL_ID AS EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT(
            'attribute_1', attribute_1,
            'attribute_2', attribute_2,
            'attribute_3', attribute_3,
            'attribute_4', attribute_4
        )
    ) AS PAYLOAD
FROM EXAMPLE_DATA;
```

Nichts davon wurde bisher mit Braze synchronisiert, also fügen Sie alles der Quelltabelle für CDI hinzu:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
  </tbody>
</table>

Eine Synchronisierung wird durchgeführt und Braze hält fest, dass Sie alle verfügbaren Daten bis zum „2023-03-16 15:00:00" synchronisiert haben. Am Morgen des 2. Tages wird dann ein ETL ausgeführt und einige Felder in Ihrer Nutzertabelle werden aktualisiert (hervorgehoben):

<table>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td style="background-color: #FFFF00;">145</td>
            <td style="background-color: #FFFF00;">red</td>
            <td>380</td>
            <td style="background-color: #FFFF00;">TRUE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">15</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td style="background-color: #FFFF00;">495</td>
            <td style="background-color: #FFFF00;">FALSE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td style="background-color: #FFFF00;">green</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td style="background-color: #FFFF00;">693</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

Jetzt müssen Sie nur noch die geänderten Werte in die CDI-Quelltabelle einfügen. Diese Zeilen können angehängt werden, anstatt die alten Zeilen zu aktualisieren. Die Tabelle sieht nun wie folgt aus:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "15"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_2":"green"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_3":"693"}</code></td>
    </tr>
  </tbody>
</table>

CDI synchronisiert nur die neuen Zeilen. Bei der nächsten Synchronisierung werden also nur die letzten fünf Zeilen synchronisiert.

## Weitere Hinweise

### Schreiben Sie nur neue oder aktualisierte Attribute, um den Verbrauch zu minimieren

Bei jeder Synchronisierung sucht Braze nach Zeilen, die noch nicht synchronisiert wurden. Dies wird anhand der Spalte `UPDATED_AT` in Ihrer Tabelle oder Ansicht überprüft. Braze wählt alle Zeilen aus und importiert sie, deren `UPDATED_AT`-Wert später als der zuletzt synchronisierte `UPDATED_AT`-Wert ist, unabhängig davon, ob sie mit den aktuellen Angaben im Nutzerprofil übereinstimmen. Zeilen am Grenz-Zeitstempel können ebenfalls erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel haben. Wir empfehlen daher, nur Attribute zu synchronisieren, die Sie hinzufügen oder aktualisieren möchten.

Die Datenpunkt-Nutzung ist bei CDI identisch mit anderen Erfassungsmethoden wie REST APIs oder SDKs. Es liegt daher in Ihrer Verantwortung, sicherzustellen, dass Sie nur neue oder aktualisierte Attribute in Ihre Quelltabellen einfügen.

### Trennen Sie `EXTERNAL_ID` von der Spalte `PAYLOAD`

Das Objekt `PAYLOAD` sollte keine externe ID oder einen anderen ID-Typ enthalten. 

### Ein Attribut entfernen

Wenn Sie ein Attribut aus dem Profil einer Nutzer:in weglassen möchten, können Sie es auf `null` setzen. Wenn Sie möchten, dass ein Attribut unverändert bleibt, senden Sie es nicht an Braze, bis es aktualisiert wurde. Um ein Attribut vollständig zu entfernen, verwenden Sie `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`.

### Inkrementelle Updates durchführen

Führen Sie inkrementelle Updates Ihrer Daten durch, um unbeabsichtigtes Überschreiben bei gleichzeitigen Updates zu verhindern.

{% alert important %}
* **Updates verschiedener Attribute:** In den allermeisten Fällen haben zwei Updates, die nicht dieselben Attribute einer Nutzer:in betreffen, völlig unabhängige Ergebnisse. Wenn Sie beispielsweise das Attribut `Color` einer Nutzer:in aktualisieren und separat deren Attribut `Size` aktualisieren, sollten beide Updates korrekt angewendet werden, auch wenn sie innerhalb weniger Sekunden nacheinander erfolgen.
* **Updates desselben Attributs:** Race-Conditions können auftreten, wenn mehrere Updates innerhalb eines einzigen Synchronisierungslaufs auf dasselbe Attribut abzielen. In diesen seltenen Fällen kann es vorkommen, dass ein Update ein anderes überschreibt. Die beste Möglichkeit, dieses Verhalten zu verhindern, besteht darin, sicherzustellen, dass die Quelldaten für Ihre CDI-Synchronisierung nur den aktuellen Status jeder Nutzer:in widerspiegeln oder dass alle Updates für eine bestimmte Nutzer:in oder eine bestimmte Nutzer-Attribut-Kombination in einer einzigen Zeile enthalten sind.
* **Objekt-Array-Operatoren:** Die einzigen Ausnahmen von unabhängigen Updates sind die Operatoren `$add`, `$remove` und `$update` für Objekt-Arrays, bei denen Updates desselben Arrays miteinander interagieren können.
* **Events:** Race-Conditions haben keinen Einfluss auf Events, da jedes Event eindeutig ist und einen Zeitstempel hat.
{% endalert %}

Die beste Möglichkeit, dieses Verhalten zu verhindern, besteht darin, sicherzustellen, dass die Quelldaten für Ihre CDI-Synchronisierung nur den aktuellen Status jeder Nutzer:in widerspiegeln oder dass alle Updates für eine bestimmte Nutzer:in oder eine bestimmte Nutzer-Attribut-Kombination in einer einzigen Zeile enthalten sind.

### Erstellen eines JSON-Strings aus einer anderen Tabelle

Wenn Sie es vorziehen, jedes Attribut intern in einer eigenen Spalte zu speichern, müssen Sie diese Spalten in einen JSON-String konvertieren, um die Synchronisierung mit Braze zu befüllen. Dazu können Sie eine Abfrage wie die folgende verwenden:

{% tabs local %}
{% tab Snowflake %}
```sql
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    )as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    ) as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab BigQuery %}
```sql
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (attribute_1 string,
     attribute_2 STRING,
     attribute_3 NUMERIC,
     my_user_id STRING);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        'attribute_1' AS attribute_1,
        'attribute_2'AS attribute_2,
        'yet_another_attribute'AS attribute_3
      )
    ) as PAYLOAD 
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Databricks %}
```sql
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (
    attribute_1 string,
    attribute_2 STRING,
    attribute_3 NUMERIC,
    my_user_id STRING
);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        attribute_1,
        attribute_2,
        attribute_3
      )
    ) as PAYLOAD 
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE TABLE [braze].[users] (
    attribute_1 VARCHAR,
    attribute_2 VARCHAR,
    attribute_3 VARCHAR,
    attribute_4 VARCHAR,
    user_id VARCHAR
)
GO

CREATE VIEW [braze].[user_update_example]
AS SELECT 
    user_id as EXTERNAL_ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[users] ;
```
{% endtab %}

{% endtabs %}

### Verwenden Sie den Zeitstempel `UPDATED_AT`

Braze verwendet den Zeitstempel `UPDATED_AT`, um zu verfolgen, welche Daten erfolgreich synchronisiert wurden. CDI verfolgt auch die Anzahl der Zeilen beim zuletzt synchronisierten Zeitstempel. Wenn zwischen den Durchläufen neue Zeilen mit demselben Zeitstempel hinzugefügt werden, synchronisiert CDI alle Zeilen mit diesem Zeitstempel erneut, was zu doppelten Daten führen kann. Weitere Details und Tipps finden Sie unter [Erneutes Synchronisieren von Zeilen mit doppelten Zeitstempeln vermeiden](#avoid-resyncing-rows-with-duplicate-timestamps).

### Tabellenkonfiguration

Wir haben ein öffentliches [GitHub-Repository](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion), in dem Kund:innen bewährte Praktiken oder Code-Snippets austauschen können. Wenn Sie Ihre eigenen Snippets beisteuern möchten, erstellen Sie einen Pull-Request!

### Datenformatierung

Alle Vorgänge, die über den Braze-Endpunkt `/users/track` möglich sind, werden durch Cloud Data Ingestion unterstützt, einschließlich der Aktualisierung verschachtelter angepasster Attribute, dem Hinzufügen des Abo-Status und der Synchronisierung von angepassten Events oder Käufen. 

Die Felder in der Payload sollten dasselbe Format haben wie beim entsprechenden Endpunkt `/users/track`. Detaillierte Formatierungsanforderungen finden Sie im Folgenden:

| Datentyp | Formatierungsspezifikationen |
| --------- | ---------| --------- | ----------- |
| `attributes` | Siehe [Nutzerattribute-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Siehe [Events-Objekt]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Siehe [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Beachten Sie die besondere Anforderung für die [Erfassung von Datumsangaben]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties) in verschachtelten Attributen. 

{% tabs local %}
{% tab Nested Custom Attributes %}
Sie können verschachtelte angepasste Attribute in die Payload-Spalte für eine Synchronisierung angepasster Attribute aufnehmen. 

```json
{
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
}
```

{% endtab %}
{% tab Event %}
Um Events zu synchronisieren, ist ein Event-Name erforderlich. Formatieren Sie das Feld `time` als ISO-8601-String oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Wenn das Feld `time` nicht vorhanden ist, verwendet Braze den Spaltenwert `UPDATED_AT` als Event-Zeit. Andere Felder wie `app_id` und `properties` sind optional. 

Beachten Sie, dass Sie nur ein Event pro Zeile synchronisieren können.

```json
{
    "app_id" : "your-app-id",
    "name" : "rented_movie",
    "time" : "2013-07-16T19:20:45+01:00",
    "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
    }
} 
```

{% endtab %}
{% tab Purchase %}
Um Kauf-Events zu synchronisieren, sind `product_id`, `currency` und `price` erforderlich. Formatieren Sie das optionale Feld `time` als ISO-8601-String oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Wenn das Feld `time` nicht vorhanden ist, verwendet Braze den Spaltenwert `UPDATED_AT` als Event-Zeit. Andere Felder wie `app_id`, `quantity` und `properties` sind optional.

Beachten Sie, dass Sie nur ein Kauf-Event pro Zeile synchronisieren können.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99 },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99 }
        ]
    }
}
```

{% endtab %}
{% tab Subscription Groups %}
```json
{
    "subscription_groups" : [
        {
            "subscription_group_id": "subscription_group_identifier_1",
            "subscription_state": "unsubscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_2",
            "subscription_state": "subscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_3",
            "subscription_state": "subscribed"
        }
      ]
}
```
{% endtab %}
{% endtabs %}

### Vermeiden Sie Zeitüberschreitungen bei Data-Warehouse-Abfragen

Wir empfehlen, Abfragen innerhalb einer Stunde abzuschließen, um eine optimale Performance zu erzielen und mögliche Fehler zu vermeiden. Wenn Abfragen diesen Zeitrahmen überschreiten, sollten Sie die Konfiguration Ihres Data Warehouse überprüfen. Die Optimierung der Ihrem Warehouse zugewiesenen Ressourcen kann dazu beitragen, die Ausführungsgeschwindigkeit von Abfragen zu verbessern.

## Produktbeschränkungen

| Beschränkung            | Beschreibung                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Anzahl der Integrationen | Es gibt keine Begrenzung für die Anzahl der Integrationen, die Sie einrichten können. Sie können jedoch nur eine Integration pro Tabelle oder Ansicht einrichten.                                             |
| Anzahl der Zeilen         | Standardmäßig können pro Durchlauf bis zu 500 Millionen Zeilen synchronisiert werden. Braze unterbricht alle Synchronisierungen mit mehr als 500 Millionen neuen Zeilen. Wenn Sie ein höheres Limit benötigen, wenden Sie sich an Ihren Customer-Success-Manager bei Braze oder an den Braze Support. |
| Attribute pro Zeile     | Jede Zeile sollte eine einzelne Nutzer-ID und ein JSON-Objekt mit bis zu 250 Attributen enthalten. Jeder Schlüssel im JSON-Objekt zählt als ein Attribut (d. h. ein Array zählt als ein Attribut). |
| Payload-Größe           | Jede Zeile kann eine Payload von bis zu 1 MB enthalten. Braze lehnt Payloads ab, die größer als 1&nbsp;MB sind, und protokolliert den Fehler „Payload was greater than 1MB" zusammen mit der zugehörigen externen ID und der gekürzten Payload im Synchronisierungsprotokoll. |
| Datentyp              | Sie können Nutzerattribute, Events und Käufe über Cloud Data Ingestion synchronisieren.                                                                                                  |
| Braze-Region           | Dieses Produkt ist in allen Braze-Regionen verfügbar. Jede Braze-Region kann sich mit jeder Quelldatenregion verbinden.                                                                              |
| Quellregion       | Braze stellt die Verbindung zu Ihrem Data Warehouse oder Ihrer Cloud-Umgebung in jeder Region und bei jedem Cloud-Anbieter her.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<br><br>