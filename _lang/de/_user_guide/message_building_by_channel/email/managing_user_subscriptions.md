---
nav_title: E-Mail-Abonnements
article_title: E-Mail-Abonnements
page_order: 6
description: "Dieser Referenzartikel behandelt die verschiedenen Abonnementstatus der Benutzer, die Erstellung und Verwaltung von Abonnementgruppen und die Segmentierung von Benutzern auf der Grundlage ihrer Abonnements."
channel:
  - email

---

# E-Mail-Abonnements

> Erfahren Sie mehr über die Abo-Status, wie Sie Abo-Gruppen erstellen und verwalten und wie Sie Nutzer:innen auf der Grundlage ihrer Abos segmentieren können.

Dieses Dokument dient nur zu Informationszwecken. Sie dienen nicht der Rechtsberatung und dürfen auch nicht als solche angesehen werden. Das Versenden von Marketing- und Transaktions-E-Mails kann bestimmten rechtlichen Anforderungen unterliegen. Um sicherzustellen, dass Sie dabei alle für Ihr Unternehmen geltenden Gesetze, Regeln und Vorschriften einhalten, sollten Sie sich von Ihrem Rechtsbeistand und/oder Ihrem Compliance-Team beraten lassen.

## Abo-Status {#subscription-states}

Braze hat drei globale Abo-Status für Nutzer:innen von E-Mails. Diese Zustände lassen Ihre Nachrichten von Nutzer:innen passieren. Nutzer:innen im Zustand `unsubscribed` erhalten beispielsweise keine Nachrichten, die auf `subscribed` oder `opted-in` ausgerichtet sind.

| Status | Definition |
| ----- | ---------- |
| Zugestimmt (Opt-in) | Ein Benutzer hat ausdrücklich bestätigt, dass er E-Mails erhalten möchte. Wir empfehlen ein ausdrückliches Opt-in-Verfahren, um die Zustimmung der Nutzer zum Versand von E-Mails einzuholen. |
| Abonniert | Ein/e Nutzer/in hat sich weder abgemeldet noch ausdrücklich für den Erhalt von E-Mails angemeldet. Dies ist der Standard Abo-Status, wenn ein Nutzerprofil erstellt wird. |
| Abgemeldet | Ein Benutzer hat sich ausdrücklich von Ihren E-Mails abgemeldet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Braze zählt keine Änderungen des Abo-Status für Ihre Datenpunkte, global und um Abo-Gruppen herum.
{% endalert %}

### Abgemeldete E-Mail-Adressen

Braze meldet automatisch jeden Nutzer:innen ab, der sich manuell über eine [angepasste Fußzeile]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer) abmeldet. Wenn der Nutzer:in seine E-Mail Adresse aktualisiert und die Option **Nutzer:innen bei Update der E-Mail abmelden** in der **Sendekonfiguration** aktiviert ist, wird der normale Versand fortgesetzt.

Wenn ein Nutzer:innen eine oder mehrere Ihrer E-Mails als Spam markiert, sendet Braze nur Transaktions-E-Mails an diesen Nutzer:innen. Transaktions-E-Mails referenzieren auf die Option **An alle Nutzer:innen senden, einschließlich abgemeldeter Nutzer**:innen in **Target Audience**.

{% alert tip %}
In unseren [IP-Warming]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)-Best Practices finden Sie Hinweise, wie Sie Ihre Nutzer:innen effektiv erneuern können.
{% endalert %}

### Bounce-E-Mails und ungültige E-Mails

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} 

Wenn eine E-Mail gebounct wird, setzt Braze den Status des Abos des Nutzers:innen nicht automatisch auf "abgemeldet". Wenn eine Adresse "hard bounce" (ungültig oder nicht vorhanden) ist, markiert Braze sie als ungültig und versucht nicht, sie weiter zu senden. Wenn der Nutzer:innen seine E-Mail Adresse ändert, setzt Braze den Versand fort. Braze wiederholt Soft Bounces für 72 Stunden.

### Aktualisierung des Status von E-Mail-Abos

Es gibt vier Möglichkeiten, den Status des E-Mail-Abos eines Nutzers:innen zu aktualisieren:

#### SDK-Integration

Verwenden Sie das Braze-SDK, um den Status des Abos eines Nutzers oder einer Nutzerin zu aktualisieren.

#### REST API

Verwenden Sie den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), um das [Attribut`email_subscribe` ]({{site.baseurl}}/api/objects_filters/user_attributes_object) für einen Nutzer:innen zu aktualisieren.

#### Benutzerprofil

1. Finden Sie den Benutzer über **Benutzer suchen**. 
2. Wählen Sie unter **Engagement** die Option **Abgemeldet**, **Abonniert** oder **Opt-in** aus, um den Status des Abonnent:in zu ändern. 

Falls verfügbar, zeigt das Nutzerprofil auch einen Zeitstempel an, wann das Abo des Nutzers:innen zuletzt geändert wurde.

#### Präferenzzentrum

Fügen Sie das [Preference Center](#email-preference-center) Liquid am Ende Ihrer E-Mails ein, damit die Nutzer:in ein Opt-in oder ein Opt-out entscheiden können. Braze verwaltet Updates des Abo-Status über das Einstellungszentrum.

### Status des E-Mail-Abonnements prüfen

![Benutzerprofil von John Doe, dessen E-Mail-Abonnementstatus auf Abonniert gesetzt ist.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Sie können den Status des E-Mail-Abos eines Nutzers:innen auf folgende Weise überprüfen:

1. **REST API-Export:** Verwenden Sie die Endpunkte [Nutzer:innen nach Segmenten exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) oder [Nutzer:innen nach Bezeichnern exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/), um einzelne Nutzerprofile im JSON-Format zu exportieren.
2. **Benutzerprofil:** Suchen Sie das Profil des Nutzers auf der Seite [Benutzer suchen]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) und wählen Sie dann den Tab **Engagement**, um den Status des Abos eines Nutzers anzuzeigen und manuell zu aktualisieren.

Wenn ein Benutzer seine E-Mail-Adresse aktualisiert, wird sein Abonnementstatus auf abonniert gesetzt, es sei denn, die aktualisierte E-Mail-Adresse existiert bereits an anderer Stelle in einem Braze-Arbeitsbereich.

## Abo-Gruppen

Abo-Gruppen sind Segmentfilter, mit denen Sie Ihre Zielgruppe aus den [globalen Abo-Statusangaben](#subscription-states) weiter eingrenzen können. Sie können bis zu 350 Abonnementgruppen pro Arbeitsbereich hinzufügen. Mit diesen Gruppen können Sie den Endbenutzern detailliertere Abonnementoptionen anbieten.

Nehmen wir zum Beispiel an, Sie versenden mehrere Kategorien von E-Mail-Kampagnen (Werbung, Newsletter oder Produktaktualisierungen). In diesem Fall können Sie Abonnementgruppen verwenden, damit Ihre Kunden von einer einzigen Seite aus auswählen können, welche E-Mail-Kategorien sie abonnieren oder abbestellen möchten, indem Sie ein [E-Mail-Präferenzcenter](#email-preference-center) verwenden. Alternativ können Sie Abonnementgruppen verwenden, um Ihren Kunden die Wahl zu lassen, wie häufig sie E-Mails von Ihnen erhalten möchten, indem Sie Abonnementgruppen für tägliche, wöchentliche oder monatliche E-Mails erstellen.

Verwenden Sie die [Endpunkte für Abo-Gruppen]({{site.baseurl}}/api/endpoints/subscription_groups), um die Abo-Gruppen, die Sie auf dem Braze-Dashboard gespeichert haben, programmatisch auf der Seite **Abo-Gruppen** zu verwalten.

### Erstellen einer Abonnementgruppe

1. Gehen Sie zu **Zielgruppe**:in > Abo-Gruppen-Management **.**
2. Wählen Sie **E-Mail Abo-Gruppe erstellen**. 
3. Geben Sie Ihrer Abo-Gruppe einen Namen und eine Beschreibung.
4. Wählen Sie **Speichern**. 

Alle Abonnementgruppen werden automatisch zu Ihrem Präferenzcenter hinzugefügt.

![Felder, um eine Abonnementgruppe zu erstellen.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmentierung mit einer Abonnementgruppe

Wenn Sie Ihre Segmente erstellen, setzen Sie den Namen der Abo-Gruppe als Filter ein. Damit bestätigen Sie, dass die Benutzer, die sich für Ihre Gruppe entschieden haben, Ihre E-Mails erhalten. Dies eignet sich hervorragend für monatliche Newsletter, Gutscheine, Mitgliedschaftsstufen und mehr.

![Beispiel für das Targeting von Nutzern im Segment "Verfallene Nutzer" mit dem Filter für Nutzer:innen in der Abo-Gruppe "Wöchentliche E-Mails".]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Archivierung von Abonnementgruppen

Archivierte Abonnementgruppen können nicht bearbeitet werden und erscheinen nicht mehr in Segmentfiltern oder in Ihrem Präferenzcenter. Wenn Sie versuchen, eine Gruppe zu archivieren, die als Segmentfilter in einer E-Mail, einer Kampagne oder einem Canvas verwendet wird, erhalten Sie eine Fehlermeldung, die Sie daran hindert, die Gruppe zu archivieren, bis Sie alle Verwendungen der Gruppe entfernen.

Um Ihre Gruppe auf der Seite **Abo-Gruppen** zu archivieren, gehen Sie wie folgt vor:

1. Suchen Sie Ihre Gruppe in der Liste der Abo-Gruppen. 
2. Wählen Sie **Archiv** aus dem Dropdown-Menü <i class="fa-solid fa-ellipsis-vertical"></i>.

Braze verarbeitet keine Statusänderungen für Nutzer:innen in archivierten Gruppen. Wenn Sie z.B. die Abo-Gruppe 1 archivieren, während Alex sie abonniert hat, bleibt Alex "abonniert", auch wenn er auf einen Abmeldelink klickt. Das spielt keine Rolle, da die Abo-Gruppe 1 archiviert ist und Sie mit ihr keine Nachrichten versenden können.

#### Anzeigen der Größe von Abonnementgruppen

Auf der Seite **Abo-Gruppen** können Sie das Diagramm **Abo-Gruppe Zeitreihe** referenzieren, um die Größe der Abo-Gruppe basierend auf der Anzahl der Nutzer:innen über einen bestimmten Zeitraum zu sehen. Diese Größen der Abo-Gruppen stimmen auch mit anderen Bereichen von Braze überein, z. B. mit der Berechnung der Segmentgröße.

![Eine Beispielgrafik „Abo-Gruppe Zeitreihe“ vom 2\. bis 11\. Dezember. Die Grafik zeigt einen Anstieg der Nutzerzahlen um ca. 10 Millionen vom 6\. zum 7.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### Anzeigen von Abonnementgruppen in der Kampagnenanalyse

Auf der Analytics-Seite einer Kampagne sehen Sie die Anzahl der Nutzer:innen, die ihr Abo geändert haben (abonniert oder abgemeldet).

1. Scrollen Sie auf der Seite **Campaign Analytics** für Ihre Kampagne nach unten zum Abschnitt **E-Mail Nachricht Performance**.
2. Wählen Sie den Pfeil unter **Abo-Gruppen** aus, um die Gesamtzahl der Statusänderungen zu sehen, die von Ihren Kund:innen übermittelt wurden.

![Die Seite „E-Mail-Messaging-Performance“ zeigt die Gesamtzahl der von Kund:innen übermittelten Statusänderungen an.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### Überprüfen der E-Mail Abo-Gruppe eines Nutzers:innen

- **Benutzerprofil:** Auf einzelne Benutzerprofile können Sie über das Braze-Dashboard von der Seite [Benutzer suchen]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#access-profiles) aus zugreifen. Hier können Sie Benutzerprofile nach E-Mail-Adresse, Telefonnummer oder externer Benutzer-ID abrufen. Auf dem Tab **Engagement** können Sie auch die E-Mail Abo-Gruppen eines Nutzers:innen einsehen.
- **Braze REST API:** Verwenden Sie den [Endpunkt Abo-Gruppen des Nutzers auflisten]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) oder den [Endpunkt Abo-Gruppenstatus des Nutzers auflisten]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/), um die Abo-Gruppen einzelner Nutzerprofile anzuzeigen. 

## E-Mail-Präferenzzentrum

Mit dem E-Mail-Präferenzcenter können Sie verwalten, welche Nutzer:innen die Newsletter der Abo-Gruppe erhalten. Sie finden es im Dashboard unter **Abo-Gruppen**. Jede Abo-Gruppe, die Sie erstellen, wird zur Liste der Präferenzzentren hinzugefügt. 

Wenn Sie mehr darüber erfahren möchten, wie Sie ein Präferenzzentrum hinzufügen oder anpassen können, lesen Sie den Abschnitt [Präferenzzentrum]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).

## Ändern von E-Mail-Abos {#changing-email-subscriptions}

In den meisten Fällen verwalten die Nutzer:innen ihr E-Mail Abo über Links in den E-Mails, die sie erhalten. Fügen Sie eine rechtskonforme Fußzeile mit einem Link zum Abmelden am Ende jeder E-Mail ein. Wenn Nutzer:innen die Abmelde-URL auswählen, meldet Braze sie ab und zeigt eine Landing Page an, die die Änderung bestätigt. Fügen Sie diesen Liquid-Tag ein: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Wenn ein Nutzer:innen im Einstellungscenter die Option "Von allen oben genannten Arten von E-Mails abmelden" auswählt, setzt Braze seinen globalen E-Mail-Abostatus auf `unsubscribed` und meldet ihn von allen Gruppen ab.

### Benutzerdefinierte Fußzeilen erstellen {#custom-footer}

Wenn Sie die Standard-Fußzeile nicht verwenden möchten, erstellen Sie eine arbeitsbereichsweite, angepasste E-Mail-Fußzeile und fügen Sie diese mit {% raw %}`{{${email_footer}}}`{% endraw %} als Template in jede E-Mail ein.

So müssen Sie nicht für jede E-Mail-Vorlage oder E-Mail-Kampagne eine neue Fußzeile erstellen. Weitere Schritte finden Sie unter [Angepasste E-Mail-Fußzeile]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/).

#### Verwaltung des Abonnementstatus für chinesische IP-Adressen

Wenn Sie mit chinesischen IP-Adressen rechnen, sollten Sie sich nicht nur auf einen Link zum Abmelden verlassen, um `unsubscribed` Listen zu pflegen. Bieten Sie alternative Wege zum Abmelden an, z.B. ein Support-Ticket oder eine E-Mail an die Vertretung des Kunden. 

### Erstellen einer angepassten Seite zum Abmelden

Wenn Nutzer:innen eine URL zum Abmelden auswählen, zeigt Braze eine Standard Landing Page an, die die Änderung bestätigt.

So erstellen Sie eine angepasste Landing Page (anstelle des Standards), die nach dem Abschluss eines Abonnements angezeigt wird:

1. Gehen Sie zu **E-Mail-Einstellungen** > **Seiten und Fußzeilen für Abonnements**.
2. Stellen Sie das HTML für Ihre angepasste Landing Page zur Verfügung. 

Fügen Sie einen Link zum Abmelden ein (z.B. {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}), damit Nutzer:innen sich erneut anmelden können, wenn sie sich versehentlich abgemeldet haben.

![Angepasste Abmeldeseite mit einer Vorschau "Sorry, dass Sie gehen!".]({% image_buster /assets/img/custom_unsubscribe.png %})

### Erstellen einer angepassten Opt-in-Seite

Verwenden Sie eine angepasste Opt-in-Seite, damit Nutzer:innen die Benachrichtigungseinstellungen vor dem Abo bestätigen und kontrollieren können. Diese zusätzliche Kommunikation kann dazu beitragen, dass E-Mail Kampagnen nicht in Spam-Ordnern landen.

1. Gehen Sie zu **Einstellungen** > **E-Mail-Voreinstellungen**.
2. Wählen Sie **Abo-Seiten und Fußzeilen** aus.
3. Passen Sie das Styling im Abschnitt **Benutzerdefinierte Opt-in-Seite** an, um zu sehen, wie Ihre Nutzer:in darauf hingewiesen werden, dass sie abonniert wurden.

Nutzer:innen gelangen über den Tag {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} auf diese Seite.

{% alert tip %}
Verwenden Sie ein Double Opt-in-Verfahren, um die Reichweite zu verbessern. Braze sendet eine zusätzliche E-Mail, in der ein Nutzer:innen die Benachrichtigungseinstellungen über einen Link bestätigt. Nach der Bestätigung ist der Nutzer:innen Opt-in.
{% endalert %}

![Angepasste Opt-in E-Mail mit der Nachricht "Schön, dass Sie immer noch von uns hören wollen".]({% image_buster /assets/img/custom_optin.png %})

## Abos und Kampagnen-Targeting {#subscriptions-and-campaign-targeting}

Standardmäßig stellt Braze Kampagnen mit Push- oder E-Mail-Nachrichten für Nutzer:innen zusammen, die ein Abonnent:in sind oder ein Opt-in haben. Ändern Sie dies in **Target Audience**, indem Sie das Dropdown-Menü neben **An diese Nutzer:innen senden** auswählen **:**.

Braze unterstützt drei Targeting-Stufen:

- Nur Nutzer:innen mit Abo oder angemeldete Nutzer:innen (Standard)
- Nur angemeldete Nutzer:innen.
- Alle Nutzer:innen, einschließlich derer, die sich abgemeldet haben.

{% alert important %}
Es liegt in Ihrer Verantwortung, bei der Verwendung dieser Targeting-Einstellungen alle geltenden [Spam-Gesetze]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) einzuhalten.
{% endalert %}

## Segmentierung nach Benutzerabonnements {#segmenting-by-user-subscriptions}

Verwenden Sie die Filter "E-Mail-Abonnementstatus" und "Push-Abonnementstatus", um Nutzer:innen nach dem Abonnementstatus zu segmentieren.

Verwenden Sie diese Option, um Nutzer:innen, die sich weder angemeldet noch abgemeldet haben, als Zielgruppe zusammenzustellen und ein explizites Opt-in zu fördern. Erstellen Sie ein Segment mit dem Filter "E-Mail/Push-Abonnement Status ist Abonnent" und senden Sie Kampagnen an Nutzer:in, die zwar Abonnent:in sind, aber kein Opt-in haben.

![E-Mail Abo-Status, der als Segmentfilter verwendet wird.]({% image_buster /assets/img_archive/not_optin.png %})

