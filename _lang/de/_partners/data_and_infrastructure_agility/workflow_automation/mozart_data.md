---
nav_title: Mozart Data
article_title: Mozart Data
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Mozart Data, einer modernen All-in-One-Datenplattform, die es Ihnen ermöglicht, mit Fivetran Daten in Snowflake zu importieren, Transformationen zu erstellen, Daten zu kombinieren und mehr."
alias: /partners/mozartdata/
page_type: partner
search_tag: Partner

---

# Mozart Data

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> [Mozart Data](https://mozartdata.com/) ist eine moderne All-in-One-Datenplattform auf der Grundlage von Fivetran, Portable und Snowflake.

Die Integration von Braze und Mozart Data ermöglicht es Ihnen:
- Verwenden Sie Fivetran, um Braze-Daten in Snowflake zu importieren.
- Erstellen Sie Transformationen, indem Sie Braze-Daten mit Daten aus anderen Anwendungen kombinieren und das Benutzerverhalten effektiv analysieren.
- Importieren Sie Daten aus Snowflake in Braze, um neue Möglichkeiten der Kundenbindung zu schaffen.
- Kombinieren Sie Braze-Daten mit Daten aus anderen Anwendungen, um ein ganzheitlicheres Verständnis des Benutzerverhaltens zu erhalten.
- Integrieren Sie ein Business Intelligence-Tool, um die in Snowflake gespeicherten Daten weiter zu untersuchen.

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
| Mozart Datenkonto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Mozart Data-Konto. [Melden Sie sich hier an.](https://app.mozartdata.com/signup)|
| Schneeflocken-Konto<br>Option 1: Neues Konto | Wählen Sie **Neues Snowflake-Konto erstellen** während des Erstellungsprozesses des Mozart Data-Kontos, damit Mozart Data ein neues Snowflake-Konto für Sie einrichten kann. |
| Schneeflocken-Konto<br>Option 2: Bestehendes Konto | Wenn Ihr Unternehmen bereits über ein Snowflake-Konto verfügt, können Sie die Option Mozart Data Connected verwenden.<br><br>Wählen Sie die Option **Sie haben bereits ein Snowflake-Konto**, um ein bestehendes Snowflake-Konto zu verbinden. Um diese Option zu nutzen, muss ein Benutzer mit Zugriffsrechten auf Kontoebene [die folgenden Schritte ausführen](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Die Integration wird sowohl für die Synchronisierung von Daten von [Braze zu Mozart Data](#syncing-data-from-braze-to-mozart-data) als auch [von Mozart Data zu Braze](#syncing-data-from-mozart-data-to-braze) unterstützt.

### Daten von Braze mit Mozart Data synchronisieren

#### Schritt 1: Lötverbinder einrichten

1. Gehen Sie in Mozart Data zu **Connectors** und klicken Sie auf **Add Connector**.
2. Suchen Sie nach "Braze" und wählen Sie die Anschlusskarte aus.
3. Geben Sie einen Namen für das Zielschema ein, in dem alle synchronisierten Daten aus Braze gespeichert werden sollen. Wir empfehlen, den Standard-Schemanamen `braze` zu verwenden.
4. Klicken Sie auf **Verbindung hinzufügen**.

#### Schritt 2: Füllen Sie das Formular für den Fivetran-Anschluss aus

Sie werden zur Fivetran-Verbindungsseite weitergeleitet. Füllen Sie auf dieser Seite die vorgegebenen Felder aus. Klicken Sie anschließend auf **Weiter** > **Speichern & Testen**, um den Fivetran-Anschluss fertigzustellen.

Fivetran beginnt mit der Synchronisierung von Daten aus Ihrem Braze-Konto mit Ihrem Snowflake Data Warehouse. Sie können auf Abfragedaten von Mozart Data zugreifen, nachdem der Connector die Synchronisierung abgeschlossen hat. 

### Daten von Mozart Data mit Braze synchronisieren

#### Schritt 1: Ein Snowflake Data Warehouse einrichten

Folgen Sie den Anweisungen zur [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake), um eine Tabelle, einen Benutzer und eine Berechtigung über die Snowflake-Benutzeroberfläche einzurichten. Beachten Sie, dass dieser Schritt Snowflake-Zugriff auf Admin-Ebene erfordert.

#### Schritt 2: Einrichten Ihrer Snowflake-Integration in Braze

Nachdem Sie Ihr Snowflake-Warehouse eingerichtet haben, gehen Sie in Mozart Data auf die Seite **Integration** und wählen Sie **Braze**. Hier finden Sie die Zugangsdaten, die Sie Braze zur Verfügung stellen müssen.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

Gehen Sie dann, während Sie bei Braze angemeldet sind, zu **Integrationen > Technologiepartner > Snowflake**, um den Integrationsprozess zu starten. Kopieren Sie die Anmeldeinformationen von Mozart Data und fügen Sie sie auf der Snowflake Data-Importseite hinzu. Klicken Sie auf **Synchronisierungsdetails einrichten** und geben Sie Ihre Snowflake-Konto- und Quelltabelleninformationen ein. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

Als nächstes wählen Sie einen Namen für Ihre Synchronisierung, geben die E-Mail-Adressen Ihrer Kontakte an und wählen einen Datentyp und eine Synchronisierungshäufigkeit. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-importsync.png %}){: style="max-width:80%;"}

#### Schritt 3: Fügen Sie dem Braze-Benutzer einen öffentlichen Schlüssel hinzu
An diesem Punkt müssen Sie zu Snowflake zurückkehren, um die Einrichtung abzuschließen. Fügen Sie den öffentlichen Schlüssel, der auf dem Braze-Dashboard angezeigt wird, dem Benutzer hinzu, den Sie für Braze erstellt haben, um sich mit Snowflake zu verbinden.

Weitere Informationen dazu finden Sie in der [Snowflake-Dokumentation](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Wenn Sie die Schlüssel zu einem beliebigen Zeitpunkt austauschen möchten, kann Mozart Data ein neues Schlüsselpaar erzeugen und Ihnen den neuen öffentlichen Schlüssel zur Verfügung stellen.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Schritt 4: Verbindung testen

Sobald der Benutzer mit dem öffentlichen Schlüssel aktualisiert wurde, kehren Sie zum Braze-Dashboard zurück und klicken auf **Verbindung testen**. Wenn Sie erfolgreich sind, sehen Sie eine Vorschau der Daten. Wenn die Verbindung aus irgendeinem Grund nicht zustande kommt, wird eine Fehlermeldung angezeigt, die Sie bei der Fehlersuche unterstützt.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
Sie müssen eine Integration erfolgreich testen, bevor sie vom Entwurfsstatus in den aktiven Status übergehen kann. Wenn Sie die Erstellungsseite verlassen müssen, wird Ihre Integration gespeichert, und Sie können die Detailseite erneut aufrufen, um Änderungen vorzunehmen und zu testen.  
{% endalert %}

## Mit dieser Integration

### Wie Sie als Mozart Data-Benutzer auf Braze-Daten zugreifen
Nach erfolgreicher Erstellung eines Mozart Data-Kontos können Sie von Mozart Data aus auf Ihre mit Ihrem Snowflake Data Warehouse synchronisierten Braze-Daten zugreifen.

#### Transformiert
Mozart Data bietet eine SQL-Transformationsschicht, mit der Benutzer eine Ansicht oder Tabelle erstellen können. Sie können eine Dimensionstabelle auf Benutzerebene erstellen (z.B. `dim_users`), um die Produktnutzungsdaten, den Transaktionsverlauf und die Aktivitäten jedes Benutzers in Bezug auf Braze-Nachrichten zusammenzufassen. 

#### Analyse
Mithilfe der Transformationsmodelle oder der von Braze synchronisierten Rohdaten können Sie das Engagement der Benutzer für Braze-Nachrichten analysieren. Darüber hinaus können Sie die Braze-Daten mit anderen Anwendungsdaten kombinieren und analysieren, wie die Erkenntnisse, die Sie aus der Interaktion der Benutzer mit den Braze-Nachrichten gewonnen haben, mit anderen Daten zusammenhängen, die Sie über die Benutzer haben. Zum Beispiel ihre demografischen Daten, ihr Einkaufsverhalten, ihre Produktnutzung und ihr Engagement im Kundenservice. 

Dies kann Ihnen helfen, fundiertere Entscheidungen über Engagement-Strategien zur Verbesserung der Benutzerbindung zu treffen. Das alles können Sie innerhalb der Benutzeroberfläche von Mozart Data mit dem Abfragetool erledigen. Dort können Sie die Ergebnisse in ein Google Sheet oder eine CSV-Datei exportieren, um sie für eine Präsentation vorzubereiten.

#### Business Intelligence (BI)
Sind Sie bereit, Ihre Erkenntnisse zu visualisieren und mit anderen Teammitgliedern zu teilen? Mozart Data lässt sich mit fast jedem BI-Tool integrieren. Wenn Sie noch kein BI-Tool haben, wenden Sie sich an Mozart Data, um ein kostenloses Metabase-Konto einzurichten. 