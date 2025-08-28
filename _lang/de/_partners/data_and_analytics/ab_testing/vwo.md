---
nav_title: VWO
article_title: Integration von VWO mit Braze
description: "Erfahren Sie, wie Sie VWO in Braze integrieren können."
alias: /partners/vwo/
page_type: partner
search_tag: Partner
---

# VWO

> [VWO](https://vwo.com/) ist eine leistungsstarke Experimentierplattform, die Marken hilft, wichtige Metriken zu verbessern, indem sie Teams in die Lage versetzt, Programme zur Optimierung der Konversion auf der Grundlage von Daten zum Kundenverhalten durchzuführen. Mit VWO können Sie Kundendaten vereinheitlichen, Insights über das Verhalten gewinnen, Hypothesen aufstellen, A/B-Tests über mehrere Plattformen (Server, Web und Mobile) durchführen, Features einführen, Erlebnisse personalisieren und die gesamte Customer Journey optimieren.

Durch die Integration von VWO mit Braze können Sie VWO-Experimentdaten nutzen, um gezielte Segmente zu erstellen und personalisierte Kampagnen zuzustellen.

## Voraussetzungen

| Anforderung     | Beschreibung |
|-----------------|-------------|
| VWO-Konto     | Ein VWO-Konto mit Zugang zu Experimentierdaten. |
| Braze-Konto   | Ein aktives Braze-Konto mit Integration des [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) auf Ihrer Webseite. Sie müssen auch die Segmentierung der Eigenschaften von Ereignissen aktivieren. Um sie anzufordern, siehe [Überlegungen](#request-event-property-segmentation). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Integration von VWO mit Braze

### Schritt 1: Aktivieren Sie die Integration von Braze in VWO

1. Melden Sie sich bei Ihrem VWO-Konto an.
2. Gehen Sie im Dashboard des VWO zu **Konfigurationen > Integrationen.** Hier können Sie Integrationen auf Workspace-Ebene aktivieren, wodurch die Integration standardmäßig auf alle zukünftigen Kampagnen angewendet wird.

   ![VWO Integration Konfiguration]({% image_buster /assets/img/vwo/vwo1_settings.png %})

4. Wählen Sie die Braze Integration aus, um sie zu aktivieren.
5. Optional können Sie die Integration von Braze für alle bestehenden Kampagnen aktivieren. Wählen Sie dazu eine Kampagne aus, gehen Sie dann zu **Konfiguration > Integrationen** und aktivieren Sie Braze.

   ![Enablement der Braze Integration]({% image_buster /assets/img/vwo/vwo2_enable_braze.png %})

6. Nachdem Sie die Integration aktiviert haben, beginnt VWO damit, Experimentdaten auf Kampagnen-Ebene an Braze zu senden.

### Schritt 2: Erstellen eines Segments in Braze mit VWO Event-Eigenschaften

1. Wählen Sie auf dem Braze-Dashboard **Segmente** > **\+ Segment erstellen**.
3. Geben Sie im Fenster **Segment erstellen** einen Namen für das Segment ein und wählen Sie dann **Segment erstellen**.
4. Wählen Sie in Ihrem neu erstellten Segment **Filter** > **Filter hinzufügen** und wählen Sie dann als Filtertyp **Angepasstes Event**.
6. Suchen Sie in der Filter-Dropdown-Liste nach **VWO**.
7. Wählen Sie die entsprechende VWO-Eigenschaft aus und geben Sie den gewünschten Wert an.
8. Konfigurieren Sie bei Bedarf die Anzahl der Besuche und den Zeitrahmen. Wenn Sie fertig sind, wählen Sie **Speichern**.

   ![Braze Segmente erstellen]({% image_buster /assets/img/vwo/vwo3_braze_segment.png %})

9. Um die Anzahl der Nutzer:innen anzuzeigen, die Ihren Segmentierungskriterien entsprechen, wählen Sie **Exakte Statistik berechnen**.

   ![Braze Segmente Statistik]({% image_buster /assets/img/vwo/vwo4_braze_segment_calculate_size.png %})

## Datenfluss

VWO sendet die Daten der Kampagnen-Experimente als angepasstes Event im folgenden Format an Braze:

- **Name der Veranstaltung:** VWO
- **Event-Eigenschaften:** `vwo_campaign_name`, `vwo_variation_name`

{% alert tip %}
Diese angepassten Event-Eigenschaften können auch zur Segmentierung und zum Targeting verwendet werden.
{% endalert %}

## Überlegungen

### Segmentierung der Eigenschaften von Ereignissen anfragen

Bevor Sie die Segmentierung der Eigenschaften von Ereignissen verwenden können, müssen Sie sie in Braze aktivieren. Verwenden Sie das folgende Template, um Ihren Braze CSM oder das Support Team für den Zugang zu kontaktieren.

   <table>
   <thead>
      <tr>
         <th>Feld</th>
         <th>Details</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Betreff</strong></td>
         <td>Anfrage zur Aktivierung der Segmentierung von Eigenschaften von Ereignissen für die VWO Integration</td>
      </tr>
      <tr>
         <td><strong>Textkörper</strong></td>
         <td>
         Hallo Braze Team,<br><br>
         Wir möchten die Segmentierung der Eigenschaften von Ereignissen aktivieren, die von unserer VWO&lt;>Braze Integration gesendet werden. Hier sind die Details:<br><br>
         - <strong>Name der Veranstaltung:</strong> VWO<br>
         - <strong>Event-Eigenschaften:</strong> <code>vwo_campaign_name</code>, <code>vwo_variation_name</code><br><br>
         Bitte bestätigen Sie, sobald die Eigenschaften in unserem Konto aktiviert wurden.<br><br>
         Ich danke Ihnen.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Braze Datenpunkte

Das angepasste Event, das von VWO an Braze gesendet wird - einschließlich aller für die Segmentierung aktivierten Event-Eigenschaften - wird Datenpunkte in Ihrer Braze-Instanz verbrauchen.

### Beschränkungen

Derzeit unterstützt diese Integration keine Realtime-Synchronisation von Testdaten. Es kann eine Verzögerung von bis zu 15 Minuten geben, bis die Daten in Braze erscheinen.

## Fehlersuche

Wenn Sie keine VWO-Daten in Braze sehen:

1. Klicken Sie mit der rechten Maustaste auf die Seite, auf der Ihre Testkampagne läuft, und wählen Sie **Element inspizieren**.
2. Suchen Sie auf dem Tab **Netzwerk** nach **Braze**, um die Netzwerkanrufe für Braze zu filtern.
3. Die Netzwerkaufrufe werden beim Laden der Seite aufgefüllt. Sie können die Seite neu laden, um die Netzwerkanrufe zu sehen.
4. Wählen Sie einen Netzanruf aus, um weitere Details zu sehen.
5. Gehen Sie zum Abschnitt **Payload der Anfrage** im Tab **Payload**, wo Sie Events: finden, die den Namen: **ce** tragen, der auf Custom Event hinweist.
6. Erweitern Sie 0: und Daten:, um n zu sehen: "VWO" (Name des angepassten Events) und p: {vwo_campaign_name: "<your vwo campaign name>", vwo_variation_name: "<variation name>"}. Diese zeigen an, dass die Werte von VWO an Braze gepusht werden.

 ![Braze Fehlerbehebung]({% image_buster /assets/img/vwo/vwo5_troubleshooting.png %})

Wenn Sie zusätzliche Unterstützung benötigen, wenden Sie sich an Ihren Customer-Success-Manager von VWO.
