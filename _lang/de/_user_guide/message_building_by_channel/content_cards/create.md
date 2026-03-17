---
nav_title: Eine Inhaltskarte erstellen
article_title: Eine Inhaltskarte erstellen
page_order: 0
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Content-Cards mit Kampagnen und Canvase von Braze erstellen, zusammenstellen, konfigurieren und versenden."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Eine Inhaltskarte erstellen

> Dieser Artikel beschreibt, wie Sie eine Content-Card in Braze erstellen, wenn Sie Kampagnen und Canvase erstellen. Hier führen wir Sie durch die Auswahl eines Nachrichtentyps, das Verfassen Ihrer Karte und die Planung der Zustellung Ihrer Nachricht.

## Schritt 1: Wählen Sie, wo Sie Ihre Botschaft aufbauen möchten

Verwenden Sie Kampagnen für einzelne, einfache Nachrichten (z. B. um Nutzer:innen mit einer Nachricht über ein Produkt zu informieren). Verwenden Sie Canvases für mehrstufige User Journeys (z. B. zum Versenden maßgeschneiderter Produktvorschläge auf Grundlage des Nutzerverhaltens im Zeitverlauf).

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
|[Klassisch]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| ![Eine klassische Content-Card mit einem kleinen Symbol und Text, um zur Buchung eines Fitnesskurses anzuregen.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |Die Classic Card verfügt über ein übersichtliches Layout mit einem fettgedruckten Titel, einem Text mit der Nachricht und einem optionalen Bild, das links neben dem Titel und dem Text platziert werden kann. Für die Classic Card verwenden Sie am besten ein quadratisches Bild oder Symbol. |
|[Bild mit Bildunterschrift]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| ![Eine hervorgehobene Content-Card mit dem Bild eines Gewichthebers und einem Text, der zur Buchung eines Trainingskurses animiert.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | Die hervorgehobene Image-Card präsentiert Ihren Inhalt mit Text und einem aufmerksamkeitsstarken Bild. |
|[Nur Bild]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| ![Eine Bild-only-Content-Card, die ausschließlich Text enthält.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | Die Karte mit reinem Bildinhalt bietet Platz für Bilder, GIFs und andere kreative Nicht-Text-Inhalte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Schritt 3: Content-Card zusammenstellen

Auf der Registerkarte **Verfassen** des Nachrichteneditors können Sie alle Aspekte des Inhalts und Verhaltens Ihrer Nachricht bearbeiten.

![Details der Beispiel-Inhaltskarte auf der Registerkarte Verfassen des Nachrichteneditors.]({% image_buster /assets/img/content_card_compose.png %})

Der Inhalt variiert je nach dem im vorherigen Schritt gewählten **Kartentyp**, kann aber eine der folgenden Optionen enthalten:

#### Sprache

Wählen Sie **Sprachen hinzufügen**, um die gewünschten Sprachen aus der vorgegebenen Liste hinzuzufügen. Dadurch wird [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) in Ihre Nachricht eingefügt. Wählen Sie die Sprachen am besten aus, bevor Sie den Content verfassen, damit Sie den Text dort einfügen können, wo er im Liquid hingehört. Eine vollständige Liste der Sprachen, die Sie verwenden können, finden Sie unter [Unterstützte Sprachen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

![Ein Fenster mit den ausgewählten Sprachen Englisch, Spanisch und Französisch sowie Titel, Beschreibung und Linktext, die für die Internationalisierung der Felder ausgewählt wurden.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

##### Erstellen von Nachrichten von rechts nach links

Wie Nachrichten von rechts nach links letztendlich aussehen, hängt weitgehend davon ab, wie die Diensteanbieter sie darstellen. Bewährte Methoden zur Erstellung von Nachrichten, die so genau wie möglich angezeigt werden, finden Sie unter [Erstellen von Nachrichten von]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) rechts nach links.

#### Titel und Nachricht

Werden Sie kreativ. Es gibt keine Grenzen, aber je schneller Sie Ihre Botschaft übermitteln und Ihren Kunden zum Klicken bringen können, desto besser! Wir empfehlen klare und prägnante Titel und Nachrichteninhalte. Beachten Sie, dass diese Felder bei Nur-Bild-Karten nicht vorhanden sind.

#### Bild

Fügen Sie ein Bild zu Ihrer Inhaltskarte hinzu, indem Sie **Bild hinzufügen** wählen oder eine Bild-URL angeben. Wenn Sie **Bild hinzufügen** wählen, öffnet sich die **Mediathek**, in der Sie ein zuvor hochgeladenes Bild auswählen oder ein neues Bild hinzufügen können. Für jede Art von Nachricht und jede Plattform können eigene Proportionen und Anforderungen gelten. Informieren Sie sich daher unbedingt darüber, bevor Sie einen Auftrag erteilen oder ein Bild von Grund auf neu erstellen! Denken Sie daran, dass die Nachrichtenfelder der Content-Cards auf eine Gesamtgröße von 2 KB begrenzt sind.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Oben pinnen

Braze zeigt oben im Feed einer Nutzer:in eine gepinnte Karte an, die die Nutzer:in nicht ausblenden kann. Wenn der Feed eines Nutzers:in mehrere gepinnte Karten enthält, ordnet Braze diese in chronologischer Reihenfolge an. Nachdem Sie eine Karte gesendet haben, können Sie das Update für die Option „Angeheftet“ nicht mehr nachträglich durchführen. Wenn Sie diese Option nach dem Versand einer Kampagne ändern, wirkt sich dies nur auf zukünftige Sendungen aus.

![Side-by-Side-Vorschau der Content-Cards in Braze für Mobilgeräte und Web mit aktivierter Option „Diese Karte oben im Feed pinnen“.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

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

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

##### Geplante Lieferung

Für Content-Card-Kampagnen mit geplanter Zustellung können Sie festlegen, wann Braze die Eignung der Zielgruppe und die Personalisierung für neue Content-Card-Kampagnen bewertet, indem Sie angeben, wann die Karte erstellt wird. Mehr dazu erfahren Sie unter [Kartenerstellung]({{site.baseurl}}/card_creation).

#### Zielgruppe auswählen

Anschließend [können Sie]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) Ihre Zielgruppe durch die Auswahl von Segmenten oder Filtern eingrenzen. Sie erhalten automatisch eine Vorschau, wie die ungefähre Segmentpopulation aussieht. Bitte beachten Sie, dass die genaue Segmentzugehörigkeit immer vor dem Versand der Nachricht berechnet wird.

{% multi_lang_include target_audiences.md %}

#### Wählen Sie Konversionsereignisse aus

Mit Braze können Sie nachverfolgen, wie oft Benutzer nach Erhalt einer Kampagne bestimmte Aktionen, d.h. [Conversion Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), durchführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen zuzulassen, in dem eine Konversion gezählt wird, wenn der Nutzer:innen die angegebene Aktion durchführt.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, füllen Sie die restlichen Abschnitte der Canvas-Komponente aus. Weitere Einzelheiten zum Aufbau des restlichen Canvas, zur Implementierung von [multivariaten Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) und [intelligenter Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) und mehr finden Sie im Schritt [Aufbau Ihres Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) in unserer Canvas-Dokumentation.

{% endtab %}
{% endtabs %}

## Schritt 6: Überprüfen und einsetzen

Nachdem Sie den letzten Teil Ihrer Kampagne oder Ihres Canvas erstellt haben, überprüfen Sie die Details, [testen Sie sie]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) und senden Sie sie, wenn Sie bereit sind.

{% alert warning %}
Nachdem eine Content-Card gestartet wurde, kann sie nicht mehr bearbeitet werden. Sie können nur den Versand an neue Nutzer unterbinden und sie aus den Feeds der Nutzer entfernen. Lesen Sie den Abschnitt [Aktualisierung der gesendeten Karten]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-launched-cards), um zu verstehen, wie Sie dieses Szenario angehen können.
{% endalert %}

Sehen Sie sich als nächstes die [Content Card-Berichterstattung]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/) an, um zu erfahren, wie Sie auf die Ergebnisse Ihrer Content Card-Kampagnen zugreifen können.

## Was Sie wissen sollten

### Nutzlast- und Zufuhrbeschränkungen

Um die Performance zu unterstützen, gelten für Content-Cards zwei wesentliche Einschränkungen: eine Begrenzung der Nutzlastgröße für jede Karte und eine maximale Anzahl von Karten, die in einem Feed angezeigt werden können.

#### Größenbeschränkungen für Content-Cards

Die gesamte Datenlast für eine einzelne Content-Card darf **nach** der Darstellung einer Liquid-Personalisierung 2 KB nicht überschreiten. Dies beinhaltet:

* Titel
* Nachricht
* Bild-URL (die Länge des URL-Strings selbst, nicht die Größe der Bilddatei)
* Link-Text
* Link-URLs für alle angegebenen Plattformen (separate URLs für iOS, Android und Internet werden alle zur Gesamtzahl hinzugerechnet)
* Schlüssel-Wert-Paare (sowohl die Schlüsselnamen als auch ihre Werte)

Die Verwendung von Liquid zum Einfügen langer Strings von Text (z. B. aus benutzerdefinierten Attributen) kann dazu führen, dass Sie das Limit überschreiten. 

Der Kampagnenkomponist zeigt eine Warnung an, wenn Ihr statischer Inhalt das Limit überschreitet. (Wir geben keine Größenangaben für dynamischen Content unter Verwendung von Liquid.) **Wenn die Größe der Nachrichten 2 KB überschreitet, wird der Versand abgebrochen.** Sie können diese Abbruchvorgänge im Protokoll der Nachrichtenaktivität mit der entsprechenden Begründung einsehen`Content card maximum size exceeded`.

{% alert important %}
Während Testversendungen können Content-Cards, die größer als 2 KB sind, weiterhin ordnungsgemäß zugestellt und angezeigt werden.
{% endalert %}

Im Folgenden finden Sie einige bewährte Verfahren für die Verwaltung der Nutzlastgröße von Content-Cards:

* Verwenden Sie URL-Kürzer für lange Links. URLs, insbesondere solche mit umfangreichen Tracking-Parametern, können Probleme mit Größenbeschränkungen verursachen. Die Verwendung eines URL-Kürzungsdienstes kann die Zeichenanzahl erheblich reduzieren und Speicherplatz in der Nutzlast freigeben.
* Kürzen Sie dynamischen Content mit Liquid. Bei der Personalisierung von Karten mit dynamischem Text aus Benutzerattributen oder API-Aufrufen kann die Länge des Inhalts unvorhersehbar sein. Bitte setzen Sie Liquid-Filter wie  proaktiv ein, um die Länge`truncate` von dynamischem Text zu begrenzen.
* Seien Sie effizient mit plattformübergreifenden URLs. Die 2-KB-Beschränkung umfasst die URLs für alle von Ihnen definierten Plattformen. Die Verwendung langer, eindeutiger URLs für jede Plattform kann die Größe der Nutzlast vervielfachen. Bitte verwenden Sie nach Möglichkeit einen einzigen Link, der auf allen Plattformen funktioniert, oder nutzen Sie bei Bedarf URL-Kürzer.
* Bitte erwägen Sie die Verwendung von Bannern für reichhaltigere Inhalte. Für Anwendungsfälle, die durchgehend große Mengen an Inhalten erfordern, sind Content-Cards möglicherweise nicht der geeignete Kanal. Banner unterliegen nicht derselben Beschränkung auf 2 KB Nutzlast und eignen sich besser für die Einbettung umfangreicherer Inhalte direkt in ein App-Erlebnis oder eine Website.

#### Anzahl der Karten im Feed

Alle Nutzer:innen können bis zu 250 nicht abgelaufene Content-Cards gleichzeitig in ihrem Feed haben. Wenn dieses Limit überschritten wird, gibt Braze die ältesten Karten nicht mehr zurück, auch wenn sie ungelesen sind. Abgelehnte Karten werden ebenfalls auf dieses Limit angerechnet, was bedeutet, dass eine hohe Anzahl abgelehnter Karten den verfügbaren Platz für ältere Karten verringern kann.

Um Probleme mit dem Kartenlimit zu vermeiden, empfehlen wir die folgenden bewährten Verfahren:

- **Verwenden Sie kürzere Verfallsdaten:** Für zeitkritische Kampagnen (z. B. Wochenendverkäufe) legen Sie bitte ein bestimmtes Ablaufdatum fest. Auf diese Weise werden Karten automatisch aus dem Feed entfernt und zählen nicht mehr zum Limit, sobald sie nicht mehr relevant sind.
- **Nutzen Sie die aktionsbasierte Entfernung:** Richten Sie Entfernungsereignisse für transaktions- oder zielbasierte Karten ein. Beispielsweise sollte eine Karte, die eine Nutzer:in dazu auffordert, ihr Profil zu vervollständigen, entfernt werden, sobald ein`profile_completed`Ereignis protokolliert wurde.
- **Überprüfen Sie lang laufende Kampagnen:** Überprüfen Sie wiederkehrende oder laufende Kampagnen, um sicherzustellen, dass sie Ihren Nutzer:innen keine schlechte Erfahrung bieten, indem sie den Feed im Laufe der Zeit mit zu vielen Karten überladen.

### Wiederzulassungsvoraussetzungen für Content-Cards

Die Wiederzulässigkeit bestimmt, ob und wann ein Nutzer:in eine Nachricht aus derselben Kampagne mehr als einmal erhalten kann. Bei Content-Cards ist es von entscheidender Bedeutung, die Funktionsweise zu verstehen, um wiederkehrende Kampagnen zu verwalten und sicherzustellen, dass Nutzer:innen keine doppelten oder veralteten Nachrichten erhalten.

{% alert tip %}
Möchten Sie, dass Ihre Inhalte länger als 30 Tage verfügbar sind? Bitte versuchen Sie es [mit Bannern]({{site.baseurl}}/user_guide/message_building_by_channel/banners).
{% endalert %}

#### Wie die Wiederwählbarkeit berechnet wird

Wenn Sie die Wiederberechtigung aktivieren, beginnt der Countdown für die „Wiederaufnahme“ eines Nutzers in eine Kampagne, nachdem ihm die Nachricht gesendet wurde. Der genaue Zeitpunkt, zu dem dieser Countdown beginnt, hängt von Ihren Einstellungen bei der Kartenerstellung ab:

* Content-Cards, die [den ersten Eindruck]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) verwenden, nutzen die Impression-Zeit, um die erneute Berechtigung zu berechnen.
* Content-Cards, die beim Start einer Kampagne oder beim Aufrufen eines Canvas-Schritts erstellt werden, verwenden den spätesten Versand- oder Zeitpunkt für Impressionen.

#### Die 30-tägige Gültigkeitsdauer und erneute Berechtigung

Eine häufige Quelle für Verwirrung ist die Wechselwirkung zwischen der erneuten Wahlberechtigung für Kampagnen und dem automatischen Ablauf aller Content-Cards nach 30 Tagen. 

Alle Content-Cards werden 30 Tage nach dem Versand oder Entfernen automatisch aus den Systemen von Braze gelöscht. Wenn Sie eine langfristig laufende, wiederkehrende Kampagne mit deaktivierter Wiederberechtigung haben, kann es vorkommen, dass eine Nutzer:in nach 30 Tagen erneut dieselbe Karte erhält. Wenn die ursprüngliche Karte gelöscht wird, erkennt das System keinen Nachweis mehr darüber, dass diese Nutzer:in die Kampagne erhalten hat, sodass sie bei ihrer nächsten Sitzung erneut teilnahmeberechtigt ist. 

Damit Nutzer:innen eine Nachricht aus einer bestimmten Kampagne nur einmal erhalten, fügen Sie Ihrer Kampagne oder Ihrem Canvas-Schritt einen Zielgruppen-Filter für Nutzer:innen hinzu, die noch keine Nachricht aus dieser Kampagne erhalten haben. Dieser Filter stellt die zuverlässigste Methode dar, um doppelte Sendungen bei lang andauernden Kampagnen zu verhindern.

### Verwaltung von Live-Content-Cards

Nachdem die Content Cards versendet wurden, warten sie in einem "Posteingang" darauf, dem Benutzer zugestellt zu werden (ähnlich wie bei E-Mails). Nachdem Inhalte in die Content-Card gezogen wurden (zum Zeitpunkt der Anzeige), können sie während ihrer Lebensdauer nicht mehr geändert werden. Das gilt auch, wenn Sie eine API über Connected-Content aufrufen und sich die Daten des Endpunkts ändern. Diese Daten werden nicht mehr aktualisiert. Sie können nur den Versand an neue Nutzer unterbinden und sie aus den Feeds der Nutzer entfernen. Wenn Sie eine Kampagne ändern, werden nur zukünftige Karten, die verschickt werden, aktualisiert.

#### Aktualisieren der gestarteten Karten

Um eine Karte für Nutzer:innen zu ändern, die diese bereits erhalten haben, müssen Sie eine der folgenden Methoden anwenden:

##### Option 1: Duplizieren Sie die Kampagne (empfohlen für sofortige Änderungen).

{% alert tip %}
Wir empfehlen diese Option für Nachrichten, bei denen Sie die neuesten Inhalte in der Content-Card anzeigen, Änderungen sofort angezeigt werden müssen oder wenn die erneute Berechtigung deaktiviert ist.
{% endalert %}

Der erste Ansatz besteht darin, die Kampagne zu archivieren und eine neue, duplizierte Kampagne zu starten:

1. Beenden Sie die ursprüngliche Kampagne und wählen Sie bei der entsprechenden Aufforderung die Option aus`Remove card after the next sync`.
2. Bitte duplizieren Sie die Kampagne, nehmen Sie Ihre Änderungen vor und starten Sie die neue Version.

Wenn Sie die Kampagne duplizieren, müssen Sie die Zielgruppe für die neue Version definieren. Verwenden Sie Filter für die Segmentierung, um zu steuern, wer die aktualisierte Karte erhält:
* Wenn Benutzer nie wieder für eine Content Card in Frage kommen sollen, können Sie nach Benutzern filtern, die die vorherige Version der Content Card nicht erhalten haben, indem Sie den Filter `Received Message from Campaign` auf die Bedingung `Has Not` setzen.
* Wenn Benutzer, die die vorherige Karte erhalten haben, in X Tagen wieder berechtigt sein sollten, können Sie den Filter für `Last Received Message from specific campaign` auf vor mehr als X Tagen **ODER** `Received Message from Campaign` mit der Bedingung `Has Not` setzen.

###### Impact

* **Bestehende Empfänger:** Neue und bestehende Empfänger sehen die aktualisierte Karte bei der nächsten Aktualisierung des Feeds, wenn sie dazu berechtigt sind.
* **Berichterstattung:** Jede Version der Karte würde eine eigene Analyse haben.

Nehmen wir an, Sie haben eine Kampagne so eingestellt, dass sie durch den Beginn einer Sitzung getriggert wird, und die Wiederzulässigkeit ist auf 30 Tage eingestellt. Ein Benutzer hat die Kampagne vor zwei Tagen erhalten, und Sie möchten die Kopie ändern. Zunächst würden Sie die Kampagne archivieren und die Karten aus dem Feed entfernen. Zweitens würden Sie die Kampagne duplizieren und mit der neuen Kopie neu starten. Wenn der oder die Nutzer:in eine weitere Sitzung hat, erhält er oder sie sofort die neue Karte.

##### Option 2: Die gleiche Kampagne beenden und erneut starten

{% alert tip %}
Wir empfehlen diese Option für eindeutige Nachrichten in einer Mitteilungszentrale oder im Posteingang (z.B. Aktionen), wenn es wichtig ist, dass die Analytics einheitlich sind, oder wenn die Aktualität der Nachricht keine Rolle spielt (z.B. wenn bestehende Empfänger:innen auf das Berechtigungsfenster warten können, bevor sie die aktualisierten Karten sehen).
{% endalert %}

Dieser Ansatz vereint alle Ihre Analytics in einer einzigen Kampagne. Neu berechtigte Nutzer:innen erhalten die neue Karte, jedoch verzögert sich das Update für bestehende Empfänger:innen, bis sie erneut berechtigt sind:

1. Beenden Sie Ihre Kampagne und wählen Sie nach Aufforderung **die Option „Karte nach der nächsten Synchronisierung entfernen**“.
2. Bearbeiten Sie Ihre Kampagne nach Bedarf.
3. Starten Sie Ihre Kampagne neu.

###### Impact

* **Bestehende Empfänger:** Benutzer, die die Karte bereits erhalten haben, würden die aktualisierten Karten erst dann erhalten, wenn sie wieder förderfähig werden. Wenn die erneute Qualifizierung deaktiviert ist, würden sie die neue Karte nie erhalten.
* **Berichterstattung:** Eine Kampagne enthält alle Reporting Analytics für die gestarteten Kartenversionen. Braze unterscheidet nicht zwischen den eingeführten Versionen.

Nehmen wir an, Sie haben eine Kampagne, die durch den Beginn einer Sitzung ausgelöst wird und deren Wiederzulässigkeit auf 30 Tage eingestellt ist. Ein Benutzer hat die Kampagne vor zwei Tagen erhalten, und Sie möchten die Kopie ändern. Beenden Sie zunächst die Kampagne und entfernen Sie die Karte aus dem Feed. Zweitens: Veröffentlichen Sie die Kampagne mit dem neuen Text erneut. Wenn der oder die Nutzer:in eine weitere Sitzung hat, erhält er oder sie die neue Karte in 28 Tagen.

#### Karten entfernen und ablaufen lassen

##### Manuelles Entfernen der Karte

Sie können Karten für die Feeds aller Nutzer:innen jederzeit manuell entfernen, indem Sie die Kampagne beenden.

1. Öffnen Sie die Content-Card-Kampagne und wählen Sie „Kampagne beenden“.
2. Wenn Sie dazu aufgefordert werden, wählen Sie **„Karte nach der nächsten Synchronisierung auswählen**“. Die Karte wird bei der nächsten Aktualisierung des Feeds entfernt.

##### Automatisiertes Entfernen von Karten {#action-based-card-removal}

Sie können eine Karte automatisch entfernen, wenn ein Nutzer:in eine bestimmte Aktion ausführt, beispielsweise einen Kauf abschließt oder ein Feature aktiviert.

Bitte geben Sie in Ihrer Kampagne oder Ihrem Canvas-Schritt ein Entfernungsereignis an. Wenn ein Nutzer:in dieses Ereignis ausführt, wird die Karte nach der Verarbeitung des Ereignisses durch Braze bei der nächsten Aktualisierung aus seinem Feed entfernt. 

{% alert note %}
Diese Entfernung erfolgt nicht sofort. Es kommt zu einer Bearbeitungsverzögerung, daher kann es einige Minuten dauern und mehr als eine Aktualisierung des Feeds erforderlich sein, bis die Karte nicht mehr angezeigt wird.
{% endalert %}

{% alert tip %}
Sie können mehrere benutzerdefinierte Ereignisse und Käufe angeben, die eine Karte aus dem Feed eines Benutzers entfernen sollen. Wenn der Benutzer **eine** dieser Aktionen durchführt, werden alle vorhandenen Karten, die von den Karten der Kampagne gesendet wurden, entfernt. Alle zukünftigen Karten, die in Frage kommen, werden weiterhin gemäß dem Zeitplan der Nachricht verschickt.
{% endalert %}

![Panel „Bedingungen für das Entfernen von Content-Cards“ mit der Option „Ereignis zum Entfernen von Content-Cards“.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Ablauf der Karte

Content-Cards bleiben ab dem Zeitpunkt ihrer Versendung bis zu 30 Tage lang verfügbar. Nach Ablauf dieser Frist entfernt Braze sie aus den Feeds der Nutzer:innen und löscht sie aus den Systemen von Braze.

#### Karten länger als 30 Tage gültig machen

{% alert tip %}
Für Anwendungsfälle, in denen Nachrichten länger als die 30-tägige Begrenzung für Content-Cards bestehen bleiben müssen, empfehlen wir die Verwendung von Bannern. Banner sind auf Dauerhaftigkeit ausgelegt und haben kein obligatorisches Ablaufdatum, sodass sie so lange sichtbar bleiben können, wie sie benötigt werden.
{% endalert %}

Wenn Sie möchten, dass eine Karte so erscheint, als wäre sie immer verfügbar (i.ed. h. länger als maximal 30 Tage gültig), können Sie eine wiederkehrende Kampagne erstellen, die die Karte alle 30 Tage effektiv ersetzt:

1. Legen Sie die Dauer der Content-Card auf 30 Tage fest.
2. Leggen Sie die erneute Qualifizierung der Kampagne auf 30 Tage fest.
3. Stellen Sie die Kampagne so ein, dass sie bei „Sitzungsbeginn“ getriggert wird.
