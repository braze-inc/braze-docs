---
nav_title: "Nutzer:in Verwaltung"
article_title: LINE Benutzerverwaltung
page_order: 0
description: "Dieser Artikel befasst sich mit der LINE-Benutzer-ID und wie Sie diese festlegen."
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# LINE Benutzerverwaltung

> Die LINE-Benutzer-ID wird im Benutzerprofil-Attribut `native_line_id` gespeichert, das zum Senden von Nachrichten an einen Benutzer im LINE-Kanal verwendet wird. Dieser Artikel beschreibt, wie Sie das Attribut `native_line_id` einstellen und finden können.

Die Benutzerdaten des Kunden werden in einem [Braze-Benutzerprofil]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) dargestellt. Ein Benutzerprofil speichert Informationen und Attribute über die Benutzer eines Unternehmens, z. B. Vornamen und E-Mail-Adressen. 

Wenn Sie LINE-Nachrichten über Braze versenden, verwendet Braze das Attribut `native_line_id`, um die Nutzer:innen zu identifizieren, an die die Nachricht gesendet werden soll. Wenn LINE Braze-Webhook-Events sendet, z. B. wenn ein:e Nutzer:in einem Kanal folgt oder auf eine Nachricht antwortet, wird die `native_line_id` verwendet, um das entsprechende Nutzerprofil nachzuschlagen.

{% alert note %}
Die LINE-Benutzer-IDs sind je nach LINE-Anbieter unterschiedlich. Ein bestimmter Benutzer hat verschiedene LINE-Benutzer-IDs für jeden Anbieter, dem er folgt. Es ist unwahrscheinlich, dass Benutzer ihre LINE ID kennen (im Gegensatz zu ihrer E-Mail oder Telefonnummer), da sie sich für jede Marke, der sie folgen, ändert.
{% endalert %}

## Einstellen des Attributs `native_line_id`

Es gibt eine Reihe von Szenarien, in denen `native_line_id` auf das Nutzerprofil gesetzt wird, die im Folgenden beschrieben werden.

| Szenario | Ob ein Nutzerprofil mit Nutzer:in existiert `native_line_id` | Ergebnis |
| --- | --- | --- |
|Ein Benutzer folgt einem LINE-Kanal | Kein:e| Ein anonymes Benutzerprofil wird erstellt (eine Zusammenführung ist erforderlich):<br> - `native_line_id` ist auf die LINE ID des Benutzers eingestellt. <br>- `line_id` Nutzer-Alias wird auf die LINE ID der Nutzerin oder des Nutzers gesetzt<br>\- Der Benutzer ist bei der Braze-Abonnementgruppe des Kanals abonniert |
|Ein Benutzer folgt einem LINE-Kanal| Ja | Alle Benutzerprofile mit dem `native_line_id`:<br>\- Sie sind bei der Braze-Abonnementgruppe des Kanals abonniert|
|Unternehmen verwendet Benutzer-CSV-Upload mit einer n`ative_line_id` Spalte| Kein:e| Wenn kein Benutzerprofil für den angegebenen `external_id` oder Benutzer-Alias existiert:<br>- `native_line_id` wird auf den angegebenen Wert gesetzt<br> \- Alle anderen in der CSV-Datei angegebenen Attribute werden im Benutzerprofil festgelegt.|
|Unternehmen verwendet Benutzer-CSV-Upload mit einer `native_line_id` Spalte | Ja | Wenn ein Benutzerprofil für den angegebenen `external_id` oder Benutzer-Alias existiert:<br>- `native_line_id` wird auf den angegebenen Wert gesetzt<br>\- Alle anderen in der CSV-Datei angegebenen Attribute werden im Benutzerprofil festgelegt.<br>\- Mehrere Profile haben das gleiche `native_line_id` |
| Das Unternehmen verwendet den Endpunkt `/users/track` und gibt das Attribut `native_line_id` an. | Kein:e | Wenn kein Nutzerprofil für den angegebenen Nutzer:in existiert[(angegeben durch `external_id`, `user_alias`, `braze_id` oder `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)):<br>- `native_line_id` wird auf den angegebenen Wert gesetzt<br>\- Alle anderen in der Anfrage angegebenen Attribute werden im Benutzerprofil festgelegt |
| Das Unternehmen verwendet den Endpunkt `/users/track` und gibt das Attribut `native_line_id` an. | Ja | Wenn ein Nutzerprofil für den angegebenen Nutzer:in existiert[(angegeben durch `external_id`, `user_alias`, `braze_id` oder `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object/)):<br>- `native_line_id` wird auf den angegebenen Wert gesetzt<br>\- Alle anderen in der Anfrage angegebenen Attribute werden im Benutzerprofil festgelegt<br>\- Mehrere Profile haben das gleiche `native_line_id` |
| Anfrage des Unternehmens an Braze, den Abo-Status zu synchronisieren | Kein:e | Wenn eine LINE ID von LINE zurückgegeben wird, die kein entsprechendes Nutzerprofil in Braze hat, wird ein anonymes Nutzerprofil erstellt:<br>- `native_line_id` ist auf die LINE ID des Benutzers eingestellt.<br>- `line_id` Nutzer-Alias wird auf die LINE ID der Nutzerin oder des Nutzers gesetzt<br>\- Der Benutzer ist bei der Braze-Abonnementgruppe des Kanals abonniert<br><br>Beachten Sie, dass, wenn später ein Benutzer mit der gleichen LINE-ID erstellt wird, es zwar doppelte Benutzer gibt, aber beide den richtigen LINE-Abonnementstatus haben. Die Zusammenlegung von Benutzern kann in diesen Fällen Ihre Benutzerbasis bereinigen. |
| Anfrage des Unternehmens an Braze, den Abo-Status zu synchronisieren | Ja | Wenn eine Benutzer-LINE-ID von LINE zurückgegeben wird, die ein entsprechendes Benutzerprofil in Braze hat:<br>\- Der Benutzer ist bei der Braze-Abonnementgruppe des Kanals abonniert |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

## Die Suche nach dem `native_line_id`

Wenn Sie ein Benutzerprofil im Braze-Dashboard anzeigen, können Sie sehen, ob das Attribut `native_line_id` gesetzt ist, indem Sie zur Registerkarte **Engagement** > **Kontakteinstellungen** > Abschnitt **LINE** gehen.

Wenn die `native_line_id` eingestellt wurde, wird sie unter **LINE User ID** angezeigt. Andernfalls wird es nicht angezeigt.

![Zeile Kontakteinstellungen auf dem Tab Engagement.]({% image_buster /assets/img/line/line_contact_settings.png %}){: style="max-width:50%;"}

