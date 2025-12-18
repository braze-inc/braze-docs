---
article_title: FAQ
hidden: true
permalink: /onboarding_faq/
excerpt_separator: ""
page_type: glossary
layout: onboarding_faq
description: "Diese Seite enthält eine Sammlung häufig gestellter Fragen, die nach Kategorien geordnet sind."

---

{% multi_lang_include video.html id="keAZAlBR9zc" source="youtube" %}


<!--- Users --->

{% api %}

### Wie gehe ich mit anonymen Nutzer:innen-Daten um?

{% apitags %}
Nutzer:innen
{% endapitags %}

Wenn ein Nutzerprofil über das SDK erkannt wird, erstellt Braze zunächst ein anonymes Nutzerprofil mit einer `braze_id`: einer eindeutigen Kennung, die von Braze festgelegt wird.

Um den Überblick über anonyme Benutzer zu behalten, können Sie [Benutzer-Aliase]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) einrichten, mit denen Sie anonyme Benutzer mit einer Kennung versehen können. Diese Nutzer:innen können dann über ihre Aliasnamen exportiert oder von der API referenziert werden.

Wenn ein anonymes Benutzerprofil mit einem Alias zu einem späteren Zeitpunkt mit `external_id` erkannt wird, wird es wie ein normales identifiziertes Benutzerprofil behandelt, behält aber seinen bestehenden Alias bei und kann weiterhin über diesen Alias referenziert werden.

Bei Alias-Benutzern, die Sie mit identifizierten Benutzern zusammenführen möchten, können Sie alle Felder zusammenführen, die für das eigentliche Profil, das Sie behalten möchten, relevant sind. Sie müssten diese Daten exportieren, bevor Sie sie mit unserem [Endpunkt Benutzerprofil nach Kennung exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) aus dem Aliasprofil löschen. Sie können dann unseren [Endpunkt Benutzer verfolgen]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) verwenden, um diese Ereignisse in dem von Ihnen geführten Profil zu veröffentlichen. Auf diese Weise bleiben alle Daten erhalten, die Sie beibehalten möchten, z. B. Attribute, die zuvor in einem Profil aufgezeichnet wurden, aber nicht in dem anderen.

Eine vollständige Aufschlüsselung der verschiedenen Methoden zur Erfassung neuer und bestehender Nutzerdaten in Braze finden Sie unter [Best Practices für die Datenerfassung]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/).

{% endapi %}
{% api %}

### Wie kann ich Benutzer importieren, die ich bereits außerhalb von Braze erfasst und identifiziert habe?

{% apitags %}
Nutzer:innen
{% endapitags %}

Um zuvor identifizierte Nutzer:innen zu importieren, können Sie eine CSV-Datei auf Braze hochladen oder Daten über die API senden.

#### CSV

Sie können Benutzerprofile über CSV-Dateien unter **Publikum** > **Benutzer importieren** hochladen und aktualisieren. Wenn Sie Kundendaten importieren, müssen Sie jeweils die eindeutige Kundennummer in Form der `external_id` angeben.

Bevor Sie mit dem CSV-Import beginnen, sollten Sie mit Ihrem Entwicklerteam klären, wie die Nutzer:innen in Braze identifiziert werden sollen. In der Regel handelt es sich dabei um eine intern verwendete Datenbank-ID. Diese sollte mit dem Identifizierungsverfahren der Braze SDK auf Mobilgeräten und im Internet übereinstimmen, sodass das jeweilige Nutzerprofil in Braze auf allen Geräten identisch ist. Erfahren Sie mehr über den [Lebenszyklus]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) des Braze [Benutzerprofils]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/).

Wenn Sie in Ihrem Import einen `external_id` angeben, aktualisiert Braze alle vorhandenen Nutzer:innen mit demselben `external_id` oder erstellt einen neu identifizierten Nutzer:in mit diesem `external_id` Satz, wenn kein solcher gefunden wird.

Weitere Informationen und den Download von CSV-Importvorlagen finden Sie unter [Benutzerimport]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

#### API

Um Nutzer:innen über die API hochzuladen, können Sie unseren [Endpunkt Nutzer:innen verfolgen]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) verwenden, um sie in Braze zu importieren.

Wenn Sie sich nicht sicher sind, ob der Benutzer bereits in Braze existiert, können Sie unseren [Endpunkt Benutzerprofil nach Kennung exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) implementieren, um dies zu überprüfen. Wenn Sie feststellen, dass jemand bereits in Braze vorhanden ist, können Sie dem jeweiligen Braze-Nutzerprofil mit dem Endpunkt `/users/track` nur die neuen Daten hinzufügen.

{% alert note %}
Das sollten Sie bei dem Endpunkt `/users/track` beachten:

- Wenn Sie über diesen Endpunkt Personen nur mit Alias erstellen, müssen Sie das `_update_existing_only` auf "false" setzen.
- Wenn Sie den Abonnementstatus mit diesem Endpunkt aktualisieren, wird sowohl der durch seine externe ID angegebene Benutzer (z. B. User1) als auch der Abonnementstatus aller Benutzer mit der gleichen E-Mail wie dieser Benutzer (User1) aktualisiert.
{% endalert %}

{% endapi %}
{% api %}

### Was ist der Unterschied zwischen den Push-Abonnement-Status?

{% apitags %}
Nutzer:innen
{% endapitags %}

Es gibt drei Optionen für den Status des Push-Abos: abonniert, Opt-in und abgemeldet.

Standardmäßig ist für den Nachrichtenempfang per Push die Abonnentenrolle oder ein Opt-in erforderlich und Push muss aktiviert sein. Sie können diese Einstellung bei Bedarf beim Verfassen einer Nachricht außer Kraft setzen.

|Einwilligungsstatus|Beschreibung|
|---|---|
|Abonniert| Standard-Push-Abonnementstatus, wenn ein Benutzerprofil in Braze erstellt wird. |
|Eingewilligt| Ein Benutzer hat sich ausdrücklich für den Erhalt von Push-Benachrichtigungen entschieden. Braze ändert den Einwilligungsstatus automatisch in `Opted-In`, wenn eine Opt-in-Anfrage auf Ebene des Betriebssystems nutzerseitig angenommen wird.<br><br>Dies gilt nicht für Nutzer:innen mit Android 12 oder darunter.|
|Abgemeldet| Ein Nutzer hat sich über Ihre Anwendung oder andere von Ihrer Marke angebotene Methoden explizit von Push abgemeldet. Standardmäßig stellen die Push Kampagnen von Braze nur Nutzer:innen zusammen, die `Subscribed` oder `Opted-in` für Push sind.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
{% api %}

### Was ist, wenn ich doppelte Benutzer identifiziert habe?

{% apitags %}
Nutzer:innen
{% endapitags %}

Wenn Sie doppelte Nutzer:innen identifiziert haben, müssen Sie diese Nutzerprofile bereinigen. Sie können dies mit den folgenden Schritten tun:

1. Exportieren Sie die Benutzerprofile über unseren `/users/export/ids` Endpunkt.
2. Identifizieren Sie das richtige Nutzerprofil (letztendlich muss Ihr Team über die richtigen Informationen entscheiden) und entweder:
    - Führen Sie alle Felder zusammen, die für das aktuelle Profil relevant sind und die Sie über den Endpunkt `/user/track` beibehalten möchten.
    - Löschen Sie mit dem Endpunkt users/delete das überflüssige Profil, ohne die Daten zusammenzuführen. Wenn Sie ein Nutzerprofil löschen, **gibt es keine Möglichkeit mehr, die Daten zurückzuholen**.

{% alert important %}
Wir empfehlen, dass Sie zunächst die neuen Benutzerprofile mit den richtigen `external_id` und den entsprechenden benutzerdefinierten Attributen und Ereignissen importieren. Nachdem Nutzerprofile gelöscht wurden, können sie nicht wiederhergestellt werden. Das Löschen sollte also der allerletzte Schritt sein.
{% endalert %}

Einige zusätzliche Dinge sind zu beachten:

- Alle Engagement-Daten (wie z.B. erhaltene Kampagnen oder Canvases) auf doppelten Benutzerprofilen gehen verloren. Die einzige Möglichkeit, den historischen Engagement-Kontext beizubehalten, besteht darin, ihn als benutzerdefiniertes Attribut hinzuzufügen (z. B. als benutzerdefiniertes Array-Attribut für alle erhaltenen Kampagnen oder Canvases).
- Bei der Migration von Benutzerprofilen muss Ihr Team auch entscheiden, welches Benutzerprofil der Duplikate beibehalten werden soll. Braze kann nicht entscheiden oder Ihnen eine Liste der zu löschenden Profile zur Verfügung stellen.  
- Letztendlich wird es für Ihr Team wichtig sein, den Registrierungsprozess aus der Sicht der Nutzer:innen zu bewerten und sicherzustellen, dass Sie die Methode `changeUser()` nur dann aufrufen, wenn ein Nutzer:in identifiziert wird.

{% endapi %}
{% api %}

<!-- Segments -->

### Wie erstelle ich ein Segment, wenn ich eine Gruppe von Nutzer:innen über CSV importiere?

{% apitags %}
Segmente
{% endapitags %}

Um Ihre CSV-Datei zu importieren, gehen Sie auf die Seite **Benutzerimport** unter dem Abschnitt Benutzer. In der Tabelle der **letzten Importe** sind bis zu zwanzig Ihrer letzten Importe, deren Dateinamen, die Anzahl der Zeilen in der Datei, die Anzahl der erfolgreich importierten Zeilen, die Gesamtzahl der Zeilen in jeder Datei und der Status jedes Imports aufgeführt.

Der Bereich **CSV importieren** enthält Anweisungen zum Importieren und eine Schaltfläche zum Starten des Imports. Klicken Sie auf **CSV-Datei auswählen** und wählen Sie die gewünschte Datei aus. Bevor Sie dann auf **Import starten** klicken, haben Sie die Möglichkeit, Braze unter "Was sollen wir mit den Benutzern in dieser CSV-Datei tun" mitzuteilen, was mit dieser Liste geschehen soll.

Wählen Sie **Benutzer in dieser CSV importieren und ermöglichen Sie es, diese bestimmte Gruppe von Benutzern als Gruppe erneut anzusprechen**, und wählen Sie dann **Automatisch ein Segment aus den Benutzern erstellen, die aus dieser CSV importiert werden**. Nachdem Sie auf **Import starten** geklickt haben, lädt Braze Ihre Datei hoch, überprüft die Spaltenüberschriften und die Datentypen der einzelnen Spalten und erstellt ein Segment.

Um eine CSV-Vorlage herunterzuladen, siehe [Benutzerimport]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

{% endapi %}
{% api %}

### Welche Arten von Filtern kann ich bei der Erstellung eines Segments verwenden?

{% apitags %}
Segmente
{% endapitags %}

Das Braze SDK bietet Ihnen ein leistungsstarkes Arsenal an Filtern, mit denen Sie Ihre Nutzer:innen auf der Grundlage bestimmter Features und Attribute segmentieren und targetieren können. Sie können das Glossar der [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) verwenden, um diese Filter nach Filterkategorien zu durchsuchen oder einzugrenzen (benutzerdefinierte Daten, Benutzeraktivität, Retargeting, Marketingaktivitäten, Benutzerattribute, Installationsattribution, soziale Aktivitäten, Tests, Sonstige).

{% endapi %}
{% api %}

### Wie richte ich die Standortbestimmung ein, damit ich Nutzer nach ihrem letzten Standort segmentieren und in meinen standortbezogenen Kampagnen und Strategien verwenden kann?

{% apitags %}
Segmente
{% endapitags %}

Navigieren Sie zur Seite **Segmente** unter Engagement, um alle Ihre aktuellen Benutzersegmente anzuzeigen. Auf dieser Seite können Sie neue Segmente erstellen und benennen. Um zu beginnen, klicken Sie auf **Segment erstellen** und geben Sie Ihrem Segment einen Namen.

Sobald Sie Ihr Segment erstellt haben, fügen Sie einen `Most Recent Location` Filter hinzu, um Nutzer:innen nach dem letzten Ort, an dem sie Ihre App genutzt haben, zu targetieren. Sie können Benutzer entweder in einem kreisförmigen Standardbereich markieren oder einen benutzerdefinierten polygonalen Bereich erstellen.

- Bei kreisförmigen Regionen können Sie den Ursprung verschieben und den Positionsradius für Ihre Segmentierung anpassen.
- Bei polygonalen Regionen können Sie genauer festlegen, welche Bereiche in Ihrem Segment enthalten sein sollen.

{% alert tip %}
Sind Sie daran interessiert, die Vorteile des Location Targeting mit Hilfe eines Braze-Partners zu nutzen? Dann schauen Sie sich unsere [Partner für kontextuelle Standortdaten]({{site.baseurl}}/partners/message_personalization/) an.
{% endalert %}

{% endapi %}
{% api %}

### Wie kann ich präzise Listen von Nutzern auf der Grundlage ihres benutzerdefinierten Ereignis- und Kaufverhaltens in den letzten 365 Tagen ansprechen?

{% apitags %}
Segmente
{% endapitags %}

Sie können [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) verwenden! Segment-Erweiterungen ermöglichen es Ihnen, eine präzisere Liste von Nutzer:innen zu targetieren, als dies mit einem regulären Segment möglich wäre.

Sie können bis zu 10 Segmenterweiterungen pro Arbeitsbereich erstellen. Liegen die Erweiterungslisten vor, können sie als Filter in Segmente aufgenommen oder davon ausgeschlossen werden. Bei der Erstellung einer Segmenterweiterung können Sie auch angeben, dass die Liste alle 24 Stunden neu generiert werden soll.

1. Erweitern Sie unter Engagements die **Segmente** und klicken Sie auf **Segmenterweiterung**.
2. Klicken Sie in der Tabelle Segmenterweiterungen auf **\+ Neue Erweiterung erstellen**.
3. Benennen Sie Ihre Segment-Erweiterung, indem Sie die Art der Nutzer:innen beschreiben, nach denen Sie filtern möchten. Dadurch wird sichergestellt, dass die Erweiterung bei der Verwendung als Segmentfilter problemlos und präzise gefunden wird.
4. Wählen Sie zwischen einem Kauf-Event oder einem angepassten Event als Targeting-Kriterium.
5. Wählen Sie aus, welchen gekauften Artikel oder welches angepasste Event Sie für Ihre Nutzer:innen-Liste als Targeting verwenden möchten. 
6. Wählen Sie, wie oft (mehr als, weniger als oder gleich) der Benutzer das Ereignis abgeschlossen haben muss und wie viele Tage er zurückblicken möchte (bis zu 365 Tage).

Um die Zielgenauigkeit zu erhöhen, können Sie die Option **Eigenschaftsfilter hinzufügen** wählen und anhand der spezifischen Eigenschaften Ihres Kaufs oder benutzerdefinierten Ereignisses segmentieren. Braze unterstützt die Segmentierung von Eigenschaften nach String-, Zahlen-, Boole- und Zeitobjekten.

Wir unterstützen auch die Segmentierung auf der Grundlage [verschachtelter Event-Eigenschaften]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

Segmenterweiterungen basieren auf der langfristigen Speicherung von Event-Eigenschaften. Die Speicherung angepasster Event-Eigenschaften ist nicht auf 30 Tage begrenzt. Das bedeutet, dass Sie auf Event-Eigenschaften zurückblicken können, die innerhalb des letzten Jahres getrackt wurden, und dass das Tracking nicht erst wartet, bis die Erweiterung eingerichtet wurde.

{% alert note %}
Die Verwendung von Ereigniseigenschaften innerhalb von Segment Extensions hat keinen Einfluss auf die Verwendung von Datenpunkten.
{% endalert %}

{% endapi %}
{% api %}

#### Segment Extensions auf dem neuesten Stand halten

{% apitags %}
Segmente
{% endapitags %}

Sie können angeben, ob die Erweiterung eine Momentaufnahme anfertigen oder jeden Tag neu generiert werden soll. Ihre Erweiterung wird immer nach dem ersten Speichern mit der Verarbeitung beginnen. Wenn Sie möchten, dass die Erweiterung täglich regeneriert wird, wählen Sie die Option **Erweiterung täglich regenerieren**. Die Regeneration beginnt dann jeden Tag gegen Mitternacht in der Zeitzone Ihres Unternehmens.

Wenn Sie fertig sind, klicken Sie auf **Speichern**. Ihre Verlängerung wird nun bearbeitet. Wie lange es dauert, Ihre Erweiterung zu erstellen, hängt davon ab, wie viele Nutzer:innen Sie haben, wie viele angepasste Events oder Kauf-Events Sie erfassen und wie viele Tage Sie im Verlauf zurückblicken wollen.

Nachdem Sie eine Erweiterung erstellt haben, können Sie sie schließlich als Filter verwenden, wenn Sie ein Segment erstellen oder eine Zielgruppe für eine Kampagne oder ein Canvas definieren. Beginnen Sie mit der Auswahl von `Braze Segment Extension` aus der Filterliste im Abschnitt **Benutzerattribute**. Wählen Sie in der Filterliste Braze-Segmenterweiterung die Erweiterung aus, die Sie in dieses Segment aufnehmen oder ausschließen möchten. Die Erweiterungskriterien finden Sie unter **Erweiterungsdetails anzeigen**. Jetzt können Sie wie gewohnt mit der Erstellung Ihres Segments fortfahren.

{% endapi %}
{% api %}

<!-- Campaigns -->

### Wie erstellt man Multichannel-Kampagnen?

{% apitags %}
Kampagnen
{% endapitags %}

Um eine Multichannel-Kampagne zu erstellen, gehen Sie auf die Seite **Kampagnen**, wählen Sie **Kampagne erstellen** und dann **Multichannel-Kampagne**. Wenn Sie sich in einer Multichannel-Kampagne befinden, wählen Sie auf der Registerkarte Verfassen die Option **Messaging-Kanal hinzufügen**, um die gewünschten Kanäle hinzuzufügen. Klicken Sie auf die eingeblendeten Kanalsymbole, um zwischen den verschiedenen Nachrichtenkomponisten umzuschalten, während Sie Ihre Kampagnentexte für die verschiedenen Kanäle erstellen.

{% endapi %}
{% api %}

### Wie kann ich mit dem Testen und Optimieren von Kampagnen beginnen?

{% apitags %}
Kampagnen
{% endapitags %}

Die Erstellung multivariater Kampagnen und die Durchführung von Canvasen mit mehreren Varianten sind ein guter Ansatzpunkt. Sie können zum Beispiel eine [multivariate Kampagne]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) durchführen, um eine Nachricht mit verschiedenen Kopien oder Betreffzeilen zu testen. Canvase mit mehreren Varianten sind hilfreich, um Workflows zu testen.

{% endapi %}
{% api %}

### Warum gibt es einen Unterschied zwischen der Anzahl der eindeutigen Empfänger und der Anzahl der Sendungen für eine bestimmte Kampagne oder ein bestimmtes Canvas?

{% apitags %}
Kampagnen
{% endapitags %}

Eine mögliche Erklärung für diesen Unterschied könnte darin liegen, dass in der Kampagne oder in Canvas die Wiederwählbarkeit aktiviert ist. Wenn Sie diese Option aktivieren, können Benutzer, die sich für das Segment und die Zustellungseinstellungen qualifizieren, die Nachricht mehr als einmal erhalten. Wenn die Wiederzulassung nicht aktiviert ist, kann die wahrscheinliche Erklärung für den Unterschied zwischen gesendeten und eindeutigen Empfänger:innen darin liegen, dass Nutzer:innen mehrere Geräte über verschiedene Plattformen hinweg mit ihren Profilen verknüpft haben.

Wenn Sie z.B. ein Canvas haben, das sowohl iOS- als auch Web-Push-Benachrichtigungen enthält, könnte ein bestimmter Benutzer mit einem mobilen und einem Desktop-Gerät mehr als eine Nachricht erhalten.

{% endapi %}
{% api %}

### Was bietet die Zustellung in der lokalen Zeitzone?

{% apitags %}
Kampagnen
{% endapitags %}

Die Zustellung nach Ortszeit ermöglicht es Ihnen, Messaging-Kampagnen an ein Segment zu senden, das auf der nutzerspezifischen Zeitzone basiert. Ohne die Zustellung in der lokalen Zeitzone werden die Kampagnen auf der Grundlage der Zeitzoneneinstellungen Ihres Unternehmens in Braze geplant.

Wenn beispielsweise ein in London ansässiges Unternehmen eine Kampagne um 12 Uhr mittags versendet, erreicht sie die Nutzer an der amerikanischen Westküste um 4 Uhr morgens. Wenn Ihre App nur in bestimmten Ländern verfügbar ist, stellt dies möglicherweise kein Risiko für Sie dar. Andernfalls empfehlen wir Ihnen dringend, das Versenden von Push-Benachrichtigungen am frühen Morgen an Ihre Nutzer zu vermeiden!

{% endapi %}
{% api %}

### Wie erkennt Braze die Zeitzone eines Benutzers?

{% apitags %}
Kampagnen
{% endapitags %}

Braze ermittelt automatisch die Zeitzone eines Benutzers anhand seines Geräts. Dies wurde entwickelt, um die Zeitzonengenauigkeit und die vollständige Abdeckung Ihrer Nutzer:innen zu unterstützen. Benutzer, die über die Benutzer-API oder anderweitig ohne Zeitzone erstellt werden, haben die Zeitzone Ihres Unternehmens als Standardzeitzone, bis sie in Ihrer App vom SDK erkannt werden.

Sie können die Zeitzone Ihres Unternehmens in Ihren [Unternehmenseinstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) überprüfen.

{% endapi %}
{% api %}

### Wie plane ich eine Kampagne für eine lokale Zeitzone?

{% apitags %}
Kampagnen
{% endapitags %}

Wenn Sie eine Kampagne planen, müssen Sie auswählen, dass sie zu einer bestimmten Zeit gesendet werden soll, und dann die Option **Kampagne an Benutzer in ihrer lokalen Zeitzone senden** wählen.

Braze empfiehlt ausdrücklich, entsprechende Kampagnen 24 Stunden im Voraus zu planen. Da sie im Laufe eines ganzen Tages versendet werden, können sie 24 Stunden im Voraus geplant werden, damit sie das gesamte Segment erreichen. Sie können diese Kampagnen jedoch bei Bedarf auch weniger als 24 Stunden im Voraus planen. Denken Sie daran, dass Braze keine Nachrichten an Nutzer:innen sendet, die die Sendezeit um mehr als 1 Stunde überschritten haben.

Wenn es beispielsweise 13.00 Uhr ist und Sie eine Kampagne für die Ortszeitzone für 15.00 Uhr planen, dann wird die Kampagne sofort an alle Nutzer:innen gesendet, deren Ortszeit 15.00 Uhr ist, aber nicht an Nutzer:innen, deren Ortszeit 17.00 Uhr ist. Außerdem muss die Sendezeit, die Sie für Ihre Kampagne wählen, in der Zeitzone Ihres Unternehmens noch nicht stattgefunden haben.

Wenn Sie eine Kampagne in einer lokalen Zeitzone bearbeiten, die weniger als 24 Stunden im Voraus geplant wurde, wird der Zeitplan der Nachricht nicht geändert. Wenn Sie eine Kampagne in einer lokalen Zeitzone so bearbeiten, dass sie zu einem späteren Zeitpunkt versendet wird (z. B. um 19 Uhr statt um 18 Uhr), erhalten die Nutzer, die sich zum Zeitpunkt der ursprünglichen Sendezeit im Zielsegment befanden, die Nachricht weiterhin zur ursprünglichen Zeit (18 Uhr). Wenn Sie eine lokale Zeitzone bearbeiten, um zu einer früheren Zeit zu senden (z. B. 16 Uhr statt 17 Uhr), wird die Kampagne trotzdem an alle Mitglieder des Segments zur ursprünglichen Zeit (17 Uhr) gesendet.

{% alert note %}
Bei Canvas-Schritten müssen Nutzer:innen nicht 24 Stunden in dem Schritt sein, um den nächsten Schritt zur Zustellung zur Ortszeit zu erhalten.
{% endalert %}

Wenn Sie den Nutzern erlaubt haben, sich erneut für die Kampagne zu qualifizieren, dann erhalten sie sie wieder zur ursprünglichen Zeit (17 Uhr). Bei allen nachfolgenden Ereignissen Ihrer Kampagne werden Ihre Nachrichten jedoch nur zu der von Ihnen festgelegten Zeit gesendet.

{% endapi %}
{% api %}

### Wann werden Änderungen an lokalen Zeitzonen-Kampagnen wirksam?

{% apitags %}
Kampagnen
{% endapitags %}

Die zeitbasierten Filter der Zielsegmente sollten bei Zeitzonenkampagnen ein Zeitfenster von mindestens 48 Stunden enthalten, um die Zustellung an das gesamte Segment zu gewährleisten. Nehmen wir zum Beispiel ein Segment, das Nutzer:innen an ihrem zweiten Tag mit den folgenden Filtern zusammenstellt:

- Erstmals verwendet vor mehr als 1 Tag
- Erstmals vor weniger als 2 Tagen benutzt

Bei der Zustellung in der lokalen Zeitzone können Benutzer in diesem Segment aufgrund der Zustellungszeit und der lokalen Zeitzone des Benutzers fehlen. Das liegt daran, dass ein Nutzer:innen das Segment zu dem Zeitpunkt verlassen kann, zu dem seine Zeitzone die Zustellung triggert.

{% endapi %}
{% api %}

### Welche Änderungen kann ich an geplanten Kampagnen vor dem Start vornehmen?

{% apitags %}
Kampagnen
{% endapitags %}

Wenn die Kampagne geplant ist, müssen außer der Zusammensetzung der Nachricht noch andere Änderungen vorgenommen werden, bevor wir die Nachrichten in die Warteschlange stellen. Wie bei allen Kampagnen können Sie Konversions-Events nicht mehr bearbeiten, sobald die Kampagne gestartet wurde.

{% endapi %}
{% api %}

### Nach welchem Zeitraum werden Nachrichten für eine geplante Kampagne in die Warteschlange gestellt?

{% apitags %}
Kampagnen
{% endapitags %}

- Einmalig geplante Kampagnen können bis zur geplanten Sendezeit bearbeitet werden.
- Wiederkehrende geplante Kampagnen können bis zur geplanten Sendezeit bearbeitet werden.
- Zeitzonenspezifische Kampagnen können bis 24 Stunden vor dem geplanten Sendetermin bearbeitet werden.
- Kampagnen zur optimalen Sendezeit können bis zu 24 Stunden vor dem Tag, an dem die Kampagne versendet werden soll, bearbeitet werden.

{% endapi %}
{% api %}

### Was passiert, wenn ich eine Bearbeitung innerhalb der "sicheren Zone" vornehme?

{% apitags %}
Kampagnen
{% endapitags %}

Eine Änderung des Sendezeitpunkts von Kampagnen innerhalb dieses Zeitraums kann zum Beispiel zu unerwünschtem Verhalten führen:

- Braze sendet keine Nachrichten an Benutzer, die die Sendezeit um mehr als eine Stunde überschritten haben.
- Nachrichten, die sich bereits in der Warteschlange befanden, werden möglicherweise immer noch zur ursprünglich eingestellten Zeit gesendet und nicht zur angepassten Zeit.

{% endapi %}
{% api %}

### Was soll ich tun, wenn die "sichere Zone" bereits überschritten ist?

{% apitags %}
Kampagnen
{% endapitags %}

Um sicherzustellen, dass die Kampagnen wie gewünscht funktionieren, empfehlen wir, die aktuelle Kampagne zu stoppen (dadurch werden alle Nachrichten in der Warteschlange gestoppt). Sie können die Kampagne dann duplizieren, die erforderlichen Änderungen vornehmen und die neue Kampagne starten. Möglicherweise müssen Sie Nutzer von dieser Kampagne ausschließen, die bereits die erste Kampagne erhalten haben.

Stellen Sie sicher, dass Sie den Kampagnenzeitplan so anpassen, dass der Versand in der jeweiligen Zeitzone zulässig ist.

{% endapi %}
{% api %}

### Wann bewertet Braze die Benutzer für die Bereitstellung in der lokalen Zeitzone?

{% apitags %}
Kampagnen
{% endapitags %}

Für die Zustellung zur Ortszeit prüft Braze die Nutzer:innen während dieser beiden Instanzen auf ihre Zugangsberechtigung:

- Um Samoa-Zeit (UTC+13) des geplanten Tages
- Zur Ortszeit des geplanten Tages

Damit ein:e Nutzer:in für einen Entry in Frage kommt, muss er für beide Prüfungen in Frage kommen. Wenn ein Canvas zum Beispiel am 7\. August 2021 um 14 Uhr Ortszeit gestartet werden soll, müssten für einen Nutzer in New York die folgenden Prüfungen durchgeführt werden, um die Berechtigung zu prüfen:

- New York am 6\. August 2021 um 9 Uhr
- New York am 7\. August 2021 um 2 Uhr nachmittags

Die Verweildauer im Segment vor dem Start muss mindestens 24 Stunden betragen. Wenn der Nutzer:innen bei der ersten Prüfung nicht teilnahmeberechtigt ist, wird Braze die zweite Prüfung nicht durchführen.

{% endapi %}
{% api %}

### Warum stimmt die Anzahl der Nutzer, die eine Kampagne betreten, nicht mit der erwarteten Anzahl überein?

{% apitags %}
Kampagnen
{% endapitags %}

Die Anzahl der Nutzer, die eine Kampagne betreten, kann von der von Ihnen erwarteten Anzahl abweichen, da die Zielgruppen und Auslöser ausgewertet werden. In Braze werden Zielgruppen vor dem Trigger ausgewertet (außer bei dem [Trigger Attributänderung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Dies führt dazu, dass Nutzer aus der Kampagne aussteigen, wenn sie zunächst nicht zu Ihrer ausgewählten Zielgruppe gehören, bevor irgendwelche Auslöseaktionen ausgewertet werden.

{% endapi %}
{% api %}

<!-- Canvases -->

### Was passiert, wenn die Zielgruppe und die Sendezeit bei einem Canvas, der eine Variante, aber mehrere Verzweigungen hat, identisch sind?

{% apitags %}
Canvase
{% endapitags %}

Für jeden Schritt wird ein Auftrag in die Warteschlange aufgenommen. Diese werden etwa zur selben Zeit ausgeführt und einer von ihnen "gewinnt". In der Praxis kann dies etwas gleichmäßig sortiert sein, aber es ist wahrscheinlich, dass zumindest eine leichte Tendenz zu dem Schritt besteht, der zuerst erstellt wurde.

Außerdem können wir keine Garantien dafür geben, wie diese Verteilung genau aussehen wird. Wenn Sie eine gleichmäßige Aufteilung sicherstellen möchten, fügen Sie einen [Zufallsfilter für die Eimeranzahl]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) hinzu.

{% endapi %}
{% api %}

### Was passiert, wenn Sie einen Canvas anhalten?

{% apitags %}
Canvase
{% endapitags %}

Wenn Sie einen Canvas anhalten, gilt Folgendes:

- Die Benutzer werden daran gehindert, den Canvas aufzurufen.
- Es werden ungeachtet der aktuellen Position im Ablauf keine weiteren Nachrichten verschickt.
    - **Eine Ausnahme:** E-Mail Canvase lässt sich nicht sofort stoppen. Nachdem die Anfragen an SendGrid gesendet wurden, können wir nicht mehr verhindern, dass sie dem Nutzer:innen zugestellt werden.

{% alert note %}
Wenn Sie einen Canvas anhalten, werden Nutzer:innen, die in einem Schritt warten, nicht beendet. Wenn Sie die Leinwand wieder aktivieren und die Benutzer immer noch warten, werden sie den Schritt abschließen und zur nächsten Komponente übergehen. Wenn jedoch der Zeitraum für den Übergang in die nächste Komponente bereits verstrichen ist, folgt der Ausschluss aus dem Canvas.
{% endalert %}

{% endapi %}
{% api %}

### Wann wird ein Ausnahmeereignis ausgelöst?

{% apitags %}
Canvase
{% endapitags %}

Ausnahme-Events triggern nur, während der Nutzer:in auf die Canvas-Komponente wartet, mit der sie verknüpft ist. Wenn ein:e Nutzer:in eine Aktion durchführt, wird das Ausnahme-Event nicht ausgelöst.

Wenn Sie Nutzer:innen ausschließen möchten, die ein bestimmtes Ereignis vorgebracht haben, verwenden Sie stattdessen [Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

{% endapi %}
{% api %}

### Wie wirkt sich die Bearbeitung eines Canvas auf Benutzer aus, die sich bereits im Canvas befinden?

{% apitags %}
Canvase
{% endapitags %}

Wenn Sie einige der Schritte eines mehrstufigen Canvas bearbeiten, erhalten Benutzer, die bereits in der Zielgruppe waren, aber die Schritte noch nicht erhalten haben, die aktualisierte Version der Nachricht. Dies geschieht allerdings nur, wenn noch keine Bewertung für den jeweiligen Schritt erfolgt ist.

Weitere Informationen darüber, was Sie nach dem Start bearbeiten können und was nicht, finden Sie unter [Ändern Ihres Canvas nach dem Start]({{site.baseurl}}/post-launch_edits/).

{% endapi %}
{% api %}

### Wie werden Benutzerkonversionen in einem Canvas verfolgt?

{% apitags %}
Canvase
{% endapitags %}

Ein Benutzer kann nur einmal pro Canvas-Eintrag konvertieren.

Umrechnungen werden der letzten Nachricht zugeordnet, die der Benutzer für diesen Eintrag erhalten hat. Der Zusammenfassungsblock am Anfang eines Canvas spiegelt alle Konvertierungen wider, die von Benutzern innerhalb dieses Pfads durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben oder nicht. Bei jedem weiteren Schritt werden nur Konversionen angezeigt, die während des letzten Schrittes, den der Nutzer:innen erhalten hat, stattgefunden haben.

{% details Use cases %}

#### Anwendungsfall 1

Es gibt einen Canvas-Pfad mit 10 Push-Benachrichtigungen und dem Konversions-Event "Sitzungsbeginn" ("Öffnet die App"):

- Nutzer:in A öffnet die App nach der Anmeldung, aber bevor er oder sie die erste Nachricht erhält.
- Benutzer B öffnet die App nach jeder Push-Benachrichtigung.

**Ergebnis:**
Die Zusammenfassung zeigt zwei Konvertierungen an, während die einzelnen Schritte eine Konvertierung von eins für den ersten Schritt und null für alle folgenden Schritte anzeigen.

{% alert note %}
Wenn Ruhezeiten zum Zeitpunkt des Konversions-Events aktiv sind, gelten die gleichen Regeln.
{% endalert %}

#### Anwendungsfall 2

Es gibt ein einstufiges Canvas mit Quiet Hours:

1. Nutzer:in betritt den Canvas.
2. Der erste Schritt wird nicht verzögert, liegt aber in den Ruhezeiten, sodass die Nachricht unterdrückt wird.
3. Nutzer:in führt das Konversions-Event durch.

**Ergebnis:**
Der Nutzer:in wird in der gesamten Canvas-Variante als konvertiert gezählt, aber nicht der Schritt, da er oder sie den Schritt nicht erhalten hat.

{% enddetails %}

{% endapi %}
{% api %}

### Ist Canvas Analytics oder der Segmenter genauer, wenn es um die Anzahl der einzelnen Benutzer geht?

{% apitags %}
Canvase
{% endapitags %}

Der Segmenter ist eine genauere Statistik für eindeutige Benutzerdaten als Canvas- oder Kampagnenstatistiken. Das liegt daran, dass Canvas- und Kampagnenstatistiken Zahlen sind, die Braze erhöht, wenn etwas passiert. Das bedeutet, dass es Variablen gibt, die dazu führen können, dass diese Zahl von der des Segmenters abweicht. So können Nutzer:innen zum Beispiel mehr als einmal für ein Canvas oder eine Kampagne konvertieren.  

{% endapi %}
{% api %}

### Warum stimmt die Anzahl der Benutzer, die ein Canvas betreten, nicht mit der erwarteten Anzahl überein?

{% apitags %}
Canvase
{% endapitags %}

Die Anzahl der Nutzer, die ein Canvas betreten, kann von der von Ihnen erwarteten Anzahl abweichen, da die Zielgruppen und Auslöser ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (es sei denn, Sie verwenden einen Trigger für [die Änderung eines Attributs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Dies führt dazu, dass Nutzer, die nicht zu Ihrer ausgewählten Zielgruppe gehören, aus dem Canvas herausfallen, bevor irgendwelche Auslöseaktionen ausgewertet werden.

{% endapi %}
{% api %}

<!-- Analytics -->

### Welche Metriken werden von Braze gemessen?

{% apitags %}
Analytics
{% endapitags %}

Je nach Kanal misst Braze eine Vielzahl von Metriken, die es Ihnen ermöglichen, den Erfolg einer Kampagne zu bestimmen und zukünftige Kampagnen zu planen. Eine umfassende Liste finden Sie in unserem [Glossar zu den Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/).

{% endapi %}
{% api %}

### Wie wird der Umsatz in Braze berechnet?

{% apitags %}
Analytics
{% endapitags %}

Auf der Seite **Einnahmen** können Sie Daten zu den Einnahmen oder Käufen über bestimmte Zeiträume, für ein bestimmtes Produkt oder die gesamten Einnahmen oder Käufe Ihrer App einsehen. Diese Umsatzzahlen ergeben sich aus den Käufen, die von Kampagnenempfängern innerhalb eines bestimmten Umrechnungszeitraums getätigt werden.

Allerdings ist es wichtig zu wissen, dass Braze ein Marketing-Tool ist und kein Tool zur Umsatzverwaltung. Unser [Kaufobjekt]({{site.baseurl}}/api/objects_filters/purchase_object/) unterstützt keine Erstattungen und Stornierungen, so dass Sie beim Vergleich mit anderen Tools möglicherweise Diskrepanzen feststellen.

{% endapi %}
{% api %}

### Welche Berichte gibt es in Currents?

{% apitags %}
Analytics
{% endapitags %}

Unser Currents-Tool streamt kontinuierlich sowohl Daten zum Messaging-Engagement als auch zum Kundenverhalten an einen unserer zahlreichen Datenpartner. So können Sie die einzigartigen und wertvollen Daten, die Braze erstellt, nutzen, um Ihre Business-Intelligence- und Analytics-Bemühungen bei anderen Best-in-Class-Partnern zu unterstützen.

Diese Daten gehen über die Metriken für das Messaging-Engagement hinaus und können auch komplexere Zahlen wie die Leistung von benutzerdefinierten Attributen und Ereignissen umfassen. Weitere Einzelheiten finden Sie in unserem [Glossar der aktuellen Ereignisse]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/).

{% endapi %}
{% api %}

### Wie kann ich einen wiederkehrenden Engagementbericht planen?

{% apitags %}
Analytics
{% endapitags %}

So richten Sie regelmäßige Engagement-Berichte ein:

1. Navigieren Sie in Ihrem Dashboard-Konto unter **Daten** zu **Engagement Reports**.
2. Klicken Sie auf **\+ Neuen Bericht erstellen**.
3. Fügen Sie die [Kampagnen und Canvas-Nachrichten]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#manually-select-campaigns-or-canvases) (einzeln oder [nach Tag]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases)) hinzu, die Sie in Ihrem Bericht zusammenstellen möchten.
4. [Nehmen Sie Statistiken]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#add-statistics-to-your-report) in den Bericht [auf]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#add-statistics-to-your-report).
5. Wählen Sie die Komprimierung und den Deliminator für Ihren Bericht.
6. Geben Sie die E-Mail-Adressen der Braze-Benutzer ein, die diesen Bericht erhalten sollen.
7. Wählen Sie den [Zeitraum]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#time-frame) aus, aus dem Sie Daten für Ihren Bericht ausführen möchten.
8. Wählen Sie die [Intervalle (täglich, wöchentlich, etc.)]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#data-display), in denen Sie die Aufschlüsselung Ihrer Daten sehen möchten.
9. Planen Sie Ihren Bericht so, dass er [sofort]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-immediately) oder zu einem [bestimmten Zeitpunkt in der Zukunft]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-at-designated-time) [gesendet wird]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-immediately).
10. Führen Sie den Bericht aus, und öffnen Sie ihn in Ihrer E-Mail, wenn er ankommt!

{% endapi %}
{% api %}

### Was ist der Unterschied zwischen Engagement Reports und dem Report Builder?

{% apitags %}
Analytics
{% endapitags %}

Engagement-Berichte liefern Ihnen CSVs mit Engagement-Statistiken für bestimmte Nachrichten aus Kampagnen und Canvases über eine ausgelöste E-Mail. Bestimmte Daten werden auf Kampagnen- oder Canvas-Ebene aggregiert und nicht auf Ebene der einzelnen Varianten oder Schritte. Berichte werden nicht im Dashboard gespeichert. Ihre erneute Erstellung kann zu statistischen Veränderungen führen.

Mit dem Report Builder können Sie die Ergebnisse mehrerer Kampagnen oder Canvases in einer einzigen Ansicht vergleichen, so dass Sie leicht feststellen können, welche Engagement-Strategien sich am stärksten auf Ihre Schlüsselkennzahlen ausgewirkt haben. Sowohl für Kampagnen als auch für Canvases können Sie Ihre Daten exportieren und Ihren Bericht speichern, um ihn in Zukunft einzusehen.

Weitere Informationen über die Verwendung von Berichten und Analysen in Braze finden Sie in der [Übersicht über Berichte]({{site.baseurl}}/user_guide/analytics/reporting/reports_overview/).

{% endapi %}
