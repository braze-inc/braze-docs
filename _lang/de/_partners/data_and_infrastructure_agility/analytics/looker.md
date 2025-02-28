---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Looker, einer Plattform für Business Intelligence und Big-Data-Analysen."
page_type: partner
search_tag: Partner

---

# [![Braze Learning Kurs]](https://learning.braze.com/looker-integration-with-braze/) ( [{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Looker

> [Looker](https://looker.com/), eine Plattform für Business Intelligence und Big-Data-Analysen, ermöglicht es Ihnen, Geschäftsanalysen in Echtzeit nahtlos zu untersuchen, zu analysieren und zu teilen.

Die Braze- und Looker-Integration ermöglicht es Braze-Benutzern, [Looker-Blöcke](#looker-blocks) und [Looker-Aktionen](#looker-actions) von Erstanbietern über die REST-API zu kennzeichnen. Diese markierten Benutzer können zu Segmenten hinzugefügt werden, um zukünftige Braze-Kampagnen oder Canvases [gezielt zu steuern](#segment-users). Um Looker mit Braze zu verwenden, empfehlen wir Ihnen, Ihre Braze-Daten [mithilfe von Braze-Strömen][6] an ein [Data Warehouse][6] zu senden und dann die Looker-Blöcke von Braze zu verwenden, um Ihre Braze-Daten in Looker schnell zu modellieren und zu visualisieren.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
|Looker-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Looker-Konto](https://looker.com/). |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz][1] ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Beschränkungen

- Dieser Prozess funktioniert nur mit Daten, die nicht gepivotet wurden.
- Die API verarbeitet maximal 100.000 Zeilen auf einmal.
- Die endgültige Anzahl der Flaggen eines Benutzers kann aufgrund von Duplikaten oder Nicht-Benutzern niedriger sein.

## Integration

### Looker Blöcke

Mit unseren Looker Blocks können Braze-Kunden schnell auf eine Ansicht der granularen Daten zugreifen, die wir über [Currents][5] anbieten. Unsere Blöcke bieten vorgefertigte Visualisierungen und Modellierungen für Currents-Daten, so dass Braze-Kunden auf einfache Weise Analysemuster wie die Kundenbindung implementieren, die Zustellbarkeit von Nachrichten bewerten, einen detaillierteren Blick auf das Nutzerverhalten werfen und vieles mehr können.

Um die Looker Blocks zu implementieren, folgen Sie den Anweisungen in den README-Dateien des GitHub-Codes.
- [Block zur Analyse des Nachrichtenengagements README][2]
- [Block zur Analyse des Benutzerverhaltens README][3]

Beide Integrationen setzen voraus, dass Ihre [ursprüngliche Braze-Integration][4] sowie Ihre Braze-Integration mit einem Looker-kompatiblen [Data Warehouse][7] entsprechend konfiguriert ist, um die erforderlichen Daten zu erfassen und zu senden.


{% alert important %}
Braze hat unsere Looker Blocks mit [Snowflake](https://www.snowflake.com/) als Data Warehouse erstellt. Wir möchten zwar, dass unsere Blöcke mit so vielen Data Warehouses wie möglich funktionieren, aber einige SQL-Funktionen können sich in Bezug auf Verfügbarkeit, Syntax oder Verhalten in verschiedenen Dialekten unterscheiden.
{% endalert %}

{% alert warning %}
Achten Sie auf unterschiedliche Namenskonventionen! Benutzerdefinierte Namen können zu Unstimmigkeiten in den Daten führen, wenn Sie nicht alle entsprechenden Namen ändern. Wenn Sie die Namen von Ansichten/Tabellen oder Modellen angepasst haben, benennen Sie sie in LookML in den von Ihnen gewählten Namen um.
{% endalert %}

#### Verfügbare Blöcke

| Block | Beschreibung |
|---|---|
| Block zur Analyse der Nachrichteninteraktion | Dieser Block enthält Daten zu Push-, E-Mail-, In-App-Nachrichten, Webhook-, News Feed-, Conversion-, Canvas-Eintrags- und Kampagnensteuerungsgruppen-Eintragsereignissen. <br><br>Erfahren Sie mehr über diesen [Looker Block](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) oder schauen Sie sich den [GitHub-Code](https://github.com/llooker/braze_message_engagement_block) an. |
| Block zur Analyse des Benutzerverhaltens | Dieser Block enthält Daten zu benutzerdefinierten Ereignissen, Käufen, Sitzungen, Standortereignissen und Deinstallationen.<br><br>Erfahren Sie mehr über diesen [Looker Block](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) oder schauen Sie sich den [GitHub-Code](https://github.com/llooker/braze_retention_block) an. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Looker-Aktionen

Mit Looker Actions können Sie Benutzer in Braze über den REST API-Endpunkt von einem Looker Look aus markieren. Aktionen erfordern, dass eine Dimension mit `braze_id` gekennzeichnet ist. Die Aktion fügt den markierten Wert an das benutzerdefinierte Attribut `looker_export` des Benutzers an.

{% alert important %}
Nur bestehende Benutzer werden markiert. Sie können keine Pivot-Looks verwenden, wenn Sie Daten in Braze markieren.
{% endalert %}

#### Schritt 1: Richten Sie eine Lötlooker-Aktion ein

Richten Sie eine Braze Looker Action mit Ihrem Braze REST API-Schlüssel und REST-Endpunkt ein.

![Die Looker Braze Konfigurationsseite. Hier finden Sie Felder für den Braze API-Schlüssel und den Braze REST API-Endpunkt.][12]

#### Schritt 2: Looker Develop einrichten

Wählen Sie in Looker Develop die entsprechenden Ansichten aus. Fügen Sie `braze_id` zum Dimensions-Tag hinzu und übertragen Sie die Änderungen.
Dieses `braze_id` Tag wird verwendet, um zu bestimmen, welches Feld der eindeutige Schlüssel ist.

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**Stellen Sie sicher, dass Sie die Änderungen übertragen. Looker Action funktioniert nur mit Produktionseinstellungen.**

#### Schritt 3: Benutzerattribute in Tags festlegen

Optional kann jedes Attribut mit Hilfe eines `braze[]` -Tags mit dem Attributnamen in den Klammern gesetzt werden. Wenn Sie zum Beispiel ein benutzerdefiniertes Attribut `user_segment` senden möchten, würde der Tag `braze[user_segment]` lauten.

Beachten Sie die folgenden Einschränkungen:
- Attribute werden nur gesendet, wenn sie **als Feld im Look enthalten** sind.
- Unterstützte Typen sind `Strings`, `Boolean`, `Numbers` und `Dates`.
- Bei Attributnamen wird zwischen Groß- und Kleinschreibung unterschieden.
- Standardattribute können ebenfalls festgelegt werden, solange sie genau mit den Namen der [Standardbenutzerprofile]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields) übereinstimmen.
- Der vollständige Tag sollte in Anführungszeichen formatiert werden. Zum Beispiel: `tags: ["braze[first_name]"]`. Andere Tags können ebenfalls zugewiesen werden, werden dann aber ignoriert.
- Weitere Informationen finden Sie auf [GitHub](https://github.com/looker/actions/tree/master/src/actions/braze).

#### Schritt 4: Senden Sie die Looker-Aktion

1. Klicken Sie innerhalb eines Looks mit einer ausgewählten `braze_id` Dimension auf das Einstellungszahnrad ( <i class="fas fa-cog"></i> ) oben rechts, und wählen Sie **Senden....**
2. Wählen Sie die benutzerdefinierte Lötaktion.
3. Geben Sie unter **Eindeutiger Schlüssel** den primären Benutzerzuordnungsschlüssel für das Braze-Konto an (`external_id` oder `braze_id`).
4. Geben Sie dem Export einen Namen. Wenn keine Angabe gemacht wird, wird `LOOKER_EXPORT` verwendet.
5. Wählen Sie unter **Erweiterte Optionen** die Option **Ergebnisse in Tabelle** oder **Alle Ergebnisse** und dann **Senden**.<br><br>![][13]<br><br>Wenn der Export korrekt gesendet wurde, sollte `LOOKER_EXPORT` im Profil des Benutzers als benutzerdefiniertes Attribut mit dem Wert erscheinen, den Sie in der Aktion eingegeben haben.<br><br>![][14]

##### Beispiel ausgehende API

Im Folgenden finden Sie ein Beispiel für einen ausgehenden API-Aufruf, der an den [Endpunkt`/users/track/` ][10] gesendet wird.

###### Header
```
Authorization: Bearer [API_KEY]
```

###### Textkörper
```json
{
   "attributes" : [
      {
        "external_id" : "user_01",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_02",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_03",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      .....
   ]
}
```

### Segmentierte Benutzer in Braze {#segment-users}

Um in Braze ein Segment dieser markierten Benutzer zu erstellen, navigieren Sie zu **Segmente** unter **Engagement**, benennen Sie Ihr Segment und wählen Sie **Looker_Export** als Filter. Als nächstes verwenden Sie die Option "Wert einschließen" und geben das benutzerdefinierte Attribut-Flag an, das Sie in Looker zugewiesen haben.

![Im Braze Segment Builder wird der Filter "looker_export" auf "includes_value" und "Looker" gesetzt.][15]

Sobald Sie es gespeichert haben, können Sie dieses Segment bei der Erstellung von Canvas oder Kampagnen im Schritt "Benutzer ansprechen" verwenden.

## Fehlersuche
Wenn Sie Probleme mit der Looker-Aktion haben, fügen Sie einen Testbenutzer zu [interne Gruppen][16] ] hinzu und überprüfen Sie, ob die folgenden Punkte erfüllt sind:

* Der API-Schlüssel hat die Berechtigung `users.track`.
* Der richtige REST-Endpunkt wird eingegeben, z. B. `https://rest.iad-01.braze.com`.
* Ein `braze_id` Tag wird in der Dimensionsansicht gesetzt.
* Ihre Abfrage enthält die Dimension oder das Attribut Id als Spalte.
* Looker-Ergebnisse werden nicht gedreht.
* Der eindeutige Schlüssel ist korrekt ausgewählt. Normalerweise ist die `external_id`.
* `braze_id` in der Dimension unterscheidet sich von `braze_id` in der API. `braze_id` in der Dimension wird verwendet, um anzuzeigen, dass es sich um das Feld `id` für die Braze API handelt. Für die meisten Zwecke ist auf `external_id` der Primärschlüssel.
* Der `external_id` Benutzer existiert in der Braze Plattform.
* Das Feld `looker_export` ist als `Automatically Detect` unter `Braze Platform > Settings > Manage Settings > Custom Attributes` eingestellt.
* Die Änderungen werden in die Produktion übernommen. Looker Action arbeitet mit Produktionseinstellungen.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/advanced_topics/how_braze_uses_currents/
[2]: https://github.com/llooker/braze_message_engagement_block/blob/master/README.md
[3]: https://github.com/llooker/braze_retention_block/blob/master/README.md
[4]: {{site.baseurl}}//user_guide/onboarding_with_braze/integration/
[5]: {{site.baseurl}}/partners/braze_currents/about/
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/
[7]: https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct
[8]: https://dashboard.braze.com/app_settings/developer_console/
[9]: {{site.baseurl}}/api/basics/#endpoints
[10]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[11]: {% image_buster /assets/img/user_track_api.png %}
[12]: {% image_buster /assets/img/braze-looker-action.png %}
[13]: {% image_buster /assets/img/send-looker-action.png %}
[14]: {% image_buster /assets/img/custom-attributes-looker.png %}
[15]: {% image_buster /assets/img/braze_segments.png %}
[16]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/
