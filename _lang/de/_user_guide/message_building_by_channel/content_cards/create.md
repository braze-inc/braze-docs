---
nav_title: Erstellen einer Content-Card
article_title: Erstellen einer Inhaltskarte
page_order: 0
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Content-Cards mit Kampagnen und Canvase von Braze erstellen, zusammenstellen, konfigurieren und versenden."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Erstellen einer Inhaltskarte

> Dieser Artikel beschreibt, wie Sie eine Content-Card in Braze erstellen, wenn Sie Kampagnen und Canvase erstellen. Hier führen wir Sie durch die Auswahl eines Nachrichtentyps, das Verfassen Ihrer Karte und die Planung der Zustellung Ihrer Nachricht.

## Schritt 1: Wählen Sie, wo Sie Ihre Botschaft aufbauen möchten

Sie sind sich nicht sicher, ob Ihre Nachricht mit einer Kampagne oder einem Canvas gesendet werden soll? Kampagnen eignen sich besser für einzelne, einfache Mitteilungskampagnen (z. B. um Benutzer mit einer einzigen Nachricht über ein neues Produkt zu informieren), während Canvases besser für mehrstufige User Journeys geeignet sind (z. B. um maßgeschneiderte Produktvorschläge auf der Grundlage des Benutzerverhaltens im Laufe der Zeit zu versenden).

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**.
2. Wählen Sie **Content-Cards** oder, für Kampagnen, die auf mehrere Kanäle zielen, **Multichannel** aus.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu.
   * Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen. Wenn Sie zum Beispiel den [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) verwenden, können Sie nach den entsprechenden Tags filtern.
5. Fügen Sie beliebig viele Varianten für Ihre Kampagne hinzu und benennen Sie sie. Sie können für jede hinzugefügte Variante verschiedene Plattformen, Nachrichtentypen und Layouts auswählen. Mehr über Varianten erfahren Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Kampagne ähnlich sind oder den gleichen Inhalt haben, sollten Sie Ihre Nachricht verfassen, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann aus dem Dropdown-Menü **Variante hinzufügen** die Option **Aus Variante kopieren** auswählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) mit dem Canvas Composer.
2. Nachdem Sie Ihr Canvas eingerichtet haben, fügen Sie einen Nachrichtenschritt in den Canvas-Builder ein. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie **Content Cards** als Ihren Nachrichtenkanal.
4. Legen Sie fest, wann Braze die Eignung der Zielgruppe und die Personalisierung für die Content Card berechnet. Dies kann beim Entry oder bei der ersten Impression geschehen (empfohlen). Schritte, die Content-Cards enthalten, können zeitplan- oder aktionsbasiert sein.
5. Legen Sie fest, ob Inhaltskarten entfernt werden sollen, wenn Benutzer einen Kauf abschließen oder ein benutzerdefiniertes Ereignis ausführen.
6. Legen Sie ein Verfallsdatum für die Inhaltskarte fest (Zeit im Feed). Dies kann nach einer bestimmten Zeitspanne oder zu einem bestimmten Zeitpunkt geschehen.
7. Filtern Sie Ihre Zielgruppe bzw. die Empfänger für diesen Schritt nach Bedarf in den **Zustellungseinstellungen**. Sie können Ihre Zielgruppe weiter verfeinern, indem Sie Segmente angeben und zusätzliche Filter hinzufügen. Die Zielgruppen-Optionen werden nach dem Delay, zum Zeitpunkt des Versands der Nachrichten, überprüft.
8. Wählen Sie andere Messaging-Kanäle, die Sie mit Ihrer Nachricht verbinden möchten.

{% endtab %}
{% endtabs %}

## Schritt 2: Nachrichtentypen angeben

Wählen Sie einen der drei wesentlichen Content-Card-Typen aus: **Klassisch**, **Bild mit Untertitel** und **Nur Bild**. 

Wenn Sie mehr über das erwartete Verhalten und das Aussehen der einzelnen Typen erfahren möchten, lesen Sie die [Kreativdetails]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/) oder die Links in der folgenden Tabelle. Diese Content-Card-Typen werden sowohl von mobilen Apps als auch von Webanwendungen akzeptiert.

| Nachrichtentyp | Beispiel | Beschreibung |
|---|---|---|
|[Klassisch]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| ![Eine klassische Content-Card mit einem kleinen Symbol und Text, um Sie zur Buchung eines Trainingskurses anzuregen.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |Die Classic Card hat ein einfaches Layout mit einem fettgedruckten Titel, einem Nachrichtentext und einem optionalen Bild, das links neben dem Titel und dem Text platziert wird. Für die Classic Card verwenden Sie am besten ein quadratisches Bild oder Symbol. |
|[Bild mit Bildunterschrift]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| ![Eine Content-Card mit einem Bild eines Gewichthebers und einem Text, der zur Buchung eines Trainingskurses anregt.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | Die hervorgehobene Image-Card präsentiert Ihren Inhalt mit Text und einem aufmerksamkeitsstarken Bild. |
|[Nur Bild]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| ![Eine Content-Card nur mit Bild und nur mit Text.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | Die Karte mit reinem Bildinhalt bietet Platz für Bilder, GIFs und andere kreative Nicht-Text-Inhalte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Schritt 3: Content-Card zusammenstellen

Auf der Registerkarte **Verfassen** des Nachrichteneditors können Sie alle Aspekte des Inhalts und Verhaltens Ihrer Nachricht bearbeiten.

![Beispiel Content-Card Details im Tab Verfassen des Nachrichten-Editors.]({% image_buster /assets/img/content_card_compose.png %})

Der Inhalt variiert je nach dem im vorherigen Schritt gewählten **Kartentyp**, kann aber eine der folgenden Optionen enthalten:

#### Sprache

Wählen Sie **Sprachen hinzufügen**, um die gewünschten Sprachen aus der vorgegebenen Liste hinzuzufügen. Dadurch wird [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) in Ihre Nachricht eingefügt. Wählen Sie die Sprachen am besten aus, bevor Sie den Content verfassen, damit Sie den Text dort einfügen können, wo er im Liquid hingehört. Eine vollständige Liste der Sprachen, die Sie verwenden können, finden Sie unter [Unterstützte Sprachen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

![Ein Fenster, in dem Englisch, Spanisch und Französisch als Sprachen ausgewählt sind und Titel, Beschreibung und Linktext als zu internationalisierende Felder ausgewählt sind.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

##### Erstellen von Nachrichten von rechts nach links

Wie Nachrichten von rechts nach links letztendlich aussehen, hängt weitgehend davon ab, wie die Diensteanbieter sie darstellen. Bewährte Methoden zur Erstellung von Nachrichten, die so genau wie möglich angezeigt werden, finden Sie unter [Erstellen von Nachrichten von]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) rechts nach links.

#### Titel und Nachricht

Werden Sie kreativ. Es gibt keine Grenzen, aber je schneller Sie Ihre Botschaft übermitteln und Ihren Kunden zum Klicken bringen können, desto besser! Wir empfehlen klare und prägnante Titel und Nachrichteninhalte. Beachten Sie, dass diese Felder bei Nur-Bild-Karten nicht vorhanden sind.

#### Bild

Fügen Sie ein Bild zu Ihrer Inhaltskarte hinzu, indem Sie **Bild hinzufügen** wählen oder eine Bild-URL angeben. Wenn Sie **Bild hinzufügen** wählen, öffnet sich die **Mediathek**, in der Sie ein zuvor hochgeladenes Bild auswählen oder ein neues Bild hinzufügen können. Für jede Art von Nachricht und jede Plattform können eigene Proportionen und Anforderungen gelten. Informieren Sie sich daher unbedingt darüber, bevor Sie einen Auftrag erteilen oder ein Bild von Grund auf neu erstellen! Denken Sie daran, dass die Nachrichtenfelder der Content-Cards auf eine Gesamtgröße von 2 KB begrenzt sind.

#### Oben pinnen

Eine angeheftete Karte wird oben im Feed eines Benutzers angezeigt und kann vom Benutzer nicht abgewählt werden. Wenn mehr als eine Karte im Feed eines Benutzers angeheftet ist, werden die angehefteten Karten in chronologischer Reihenfolge angezeigt. Nachdem eine Karte versendet wurde, können Sie die angeheftete Option nicht mehr rückwirkend aktualisieren. Wenn Sie diese Option nach dem Versand einer Kampagne ändern, wirkt sich dies nur auf zukünftige Sendungen aus.

![Seite an Seite der Vorschau der Content-Cards in Braze for Mobile und Internet mit der ausgewählten Option "Diese Karte an den Anfang des Feeds heften".]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### On-Click-Verhalten

Wenn Ihr Kunde auf einen in der Karte dargestellten Link klickt, kann Ihr Link ihn entweder tiefer in Ihre App oder auf eine andere Website führen. Wenn Sie ein On-Click-Verhalten für Ihre Content Card wählen, denken Sie daran, Ihren **Linktext** entsprechend zu aktualisieren.

Die folgenden Aktionen sind für Content-Card-Verknüpfungen verfügbar:

| Aktion | Beschreibung |
|---|---|
| Weiterleitung zu Web-URL | Öffnen Sie eine nicht-native Webseite. |
| [Deeplink in die App]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Setzt einen Deeplink in einen Bildschirminhalt der App. |
| Angepasstes Event protokollieren | Wählen Sie ein [benutzerdefiniertes Ereignis]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) zum Auslösen. Kann verwendet werden, um eine andere Inhaltskarte anzuzeigen oder zusätzliche Nachrichten auszulösen. |
| Angepasstes Attribut protokollieren | Wählen Sie ein [benutzerdefiniertes Attribut]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), das für den aktuellen Benutzer festgelegt werden soll. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Die Optionen **Angepasstes Event protokollieren** und **Angepasstes Attribut protokollieren** erfordern die folgende SDK-Versionskompatibilität:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Schritt 4: Konfigurieren Sie zusätzliche Einstellungen (optional)

Sie können [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) verwenden, um Kategorien für Ihre Karten zu erstellen, [mehrere Content Card Feeds]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) anzulegen und die Sortierung der Karten anzupassen.

Um Schlüssel-Wert-Paare zu Ihrer Nachricht hinzuzufügen, gehen Sie auf die Registerkarte **Einstellungen** und wählen Sie **Neues Paar hinzufügen**.

## Schritt 5: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas

{% tabs %}
{% tab Campaign %}

Bauen Sie den Rest Ihrer Kampagne auf. In den nächsten Abschnitten erfahren Sie mehr darüber, wie Sie unsere Tools zur Erstellung von Content Cards am besten einsetzen.

#### Wählen Sie einen Zustellungszeitplan oder einen Auslöser

Content-Cards können auf der Grundlage eines Zeitplans, einer Aktion oder eines API-Triggers zugestellt werden. Mehr dazu erfahren Sie unter [Planen Ihrer Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Sie können auch die Dauer der Kampagne und die [Ruhezeiten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) festlegen und das Verfallsdatum der Content Card bestimmen. Legen Sie ein bestimmtes Ablaufdatum oder die Tage bis zum Ablauf der Karte fest, bis zu 30 Tage. Alle Varianten haben das gleiche Verfallsdatum.

{% alert note %}
Die Frequenzbegrenzung gilt nicht für Inhaltskarten.
{% endalert %}

##### Geplante Lieferung

Für Content-Card-Kampagnen mit geplanter Zustellung können Sie festlegen, wann Braze die Eignung der Zielgruppe und die Personalisierung für neue Content-Card-Kampagnen bewertet, indem Sie angeben, wann die Karte erstellt wird. Mehr dazu erfahren Sie unter [Kartenerstellung]({{site.baseurl}}/card_creation).

#### Wählen Sie Benutzer als Zielgruppe aus

Als nächstes können Sie [Nutzer:innen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) durch Segmente oder Filter zusammenstellen, um Ihre Zielgruppe einzugrenzen. Sie erhalten automatisch eine Vorschau darauf, wie die ungefähre Anzahl der Segmente im Moment aussieht. Denken Sie daran, dass die genaue Segmentzugehörigkeit immer erst kurz vor dem Versand der Nachricht berechnet wird.

{% multi_lang_include target_audiences.md %}

#### Wählen Sie Konversionsereignisse aus

Mit Braze können Sie nachverfolgen, wie oft Benutzer nach Erhalt einer Kampagne bestimmte Aktionen, d.h. [Conversion Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), durchführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen zuzulassen, in dem eine Konversion gezählt wird, wenn der Nutzer:innen die angegebene Aktion durchführt.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, füllen Sie die restlichen Abschnitte der Canvas-Komponente aus. Weitere Einzelheiten zum Aufbau des restlichen Canvas, zur Implementierung von [multivariaten Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) und [intelligenter Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) und mehr finden Sie im Schritt [Aufbau Ihres Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) in unserer Canvas-Dokumentation.

{% endtab %}
{% endtabs %}

## Schritt 6: Überprüfen und einsetzen

Nachdem Sie den letzten Teil Ihrer Kampagne oder Ihres Canvas erstellt haben, überprüfen Sie die Details, [testen Sie sie]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/testing/) und senden Sie sie, wenn Sie bereit sind.

{% alert warning %}
Nachdem eine Content-Card gestartet wurde, kann sie nicht mehr bearbeitet werden. Sie können nur den Versand an neue Nutzer unterbinden und sie aus den Feeds der Nutzer entfernen. Lesen Sie den Abschnitt [Aktualisierung der gesendeten Karten]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-launched-cards), um zu verstehen, wie Sie dieses Szenario angehen können.
{% endalert %}

Sehen Sie sich als nächstes die [Content Card-Berichterstattung]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/) an, um zu erfahren, wie Sie auf die Ergebnisse Ihrer Content Card-Kampagnen zugreifen können.

## Was Sie wissen sollten

### Größenbeschränkungen für Content-Cards

Die Größe einer Content-Card-Nutzlast kann nach dem Liquid-Rendering bis zu 2 KB betragen. Dazu gehören der **Titel**, die **Nachricht**, die **Bild-URL**, der **Linktext**, die **Link-URL(s)** und die **Schlüssel-Wert-Paare** (Namen und Werte). Dieses Limit bezieht sich jedoch nicht auf die Größe des Bildes, sondern nur auf die Länge der Bild-URL.

{% alert important %}
Nachrichten, die größer als 2 KB sind, werden nicht gesendet. Während der Testsendungen können Content-Cards, die größer als 2 KB sind, noch zugestellt und korrekt angezeigt werden.
{% endalert %}

### Anzahl der Karten im Feed

Alle Nutzer:innen können bis zu 250 nicht abgelaufene Content-Cards gleichzeitig in ihrem Feed haben. Wenn dieses Limit überschritten wird, gibt Braze die ältesten Karten nicht mehr zurück, auch wenn sie ungelesen sind. Abgeworfene Karten zählen ebenfalls zu diesem Limit, d.h. eine hohe Anzahl an abgeworfenen Karten kann den Platz für neue Karten verringern.

### Verhalten beim Senden

Nachdem die Content Cards versendet wurden, warten sie in einem "Posteingang" darauf, dem Benutzer zugestellt zu werden (ähnlich wie bei E-Mails). Nachdem Inhalte in die Content-Card gezogen wurden (zum Zeitpunkt der Anzeige), können sie während ihrer Lebensdauer nicht mehr geändert werden. Das gilt auch, wenn Sie eine API über Connected-Content aufrufen und sich die Daten des Endpunkts ändern. Diese Daten werden nicht mehr aktualisiert. Sie können nur den Versand an neue Nutzer unterbinden und sie aus den Feeds der Nutzer entfernen. Wenn Sie eine Kampagne ändern, werden nur zukünftige Karten, die verschickt werden, aktualisiert.

Wenn Sie alte Karten entfernen möchten, müssen Sie zunächst die Kampagne beenden. Um eine Kampagne zu beenden, öffnen Sie Ihre Content-Card-Kampagne und wählen Sie **Kampagne beenden** aus. Wenn Sie die Kampagne stoppen, müssen Sie entscheiden, wie Sie mit Nutzer:innen umgehen, die Ihre Karte bereits erhalten haben. 

Wenn Sie die Content Card aus den Feeds Ihrer Benutzer entfernen möchten, wählen Sie **Karte aus Feed entfernen**. Die Karte wird dann bei der nächsten Synchronisierung vom SDK versteckt.

![Dialog zum Bestätigen der Deaktivierung von Content-Cards]({% image_buster /assets/img/cc_remove.png %}){: style="max-width:75%" }

{% alert tip %}
Möchten Sie, dass Ihre Inhalte länger als 30 Tage verfügbar sind? Versuchen Sie es mit [Bannern]({{site.baseurl}}/user_guide/message_building_by_channel/banners).
{% endalert %}

### Events zum Entfernen von Karten {#action-based-card-removal}

Einige Content-Cards sind nur relevant, bis ein Nutzer:innen eine Aktion ausführt. Eine Karte, die Nutzer:innen auffordert, ihr Konto zu aktivieren, sollte zum Beispiel nicht mehr angezeigt werden, nachdem der Nutzer:in diese Onboarding-Aufgabe eingestiegen ist.

Innerhalb einer Kampagne oder einer Canvas-Nachricht können Sie optional ein **Removal Event** hinzufügen, um festzulegen, welche angepassten Events oder Käufe dazu führen sollen, dass zuvor gesendete Karten aus dem Feed des Benutzers entfernt werden, ausgelöst durch das SDK oder die REST API.

Die Karten werden bei nachfolgenden Aktualisierungen entfernt, nachdem Braze das angegebene Ereignis verarbeitet hat.

{% alert tip %}
Sie können mehrere benutzerdefinierte Ereignisse und Käufe angeben, die eine Karte aus dem Feed eines Benutzers entfernen sollen. Wenn der Benutzer **eine** dieser Aktionen durchführt, werden alle vorhandenen Karten, die von den Karten der Kampagne gesendet wurden, entfernt. Alle zukünftigen Karten, die in Frage kommen, werden weiterhin gemäß dem Zeitplan der Nachricht verschickt.
{% endalert %}

![Content-Card-Entfernungsbedingungen Panel mit der Option Content-Card-Entfernungsereignis.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

### Aktualisieren der gestarteten Karten

Inhaltskarten können nach dem Versenden nicht mehr bearbeitet werden. Wenn Sie feststellen, dass Sie Änderungen an bereits versendeten Karten vornehmen müssen, sollten Sie die [Wiederzulassung von Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/) in Betracht ziehen, wie in den folgenden Optionen beschrieben.

{% alert note %}
Wenn eine Content-Card wieder zugelassen wird, kann sie erneut gesendet werden, wenn sich die ursprüngliche Karte noch in der App eines Nutzers:innen befindet. Um doppelte Karten in der App eines Nutzers zu vermeiden, können Sie die Wiederzulassung deaktivieren oder das Wiederzulassungsfenster verlängern, so dass Nutzer:innen erst dann eine neue Karte erhalten, wenn die ursprüngliche abgelaufen ist.
{% endalert %}

Beachten Sie auch, dass Content-Cards, die [bei der ersten Impression]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) verwendet werden, die Impressionszeit zur Berechnung der Wiederzulässigkeit verwenden. Content-Cards, die beim Start einer Kampagne oder beim Eingang in den Canvas-Schritt erstellt werden, verwenden jedoch den spätesten Sende- oder Impressionszeitpunkt.

#### Option 1: Duplizieren der Kampagne

Eine Möglichkeit besteht darin, die Kampagne zu archivieren und aktive Karten aus dem Feed zu entfernen. Dann können Sie die Kampagne duplizieren und mit Updates starten, damit alle berechtigten Nutzer:innen die aktualisierten Karten erhalten.

* Wenn Benutzer nie wieder für eine Content Card in Frage kommen sollen, können Sie nach Benutzern filtern, die die vorherige Version der Content Card nicht erhalten haben, indem Sie den Filter `Received Message from Campaign` auf die Bedingung `Has Not` setzen.
* Wenn Benutzer, die die vorherige Karte erhalten haben, in X Tagen wieder berechtigt sein sollten, können Sie den Filter für `Last Received Message from specific campaign` auf vor mehr als X Tagen **ODER** `Received Message from Campaign` mit der Bedingung `Has Not` setzen.

##### Anwendungsfall

Nehmen wir an, Sie haben eine Kampagne so eingestellt, dass sie durch den Beginn einer Sitzung getriggert wird, und die Wiederzulässigkeit ist auf 30 Tage eingestellt. Ein Benutzer hat die Kampagne vor zwei Tagen erhalten, und Sie möchten die Kopie ändern. Zunächst würden Sie die Kampagne archivieren und die Karten aus dem Feed entfernen. Zweitens würden Sie die Kampagne duplizieren und mit der neuen Kopie neu starten. Wenn der oder die Nutzer:in eine weitere Sitzung hat, erhält er oder sie sofort die neue Karte.

##### Impact

* **Berichterstattung:** Jede Version der Karte würde eine eigene Analyse haben.
* **Bestehende Empfänger:** Neue und bestehende Empfänger sehen die aktualisierte Karte bei der nächsten Aktualisierung des Feeds, wenn sie dazu berechtigt sind.

{% alert tip %}
Wir empfehlen diese Option für Nachrichten, in denen Sie den neuesten Inhalt der Karte anzeigen (z. B. Homepage-Banner), Änderungen sofort angezeigt werden müssen oder wenn die Wiederzulassung deaktiviert ist.
{% endalert %}

#### Option 2: Anhalten und neu starten

Wenn für eine Karte die Wiederzulassung aktiviert ist, können Sie das tun:

1. Stoppen Sie Ihre Kampagne.
2. Entfernen Sie aktive Content Cards aus den Feeds der Benutzer.
3. Bearbeiten Sie Ihre Kampagne nach Bedarf.
4. Starten Sie Ihre Kampagne neu.

Bei diesem Ansatz erhalten neu berechtigte Nutzer:innen die neue Karte, und bisherige Empfänger:innen erhalten die neue Karte, wenn sie wieder berechtigt sind.

##### Anwendungsfall

Nehmen wir an, Sie haben eine Kampagne, die durch den Beginn einer Sitzung ausgelöst wird und deren Wiederzulässigkeit auf 30 Tage eingestellt ist. Ein Benutzer hat die Kampagne vor zwei Tagen erhalten, und Sie möchten die Kopie ändern. Beenden Sie zunächst die Kampagne und entfernen Sie die Karte aus dem Feed. Zweitens: Veröffentlichen Sie die Kampagne mit dem neuen Text erneut. Wenn der oder die Nutzer:in eine weitere Sitzung hat, erhält er oder sie die neue Karte in 28 Tagen.

##### Impact

* **Berichterstattung:** Eine Kampagne enthält alle Reporting Analytics für die gestarteten Kartenversionen. Braze unterscheidet nicht zwischen den eingeführten Versionen.
* **Bestehende Empfänger:** Benutzer, die die Karte bereits erhalten haben, würden die aktualisierten Karten erst dann erhalten, wenn sie wieder förderfähig werden. Wenn die erneute Qualifizierung deaktiviert ist, würden sie die neue Karte nie erhalten.

{% alert tip %}
Wir empfehlen diese Option für eindeutige Nachrichten in einer Mitteilungszentrale oder im Posteingang (z.B. Aktionen), wenn es wichtig ist, dass die Analytics einheitlich sind, oder wenn die Aktualität der Nachricht keine Rolle spielt (z.B. wenn bestehende Empfänger:innen auf das Berechtigungsfenster warten können, bevor sie die aktualisierten Karten sehen).
{% endalert %}

#### Aufbewahren der Karten in den Nutzer-Feeds

Wenn Sie möchten, können Sie eine aktive Content-Card-Kampagne in den Feeds der Nutzer:innen beibehalten und sie nicht entfernen. Wenn die Live-Kampagne bearbeitet wird, ist die vorherige, unbearbeitete Version der Kampagnenkarte immer noch live, und nur Nutzer:innen, die die Kriterien nach den Bearbeitungen erfüllen, sehen die neue Version. Benutzer, die bereits mit der Kampagne in Berührung gekommen sind, sehen jedoch möglicherweise zwei Versionen der Karte.

