---
nav_title: Erstellen einer Prognose über die Abwanderung
article_title: Erstellen einer Prognose über die Abwanderung
description: "Dieser Artikel beschreibt, wie Sie im Braze-Dashboard eine Prognose zur Abwanderung erstellen."
page_order: 1

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

Klicken Sie auf **Weiter**, um zum nächsten Schritt zu gelangen. Optional können Sie auf **Jetzt erstellen** klicken, um alle Standardeinstellungen zu verwenden und zum letzten Schritt der Erstellung überzugehen. Sie haben die Möglichkeit, die Einstellungen zu überprüfen, bevor Sie mit dem Erstellungsprozess beginnen. Sie können später zu jedem Schritt zurückkehren, indem Sie ihn in der Fortschrittsanzeige oben auswählen.

## Schritt 2: Definieren Sie abwandern

Verwenden Sie im Bereich **Abwanderungsdefinition** die bereitgestellten Filter, um festzulegen, wie Sie die Benutzerabwanderung für Ihr Unternehmen definieren. Mit anderen Worten: Was muss ein:e Nutzer:in in welchem Zeitraum tun, damit Sie sie:ihn als abgewandert betrachten?

Denken Sie daran, dass Sie nicht erklären müssen, welche Verhaltensweisen dem Abwandern vorausgehen, sondern nur, was eine:n Nutzer:in zu einer abgewanderten Nutzerin oder einem abgewanderten Nutzer macht. Stellen Sie sich das so vor, dass ein:e Nutzer:in etwas abwandern kann, das sie:er entweder einmal tut (`do`) oder nicht mehr tut (`do not`). Sie könnten zum Beispiel Nutzer:innen, die Ihre App seit 7 Tagen nicht mehr geöffnet haben, als abgewandert betrachten. Sie können die Deinstallation oder angepasste Events wie die Abmeldung, die Deaktivierung eines Kontos oder andere in Betracht ziehen, um eine:n Nutzer:in abwandern zu lassen. 

#### Abwanderungsfenster

Das Abwanderungsfenster ist der Zeitrahmen, in dem ein:e Nutzer:in das Verhalten durchführt, das als Abwandern bezeichnet wird. Es kann bis zu 60 Tage eingestellt werden. In diesem Fenster können Sie historische Daten abfragen, um die Prognose zu trainieren. Nachdem die Vorhersage erstellt wurde und die Benutzer Bewertungen erhalten haben, zeigt der _Churn Risk Score_ außerdem an, wie wahrscheinlich es ist, dass ein Benutzer innerhalb der durch das Churn Window festgelegten Anzahl von Tagen abwandert. 

Hier ein Beispiel für eine einfache Definition auf der Grundlage der verstrichenen Sitzungen der letzten 7 Tage.

![Abwanderungsdefinition: Ein:e Nutzer:in gilt als abgewandert, wenn sie:er innerhalb von 7 Tagen keine Sitzung beginnt][1]

Für diesen Fall wählen wir `do not` und `start a session` aus. Sie können andere Filter mit `AND` und `OR` nach Belieben kombinieren, um die von Ihnen gewünschte Definition zu erstellen. Interessieren Sie sich für einige mögliche Definitionen des Abwanderns, die Sie berücksichtigen sollten? Im folgenden Abschnitt über die [Definition von Abwanderung](#sample-definitions) finden Sie einige Anregungen.

{% alert note %}
Bei `do` gehen wir davon aus, dass aktive Nutzer:innen die von Ihnen für diese Zeile angegebene Aktion nicht durchgeführt haben, bevor sie abgewandert sind. Diese Aktion führt zu Abwanderung. <br><br>Für `do not` betrachten wir aktive Nutzer:innen als diejenigen, die diese Aktion in den Tagen zuvor durchgeführt und dann beendet haben.
{% endalert %}

Unterhalb der Definition sehen Sie Schätzungen darüber, wie viele Nutzer:innen (die in der Vergangenheit abgewandert sind und die nach Ihrer Definition nicht abgewandert sind) verfügbar sind. Sie sehen auch die erforderlichen Mindestwerte. Braze muss über diese Mindestanzahl von Nutzer:innen in den historischen Daten verfügen, damit die Prognosen über genügend Daten verfügen, um daraus zu lernen.

## Schritt 3: Filtern Sie Ihre Prognosen-Zielgruppen

Ihre Vorhersagezielgruppe ist die Gruppe von Nutzern, für die Sie das Abwanderungsrisiko vorhersagen möchten. Standardmäßig ist dies auf **Alle Benutzer** eingestellt, was bedeutet, dass diese Vorhersage für alle Ihre aktiven Benutzer Abwanderungsrisikowerte erstellt. In der Regel wird das Modell besser funktionieren, wenn Sie die Gruppe der Nutzer, die Sie am Churning hindern möchten, anhand einiger Kriterien eingrenzen und filtern. Denken Sie an die Benutzer, die Ihnen am meisten bedeuten und die Sie gerne behalten möchten, und definieren Sie sie hier. Sie könnten zum Beispiel Nutzer behalten wollen, die die App vor mehr als einem Monat zum ersten Mal genutzt oder einen Kauf getätigt haben.

{% alert note %}
Die prognostizierte Zielgruppe darf 100 Millionen Nutzer nicht überschreiten.
{% endalert %}

Das Zeitfenster für Filter, die mit "Zuletzt..." beginnen, wie "Zuletzt genutzte App" und "Zuletzt getätigter Kauf", **kann das in der Abwanderungsdefinition angegebene Abwanderungsfenster nicht überschreiten**, wenn das Prognose-Fenster 14 Tage oder weniger beträgt. Wenn Ihre Churn-Definition beispielsweise ein Zeitfenster von 14 Tagen hat, darf das Zeitfenster für die Filter "Letzte..." 14 Tage nicht überschreiten.

#### Alle-Filter-Modus

Um sofort eine neue Prognose erstellen zu können, wird nur eine Teilmenge der Segmentierungsfilter von Braze unterstützt. Im Alle-Filter-Modus können Sie alle Braze-Filter verwenden, benötigen aber ein Abwanderungsfenster, um die Prognose zu erstellen. Wenn das Abwanderungsfenster beispielsweise auf 15 Tage eingestellt ist, dauert es 15 Tage, um die Nutzerdaten zu sammeln und die Prognose zu erstellen, wenn Sie Filter verwenden, die nur im Alle-Filter-Modus unterstützt werden. Außerdem sind einige Schätzungen über die Zuschauerzahlen im Modus Vollständiger Filter nicht verfügbar.

Eine Beispielliste mit Definitionen für die Vorhersagezielgruppe finden Sie im folgenden Abschnitt über [Beispieldefinitionen für Abwanderung](#sample-definitions).

![][3]

Genau wie auf der vorherigen Seite sehen Sie im unteren Bereich die geschätzte Anzahl der historischen Nutzer, die sich aus der Definition der Abwanderung und der Definition der Vorhersagezielgruppe ergibt. Diese Schätzungen müssen die angegebenen Mindestanforderungen erfüllen, um eine Prognose erstellen zu können.

## Schritt 4: Wählen Sie die Update-Häufigkeit für die Prognose der Abwanderung

Das maschinelle Lernmodell, das beim Ausfüllen dieser Seite erstellt wird, wird nach einem von Ihnen gewählten Zeitplan verwendet, um neue Churn-Risikobewertungen zu erstellen. Wählen Sie die **maximale Häufigkeit der Aktualisierungen**, die Sie für sinnvoll halten. Wenn Sie z. B. eine wöchentliche Werbeaktion versenden möchten, um zu verhindern, dass Benutzer abwandern, stellen Sie die Aktualisierungshäufigkeit auf **Wöchentlich** an einem Tag und zu einer Uhrzeit Ihrer Wahl ein. 

![Der Zeitplan für das Update der Prognosen ist auf täglich um 17 Uhr eingestellt.][2]

{% alert note %}
Die Vorschau und die Demo-Prognose werden das Abwanderungsrisiko der Nutzer:innen niemals aktualisieren. Darüber hinaus erfordern tägliche Updates für Vorhersagen einen zusätzlichen Kauf im Vergleich zu wöchentlichen oder monatlichen Updates mit Predictive Churn. Um diese Funktionalität zu erwerben, wenden Sie sich an Ihren Account Manager.
{% endalert %}

## Schritt 5: Prognose erstellen

Überprüfen Sie, ob Ihre Angaben korrekt sind, und wählen Sie **Prognose erstellen**. Sie können Ihre Änderungen auch in Entwurfsform speichern, indem Sie **Als Entwurf speichern** wählen, um zu dieser Seite zurückzukehren und das Modell später zu erstellen. Nachdem Sie auf **Vorhersage erstellen** geklickt haben, beginnt der Prozess zur Erstellung des Modells. Dies kann je nach Datenvolumen zwischen 30 Minuten und einigen Stunden dauern. Für diese Prognose sehen Sie eine Seite, auf der erklärt wird, dass das Training für die Dauer der Modellerstellung im Gange ist.

Sobald dies geschehen ist, wechselt die Seite automatisch in die Analytics-Ansicht und Sie erhalten außerdem eine E-Mail, die Sie darüber informiert, dass die Vorhersage und die Ergebnisse fertig sind. Im Falle eines Fehlers kehrt die Seite in den Bearbeitungsmodus zurück und gibt eine Erklärung, was schief gelaufen ist.

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

[1]: {% image_buster /assets/img/churn/churn1.png %}
[2]: {% image_buster /assets/img/churn/churn2.png %}
[3]: {% image_buster /assets/img/churn/churn5.png %}

