---
nav_title: Erstellen einer Prognose über die Abwanderung
article_title: Erstellen einer Prognose über die Abwanderung
description: "Dieser Artikel beschreibt, wie Sie im Braze-Dashboard eine Prognose zur Abwanderung erstellen."
page_order: 1.1

---

# Erstellen einer Prognose über die Abwanderung

> Erfahren Sie, wie Sie im Braze-Dashboard eine Prognose zur Abwanderung erstellen können.

## Schritt 1: Erstellen Sie eine neue Vorhersage

Gehen Sie in Braze zu **Analytics** > **Predictive Churn**.

Eine Prognose ist eine Instanz eines trainierten Modells des maschinellen Lernens und aller Parameter und Daten, die es verwendet. Auf dieser Seite sehen Sie eine Liste aktueller aktiver Vorhersagen zusammen mit einigen grundlegenden Informationen über sie. Hier können Sie Vorhersagen umbenennen, archivieren und neue erstellen. Archivierte Vorhersagen sind inaktiv und aktualisieren die Bewertungen der Benutzer nicht. 

Um eine neue Vorhersage zu erstellen, wählen Sie **Vorhersage erstellen** und wählen eine neue **Churn-Vorhersage**.

{% alert note %}
Es gibt eine Obergrenze von fünf gleichzeitig aktiven Prognosen zur Abwanderung. Vor dem Kauf von Predictive Churn steht Ihnen maximal eine aktive Vorschau zur Abwanderung zur Verfügung. Eine Abwanderungsvorhersage in der Vorschau aktualisiert die Ergebnisse nicht regelmäßig und ermöglicht es Ihnen nicht, Benutzer auf der Grundlage der Vorhersage anzusprechen. Kontaktieren Sie Ihren Kundenbetreuer für weitere Informationen.
{% endalert %}

Auf der Seite **Grundlagen** geben Sie Ihrer neuen Vorhersage einen eindeutigen Namen. Sie können auch eine optionale Beschreibung eingeben, um sich Notizen zu dieser speziellen Vorhersage zu machen.

Wählen Sie **Vorwärts**, um zum nächsten Schritt zu gelangen. Optional können Sie **Jetzt erstellen** auswählen, um alle Standardeinstellungen zu verwenden und zum letzten Schritt der Erstellung überzugehen. Sie haben die Opportunity, die Einstellungen zu überprüfen, bevor Sie mit der Erstellung beginnen. Sie können später zu jedem Schritt zurückkehren, indem Sie ihn in der Fortschrittsanzeige auswählen.

## Schritt 2: Definieren Sie abwandern

Verwenden Sie im Bereich **Abwanderungsdefinition** die bereitgestellten Filter, um festzulegen, wie Sie die Benutzerabwanderung für Ihr Unternehmen definieren. Mit anderen Worten: Was muss ein:e Nutzer:in in welchem Zeitraum tun, damit Sie sie:ihn als abgewandert betrachten?

Denken Sie daran, dass Sie nicht erklären müssen, welche Verhaltensweisen dem Abwandern vorausgehen, sondern nur, was eine:n Nutzer:in zu einer abgewanderten Nutzerin oder einem abgewanderten Nutzer macht. Stellen Sie sich das so vor, dass ein:e Nutzer:in etwas abwandern kann, das sie:er entweder einmal tut (`do`) oder nicht mehr tut (`do not`). Sie könnten zum Beispiel Nutzer:innen, die Ihre App seit 7 Tagen nicht mehr geöffnet haben, als abgewandert betrachten. Sie können die Deinstallation oder angepasste Events wie die Abmeldung, die Deaktivierung eines Kontos oder andere in Betracht ziehen, um eine:n Nutzer:in abwandern zu lassen. 

#### Abwanderungsfenster

Das Abwanderungsfenster ist der Zeitraum, in dem die Aktivität eines Nutzers:innen die Kriterien für eine Abwanderung erfüllt. Sie können ihn für bis zu 60 Tage einstellen, je nach den verfügbaren Daten. In diesem Fenster können Sie historische Daten abrufen, um Ihre Prognosen zu trainieren. Sobald die Prognose erstellt ist, werden Sie sehen, ob genügend Daten für genaue Ergebnisse vorhanden waren.

Nachdem die Prognosen erstellt wurden und die Nutzer:innen Bewertungen erhalten haben, zeigt der _Churn Risk Score_ an, wie wahrscheinlich es ist, dass ein Nutzer:innen innerhalb des von Ihnen im Churn-Fenster festgelegten Zeitraums abwandert. 

Hier ein Beispiel für eine einfache Definition auf der Grundlage der verstrichenen Sitzungen der letzten 7 Tage.

![Churn Definition, bei der ein Nutzer:innen als abgewandert gilt, wenn er innerhalb von 7 Tagen keine Sitzung beginnt]({% image_buster /assets/img/churn/churn1.png %})

Für diesen Fall wählen wir `do not` und `start a session` aus. Sie können andere Filter mit `AND` und `OR` nach Belieben kombinieren, um die von Ihnen gewünschte Definition zu erstellen. Interessieren Sie sich für einige mögliche Definitionen des Abwanderns, die Sie berücksichtigen sollten? Im folgenden Abschnitt über die [Definition von Abwanderung](#sample-definitions) finden Sie einige Anregungen.

{% alert note %}
Bei `do` gehen wir davon aus, dass aktive Nutzer:innen die von Ihnen für diese Zeile angegebene Aktion nicht durchgeführt haben, bevor sie abgewandert sind. Diese Aktion führt zu Abwanderung. <br><br>Für `do not` betrachten wir aktive Nutzer:innen als diejenigen, die diese Aktion in den Tagen zuvor durchgeführt und dann beendet haben. <br><br>**Beispiel:** Wenn Abwandern als "hat in den letzten 60 Tagen nicht gekauft" definiert ist, betrachten wir als aktive Nutzer:innen diejenigen, die in den letzten 60 Tagen gekauft haben. Daher gilt jeder, der in den letzten 60 Tagen keinen Kauf getätigt hat, nicht als aktiver Nutzer:innen. Das bedeutet, dass eine Zielgruppe, die auf der Grundlage dieser Abwanderungsdefinition erstellt wird, nur Nutzer:innen enthält, die in den letzten 60 Tagen gekauft haben. Dies kann dazu führen, dass die Zielgruppe für die voraussichtliche Abwanderung deutlich kleiner ist als die ursprüngliche Population - die meisten Nutzer:innen in einem Workspace erfüllen möglicherweise bereits die Definition von abgewandert und sind daher in der Prognose für die Abwanderung nicht aktiv.
{% endalert %}

Unterhalb der Definition sehen Sie Schätzungen darüber, wie viele Nutzer:innen (die in der Vergangenheit abgewandert sind und die nach Ihrer Definition nicht abgewandert sind) verfügbar sind. Sie sehen auch die erforderlichen Mindestwerte. Braze muss über diese Mindestanzahl von Nutzer:innen in den historischen Daten verfügen, damit die Prognosen über genügend Daten verfügen, um daraus zu lernen.

## Schritt 3: Filtern Sie Ihre Prognosen-Zielgruppen

Ihre Prognose-Zielgruppe ist die Gruppe von Nutzern:innen, für die Sie das Abwanderungsrisiko prognostizieren möchten. Die Zielgruppe für Prognosen definiert die Gruppe der Nutzer:innen, die das Modell für maschinelles Lernen betrachtet, um aus der Vergangenheit zu lernen. Standardmäßig ist diese Option auf **Alle Nutzer:innen** eingestellt. Das bedeutet, dass diese Prognose für alle aktiven Nutzer:innen Risikowerte für das Abwandern erstellt (siehe den vorherigen Hinweis, wer für ein Abwanderungsmodell als aktiv gilt).

Je nach Anwendungsfall möchten Sie vielleicht Filter verwenden, um die Nutzer:innen zu bestimmen, die Sie für das Modell bewerten möchten. Wählen Sie dazu **Meine eigene Vorhersagezielgruppe definieren** und wählen Sie Ihre Zielgruppenfilter. Wenn Sie beispielsweise eine Mitfahr-App mit Fahrern und Nutzern:innen in Ihrer Nutzerbasis betreiben und ein Modell zur Abwanderung von Nutzern:innen erstellen, werden Sie Ihre Prognosen auf die Nutzer:innen filtern wollen. Denken Sie daran, dass Sie in vielen Anwendungsfällen keine bestimmte Zielgruppe für die Prognosen auswählen müssen. Wenn Ihr Anwendungsfall beispielsweise darin besteht, Nutzer:innen in der EU-Region anzusprechen, bei denen die Wahrscheinlichkeit des Abwanderns am größten ist, können Sie Ihr Modell auf alle Nutzer:innen anwenden und dann einfach einen Filter für die EU-Region in das Segment der Kampagne aufnehmen.

Braze zeigt Ihnen die geschätzte Größe Ihrer Prognosen-Zielgruppen an. Wenn Sie die gewünschte Zielgruppe angeben und die Mindestanforderungen für die Ausführung des Modells nicht erfüllen, versuchen Sie, einen breiteren Filter anzugeben oder die Option **Alle Nutzer**: **innen** zu verwenden. Beachten Sie, dass die Größe Ihrer Gruppe "alle Nutzer:innen" nicht statisch ist und von Modell zu Modell variiert, da sie Ihre Definition des Abwanderns berücksichtigt. Ein Beispiel: Die Definition von Abwanderung ist, dass innerhalb von 30 Tagen **kein** Kauf getätigt wird. In diesem Fall lässt Braze das Modell auf Nutzer:innen laufen, die in den letzten 30 Tagen gekauft **haben** (und prognostiziert die Wahrscheinlichkeit, dass sie in den nächsten 30 Tagen **nicht** kaufen werden), so dass dies die Nutzer:innen sind, die in der Metrik "Alle Nutzer" berücksichtigt werden.

{% alert note %}
Die prognostizierte Zielgruppe darf 100 Millionen Nutzer nicht überschreiten.
{% endalert %}

Das Zeitfenster für Filter, die mit "Zuletzt..." beginnen, wie "Zuletzt genutzte App" und "Zuletzt getätigter Kauf", **kann das in der Abwanderungsdefinition angegebene Abwanderungsfenster nicht überschreiten**, wenn das Prognose-Fenster 14 Tage oder weniger beträgt. Wenn Ihre Churn-Definition beispielsweise ein Zeitfenster von 14 Tagen hat, darf das Zeitfenster für die Filter "Letzte..." 14 Tage nicht überschreiten.

#### Alle-Filter-Modus

Um sofort eine neue Prognose erstellen zu können, wird nur eine Teilmenge der Segmentierungsfilter von Braze unterstützt. Im Alle-Filter-Modus können Sie alle Braze-Filter verwenden, benötigen aber ein Abwanderungsfenster, um die Prognose zu erstellen. Wenn das Abwanderungsfenster beispielsweise auf 15 Tage eingestellt ist, dauert es 15 Tage, um die Nutzerdaten zu sammeln und die Prognose zu erstellen, wenn Sie Filter verwenden, die nur im Alle-Filter-Modus unterstützt werden. Außerdem sind einige Schätzungen über die Zuschauerzahlen im Modus Vollständiger Filter nicht verfügbar.

Eine Beispielliste mit Definitionen für die Vorhersagezielgruppe finden Sie im folgenden Abschnitt über [Beispieldefinitionen für Abwanderung](#sample-definitions).

![]({% image_buster /assets/img/churn/churn5.png %})

Genau wie auf der vorherigen Seite sehen Sie im unteren Bereich die geschätzte Anzahl der historischen Nutzer, die sich aus der Definition der Abwanderung und der Definition der Vorhersagezielgruppe ergibt. Diese Schätzungen müssen die angegebenen Mindestanforderungen erfüllen, um eine Prognose erstellen zu können.

## Schritt 4: Wählen Sie die Update-Häufigkeit für die Prognose der Abwanderung

Das Modell des maschinellen Lernens generiert Ereigniswahrscheinlichkeitsbewertungen für Nutzer:innen. Diese Bewertungen werden nach dem Zeitplan aktualisiert, den Sie hier auswählen. Sie können Nutzer:innen auf der Grundlage ihres Event Likelihood Scores gezielt zusammenstellen. 

Wählen Sie die **maximale Häufigkeit der Aktualisierungen**, die Sie für sinnvoll halten. Wenn Sie z. B. eine wöchentliche Werbeaktion versenden möchten, um zu verhindern, dass Benutzer abwandern, stellen Sie die Aktualisierungshäufigkeit auf **Wöchentlich** an einem Tag und zu einer Uhrzeit Ihrer Wahl ein. 

![Zeitplan für das Update der Prognosen auf täglich um 17 Uhr eingestellt.]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
Die Vorschau und die Demo-Prognose werden das Abwanderungsrisiko der Nutzer:innen niemals aktualisieren. Darüber hinaus erfordern tägliche Updates für Vorhersagen einen zusätzlichen Kauf im Vergleich zu wöchentlichen oder monatlichen Updates mit Predictive Churn. Um diese Funktionalität zu erwerben, wenden Sie sich an Ihren Account Manager.
{% endalert %}

## Schritt 5: Prognose erstellen

Überprüfen Sie, ob Ihre Angaben korrekt sind, und wählen Sie **Prognose erstellen**. Sie können Ihre Änderungen auch in Entwurfsform speichern, indem Sie **Als Entwurf speichern** wählen, um zu dieser Seite zurückzukehren und das Modell später zu erstellen. Nachdem Sie **Prognose erstellen** ausgewählt haben, beginnt der Prozess, der das Modell erzeugt. Dies kann je nach Datenvolumen zwischen 30 Minuten und einigen Stunden dauern. Für diese Prognose sehen Sie eine Seite, auf der erklärt wird, dass das Training für die Dauer der Modellerstellung im Gange ist. Das Braze-Modell berücksichtigt angepasste Events, Kauf-Events, Kampagnen-Interaktions-Events und Sitzungsdaten.

Danach wechselt die Seite automatisch in die Analytics-Ansicht, und Sie erhalten außerdem eine E-Mail, die Sie darüber informiert, dass die Prognose und die Ergebnisse fertig sind. Im Falle eines Fehlers kehrt die Seite in den Bearbeitungsmodus zurück und gibt eine Erklärung, was schief gelaufen ist.

Die Vorhersage wird alle **zwei Wochen automatisch** neu aufgebaut ("retrainiert"), um sie auf der Grundlage der neuesten verfügbaren Daten auf dem neuesten Stand zu halten. Beachten Sie, dass dies ein anderer Prozess ist als die Erstellung der _Churn Risk Scores_ der Benutzer, die das Ergebnis der Vorhersage sind. Letzteres hängt von der Häufigkeit der Updates ab, die Sie in Schritt 4 gewählt haben.

## Definitionen für voraussichtliche Abwanderung und Prognosen der Zielgruppe {#sample-definitions}

**Beispiele für Churn-Definitionen**<br>
- "Innerhalb von 7 Tagen ein angepasstes Event 'Abo-Kündigung' durchführen"<br>
- "Machen Sie innerhalb von 30 Tagen ein angepasstes Event 'Probezeit abgelaufen'"<br>
- "Innerhalb von 1 Tag deinstallieren." <br>
- "Innerhalb von 14 Tagen keinen Kauf tätigen." <br>

Für die von uns skizzierten Definitionen der Abwanderung gibt es möglicherweise auch entsprechende Definitionen für Prognosen der Zielgruppen:<br>
- **Sie haben das Abonnement vor mehr als 2 Wochen begonnen ODER Sie haben das Abonnement vor weniger als zwei Wochen begonnen**<br>Vielleicht möchten Sie in diesem Fall 2 Prognosen erstellen und neuen Abonnent:innen dann andere Nachrichten schicken als längerfristigen Abonnent:innen. Sie könnten dies auch als "Erster getätigter Kauf vor mehr als 30 Tagen" definieren.<br>
- **Deinstallationsprogramme**<br>Sie könnten sich auf Kunden konzentrieren, die in der jüngsten Vergangenheit etwas gekauft oder die App erst kürzlich genutzt haben.<br>
- **Diejenigen, die Gefahr laufen, nicht zu kaufen, als Definition von Abwandern**<br>Vielleicht möchten Sie sich auf Kunden konzentrieren, die in letzter Zeit in Ihrer App gestöbert, gesucht oder sich damit beschäftigt haben. Vielleicht kann die richtige Rabattaktion die Abwanderung dieser engagierten Gruppe verhindern.

## Archivierte Vorhersagen

Bei archivierten Vorhersagen werden die Benutzerbewertungen nicht mehr aktualisiert. Alle archivierten Prognosen, die nicht archiviert sind, aktualisieren die Nutzer:innen weiterhin nach einem festgelegten Zeitplan. Archivierte Vorhersagen werden nie gelöscht und bleiben in der Liste.


