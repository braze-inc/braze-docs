---
nav_title: Mozart Data
article_title: Mozart Data
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Mozart Data, einer modernen All-in-One-Datenplattform, die es Ihnen erlaubt, mit Fivetran Daten in Snowflake zu importieren, Transformationen zu erstellen, Daten zu kombinieren und vieles mehr."
alias: /partners/mozart_data/
page_type: partner
search_tag: Partner

---

# Mozart Data

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> [Mozart Data](https://mozartdata.com/) ist eine moderne All-in-One-Datenplattform, die auf Fivetran, Portable und Snowflake basiert.

Die Datenintegration von Braze und Mozart Data lässt Sie zu:
- Verwenden Sie Fivetran, um Braze-Daten in Snowflake zu importieren.
- Erstellen Sie Transformationen, indem Sie Braze-Daten mit anderen Anwendungsdaten kombinieren und das Nutzer:innen-Verhalten effektiv analysieren.
- Importieren Sie Daten aus Snowflake in Braze, um neue Customer-Engagement Opportunities zu erstellen
- Kombinieren Sie Braze-Daten mit anderen Anwendungsdaten, um ein ganzheitlicheres Verständnis des Nutzer:innen-Verhaltens zu erhalten.
- Integrieren Sie ein Business-Intelligence-Tool, um die in Snowflake gespeicherten Daten weiter zu untersuchen.

## Voraussetzungen

<style>
table th:nth-child(1) {
    width: 25%;
}
table th:nth-child(2) {
    width: 75%;
}
table td {
    word-break: break-word;
}
</style>

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Mozart Daten Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Konto bei Mozart Data. [Registrieren Sie sich hier.](https://app.mozartdata.com/signup)|
| Snowflake Konto<br>Option 1: Neues Konto | Wählen Sie **Neues Snowflake-Konto erstellen** während des Prozesses zur Erstellung eines Kontos bei Mozart Data aus, damit Mozart Data ein neues Snowflake-Konto für Sie einrichten kann. |
| Snowflake Konto<br>Option 2: Bestehendes Konto | Wenn Ihr Unternehmen bereits über ein Snowflake-Konto verfügt, können Sie die Option Mozart Data Connected verwenden.<br><br>Wählen Sie die Option **Bereits ein Snowflake-Konto haben**, um ein bestehendes Snowflake-Konto zu verbinden. Um diese Option zu nutzen, muss ein Nutzer:in mit Zugriffsrechten auf Kontoebene [die folgenden Schritte ausführen](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Die Integration wird sowohl für die Synchronisierung von Daten von [Braze zu Mozart Data](#syncing-data-from-braze-to-mozart-data) als auch [von Mozart Data zu Braze](#syncing-data-from-mozart-data-to-braze) unterstützt.

### Daten von Braze mit Mozart Data synchronisieren

#### Schritt 1: Braze-Konnektor einrichten

1. Gehen Sie in Mozart Daten zu **Konnektoren** und klicken Sie auf **Konnektor hinzufügen**.
2. Suchen Sie nach "Braze" und wählen Sie die Konnektor-Karte aus.
3. Geben Sie den Namen eines Zielschemas ein, in dem alle synchronisierten Daten aus Braze gespeichert werden sollen. Wir empfehlen, den Standard-Schemanamen `braze` zu verwenden.
4. Klicken Sie auf **Konnektor hinzufügen**.

#### Schritt 2: Füllen Sie das Fivetran Konnektor Formular aus

Sie werden auf die Seite des Fivetran Konnektors weitergeleitet. Füllen Sie auf dieser Seite die vorgegebenen Felder aus. Klicken Sie anschließend auf **Weiter** > **Speichern & Testen**, um den Fivetran Konnektor fertigzustellen.

Fivetran beginnt mit der Synchronisierung der Daten von Ihrem Braze-Konto mit Ihrem Snowflake Data Warehouse. Sie können auf Abfragedaten von Mozart Data zugreifen, nachdem der Konnektor die Synchronisierung abgeschlossen hat. 

### Daten von Mozart Data mit Braze synchronisieren

#### Schritt 1: Einrichten eines Snowflake Data Warehouse

Folgen Sie den Anweisungen zur [Datenaufnahme in der Cloud]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake), um eine Tabelle, einen Nutzer:in und eine Berechtigung über die Snowflake Schnittstelle einzurichten. Beachten Sie, dass dieser Schritt Snowflake-Zugriff auf Admin-Ebene erfordert.

#### Schritt 2: Einrichten Ihrer Snowflake Integration in Braze

Nachdem Sie Ihr Snowflake Warehouse eingerichtet haben, gehen Sie in Mozart Data auf die Seite **Integration** und wählen Sie **Braze** aus. Hier finden Sie die Zugangsdaten, die Sie benötigen, um Braze zur Verfügung zu stellen.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

Gehen Sie dann, während Sie bei Braze angemeldet sind, zu **Integrationen > Technologiepartner > Snowflake**, um den Integrationsprozess zu starten. Kopieren Sie die Zugangsdaten von Mozart Data und fügen Sie sie der Snowflake Data-Importseite hinzu. Klicken Sie auf **Synchronisierungsdetails einrichten** und geben Sie Ihr Snowflake-Konto und die Informationen zur Quelltabelle ein. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

Als Nächstes wählen Sie einen Namen für Ihre Synchronisierung, geben die E-Mails der Kontakte an und wählen einen Datentyp und eine Synchronisierungshäufigkeit aus. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-importsync.png %}){: style="max-width:80%;"}

#### Schritt 3: Fügen Sie der Nutzer:in Braze einen Public Key hinzu
An dieser Stelle müssen Sie zu Snowflake zurückkehren, um die Einrichtung abzuschließen. Fügen Sie den öffentlichen Schlüssel, der auf dem Braze-Dashboard angezeigt wird, dem Nutzer:in hinzu, den Sie für Braze erstellt haben, um sich mit Snowflake zu verbinden.

Weitere Informationen dazu finden Sie in der [Snowflake-Dokumentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Wenn Sie die Schlüssel zu einem beliebigen Zeitpunkt austauschen möchten, kann Mozart Data ein neues Schlüsselpaar erzeugen und Ihnen den neuen öffentlichen Schlüssel zur Verfügung stellen.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Schritt 4: Verbindung testen

Sobald der Nutzer:innen mit dem öffentlichen Schlüssel aktualisiert wurde, kehren Sie zum Braze-Dashboard zurück und klicken auf **Verbindung testen**. Wenn Sie erfolgreich sind, sehen Sie eine Vorschau der Daten. Wenn die Verbindung aus irgendeinem Grund nicht zustande kommt, wird eine Fehlermeldung angezeigt, die Sie bei der Fehlerbehebung unterstützt.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
Sie müssen eine Integration erfolgreich testen, bevor sie vom Entwurfsstatus in den aktiven Status übergehen kann. Wenn Sie die Erstellungsseite verlassen müssen, wird Ihre Integration gespeichert, und Sie können die Detailseite erneut aufrufen, um Änderungen vorzunehmen und zu testen.  
{% endalert %}

## Verwendung dieser Integration

### So greifen Sie als Nutzer:in von Mozart Data auf Braze-Daten zu
Nach erfolgreicher Einrichtung eines Mozart Data-Kontos können Sie von Mozart Data aus auf Ihre mit Ihrem Snowflake Data Warehouse synchronisierten Braze-Daten zugreifen.

#### Transformationen
Mozart Data bietet eine SQL-Transformationsschicht, mit der Nutzer:innen eine Ansicht oder Tabelle erstellen können. Sie können eine Dimensionstabelle auf Benutzerebene erstellen (z.B. `dim_users`), um die Daten zur Nutzung der Produkte, den Verlauf von Transaktionen und das Engagement jedes Nutzers mit Nachrichten von Braze zusammenzufassen. 

#### Analyse
Mithilfe der Transformationsmodelle oder der von Braze synchronisierten Rohdaten können Sie das Engagement der Nutzer:innen bei Nachrichten von Braze analysieren. Darüber hinaus können Sie die Daten von Braze mit anderen Anwendungsdaten kombinieren und analysieren, wie sich die Insights, die Sie aus der Interaktion der Nutzer:innen mit den Nachrichten von Braze gewonnen haben, auf andere Daten beziehen, die Ihnen über die Nutzer:innen vorliegen. Zum Beispiel ihre demografischen Daten, den Verlauf des Einkaufs, die Nutzung von Produkten und das Engagement im Customer-Engagement. 

Dies kann Ihnen helfen, fundiertere Entscheidungen über Engagement-Strategien zu treffen, um die Bindung der Nutzer:innen zu verbessern. Das alles können Sie innerhalb der Schnittstelle von Mozart Data mit dem Abfragetool erledigen. Dort können Sie die Ergebnisse in ein Google Sheet oder eine CSV-Datei exportieren, um sie für eine Präsentation vorzubereiten.

#### Business-Intelligence (BI)
Sind Sie bereit, Ihre Insights zu visualisieren und mit anderen Teammitgliedern zu teilen? Mozart Data lässt sich mit fast allen BI-Tools integrieren. Wenn Sie noch kein BI-Tool haben, wenden Sie sich an Mozart Data, um ein kostenloses Metabase-Konto einzurichten. 