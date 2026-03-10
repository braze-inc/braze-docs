---
nav_title: Prognose zur Abwanderung erstellen
article_title: Prognose zur Abwanderung erstellen
description: "Dieser Artikel beschreibt, wie Sie eine Prognose zur Abwanderung im Braze-Dashboard erstellen."
page_order: 1.1

---

# Prognose zur Abwanderung erstellen

> Erfahren Sie, wie Sie eine Prognose zur Abwanderung im Braze-Dashboard erstellen.

## 1. Schritt: Neue Prognose erstellen

Gehen Sie in Braze zu **Analytics** > **Predictive Churn**.

Eine Prognose ist eine Instanz eines trainierten Modells für maschinelles Lernen sowie alle Parameter und Daten, die es verwendet. Auf dieser Seite sehen Sie eine Liste der aktuell aktiven Prognosen zusammen mit einigen grundlegenden Informationen. Hier können Sie Prognosen umbenennen, archivieren und neue erstellen. Archivierte Prognosen sind inaktiv und aktualisieren keine Nutzer:innen-Scores.

Um eine neue Prognose zu erstellen, wählen Sie **Create Prediction** und dann eine neue **Churn Prediction** aus.

{% alert note %}
Es gibt ein Limit von fünf gleichzeitig aktiven Prognosen zur Abwanderung. Vor dem Kauf von Predictive Churn ist das Limit eine aktive Vorschau-Prognose zur Abwanderung. Eine Vorschau-Prognose zur Abwanderung aktualisiert die Scores nicht regelmäßig und erlaubt es Ihnen nicht, Nutzer:innen basierend auf der Ausgabe der Prognose anzusprechen. Kontaktieren Sie Ihren Account Manager für Details.
{% endalert %}

Geben Sie auf der Seite **Basics** Ihrer neuen Prognose einen eindeutigen Namen. Sie können auch eine optionale Beschreibung hinzufügen, um Notizen zu dieser bestimmten Prognose festzuhalten.

Wählen Sie **Forward**, um zum nächsten Schritt zu gelangen. Optional können Sie **Build Now** auswählen, um alle Standardeinstellungen zu verwenden und zum letzten Schritt der Erstellung zu springen. Sie haben die Möglichkeit, die Einstellungen vor dem Start des Build-Prozesses zu überprüfen. Sie können jederzeit zu einem früheren Schritt zurückkehren, indem Sie ihn im Fortschrittsbalken auswählen.

## 2. Schritt: Abwanderung definieren

Im Panel **Churn Definition** verwenden Sie die bereitgestellten Filter, um festzulegen, wie Sie die Abwanderung von Nutzer:innen für Ihr Unternehmen definieren. Mit anderen Worten: Was muss ein:e Nutzer:in in welchem Zeitraum tun, damit Sie ihn/sie als abgewandert betrachten?

Denken Sie daran, dass Sie nicht erklären müssen, welche Verhaltensweisen einer Abwanderung vorausgehen könnten – nur was eine:n Nutzer:in zu einer/einem abgewanderten Nutzer:in macht. Denken Sie dabei an etwas, das ein:e Nutzer:in entweder einmal tut (`do`) oder aufhört zu tun (`do not`), was als Abwanderung gilt. Zum Beispiel könnten Sie Nutzer:innen, die Ihre App 7 Tage lang nicht geöffnet haben, als abgewandert betrachten. Sie könnten auch eine Deinstallation oder angepasste Events wie das Abbestellen, Deaktivieren eines Kontos oder andere Aktionen als Auslöser für die Abwanderung betrachten.

#### Abwanderungsfenster

Das Abwanderungsfenster ist der Zeitraum, in dem die Aktivität einer/eines Nutzer:in die Kriterien für eine Abwanderung erfüllt. Sie können es auf bis zu 60 Tage einstellen, abhängig von den verfügbaren Daten. Dieses Fenster wird verwendet, um historische Daten zum Trainieren Ihrer Prognose heranzuziehen. Sobald die Prognose erstellt ist, sehen Sie, ob genügend Daten für genaue Ergebnisse vorhanden waren.

Nachdem die Prognose erstellt wurde und Nutzer:innen Scores erhalten haben, zeigt der _Churn Risk Score_ an, wie wahrscheinlich es ist, dass ein:e Nutzer:in innerhalb des im Abwanderungsfenster festgelegten Zeitraums abwandert.

Hier ist ein Beispiel für eine einfache Definition basierend auf ausbleibenden Sitzungen in den letzten 7 Tagen.

![Abwanderungsdefinition, bei der ein:e Nutzer:in als abgewandert gilt, wenn er/sie innerhalb von 7 Tagen keine Sitzung startet]({% image_buster /assets/img/churn/churn1.png %})

In diesem Fall wählen wir `do not` und `start a session`. Sie können andere Filter mit `AND` und `OR` kombinieren, um die gewünschte Definition zu erstellen. Interessiert an möglichen Abwanderungsdefinitionen? Im folgenden Abschnitt [Beispieldefinitionen für Abwanderung](#sample-definitions) finden Sie Inspiration.

{% alert note %}
Bei `do` gehen wir davon aus, dass aktive Nutzer:innen die von Ihnen für diese Zeile angegebene Aktion nicht ausgeführt haben, bevor sie abgewandert sind. Das Ausführen der Aktion führt dazu, dass sie als abgewandert gelten. <br><br>Bei `do not` betrachten wir aktive Nutzer:innen als diejenigen, die diese Aktion in den vorherigen Tagen ausgeführt haben und dann damit aufgehört haben. <br><br>**Beispiel:** Wenn Abwanderung als „hat in den letzten 60 Tagen keinen Kauf getätigt" definiert ist, betrachten wir aktive Nutzer:innen als diejenigen, die in den letzten 60 Tagen einen Kauf getätigt haben. Folglich wird jede:r, der/die in den letzten 60 Tagen keinen Kauf getätigt hat, nicht als aktive:r Nutzer:in betrachtet. Das bedeutet, dass eine aus dieser Abwanderungsdefinition erstellte Abwanderungs-Zielgruppe nur Nutzer:innen umfasst, die in den letzten 60 Tagen einen Kauf getätigt haben. Dies kann dazu führen, dass die resultierende Zielgruppe für die voraussichtliche Abwanderung deutlich kleiner aussieht als die ursprüngliche Population – die meisten Nutzer:innen in einem Workspace erfüllen möglicherweise bereits die Definition der Abwanderung und sind daher in der Abwanderungsprognose nicht aktiv.
{% endalert %}

Unterhalb der Definition sehen Sie Schätzungen, wie viele Nutzer:innen (in der Vergangenheit, die gemäß Ihrer Definition abgewandert sind und die nicht abgewandert sind) verfügbar sind. Sie sehen auch die erforderlichen Mindestwerte. Braze benötigt diese Mindestanzahl an Nutzer:innen in den historischen Daten, damit die Prognose genügend Daten zum Lernen hat.

## 3. Schritt: Prognose-Zielgruppe filtern

Ihre Prognose-Zielgruppe ist die Gruppe von Nutzer:innen, für die Sie das Abwanderungsrisiko vorhersagen möchten. Die Prognose-Zielgruppe definiert die Gruppe von Nutzer:innen, die das Modell für maschinelles Lernen betrachtet, um aus der Vergangenheit zu lernen. Standardmäßig ist dies auf **All Users** eingestellt, was bedeutet, dass diese Prognose Abwanderungsrisiko-Scores für alle Ihre aktiven Nutzer:innen erstellt (siehe den vorherigen Hinweis dazu, wer für ein Abwanderungsmodell als aktiv gilt).

Je nach Anwendungsfall möchten Sie möglicherweise Filter verwenden, um die Nutzer:innen festzulegen, die Sie für das Modell bewerten möchten. Wählen Sie dazu **Define my own prediction audience** und wählen Sie Ihre Zielgruppen-Filter. Wenn Sie beispielsweise eine Mitfahr-App mit Fahrer:innen und Fahrgästen in Ihrer Nutzerbasis betreiben und ein Abwanderungsmodell für Fahrgäste erstellen, sollten Sie Ihre Prognose-Zielgruppe auf Fahrgäste beschränken. Beachten Sie, dass viele Anwendungsfälle keine spezifische Prognose-Zielgruppe erfordern. Wenn Ihr Anwendungsfall beispielsweise darin besteht, Nutzer:innen in der EU-Region anzusprechen, die am wahrscheinlichsten abwandern, können Sie Ihr Modell auf alle Nutzer:innen anwenden und dann einfach einen Filter für die EU-Region im Segment der Kampagne hinzufügen.

Braze zeigt Ihnen die geschätzte Größe Ihrer Prognose-Zielgruppe an. Wenn Sie Ihre gewünschte Zielgruppe angeben und das erforderliche Minimum zum Ausführen des Modells nicht erreichen, versuchen Sie, einen breiteren Filter anzugeben oder die Option **All Users** zu verwenden. Beachten Sie, dass die Größe Ihrer „Alle Nutzer:innen"-Gruppe nicht statisch ist und von Modell zu Modell variiert, da sie Ihre Abwanderungsdefinition berücksichtigt. Wenn die Abwanderungsdefinition beispielsweise lautet, **keinen** Kauf in 30 Tagen zu tätigen, führt Braze das Modell für Nutzer:innen aus, die in den letzten 30 Tagen **einen Kauf getätigt haben** (und prognostiziert die Wahrscheinlichkeit, dass sie in den nächsten 30 Tagen **keinen** Kauf tätigen werden). Diese Nutzer:innen werden in der Metrik „Alle Nutzer:innen" widergespiegelt.

{% alert note %}
Die Prognose-Zielgruppe darf 100 Millionen Nutzer:innen nicht überschreiten.
{% endalert %}

Wenn das Prognosefenster 14 Tage oder weniger beträgt, darf das Zeitfenster für Filter, die mit „Last..." beginnen, wie „Last Used App" und „Last Made Purchase", **das in der Abwanderungsdefinition angegebene Abwanderungsfenster nicht überschreiten**. Wenn Ihre Abwanderungsdefinition beispielsweise ein Fenster von 14 Tagen hat, darf das Zeitfenster für die „Last..."-Filter 14 Tage nicht überschreiten.

Das Abwanderungsfenster wird ausgewertet, indem die Anzahl der Tage ab dem letzten Ausführungstag des Modells zurückgerechnet wird. Wenn das Abwanderungsfenster also 15 Tage beträgt und das Modell zuletzt am 1. Dezember ausgeführt wurde, analysiert das Modell den Zeitraum vom 16. November bis zum 30. November, um die Nutzer:innen-Aktivität für die Zielgruppen-Berechtigung und das Training zu verstehen.

#### Alle-Filter-Modus

Um eine neue Prognose sofort zu erstellen, wird nur eine Teilmenge der Braze-Segmentierungsfilter unterstützt. Der Alle-Filter-Modus ermöglicht es Ihnen, alle Braze-Filter zu verwenden, erfordert jedoch ein Abwanderungsfenster, um die Prognose zu erstellen. Wenn das Abwanderungsfenster beispielsweise auf 15 Tage eingestellt ist, dauert es 15 Tage, um die Nutzerdaten zu sammeln und die Prognose zu erstellen, wenn Filter verwendet werden, die nur im Alle-Filter-Modus unterstützt werden. Zusätzlich sind einige Schätzungen zu Zielgruppengrößen im Alle-Filter-Modus nicht verfügbar.

Eine Beispielliste von Prognose-Zielgruppen-Definitionen finden Sie in unseren Beispieldefinitionen im folgenden Abschnitt [Beispieldefinitionen für Abwanderung](#sample-definitions).

![]({% image_buster /assets/img/churn/churn5.png %})

Wie auf der vorherigen Seite zeigt Ihnen das untere Panel die geschätzte Anzahl historischer Nutzer:innen, die sich aus Ihrer Abwanderungsdefinition und Prognose-Zielgruppen-Definition ergeben. Diese Schätzungen müssen die angezeigten Mindestanforderungen erfüllen, um eine Prognose erstellen zu können.

## 4. Schritt: Aktualisierungshäufigkeit für die Abwanderungsprognose wählen

Das Modell für maschinelles Lernen generiert Wahrscheinlichkeits-Scores für Nutzer:innen, und diese Scores werden basierend auf dem hier ausgewählten Zeitplan aktualisiert. Sie können Nutzer:innen basierend auf ihrem Wahrscheinlichkeits-Score ansprechen.

Wählen Sie die **maximale Aktualisierungshäufigkeit**, die für Sie nützlich ist. Wenn Sie beispielsweise eine wöchentliche Aktion senden möchten, um Nutzer:innen von der Abwanderung abzuhalten, stellen Sie die Aktualisierungshäufigkeit auf **Weekly** am Tag und zur Uhrzeit Ihrer Wahl ein.

![Zeitplan für Prognose-Updates auf täglich um 17 Uhr eingestellt.]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
Vorschau- und Demo-Prognosen aktualisieren niemals das Abwanderungsrisiko der Nutzer:innen. Darüber hinaus erfordern tägliche Updates für Prognosen einen zusätzlichen Kauf über die wöchentlichen oder monatlichen Updates mit Predictive Churn hinaus. Um diese Funktionalität zu erwerben, kontaktieren Sie Ihren Account Manager.
{% endalert %}

## 5. Schritt: Prognose erstellen

Überprüfen Sie, ob die von Ihnen angegebenen Details korrekt sind, und wählen Sie **Build Prediction**. Sie können Ihre Änderungen auch als Entwurf speichern, indem Sie **Save As Draft** auswählen, um später zu dieser Seite zurückzukehren und das Modell zu erstellen. Nachdem Sie **Build Prediction** ausgewählt haben, beginnt der Prozess zur Generierung des Modells. Dies kann je nach Datenvolumen zwischen 30 Minuten und einigen Stunden dauern. Für diese Prognose sehen Sie eine Seite, die erklärt, dass das Training während des Modell-Erstellungsprozesses läuft. Das Braze-Modell berücksichtigt angepasste Events, Kauf-Events, Kampagnen-Interaktions-Events und Sitzungsdaten.

Nach Abschluss wechselt die Seite automatisch zur Analytics-Ansicht, und Sie erhalten auch eine E-Mail, die Sie darüber informiert, dass die Prognose und die Ergebnisse bereit sind. Im Falle eines Fehlers kehrt die Seite in den Bearbeitungsmodus zurück mit einer Erklärung, was schiefgelaufen ist.

Die Prognose wird automatisch alle **zwei Wochen** neu erstellt („neu trainiert"), um sie mit den neuesten verfügbaren Daten aktuell zu halten. Beachten Sie, dass dies ein separater Prozess ist von der Erstellung der _Churn Risk Scores_ der Nutzer:innen, der Ausgabe der Prognose. Letzteres wird durch die Aktualisierungshäufigkeit bestimmt, die Sie in Schritt 4 gewählt haben.

## Beispieldefinitionen für Abwanderung und Prognose-Zielgruppen {#sample-definitions}

**Beispieldefinitionen für Abwanderung**<br>
- „Innerhalb von 7 Tagen angepasstes Event ‚Abo-Kündigung' ausführen"<br>
- „Innerhalb von 30 Tagen angepasstes Event ‚Testphase abgelaufen' ausführen"<br>
- „Innerhalb von 1 Tag deinstallieren." <br>
- „Innerhalb von 14 Tagen keinen Kauf tätigen." <br>

Für die beschriebenen Abwanderungsdefinitionen gibt es möglicherweise entsprechende Prognose-Zielgruppen-Definitionen:<br>
- **Abo vor mehr als 2 Wochen gestartet ODER Abo vor weniger als zwei Wochen gestartet**<br>In diesem Fall möchten Sie möglicherweise 2 Prognosen erstellen und dann neue Abonnent:innen anders ansprechen als langjährige Abonnent:innen. Sie könnten dies auch als „Erster Kauf vor mehr als 30 Tagen" definieren.<br>
- **Deinstallationen**<br>Sie könnten sich auf Kund:innen konzentrieren, die kürzlich etwas gekauft oder die App vor Kurzem genutzt haben.<br>
- **Risiko, keinen Kauf zu tätigen, als Definition der Abwanderung**<br>Sie möchten sich möglicherweise auf Kund:innen konzentrieren, die kürzlich gestöbert, gesucht oder sich stärker mit Ihrer App beschäftigt haben. Vielleicht kann die richtige Rabattaktion diese engagiertere Gruppe davon abhalten abzuwandern.

## Archivierte Prognosen

Archivierte Prognosen aktualisieren keine Nutzer:innen-Scores mehr. Jede archivierte Prognose, die wiederhergestellt wird, aktualisiert die Nutzer:innen-Scores weiterhin nach ihrem vorgegebenen Zeitplan. Archivierte Prognosen werden niemals gelöscht und verbleiben in der Liste.