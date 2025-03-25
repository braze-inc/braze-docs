---
nav_title: Globale Kontrollgruppe
article_title: Globale Kontrollgruppe
alias: /global_control_group/
page_order: 0

description: "Dieser Artikel beschreibt, wie Sie die globale Kontrollgruppe einrichten und richtig verwenden. Außerdem erfahren Sie, wie Sie Berichte und Metriken einsehen können, die sich aus der Verwendung dieser Gruppen ergeben."
page_type: reference
tool: Reports
search_rank: 1

---

# Globale Kontrollgruppe

> Verwenden Sie die Globale Kontrollgruppe, um einen Prozentsatz aller Benutzer festzulegen, die keine Kampagnen oder Canvases erhalten sollen. So können Sie die Gesamtwirkung Ihrer Messaging-Maßnahmen im Laufe der Zeit analysieren. 

Wenn Sie das Verhalten von Nutzern, die Nachrichten erhalten, mit dem von Nutzern vergleichen, die keine Nachrichten erhalten, können Sie besser verstehen, wie Ihre Marketingkampagnen und Canvases zu einem Anstieg der Sitzungen und benutzerdefinierten Ereignisse führen.

## Wie die globale Kontrollgruppe funktioniert

Mit der Globalen Kontrollgruppe können Sie einen Prozentsatz aller Benutzer als Kontrollgruppe festlegen. Nach dem Speichern erhalten die Benutzer der Gruppe keine Kampagnen oder Leinwände. 

Ihre Globale Kontrollgruppe wird auf alle Kanäle, Kampagnen und Canvases angewendet, mit Ausnahme von [API-Kampagnen]({{site.baseurl}}/api/api_campaigns#api-campaigns) und News Feed Cards (veraltet). Die Nutzer in Ihrer Kontrollgruppe erhalten weiterhin API-Kampagnen und News Feed Cards. Diese Ausnahme gilt nicht für Content Cards - wenn Sie Content Cards verwenden, erhalten die Benutzer in Ihrer Kontrollgruppe diese nicht.

### Weisen Sie Benutzer zufällig der Globalen Kontrollgruppe zu

Braze wählt nach dem Zufallsprinzip mehrere Bereiche mit [zufälligen Bucket-Nummern]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) aus und schließt Benutzer aus diesen ausgewählten Buckets ein. Wenn Sie derzeit Random Bucket Numbers für andere Zwecke verwenden, lesen Sie bitte die Hinweise, [auf die Sie achten sollten](#things-to-watch-for). 

### Datenverfolgung für die Berichterstattung

Braze misst das Nutzerverhalten in der Kontrollgruppe und in der Stichprobe. Die Stichprobe ist eine zufällige Nutzermenge, die nicht zu der Kontrollgruppe gehört und mit derselben Random-Bucket-Number-Methode erstellt wurde.

### Nutzer:innen von Feature-Flags ausschließen

Sie können keine [Funktionsflags]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) für Benutzer in Ihrer Globalen Kontrollgruppe aktivieren. Das bedeutet, dass Benutzer in Ihrer Globalen Kontrollgruppe auch nicht an Experimenten mit Funktionskennzeichen teilnehmen können.

## Eine globale Kontrollgruppe erstellen

### Schritt 1: Navigieren Sie zu den Globalen Kontrollgruppeneinstellungen

Gehen Sie auf dem Dashboard zu **Zielgruppe** > **Globale Kontrollgruppe**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie diese Seite unter **Engagement** > **Globale Nachrichteneinstellungen** > **Globale Kontrollgruppeneinstellungen**.
{% endalert %}

### Schritt 2: Weisen Sie dieser Kontrollgruppe einen Prozentsatz aller Benutzer zu

Geben Sie einen Prozentsatz für Ihre Kontrollgruppe ein und klicken Sie auf **Speichern**. Nach der Eingabe zeigt Ihnen Braze eine Schätzung an, wie viele Nutzer:innen in Ihre Globale Kontrolle, Behandlung und Behandlungsstichprobe fallen werden. Beachten Sie, dass diese Schätzung umso genauer ist, je mehr Benutzer Sie in Ihrem Arbeitsbereich haben. 

Die Anzahl der Nutzer:innen in Ihrer globalen Kontrollgruppe wird nach der Ersteinrichtung automatisch aktualisiert, damit sie proportional zu diesem Prozentsatz der Zielgruppe bleibt, wenn weitere Nutzer:innen zu Ihrem Workspace hinzugefügt werden. Wenn zum Beispiel die Zahl der Nutzer:innen in Ihrem Workspace wächst, wächst auch die Zahl der Nutzer:innen in Ihrer globalen Kontrollgruppe, so dass Ihre Kontrollgruppe einen konstanten Prozentsatz Ihrer Zielgruppe im Workspace behält. Die Richtlinien für den Prozentsatz finden Sie im folgenden [Abschnitt über bewährte Verfahren](#percentage-guidelines).

![Die globalen Kontrollgruppeneinstellungen mit den Zielgruppeneinstellungen auf "Fünf Prozent der globalen Kontrollgruppenpopulation zuweisen".][4]

### Schritt 3: Ausschlusseinstellungen zuweisen

Mit Tags können Sie Ausschlusskriterien zu der globalen Kontrollgruppe hinzufügen. Alle Kampagnen oder Canvases, die die in den Ausschlusseinstellungen enthaltenen Tags verwenden, nutzen Ihre Globale Kontrollgruppe nicht. Diese Kampagnen und Canvases werden weiterhin an alle Nutzer in der Zielgruppe gesendet, einschließlich derer in Ihrer globalen Kontrollgruppe.

{% alert tip %}
Wenn Sie transaktionsbezogene Nachrichten haben, die an alle Nutzer:innen gesendet werden sollen, möchten Sie vielleicht Ausschlusseinstellungen hinzufügen.
{% endalert %}

![Die Option zum Hinzufügen von Ausschlusseinstellungen zu Ihrer Globalen Kontrollgruppe.][5]

### Schritt 4: Speichern Sie Ihre Kontrollgruppe

An diesem Punkt generiert Braze eine zufällig ausgewählte Gruppe von Benutzern, die den ausgewählten Prozentsatz Ihrer gesamten Benutzerbasis ausmachen. Nach dem Speichern werden alle derzeit aktiven und zukünftigen Kampagnen und Canvases nicht mehr an Benutzer in dieser Gruppe gesendet, außer für Kampagnen oder Canvases, die eines der Tags in Ihren Ausschlusseinstellungen enthalten.

## Deaktivieren Sie Ihre Globale Kontrollgruppe

Sie können Ihre Globale Kontrollgruppe jederzeit auf der Registerkarte **Einstellungen für Globale Kontrollgruppen** deaktivieren. Beachten Sie jedoch, dass Benutzer in dieser Gruppe dann sofort für Kampagnen und Leinwände zugelassen werden.

Bevor Sie Ihre Kontrollgruppe deaktivieren, empfehlen wir Ihnen, eine CSV-Datei mit einem Nutzerverzeichnis [zu exportieren](#export-group-members), da Sie diese noch später benötigen könnten. Wenn Sie eine Kontrollgruppe deaktivieren, gibt es für Braze keine Möglichkeit, die Gruppe wiederherzustellen oder festzustellen, welche Benutzer in dieser Gruppe waren.

Wenn Sie die Kontrollgruppe deaktiviert haben, können Sie eine neue Gruppe speichern. Wenn Sie einen Prozentsatz eingeben und speichern, erzeugt Braze eine neue, zufällig ausgewählte Gruppe von Benutzern. Wenn Sie den gleichen Prozentsatz wie zuvor eingeben, erstellt Braze trotzdem eine neue Gruppe von Benutzern für Ihre Kontroll- und Behandlungsgruppen.

![Ein Dialogfenster mit der Überschrift "Sie ändern die globalen Messaging-Einstellungen" und diesem Text: "Sobald Ihre Globale Kontrollgruppe deaktiviert ist, wird sie nicht mehr von neuen oder derzeit aktiven Kampagnen oder Canvases ausgeschlossen. Benutzer in dieser Gruppe sind sofort berechtigt, Nachrichten zu erhalten. Sind Sie sicher, dass Sie fortfahren möchten?" mit zwei Tasten: Abbrechen und Fortfahren.][2]{: style="max-width:50%" }

## Exportieren Sie Ihre Kontrollgruppenmitglieder {#export-group-members}

Wenn Sie wissen möchten, wer zur globalen Kontrollgruppe gehört, können Sie die Gruppenmitglieder per CSV oder API exportieren. 

Um einen CSV-Export durchzuführen, navigieren Sie zur Registerkarte **Globale Kontrollgruppeneinstellungen** und klicken auf <i class="fas fa-download"></i> **Export**. Für den Export per API verwenden Sie den [Endpunkt`/users/export/global_control_group` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).

{% alert important %}
Historische Kontrollgruppen bleiben nicht erhalten, Sie können also nur die Mitglieder Ihrer aktuellen Gruppe exportieren. Stellen Sie sicher, dass Sie alle notwendigen Daten exportiert haben, bevor Sie eine Kontrollgruppe deaktivieren.
{% endalert %}

## Anzeigen, ob jemand einer globalen Kontrollgruppe angehört

Sie können die Zugehörigkeit zu einer globalen Kontrollgruppe prüfen, wenn Sie im jeweiligen Nutzerprofil unter **Engagement** den Abschnitt **Verschiedenes** aufrufen.

![Abschnitt "Verschiedenes" mit der zufällig generierten nutzerspezifischen Bucket-Nummer 2030 und Angaben zur Mitgliedschaft in der globalen Kontrollgruppe.][1]{: style="max-width:60%;"}

## Berichterstattung

Informationen zu den Berichtsmetriken finden Sie unter [Globale Kontrollgruppenberichte]({{site.baseurl}}/user_guide/data_and_analytics/reporting/global_control_group_reporting/).

## Fehlersuche

Bei der Einrichtung Ihrer globalen Kontrollgruppen und der Anzeige von Berichten können Sie auf folgende Fehler stoßen:

| Fehler | Fehlersuche |
| --- | --- |
| Der Prozentsatz, der bei der Benennung einer globalen Kontrollgruppe eingegeben wurde, konnte nicht gespeichert werden. | Dieses Problem tritt auf, wenn Sie keine ganze Zahl oder eine ganze Zahl eingeben, die nicht zwischen 1 und 15 (einschließlich) liegt. |
| Fehlermeldung "Braze kann die globale Kontrollgruppe nicht aktualisieren" in den globalen Einstellungen. | Dies bedeutet in der Regel, dass eine Komponente dieser Seite geändert wurde, wahrscheinlich aufgrund von Aktionen, die ein anderer Benutzer in Ihrem Braze-Konto vorgenommen hat. Aktualisieren Sie in diesem Fall die Seite und versuchen Sie es erneut. |
| Der Bericht Globale Kontrollgruppe enthält keine Daten. | Wenn Sie auf den Bericht zur globalen Kontrollgruppe zugreifen, ohne zuvor eine globale Kontrollgruppe gespeichert zu haben, enthält der Bericht keine Daten. Erstellen und speichern Sie eine Globale Kontrollgruppe und versuchen Sie es erneut. |
| Meine Konversionsrate liegt bei 0% oder ich sehe die grafische Darstellung nicht, obwohl mehr als null Ereignisse stattfinden. | Wenn die Konversionsanzahl sehr gering und die Kontroll- bzw. Behandlungsgruppe sehr groß ist, kann die Konversionsrate auf 0 % aufgerundet werden und wird dann nicht im Diagramm angezeigt. Überprüfen Sie in diesem Fall die Ereignisanzahl. Sie können die Effektivität Ihrer beiden Gruppen mit Hilfe der Metrik des inkrementellen Uplifts in Prozent vergleichen.  |
| Meine Konversionsrate (oder andere Metriken) ändern sich drastisch, je nachdem, für welchen Zeitraum ich die Daten ansehe. | Wenn Sie Daten über kurze Zeiträume betrachten, kann es vorkommen, dass Ihre Kennzahlen von Tag zu Tag oder von Woche zu Woche schwanken. Wir empfehlen Ihnen, mindestens die Kennzahlen für einen Monat zu betrachten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Darauf sollten Sie achten {#things-to-watch-for}

#### Überlappende zufällige Bucket-Nummern

Ihre Globale Kontrollgruppe wird mit Hilfe von Random Bucket Numbers gebildet. Wenn Sie also andere Tests durchführen, die Segmentfilter mit Random Bucket Numbers verwenden, sollten Sie bedenken, dass es zu Überschneidungen zwischen den von Ihnen erstellten Segmenten und den Benutzern Ihrer Globalen Kontrollgruppe kommen kann.

#### Doppelte E-Mail-Adressen

Wenn zwei Benutzer mit unterschiedlichen externen Benutzer-IDs dieselbe E-Mail-Adresse haben und einer dieser Benutzer in der Kontrollgruppe ist und der andere nicht, dann wird trotzdem eine E-Mail an diese Adresse gesendet, wenn der Benutzer, der nicht in der Kontrollgruppe ist, eine E-Mail erhalten kann. Wenn dies der Fall ist, markieren wir beide Benutzerprofile als solche, die die Kampagne oder die Leinwand mit dieser E-Mail erhalten haben.

#### Globale Kontrollgruppe und nachrichtenspezifische Kontrollgruppen

Es ist möglich, gleichzeitig eine globale und eine kampagnen- oder Canvas-spezifische Kontrollgruppe zu verwenden. Mit einer kampagnenspezifischen oder Canvas-spezifischen Kontrollgruppe können Sie die Wirkung einer bestimmten Botschaft messen.

Benutzer in Ihrer globalen Kontrollgruppe erhalten keine Nachrichten außer denen mit Tag-Ausnahmen. Wenn Sie einer Kampagne oder einem Canvas ein Steuerelement hinzufügen, hält Braze einen Teil Ihrer globalen Behandlungsgruppe vom Empfang dieser bestimmten Kampagne oder dieses Canvas zurück. Das bedeutet, dass ein Mitglied der globalen Kontrollgruppe, das nicht für eine bestimmte Kampagne oder ein bestimmtes Canvas in Frage kommt, auch nicht in der Kontrollgruppe für diese bestimmte Kampagne oder dieses Canvas vertreten ist.

> Kurz gesagt, Benutzer in der globalen Kontrollgruppe werden vor dem Eintritt in die Kampagne oder die Canvas-Zielgruppe herausgefiltert. Von den Benutzern, die die Kampagne oder das Canvas betreten, wird dann ein bestimmter Prozentsatz der Kontrollvariante zugewiesen.

#### Globale Kontrollgruppensegmente in der Entwicklerkonsole

Im Abschnitt **Zusätzliche API-Kennungen** auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) werden möglicherweise mehrere **Global Control-Segmente** angezeigt. Das liegt daran, dass jedes Mal eine neue globale Kontrollgruppe gebildet wird, wenn die globale Kontrollgruppe aktiviert bzw. deaktiviert wird. Dies führt dazu, dass mehrere Segmente als "Globale Kontrollgruppe" bezeichnet werden.

Nur eines dieser Segmente ist aktiv und kann über den [Endpunkt`/users/export/global_control_group` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) abgefragt oder aus dem Dashboard exportiert werden. Der Export aus dem Dashboard gibt ausdrücklich an, aus welchen Untersegmenten sich diese globale Kontrollgruppe zusammensetzt.

## Bewährte Testverfahren

### Optimale Größe der Kontrollgruppe {#percentage-guidelines}

Diese beiden wichtigen Regeln sollten Sie beachten\*\*:
1. Ihre Kontrollgruppe sollte nicht kleiner als 1000 Benutzer sein.
2. Ihre Kontrollgruppe sollte nicht mehr als 10% Ihrer gesamten Zielgruppe ausmachen.

Wenn Ihre Zielgruppe insgesamt kleiner als 10.000 ist, sollten Sie Ihren Prozentsatz erhöhen, um eine Gruppe von mehr als 1000 Nutzer:innen zu bilden; in diesem Fall sollten Sie Ihren Prozentsatz nicht höher als 15% anheben. Denken Sie daran: Je kleiner der Workspace, desto schwieriger sind statistisch aussagekräftige Tests.

- Mit Blick auf die Größe der Kontrollgruppe sollten Sie bedenken, dass Sie für aussagekräftige Verhaltensanalysen eine erhebliche Kundenanzahl in der Kontrollgruppe benötigen. Je größer jedoch Ihre Kontrollgruppe ist, desto weniger Kunden erhalten Ihre Kampagnen. Das ist ein Nachteil, wenn Sie Ihre Kampagnen nutzen, um Engagement und Konversionen zu fördern.
- Welcher prozentuale Anteil an der gesamten Zielgruppe geeignet ist, hängt von deren Größe ab. Je größer sie ist, desto kleiner kann der Prozentsatz sein. Bei kleinen Zielgruppen benötigen Sie dagegen einen höheren Prozentsatz für die Kontrollgruppe.

### Versuchsdauer 

#### Wählen Sie eine ideale Dauer {#reshuffle}

Wie lange Sie Ihr Experiment laufen lassen sollten, bevor Sie die Mitglieder der Kontrollgruppe neu zusammenstellen, hängt davon ab, was Sie testen und wie die Nutzer:innen sich grundsätzlich verhalten. Wenn Sie sich nicht sicher sind, ist ein Vierteljahr (drei Monate) ein guter Anfang, aber Sie sollten nicht kürzer als einen Monat gehen.

Die Versuchsdauer hängt von den Fragen ab, die Sie beantworten möchten. Sie möchten herausfinden, ob es einen Unterschied bei den Sitzungen gibt? Wenn ja, denken Sie darüber nach, wie oft Ihre Nutzer:innen organische Sitzungen haben. Marken, deren Nutzer:innen jeden Tag Sitzungen haben, können kürzere Experimente durchführen als Marken, deren Nutzer:innen nur ein paar Mal im Monat Sitzungen haben. 

Oder Sie interessieren sich für ein benutzerdefiniertes Ereignis, so dass Ihr Experiment möglicherweise länger laufen muss als ein Experiment, bei dem Sie Sitzungen untersuchen, wenn es wahrscheinlich ist, dass Ihre Benutzer dieses benutzerdefinierte Ereignis weniger häufig auslösen.

{% alert tip %}
Je länger Sie dieselbe Kontrollgruppe verwenden, desto stärker wird sie von der Behandlungsgruppe abweichen, was zu Verzerrungen führen kann. Wenn Sie die Globale Kontrollgruppe zurücksetzen, wird die Population wieder ausgeglichen.
{% endalert %}

#### Versuche nicht vorzeitig beenden

Sie sollten entscheiden, wie lange Ihr Experiment laufen soll, bevor Sie es beginnen. Erst wenn Sie diesen Punkt erreicht haben, sollten Sie Ihr Experiment beenden und die endgültigen Ergebnisse sammeln. Wenn Sie Ihr Experiment vorzeitig beenden oder immer dann, wenn Sie vielversprechende Daten sehen, führt dies zu Verzerrungen.

#### Geeignete Kennzahlen überlegen

Überlegen Sie, welche Verhaltensweisen für die jeweiligen Metriken relevant sind. Interessieren Sie sich für die Verkaufszahlen bei Abos, die nur jahresweise verlängert werden? Oder haben die Kund:innen eine wöchentliche Gewohnheit für das Ereignis, das Sie messen möchten? Überlegen Sie sich, wie lange es dauert, bis die Nutzer ihr Verhalten aufgrund Ihrer Botschaft möglicherweise ändern. Nachdem Sie entschieden haben, wie lange Ihr Experiment laufen soll, achten Sie darauf, dass Sie Ihr Experiment nicht vorzeitig beenden oder die Endergebnisse aufzeichnen, da sonst Ihre Ergebnisse verfälscht werden könnten.

[1]: {% image_buster /assets/img/control_group/control_group1.png %}
[2]: {% image_buster /assets/img/control_group/control_group2.png %}
[4]: {% image_buster /assets/img/control_group/control_group4.png %}
[5]: {% image_buster /assets/img/control_group/control_group5.png %}
[6]: {% image_buster /assets/img/control_group/control_group6.png %}
