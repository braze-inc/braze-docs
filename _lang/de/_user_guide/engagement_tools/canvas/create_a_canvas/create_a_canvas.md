---
nav_title: Erstellen einer Leinwand
article_title: Erstellen einer Leinwand
page_order: 0
page_type: reference
description: "Dieser Referenzartikel behandelt die notwendigen Schritte zur Erstellung, Pflege und Prüfung eines Canvas."
tool: Canvas
search_rank: 1
---

# Erstellen einer Leinwand

> Dieser Referenzartikel behandelt die notwendigen Schritte zur Erstellung, Pflege und Prüfung eines Canvas. Folgen Sie diesem Leitfaden oder schauen Sie sich unseren [Canvas Braze Learning-Kurs](https://learning.braze.com/quick-overview-canvas-setup) an.

{% details Original Canvas editor %}
Sie können Canvase nicht mehr mit dem ursprünglichen Canvas-Experiment erstellen oder duplizieren. Braze empfiehlt Ihnen, [Ihre Canvase]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) mit dem aktuellsten Editor zu [klonen]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% enddetails %}

## Erstellen einer Leinwand

### Schritt 1: Ein neues Canvas einrichten 

Gehen Sie zunächst auf **Messaging** > **Canvas** und wählen Sie dann **Canvas erstellen**.

Der Canvas-Builder führt Sie Schritt für Schritt durch die Einrichtung Ihres Canvas – von der Namensgebung bis zur Festlegung von Konversions-Events und der Einbindung der richtigen Nutzer:innen in Ihre Customer Journey. Wählen Sie eine der folgenden Registerkarten, um zu sehen, welche Einstellungen Sie für die einzelnen Erstellungsschritte vornehmen können.

{% tabs local %}
  {% tab Basics %}
    Hier werden Sie die Grundlagen Ihres Canvas einrichten:
    \- Canvas benennen
    \- Teams hinzufügen
    \- Tags hinzufügen
    \- Konversions-Events zuweisen und deren Event-Typen und Fristen wählen

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    Hier entscheiden Sie, wie und wann Ihre Nutzer:innen Ihr Canvas betreten:
    \- Geplant: Dies ist ein zeitbasierter Canvas-Eintrag
    \- Handlungsorientiert: Ihr:e Nutzer:in betritt Ihr Canvas, nachdem er oder sie eine bestimmte Aktion ausgeführt hat.
    \- API-getriggert: Verwenden Sie eine API-Anfrage, um Nutzer:innen in Ihr Canvas aufzunehmen.

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Target Audience %}
    Hier wählen Sie Ihr Zielpublikum aus:
    \- Erstellen Sie Ihre Zielgruppe durch Hinzufügen von Segmenten und Filtern
    \- Feinabstimmung der Limits zum erneuten Entry und zum Entry in Cavas
    \- Sehen Sie sich eine Zusammenfassung Ihrer Zielgruppe an

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    Hier wählen Sie Ihre Canvas-Sendeeinstellungen aus:
    \- Wählen Sie Ihre Abonnementeinstellungen
    \- Legen Sie ein Sendeleistungslimit für Ihre Canvas-Nachrichten fest
    \- Stille Stunden aktivieren und einstellen

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Build Canvas %}
    Hier bauen Sie Ihr Canvas.

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab Summary %}
    Hier finden Sie eine Übersicht über Ihre Canvas-Details. Wenn Sie den [Canvas-Genehmigungsworkflow]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) aktiviert haben, können Sie die aufgeführten Canvas-Details vor dem Start genehmigen.

  {% endtab %}
{% endtabs %}

#### Schritt 1.1: Beginnen Sie mit Ihren Canvas-Grundlagen

Hier benennen Sie Ihr Canvas, weisen [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) zu und erstellen oder fügen [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags) hinzu. Sie können auch Konvertierungsereignisse für den Canvas zuweisen.

{% alert tip %}
Markieren Sie Ihre Canvases, damit Sie sie leicht finden und Berichte daraus erstellen können. Wenn Sie zum Beispiel den [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.
{% endalert %}

![Die Canvas-Detailseite, mit Feldern für den Canvas-Namen, die Beschreibung, den Standort und die Tags.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### Wählen Sie Konversions-Events aus

Wählen Sie den Typ Ihres Konversions-Events und wählen Sie dann die Konversionen aus, die Sie aufzeichnen möchten. Diese [Konvertierungsereignisse]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) messen die Effizienz Ihres Canvas. 

![Primäres Konversions-Event A mit dem Konversions-Event-Typ Kauf tätigen, um Konversationen für Nutzer:innen aufzuzeichnen, die innerhalb einer dreitägigen Konversions-Frist einen Kauf tätigen.]({% image_buster /assets/img/add_canvas_conversions.png %})

Wenn Ihr Canvas mehrere Varianten oder eine Kontrollgruppe hat, verwendet Braze dieses Konversions-Event, um die beste Variante zum Erreichen dieses Konversionsziels zu ermitteln. Mit der gleichen Logik können Sie mehrere Konversions-Events erstellen.

#### Schritt 1.2: Bestimmen Sie Ihren Canvas-Entry-Zeitplan

Sie können eine von drei Möglichkeiten wählen, wie Nutzer:innen in Ihr Canvas gelangen können. 

##### Entry-Zeitplan-Typen

{% tabs local %}
  {% tab Scheduled Delivery %}
    Bei der zeitgesteuerten Zustellung geben die Nutzer:innen einen Zeitplan ein, ähnlich wie Sie eine Kampagne planen würden. Sie können Nutzer:innen in ein Canvas registrieren, sobald es gestartet wird, sie zu einem späteren Zeitpunkt in Ihre Journey einbeziehen oder sie auf einer wiederkehrenden Basis (täglich, wöchentlich oder monatlich) registrieren. 

    In this example, based on the time-based options, users will enter this Canvas every Tuesday at 12 pm in their local time zone every week, beginning November 14, 2025 until December 31, 2025.

    ![The "Entry Schedule" page with the type set to "Scheduled". Due to the selection, time-based options are shown, including frequency, start time, recurrence, days, and more.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    Bei der aktionsbasierten Zustellung rufen Nutzer:innen den Canvas auf und erhalten Nachrichten, wenn sie bestimmte Aktionen ausführen, z. B. Ihre App öffnen, einen Kauf tätigen oder ein angepasstes Event auslösen.

    You can control other aspects of the Canvas behavior from the **Entry Audience** window, including rules for re-eligibility and frequency capping settings. Note that action-based delivery is unavailable for Canvas components with in-app messages.

    ![An example of action-based delivery. Users will enter the Canvas if they make a purchase with an entry window beginning at 1:30 pm on June 10, 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API-Triggered Delivery %}
    Bei der API-getriggerten Zustellung rufen Nutzer:innen Ihr Canvas auf und erhalten Nachrichten, nachdem sie mit dem [Endpunkt`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) über die API hinzugefügt wurden. Im Dashboard finden Sie eine beispielhafte cURL-Anfrage, die dies ebenfalls ermöglicht, sowie die Zuweisung optionaler [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) mithilfe des [Canvas-Entry-Eigenschaftenobjekts]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). 

    ![An example of API-triggered delivery with a Canvas ID and an example of a cURL request.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    You can use the following endpoints for API-triggered delivery:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

Nachdem Sie Ihre Zustellungsmethode ausgewählt haben, passen Sie die Einstellungen an Ihren Anwendungsfall an und fahren dann mit der Festlegung Ihrer Zielgruppe fort.

{% details Deduplicate behavior for Canvases using the original editor %}
Sollte das Zeitfenster für die erneute Qualifizierung kürzer sein als die maximale Dauer des Canvas, ist es zulässig, dass ein:e Nutzer:in erneut zugreift und mehr als eine Nachricht einer Komponente empfängt. In dem seltenen Fall, dass die erneute Eingabe eines Benutzers dieselbe Komponente erreicht wie seine vorherige Eingabe, wird Braze die Nachrichten dieser Komponente deduplizieren. 

Wenn ein:e Nutzer:in den Canvas erneut aufruft, dieselbe Komponente wie bei seinem oder ihrem vorherigen Entry erreicht und Anspruch auf eine In-App-Nachricht für jeden Entry hat, erhält der oder die Nutzer:in die Nachricht zweimal (je nach Priorität der In-App-Nachrichten), solange er oder sie eine Sitzung zweimal öffnet.
{% enddetails %}

#### Schritt 1.3: Entry-Zielgruppe festlegen

Nur die Nutzer:innen, die Ihren definierten Kriterien entsprechen, können die Reise im Schritt **Target Audience** betreten. Das bedeutet, dass Braze die Zielgruppe zunächst auf ihre Eignung hin überprüft **, bevor** die Nutzer:innen die Canvas-Reise betreten. Wenn Sie zum Beispiel neue Nutzer ansprechen möchten, können Sie ein Segment von Nutzern auswählen, die Ihre App vor weniger als einer Woche zum ersten Mal verwendet haben.

In **Eingangskontrollen** können Sie die Anzahl der Nutzer:innen jedes Mal begrenzen, wenn der Zeitplan für den Canvas ausgeführt wird. Bei API trigger- und aktionsbasierten Canvase tritt dieses Limit zu jeder UTC-Stunde ein. 

{% alert important %}
Vermeiden Sie es, eine aktionsbasierte Kampagne oder ein Canvas mit demselben Auslöser wie den Zielgruppenfilter zu konfigurieren (z. B. ein geändertes Attribut oder die Durchführung eines benutzerdefinierten Ereignisses). Es kann eine [Race-Condition]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) auftreten, bei der der Nutzer:in zu dem Zeitpunkt, an dem er das Trigger-Ereignis ausführt, nicht in der Zielgruppe ist. Das bedeutet, dass er die Kampagne nicht erhält oder den Canvas nicht betreten kann.
{% endalert %}

##### Zielgruppe testen

Nachdem Sie Segmente und Filter zu Ihrer Zielgruppe hinzugefügt haben, können Sie testen, ob Ihre Zielgruppe wie erwartet eingerichtet ist, indem Sie [einen Nutzer oder eine Nutzerin suchen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) und überprüfen, ob er oder sie den Zielgruppen-Kriterien entspricht.

![Das Feld "User Lookup", in dem Sie nach externer Nutzer:innen ID oder Braze ID suchen können.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:100%;"}{: style="max-width:80%;"}

##### Entry-Kontrollen auswählen

Entry-Kontrollen bestimmen, ob Nutzer:innen ein Canvas erneut aufrufen dürfen. Sie können auch die Anzahl der Personen, die dieses Canvas betreten können, durch eine ausgewählte Kadenz begrenzen (täglich, Lifetime des Canvas oder jedes Mal, wenn das Canvas geplant ist). 

Wenn Sie beispielsweise **Eingangsvolumen begrenzen** auswählen und das Feld **Maximale Einträge** auf 5.000 Nutzer:innen mit **Täglich** als Grenzkadenz festlegen, sendet das Canvas nur an 5.000 Nutzer:innen pro Tag.

![Die Seite "Eingangskontrollen" zeigt Kontrollkästchen für "Nutzern:innen erlauben, Canvas erneut zu betreten" und "Eingangsvolumen begrenzen" an. Letzteres erlaubt es Ihnen, die maximalen Eingänge festzulegen und zu bestimmen, ob Sie täglich, die Lifetime des Canvas oder jedes Mal, wenn der Canvas auf dem Zeitplan steht, begrenzen möchten.]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze empfiehlt nicht, das Feature **Jedes Mal, wenn der Canvas auf dem Zeitplan steht** für IP-Warming zu verwenden, da dies zu einem erhöhten Sendevolumen führen kann.
{% endalert %}

##### Ausstiegskriterien festlegen

Die Einstellung der [Ausstiegskriterien]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) bestimmt, welche Benutzer ein Canvas verlassen sollen. Wenn ein:e Nutzer:in das Ausnahme-Event ausführt oder mit den Segmenten und Filtern übereinstimmt, erhält er oder sie keine weiteren Nachrichten.

##### Zielpopulation berechnen

Im Bereich **Zielgruppe** sehen Sie eine Zusammenfassung Ihrer Zielgruppe, z. B. Ihre ausgewählten Segmente und zusätzlichen Filter, sowie eine Aufschlüsselung der Anzahl der Nutzer, die über einen Messaging-Kanal erreichbar sind. Um die genaue Anzahl der erreichbaren Nutzer in Ihrer Zielgruppe zu berechnen, anstatt der Standardschätzung, wählen Sie [Exakte Statistik berechnen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics).

Beachten Sie Folgendes:

- Die Berechnung der genauen Statistiken kann einige Minuten in Anspruch nehmen. Diese Funktion berechnet die genauen Statistiken nur auf Segmentebene, nicht auf Filter- oder Filtergruppenebene.
- Bei großen Segmenten ist es normal, dass selbst bei der Berechnung exakter Statistiken leichte Abweichungen auftreten. Es wird erwartet, dass die Genauigkeit dieses Features 99,999 % oder mehr beträgt.

Wenn Sie zusätzliche Statistiken anzeigen möchten, z. B. den durchschnittlichen Lifetime-Umsatz für gezielte Nutzer, wählen Sie **Zusätzliche Statistiken anzeigen**.

![Aufschlüsselung der Zielpopulation mit Option zur Berechnung der genauen Statistik.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### Warum die Anzahl der Zielgruppen von der Anzahl der erreichbaren Nutzer:innen abweichen kann

{% multi_lang_include segments.md section='Differing audience size' %}

#### Schritt 1.4: Wählen Sie Ihre Sendeeinstellungen aus

Wählen Sie **Sendeeinstellungen**, um Ihre Abonnementeinstellungen zu bearbeiten, die Tarifbegrenzung zu aktivieren und die Ruhezeiten einzuschalten. Indem Sie [Rate-Limits]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) oder [Frequency-Capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping) einschalten, können Sie den Marketing-Druck auf Ihre Nutzer:innen verringern und sicherstellen, dass Sie sie nicht zu sehr mit Nachrichten überhäufen.

Für Canvase, die auf E-Mail- und Push-Kanäle abzielen, sollten Sie Ihr Canvas möglicherweise so einschränken, dass nur die Nutzer:innen, die sich ausdrücklich dafür angemeldet haben, die Nachricht erhalten (abonnierte oder abbestellte Nutzer:innen ausgenommen). Nehmen wir an, Sie haben drei Nutzer:innen mit unterschiedlichem Opt-in-Status:

- **Nutzer:in A** hat E-Mail abonniert und Push-Benachrichtigungen aktiviert. Diese Nutzer:innen erhalten die E-Mail nicht, aber den Push.
- **Benutzer B** hat sich für E-Mails entschieden, ist aber nicht für Push aktiviert. Dieser Benutzer erhält die E-Mail, aber nicht die Push-Mitteilung.
- **Nutzer:in** in hat Opt-in für E-Mail und ist für Push aktiviert. Dieser Benutzer erhält sowohl die E-Mail als auch die Push-Mitteilung.

Legen Sie dazu in den **Abonnementeinstellungen** fest, dass diese Canvas nur an "eingeloggte Benutzer" gesendet wird. Mit dieser Option stellen Sie sicher, dass nur Nutzer, die sich dafür entschieden haben, Ihre E-Mail erhalten, und Braze sendet Ihre Push-Nachrichten nur an Nutzer, die standardmäßig für Push aktiviert sind. 

Diese Abo-Einstellungen werden schrittweise angewendet, d. h. es gibt keine Auswirkungen auf die Entry-Zielgruppe. Diese Einstellung wird also verwendet, um die Berechtigung eines Benutzers zum Erhalt jedes Canvas-Schrittes zu bewerten.

{% alert important %}
Fügen Sie bei dieser Konfiguration keine Filter in den Schritt **Zielgruppen** ein, die die Zielgruppe auf einen einzigen Kanal beschränken (z.B. `Foreground Push Enabled = True` oder `Email Subscription = Opted-In`).
{% endalert %}

Legen Sie, falls gewünscht, die Ruhezeiten (die Zeit, in der Ihre Nachrichten nicht gesendet werden) für Ihr Canvas fest. Aktivieren Sie **Stille Stunden aktivieren** in Ihren **Sendeeinstellungen**. Wählen Sie dann Ihre Ruhezeiten in der Ortszeit Ihres Benutzers und die Aktion, die folgen soll, wenn die Nachricht innerhalb dieser Ruhezeiten ausgelöst wird.

![Die Seite "Ruhezeiten" zeigt ein Kontrollkästchen für das Enablement von Ruhezeiten an. Wenn diese Option aktiviert ist, können Sie die Startzeit, die Endzeit und das Fallback-Verhalten festlegen.]({% image_buster /assets/img/quiet_hours.png %})

### Schritt 2: Canvas erstellen

{% alert tip %}
Sparen Sie Zeit und rationalisieren Sie Ihre Canvas-Erstellung mit den [Braze Canvas-Vorlagen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates)! Durchsuchen Sie unsere Bibliothek mit vorgefertigten Vorlagen, um eine für Ihren Anwendungsfall passende Vorlage zu finden, und passen Sie sie an Ihre speziellen Bedürfnisse an.
{% endalert %}

#### Schritt 2.1: Eine Variante hinzufügen

![Der Button "Variante hinzufügen" ausgewählt, um ein Kontextmenü mit der Option "Variante hinzufügen" anzuzeigen.]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Wählen Sie **Variante hinzufügen** und fügen Sie dann eine neue Variante zu Ihrem Canvas hinzu. Varianten stellen eine Journey dar, die Ihre Nutzer:innen unternehmen werden, und können mehrere Schritte und Verzweigungen enthalten.

Sie können zusätzliche Varianten hinzufügen, indem Sie den <i class="fas fa-plus-circle"></i> Plus-Button auswählen. Wenn Sie neue Varianten hinzufügen, können Sie einstellen, wie sich Ihre Nutzer auf die einzelnen Varianten verteilen, so dass Sie die Wirksamkeit verschiedener Engagement-Strategien miteinander vergleichen und analysieren können.

![Zwei Beispielvarianten in einem Braze-Canvas.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Standardmäßig wird die Zuweisung der Canvas-Variante beim Betreten des Canvas festgelegt, d. h., wenn ein Benutzer zum ersten Mal eine Variante eingibt, ist dies seine Variante, wenn er den Canvas erneut betritt. Es gibt jedoch Möglichkeiten, dieses Verhalten zu umgehen. <br><br>Dazu können Sie mit Liquid einen Zufallszahlengenerator erstellen, ihn zu Beginn des Canvas-Eintrags eines jeden Benutzers ausführen, den Wert als benutzerdefiniertes Attribut speichern und dann dieses Attribut verwenden, um die Benutzer nach dem Zufallsprinzip aufzuteilen.

{% details Expand for steps %}

1. Erstellen Sie ein benutzerdefiniertes Attribut zum Speichern Ihrer Zufallszahl. Geben Sie dem Attribut einen leicht auffindbaren Namen, z.B. "lottery_number" oder "random_assignment".. Sie können das Attribut entweder [in Ihrem Dashboard]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) oder über API-Aufrufe an unseren [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) erstellen.<br><br>
2. Erstellen Sie zu Beginn Ihres Canvas eine Webhook-Kampagne. Diese Kampagne wird das Medium sein, in dem Sie Ihre Zufallszahl erstellen und als benutzerdefiniertes Attribut speichern. Weitere Informationen finden Sie unter [Erstellen eines Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook). Legen Sie die URL zu unserem Endpunkt `/users/track` fest.<br><br>
3. Erstellen Sie den Zufallszahlengenerator. Sie können dies mit dem [hier beschriebenen](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486) Code tun, der die eindeutige Eingabezeit jedes Nutzers:innen ausnutzt, um eine Zufallszahl zu erzeugen. Setzen Sie die resultierende Zahl als Liquid-Variable in Ihrer Webhook-Kampagne ein.<br><br>
4. Formatieren Sie den Aufruf `/users/track` Ihrer Webhook-Kampagne so, dass er das in Schritt 1 erstellte benutzerdefinierte Attribut auf die Zufallszahl setzt, die Sie im Profil Ihres aktuellen Benutzers generiert haben. Wenn dieser Schritt ausgeführt wird, haben Sie erfolgreich eine Zufallszahl erstellt, die sich jedes Mal ändert, wenn ein Benutzer Ihre Kampagne betritt.<br><br>
5. Passen Sie die Zweige Ihres Canvas so an, dass sie nicht mehr durch zufällig gewählte Varianten, sondern nach den Regeln der Zielgruppe unterteilt sind. Legen Sie in den Zielgruppen-Regeln der einzelnen Branches den Zielgruppen-Filter entsprechend Ihres angepassten Attributs fest. <br><br>Ein Branch kann zum Beispiel "lottery_number ist kleiner als 3" als Zielgruppen-Filter haben, während ein anderer Branch "lottery_number ist mehr als 3 und weniger als 6" als Zielgruppen-Filter hat.

{% enddetails %}
{% endalert %}

#### Schritt 2.2: Canvas-Schritte hinzufügen

Sie können Ihrem Canvas-Workflow weitere Schritte hinzufügen, indem Sie Komponenten aus der Seitenleiste **Komponenten** ziehen und ablegen. Oder wählen Sie die Schaltfläche <i class="fas fa-plus-circle"></i> plus, um eine Komponente mit dem Popover-Menü hinzuzufügen.

{% alert tip %}
Wenn Sie weitere Schritte hinzufügen, können Sie die Zoomstufe erhöhen, um sich auf Details zu konzentrieren oder die gesamte Nutzer-Journey zu betrachten. Vergrößern Sie mit <kbd>Umschalt</kbd> + <kbd>+</kbd> oder verkleinern Sie mit <kbd>Umschalt</kbd> + <kbd>-</kbd>.
{% endalert %}

![Das Komponentensuchfenster fügt dem Braze-Canvas einen Verzögerungsschritt hinzu.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Sie können bis zu 200 Schritte in einem Canvas hinzufügen. Wenn Ihr Canvas 200 Schritte überschreitet, kann es zu Ladeproblemen kommen.
{% endalert %}

##### Maximale Dauer

Da Ihre Canvas-Journey in Schritten voranschreitet, ist die maximale Dauer die längste Zeit, die ein:e Nutzer:in für die Fertigstellung dieses Canvas benötigen kann. Dies wird berechnet, indem die Verzögerungen und Auslösefenster jedes Schritts für jede Variante für den längsten Weg addiert werden. Wenn Ihr Canvas zum Beispiel einen Delay-Schritt mit einem Delay von 3 Tagen und einen Nachrichtenschritt hat, beträgt die maximale Dauer Ihres Canvas 3 Tage.

##### Einen Schritt bearbeiten

Möchten Sie einen Schritt in Ihrer Nutzer-Journey bearbeiten? Finden Sie heraus, wie Sie dies je nach Ihrem Canvas-Workflow tun können!

Sie können jeden Schritt in Ihrem Canvas-Workflow bearbeiten, indem Sie eine der Komponenten auswählen. Nehmen wir zum Beispiel an, Sie möchten Ihren ersten Schritt, eine [Delay-Komponente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), in Ihrem Workflow auf einen bestimmten Tag festlegen. Wählen Sie den Schritt aus, um seine Einstellungen anzuzeigen und passen Sie Ihr Delay an den 1\. März an. Das bedeutet, dass Ihre Nutzer:innen am 1\. März zum nächsten Schritt in Ihrem Canvas übergehen werden.

![Ein Beispiel für einen "Verzögerungsschritt", bei dem die Verzögerung auf "Bis zu einem bestimmten Tag" eingestellt ist.]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Oder Sie können die **Aktionseinstellungen** Ihres Schritts [Aktionspfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) schnell bearbeiten und anpassen, um Benutzer für ein bestimmtes Zeitfenster festzuhalten. Dadurch wird ihr nächster Weg auf der Grundlage der Aktionen während dieses Bewertungszeitraums priorisiert.

![Der zweite Schritt im Canvas, "Aktionseinstellungen", mit einem auf 1 Tag eingestellten Bewertungsfenster.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Die einfachen Komponenten in Canvas ermöglichen eine einfache Bearbeitung, sodass das Anpassen der Feinheiten Ihres Canvas einfacher wird. 

##### Nachrichten in Canvas

Bearbeiten Sie die Nachrichten in einer Canvas-Komponente, um die Nachrichten zu steuern, die ein bestimmter Schritt senden wird. Canvas kann E-Mail-, Mobile- und Web-Push-Nachrichten sowie Webhooks zur Integration mit anderen Systemen versenden. Ähnlich wie bei Kampagnen können Sie bestimmte [Liquid-Vorlagen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) verwenden, um Ihre Nachrichten zu personalisieren.

{% alert tip %}
Wussten Sie schon, dass Sie die Namen von Canvas-Komponenten in Ihre Nachrichten und Link-Templates aufnehmen können?<br>
Verwenden Sie das `campaign.${name}`-Liquid-Tag in Canvas, um den Namen der aktuellen Canvas-Komponente anzuzeigen.
{% endalert %}

Die Komponente Nachricht verwaltet die an Benutzer gesendeten Nachrichten. Sie können Ihre **Messaging-Kanäle** auswählen und die **Zustellungseinstellungen** anpassen, um Ihre Canvas-Nachrichten zu optimieren. Weitere Einzelheiten zu dieser Komponente finden Sie unter [Nachricht]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

![Der Schritt "Messaging-Kanäle einrichten", bei dem Sie "Messaging-Kanäle" auswählen, zeigt die Liste der verfügbaren Messaging-Kanäle an, wie Android Push, Content-Cards, E-Mail und mehr.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Wählen Sie **Fertig**, nachdem Sie die Konfiguration Ihrer Canvas-Komponente abgeschlossen haben.

{% tabs local %}
{% tab Canvas Entry Properties %}

Die `canvas_entry_properties` werden im Entry-Zeitplan bei der Erstellung eines Canvas konfiguriert und geben den Trigger an, mit dem ein:e Nutzer:in einen Canvas aufrufen kann. Diese Eigenschaften können auch auf die Eigenschaften von Eingabe-Nutzdaten in API-ausgelösten Canvases zugreifen. Beachten Sie, dass das Objekt `canvas_entry_properties` bis zu 50 KB groß sein kann. 

Verwenden Sie das folgende Liquid, wenn Sie auf diese Entry-Eigenschaften verweisen: {% raw %} ``canvas_entry_properties.${property_name}`` {% endraw %}. Beachten Sie, dass es sich bei den Events um angepasste Events oder Kauf-Events handeln muss, um auf diese Weise verwendet werden zu können.

{% raw %}
Betrachten Sie zum Beispiel die folgende Anfrage: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Mit diesem ``{{canvas_entry_properties.${product_name}}}``-Liquid können Sie das Wort „Schuhe“ in eine Nachricht einfügen.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
Event-Eigenschaften sind die Eigenschaften, die Sie für angepasste Events und Käufe festlegen. Diese `event_properties` können sowohl in Kampagnen mit aktionsbasierter Zustellung als auch in Canvase verwendet werden. 

In Canvas können angepasste Event- und Kauf-Event-Eigenschaften in Liquid in jedem Nachrichten-Schritt verwendet werden, der auf einen Aktions-Pfad-Schritt folgt. Verwenden Sie dieses {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %}-Liquid, wenn Sie auf diese `event_properties` verweisen. Diese Events müssen angepasste Events oder Kauf-Events sein, um auf diese Weise in der Komponente „Nachricht“ verwendet werden zu können.

Im ersten Nachrichten-Schritt, der einem Aktionspfad folgt, können Sie `event_properties` verwenden, das sich auf das Event bezieht, das in diesem Aktionspfad referenziert wird. Zwischen dem Schritt „Aktionspfade“ und dem Schritt „Nachricht“ können weitere Schritte liegen (die keine anderen Aktionspfade oder Nachrichten sind). Beachten Sie, dass Sie nur dann auf `event_properties` zugreifen können, wenn Ihr Schritt „Nachricht“ auf einen Nicht-Alle-anderen-Pfad in einem Aktionspfad-Schritt zurückverfolgt werden kann.

{% endtab %}
{% endtabs %}

#### Schritt 2.3: Verbindungen bearbeiten

Um eine Verbindung zwischen Schritten zu verschieben, wählen Sie den Pfeil, der die beiden Komponenten verbindet, und dann eine andere Komponente aus. Um die Verbindung zu entfernen, wählen Sie den Pfeil gefolgt von **Verbindung abbrechen** in der Fußzeile des Canvas Composers aus.

### Schritt 3: Eine Kontrollgruppe hinzufügen

Sie können eine Kontrollgruppe zu Ihrem Canvas hinzufügen, indem Sie auf die Schaltfläche <i class="fas fa-plus-circle"></i> plus klicken, um eine neue Variante hinzuzufügen. 

Braze verfolgt die Konversionen der Nutzer, die der Kontrollgruppe angehören, obwohl diese keine Nachrichten erhalten. Um einen genauen Test zu gewährleisten, verfolgen wir die Anzahl der Konversionen für Ihre Varianten und die Kontrollgruppe für genau denselben Zeitraum, wie auf dem Bildschirm zur Auswahl des Konversions-Events angezeigt wird. 

Sie können die Verteilung zwischen Ihren Nachrichten anpassen, indem Sie auf die Überschriften der **Variantennamen** doppelklicken.

In diesem Beispiel haben wir unser Canvas in zwei Varianten unterteilt. Variante 1 hat 70 % der Nutzer:innen. Bei der zweiten Variante handelt es sich um eine Kontrollgruppe mit den restlichen 30 % der Nutzer:innen.

![Eine Beispielvariante in einem Braze-Canvas, bei der 70 % auf "Variante 1" gehen, die im ersten Schritt 1 Tag lang verzögert und dann im zweiten Schritt eine Nachricht sendet. Die anderen 30% gehen an eine "Kontrolle", die keine weiteren Schritte vorsieht.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### Intelligente Auswahl für Canvas

In multivariaten Canvase sind jetzt intelligente Auswahlmöglichkeiten verfügbar. Ähnlich wie das Feature [Intelligente Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) für multivariate Kampagnen analysiert die Intelligente Auswahl für Canvas die Performance der einzelnen Canvas-Varianten und passt den Prozentsatz der Nutzer:innen an, die durch die einzelnen Varianten geleitet werden. Diese Verteilung basiert auf den Performance-Metriken der einzelnen Varianten, um die erwartete Gesamtzahl der Konversionen zu maximieren.

Denken Sie daran, dass Sie mit multivariaten Canvase nicht nur Texte, sondern auch Timing und Kanäle testen können. Mit der intelligenten Auswahl können Sie Canvase effizienter testen und darauf vertrauen, dass Ihre Nutzer:innen auf die bestmögliche Canvas-Journey geschickt werden.

![Die Option "Intelligente Auswahl" ist auf der Seite "Variantenverteilung bearbeiten" Enablement aktiviert. Bei der Analyse und Optimierung des Canvas wird ein horizontaler Balken quer über die Seite angezeigt, der in mehrere Abschnitte unterteilt ist, die jeweils in Farbe und Größe variieren. Dies ist nur eine visuelle Darstellung und steht in keinem Zusammenhang mit bestimmten Analytics.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

Intelligent Selection for Canvas optimiert Ihre Canvas-Ergebnisse, indem es schrittweise Echtzeit-Anpassungen an der Verteilung der in jede Variante sortierten Benutzer vornimmt. Wenn der statistische Algorithmus einen entscheidenden Gewinner unter Ihren Varianten ermittelt, schließt er die leistungsschwächeren Varianten aus und ordnet alle zukünftigen in Frage kommenden Empfänger:innen des Canvas den Gewinnervarianten zu. 

Aus diesem Grund funktioniert die intelligente Auswahl am besten auf Canvase, bei denen häufig neue Nutzer:innen hinzukommen.

### Schritt 4: Speichern und starten

Nachdem Sie Ihr Canvas erstellt haben, wählen Sie **Canvas starten**, um Ihr Canvas zu speichern und zu starten. Nachdem Sie Ihr Canvas gestartet haben, können Sie auf der Seite **Canvas-Details** die Analysen für Ihre Reise einsehen, sobald diese eintreffen. 

Sie können Ihr Canvas auch als Entwurf speichern, wenn Sie darauf zurückkommen möchten.

![Ein Beispiel-Canvas in Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
Müssen Sie nach dem Start Änderungen an Ihrem Canvas vornehmen? Nun, Sie können! Weitere Informationen finden Sie unter [Bearbeiten von Leinwänden nach dem Start]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

