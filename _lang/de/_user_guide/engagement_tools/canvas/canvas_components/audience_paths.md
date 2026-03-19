---
nav_title: Zielgruppen-Pfade
article_title: Zielgruppenpfade 
alias: /audience_paths/
page_order: 3
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Zielgruppenpfade in Ihrem Canvas verwenden können, um Nutzer:innen in großem Umfang intuitiv zu filtern und zu segmentieren, und zwar mit strategischen, prioritätsbasierten Nutzergruppierungen."
tool: Canvas

---

# Zielgruppenpfade 

> Mit Canvas-Zielgruppenpfaden können Sie Nutzer:innen in großem Umfang intuitiv filtern und segmentieren, und zwar mit strategischen, prioritätsbasierten Nutzergruppierungen. 

Diese Canvas-Komponente ersetzt die Notwendigkeit, übermäßig viele zielgruppenbasierte vollständige Schritte zu erstellen, sodass Sie acht vollständige Komponenten in einer einzigen kombinieren können. So können Sie die Benutzeransprache vereinfachen und gleichzeitig Ihre Canvases von unnötiger Unordnung und Komplexität befreien. 

## Funktionsweise

![Ein Zielgruppen-Pfad mit zwei Gruppen: engagierte Nutzer:innen und alle anderen.]({% image_buster /assets/img/audience_path/audience_path.png %}){: style="float:right;max-width:45%;margin-left:15px;margin-top:15px;"}

Zielgruppenpfade sind vergleichbar mit Sortiertrichtern mit Ranking-Kriterien. Die Benutzer werden für jedes Kriterium in der Reihenfolge ihrer Priorität bewertet und auf den Weg des höchsten Kriteriums geschickt, das sie erfüllen. Dadurch wird die Unklarheit darüber verringert, wohin die Nutzer:innen gehen und welche Nachrichten sie erhalten werden. Beachten Sie, dass die Ranglisten [nach dem Start]({{site.baseurl}}/post-launch_edits/) nicht [mehr geändert werden können]({{site.baseurl}}/post-launch_edits/).

Mit Zielgruppenpfade können Sie Folgendes tun:

- Leiten Sie Benutzer auf der Grundlage von Zielgruppenkriterien auf verschiedene Canvas-Pfade weiter.
- Weisen Sie den verschiedenen Zielgruppen Prioritäten zu, damit Ihre Nachrichten die richtigen Nutzer erreichen. 
  - Zuvor wurden Benutzer, die die Kriterien von zwei möglichen vollständigen Schritten erfüllten, nach dem Zufallsprinzip zugewiesen. 
- Stellen Sie Nutzer:innen in großem Umfang gezielt zusammen.
  - Erstellen Sie bis zu acht Zielgruppen (zwei Standard- und sechs zusätzliche Gruppen) pro Komponente. Sie können jedoch mehrere Schritte für den Zielgruppenpfad miteinander verbinden, um Ihre Nutzer:innen weiter zu sortieren. 

### Wie Nutzer:innen bewertet werden

![Canvas zeigt eine 24-stündige Verzögerung nach einem Nachrichten-Schritt, gefolgt von einem Zielgruppen-Pfad.]({% image_buster /assets/img/audience_path/audience_path5.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Nutzer:innen werden anhand von Filtern und Segmentzugehörigkeit **in dem Moment** bewertet**, in dem sie den Schritt „Zielgruppen-Pfad“ erreichen** – nicht, wenn sie die Canvas betreten haben. Nach der Bewertung werden sie umgehend auf den entsprechenden Pfad weitergeleitet. Wenn ein Nutzer einer Zielgruppe zugeordnet wird, verbleibt er in dieser Gruppe, auch wenn sich sein Nutzerprofil später ändert.

{% alert important %}
Zielgruppen-Pfade werden auf Grundlage der aktuellen Attribute, Filter und Segmentzugehörigkeit einer Nutzer:in zum Zeitpunkt der Auswertung bewertet. Sie bewerten nicht auf der Grundlage des spezifischen Ereignisses, das den Eingang in Canvas getriggert hat. Um Nutzer:innen basierend auf einer von ihnen ausgeführten Aktion (z. B. einem angepassten Event) weiterzuleiten, verwenden Sie bitte stattdessen [Aktions-Pfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/).
{% endalert %}

### Zeit für Nutzer:innen-Bewertungen zulassen

Da die Auswertung unmittelbar erfolgt, ist es wichtig, eine Verzögerung vor dem Zielgruppen-Pfad einzufügen, wenn die Pfadkriterien von einer Benutzerinteraktion mit einem vorherigen Schritt abhängen.

Wenn Nutzern beispielsweise Nachricht A gesendet wird und der nächste Schritt ein Zielgruppen-Pfad ist, der auswertet, ob sie mit dieser Nachricht interagiert haben, gelangen alle Nutzer:innen zu dem Schritt für diejenigen, die nicht mit dieser Nachricht interagiert haben. Das liegt daran, dass die Nutzer:innen sofort zum Schritt Zielgruppen-Pfad übergegangen sind, ohne Zeit für eine Interaktion mit der Nachricht zu haben. Mit anderen Worten: Nutzer:innen werden fast unmittelbar nach dem Versand der Nachricht auf eine Interaktion mit der Nachricht geprüft.

Um den Nutzer:innen Zeit für die Interaktion mit einer gesendeten Nachricht zu geben, fügen Sie bitte eine Verzögerung zwischen dem Schritt „Nachricht“ und dem Zielgruppen-Pfad ein. Beispielsweise gewährt eine Verzögerung von 24 Stunden den Nutzer:innen nach dem Versand der Nachricht 24 Stunden Zeit, um mit Nachricht A zu interagieren, bevor sie bewertet wird.

## Erstellen eines Zielgruppenpfads

Um einen Schritt für einen Zielgruppenpfad hinzuzufügen, gehen Sie wie folgt vor: 

1. Fügen Sie einen Schritt zu Ihrem Canvas hinzu. 
2. Ziehen Sie die Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie <i class="fas fa-plus-circle"></i> **Hinzufügen** am Ende eines Schritts und wählen Sie **Zielgruppen-Pfade**.

Die Standardkomponente für Zielgruppenpfade enthält zwei Standardzielgruppen, **Gruppe 1** und **Alle anderen**. Die Gruppe **"Alle anderen"** umfasst alle Benutzer, die nicht zu einer der definierten Zielgruppen gehören. Diese Gruppe wird immer an letzter Stelle stehen.

### Definieren von Zielgruppen

Der folgende Screenshot zeigt das Layout eines erweiterten Audience Paths-Schrittes. Hier können Sie bis zu acht Hörergruppen definieren (eine voreingestellte und sieben anpassbare). Um eine Zielgruppe zu definieren, wählen Sie den Gruppennamen im Editor „Zielgruppenpfade“ aus. Sie können Ihre Zielgruppengruppe umbenennen, die Filter und Segmente auswählen, die für Ihre Gruppe gelten, und Gruppen hinzufügen oder löschen.

Wenn Sie beispielsweise das Onboarding Messaging auf eine Gruppe von Nutzern ausrichten möchten, könnten Sie Retargeting-Filter auswählen, z. B. "Hat auf E-Mail geklickt" und "Hat auf In-App-Nachrichten geklickt".

![Ein erweiterter Zielgruppen-Pfad mit Gruppen für „Liebhaber asiatischer Küche“, „Liebhaber lateinamerikanischer Küche“, „Liebhaber europäischer Küche“ und „Alle anderen“.]({% image_buster /assets/img/audience_path/audience_path3.png %})

Nachdem der Schritt für Zielgruppenpfade abgeschlossen ist, hat jede Zielgruppe einen eigenen Branch. Sie können mit der Verwendung von Zielgruppenpfaden fortfahren, um Ihr Publikum weiter zu filtern. Alternativ können Sie Ihre Canvas-Journey mit den Standard-Canvas-Schritten fortsetzen. 

![Zwei Zielgruppen-Pfade mit unterschiedlichen Gruppen, basierend auf dem Engagement.]({% image_buster /assets/img/audience_path/audience_path4.png %}){: style="max-width:50%"}

### Testen von Zielgruppen

Nachdem Sie Ihrer Zielgruppe Segmente und Filter hinzugefügt haben, können Sie testen, ob Ihre Zielgruppen wie erwartet eingerichtet sind, indem Sie [nach einem Benutzer suchen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), um zu überprüfen, ob er den Zielgruppenkriterien entspricht.

![Der Abschnitt „Benutzersuche“.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

## Audience Paths verwenden

Die eigentliche Stärke von Zielgruppenpfaden liegt in der Möglichkeit, Prioritäten zu vergeben. Auch wenn diese Funktion nicht strategisch eingesetzt werden muss, kann es vorkommen, dass einige Vermarkter bestimmte Produkte, wie z.B. Sonderangebote oder limitierte Auflagen, an die Nutzer herantragen. 

Indem Sie diesen Gruppen eine hohe Priorität zuweisen, können Sie Nutzer ansprechen, die unter bestimmte Filter und Segmente fallen, und gleichzeitig Nutzer ansprechen, die diese spezifischen Kriterien nicht erfüllen - und das alles in einem einzigen Canvas-Schritt.

![Ein Zielgruppen-Pfad mit Gruppen für "Mag große Markenschuhe", "Mag große Marken" und "Alle anderen".]({% image_buster /assets/img/audience_path/audience_path2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Nehmen wir zum Beispiel an, Sie möchten einer Gruppe von Nutzern Anzeigen für neue Produkte schicken. Sie beginnen damit, dass Sie Filter, die unter diese Produkte fallen, auf dem Audience Path weit oben platzieren. Wenn Sie eine Marketing-Kampagne für das Unternehmen "Big Brand" erstellen und gerade eine neue Einzelhandelsmarke auf den Markt gebracht haben, könnten Sie Filter wie "Likes Big Brand Shoes" oder "Likes Big Brand Bags" auswählen und je nachdem, in welche gefilterte Gruppe diese Personen fallen, unterschiedliche Nachrichten per E-Mail versenden. 

Wenn Nutzer:innen diese Komponente Zielgruppen-Pfade betreten, wird zunächst geprüft, ob sie unter die höchstrangige Zielgruppe fallen: Zielgruppe 1 "Mag große Markenschuhe". Wenn ja, fahren sie mit der nächsten in Ihrem Canvas definierten Komponente fort. Wenn sie "Big Brand Shoes" nicht mögen, werden sie für die nächste Zielgruppe bewertet, Zielgruppe 2 "Likes Big Brand Bags", und fahren mit dem nächsten Schritt fort, wenn die Kriterien erfüllt sind. Nutzer:innen, die nicht in die vorherigen Gruppen fallen, fallen in die Gruppe "Alle anderen" und gehen ebenfalls zum nächsten Canvas-Schritt, den Sie für diesen Pfad definieren.

Sie können die Leistung dieses Schrittes auch mit [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#performance-visualization) sehen.

### Segmentierung von Audience Paths mit zufälligen Bucket-Nummern

Wenn Ihr Canvas ein [Rate-Limit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) verwendet (z. B. eine Begrenzung der Gesamtzahl der Nutzer:innen, die das Canvas erhalten), empfiehlt Braze, dass Sie keine zufälligen Bucket-Nummern zur Segmentierung Ihrer Zielgruppenpfade verwenden. 

Eine [zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) ist ein Benutzerattribut, das verwendet werden kann, um gleichmäßig verteilte Segmente von zufälligen Benutzern zu erstellen. Braze verwendet die zufällige Bucket-Nummer, um Nutzer:innen während der Segmentierungsphase der Canvas-Eingabe zu gruppieren, und jede Gruppe wird separat verarbeitet. Je nachdem, welche Gruppen die Verarbeitung zuerst abschließen, können einige Nutzer:innen aufgrund des Rate-Limits bei der Eingabe gedeckelt werden, was zu einer ungleichmäßigen Verteilung der Nutzer:innen führen kann, wenn sie den Schritt „Zielgruppenpfade“ erreichen.

Versuchen Sie in diesem Fall, stattdessen [Experimentierpfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) zu verwenden.

### Verwenden des Filter „Intelligenter Kanal“ mit Zielgruppenpfaden

Mit einer Kombination aus Zielgruppenpfad-Schritten und „Intelligenter Kanal“-Filtern können Sie Ihr Messaging-Erlebnis auf die Vorlieben und das Verhalten der einzelnen Nutzer:innen abstimmen. Auf diese Weise erhalten Ihre Nutzer:innen die relevantesten Nachrichten über die entsprechenden Kanäle.

In einem Zielgruppenpfad-Schritt können Sie zum Beispiel drei Zielgruppen erstellen: E-Mail, Mobile Push, und Alle anderen. Fügen Sie für die E-Mail-Zielgruppe den Filter `Intelligent Channel is Email` hinzu. Fügen Sie für die Mobile Push-Zielgruppe den Filter `Intelligent Channel is Mobile Push` hinzu. Dann können Sie für jeden der Zielgruppenpfade einen Nachrichtenschritt hinzufügen, um personalisierte und relevante Nachrichten zuzustellen.

{% alert tip %}
In unseren [Braze-Canvas-Templates]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) finden Sie Beispiele dafür, wie Sie diese vorgefertigten Templates zu Ihrem Vorteil anpassen können.
{% endalert %}
