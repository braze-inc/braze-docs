---
nav_title: Ein Canvas erstellen
article_title: Ein Canvas erstellen
page_order: 0
page_type: reference
description: "Dieser Referenzartikel behandelt die notwendigen Schritte zur Erstellung, Pflege und Prüfung eines Canvas."
tool: Canvas
search_rank: 1
---

# Ein Canvas erstellen

> Dieser Referenzartikel behandelt die notwendigen Schritte zur Erstellung, Pflege und Prüfung eines Canvas. Folgen Sie diesem Leitfaden oder schauen Sie sich unseren [Braze-Lernkurs zu Canvas](https://learning.braze.com/quick-overview-canvas-setup) an.

{% details Details zum ursprünglichen Canvas-Editor anzeigen %}
Sie können Canvase nicht mehr mit dem ursprünglichen Canvas-Editor erstellen oder duplizieren. Braze empfiehlt, [Ihre Canvase]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) mit dem aktuellsten Editor zu klonen.
{% enddetails %}

## Ein Canvas erstellen

### Schritt 1: Ein neues Canvas einrichten 

Gehen Sie zunächst auf **Messaging** > **Canvas** und wählen Sie dann **Canvas erstellen**.

Der Canvas-Builder führt Sie Schritt für Schritt durch die Einrichtung Ihres Canvas – von der Namensgebung bis zur Festlegung von Konversions-Events und der Einbindung der richtigen Nutzer:innen in Ihre Customer Journey. Wählen Sie einen der folgenden Tabs, um zu sehen, welche Einstellungen Sie für die einzelnen Builder-Schritte vornehmen können.

{% tabs local %}
  {% tab Basics %}
    Hier richten Sie die Grundlagen Ihres Canvas ein:
    - Canvas benennen
    - Teams hinzufügen
    - Tags hinzufügen
    - Konversions-Events zuweisen und deren Event-Typen und Fristen wählen

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    Hier entscheiden Sie, wie und wann Ihre Nutzer:innen Ihr Canvas betreten:
    - Geplant: Dies ist ein zeitbasierter Canvas-Eingang
    - Aktionsbasiert: Ihre Nutzer:innen betreten Ihr Canvas, nachdem sie eine definierte Aktion ausgeführt haben
    - API-getriggert: Verwenden Sie eine API-Anfrage, um Nutzer:innen in Ihr Canvas aufzunehmen

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Target Audience %}
    Hier wählen Sie Ihre Zielgruppe aus:
    - Erstellen Sie Ihre Zielgruppe durch Hinzufügen von Segmenten und Filtern
    - Feinabstimmung der Canvas-Wiedereintritts- und Eingangslimits
    - Sehen Sie eine Zusammenfassung Ihrer Zielgruppe

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    Hier wählen Sie Ihre Canvas-Sendeeinstellungen:
    - Wählen Sie Ihre Abo-Einstellungen
    - Legen Sie ein Rate-Limit für Ihre Canvas-Nachrichten fest
    - Ruhezeiten aktivieren und einstellen

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Build Canvas %}
    Hier erstellen Sie Ihr Canvas.

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab Summary %}
    Hier finden Sie die Zusammenfassung Ihrer Canvas-Details. Wenn Sie den [Canvas-Genehmigungsworkflow]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) aktiviert haben, können Sie die aufgeführten Canvas-Details vor dem Start genehmigen.

  {% endtab %}
{% endtabs %}

#### Schritt 1.1: Beginnen Sie mit Ihren Canvas-Grundlagen

Hier benennen Sie Ihr Canvas, weisen [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams) zu und erstellen oder fügen [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags) hinzu. Sie können auch Konversions-Events für das Canvas zuweisen.

{% alert tip %}
Versehen Sie Ihre Canvase mit Tags, damit Sie sie leicht finden und Berichte daraus erstellen können. Wenn Sie zum Beispiel den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.
{% endalert %}

![Die Canvas-Detailseite mit Feldern für den Canvas-Namen, die Beschreibung, den Standort und die Tags.]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### Konversions-Events auswählen

Wählen Sie den Typ Ihres Konversions-Events und dann die Konversionen aus, die aufgezeichnet werden sollen. Diese [Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) messen die Effizienz Ihres Canvas. 

![Primäres Konversions-Event A mit dem Konversions-Event-Typ „Kauf tätigen", um Konversionen für Nutzer:innen aufzuzeichnen, die innerhalb einer dreitägigen Konversionsfrist einen Kauf tätigen.]({% image_buster /assets/img/add_canvas_conversions.png %})

Wenn Ihr Canvas mehrere Varianten oder eine Kontrollgruppe hat, verwendet Braze dieses Konversions-Event, um die beste Variante zum Erreichen dieses Konversionsziels zu ermitteln. Mit der gleichen Logik können Sie mehrere Konversions-Events erstellen.

#### Schritt 1.2: Bestimmen Sie Ihren Canvas-Eingangszeitplan

Sie können eine von drei Möglichkeiten wählen, wie Nutzer:innen in Ihr Canvas gelangen können. 

##### Eingangszeitplan-Typen

{% tabs local %}
  {% tab Scheduled Delivery %}
    Bei der zeitgesteuerten Zustellung treten Nutzer:innen nach einem Zeitplan ein, ähnlich wie Sie eine Kampagne planen würden. Sie können Nutzer:innen in ein Canvas aufnehmen, sobald es gestartet wird, sie zu einem späteren Zeitpunkt in Ihre Journey einbeziehen oder auf wiederkehrender Basis (täglich, wöchentlich oder monatlich) aufnehmen. 

    In diesem Beispiel treten Nutzer:innen basierend auf den zeitbasierten Optionen jeden Dienstag um 12 Uhr in ihrer Ortszeit jede Woche in dieses Canvas ein, beginnend am 14. November 2025 bis zum 31. Dezember 2025.

    ![Die Seite „Eingangszeitplan" mit dem Typ „Geplant". Aufgrund der Auswahl werden zeitbasierte Optionen angezeigt, einschließlich Häufigkeit, Startzeit, Wiederholung, Tage und mehr.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    Bei der aktionsbasierten Zustellung treten Nutzer:innen in das Canvas ein und erhalten Nachrichten, wenn sie bestimmte Aktionen ausführen, z. B. Ihre App öffnen, einen Kauf tätigen oder ein angepasstes Event auslösen.

    Sie können weitere Aspekte des Canvas-Verhaltens über das Fenster **Eingangs-Zielgruppe** steuern, einschließlich Regeln für die erneute Qualifizierung und Frequency-Capping-Einstellungen. Beachten Sie, dass die aktionsbasierte Zustellung für Canvas-Komponenten mit In-App-Nachrichten nicht verfügbar ist.

    ![Ein Beispiel für aktionsbasierte Zustellung. Nutzer:innen treten in das Canvas ein, wenn sie einen Kauf tätigen, mit einem Eingangsfenster ab 13:30 Uhr am 10. Juni 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API-Triggered Delivery %}
    Bei der API-getriggerten Zustellung treten Nutzer:innen in Ihr Canvas ein und erhalten Nachrichten, nachdem sie über den [`/canvas/trigger/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) per API hinzugefügt wurden. Im Dashboard finden Sie eine beispielhafte cURL-Anfrage sowie die Möglichkeit, optionale [`context`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)-Daten mithilfe des [Context-Objekts]({{site.baseurl}}/api/objects_filters/context_object/) zuzuweisen. 

    ![Ein Beispiel für API-getriggerte Zustellung mit einer Canvas-ID und einem Beispiel einer cURL-Anfrage.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    Sie können die folgenden Endpunkte für die API-getriggerte Zustellung verwenden:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

Nachdem Sie Ihre Zustellungsmethode ausgewählt haben, passen Sie die Einstellungen an Ihren Anwendungsfall an und fahren dann mit der Festlegung Ihrer Zielgruppe fort.

{% details Deduplizierungsverhalten für Canvase mit dem ursprünglichen Editor %}
Sollte das Zeitfenster für die erneute Qualifizierung kürzer sein als die maximale Dauer des Canvas, ist es möglich, dass Nutzer:innen erneut eintreten und Nachrichten von mehr als einer Komponente erhalten. In dem seltenen Fall, dass der erneute Eintritt dieselbe Komponente wie der vorherige Eintritt erreicht, wird Braze die Nachrichten dieser Komponente deduplizieren. 

Wenn Nutzer:innen das Canvas erneut betreten, dieselbe Komponente wie bei ihrem vorherigen Eintritt erreichen und für eine In-App-Nachricht bei jedem Eintritt berechtigt sind, erhalten sie die Nachricht zweimal (abhängig von der Priorität der In-App-Nachrichten), solange sie eine Sitzung zweimal öffnen.
{% enddetails %}

#### Schritt 1.3: Eingangs-Zielgruppe festlegen

Nur Nutzer:innen, die Ihren definierten Kriterien entsprechen, können die Journey im Schritt **Zielgruppe** betreten. Das bedeutet, dass Braze die Zielgruppe zunächst auf ihre Eignung hin überprüft, **bevor** die Nutzer:innen die Canvas-Journey betreten. Wenn Sie zum Beispiel neue Nutzer:innen ansprechen möchten, können Sie ein Segment von Nutzer:innen auswählen, die Ihre App vor weniger als einer Woche zum ersten Mal verwendet haben.

Unter **Eingangskontrollen** können Sie die Anzahl der Nutzer:innen begrenzen, die jedes Mal eintreten, wenn der Canvas-Zeitplan ausgeführt wird. Bei API-getriggerten und aktionsbasierten Canvasen tritt dieses Limit zu jeder UTC-Stunde ein. 

{% include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

##### Zielgruppe testen

Nachdem Sie Segmente und Filter zu Ihrer Zielgruppe hinzugefügt haben, können Sie testen, ob Ihre Zielgruppe wie erwartet eingerichtet ist, indem Sie [eine:n Nutzer:in suchen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) und überprüfen, ob diese:r den Zielgruppen-Kriterien entspricht.

![Das Feld „User Lookup", das Ihnen die Suche nach externer Nutzer:innen-ID oder Braze-ID ermöglicht.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

##### Eingangskontrollen auswählen

Eingangskontrollen bestimmen, ob Nutzer:innen ein Canvas erneut betreten dürfen. Sie können auch die Anzahl der Personen begrenzen, die dieses Canvas potenziell betreten, mit einer ausgewählten Kadenz abhängig von Ihrem Eingangszeitplan-Typ:

- **Geplant:** Lifetime des Canvas oder jedes Mal, wenn der Canvas-Zeitplan ausgeführt wird
- **Aktionsbasiert:** Stündlich, täglich oder Lifetime des Canvas
- **API-getriggert:** Stündlich, täglich oder Lifetime des Canvas

Wenn Sie beispielsweise ein aktionsbasiertes Canvas haben und **Eingangsvolumen begrenzen** auswählen und das Feld **Maximale Einträge** auf 5.000 Nutzer:innen mit **Täglich** als Grenzkadenz festlegen, sendet das Canvas nur an 5.000 Nutzer:innen pro Tag.

![Die Seite „Eingangskontrollen" mit Kontrollkästchen für „Nutzer:innen den erneuten Eintritt in Canvas erlauben" und „Eingangsvolumen begrenzen". Letzteres ermöglicht es Ihnen, die maximalen Einträge festzulegen und eine Kadenz zu wählen, die vom Eingangszeitplan-Typ abhängt (z. B. Lifetime des Canvas oder jedes Mal, wenn der Canvas-Zeitplan ausgeführt wird bei geplanten Eingängen, und stündlich, täglich oder Lifetime des Canvas bei aktionsbasierten und API-getriggerten Eingängen).]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze empfiehlt nicht, **Jedes Mal, wenn der Canvas-Zeitplan ausgeführt wird** für IP-Warming auszuwählen, da dies zu einem erhöhten Sendevolumen führen kann.
{% endalert %}

##### Ausstiegskriterien festlegen

Das Festlegen der [Ausstiegskriterien]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) bestimmt, welche Nutzer:innen ein Canvas verlassen sollen. Wenn Nutzer:innen das Ausnahme-Event ausführen oder mit den Segmenten und Filtern übereinstimmen, erhalten sie keine weiteren Nachrichten.

##### Zielpopulation berechnen

Im Bereich **Zielpopulation** sehen Sie eine Zusammenfassung Ihrer Zielgruppe, z. B. Ihre ausgewählten Segmente und zusätzlichen Filter, sowie eine Aufschlüsselung, wie viele Nutzer:innen pro Messaging-Kanal erreichbar sind. Um die genaue Anzahl der erreichbaren Nutzer:innen in Ihrer Zielgruppe anstelle der Standardschätzung zu berechnen, wählen Sie [Exakte Statistik berechnen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics).

Beachten Sie Folgendes:

- Die Berechnung der genauen Statistik kann einige Minuten dauern. Diese Funktion berechnet die genauen Statistiken nur auf Segmentebene, nicht auf Filter- oder Filtergruppenebene.
- Bei großen Segmenten ist es normal, dass selbst bei der Berechnung exakter Statistiken leichte Abweichungen auftreten. Die Genauigkeit dieses Features beträgt erwartungsgemäß 99,999 % oder mehr.

Um zusätzliche Statistiken anzuzeigen, z. B. den durchschnittlichen Lifetime-Umsatz für angesprochene Nutzer:innen, wählen Sie **Zusätzliche Statistiken anzeigen**.

![Aufschlüsselung der Zielpopulation mit Option zur Berechnung der genauen Statistik.]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### Warum die Zielgruppen-Anzahl von der Anzahl der erreichbaren Nutzer:innen abweichen kann

{% multi_lang_include segments.md section='Differing audience size' %}

#### Schritt 1.4: Sendeeinstellungen auswählen

Wählen Sie **Sendeeinstellungen**, um Ihre Abo-Einstellungen zu bearbeiten, Rate-Limiting zu aktivieren und Ruhezeiten einzuschalten. Indem Sie [Rate-Limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components) oder [Frequency-Capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping) einschalten, können Sie den Marketing-Druck auf Ihre Nutzer:innen verringern und sicherstellen, dass Sie sie nicht mit zu vielen Nachrichten überhäufen.

Für Canvase, die auf E-Mail- und Push-Kanäle abzielen, möchten Sie Ihr Canvas möglicherweise so einschränken, dass nur Nutzer:innen, die sich ausdrücklich angemeldet haben, die Nachricht erhalten (abonnierte oder abgemeldete Nutzer:innen ausgenommen). Nehmen wir an, Sie haben drei Nutzer:innen mit unterschiedlichem Opt-in-Status:

- **Nutzer:in A** hat E-Mail abonniert und Push ist aktiviert. Diese:r Nutzer:in erhält die E-Mail nicht, aber den Push.
- **Nutzer:in B** hat Opt-in für E-Mail, aber Push ist nicht aktiviert. Diese:r Nutzer:in erhält die E-Mail, aber nicht den Push.
- **Nutzer:in C** hat Opt-in für E-Mail und Push ist aktiviert. Diese:r Nutzer:in erhält sowohl die E-Mail als auch den Push.

Legen Sie dazu in den **Abo-Einstellungen** fest, dass dieses Canvas nur an „Nutzer:innen mit Opt-in" gesendet wird. Diese Option stellt sicher, dass nur Nutzer:innen mit Opt-in Ihre E-Mail erhalten, und Braze sendet Ihren Push standardmäßig nur an Nutzer:innen, die für Push aktiviert sind. 

Diese Abo-Einstellungen werden pro Schritt angewendet, d. h. es gibt keine Auswirkungen auf die Eingangs-Zielgruppe. Diese Einstellung wird verwendet, um die Berechtigung von Nutzer:innen zum Erhalt jedes Canvas-Schritts zu bewerten.

{% alert important %}
Fügen Sie bei dieser Konfiguration keine Filter in den Schritt **Zielgruppe** ein, die die Zielgruppe auf einen einzigen Kanal beschränken (z. B. `Foreground Push Enabled = True` oder `Email Subscription = Opted-In`).
{% endalert %}

Legen Sie bei Bedarf Ruhezeiten (die Zeit, in der Ihre Nachrichten nicht gesendet werden) für Ihr Canvas fest. Aktivieren Sie **Ruhezeiten aktivieren** in Ihren **Sendeeinstellungen**. Wählen Sie dann Ihre Ruhezeiten in der Ortszeit Ihrer Nutzer:innen und die Aktion, die folgen soll, wenn die Nachricht innerhalb dieser Ruhezeiten ausgelöst wird.

![Die Seite „Ruhezeiten" mit einem Kontrollkästchen zur Aktivierung der Ruhezeiten. Wenn aktiviert, können Startzeit, Endzeit und Fallback-Verhalten festgelegt werden.]({% image_buster /assets/img/quiet_hours.png %})

### Schritt 2: Ihr Canvas erstellen

{% alert tip %}
Sparen Sie Zeit und optimieren Sie Ihre Canvas-Erstellung mit [Braze Canvas-Templates]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates)! Durchsuchen Sie unsere Bibliothek mit vorgefertigten Templates, um eines für Ihren Anwendungsfall zu finden, und passen Sie es an Ihre speziellen Bedürfnisse an.
{% endalert %}

#### Schritt 2.1: Eine Variante hinzufügen

![Der Button „Variante hinzufügen" wurde ausgewählt, um ein Kontextmenü mit der Option „Variante hinzufügen" anzuzeigen.]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

Wählen Sie **Variante hinzufügen** und fügen Sie dann eine neue Variante zu Ihrem Canvas hinzu. Varianten stellen eine Journey dar, die Ihre Nutzer:innen durchlaufen, und können mehrere Schritte und Verzweigungen enthalten.

Sie können zusätzliche Varianten hinzufügen, indem Sie den <i class="fas fa-plus-circle"></i> Plus-Button auswählen. Wenn Sie neue Varianten hinzufügen, können Sie einstellen, wie Ihre Nutzer:innen auf die einzelnen Varianten verteilt werden, sodass Sie die Wirksamkeit verschiedener Engagement-Strategien vergleichen und analysieren können.

![Zwei Beispiel-Varianten in einem Braze-Canvas.]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
Standardmäßig wird die Canvas-Variantenzuweisung beim Betreten des Canvas festgelegt. Wenn Nutzer:innen also zum ersten Mal eine Variante betreten, ist dies ihre Variante bei jedem erneuten Eintritt in das Canvas. Es gibt jedoch Möglichkeiten, dieses Verhalten zu umgehen. <br><br>Dazu können Sie mit Liquid einen Zufallszahlengenerator erstellen, ihn zu Beginn jedes Canvas-Eintritts ausführen, den Wert als angepasstes Attribut speichern und dann dieses Attribut verwenden, um die Nutzer:innen zufällig aufzuteilen.

{% details Schritte anzeigen %}

1. Erstellen Sie ein angepasstes Attribut zum Speichern Ihrer Zufallszahl. Geben Sie ihm einen leicht auffindbaren Namen, z. B. „lottery_number" oder „random_assignment". Sie können das Attribut entweder [in Ihrem Dashboard]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) oder über API-Aufrufe an unseren [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) erstellen.<br><br>
2. Erstellen Sie zu Beginn Ihres Canvas eine Webhook-Kampagne. Diese Kampagne dient als Medium, in dem Sie Ihre Zufallszahl erstellen und als angepasstes Attribut speichern. Weitere Informationen finden Sie unter [Einen Webhook erstellen]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook). Setzen Sie die URL auf unseren `/users/track`-Endpunkt.<br><br>
3. Erstellen Sie den Zufallszahlengenerator. Sie können dies mit dem [hier beschriebenen](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486) Code tun, der die eindeutige Eintrittszeit jeder Nutzer:in nutzt, um eine Zufallszahl zu erzeugen. Setzen Sie die resultierende Zahl als Liquid-Variable in Ihrer Webhook-Kampagne.<br><br>
4. Formatieren Sie den `/users/track`-Aufruf Ihrer Webhook-Kampagne so, dass er das in Schritt 1 erstellte angepasste Attribut auf die Zufallszahl setzt, die Sie im Profil der aktuellen Nutzer:in generiert haben. Wenn dieser Schritt ausgeführt wird, haben Sie erfolgreich eine Zufallszahl erstellt, die sich bei jedem Eintritt in Ihre Kampagne ändert.<br><br>
5. Passen Sie die Zweige Ihres Canvas so an, dass sie nicht nach zufällig gewählten Varianten, sondern nach Zielgruppen-Regeln unterteilt werden. Legen Sie in den Zielgruppen-Regeln der einzelnen Zweige den Zielgruppen-Filter entsprechend Ihres angepassten Attributs fest. <br><br>Ein Zweig kann zum Beispiel „lottery_number ist kleiner als 3" als Zielgruppen-Filter haben, während ein anderer Zweig „lottery_number ist größer als 3 und kleiner als 6" als Zielgruppen-Filter hat.

{% enddetails %}
{% endalert %}

#### Schritt 2.2: Canvas-Schritte hinzufügen

Sie können Ihrem Canvas-Workflow weitere Schritte hinzufügen, indem Sie Komponenten aus der Seitenleiste **Komponenten** per Drag-and-Drop ziehen. Oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button, um eine Komponente über das Popover-Menü hinzuzufügen.

{% alert tip %}
Wenn Sie weitere Schritte hinzufügen, können Sie die Zoomstufe anpassen, um sich auf Details zu konzentrieren oder die gesamte Nutzer-Journey zu überblicken. Vergrößern Sie mit <kbd>Umschalt</kbd> + <kbd>+</kbd> oder verkleinern Sie mit <kbd>Umschalt</kbd> + <kbd>-</kbd>.
{% endalert %}

![Das Fenster für die Komponentensuche fügt dem Braze-Canvas einen Verzögerungsschritt hinzu.]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
Sie können bis zu 200 Schritte in einem Canvas hinzufügen. Wenn Ihr Canvas 200 Schritte überschreitet, kann es zu Ladeproblemen kommen.
{% endalert %}

##### Maximale Dauer

Da Ihre Canvas-Journey in Schritten voranschreitet, ist die maximale Dauer die längste mögliche Zeit, die Nutzer:innen für die Fertigstellung dieses Canvas benötigen können. Sie wird berechnet, indem die Verzögerungen und Trigger-Fenster jedes Schritts für jede Variante auf dem längsten Pfad addiert werden. Wenn Ihr Canvas zum Beispiel einen Verzögerungsschritt mit einer Verzögerung von 3 Tagen und einen Nachrichtenschritt hat, beträgt die maximale Dauer Ihres Canvas 3 Tage.

##### Einen Schritt bearbeiten

Möchten Sie einen Schritt in Ihrer Nutzer-Journey bearbeiten? Erfahren Sie, wie Sie dies je nach Ihrem Canvas-Workflow tun können!

Sie können jeden Schritt in Ihrem Canvas-Workflow bearbeiten, indem Sie eine der Komponenten auswählen. Nehmen wir zum Beispiel an, Sie möchten Ihren ersten Schritt, eine [Verzögerungskomponente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), in Ihrem Workflow auf einen bestimmten Tag festlegen. Wählen Sie den Schritt aus, um seine Einstellungen anzuzeigen, und passen Sie die Verzögerung auf den 1. März an. Das bedeutet, dass Ihre Nutzer:innen am 1. März zum nächsten Schritt in Ihrem Canvas übergehen.

![Ein Beispiel für einen „Verzögerungs"-Schritt, bei dem die Verzögerung auf „Bis zu einem bestimmten Tag" eingestellt ist.]({% image_buster /assets/img_archive/edit_delay_flow.png %})

Oder Sie können die **Aktionseinstellungen** Ihres [Aktions-Pfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)-Schritts schnell bearbeiten und anpassen, um Nutzer:innen für ein bestimmtes Zeitfenster zu halten. Dadurch wird ihr nächster Pfad basierend auf den Aktionen während dieses Bewertungszeitraums priorisiert.

![Der zweite Schritt im Canvas, „Aktionseinstellungen", mit einem auf 1 Tag eingestellten Bewertungsfenster.]({% image_buster /assets/img_archive/action_paths_flow.png %})

Die schlanken Komponenten in Canvas ermöglichen eine einfache Bearbeitung, sodass das Anpassen der Feinheiten Ihres Canvas leichter wird. 

##### Nachrichten in Canvas

Bearbeiten Sie die Nachrichten in einer Canvas-Komponente, um die Nachrichten zu steuern, die ein bestimmter Schritt senden wird. Canvas kann E-Mail-, Mobile- und Web-Push-Nachrichten sowie Webhooks zur Integration mit anderen Systemen versenden. Ähnlich wie bei Kampagnen können Sie bestimmte [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/)-Templates verwenden, um Ihre Nachrichten zu personalisieren.

{% alert tip %}
Wussten Sie, dass Sie Canvas-Komponentennamen in Ihre Nachrichten und Link-Templates aufnehmen können?<br>
Verwenden Sie den `campaign.${name}`-Liquid-Tag in Canvas, um den Namen der aktuellen Canvas-Komponente anzuzeigen.
{% endalert %}

Die Nachrichtenkomponente verwaltet die an Nutzer:innen gesendeten Nachrichten. Sie können Ihre **Messaging-Kanäle** auswählen und die **Zustellungseinstellungen** anpassen, um Ihr Canvas-Messaging zu optimieren. Weitere Details zu dieser Komponente finden Sie unter [Nachricht]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

![Der Schritt „Nachrichten einrichten" mit ausgewählten „Messaging-Kanälen", der die Liste der verfügbaren Messaging-Kanäle anzeigt, z. B. Android Push, Content-Cards, E-Mail und mehr.]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

Wählen Sie **Fertig**, nachdem Sie die Konfiguration Ihrer Canvas-Komponente abgeschlossen haben.

{% tabs local %}
{% tab Canvas Entry Properties %}

Das [`context`-Objekt]({{site.baseurl}}/api/objects_filters/context_object) wird im Schritt **Eingangszeitplan** bei der Erstellung eines Canvas konfiguriert und gibt den Trigger an, der Nutzer:innen in ein Canvas eintreten lässt. Diese Eigenschaften können auch auf die Eigenschaften von Eingangs-Payloads in API-getriggerten Canvasen zugreifen. Beachten Sie, dass das `context`-Objekt bis zu 50 KB groß sein kann. 

Verwenden Sie das folgende Liquid, wenn Sie auf diese beim Eintritt in das Canvas erstellten Eigenschaften verweisen: {% raw %} ``context.${property_name}`` {% endraw %}. Beachten Sie, dass es sich bei den Events um angepasste Events oder Kauf-Events handeln muss, um auf diese Weise verwendet werden zu können.

{% raw %}
Betrachten Sie zum Beispiel die folgende Anfrage: `\"context\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Mit diesem Liquid ``{{context.${product_name}}}`` können Sie das Wort „shoes" in eine Nachricht einfügen.
{% endraw %}

{% endtab %}

{% tab Event Properties %}
Event-Eigenschaften sind die Eigenschaften, die Sie für angepasste Events und Käufe festlegen. Diese `event_properties` können sowohl in Kampagnen mit aktionsbasierter Zustellung als auch in Canvasen verwendet werden. 

In Canvas können angepasste Event- und Kauf-Event-Eigenschaften in Liquid in jedem Nachrichtenschritt verwendet werden, der auf einen Aktions-Pfade-Schritt folgt. Verwenden Sie dieses Liquid {% raw %} ``{{event_properties.${property_name}}}`` {% endraw %}, wenn Sie auf diese `event_properties` verweisen. Diese Events müssen angepasste Events oder Kauf-Events sein, um auf diese Weise in der Nachrichtenkomponente verwendet werden zu können.

Im ersten Nachrichtenschritt nach einem Aktions-Pfad können Sie `event_properties` verwenden, die sich auf das in diesem Aktions-Pfad referenzierte Event beziehen. Zwischen dem Aktions-Pfade-Schritt und dem Nachrichtenschritt können weitere Schritte liegen (die keine anderen Aktions-Pfade oder Nachrichtenschritte sind). Beachten Sie, dass Sie nur dann auf `event_properties` zugreifen können, wenn Ihr Nachrichtenschritt auf einen Nicht-Alle-anderen-Pfad in einem Aktions-Pfade-Schritt zurückverfolgt werden kann.

{% endtab %}
{% endtabs %}

#### Schritt 2.3: Verbindungen bearbeiten

Um eine Verbindung zwischen Schritten zu verschieben, wählen Sie den Pfeil, der die beiden Komponenten verbindet, und dann eine andere Komponente aus. Um die Verbindung zu entfernen, wählen Sie den Pfeil und dann **Verbindung abbrechen** in der Fußzeile des Canvas-Composers.

### Schritt 3: Eine Kontrollgruppe hinzufügen

Sie können eine Kontrollgruppe zu Ihrem Canvas hinzufügen, indem Sie den <i class="fas fa-plus-circle"></i> Plus-Button auswählen, um eine neue Variante hinzuzufügen. 

Braze verfolgt die Konversionen der Nutzer:innen in der Kontrollgruppe, obwohl diese keine Nachrichten erhalten. Um einen genauen Test zu gewährleisten, verfolgen wir die Anzahl der Konversionen für Ihre Varianten und die Kontrollgruppe für genau denselben Zeitraum, wie auf dem Bildschirm zur Auswahl des Konversions-Events angezeigt. 

Sie können die Verteilung zwischen Ihren Nachrichten anpassen, indem Sie auf die Überschriften der **Variantennamen** doppelklicken.

In diesem Beispiel haben wir unser Canvas in zwei Varianten unterteilt. Variante 1 hat 70 % der Nutzer:innen. Die zweite Variante ist eine Kontrollgruppe mit den restlichen 30 % der Nutzer:innen.

![Eine Beispielvariante in einem Braze-Canvas, bei der 70 % auf „Variante 1" entfallen, die im ersten Schritt um 1 Tag verzögert und dann im zweiten Schritt eine Nachricht sendet. Die anderen 30 % gehen an eine „Kontrolle", die keine weiteren Schritte hat.]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### Intelligente Auswahl für Canvas

In multivariaten Canvasen sind jetzt Funktionen zur intelligenten Auswahl verfügbar. Ähnlich wie das Feature [Intelligente Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) für multivariate Kampagnen analysiert die intelligente Auswahl für Canvas die Performance der einzelnen Canvas-Varianten und passt den Prozentsatz der Nutzer:innen an, die durch die einzelnen Varianten geleitet werden. Diese Verteilung basiert auf den Performance-Metriken der einzelnen Varianten, um die erwartete Gesamtzahl der Konversionen zu maximieren.

Denken Sie daran, dass Sie mit multivariaten Canvasen nicht nur Texte, sondern auch Timing und Kanäle testen können. Mit der intelligenten Auswahl können Sie Canvase effizienter testen und darauf vertrauen, dass Ihre Nutzer:innen auf die bestmögliche Canvas-Journey geschickt werden.

![Die Option „Intelligente Auswahl" ist auf der Seite „Variantenverteilung bearbeiten" aktiviert. Bei der Analyse und Optimierung des Canvas wird ein horizontaler Balken quer über die Seite angezeigt, der in mehrere Abschnitte unterteilt ist, die jeweils in Farbe und Größe variieren. Dies ist nur eine visuelle Darstellung und steht in keinem Zusammenhang mit bestimmten Analytics.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

Die intelligente Auswahl für Canvas optimiert Ihre Canvas-Ergebnisse, indem sie schrittweise Realtime-Anpassungen an der Verteilung der in jede Variante sortierten Nutzer:innen vornimmt. Wenn der statistische Algorithmus einen entscheidenden Gewinner unter Ihren Varianten ermittelt, schließt er die leistungsschwächeren Varianten aus und ordnet alle zukünftigen berechtigten Empfänger:innen des Canvas den Gewinnervarianten zu. 

Aus diesem Grund funktioniert die intelligente Auswahl am besten bei Canvasen, in die häufig neue Nutzer:innen eintreten.

### Schritt 4: Speichern und starten

Nachdem Sie Ihr Canvas erstellt haben, wählen Sie **Canvas starten**, um Ihr Canvas zu speichern und zu starten. Nachdem Sie Ihr Canvas gestartet haben, können Sie auf der Seite **Canvas-Details** die Analytics für Ihre Journey einsehen, sobald diese eintreffen. 

Sie können Ihr Canvas auch als Entwurf speichern, wenn Sie darauf zurückkommen möchten.

![Ein Beispiel-Canvas in Braze.]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
Müssen Sie nach dem Start Änderungen an Ihrem Canvas vornehmen? Das ist möglich! Weitere Informationen finden Sie unter [Canvase nach dem Start bearbeiten]({{site.baseurl}}/post-launch_edits/).
{% endalert %}