{% if include.section == "SDK requirements" %}

## Voraussetzungen

### Minimale SDK-Versionen

Nachrichten, die mit dem Drag-and-Drop-Editor erstellt wurden, können nur an Nutzer:innen mit den folgenden mindestens erforderlichen SDK-Versionen gesendet werden. Weitere Informationen finden Sie unter [Erstellen einer In-App-Nachricht per Drag-and-Drop: Voraussetzungen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites).

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### SDK-Versionen für Textlinks

Um Textlinks einzubinden, die die Nachricht nicht beenden, sind die folgenden SDK-Mindestversionen erforderlich:

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
Wenn Sie in Ihrer In-App-Nachricht einen Link einfügen, der zu einer URL weiterleitet, und der Nutzer:innen nicht über die angegebenen SDK-Mindestversionen verfügt, wird die Nachricht durch einen Klick auf den Link geschlossen, und der Nutzer:innen kann nicht zur Nachricht zurückkehren, um das Formular abzuschicken.
{% endalert %}

{% endif %}

{% if include.section == "message style" %}

Bevor Sie mit dem Anpassen Ihres Templates beginnen, können Sie über das Seitenmenü Stile auf Nachrichtenebene für die gesamte Nachricht festlegen. Vielleicht möchten Sie zum Beispiel die Schriftart des gesamten Textes oder die Farbe aller Links in Ihrer Nachricht anpassen. Sie können die Nachricht auch als Modal oder im Vollbildmodus anzeigen.

{% endif %}


<!-- Add this below after the disclaimers are added to all email sign-up templates: "We have provided a placeholder disclaimer in the template solely as an example, but this should not be relied upon for compliance purposes."-->

{% if include.section == "email disclaimer" %}

Wir empfehlen Ihnen, in Ihre Nachricht eine Opt-in-Sprache und Links zu den Datenschutzrichtlinien und Geschäftsbedingungen Ihrer Marke aufzunehmen. Arbeiten Sie unbedingt mit Ihrer Rechtsabteilung zusammen, um eine Sprache zu entwickeln, die auf Ihre spezifische Marke zugeschnitten ist.

{% alert note %}
Unsere Empfehlung lautet, immer die ausdrückliche Zustimmung zum Versand von E-Mails einzuholen und den Nutzer:innen die Möglichkeit zu geben, die Zustellbarkeit abzulehnen.
{% endalert %}

{% endif %}

{% if include.section == "email validation" %}

Wenn der oder die Nutzer:in eine E-Mail-Adresse eingibt, die nicht akzeptierte Sonderzeichen enthält, wird eine allgemeine Fehlermeldung angezeigt und das Formular kann nicht gesendet werden. Diese Fehlermeldung ist nicht anpassbar. Sie können das Fehlerverhalten auf der Registerkarte **Vorschau & Test** und auf Ihrem Testgerät sehen. Erfahren Sie mehr darüber, wie Braze E-Mail-Adressen unter [E-Mail-Validierung]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/) formatiert.

{% endif %}

{% if include.section == "email double opt-in" %}

### Doppelte Opt-in-Verifizierung

Um sicher zu gehen, dass jeder, der sich in Ihre Liste eingetragen hat, dies auch wirklich beabsichtigt und die richtige E-Mail-Adresse angegeben hat, empfehlen wir Ihnen, von jedem, der sich über Ihr E-Mail-Anmeldeformular eingetragen hat, eine zweite Bestätigung einzuholen, indem Sie einen [Double Opt-in](https://www.braze.com/resources/articles/embracing-the-email-double-opt-in) Flow versenden.

Canvas Flow ist eine Möglichkeit, dies einzurichten:

1. Erstellen Sie ein Canvas, das auf Aktionen basiert, und richten Sie es so ein, dass es ausgelöst wird, wenn ein Nutzer:innen eine E-Mail Adresse zu Braze hinzufügt. Stellen Sie sicher, dass Sie auch Nutzer:innen ansprechen können, die neu auf der Plattform sind (z. B. indem Sie ein Segment ohne Filter im Canvas verwenden).
2. Erstellen Sie einen Schritt für eine E-Mail Nachricht mit einem CTA, der einen Hyperlink zu dem {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} Liquid-Tag enthält. Dadurch wird der Status des E-Mail-Abonnements des Nutzers oder der Nutzerin in `opted_in` geändert, wenn er oder sie auf die Schaltfläche klickt.
3. Fügen Sie einen [Aktions-Pfade Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-paths) hinzu.
4. Für den ersten Pfad lösen Sie eine E-Mail aus, wenn ein:e Nutzerin den jeweiligen E-Mail-Abonnementstatus in `opted_in` ändert. Diese E-Mail sollte Nutzer:innen darüber informieren, dass ihre E-Mail bestätigt wurde.
5. Richten Sie den anderen Pfad ein, um den Canvas zu verlassen, nachdem das Fenster abgelaufen ist.

{% endif %}

{% if include.section == "reporting" %}

Nachdem Ihre Kampagne gestartet ist, können Sie die Ergebnisse in Realtime analysieren, um zu sehen, wie viele Nutzer:innen sich mit Ihrer Kampagne beschäftigt haben. Um zu sehen, wie viele Nutzer sich für die Abo-Gruppe entschieden haben, können Sie [ein Segment von Nutzern erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), die die Abo-Gruppe abonniert haben, indem Sie nach Nutzern filtern, die die In-App-Nachricht erhalten und das Formular abgeschickt haben.

{% endif %}