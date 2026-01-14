---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Looker, einer Business-Intelligence- und Big-Data-Analytics-Plattform."
page_type: partner
search_tag: Partner

---

# [![Braze Lernangebote]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Looker

> [Looker](https://looker.com/), eine Business-Intelligence- und Big-Data-Analytics-Plattform, ermöglicht es Ihnen, Realtime Business Analytics nahtlos zu erforschen, zu analysieren und zu teilen.

Die Integration von Braze und Looker erlaubt es Nutzern:innen von Braze, die Markierung von [Looker Blocks](#looker-blocks) und [Looker-Aktionen](#looker-actions) durch Nutzer:innen über die REST API zu nutzen. Diese markierten Nutzer:innen können zu Segmenten hinzugefügt werden, um zukünftige Kampagnen oder Canvase [zu targetieren](#segment-users). Um Looker mit Braze zu verwenden, empfehlen wir Ihnen, Ihre Braze-Daten [mit Braze-Currents an ein Data Warehouse zu senden]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) und dann die Looker Blocks von Braze zu verwenden, um Ihre Braze-Daten in Looker schnell zu modellieren und zu visualisieren.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
|Looker Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Looker-Konto](https://looker.com/). |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/) ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Beschränkungen

- Dieser Vorgang funktioniert nur mit Daten, die nicht gepivotet wurden.
- Die API verarbeitet maximal 100.000 Zeilen auf einmal.
- Die endgültige Anzahl der Nutzer:in kann aufgrund von Duplikaten oder Nicht-Nutzern niedriger ausfallen.

## Integration

### Looker Blocks

Mit unseren Looker Blocks können Braze-Kunden schnell auf eine Ansicht der granularen Daten zugreifen, die wir über [Currents]({{site.baseurl}}/partners/braze_currents/about/) anbieten. Unsere Blöcke bieten vorgefertigte Visualisierungen und Modellierungen für Currents-Daten, so dass Braze-Kunden auf einfache Weise Analysemuster wie die Bindung von Kunden, die Zustellbarkeit von Nachrichten, einen detaillierteren Blick auf das Nutzerverhalten und mehr umsetzen können.

Um die Looker Blocks zu implementieren, folgen Sie den Anweisungen in den README-Dateien des GitHub Codes.
- [Analytics-Block für das Engagement von Nachrichten README](https://github.com/llooker/braze_message_engagement_block/blob/master/README.md)
- [Block für Verhaltensanalysen Nutzer:in README](https://github.com/llooker/braze_retention_block/blob/master/README.md)

Beide Integrationen setzen voraus, dass Ihre [ursprüngliche Braze Integration]({{site.baseurl}}/user_guide/onboarding_with_braze/integration/) sowie Ihre Braze Integration mit einem Looker-kompatiblen [Data Warehouse](https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) entsprechend konfiguriert ist, um die erforderlichen Daten zu erfassen und zu senden.


{% alert important %}
Braze hat unsere Looker Blocks mit [Snowflake](https://www.snowflake.com/) als Data Warehouse erstellt. Wir sind zwar bestrebt, dass unsere Blöcke mit möglichst vielen Data Warehouses funktionieren, aber einige SQL-Funktionen können sich in Bezug auf Verfügbarkeit, Syntax oder Verhalten in verschiedenen Dialekten unterscheiden.
{% endalert %}

{% alert warning %}
Achten Sie auf unterschiedliche Namenskonventionen! Angepasste Namen können zu Unstimmigkeiten in den Daten führen, wenn Sie nicht alle entsprechenden Namen ändern. Wenn Sie die Namen von Ansichten/Tabellen oder Modellen angepasst haben, benennen Sie sie in der LookML in den von Ihnen ausgewählten Namen um.
{% endalert %}

#### Verfügbare Blöcke

| Block | Beschreibung |
|---|---|
| Analytics-Block für das Engagement von Nachrichten | Dieser Block enthält Daten zu Push-, E-Mail-, In-App-Nachrichten, Webhook-, Konversions-, Canvas-Eingangs- und Kampagnen-Kontrollgruppen-Events. <br><br>Erfahren Sie mehr über diesen [Looker Block](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), oder sehen Sie sich den [GitHub Code](https://github.com/llooker/braze_message_engagement_block) an. |
| Block für Verhaltensanalysen des Nutzer:innen | Dieser Block enthält Daten zu angepassten Events, Käufen, Sitzungen, Standort-Events und Deinstallationen.<br><br>Erfahren Sie mehr über diesen [Looker Block](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct), oder sehen Sie sich den [GitHub Code](https://github.com/llooker/braze_retention_block) an. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Looker-Aktionen

Mit Looker-Aktionen können Sie Nutzer:innen in Braze über den Endpunkt der REST API von einem Looker-Look aus markieren. Aktionen setzen voraus, dass eine Dimension mit dem Tag `braze_id` versehen ist. Die Aktion fügt den markierten Wert an das angepasste Attribut `looker_export` des Nutzers:innen an.

{% alert important %}
Nur bestehende Nutzer:innen werden markiert. Sie können keine Pivot-Looks verwenden, wenn Sie Daten in Braze markieren.
{% endalert %}

#### Schritt 1: Einrichten einer Braze Looker-Aktion

Richten Sie eine Braze Looker-Aktion mit Ihrem Braze REST API-Schlüssel und Ihrem REST-Endpunkt ein.

![Die Looker Braze Konfigurationsseite. Hier finden Sie Felder für den Braze API-Schlüssel und den Braze REST API Endpunkt.]({% image_buster /assets/img/braze-looker-action.png %})

#### Schritt 2: Looker Develop einrichten

Wählen Sie in Looker Develop die entsprechenden Ansichten aus. Fügen Sie `braze_id` zum Tag dimensions hinzu und bestätigen Sie die Änderungen.
Dieser `braze_id` Tag wird verwendet, um zu bestimmen, welches Feld der eindeutige Schlüssel ist.

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**Stellen Sie sicher, dass Sie die Änderungen übertragen. Looker-Aktionen funktionieren nur mit Produktionseinstellungen.**

#### Schritt 3: Nutzer:innen-Attribute in Tags festlegen

Optional kann jedes Attribut über einen `braze[]` Tag mit dem Attributnamen in den Klammern festgelegt werden. Wenn Sie zum Beispiel ein angepasstes Attribut `user_segment` senden möchten, würde der Tag `braze[user_segment]` lauten.

Beachten Sie die folgenden Einschränkungen:
- Attribute werden nur gesendet, wenn sie **als Feld im Look enthalten** sind.
- Unterstützte Typen sind `Strings`, `Boolean`, `Numbers` und `Dates`.
- Bei den Namen der Attribute wird zwischen Groß- und Kleinschreibung unterschieden.
- Standardattribute können ebenfalls festgelegt werden, solange sie genau mit den Namen der [Nutzerprofile]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields) übereinstimmen.
- Der vollständige Tag sollte in Anführungszeichen formatiert werden. Zum Beispiel: `tags: ["braze[first_name]"]`. Andere Tags können ebenfalls zugewiesen werden, werden dann aber ignoriert.
- Weitere Informationen finden Sie auf [GitHub](https://github.com/looker/actions/tree/master/src/actions/braze).

#### Schritt 4: Senden Sie die Looker-Aktion

1. Klicken Sie innerhalb eines Looks, für den eine Dimension `braze_id` ausgewählt ist, auf das Einstellungsrad ( <i class="fas fa-cog"></i> ) oben rechts und wählen Sie **Senden....**
2. Wählen Sie die angepasste Braze-Aktion aus.
3. Geben Sie unter **Eindeutiger Schlüssel** den primären Nutzer:innen-Abbildungsschlüssel für das Braze-Konto an (`external_id` oder `braze_id`).
4. Geben Sie dem Export einen Namen. Wenn keine Angabe gemacht wird, wird `LOOKER_EXPORT` verwendet.
5. Wählen Sie unter **Erweiterte Optionen** **Ergebnisse in Tabelle** oder **Alle Ergebnisse** und dann **Senden**.<br><br>![]({% image_buster /assets/img/send-looker-action.png %})<br><br>Wenn der Export korrekt gesendet wurde, dann sollte `LOOKER_EXPORT` im Profil des Nutzers:in als angepasstes Attribut mit dem Wert erscheinen, den Sie in der Aktion eingegeben haben.<br><br>![]({% image_buster /assets/img/custom-attributes-looker.png %})

##### Beispiel einer ausgehenden API

Im Folgenden finden Sie ein Beispiel für einen ausgehenden API-Aufruf, der an den [Endpunkt`/users/track/` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) gesendet wird.

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

### Segmentierung der Nutzer:innen in Braze {#segment-users}

Um in Braze ein Segment dieser markierten Nutzer:innen zu erstellen, navigieren Sie zu **Segmente** unter **Engagement**, benennen Sie Ihr Segment und wählen Sie **Looker_Export** als Filter. Als nächstes verwenden Sie die Option "Wert einschließen" und geben das angepasste Attribut-Flag an, das Sie in Looker zugewiesen haben.

![Im Braze Segment Builder wird der Filter "looker_export" auf "includes_value" und "Looker" gesetzt.]({% image_buster /assets/img/braze_segments.png %})

Einmal gespeichert, können Sie dieses Segment bei der Erstellung von Canvas oder Kampagnen im Schritt Targeting Nutzer:innen referenzieren.

## Fehlersuche
Wenn Sie Probleme mit der Looker-Aktion haben, fügen Sie einen Testnutzer:in zu [interne Gruppen]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/) hinzu und überprüfen Sie, ob die folgenden Punkte erfüllt sind:

* Der API-Schlüssel hat die Berechtigungen `users.track`.
* Der richtige REST-Endpunkt wird eingegeben, z. B. `https://rest.iad-01.braze.com`.
* Ein `braze_id` Tag wird in der Dimensionsansicht gesetzt.
* Ihre Abfrage enthält die Dimension ID oder das Attribut als Spalte.
* Looker-Ergebnisse werden nicht gedreht.
* Der eindeutige Schlüssel ist korrekt ausgewählt. Normalerweise ist die `external_id`.
* `braze_id` in der Dimension unterscheidet sich von `braze_id` in der API. `braze_id` in der Dimension wird verwendet, um anzuzeigen, dass es sich um das Feld `id` für die Braze API handelt. Für die meisten Zwecke ist auf `external_id` der Primärschlüssel.
* Die Nutzer:innen von `external_id` existieren auf der Braze Plattform.
* Das Feld `looker_export` ist als `Automatically Detect` unter `Braze Platform > Settings > Manage Settings > Custom Attributes` eingestellt.
* Die Änderungen werden in die Produktion übernommen. Looker Action arbeitet mit Produktionseinstellungen.

