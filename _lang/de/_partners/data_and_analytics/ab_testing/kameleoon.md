---
nav_title: Kameleoon
article_title: Kameleoon
description: "Lernen Sie, wie Sie Kameleoon in Braze integrieren können"
alias: /partners/kameleoon/
page_type: partner
search_tag: Partner
---

# Kameleoon

>[Kameleoon](https://www.kameleoon.com) ist eine Optimierungslösung mit experimentellen, KI-gestützten Personalisierungs- und Feature-Management-Funktionen in einer einzigen, einheitlichen Plattform.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Anforderung | Beschreibung |  
| --- | --- |  
| Kameleoon Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Kameleoon-Konto.|  
| Braze-Konto| Ein aktives Braze-Konto mit Integration des [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) auf Ihrer Webseite. Sie müssen auch die Segmentierung der Eigenschaften von Ereignissen aktivieren. Um sie anzufordern, lesen Sie bitte unter [Überlegungen](#considerations) nach.|  
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Anwendungsfälle

Kameleoon sendet angepasste Events an Braze, um Nutzer:in zu identifizieren, die an Experimentier- und Personalisierungskampagnen teilnehmen, und ermöglicht so ein präziseres Targeting und personalisierte Nachrichten.

## Integration von Kameleoon

Diese Integration läuft als JavaScript-Tracker über Kameleoon's engine.js. Es kann schnell von der Kameleoon-Plattform aus aktiviert werden.

### Schritt 1: Gehen Sie zur Seite Kameleoon Integrationen

Wählen Sie in Ihrer Kameleoon App **Admin** und dann **Integrationen** in der Seitenleiste.

![Das Admin Panel der Kameleoon Plattform.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### Schritt 2: Installieren Sie das Tool Braze

Standardmäßig ist das Tool Braze nicht installiert. Suchen Sie nach dem Braze-Symbol und wählen Sie dann **das Tool installieren**. ![Ein graues Quadrat mit einem nach unten zeigenden Pfeil.]({% image_buster /assets/img/kameleoon/img_2.png %})

Wählen Sie die Projekte aus, für die Sie das Braze-Tool aktivieren möchten, damit die Daten von Kameleoon korrekt an Braze gemeldet werden.

![Das Symbol für das Werkzeug Braze in Kameloon.]({% image_buster /assets/img/kameleoon/img_3.png %})

Nachdem Sie das Tool konfiguriert haben, wählen Sie **Validieren** aus, um das Panel für die Konfiguration zu schließen. Neben dem Symbol des Braze-Tools sehen Sie dann ein Umschalten **auf EIN** und die Anzahl der Projekte, für die das Tool konfiguriert ist.

![Das Werkzeug Braze ist in Kameleoon auf "Ein" umgeschaltet.]({% image_buster /assets/img/kameleoon/img_4.png %})

{% alert important %}  
Dieses Feature befindet sich in der Beta-Phase. Nehmen Sie am [Kameleoon Beta-Programm](https://help.kameleoon.com/account-and-team-management/join-beta-program/) teil, um diese Integration zu nutzen.  
{% endalert %}  
    
### Schritt 3: Verbinden Sie Braze mit Kampagnen von Kameleoon

#### Im Grafik/Code-Editor

Um Ihr Experiment abzuschließen, wählen Sie den Schritt **Integrationen**, um Braze als Tracking-Tool zu konfigurieren, und wählen Sie dann **Braze** aus.

![Das Integrations-Dashboard in Kameleoon zeigt alle verfügbaren Integrationen, einschließlich der aktiven Integration Braze.]({% image_buster /assets/img/kameleoon/img_5.png %})

Braze wird in der Zusammenfassung erwähnt, bevor Sie live gehen. Kameleoon überträgt die Daten automatisch an Braze, und Sie können sie direkt in Braze für die Analyse und Segmentierung verwenden.

##### Personalisierung erstellen

Auf der Seite **zur Erstellung der Personalisierung** können Sie Braze unter den Berichtstools auswählen, um Ihre Berichte zu personalisieren.

![Der Abschnitt Reporting Tools zeigt Integrationen wie Heap, Mixpanel, Clarity, mit ausgewähltem Braze.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### Erstellung von Feature-Flags

Richten Sie die Integration in der Feature-Flag Umgebung im Abschnitt **Integrationen** ein. Aktivieren Sie es für die Umgebungen, in denen es aktiv sein soll.

![Die Seite Feature-Flag in Kameleoon mit den verfügbaren Integrationen. Für jeden Partner gibt es zwei Schalter, "Zustellungsregeln" und "Feature-Experimente".]({% image_buster /assets/img/kameleoon/img_7.png %})

##### Ergebnis-Seite

Nachdem Braze als Berichtstool für ein Experiment festgelegt wurde, können Sie es auf der Kameleoon-Ergebnisseite im **Konfigurationsmenü des Experiments** auswählen (oder die Auswahl aufheben).

{% alert note %}  
Diese Integration erfordert eine [hybride Implementierung](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics) und ist nur mit Web-SDKs kompatibel.
{% endalert %}

![Das seitliche Panel der Ergebnisseite in Kameleoon.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

Die mit dem Experiment verbundenen Berichtstools werden angezeigt. Wählen Sie **Bearbeiten**, um diese Auswahl zu bearbeiten.

### Schritt 4: Analysieren und nutzen Sie Ihre Kameleoon Daten in Braze

Nachdem die Integration eingerichtet ist, sendet Kameleoon angepasste Events namens `kameleoon_exposure` mit Eigenschaften wie **Experimentname**, **Experiment-ID**, **Variationsname**, **Variations-ID** an Braze.

![Das angepasste Event-Benutzerprotokoll in Braze, das ein Beispiel für die Nutzlast des Events zeigt, das Braze von Kameleoon erhalten hat.]({% image_buster /assets/img/kameleoon/img_9.png %})

Sie können diese Daten dann in den angepassten Events einsehen, angepasste Event-Berichte erstellen, um die Exposition von Kameleoon Kampagnen zu ermitteln, und eine Segmentierung auf der Grundlage von Event-Eigenschaften aktivieren. Sie können angepasste Events verwenden, wenn Sie nachfolgende oder verknüpfte Kampagnen und Canvase über [Aktions-Pfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/#action-groups), [aktionsbasierte Auslöser]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery) oder die Erstellung von [Segmenten]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) erstellen.

Außerdem werden diese Events über [angepasste Event-Objekte von Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) zugänglich sein, um eine umfassende Berichterstattung und Analyse zu ermöglichen.

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
         <td>Anfrage zum Enablement der Segmentierung von Eigenschaften für die Integration von Kameleoon</td>
      </tr>
      <tr>
         <td><strong>Textkörper</strong></td>
         <td>
         Hallo Braze Team,<br><br>
         Wir möchten die Segmentierung der Eigenschaften von Ereignissen aktivieren, die von unserer Kameleoon&lt;>Braze Integration gesendet werden. Hier sind die Details:<br><br>
         - <strong>Name der Veranstaltung:</strong> Kameleoon<br>
         - <strong>Event-Eigenschaften:</strong> <code>kameleoon_campaign_name</code>, <code>kameleoon_variation_name</code><br><br>
         Bitte bestätigen Sie, sobald die Eigenschaften in unserem Konto aktiviert wurden.<br><br>
         Ich danke Ihnen.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Braze Datenpunkte

Das angepasste Event, das von Kameleoon an Braze gesendet wird - einschließlich aller für die Segmentierung aktivierten Event-Eigenschaften -, protokolliert Datenpunkte in Ihrer Braze-Instanz.