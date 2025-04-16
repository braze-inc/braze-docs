---
nav_title: Unterdrückungslisten
article_title: Unterdrückungslisten
page_order: 2.5
page_type: reference
tool: Segments
description: "Auf dieser Seite erfahren Sie, wie Sie Unterdrückungslisten verwenden, um festzulegen, welche Nutzer:innen Ihre Nachrichten nicht erhalten sollen."

---

# Unterdrückungslisten

> Unterdrückungslisten geben Gruppen von Nutzer:innen an, die niemals Nachrichten erhalten werden. Administratoren können dynamische Unterdrückungslisten mit Segmentfiltern erstellen, um eine Nutzer:innen-Gruppe auf die gleiche Weise einzugrenzen, wie Sie es bei der Segmentierung tun würden.

{% alert important %}
Die Unterdrückungslisten befinden sich derzeit in der Beta-Phase. Wenn Sie daran interessiert sind, an dieser Beta-Phase teilzunehmen, wenden Sie sich an Ihren Customer-Success-Manager:in. Während der Beta-Phase können sich die Funktionen noch ändern. Sie können bis zu fünf Unterdrückungslisten gleichzeitig aktiv haben, aber lassen Sie Ihren Customer-Success-Manager wissen, wenn Sie mehr benötigen.
{% endalert %}

## Funktionsweise

Unterdrückungslisten sind dynamisch und gelten automatisch für bestimmte Formen von Messaging, aber Sie können Ausnahmen für ausgewählte Tags festlegen. Wenn die von Ihnen ausgewählten Tags in einer Kampagne oder einem Canvas verwendet werden, gilt diese Unterdrückungsliste nicht für diese Kampagne oder dieses Canvas. Nachrichten aus Kampagnen oder Canvase mit Ausnahme-Tags erreichen weiterhin alle Nutzer:innen der Unterdrückungsliste, die zu Ihren Zielsegmenten gehören.

### Nachrichten, die nicht von Unterdrückungslisten betroffen sind

Im Rahmen der Beta-Phase werden die Unterdrückungslisten nicht auf die folgenden Nachrichtentypen angewendet (mit anderen Worten: Nutzer:innen der Unterdrückungslisten erhalten **weiterhin** Nachrichten, die zu den folgenden gehören):
- Feature-Flags
- Transaktionale Anwendungsfälle
- API Kampagnen
- Per API getriggerte Kampagnen
- API-getriggerte Canvase
- Kampagnen, die durch die Braze API (`/messages` und `/send`) getriggert werden

Sie brauchen für diese Anwendungsfälle keine Tags hinzuzufügen, da die Unterdrückungslisten automatisch nicht für sie gelten. Um eine Gruppe von Nutzern von einer Nachricht innerhalb dieser Anwendungsfälle auszuschließen, müssen Sie ein Targeting-Segment erstellen, das diese Nutzer:innen ausschließt.

{% alert important %}
Während der Beta-Phase sammeln wir das Feedback unserer Kund:in, um unser Produkt zu verbessern. Informieren Sie Ihren Customer-Success-Manager:in, wenn Sie planen, Unterdrückungslisten auf transaktionale Anwendungsfälle anzuwenden.
{% endalert %}

### Von Unterdrückungslisten betroffene Kanäle

Die Unterdrückungslisten sind dynamisch und gelten automatisch für alle folgenden Kanäle (es sei denn, die Kampagne oder der Canvas enthält einen Ausnahme-Tag): 
- SMS
- E-Mail
- Push
- In-App-Nachrichten
- Content-Card
- Banner
- SMS/MMS
- Webhook
- WhatsApp
- LINE

## Unterdrückungslisten einrichten

Da Unterdrückungslisten die von Ihnen gesendeten Nachrichten erheblich beeinflussen können, können nur Administratoren Unterdrückungslisten bearbeiten, speichern, aktivieren und deaktivieren (alle Nutzer:innen können Unterdrückungslisten anzeigen).

1. Gehen Sie zu **Zielgruppe** > **Unterdrückungslisten**.<br><br>![Die Seite "Unterdrückungslisten" mit einer Liste von drei Unterdrückungslisten.][1]<br><br>
2. Wählen Sie **Unterdrückungsliste erstellen** und fügen Sie einen Namen hinzu.<br><br>![Ein Fenster namens "Unterdrückungsliste erstellen" mit einem Feld zur Eingabe eines Namens.][2]{: style="max-width:80%;"}<br><br>
3. Verwenden Sie Segmente-Filter, um die Nutzer:innen in Ihren Unterdrückungslisten zu identifizieren. Sie müssen mindestens eine auswählen.

{% alert important %}
Obwohl der Einrichtungsprozess ähnlich wie bei der [Erstellung von Segmenten]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) aussieht, ist eine Unterdrückungsliste eine Gruppe von Nutzern:innen, an die Sie **keine** Nachrichten senden möchten, unabhängig von der Mitgliedschaft in einem Segment.
{% endalert %}

![Ein Unterdrückungslisten-Builder mit einem Filter für Nutzer:innen, die zuletzt vor mehr als 90 Tagen eine E-Mail geöffnet haben.][3]

{: start="4"}
4\. Legen Sie fest, ob Ausnahmen auf der Basis von Tags gelten sollen, indem Sie das Kästchen unter dem Namen Ihres Segments markieren (weitere Informationen finden Sie unter [Funktionsweise](#how-it-works) ). Fügen Sie dann die Tags von Kampagnen oder Canvase hinzu, die Nutzer:innen in dieser Unterdrückungsliste noch erhalten sollen. <br><br>Mit anderen Worten: Wenn Sie den Ausnahme-Tag "Versandbestätigung" hinzufügen, werden Nutzer:innen von allen Nachrichten ausgeschlossen, die nicht den Tag "Versandbestätigung" verwenden.<br><br>![Der Abschnitt "Versandlistendetails" mit dem Tag "Versandbestätigung", der eine Ausnahme darstellt.][4]<br><br>
5\. Speichern oder aktivieren Sie Ihre Unterdrückungsliste.
- Wenn Sie speichern, wird Ihre Unterdrückungsliste zwar gespeichert, aber nicht aktiviert, d.h. sie wird nicht in Kraft treten. Ihre Unterdrückungsliste bleibt inaktiv, bis Sie sie aktivieren, und inaktive Unterdrückungslisten haben keine Auswirkungen auf das Messaging (Nutzer:innen werden nicht von Nachrichten ausgeschlossen).
- Wenn Sie diese Funktion aktivieren, wird Ihre Unterdrückungsliste gespeichert und tritt sofort in Kraft. Das bedeutet, dass Nutzer:in Ihrer Unterdrückungsliste sofort von Kampagnen oder Canvase ausgeschlossen werden (mit Ausnahme von Kampagnen, die einen Ausnahme-Tag enthalten).

{% alert note %}
Nur Administratoren können Unterdrückungslisten speichern oder aktivieren. In der Beta-Phase können Sie bis zu fünf Unterdrückungslisten gleichzeitig aktiv haben.
{% endalert %}

Sie können Unterdrückungslisten deaktivieren oder archivieren, wenn Sie sie nicht mehr benötigen. 
- Um zu deaktivieren, wählen Sie eine aktive Unterdrückungsliste aus und wählen **Deaktivieren**. Deaktivierte Unterdrückungslisten können später wieder aktiviert werden.
- Um zu archivieren, gehen Sie auf die Seite **Unterdrückungslisten**.

## Verwendung der Unterdrückungsliste

### Für Kampagnen

![Der Bereich "Unterdrückungslisten" mit einer aktiven Unterdrückungsliste namens "Niedrige Marketing Health Scores".][5]

Wenn ein Nutzer:innen in einer Unterdrückungsliste steht, erhält er keine Kampagne, für die diese Unterdrückungsliste gilt. Siehe [Nachrichten, die nicht von Unterdrückungslisten betroffen sind](#messages-not-affected-by-suppression-lists), für Fälle, in denen eine Unterdrückungsliste nicht anwendbar ist.

#### Prüfen, welche Unterdrückungslisten angewendet werden

Um die Verwendung von Unterdrückungslisten innerhalb einer Kampagne zu überprüfen, gehen Sie zum Abschnitt **Unterdrückungsliste** auf der Seite **Zielgruppen**, um zu sehen, welche Unterdrückungslisten auf diese Kampagne angewendet werden.

### Für Canvase

Wenn sich ein Nutzer:innen auf einer Unterdrückungsliste befindet, kann er zwar immer noch den Canvas betreten, aber keine Nachrichten-Schritte innerhalb des Canvas empfangen. Wenn sie einen Nachrichten-Schritt voranbringen, werden sie aus dem Canvas herausgenommen. Nutzer:innen, die sich auf einer Unterdrückungsliste befinden, können jedoch immer noch Schritte empfangen, die keine Nachrichten sind, bevor sie eine Nachricht erhalten. 

#### Verhindern, dass Segmente ein Canvas betreten

Damit ein Segment **überhaupt** nicht in ein Canvas aufgenommen wird, können Sie die Zieleinstellungen dieses Canvas so konfigurieren, dass dieses Segment ausgeschlossen wird. Gehen Sie dazu folgendermaßen vor:

1. Erstellen Sie ein Segment mit denselben Filtern und Kriterien wie Ihre Verdrängungsliste.
2. Im Schritt **Target** verwenden Sie den Filter **Segment Membership**, um Nutzer:innen anzusprechen, die nicht in Ihrem Segment enthalten sind.

Nehmen wir zum Beispiel an, Sie haben ein Canvas mit einer Unterdrückungsliste angelegt. Der Canvas besteht aus einem Nutzer:innen-Update-Schritt gefolgt von einem Nachrichten-Schritt. In diesem Szenario betreten Nutzer:innen der Unterdrückungsliste das Canvas, durchlaufen den Schritt Benutzer:innen aktualisieren (wo der Nutzer je nach Konfiguration dieses Schritts aktualisiert werden kann) und verlassen es dann im Schritt Nachricht (wobei der Nutzer in die Metriken "Verlassen" aufgenommen wird). 

#### Prüfen, welche Unterdrückungslisten angewendet werden

Um die Verwendung von Unterdrückungslisten innerhalb eines Canvas zu überprüfen, gehen Sie zum Abschnitt **Unterdrückungsliste** auf der Seite **Zielgruppe**, um zu sehen, welche Unterdrückungslisten auf diesen Canvas angewendet werden. Sie können die angewandten Unterdrückungslisten auch im Schritt **Zusammenfassung** einsehen.

[1]: {% image_buster /assets/img/suppression_lists_home.png %}
[2]: {% image_buster /assets/img/create_suppression_list.png %}
[3]: {% image_buster /assets/img/suppression_list_filters.png %}
[4]: {% image_buster /assets/img/exception_tags.png %}
[5]: {% image_buster /assets/img/active_suppression_list.png %}
