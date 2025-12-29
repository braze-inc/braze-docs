---
nav_title: Eine E-Mail erstellen
article_title: Erstellen einer E-Mail mit benutzerdefiniertem HTML
page_order: 1
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie eine E-Mail mit der Braze-Plattform erstellen. Darin enthalten sind bewährte Verfahren für das Verfassen Ihrer Nachrichten, die Vorschau Ihrer Inhalte und die Planung Ihrer Kampagne oder Ihres Canvas."
tool:
  - Campaigns
channel:
  - email
search_rank: 1  
---

# Erstellen einer E-Mail mit benutzerdefiniertem HTML

> E-Mail-Nachrichten eignen sich hervorragend, um Ihren Nutzern Inhalte zu ihren Bedingungen zu übermitteln. Sie sind auch ein hervorragendes Instrument, um Nutzer, die Ihre App vielleicht sogar deinstalliert haben, wieder anzusprechen. Das Versenden von individuellen und maßgeschneiderten E-Mail-Nachrichten verbessert die Erfahrung Ihrer Nutzer und hilft ihnen, den größten Nutzen aus Ihrer App zu ziehen. 

Wenn Sie Beispiele für E-Mail-Kampagnen sehen möchten, schauen Sie sich unsere [Fallstudien](https://www.braze.com/customers) an. 

{% alert tip %}
Wenn Sie zum ersten Mal eine Kampagne per E-Mail erstellen, empfehlen wir Ihnen diese Braze-Lernkurse:<br><br>
- [E-Mail Opt-Ins und Genehmigungen](https://learning.braze.com/messaging-channels-email)
- [Projekt: Grundlegendes E-Mail Marketing-Programm erstellen](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## Schritt 1: Wählen Sie, wo Sie Ihre Botschaft aufbauen möchten

Sie sind sich nicht sicher, ob Ihre Nachricht über eine Kampagne oder ein Canvas versendet werden soll? Kampagnen eignen sich eher für einzelne einfache Messaging-Kampagnen, während Canvases besser für mehrstufige User Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**.
2. Wählen Sie **E-Mail**, oder für Kampagnen, die auf mehrere Kanäle abzielen, wählen Sie **Multichannel**.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu.
   * Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen. Wenn Sie zum Beispiel den [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.
5. Fügen Sie so viele Varianten hinzu, wie Sie für Ihre Kampagne benötigen, und benennen Sie sie. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Kampagne ähnlich sind oder den gleichen Inhalt haben, sollten Sie Ihre Nachricht verfassen, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann aus der Dropdown-Liste **Variante hinzufügen** die Option **Aus Variante kopieren** wählen.
{% endalert %}
{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) mit dem Canvas Composer.
2. Wenn Sie den Canvas eingerichtet haben, fügen Sie im Canvas Builder einen Schritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie einen [Zeitplan für den Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) und geben Sie bei Bedarf eine Verzögerung an.
4. Filtern Sie Ihre Zielgruppe für diesen Schritt, falls erforderlich. Sie können den Empfängerkreis mit Segmenten und zusätzlichen Filtern weiter eingrenzen. Die Zielgruppen-Optionen werden nach dem Delay, zum Zeitpunkt des Versands der Nachrichten, überprüft.
5. Legen Sie das [Fortschrittsverhalten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) fest.
6. Wählen Sie andere Messaging-Kanäle, die Sie mit Ihrer Nachricht verbinden möchten.
{% endtab %}
{% endtabs %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## Schritt 2: Wählen Sie Ihre Bearbeitungserfahrung {#step-2-choose-your-template-and-compose-your-email}

Braze bietet zwei Bearbeitungsmöglichkeiten für die Erstellung einer E-Mail-Kampagne: unseren [Drag-and-Drop-Editor]({{site.baseurl}}/dnd/) und unseren Standard-HTML-Editor. Wählen Sie die passende Kachel für die gewünschte Bearbeitungsumgebung aus. 

![Sie haben die Wahl zwischen dem Drag-and-Drop-Editor, dem HTML-Editor oder Templates für die Bearbeitung Ihrer E-Mails.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

Dann können Sie entweder eine vorhandene [E-Mail-Vorlage]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template) auswählen, eine Vorlage aus einer Datei [hochladen]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/) (nur HTML-Editor) oder eine leere Vorlage verwenden. 

{% alert tip %}
Wir empfehlen, pro E-Mail Kampagne eine Bearbeitungsumgebung auszuwählen. Wählen Sie zum Beispiel in einer einzigen E-Mail Kampagne entweder den Editor **Klassischer HTML-Editor** oder **Block-Editor** aus, anstatt zwischen den Editoren zu wechseln.
{% endalert %}

## Schritt 3: E-Mail-Nachricht verfassen

Nachdem Sie Ihre Vorlage ausgewählt haben, sehen Sie eine Übersicht über Ihre E-Mail, in der Sie direkt zum Vollbild-Editor wechseln können, um Ihre E-Mail zu verfassen, Ihre Versandinformationen zu ändern und Warnungen zur Zustellbarkeit oder zur Einhaltung von Gesetzen anzuzeigen. Sie können zwischen HTML-, klassischen, Klartext- und [AMP-Tabs]({{site.baseurl}}/user_guide/message_building_by_channel/email/amphtml/) wechseln, während Sie schreiben. 

![Der Button "Aus HTML neu generieren".]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

Die Klartextversion Ihrer E-Mail wird immer automatisch von der HTML-Version aktualisiert, bis eine Änderung an der Klartextversion erkannt wird. Wenn eine Bearbeitung erkannt wird, wird Braze den Klartext nicht mehr aktualisieren, da wir davon ausgehen, dass Sie absichtlich Änderungen vorgenommen haben, die nicht überschrieben werden sollten. Sie können auf dem Tab **Klartext** zur automatischen Synchronisierung zurückkehren, indem Sie das Symbol **Aus HTML neu generieren** auswählen, das nur erscheint, wenn der Klartext nicht synchronisiert wird.

{% alert tip %}
Zur Erstellung von E-Mails mit Bewegungselementen und einer genauen Vorschau sollten Sie GIFs anstelle von Elementen verwenden, die JavaScript erfordern, da die meisten Posteingänge JavaScript nicht unterstützen.
{% endalert %}

![Panel für E-Mail-Varianten zum Verfassen Ihrer E-Mail.]({% image_buster /assets/img/email.png %}){: style="max-width:75%" }

{% alert important %}
Braze entfernt automatisch HTML-Event-Handler, die als Attribute referenziert werden. Dadurch wird der HTML-Code geändert. Es empfiehlt sich daher, die E-Mail nach der Fertigstellung erneut zu überprüfen. Erfahren Sie mehr über [HTML-Handler](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

{% alert tip %}
Benötigen Sie Hilfe bei der Erstellung überzeugender Texte? Versuchen Sie es mit dem [KI-Textwerkstatt-Assistenten]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Geben Sie einen Produktnamen oder eine Beschreibung ein und die KI generiert menschenähnliche Marketingtexte für Ihre Werbebotschaften.

![KI Copywriter Button starten, der sich auf dem Tab Body des E-Mail Composers befindet.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

Benötigen Sie Hilfe bei der Erstellung von Nachrichten von rechts nach links für Sprachen wie Arabisch und Hebräisch? Lesen Sie den Abschnitt [Erstellen von Nachrichten von rechts nach links]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) für bewährte Verfahren.

### Schritt 3a: Sendeinformationen hinzufügen

Nachdem Sie Ihre E-Mail-Nachricht entworfen und erstellt haben, ist es an der Zeit, Ihre Versandinformationen im Bereich **Sendeeinstellungen** hinzuzufügen.

1. Wählen Sie unter **Sende-Info** eine E-Mail als **Absender-Anzeigename + Adresse**. Sie können dies auch anpassen, indem Sie **Anpassen aus Anzeigename + Adresse** wählen.
2. Wählen Sie eine E-Mail als **Reply-To Adresse**. Sie können diese auch anpassen, indem Sie **Antwortadresse anpassen** auswählen.
3. Wählen Sie dann eine E-Mail als **BCC-Adresse**, damit Ihre E-Mail für diese Adresse sichtbar ist.
4. Fügen Sie eine Betreffzeile zu Ihrer E-Mail hinzu. Optional können Sie auch einen Preheader und ein Leerzeichen nach dem Preheader hinzufügen.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Im rechten Panel wird eine Vorschau mit Ihren Sendeinformationen eingeblendet. Diese Informationen können auch unter **Einstellungen** > **E-Mail-Einstellungen** > **Sendekonfiguration** aktualisiert werden.

#### Erweitert

Unter **Sendeeinstellungen** > **Erweitert** können Sie Inline-CSS aktivieren und eine Personalisierung für E-Mail-Kopfzeilen und E-Mail-Extras hinzufügen, mit der Sie zusätzliche Daten an andere E-Mail-Dienstanbieter zurücksenden können.

##### E-Mail-Kopfzeilen

Um E-Mail-Header hinzuzufügen, wählen Sie **Neuen Header hinzufügen**. E-Mail-Kopfzeilen enthalten Informationen über die gesendete E-Mail. Diese [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) enthalten in der Regel Informationen über Absender, Empfänger, Authentifizierungsprotokolle und E-Mail-Routing-Informationen. Braze fügt automatisch die vom RFC geforderten Header-Informationen hinzu, damit die E-Mails ordnungsgemäß an Ihren Posteingangsanbieter zugestellt werden können.

Braze lässt Ihnen die Flexibilität, bei Bedarf zusätzliche E-Mail-Header für fortgeschrittene Anwendungsfälle hinzuzufügen. Es gibt einige reservierte Felder, die von der Braze-Plattform beim Senden überschrieben werden. 

Vermeiden Sie die Verwendung der folgenden Tasten:

<style>
#reserved-fields td {
    word-break: break-word;
    width: 33%;
}
</style>

<table id="reserved-fields">
<thead>
  <tr>
    <th>Reservierte Felder</th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BCC</td>
    <td>dkim-signature</td>
    <td>Antwort an</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>Von</td>
    <td>Betreff</td>
  </tr>
  <tr>
    <td>Content-Transfer-Encoding</td>
    <td>MIME-Version</td>
    <td>An</td>
  </tr>
  <tr>
    <td>Content-Typ</td>
    <td>Empfangen</td>
    <td>x-sg-eid</td>
  </tr>
  <tr>
    <td>DKIM-Signatur</td>
    <td>erhalten</td>
    <td>x-sg-id</td>
  </tr>
</tbody>
</table>

##### Hinzufügen von E-Mail-Extras

Mit E-Mail-Extras können Sie zusätzliche Daten an andere Anbieter von E-Mail Diensten zurücksenden. Dies gilt nur für fortgeschrittene Anwendungsfälle. Sie sollten E-Mail-Extras also nur verwenden, wenn Ihr Unternehmen dies bereits eingerichtet hat.

Um E-Mail-Extras hinzuzufügen, gehen Sie zu den **Versandinformationen** und wählen Sie **Neues Extra hinzufügen**.

{% alert warning %}
Die Summe der hinzugefügten Schlüssel-Wert-Paare sollte 1 KB nicht überschreiten. Andernfalls werden die Nachrichten abgebrochen.
{% endalert %}

E-Mail-Extrawerte werden nicht in Currents oder Snowflake veröffentlicht. Wenn Sie zusätzliche Metadaten oder dynamische Werte an Currents oder Snowflake senden möchten, verwenden Sie stattdessen [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/).

### Schritt 3b: Nachricht in der Vorschau anzeigen und testen

Nachdem Sie Ihre perfekte E-Mail verfasst haben, müssen Sie sie testen, bevor Sie sie versenden. Wählen Sie unten auf dem Übersichtsbildschirm **Vorschau und Test** aus. 

Hier können Sie eine Vorschau darauf sehen, wie Ihre E-Mail im Posteingang eines Kunden erscheinen wird. Wenn Sie **Vorschau als Benutzer** ausgewählt haben, können Sie Ihre E-Mail als zufälliger Benutzer anzeigen lassen, einen bestimmten Benutzer auswählen oder einen benutzerdefinierten Benutzer erstellen. So können Sie testen, ob Ihre Connected-Content- und Personalisierungsaufrufe wie gewünscht funktionieren. 

Dann können Sie **Vorschau-Link kopieren**, um einen Vorschau-Link zu erzeugen und zu kopieren, der zeigt, wie die E-Mail für einen zufälligen Nutzer:innen aussehen wird. Der Link bleibt sieben Tage lang bestehen, bevor er erneuert werden muss.

Sie können auch zwischen der Desktop-, der Mobil- und der Klartextansicht wechseln, um ein Gefühl dafür zu bekommen, wie Ihre Nachricht in verschiedenen Kontexten erscheinen wird.

{% alert tip %}
Sind Sie neugierig, wie Ihre E-Mails für Nutzer:innen im Dark Mode aussehen? Wählen Sie den Schalter für die **Vorschau im dunklen Modus** im Bereich **Vorschau und Test** (nur im Drag & Drop-Editor).
{% endalert %}

Wenn Sie für eine abschließende Prüfung bereit sind, wählen Sie **Senden testen** und senden Sie eine Testnachricht an sich selbst oder an eine Gruppe von Inhaltstestern, um sicherzustellen, dass Ihre E-Mail auf einer Vielzahl von Geräten und E-Mail-Clients korrekt angezeigt wird.

![Test-Sendeoption und Vorschau einer Beispiel-E-Mail beim Verfassen Ihrer E-Mail.]({% image_buster /assets/img_archive/newEmailTest.png %})

Wenn Sie Probleme mit Ihrer E-Mail sehen oder Änderungen vornehmen möchten, wählen Sie **E-Mail bearbeiten**, um zum Editor zurückzukehren.

{% alert tip %}
E-Mail Clients, die eine Vorschau unterstützen, ziehen immer so viele Zeichen ein, dass der gesamte verfügbare Platz für den Vorschautext ausgefüllt wird. Dies kann jedoch dazu führen, dass der Text in der Vorschau unvollständig oder nicht optimiert ist.
<br><br>Um dies zu vermeiden, können Sie nach dem gewünschten Vorschautext Leerzeichen einfügen, damit E-Mail-Clients keine anderen störenden Texte oder Zeichen in den Umschlag-Content einfügen. Fügen Sie dazu nach dem Vorschautext, der angezeigt werden soll, eine Kette von Nicht-Verbindungszeichen mit Null-Breite (`&zwnj;`) und Nicht-Umbruch-Leerzeichen (`&nbsp;`) ein. <br><br>Wenn Sie den folgenden Code für den HTML-Editor an das Ende Ihres Vorschautextes im Preheader-Bereich anfügen, wird der gewünschte Leerraum hinzugefügt:<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```
Für den Drag-and-Drop-Editor fügen Sie nur die Nicht-Joiners mit Null-Breite (`&zwnj;`) ohne die `<div>` Formatierung direkt in den Preheader im Abschnitt **Sendeeinstellungen** ein.

{% endalert %}

### Schritt 3c: Auf E-Mail-Fehler prüfen

Der Editor weist Sie auf alle Probleme hin, die er in Ihrer Nachricht entdeckt, bevor Sie sie abschicken. Hier finden Sie eine Liste der Fehler, die in unserem Editor berücksichtigt werden:

- **Von Anzeigename** und **Überschrift** nicht zusammen angegeben
- Ungültige **Absender-** und **Reply-To-Adressen** 
- Doppelte **Header**-Schlüssel
- Liquid Syntax Probleme
- E-Mail-Textkörper, die größer als 400kb sind (es wird dringend empfohlen, dass sie [kleiner als 102kb]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size) sind)
- E-Mails mit leerem **Text** oder **Betreff**
- E-Mails ohne Link zum Abbestellen
- Die E-Mail, von der aus Sie senden, steht nicht auf der Liste der zulässigen Absender (der Versand wird stark eingeschränkt, um die Zustellbarkeit zu gewährleisten)

## Schritt 4: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas

{% tabs %}
{% tab Campaign %}
Bauen Sie nun den Rest Ihrer Kampagne auf! In den folgenden Abschnitten finden Sie weitere Informationen darüber, wie Sie unsere Tools am besten für Ihre E-Mail-Kampagne nutzen können.

#### Zeitplan für die Zustellung oder Trigger wählen

E-Mails können auf der Grundlage eines Zeitplans, einer Aktion oder eines API-Triggers zugestellt werden. Mehr dazu erfahren Sie unter [Planen Ihrer Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

{% alert note %}
Wenn bei API-ausgelösten Kampagnen die Auslöseaktion auf **Mit Kampagne interagieren** eingestellt ist, führt die Auswahl der Option **Empfangen** als Interaktion dazu, dass Ihre neue Kampagne ausgelöst wird, sobald Braze die ausgewählte Kampagne als gesendet markiert, selbst wenn die Nachricht abprallt oder nicht zugestellt werden kann.
{% endalert %}

Sie können auch die Dauer der Kampagne festlegen, [stille Stunden]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) angeben und Regeln für [die Begrenzung der Häufigkeit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) festlegen.

#### Wählen Sie Benutzer als Zielgruppe aus

Als Nächstes müssen Sie mithilfe von Segmenten oder Filtern eine [Zielgruppe erstellen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/). Sie erhalten automatisch eine Vorschau darauf, wie die Population dieses Segments im Moment aussieht und wie viele Nutzer:innen in diesem Segment per E-Mail erreichbar sind. Denken Sie daran, dass die genaue Segmentzugehörigkeit immer erst kurz vor dem Versand der Nachricht berechnet wird.

{% multi_lang_include target_audiences.md %}

Sie können Ihre Kampagne auch nur an Benutzer senden, die einen bestimmten [Abonnementstatus]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) haben, z. B. an diejenigen, die ein Abonnement abgeschlossen und sich für E-Mails angemeldet haben.

Optional können Sie auch die Zustellung auf eine bestimmte Anzahl von Nutzern innerhalb des Segments beschränken oder zulassen, dass Nutzer die gleiche Nachricht bei einer Wiederholung der Kampagne zweimal erhalten.

##### Mehrkanalige Kampagnen mit E-Mail und Push

Bei Multichannel-Kampagnen, die sowohl auf E-Mail- als auch auf Push-Kanäle abzielen, möchten Sie Ihre Kampagne möglicherweise so einschränken, dass nur die Nutzer, die sich explizit dafür entschieden haben, die Nachricht zu erhalten (unter Ausschluss der abonnierten oder abgemeldeten Nutzer). Nehmen wir an, Sie haben drei Nutzer:innen mit unterschiedlichem Opt-in-Status:

- **Nutzer:in** ist auf E-Mail abonniert und hat Push aktiviert. Diese Nutzer:innen erhalten die E-Mail nicht, aber den Push.
- **Benutzer B** hat sich für E-Mails entschieden, ist aber nicht für Push aktiviert. Dieser Benutzer erhält die E-Mail, aber nicht die Push-Mitteilung.
- **Nutzer:in** in hat Opt-in für E-Mail und ist für Push aktiviert. Dieser Benutzer erhält sowohl die E-Mail als auch die Push-Mitteilung.

Wählen Sie dazu unter **Zielgruppen-Zusammenfassung** aus, dass diese Kampagne nur an „Opted-in Nutzer:innen“ gesendet werden soll. Mit dieser Option stellen Sie sicher, dass nur Nutzer, die sich dafür entschieden haben, Ihre E-Mail erhalten, und Braze sendet Ihre Push-Nachrichten nur an Nutzer, die standardmäßig für Push aktiviert sind.

{% alert important %}
Fügen Sie bei dieser Konfiguration keine Filter in den Schritt **Zielgruppen** ein, die die Zielgruppe auf einen einzigen Kanal beschränken (z.B. `Foreground Push Enabled = True` oder `Email Subscription = Opted-In`).
{% endalert %}

#### Wählen Sie Konversionsereignisse aus

Mit Braze können Sie nachverfolgen, wie oft Benutzer nach Erhalt einer Kampagne bestimmte Aktionen, d.h. [Conversion Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), durchführen. Sie können jede der folgenden Aktionen als Konversions-Event angeben:

- Öffnet App
- Tätigt einen Kauf (Dies kann ein allgemeiner Kauf oder ein bestimmter Artikel sein)
- Führt ein bestimmtes benutzerdefiniertes Ereignis aus
- Öffnet E-Mail

Sie können ein Zeitfenster von bis zu 30 Tagen zulassen, in dem eine Konversion gezählt wird, wenn die angegebene Aktion durchgeführt wird. Braze verfolgt zwar automatisch die Öffnungen und Klicks für Ihre Kampagne, aber Sie können das Konvertierungsereignis so einstellen, dass es eintritt, wenn ein Benutzer eine E-Mail-Adresse öffnet oder anklickt, um die Vorteile der [intelligenten Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) zu nutzen.
{% endtab %}

{% tab Canvas %}
Falls noch nicht geschehen, füllen Sie die restlichen Abschnitte der Canvas-Komponente aus. Weitere Einzelheiten zum Aufbau des restlichen Canvas, zur Implementierung von multivariaten Tests und intelligenter Auswahl und mehr finden Sie im Schritt [Aufbau Ihres Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) in unserer Canvas-Dokumentation.
{% endtab %}
{% endtabs %}

## Schritt 5: Überprüfen und einsetzen

Im letzten Abschnitt erhalten Sie eine Zusammenfassung der Kampagne, die Sie gerade entworfen haben. Bestätigen Sie alle relevanten Details und wählen Sie **Kampagne starten**. Jetzt ist es an der Zeit, auf die Daten zu warten! 

Wie Sie die Ergebnisse Ihrer E-Mail-Kampagnen einsehen können, erfahren Sie unter [E-Mail-Berichterstattung]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/).

