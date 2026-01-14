---
nav_title: Aktionsbasierte Zustellung
article_title: Aktionsbasierte Zustellung
page_order: 1
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie Kampagnen triggern können, die gesendet werden, nachdem ein:e Nutzer:in ein bestimmtes Event abgeschlossen hat."
tool: Campaigns

---

# Aktionsbasierte Zustellung

> Aktionsbasierte Zustellungskampagnen oder Event-gesteuerte Kampagnen sind sehr effektiv für transaktions- oder leistungsbezogene Nachrichten. Anstatt Ihre Kampagne an bestimmten Tagen zu versenden, können Sie sie auslösen, wenn ein Nutzer ein bestimmtes Ereignis abgeschlossen hat. 

## Eine ausgelöste Kampagne einrichten

### Schritt 1: Wählen Sie ein Trigger-Event aus

Wählen Sie ein Trigger-Event aus. Dies kann eine der folgenden Möglichkeiten beinhalten:
- Einen Kauf tätigen
- Eine Sitzung starten
- Ausführen eines benutzerdefinierten Ereignisses
- Ausführen des primären Konversionsereignisses der Kampagne
- Hinzufügen einer E-Mail-Adresse zu einem Benutzerprofil
- Ändern eines benutzerdefinierten Attributwerts
- Update eines Abo-Status
- Aktualisieren des Status einer Abonnementgruppe
- Interaktion mit anderen Kampagnen
    - In-App-Nachricht anzeigen
    - In-App-Nachricht anklicken
    - Klicken Sie auf die Schaltflächen für In-App-Nachrichten
    - E-Mail anklicken
    - Alias in E-Mail anklicken
    - Angeklickter Alias in einer Kampagne oder einem Canvas-Schritt
    - E-Mail öffnen
    - E-Mail geöffnet (Bot/automatisch)
    - E-Mail geöffnet (andere Öffnungsweisen)
    - Push-Benachrichtigung direkt öffnen
    - Klicken Sie auf die Schaltfläche Push-Benachrichtigung
    - Klicken Sie auf Push-Story Seite
    - Konversions-Event durchführen
    - E-Mail erhalten
    - SMS empfangen
    - Klicken Sie auf den verkürzten SMS-Link
    - Push-Benachrichtigung erhalten
    - Webhook empfangen
    - Sind in der Kontrollgruppe eingeschrieben
    - Inhaltskarte anzeigen
    - Inhaltskarte anklicken
    - Inhalt der Karte verwerfen
- Einen Standort eingeben
- Durchführung des Ausnahmeereignisses für eine andere Kampagne
- Mit einem Canvas-Schritt interagieren
- Triggern eines Geofence
- Versenden einer eingehenden SMS-Nachricht
- Versenden einer eingehenden WhatsApp-Nachricht

Sie können die triggernden Events auch über die [angepassten Event-Eigenschaften]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) von Braze weiter filtern, was eine Anpassung der Event-Eigenschaften für angepasste Events und In-App-Käufe zulässt. Mit dieser Funktion können Sie die Benutzer, die eine Nachricht erhalten, anhand der spezifischen Attribute des benutzerdefinierten Ereignisses genauer bestimmen und so eine stärkere Personalisierung der Kampagne und eine differenziertere Datenerfassung ermöglichen. 

Nehmen wir zum Beispiel an, wir haben eine Kampagne mit einem angepassten Event für einen Warenkorb-Abbruch, das durch den Filter für die Eigenschaft "Warenkorb-Wert" weiter adressiert wird. Diese Kampagne erreicht nur Nutzer:innen, die Waren im Wert von $100 bis $200 in ihrem Warenkorb liegen haben. 

![]({% image_buster /assets/img_archive/customEventProperties.png %})

{% alert note %}
Das Trigger-Ereignis "Sitzung starten" kann das allererste Öffnen der App durch den Nutzer sein, wenn das Segment Ihrer Kampagne für neue Nutzer gilt. (zum Beispiel, wenn Ihr Segment aus Nutzern ohne Sitzungen besteht).
{% endalert %}

Denken Sie daran, dass Sie eine ausgelöste Kampagne immer noch an ein bestimmtes Nutzersegment senden können. Nutzer, die nicht zu diesem Segment gehören, erhalten die Kampagne also nicht, selbst wenn sie das Auslöseereignis abschließen. Wenn Sie feststellen, dass Nutzer:innen die Kampagne nicht erhalten, obwohl sie sich für das Segment qualifiziert haben, lesen Sie unseren Abschnitt darüber, [warum ein Nutzer eine getriggerte Kampagne nicht erhalten haben könnte]({{site.baseurl}}/help/help_articles/campaigns_and_canvas/not_triggering/).

Für das Trigger-Event, wenn ein:e Nutzer:in seinem Profil eine E-Mail-Adresse hinzufügt, gelten die folgenden Regeln:

- Das Trigger-Event wird nach dem Update der Attribute des Nutzerprofils abgefeuert. Das bedeutet, dass die Auswertung der Segmente und Filter der Kampagne nach jeder Attributaktualisierung erfolgt. Dies ist von Vorteil, da Sie damit Filter wie "E-Mail-Adresse stimmt mit gmail.com überein" einrichten können, um eine Trigger-Kampagne zu erstellen, die nur an Gmail-Benutzer gesendet wird und ausgelöst wird, sobald diese ihre E-Mail-Adresse hinzufügen.
- Das Trigger-Event wird ausgelöst, wenn eine E-Mail-Adresse zu einem Nutzerprofil hinzugefügt wird. Wenn Sie mehrere Benutzerprofile haben, die Sie mit derselben E-Mail-Adresse erstellen, wird die Kampagne möglicherweise mehrfach ausgelöst, einmal für jedes Benutzerprofil.

Darüber hinaus unterliegen ausgelöste In-App-Nachrichten weiterhin den Regeln für die Zustellung von In-App-Nachrichten und erscheinen zu Beginn einer App-Sitzung.

![]({% image_buster /assets/img_archive/schedule_triggered1.png %})

### Schritt 2: Verzögerungsdauer auswählen

Wählen Sie aus, wie lange gewartet werden soll, bevor die Kampagne gesendet wird, nachdem die Trigger-Kriterien erfüllt sind. Wenn die gewählte Verzögerungsdauer länger ist als die Dauer des Versands der Nachricht, werden keine Benutzer die Kampagne erhalten. 

Außerdem erhalten Nutzer, die das Trigger-Ereignis nach dem Start Ihrer Kampagne abschließen, die Nachricht als erste, nachdem die Verzögerung verstrichen ist. Nutzer:innen, die das Trigger-Event vor dem Start der Kampagne abgeschlossen haben, sind nicht für die Kampagne qualifiziert.

![]({% image_buster /assets/img_archive/schedule_triggered22.png %})

Sie können die Kampagne auch entweder an einem bestimmten Wochentag (indem Sie "am nächsten" wählen und dann einen Tag auswählen) oder an einer bestimmten Anzahl von Tagen (indem Sie "in" auswählen) in der Zukunft versenden. Alternativ können Sie Ihre Nachricht auch mit der Funktion [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) versenden, anstatt manuell eine Zustellzeit auszuwählen.

![]({% image_buster /assets/img_archive/schedule_triggered7.png %})
![]({% image_buster /assets/img_archive/schedule_triggered8.png %})

### Schritt 3: Ausnahme-Events auswählen

Wählen Sie ein Ausnahme-Event aus, durch das Nutzer:innen von dieser Kampagne ausgeschlossen werden. Sie können dies nur tun, wenn Ihre getriggerte Nachricht zeitverzögert gesendet wird. [Ausnahme-Events]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#exception-events) können ein Kauf, der Beginn einer Sitzung, die Durchführung eines der in einer Kampagne vorgesehenen [Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events) oder die Durchführung eines angepassten Events sein. Wenn ein:e Nutzer:in das Trigger-Event ausführt, dann aber aufgrund der Zeitverzögerung Ihr Ausnahme-Event ausführt, bevor die Nachricht gesendet wird, erhält er die Kampagne nicht. Nutzer:innen, die die Kampagne aufgrund des Ausnahme-Events nicht erhalten haben, sind automatisch berechtigt, sie in der Zukunft zu erhalten, wenn sie das nächste Mal das triggernde Event abschließen, auch wenn Sie nicht festlegen, dass Nutzer:innen [erneut berechtigt sind]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/).

![]({% image_buster /assets/img_archive/schedule_triggered32.png %})

Mehr über den Einsatz von Ausnahme-Events erfahren Sie in unserem Abschnitt über [Anwendungsfälle]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#use-cases).

> Wenn Sie eine Kampagne mit einem Auslöseereignis senden, das mit dem Ausnahmeereignis übereinstimmt, bricht Braze die Kampagne ab und plant automatisch eine neue Kampagne auf der Grundlage der Zustellungszeit der Nachricht des Ausnahmeereignisses. Wenn Ihr erstes Trigger-Event beispielsweise bei fünf Minuten beginnt und das Ausnahme-Events bei 10 Minuten, würden Sie die 10 Minuten des Ausnahme-Events als Zustellungszeit für die Nachrichten der offiziellen Kampagne zugrunde legen.

{% alert note %}
Sie können einen "Sitzungsstart" nicht gleichzeitig zum Trigger-Event und zum Ausnahme-Event für eine Kampagne machen. Sie haben jedoch jederzeit die Möglichkeit, ein anderes angepasstes Event außerhalb dieser Option auszuwählen.
{% endalert %}

### Schritt 4: Dauer zuweisen

Legen Sie die Dauer der Kampagne fest, indem Sie eine Startzeit und optional eine Endzeit angeben.

![]({% image_buster /assets/img_archive/schedule_triggered43.png %})

Wenn ein Benutzer ein Trigger-Ereignis innerhalb des angegebenen Zeitrahmens ausführt, sich aber aufgrund einer geplanten Verzögerung außerhalb des Zeitrahmens für die Nachricht qualifiziert, erhält er die Kampagne nicht. Wenn Sie also eine Zeitverzögerung einstellen, die länger als der Zeitrahmen der Nachricht ist, werden keine Nutzer:innen Ihre Kampagne erhalten. Außerdem können Sie wählen, ob die Nachricht in den [Ortszeiten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/#local-time-zone-campaigns) der Nutzer:innen gesendet werden soll.

### Schritt 5: Zeitrahmen wählen

Wählen Sie aus, ob die:der Nutzer:in die Kampagne während eines bestimmten Teils des Tages erhalten soll. Wenn Sie der Nachricht einen Zeitrahmen geben und der Benutzer entweder das auslösende Ereignis außerhalb des Zeitrahmens abschließt oder die Verzögerung der Nachricht dazu führt, dass er den Zeitrahmen verpasst, wird der Benutzer Ihre Nachricht standardmäßig nicht erhalten.

![]({% image_buster /assets/img_archive/schedule_triggered5.png %})

Für den Fall, dass ein Benutzer das auslösende Ereignis innerhalb des Zeitrahmens abschließt, aber durch die Verzögerung der Nachricht aus dem Zeitrahmen fällt, können Sie das folgende Kästchen markieren, damit diese Benutzer die Kampagne trotzdem erhalten.

![]({% image_buster /assets/img_archive/schedule_triggered_next_available.png %})

Wenn ein:e Nutzer:in die Nachricht nicht erhält, weil er den Zeitrahmen verpasst hat, ist er dennoch qualifiziert, sie zu erhalten, wenn er das nächste Mal das Trigger-Event abschließt, auch wenn Sie nicht gewählt haben, dass Nutzer:innen [erneut qualifiziert]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/) werden. Wenn Sie sich dafür entscheiden, dass Nutzer:innen erneut teilnahmeberechtigt werden, können sie die Kampagne jedes Mal erhalten, wenn sie das Trigger-Event abschließen, vorausgesetzt, sie qualifizieren sich innerhalb des festgelegten Zeitraums.

Wenn Sie der Kampagne auch eine bestimmte Dauer zugewiesen haben, muss sich ein Benutzer sowohl innerhalb der Dauer als auch innerhalb des bestimmten Teils des Tages qualifizieren, um die Nachricht zu erhalten.

### Schritt 6: Wiederzulassung bestimmen

Bestimmen Sie, ob Nutzer:innen für die Kampagne [wieder wählbar]({% image_buster /assets/img_archive/ReEligible.png %}) werden können. Wenn Sie zulassen, dass Nutzer:innen wieder teilnahmeberechtigt werden, können Sie eine Zeitverzögerung festlegen, bevor die Nutzer:innen die Kampagne erneut erhalten können. So verhindern Sie, dass Ihre getriggerten Kampagnen "spammy" werden.

![]({% image_buster /assets/img_archive/schedule_triggered6.png %})

## Anwendungsfälle

Ausgelöste Kampagnen sind sehr effektiv für transaktions- oder leistungsbezogene Nachrichten.

Zu den Transaktionskampagnen gehören Nachrichten, die gesendet werden, nachdem der Nutzer einen Kauf abgeschlossen oder einen Artikel in seinen Warenkorb gelegt hat. Der letztgenannte Fall ist ein gutes Beispiel für eine Kampagne, die von einem Ausnahme-Event profitieren würde. Angenommen, Ihre Kampagne erinnert Nutzer an Artikel in ihrem Einkaufswagen, die sie noch nicht gekauft haben. Das Ausnahme-Event wäre in diesem Fall, dass die:der Nutzer:in die Produkte in seinem Warenkorb kauft. Bei erfolgsbasierten Kampagnen können Sie eine Nachricht 5 Minuten, nachdem der Nutzer eine Konversion abgeschlossen oder ein Spiellevel besiegt hat, senden.

Außerdem können Sie bei der Erstellung von Willkommenskampagnen Nachrichten auslösen, die gesendet werden, nachdem sich der Benutzer registriert oder ein Konto eingerichtet hat. Wenn Sie die Nachrichten an verschiedenen Tagen nach der Registrierung verschicken, können Sie ein gründliches Onboarding durchführen.

## Warum hat ein Benutzer meine ausgelöste Kampagne nicht erhalten?

Jeder dieser Punkte verhindert, dass ein:e Nutzer:in, die:der das Trigger-Event abgeschlossen hat, die Kampagne erhält:

- Die:der Nutzer:in hat das Ausnahme-Event abgeschlossen, bevor die Zeitspanne vollständig verstrichen ist.
- Liquid-[`abort_message` Logik]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) wurde verwendet und die Nachricht wurde auf der Grundlage der `abort_message`-Logik oder -Regeln abgebrochen.
- Die Zeitverzögerung, durch die die:der Nutzer:in nach Ablauf der Laufzeit für den Empfang der Kampagne qualifiziert wird.
- Die Zeitverzögerung hat dazu geführt, dass der Nutzer außerhalb des festgelegten Teils des Tages für den Erhalt der Kampagne qualifiziert wurde.
- Der Nutzer hat die Kampagne bereits erhalten, und Nutzer können sich nicht erneut qualifizieren.
- Nutzer:innen können die Kampagne zwar erneut erhalten, aber erst nach einem bestimmten Zeitraum triggern, und dieser Zeitraum ist noch nicht verstrichen.

[Die Segmentierung]({{site.baseurl}}/user_guide/engagement_tools/segments/) einer getriggerten Kampagne anhand von Nutzerdaten, die zum Zeitpunkt des Events aufgezeichnet wurden, kann eine [Race-Condition]({{site.baseurl}}/help/best_practices/race_conditions/#race-conditions) verursachen. Dies geschieht, wenn das Benutzerattribut, nach dem die Kampagne segmentiert ist, geändert wird, aber die Änderung für den Benutzer noch nicht verarbeitet wurde, als die Kampagne gesendet wurde. Da Kampagnen beim Entry die Mitgliedschaft in einem Segment prüfen, kann dies dazu führen, dass die:der Nutzer:in die Kampagne nicht erhält.

Stellen Sie sich zum Beispiel vor, Sie möchten eine durch ein Event getriggerte Kampagne an männliche Nutzer:innen senden, die sich gerade registriert haben. Bei der Registrierung der Nutzerin oder des Nutzers zeichnen Sie ein angepasstes Event `registration` auf und setzen gleichzeitig das Attribut `gender` der Nutzerin oder des Nutzers. Das Event kann die Kampagne triggern, bevor Braze das Geschlecht der Nutzerin oder des Nutzers verarbeitet hat, so dass dieser die Kampagne nicht erhalten kann.

Stellen Sie sicher, dass das Attribut, nach dem die Kampagne segmentiert ist, vor dem Event auf die Server von Braze übertragen wird. Wenn dies nicht möglich ist, ist die beste Möglichkeit, die Zustellung zu garantieren, die Verwendung [angepasster Event-Eigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties), um die relevanten Nutzer:innen-Eigenschaften an das Event anzuhängen und einen Eigenschaftsfilter für die spezifische Event-Eigenschaft anstelle eines Segmentierungsfilters anzuwenden. In unserem Beispiel würden Sie dem benutzerdefinierten Ereignis `registration` die Eigenschaft `gender` hinzufügen, damit Braze garantiert über die Daten verfügt, die Sie benötigen, wenn Ihre Kampagne ausgelöst wird.

Wenn eine Kampagne aktionsbasiert ist und eine Verzögerung aufweist, können Sie außerdem die Option zur **Neubewertung der Segmentzugehörigkeit zum Zeitpunkt des Versands** aktivieren, um sicherzustellen, dass die Benutzer noch zur Zielgruppe gehören, wenn die Nachricht versendet wird.

Wenn Ihre Kampagne durch ein bestimmtes benutzerdefiniertes Ereignis ausgelöst wird und Sie ein Segment als Zielgruppe auswählen, müssen die Benutzer dasselbe benutzerdefinierte Ereignis durchführen, um in das Segment aufgenommen zu werden. Das bedeutet, dass Nutzer:innen Teil der Zielgruppe sein müssen, bevor eine aktionsbasierte Kampagne ausgelöst werden kann. Der allgemeine Arbeitsablauf für eine ausgelöste Kampagne sieht folgendermaßen aus:

1. **Schließen Sie sich der Zielgruppe an:** Wenn ein:e Nutzer:in das angepasste Event ausführt, wird er zur Zielgruppe der Kampagne hinzugefügt.
2. **Triggern Sie die E-Mail:** Ein:e Nutzer:in muss das angepasste Event erneut ausführen, um die E-Mail zu triggern, da er zur Zielgruppe gehören muss, bevor die E-Mail versendet werden kann.

Wir empfehlen, entweder die Zielgruppe so zu ändern, dass sie alle Nutzer:innen umfasst, oder zu überprüfen, ob die Nutzer:innen, die das Event ausführen sollen, bereits zur Zielgruppe der Kampagne gehören, damit die Nachricht getriggert werden kann.

![]({% image_buster /assets/img_archive/reevaluate_segment_membership.png %})

### Fehlerbehebung bei angepassten Events

Bestätigen Sie zunächst, dass das angepasste Event an Braze weitergegeben wird. Gehen Sie zu **Analytics** > **Bericht über angepasste Events**, und wählen Sie dann das entsprechende angepasste Event und den Datumsbereich aus. Wenn das Ereignis nicht angezeigt wird, vergewissern Sie sich, dass es korrekt eingerichtet ist und dass der Nutzer:innen die richtige Aktion durchgeführt hat.

Wenn das angepasste Event angezeigt wird, gehen Sie zur weiteren Fehlerbehebung wie folgt vor:

- Überprüfen Sie das heruntergeladene Profil des Nutzers:innen, um sich zu vergewissern, dass er das Ereignis ausgelöst hat und wann er es ausgelöst hat. Wenn das Ereignis getriggert wurde, vergleichen Sie den Zeitstempel, zu dem das Ereignis getriggert wurde, mit dem Zeitpunkt, zu dem die Kampagne live ging. Das Ereignis kann ausgelöst worden sein, bevor die Kampagne live ging.
- Überprüfen Sie die Changelogs für die Kampagne und alle Segmente, die beim Targeting verwendet wurden, um festzustellen, ob sich der Nutzer:in dem Segment befand, als sein angepasstes Event ausgelöst wurde. Wenn sie nicht in dem Segment wären, hätten sie die Kampagne nicht erhalten.
- Überprüfen Sie, ob der Nutzer:innen durch die Segmentierung in eine Kontrollgruppe aufgenommen wurde und somit die Kampagne nicht erhalten hat.
- Wenn es eine geplante Verzögerung gibt, prüfen Sie, ob das angepasste Event des Nutzers:innen vor der Verzögerung ausgelöst wurde. Wäre das Ereignis vor der Verzögerung ausgelöst worden, hätten sie die Kampagne nicht erhalten.

{% alert note %}
In-App-Nachrichten können nur durch Ereignisse ausgelöst werden, die über das SDK gesendet werden, nicht über die REST API.
{% endalert %}

