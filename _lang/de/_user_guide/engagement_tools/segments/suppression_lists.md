---
nav_title: Unterdrückungslisten
article_title: Unterdrückungslisten
page_order: 3
page_type: reference
tool: Segments
description: "Auf dieser Seite erfahren Sie, wie Sie Unterdrückungslisten verwenden, um festzulegen, welche Nutzer:innen Ihre Nachrichten nicht erhalten sollen."

---

# Unterdrückungslisten

> Unterdrückungslisten sind Gruppen von Nutzer:innen, die automatisch keine Kampagnen oder Canvase erhalten. Unterdrückungslisten werden durch Segmente definiert, und Nutzer:innen betreten und verlassen Unterdrückungslisten, wenn sie die Filterkriterien erfüllen. Sie können auch Ausnahme-Tags festlegen, so dass die Unterdrückungsliste nicht für Kampagnen oder Canvase mit diesen Tags gilt. Nachrichten aus Kampagnen oder Canvase mit Ausnahme-Tags erreichen weiterhin Nutzer:innen der Unterdrückungsliste, die sich in den Zielsegmenten befinden.

## Warum Unterdrückungslisten verwenden?

Die Unterdrückungslisten sind dynamisch und gelten automatisch für alle Arten von Messaging, aber Sie können Ausnahmen für ausgewählte Tags festlegen. Wenn die von Ihnen ausgewählten Tags in einer Kampagne oder einem Canvas verwendet werden, gilt diese Unterdrückungsliste nicht für diese Kampagne oder dieses Canvas. Nachrichten aus Kampagnen oder Canvase mit Ausnahme-Tags erreichen weiterhin alle Nutzer:innen der Unterdrückungsliste, die zu Ihren Zielsegmenten gehören.

### Von Unterdrückungslisten betroffene Nachrichtentypen und Kanäle

Die Unterdrückungslisten gelten für alle Nachrichtentypen und Kanäle mit Ausnahme von [Feature-Flags]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/). Das bedeutet, dass Unterdrückungslisten standardmäßig für alle Kanäle, Kampagnen und Canvase gelten, einschließlich:
- [API Kampagnen]({{site.baseurl}}/api/api_campaigns/)
- API-getriggerte Kampagnen und Canvase
- [Transaktions-E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/)

Der einzige Nachrichtentyp, für den die Unterdrückungslisten nicht gelten, sind Feature-Flags. Nutzer:innen in einer Unterdrückungsliste werden zwar nicht von Feature-Flags, aber von allen anderen Kanälen unterdrückt. 

Sie können Ausnahme-Tags verwenden, so dass Nutzer:innen der Unterdrückungsliste dennoch durch bestimmte Kampagnen und Canvase targetiert werden. Einzelheiten finden Sie in Schritt 4 unter [Einrichten von Unterdrückungslisten](#setup). Wenn Sie keine Ausnahme-Tags zu einer Unterdrückungsliste hinzufügen, werden Nutzer:innen in dieser Unterdrückungsliste nicht mit Nachrichten außer Feature-Flags angesprochen. 

{% alert note %}
Unterdrückungslisten werden auf API Kampagnen angewendet, die im Braze-Dashboard mit einem `campaign_id` erstellt werden. Unterdrückungslisten gelten nicht für Nachrichten, die über [Messaging-Endpunkte von Braze]({{site.baseurl}}/api/endpoints/messaging/) ohne einen zugehörigen `campaign_id` gesendet werden.
{% endalert %}

![Der Abschnitt "Ausnahmeeinstellungen" mit einem Kontrollkästchen, um die Unterdrückungsliste nicht auf API-getriggerte Kampagnen und Canvase anzuwenden.]({% image_buster /assets/img/suppression_list_checkbox.png %}){: style="max-width:70%;"}

## Unterdrückungslisten einrichten {#setup}

{% alert note %}
Alle Nutzer:innen können Unterdrückungslisten einsehen, aber nur Nutzer:innen mit [Admin-Rechten]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=admin#list-of-permissions) können Unterdrückungslisten erstellen und verwalten.
{% endalert %}

1. Gehen Sie zu **Zielgruppe** > **Unterdrückungslisten**.<br><br>![Die Seite "Unterdrückungslisten" mit einer Liste von drei Unterdrückungslisten.]({% image_buster /assets/img/suppression_lists_home.png %})<br><br>
2. Wählen Sie **Unterdrückungsliste erstellen** und fügen Sie einen Namen hinzu.<br><br>![Ein Fenster namens "Unterdrückungsliste erstellen" mit einem Feld zur Eingabe eines Namens.]({% image_buster /assets/img/create_suppression_list.png %}){: style="max-width:80%;"}<br><br>
3. Verwenden Sie Segmente-Filter, um die Nutzer:innen in Ihren Unterdrückungslisten zu identifizieren. Sie müssen mindestens eine auswählen.

{% alert important %}
Obwohl der Einrichtungsprozess ähnlich wie bei der [Erstellung von Segmenten]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) aussieht, ist eine Unterdrückungsliste eine Gruppe von Nutzern:innen, an die Sie **keine** Nachrichten senden möchten, unabhängig von der Mitgliedschaft in einem Segment.
{% endalert %}

![Ein Unterdrückungslisten-Builder mit einem Filter für Nutzer:innen, die zuletzt vor mehr als 90 Tagen eine E-Mail geöffnet haben.]({% image_buster /assets/img/suppression_list_filters.png %})

{: start="4"}
4\. Legen Sie fest, ob Sie Ausnahmen auf der Grundlage von Tags haben möchten, indem Sie das Kästchen unter dem Namen Ihres Segments markieren (weitere Informationen finden Sie unter [Warum Unterdrückungslisten?](#why-use-suppression-lists) ). Fügen Sie dann die Tags von Kampagnen oder Canvase hinzu, die Nutzer:innen in dieser Unterdrückungsliste noch erhalten sollen. <br><br>Mit anderen Worten: Wenn Sie den Ausnahme-Tag "Versandbestätigung" hinzufügen, werden Nutzer:innen von allen Nachrichten ausgeschlossen, die nicht den Tag "Versandbestätigung" verwenden.<br><br>![Der Abschnitt "Versandlistendetails" mit dem Tag "Versandbestätigung", der eine Ausnahme darstellt.]({% image_buster /assets/img/exception_tags.png %})<br><br>
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

Um zu überprüfen, ob Ihre Unterdrückungsliste verhindert hat, dass ein Nutzer:innen eine Nachricht erhält, verwenden Sie **User Lookup** im Schritt **Target Audience** innerhalb Ihrer Kampagne oder Canvas. Hier können Sie sehen, zu welcher Unterdrückungsliste sie gehören.

!["User Lookup"-Fenster, das anzeigt, dass ein Nutzer:innen in einer Unterdrückungsliste steht.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

{% alert tip %}
Sie können die angewandten Unterdrückungslisten auch im Schritt **Zusammenfassung** finden.
{% endalert %}

Verwenden Sie bei der Erstellung einer Kampagne oder eines Canvas die **Benutzersuche** im Schritt **Target Audience**, um nach einem Nutzer:innen zu suchen, und wenn dieser nicht zur Zielgruppe gehört, können Sie die Unterdrückungsliste sehen, zu der er gehört. 

!["User Lookup"-Fenster, das anzeigt, dass ein Nutzer:innen in einer Unterdrückungsliste steht.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

### Kampagne 

Wenn ein Nutzer:innen in einer Unterdrückungsliste steht, erhält er keine Kampagne, für die diese Unterdrückungsliste gilt. Siehe [Nachrichtentypen und Kanäle, die von Unterdrückungslisten betroffen sind](#message-types-and-channels-affected-by-suppression-lists), für Fälle, in denen eine Unterdrückungsliste nicht gilt.

![Der Abschnitt "Unterdrückungslisten" mit einer aktiven Unterdrückungsliste namens "Niedrige Marketing-Gesundheitswerte".]({% image_buster /assets/img/active_suppression_list.png %})

### Canvas 

Sobald ein Nutzer:innen zu einer Unterdrückungsliste hinzugefügt wird, wird er keine Canvase mehr betreten. Wenn sie bereits einen Canvas eingegeben haben, erhalten sie keine Nachrichten-Schritte. Das bedeutet, dass ein Nutzer:innen, der sich bereits in einem Canvas befindet, wenn er zu einer Unterdrückungsliste hinzugefügt wird, den Canvas bis zum nächsten Canvas-Schritt voranbringt und ihn dann verlässt, ohne die Nachricht zu erhalten. 

Nehmen wir zum Beispiel an, ein Canvas hat einen Nutzer:innen-Update-Schritt gefolgt von einem Nachrichten-Schritt. Wenn ein Nutzer:innen in den Canvas eintritt und dann zu einer Unterdrückungsliste hinzugefügt wird, durchläuft dieser Nutzer:innen weiterhin den Schritt Benutzer-Update (wo er möglicherweise aktualisiert wird) und verlässt dann den Schritt Nachricht, woraufhin er in die verlassenen Metriken aufgenommen wird.
