## Analytik anzeigen

Sobald Sie Ihre Kampagne gestartet haben, können Sie zur Detailseite dieser Kampagne zurückkehren, um die wichtigsten Kennzahlen einzusehen. Navigieren Sie zur Seite **Kampagnen** und wählen Sie Ihre Kampagne aus, um die Detailseite zu öffnen.{% if include.channel != "banner" %} Für {% if include.channel == "Content Card" %}Content-Cards {% elsif include.channel == "banner" %}Banner {% elsif include.channel == "email" %}E-Mail {% elsif include.channel == "in-app message" %}In-App-Nachrichten {% elsif include.channel == "push" %}Push-Nachrichten {% elsif include.channel == "SMS" %}SMS-Nachrichten {% elsif include.channel == "whatsapp" %}WhatsApp-Nachrichten {% elsif include.channel == "webhook" %}Webhooks {% endif %}, die in Canvas gesendet werden, beziehen Sie sich auf [Canvas-Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/).{% endif %}

{% alert tip %}
Suchen Sie nach Definitionen für die in Ihrem Bericht aufgeführten Begriffe und Kennzahlen? Siehe unser
  {% if include.channel == "email" %}[Glossar E-Mail-Analytics]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/)
  {% elsif include.channel == "banner" %}[Bericht Metriken Glossar]({{site.baseurl}}/user_guide/data/report_metrics/) und Filter nach Bannern.
  {% elsif include.channel == "Content Card" %}[Bericht Metriken Glossar]({{site.baseurl}}/user_guide/data/report_metrics/) und Filter nach Content-Cards.
  {% elsif include.channel == "in-app message" %}[Bericht Metriken Glossar]({{site.baseurl}}/user_guide/data/report_metrics/) und Filter nach In-App-Nachricht.
  {% elsif include.channel == "push" %}[Bericht Metriken Glossar]({{site.baseurl}}/user_guide/data/report_metrics/) und Filter nach Push.
  {% elsif include.channel == "SMS" %}[Bericht Metriken Glossar]({{site.baseurl}}/user_guide/data/report_metrics/) und Filter nach SMS/MMS und RCS.
  {% elsif include.channel == "whatsapp" %}[Bericht Metriken Glossar]({{site.baseurl}}/user_guide/data/report_metrics/) und Filter nach WhatsApp.
  {% elsif include.channel == "webhook" %}[Bericht Metriken Glossar]({{site.baseurl}}/user_guide/data/report_metrics/) und Filter nach Webhook.{% endif %}
{% endalert %}

Auf der Registerkarte **Kampagnenanalyse** können Sie Ihre Berichte in einer Reihe von Panels einsehen. Es kann sein, dass Sie mehr oder weniger als die in den folgenden Abschnitten aufgelisteten sehen, aber jede hat ihren eigenen nützlichen Zweck.

### Kampagnendetails

Der Bereich **Kampagnendetails** zeigt einen Überblick über die gesamte Leistung Ihrer
  {% if include.channel == "banner" %}Banner.
  {% elsif include.channel == "Content Card" %}Content-Card.
  {% elsif include.channel == "email" %}E-Mail.
  {% elsif include.channel == "in-app message" %}In-App-Nachricht.
  {% elsif include.channel == "push" %}Push-Nachricht.
  {% elsif include.channel == "SMS" %}SMS, MMS und RCS.
  {% elsif include.channel == "whatsapp" %}WhatApp Nachrichten.
  {% elsif include.channel == "webhook" %}Webhook.
  {% endif %}

In diesem Bereich sehen Sie die Gesamtmetriken, wie z.B. die Anzahl der gesendeten Nachrichten an die Anzahl der Empfänger, die primäre Konversionsrate und den Gesamtumsatz, der mit dieser Nachricht erzielt wurde. Auf dieser Seite können Sie auch die Einstellungen für Zustellung, Zielgruppe und Konversion überprüfen.

{% if include.channel == "whatsapp" %}
{% alert note %}
Der WhatsApp-Kanal enthält die Leserate. Diese Metrik wird nur für Benutzer mit aktivierten Lesebestätigungen geliefert, was variieren kann.
{% endalert %}
{% endif %}

{% if include.channel == "Content Card" %}
![Kampagnendetails-Panel mit einer Übersicht über die zur Bestimmung der Kampagnen-Performance verwendeten Metriken.]({% image_buster /assets/img/cc-campaign-details.png %})

{% elsif include.channel == "banner" %}
![Kampagnendetails-Panel mit einer Übersicht über die zur Bestimmung der Kampagnen-Performance verwendeten Metriken.]({% image_buster /assets/img/banners/campaign_details.png %})

{% elsif include.channel == "email" %}
![Kampagnendetails-Panel mit einer Übersicht über die zur Bestimmung der Kampagnen-Performance verwendeten Metriken.]({% image_buster /assets/img/campaign_details_email.png %})

{% elsif include.channel == "push" %}
![Kampagnendetails-Panel mit einer Übersicht über die zur Bestimmung der Kampagnen-Performance verwendeten Metriken.]({% image_buster /assets/img/campaign_details_push.png %})

{% elsif include.channel == "SMS" %}
![Kampagnendetails-Panel mit einer Übersicht über die zur Bestimmung der Kampagnen-Performance verwendeten Metriken.]({% image_buster /assets/img/campaign_details_sms.png %})

{% elsif include.channel == "in-app message" %}
![Kampagnendetails-Panel mit einer Übersicht über die zur Bestimmung der Kampagnen-Performance verwendeten Metriken.]({% image_buster /assets/img/campaign_details_iam.png %})

In Canvas sehen Sie die Performance von In-App-Nachrichten, die dem von Ihnen erstellten Canvas zugeordnet sind. Sie können das Bedienfeld oben auf der Seite verwenden, um andere Nachrichtenarten (Kanäle) zu löschen und nur die In-App-Nachrichten in Ihrem Canvas anzuzeigen.

![]({% image_buster /assets/img/in-app_message_canvas_reporting.png %})

{% elsif include.channel == "webhook" %}
![Kampagnendetails-Panel mit einer Übersicht über die zur Bestimmung der Kampagnen-Performance verwendeten Metriken.]({% image_buster /assets/img/campaign_details_webhook.png %})

{% endif %}

{% if include.channel == "Content Card" %}

#### Kontrollgruppen {#cc-control-group}

Um die Wirkung einer einzelnen Content Card zu messen, können Sie einem A/B-Test eine [Kontrollgruppe]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) hinzufügen. Der Bereich **Kampagnendetails** auf der obersten Ebene enthält keine Metriken aus der Variante Kontrollgruppe.

{% elsif include.channel == "SMS" %}

#### Kontrollgruppen {#sms-control-group}

Um die Auswirkungen einer einzelnen SMS-, MMS- oder RCS-Nachricht zu messen, können Sie einem A/B-Test eine [Kontrollgruppe]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) hinzufügen. Der Bereich **Kampagnendetails** auf der obersten Ebene enthält keine Metriken aus der Variante Kontrollgruppe.

{% elsif include.channel == "whatsapp" %}

#### Kontrollgruppen {#whatsapp-control-group}

Um die Wirkung einer einzelnen WhatsApp-Nachricht zu messen, können Sie eine [Kontrollgruppe]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) zu einem A/B-Test hinzufügen. Der Bereich **Kampagnendetails** auf der obersten Ebene enthält keine Metriken aus der Variante Kontrollgruppe.

{% elsif include.channel == "webhook" %}

#### Kontrollgruppen {#webhook-control-group}

Um die Wirkung einer einzelnen Webhook-Nachricht zu messen, können Sie eine [Kontrollgruppe]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#step-4-choose-a-segment-and-distribute-your-users-across-variants) zu einem A/B-Test hinzufügen. Der Bereich **Kampagnendetails** auf der obersten Ebene enthält keine Metriken aus der Variante Kontrollgruppe.

{% endif %}

#### Änderungen seit letztem Aufruf

Die Anzahl der Aktualisierungen der Kampagne durch andere Mitglieder Ihres Teams wird durch die Metrik *Änderungen seit letzter Ansicht* auf der Kampagnenübersichtsseite verfolgt. Wählen Sie **Änderungen seit der letzten Ansicht**, um ein Änderungsprotokoll der Aktualisierungen des Namens, des Zeitplans, der Tags, der Nachricht, der Zielgruppe, des Genehmigungsstatus oder der Teamzugriffskonfiguration der Kampagne anzuzeigen. Bei jeder Aktualisierung können Sie sehen, wer die Aktualisierung durchgeführt hat und wann. Sie können dieses Changelog verwenden, um Änderungen an Ihrer Kampagne zu überprüfen.

<!--
### Message Performance

The **Message Performance** panel outlines how well your message has performed across various dimensions. The metrics in this panel vary depending on your chosen messaging channel, and whether or not you are running a multivariate test. You can click on the <i class="fa fa-eye preview-icon"></i> **Preview** icon to view your message for each variant or channel.
-->
{% if include.channel == "Content Card" %}
### Leistung der Content-Card

Der Bereich **Leistung der Inhaltskarte** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Dimensionen abgeschnitten hat. Die Metriken in diesem Bereich variieren je nach dem von Ihnen gewählten Nachrichtenkanal und je nachdem, ob Sie einen multivariaten Test durchführen oder nicht. Sie können auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau** klicken, um Ihre Nachricht für jede Variante oder jeden Kanal zu sehen.

![Performance-Analytics von Content-Card-Nachrichten]({% image_buster /assets/img/cc-message-performance.png %})

{% elsif include.channel == "email" %}
### E-Mail-Performance

Im Bereich **E-Mail-Leistung** sehen Sie, wie gut Ihre Nachricht in verschiedenen Bereichen abgeschnitten hat. Die Metriken in diesem Bereich variieren je nach dem von Ihnen gewählten Nachrichtenkanal und je nachdem, ob Sie einen multivariaten Test durchführen oder nicht. Sie können auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau** klicken, um Ihre Nachricht für jede Variante oder jeden Kanal zu sehen.

![Performance-Analytics von E-Mail-Nachrichten]({% image_buster /assets/img_archive/email_message_performance.png %})

{% elsif include.channel == "in-app message" %}
### Leistung von In-App-Nachrichten

Das **In-App Message Performance-Panel** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Bereichen abgeschnitten hat. Die Metriken in diesem Bereich variieren je nach dem von Ihnen gewählten Nachrichtenkanal und je nachdem, ob Sie einen multivariaten Test durchführen oder nicht. Sie können auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau** klicken, um Ihre Nachricht für jede Variante oder jeden Kanal zu sehen.

![Performance-Analytics von In-App-Nachrichten]({% image_buster /assets/img_archive/iam_message_performance.png %})

{% elsif include.channel == "push" %}
### Push-Performance

Das Panel **Push-Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Bereichen abgeschnitten hat. Die Metriken in diesem Bereich variieren je nach dem von Ihnen gewählten Nachrichtenkanal und je nachdem, ob Sie einen multivariaten Test durchführen oder nicht. Sie können auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau** klicken, um Ihre Nachricht für jede Variante oder jeden Kanal zu sehen.

![Leistungsanalyse von Push-Nachrichten]({% image_buster /assets/img_archive/push_message_performance.png %})

{% elsif include.channel == "SMS" %}
### SMS/MMS/RCS-Performance

Das Panel **SMS/MMS/RCS Performance** gibt Aufschluss darüber, wie gut Ihre Nachricht in verschiedenen Bereichen abgeschnitten hat. Die Metriken in diesem Bereich variieren je nach dem von Ihnen gewählten Nachrichtenkanal und je nachdem, ob Sie einen multivariaten Test durchführen oder nicht. Sie können auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau** klicken, um Ihre Nachricht für jede Variante oder jeden Kanal zu sehen.

![SMS/MMS/RCS Performance Panel, das eine Tabelle mit Metriken für eine Kontrollgruppe, Variante 1 und Variante 2 enthält.]({% image_buster /assets/img_archive/sms_message_performance.png %})

{% elsif include.channel == "banner" %}
### Banner-Performance

Das **Banner Performance** Panel zeigt Ihnen, wie gut Ihre Nachricht in den verschiedenen Bereichen abgeschnitten hat. Diese Metriken sind abhängig von Ihrem Messaging-Kanal und davon, ob Sie einen multivariaten Test durchführen oder nicht.

![SMS/MMS-Performance-Panel, das eine Tabelle mit Metriken für eine Kontrollgruppe, Variante 1 und Variante 2 enthält.]({% image_buster /assets/img/banners/banner_performance.png %})

{% elsif include.channel == "webhook" %}
### Webhook-Performance

Das **Webhook-Panel Performance** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Bereichen abgeschnitten hat. Die Metriken in diesem Bereich variieren je nach dem von Ihnen gewählten Nachrichtenkanal und je nachdem, ob Sie einen multivariaten Test durchführen oder nicht. Sie können auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau** klicken, um Ihre Nachricht für jede Variante oder jeden Kanal zu sehen.

![Webhook-Performance-Panel, das eine Tabelle mit Metriken für eine Kontrollgruppe und Variante 1 enthält.]({% image_buster /assets/img/webhook_message_performance.png %})

{% elsif include.channel == "whatsapp" %}
### WhatsApp-Performance

Das **WhatsApp Performance-Panel** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Bereichen abgeschnitten hat. Die Metriken in diesem Bereich variieren je nach dem von Ihnen gewählten Nachrichtenkanal und je nachdem, ob Sie einen multivariaten Test durchführen oder nicht. Sie können auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau** klicken, um Ihre Nachricht für jede Variante oder jeden Kanal zu sehen.

![WhatsApp-Performance-Panel, das eine Tabelle mit Metriken für Variante 1 enthält.]({% image_buster /assets/img/whatsapp_message_performance.png %})

{% endif %}

Wenn Sie Ihre Ansicht vereinfachen möchten, klicken Sie auf <i class="fas fa-plus"></i> **Spalten hinzufügen/entfernen** und löschen Sie alle gewünschten Metriken. Standardmäßig werden alle Metriken angezeigt.

{% if include.channel == "email" %}

#### Heatmaps

Mit Heatmaps können Sie sehen, wie erfolgreich verschiedene Links in einer einzigen E-Mail-Kampagne sind. Gehen Sie im Bereich **Nachrichtenanalyse** zum Bereich **E-Mail-Leistung**. Wählen Sie **Vorschau & Heatmap**, um eine Vorschau auf Ihre E-Mail Kampagne und die Heatmap zu sehen. Alternativ können Sie auch den Hyperlink im Namen der Variante auswählen, um die Heatmap anzuzeigen.

In dieser Ansicht können Sie mit dem Schalter **Heatmap anzeigen** eine visuelle Ansicht Ihrer E-Mail aufrufen, die die Gesamthäufigkeit und den Ort der Klicks innerhalb der Laufzeit der Kampagne anzeigt. Im Bereich **Link-Tabelle nach Gesamtklicks** können Sie alle Links in Ihrer E-Mail-Kampagne anzeigen und nach Gesamtklicks sortieren. Dies kann zusätzliche Insights darüber liefern, wo Ihre Benutzer navigieren. Um eine Kopie der Heatmap für Verweise zu speichern, gehen Sie auf "Herunterladen".

![Beispiel für die Seite Vorschau und Heatmap, die eine E-Mail-Kampagne und ein Panel mit Link-Alias-Beispielen und deren Gesamtklicks enthält.]({% image_buster /assets/img_archive/email_heatmap_example.png %})

#### Bilder

Wir empfehlen Ihnen, CORS für Bild-URLs zu aktivieren, damit Bilder in Heatmap-Vorschauen und Exporten nicht beschädigt werden.

{% endif %}

{% if include.channel == "Content Card" %}

#### Content-Card-Metriken

Im Folgenden finden Sie eine Aufschlüsselung einiger wichtiger Metriken, die Sie bei der Überprüfung Ihrer Nachrichten-Performance sehen können. Die vollständigen Definitionen aller Content Cards-Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/), und filtern Sie nach Content Cards.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrisch</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#messages-sent">Nachrichten gesendet</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Messages Sent' %} <br><br>
                Dies wird unterschiedlich berechnet, je nachdem, was Sie für Folgendes ausgewählt haben: 
                <a href="/docs/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression">Kartenerstellung</a>:<br><br>
                <ul>
                    <li><b>Beim Start oder beim Einstieg in die Stufe:</b> Die Anzahl der erstellten und sichtbaren Karten. Dabei wird nicht berücksichtigt, ob die Benutzer die Karte angesehen haben.</li>
                    <li><b>Auf den ersten Blick:</b> Die Anzahl der Karten, die den Benutzern angezeigt werden.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#total-impressions">Impressionen gesamt</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %} Diese Zahl kann für denselben Nutzer:innen mehrfach erhöht werden.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-impressions">Eindeutige Impressionen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Diese Zahl</span> wird nicht erhöht, wenn ein Nutzer:innen eine Content-Card zum zweiten Mal ansieht.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-recipients">Eindeutige Empfänger:innen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Recipients' %} <br><br> Bei Content-Cards kann jede Content-Card nur einmal empfangen werden. Wenn Sie also dieselbe Content-Card ein zweites Mal ansehen, egal an welchem Tag, wird dieser Wert nicht erhöht. Da ein Betrachter jeden Tag ein einzigartiger Empfänger sein kann, sollten Sie erwarten, dass dieser Wert höher ist als die <i>Unique Impressions</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-clicks">Eindeutige Klicks</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Clicks' %} Dies beinhaltet Klicks auf von Braze bereitgestellte Links zum Abmelden.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data/report_metrics/#unique-dismissals">Eindeutige Ausblendungen</a></td>
            <td>{% multi_lang_include metrics.md metric='Unique Dismissals' %}</td>
        </tr>
    </tbody>
</table>

{% alert note %}
Was die Protokollierung der Impressionen angeht, gibt es einige Unterschiede zwischen Web, Android und iOS. Im Allgemeinen protokolliert Braze eine Impression, wenn eine Karte gesehen wird, d. h. nachdem ein Benutzer zu der entsprechenden Content-Card in seinem Feed gescrollt hat.
{% endalert %}

#### Einzigartige Empfänger versus einzigartige Impressionen

Es gibt einige Metriken, die die Sichtbarkeit Ihrer Nachricht erfassen. Dazu gehören _gesendete Nachrichten_, _eindeutige Empfänger_ und _eindeutige Impressionen_. Insbesondere der Unterschied zwischen _Unique Recipients_ und _Unique Impressions_ kann ein wenig verwirrend sein. Lassen Sie uns ein paar Beispielszenarien verwenden, um diese Metriken besser zu verstehen.

Angenommen, Sie sehen sich heute eine Content-Card an, erhalten morgen eine neue Karte aus derselben Kampagne und übermorgen wieder - dann werden Sie dreimal als _eindeutiger Empfänger_:in gezählt. Sie werden jedoch nur für eine _Eindeutige Impression_ gezählt. Sie werden auch in der Anzahl der _gesendeten Nachrichten_ berücksichtigt, da die Karte auf Ihrem Gerät verfügbar war.

Ein weiteres Beispiel: Nehmen wir an, Sie sehen fünf _Unique Impressions_ für eine Content Card-Kampagne mit 150.000 _gesendeten Nachrichten_. Das bedeutet, dass die Karte (im Backend) einer Zielgruppe von 150.000 Nutzern zur Verfügung gestellt wurde, aber nur die Geräte von fünf Nutzern haben alle folgenden Schritte nach dem Senden ausgeführt:

1. Sie haben eine Sitzung gestartet oder die App hat explizit eine Synchronisierung von Content Cards angefordert (oder beides).
2. Zur Ansicht „Content-Cards“ navigiert
3. SDK hat eine Impression aufgenommen und auf dem Server protokolliert

Ihre _gesendeten Nachrichten_ beziehen sich auf die Inhaltskarten, die gesehen werden können, während sich die _eindeutigen Empfänger_ auf die Inhaltskarten beziehen, die tatsächlich gesehen wurden.

{% elsif include.channel == "banner" %}

### Banner-Metriken

Dies sind die wichtigsten Metriken, die Sie bei der Überprüfung der Performance Ihrer Banner Kampagne tracken sollten. Klicks und Impressionen für Banner werden mit dem SDK automatisch getrackt. 

Die vollständigen Definitionen aller Metriken für Banner finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/), und filtern Sie nach Bannern.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrisch</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Impressionen gesamt</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Eindeutige Impressionen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %} <span style="white-space: nowrap">Jeder Nutzer:innen wird nur einmal gezählt.</span></td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Klicks gesamt</a></td>
            <td class="no-split"><i>Gesamtklicks</i> ist die Gesamtzahl (und der Prozentsatz) der Nutzer, die innerhalb der zugestellten Nachricht geklickt haben, unabhängig davon, ob derselbe Nutzer mehrmals geklickt hat.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Eindeutige Klicks</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Eindeutige Klicks' %} Jeder Nutzer:innen wird nur einmal gezählt.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#primary-conversions">Primäre Konversionen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Primäre Konversionen (A) oder primäres Konversions-Event' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Eindeutige Empfänger:innen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Recipients' %} <br><br> Da ein Betrachter jeden Tag ein einzigartiger Empfänger sein kann, sollten Sie erwarten, dass dieser Wert höher ist als die <i>Unique Impressions</i>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#revenue">Umsatz</a></td>
            <td>{% multi_lang_include metrics.md metric='Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confidence">Vertrauen</a></td>
            <td>{% multi_lang_include metrics.md metric='Confidence' %}</td>
        </tr>
    </tbody>
</table>

#### Einzigartige Empfänger versus einzigartige Impressionen

Es gibt einige Metriken, die die Sichtbarkeit Ihrer Nachricht erfassen. Dazu gehören _gesendete Nachrichten_, _eindeutige Empfänger_ und _eindeutige Impressionen_. Insbesondere der Unterschied zwischen _Unique Recipients_ und _Unique Impressions_ kann ein wenig verwirrend sein. Lassen Sie uns ein paar Beispielszenarien verwenden, um diese Metriken besser zu verstehen.

Angenommen, Sie sehen sich heute ein Banner an, dann morgen dasselbe Banner und übermorgen noch einmal - dann werden Sie dreimal als _eindeutiger Empfänger:in_ gezählt. Sie werden jedoch nur für eine _Eindeutige Impression_ gezählt. Sie werden auch in der Anzahl der _gesendeten Nachrichten_ berücksichtigt, da die Karte auf Ihrem Gerät verfügbar war.

Ein weiteres Beispiel: Nehmen wir an, Sie sehen fünf _eindeutige Impressionen_ auf einer Bannerkampagne mit 150.000 _gesendeten Nachrichten_. Das bedeutet, dass das Banner (im Backend) einer Zielgruppe von 150.000 Nutzern zur Verfügung gestellt wurde, aber nur fünf Nutzer:innen haben alle folgenden Schritte nach dem Senden ausgeführt:

1. Sie haben eine Sitzung gestartet oder die App hat explizit eine Banner-Synchronisierung angefordert (oder beides).
2. Navigiert zur Ansicht Banner
3. SDK hat eine Impression aufgenommen und auf dem Server protokolliert

Ihre _gesendeten Nachrichten_ referenzieren auf die verfügbaren Banner, während _Eindeutige Empfänger:innen_ sich auf die Banner beziehen, die tatsächlich gesehen wurden.

{% elsif include.channel == "email" %}

#### E-Mail-Metriken

Im Folgenden finden Sie einige wichtige E-Mail-spezifische Metriken, die Sie bei anderen Kanälen nicht sehen werden. Die vollständigen Definitionen aller in Braze verwendeten E-Mail-Metriken finden Sie in unserem [E-Mail-Analyse-Glossar]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrisch</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-clicks">Eindeutige Klicks</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Unique Clicks' %} Dies wird über einen Zeitraum von sieben Tagen für E-Mails getrackt und durch <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a> gemessen. Dazu gehören auch Klicks auf die von Braze zur Verfügung gestellten Abmeldelinks. Diese Zahl sollte zwischen 5-10% liegen. Alles, was über 10% liegt, ist außergewöhnlich!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-opens">Eindeutige Öffnungen</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Unique Opens' %} Bei E-Mails wird dies über einen Zeitraum von 7 Tagen getrackt. Diese Zahl sollte zwischen 30-40% liegen. Alles, was über 40% liegt, ist außergewöhnlich!
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#click-to-open-rate">Effektive Klickrate</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#spam">Spam-Rate</a></td>
            <td class="no-split">
                {% multi_lang_include metrics.md metric='Spam' %} Wenn dieser Wert größer als 0,08 ist, könnte das ein Zeichen dafür sein, dass entweder Ihr Nachrichtentext zu verkaufsorientiert ist oder dass Sie Ihre Methoden zur Erfassung von E-Mail-Adressen überdenken sollten (um sicherzustellen, dass Sie diejenigen ansprechen, die an Ihrer Korrespondenz interessiert sind).
            </td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unsubscribers-or-unsub">Abgemeldete Personen oder Abmeldung</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#other-opens">Sonstige Öffnungen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Other Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#estimated-real-opens">Geschätzte reale Öffnungen</a></td>
            <td class="no-split"> {% multi_lang_include metrics.md metric='Estimated Real Opens' %} Einzelheiten finden Sie im folgenden Abschnitt.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#machine-opens">Automatische Öffnungen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Machine Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Absprünge</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Bounces' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#hard-bounce">Hard Bounce</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Hard Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#soft-bounce">Soft Bounce</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Soft Bounce' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deferral">Aufschub</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Deferral' %}</td>
        </tr>
    </tbody>
</table>

##### Aufschübe

Aufgeschoben ist, wenn eine E-Mail nicht sofort zugestellt werden konnte. Braze versucht jedoch, die E-Mail bis zu 72 Stunden nach diesem vorübergehenden Zustellungsfehler erneut zuzustellen, um die Chancen auf eine erfolgreiche Zustellung zu maximieren, bevor die Versuche für diese spezielle Kampagne eingestellt werden. Typische Gründe für Aufschübe sind reputationsbasierte Rate-Limiting des Posteingangs-Anbieters für das E-Mail-Volumen, vorübergehende Verbindungsprobleme oder DNS-Fehler.

_Aufschübe_ unterscheiden sich von _Soft Bounces_. Wenn während dieses Zeitraums keine E-Mail erfolgreich zugestellt wurde, sendet Braze ein Soft Bounce-Ereignis pro versuchter Kampagne. Vor dem 25\. Februar 2025 wurden diese Wiederholungsversuche als mehrere Soft Bounces für 1 gesendete Kampagne gezählt.

Beachten Sie, dass _Aufschübe_ derzeit nur mit Currents oder Braze Snowflake Features (wie Query Builder, SQL Segmente, Snowflake Data Sharing) möglich sind. Wenn Sie dies in Kampagnen- oder Canvas-Analytics berücksichtigen möchten, [senden Sie uns bitte ein Produkt-Feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal).

##### Geschätzte reale Öffnungsrate {#estimated-real-open-rate}

Diese Statistik verwendet ein proprietäres, von Braze entwickeltes Analysemodell, um eine Schätzung der individuellen Öffnungsrate der Kampagne zu rekonstruieren, als ob es keine maschinellen Öffnungen gäbe. Während wir bei einigen Öffnungsereignissen von E-Mail-Absendern die Kennzeichnung *Automatische Öffnung* erhalten (siehe oben), können diese Kennzeichnungen oft tatsächliche Öffnungen als reale Öffnungen kennzeichnen. Mit anderen Worten: Die *anderen Öffnungen* sind wahrscheinlich eine Unterschätzung der tatsächlichen Öffnungen (durch tatsächliche Nutzer). Stattdessen verwendet Braze die Klickdaten der einzelnen Kampagnen, um auf die Rate zu schließen, mit der Menschen die Nachricht tatsächlich geöffnet haben. Dies kompensiert verschiedene Mechanismen zum Öffnen von Geräten, einschließlich Apples MPP.

Die _geschätzte tatsächliche Öffnungsrate_ wird 36 Stunden nach Beginn des E-Mail-Versands berechnet und danach alle 24 Stunden neu berechnet. Wenn sich eine Kampagne wiederholt, wird die Schätzung 36 Stunden nach einem weiteren Versand neu berechnet.

Normalerweise sind etwa 10.000 zugestellte E-Mails erforderlich, damit die Statistik erfolgreich berechnet werden kann, obwohl diese Zahl je nach Klickrate variieren kann. Wenn die Statistik nicht berechnet werden kann, wird in der Spalte "--" angezeigt.

###### Beschränkungen

Die geschätzte reale Öffnungsrate ist nur in Kampagnen verfügbar und wird nicht in Aktuelle Ereignisse angezeigt. Diese Metrik wird nur für aktive Kampagnen, die vor dem 14. November 2023 gestartet wurden, rückwirkend berechnet.

{% elsif include.channel == "in-app message" %}

#### Metriken für In-App-Nachrichten

Im Folgenden finden Sie einige wichtige Metriken für In-App-Nachrichten, die Sie in Ihren Analysen sehen können. Die vollständigen Definitionen aller in Braze verwendeten Metriken für In-App-Nachrichten finden Sie in unserem [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).

{% alert note %}
Die Berichterstattung für _Button 1-Klicks_ und _Button 2-Klicks_ funktioniert nur, wenn Sie in der In-App-Nachricht den **Bezeichner für die Berichterstattung** mit "0" bzw. "1" angeben.

![Das Feld "Bezeichner für die Berichterstattung" mit einem Wert von "0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrisch</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#body-clicks">Klicks auf Text</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Body Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-1-clicks">Klicks auf Button 1</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Button 1 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#button-2-clicks">Klicks auf Button 2</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Button 2 Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-impressions">Eindeutige Impressionen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-impressions">Impressionen gesamt</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversions-b-c-d">Konversionen (B, C, D)</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-conversions">Konversionen gesamt</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Conversions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#conversion-rate">Konversionsrate</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Conversion Rate' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#close-message">Nachricht schließen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Close Message' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "push" %}

#### Push-Metriken

Im Folgenden finden Sie eine Aufschlüsselung einiger wichtiger Metriken, die Sie bei der Überprüfung Ihrer Nachrichten-Performance sehen können. Die vollständigen Definitionen aller Push-Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/), und filtern Sie nach Push.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrisch</th>
            <th>Beschreibung</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#bounces">Absprünge</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Bounces' %} Siehe <a href="#bounced-push">Geplatzte Push-Benachrichtigungen</a>.</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#direct-opens">Direkte Öffnungen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Direct Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opens">Öffnungen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Opens' %}</td>
        </tr>
    </tbody>
</table>

> Die Zustellung von Benachrichtigungen erfolgt nach bestem Wissen und Gewissen durch die Apple Push Notification Services (APNs). Es ist nicht dazu gedacht, Daten an Ihre App zu liefern, sondern nur, um den Benutzer darüber zu informieren, dass neue Daten verfügbar sind. Der wichtige Unterschied ist, dass wir anzeigen, wie viele Nachrichten wir erfolgreich an APNs zugestellt haben, nicht unbedingt, wie viele APNs erfolgreich an Geräte zugestellt wurden.

##### Tracking von Abbestellungen

Push-Abmeldungen werden in der Kampagnen-Analytics nicht als Metrik berücksichtigt. Unter [Verfolgung von Push-Abmeldungen]({{site.baseurl}}/help/help_articles/push/push_unsubscribes) erfahren Sie, wie Sie diese Metrik manuell verfolgen können.

##### Öffnungen verstehen

Auch wenn _Direct Opens_ und _Influenced Opens_ das Wort "Opens" enthalten, handelt es sich dabei um unterschiedliche Metriken. _Direkte Öffnungen_ bezieht sich auf das direkte Öffnen einer Push-Benachrichtigung, wie in der Tabelle oben angegeben. _Beeinflusste Öffnungen_ bezieht sich auf das Öffnen einer App, ohne dass eine Push-Benachrichtigung innerhalb eines bestimmten Zeitrahmens nach Erhalt geöffnet wird. _Beeinflusste Öffnungen_ bezieht sich also auf die App-Öffnungen, nicht auf die Push-Benachrichtigungs-Öffnungen.

##### Warum Push-Sendungen die Zahl der einzelnen Empfänger übersteigen können

Die Anzahl der _Sendungen_ kann die Anzahl der _eindeutigen Empfänger_ aus den folgenden Gründen übersteigen:

- **Die Wiederzulassung ist aktiviert:** Wenn die Wiederzulassung in Ihren Kampagnen- oder Canvas-Einstellungen aktiviert ist, können Benutzer, die das Segment und die Zustellungskriterien erfüllen, dieselbe Push-Benachrichtigung mehrmals erhalten. Dies führt zu einer höheren Anzahl von Gesamtsendungen.
- **Benutzer haben mehrere Geräte:** Wenn die Wiederzulassung nicht aktiviert ist, kann der Unterschied dadurch erklärt werden, dass Benutzer mehrere Geräte mit ihrem Profil verknüpft haben. Ein Benutzer könnte zum Beispiel sowohl ein Smartphone als auch ein Tablet besitzen, und die Push-Benachrichtigung wird an alle registrierten Geräte gesendet. Jede Zustellung zählt als eine Sendung, aber es wird nur ein einziger Empfänger erfasst.
- **Benutzer werden mehreren Apps zugewiesen:** Wenn Benutzer mit mehr als einer App verbunden sind (z.B. beim Testen einer neuen App), erhalten sie möglicherweise dieselbe Push-Benachrichtigung in jeder App. Dies trägt zu einer höheren Anzahl von Sendungen bei.

##### Warum Bounces auftreten {#bounced-push}

{% tabs %}
{% tab Apple Push-Benachrichtigungsdienst %}

Bounces treten bei Apple Push Notification Services (APNs) auf, wenn eine Push-Benachrichtigung versucht, an ein Gerät zuzustellen, auf dem die gewünschte App nicht installiert ist. APNs hat auch das Recht, Token für Geräte beliebig zu ändern. Wenn Sie versuchen, an das Gerät eines Benutzers zu senden, dessen Push-Token sich in der Zeit zwischen der Registrierung des Tokens (z. B. zu Beginn jeder Sitzung, wenn wir einen Benutzer für ein Push-Token registrieren) und dem Zeitpunkt des Sendens geändert hat, würde dies einen Bounce verursachen.

Wenn ein Benutzer Push in seinen Geräteeinstellungen beim nächsten Öffnen einer App deaktiviert, erkennt das SDK, dass Push deaktiviert wurde und benachrichtigt Braze. An diesem Punkt aktualisieren wir den Status von Push aktiviert auf deaktiviert. Wenn ein deaktivierter Benutzer eine Push-Kampagne erhält, bevor er eine neue Sitzung hat, wird die Kampagne erfolgreich gesendet und erscheint als zugestellt. Der Push wird für diesen Benutzer nicht ausgelöst. Wenn Sie im Anschluss an eine Sitzung versuchen, eine Push-Mitteilung an den Benutzer zu senden, weiß Braze bereits, ob wir ein Vordergrund-Token haben, so dass keine Benachrichtigung gesendet wird.

Push-Benachrichtigungen, die vor der Zustellung ablaufen, gelten nicht als fehlgeschlagen und werden nicht als Bounce registriert.

{% endtab %}
{% tab Firebase Cloud Messaging %}

Firebase Cloud Messaging (FCM) Bounces können in drei Fällen auftreten:

| Szenario | Beschreibung |
| -- | -- |
| Nicht installierte Anwendungen | Wenn eine Nachricht versucht, an ein Gerät zugestellt zu werden, und die vorgesehene App auf diesem Gerät deinstalliert wird, wird die Nachricht verworfen und die Registrierungs-ID des Geräts wird ungültig. Alle weiteren Versuche, das Gerät zu benachrichtigen, geben den Fehler NotRegistered zurück. |
| Gesicherte Anwendung | Wenn eine Anwendung gesichert wird, kann ihre Registrierungs-ID ungültig werden, bevor die Anwendung wiederhergestellt wird. In diesem Fall speichert FCM die Registrierungs-ID der Anwendung nicht mehr und die Anwendung wird keine Nachrichten mehr erhalten. Die Registrierungs-IDs sollten daher **nicht** gespeichert werden, wenn eine Anwendung gesichert wird. |
| Aktualisierte Anwendung | Wenn eine Anwendung aktualisiert wird, funktioniert die Registrierungs-ID der vorherigen Version möglicherweise nicht mehr. Daher sollte eine aktualisierte Anwendung ihre bestehende Registrierungs-ID ersetzen. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}


{% elsif include.channel == "SMS" %}

#### SMS-, MMS- und RCS-Metriken

Im Folgenden finden Sie eine Aufschlüsselung einiger wichtiger Metriken, die Sie bei der Überprüfung Ihrer Nachrichten-Performance sehen können. Die vollständigen Definitionen aller SMS-, MMS- und RCS-Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/). Filtern Sie nach SMS/MMS und RCS.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrisch</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sent">Gesendet</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sent' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#delivery-failures">Zustellfehler</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Delivery Failures' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#confirmed-delivery">Bestätigte Zustellung</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Confirmed Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#rejections">Zurückweisungen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Rejections' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#opt-out">Opt-out</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Opt-Out' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#help">Hilfe</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Help' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#total-clicks">Klicks gesamt</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Clicks' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "webhook" %}

#### Webhook-Metriken

Hier sind einige wichtige Webhook-Metriken, die Sie in Ihren Analysen sehen können. Die vollständigen Definitionen aller Webhook-Metriken, die in Braze verwendet werden, finden Sie in unserem [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrisch</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#unique-recipients">Eindeutige Empfänger:innen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Recipients' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Sendungen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#errors">Fehler</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Errors' %}</td>
        </tr>
    </tbody>
</table>

{% elsif include.channel == "whatsapp" %}

#### WhatsApp-Metriken

Hier sind einige wichtige WhatsApp-Metriken, die Sie in Ihren Analysen sehen können. Die vollständigen Definitionen aller WhatsApp-Metriken, die in Braze verwendet werden, finden Sie in unserem [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metrisch</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#sends">Sendungen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Sends' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#deliveries">Zustellungen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Deliveries' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#reads">Gelesen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Reads' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#failures">Misserfolge</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Failures' %}</td>
        </tr>
    </tbody>
</table>

#### Endbenutzer-Sperrung und Berichtsmetriken

Über das [Dashboard des WhatsApp Managers](https://www.facebook.com/business/help/683499390267496?content_id=NZUBj7XjkYjYuWx) können Sie auf weitere Metriken zugreifen. Allerdings ist [eine Bestätigung Ihres Zugriffs](https://www.facebook.com/business/help/218116047387456) erforderlich, um alle verfügbaren Einblicke zu erhalten. 

{% endif %}

### Historische Leistung

Im Bereich **Historische Leistung** können Sie die Metriken aus dem Bereich **Nachrichtenleistung** als Diagramm im Zeitverlauf betrachten. Verwenden Sie die Filter am oberen Rand des Fensters, um die im Diagramm angezeigten Statistiken und Kanäle zu ändern. Der Zeitbereich dieses Diagramms entspricht immer dem oben auf der Seite angegebenen Zeitbereich. 

Um eine Aufschlüsselung nach Tagen zu erhalten, klicken Sie auf das Hamburger-Menü <i class="fas fa-bars"></i> und wählen Sie **CSV herunterladen**, um einen CSV-Export des Berichts zu erhalten.

![Eine Grafik des Panels „Historische Leistung“ mit Beispielstatistiken für eine E-Mail von Februar 2021 bis Mai 2022.]({% image_buster /assets/img/cc-historical-performance.png %})

{% if include.channel == "in-app message" %}

{% alert note %}
Wenn Sie sich dafür entscheiden, nur an Benutzer zu senden, die die neueste Braze-Version der In-App-Nachrichten (Generation 3) sehen können, wird Ihre **Zielgruppe** nicht entsprechend angepasst.
{% endalert %}

{% endif %}

{% if include.channel == "SMS" %}

### Schlüsselwort-Antworten

Der Bereich **Schlüsselwortantworten** zeigt Ihnen eine Zeitleiste der eingehenden Schlüsselwörter, mit denen Nutzer nach Erhalt Ihrer Nachricht geantwortet haben.  

![Panel auf Kampagnenebene SMS/MMS/RCS Schlüsselwortantworten, das ein Liniendiagramm der Schlüsselwortverteilung im Zeitverlauf und einen Abschnitt Schlüsselwortkategorien mit ausgewählten Kontrollkästchen für Opt-in, Opt-out, Hilfe, Andere, Mehr und Coaching enthält.]({% image_buster /assets/img/sms/keyword_responses.png %})

Hier können Sie auch die Antwortverteilung für jede Keyword-Kategorie einsehen, um die nächsten Schritte für das [Retargeting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns) festzulegen und bequem [ein Segment zu erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment).

![Die Tabelle unterhalb des Liniendiagramms enthält Spalten für Schlüsselwortkategorie, Antwortverteilung und Retargeting, wobei Sie die Möglichkeit haben, ein Segment mit der Schlüsselwortkategorie zu erstellen.]({% image_buster /assets/img/sms/keyword_segments.png %})

{% endif %}

### Details zum Konversions-Event

Das Panel **Details zum Konversions-Event** zeigt Ihnen die Performance Ihrer Konversions-Events für Ihre Kampagne. Weitere Informationen finden Sie unter [Konvertierungsereignisse]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/#step-3-view-results).

![Das Panel „Details zum Konversions-Event“.]({% image_buster /assets/img/cc-conversion.png %})

### Konversionskorrelation

Das Panel **Konversionskorrelation** gibt Ihnen Aufschluss darüber, welche Benutzerattribute und Verhaltensweisen die von Ihnen für Kampagnen festgelegten Ergebnisse fördern oder beeinträchtigen. Weitere Informationen finden Sie unter [Umrechnungskorrelation]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation/).

![Das Panel „Konversionskorrelation“ mit einer Analyse der Benutzerattribute und des Benutzerverhaltens aus dem primären Konversions-Event - A.]({% image_buster /assets/img/convcorr.png %})

{% if include.channel == "whatsapp" %}

### Meta-Analysen

Zusätzlich zu den Braze-Analysen können Sie im WhatsApp Business Manager auf die Analysen auf Vorlagenebene zugreifen. Weitere Informationen finden Sie in [der Dokumentation von Meta](https://www.facebook.com/business/help/218116047387456). 

{% endif %}

{% if include.channel == "SMS" %}

### SMS-Currents-Events

Wie bei E-Mails empfängt Braze Ereignisse auf Benutzerebene im Zusammenhang mit einer SMS-Nachricht, während sie sich auf den Weg zu einem Benutzer macht. Alle eingehenden SMS-Ereignisse werden auch als Currents-Event über das Ereignis [SMS InboundReceived]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#sms-inbound-received-events) gesendet. So können Sie zusätzliche Aktionen oder Berichte zu den Nachrichten durchführen, die Ihre Benutzer außerhalb der Braze-Plattform einreichen. 

{% alert note %}
Eingehende Nachrichten werden nach 1.600 Zeichen abgeschnitten.
{% endalert %}

{% endif %}

{% if include.channel != "whatsapp" %}

## Bindungsbericht

Berichte zur Bindung zeigen Ihnen die Raten, mit denen Ihre Nutzer:innen ein ausgewähltes Bindungsereignis über Zeiträume in einer bestimmten Kampagne{% if include.channel != "banner" %} oder Canvas{% endif %} durchgeführt haben. Weitere Informationen finden Sie unter [Aufbewahrungsberichte]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/).

## Funnel-Bericht

Funnel-Berichte bieten einen visuellen Bericht, mit dem Sie die Wege Ihrer Kund:in nach dem Erhalt einer Kampagne{% if include.channel != "banner" %} oder Canvas{% endif %} analysieren können. Wenn Ihre Kampagne {% if include.channel != "banner" %}oder Canvas {% endif %}eine Kontrollgruppe oder mehrere Varianten verwendet, können Sie besser nachvollziehen, wie sich die verschiedenen Varianten auf den Konversionstrichter ausgewirkt haben, und auf der Grundlage dieser Daten optimieren.

Weitere Informationen finden Sie unter [Trichterberichte]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/).

{% endif %}

