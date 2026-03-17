---
nav_title: E-Mail-Abonnements
article_title: E-Mail-Abonnements
page_order: 6
description: "Dieser Referenzartikel behandelt die verschiedenen Abonnementstatus der Benutzer, die Erstellung und Verwaltung von Abonnementgruppen und die Segmentierung von Benutzern auf der Grundlage ihrer Abonnements."
channel:
  - email

---

# E-Mail-Abonnements

> Erfahren Sie mehr über den Abonnementstatus von Nutzern, wie Sie Abo-Gruppen erstellen und verwalten und wie Sie Nutzer:innen anhand ihrer Abonnements segmentieren können.

Dieses Dokument dient nur zu Informationszwecken. Sie dienen nicht der Rechtsberatung und dürfen auch nicht als solche angesehen werden. Das Versenden von Marketing- und Transaktions-E-Mails kann bestimmten rechtlichen Anforderungen unterliegen. Um sicherzustellen, dass Sie dabei alle für Ihr Unternehmen geltenden Gesetze, Regeln und Vorschriften einhalten, sollten Sie sich von Ihrem Rechtsbeistand und/oder Ihrem Compliance-Team beraten lassen.

## Abo-Status {#subscription-states}

Braze verfügt über drei globale Abonnementstatus für E-Mail-Nutzer:innen. Diese Zustände steuern den Empfang Ihrer Nachrichten von Nutzer:innen. Beispielsweise erhalten Nutzer:innen im Bundesstaat`unsubscribed` keine Nachrichten, die `opted-in`auf`subscribed`oder ausgerichtet sind.

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

Braze meldet jeden Nutzer:in automatisch ab, der sich manuell über eine [angepasste Fußzeile]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer) abmeldet. Wenn der Nutzer seine E-Mail-Adresse aktualisiert und **die Option „Nutzer:innen bei Aktualisierung ihrer E-Mail-Adresse erneut anmelden“** in **den Versandkonfigurationen** aktiviert ist, wird der normale Versand fortgesetzt.

Sollte ein Nutzer:in eine oder mehrere Ihrer E-Mails als Spam markieren, versendet Braze nur noch Transaktions-E-Mails an diesen Nutzer:in. Transaktions-E-Mails referieren auf die Option **„An alle Nutzer:innen senden, einschließlich abgemeldeter Nutzer:innen“** in **der Zielgruppe**.

{% alert tip %}
In unseren [IP-Warming]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)-Best Practices finden Sie Hinweise, wie Sie Ihre Nutzer:innen effektiv erneuern können.
{% endalert %}

### Bounce-E-Mails und ungültige E-Mails

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} 

Wenn eine E-Mail-Adresse einen Hard Bounce verursacht, setzt Braze den Status des Abos der Nutzer:in nicht automatisch auf „abgemeldet”. Wenn eine Adresse einen Hard Bounce verursacht (ungültig oder nicht existent), kennzeichnet Braze sie als ungültig und unternimmt keine weiteren Versandversuche. Sollte der Nutzer:in seine E-Mail-Adresse ändern, setzt Braze den Versand fort. Braze wiederholt Soft Bounces 72 Stunden lang.

### Aktualisierung des Status von E-Mail-Abos

Es gibt vier Möglichkeiten, den Status des E-Mail-Abos eines Nutzers:innen zu aktualisieren:

#### SDK-Integration

Verwenden Sie das Braze-SDK, um den Status des Abos eines Nutzers oder einer Nutzerin zu aktualisieren.

#### REST API

Verwenden Sie den[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)[Endpunkt,]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) um das[`email_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object)[Attribut]({{site.baseurl}}/api/objects_filters/user_attributes_object) für eine Nutzer:in zu Update.

#### Benutzerprofil

1. Finden Sie den Benutzer über **Benutzer suchen**. 
2. Wählen Sie unter **„Engagement“** **die Option „Abmelden“**, **„Angemeldet“** oder **„Opt-in“**, um den Abonnementstatus der Nutzer:in zu ändern. 

Falls verfügbar, zeigt das Nutzerprofil auch einen Zeitstempel an, wann das Abo des Nutzers:innen zuletzt geändert wurde.

#### Präferenzzentrum

Fügen Sie [das Präferenzcenter](#email-preference-center) Liquid am Ende Ihrer E-Mails ein, damit die Nutzer:innen Opt-in oder Opt-out durchführen können. Braze verwaltet Updates des Abonnementstatus über das Einstellungscenter.

### Status des E-Mail-Abonnements prüfen

![Benutzerprofil von John Doe, dessen E-Mail-Abonnementstatus auf Abonniert gesetzt ist.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Sie können den Status des E-Mail-Abonnements eines Nutzers auf folgende Weise überprüfen:

1. **REST API-Export:** Verwenden Sie die Endpunkte [Nutzer:innen nach Segmenten exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) oder [Nutzer:innen nach Bezeichnern exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/), um einzelne Nutzerprofile im JSON-Format zu exportieren.
2. **Benutzerprofil:** Suchen Sie das Profil des Nutzers auf der Seite [Benutzer suchen]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) und wählen Sie dann den Tab **Engagement**, um den Status des Abos eines Nutzers anzuzeigen und manuell zu aktualisieren.

Wenn ein Benutzer seine E-Mail-Adresse aktualisiert, wird sein Abonnementstatus auf abonniert gesetzt, es sei denn, die aktualisierte E-Mail-Adresse existiert bereits an anderer Stelle in einem Braze-Arbeitsbereich.

## Abo-Gruppen

Abo-Gruppen sind Segmentfilter, mit denen Sie Ihre Zielgruppe aus den [globalen Abo-Statusangaben](#subscription-states) weiter eingrenzen können. Sie können bis zu 350 Abonnementgruppen pro Arbeitsbereich hinzufügen. Mit diesen Gruppen können Sie den Endbenutzern detailliertere Abonnementoptionen anbieten.

Nehmen wir zum Beispiel an, Sie versenden mehrere Kategorien von E-Mail-Kampagnen (Werbung, Newsletter oder Produktaktualisierungen). In diesem Fall können Sie Abonnementgruppen verwenden, damit Ihre Kunden von einer einzigen Seite aus auswählen können, welche E-Mail-Kategorien sie abonnieren oder abbestellen möchten, indem Sie ein [E-Mail-Präferenzcenter](#email-preference-center) verwenden. Alternativ können Sie Abonnementgruppen verwenden, um Ihren Kunden die Wahl zu lassen, wie häufig sie E-Mails von Ihnen erhalten möchten, indem Sie Abonnementgruppen für tägliche, wöchentliche oder monatliche E-Mails erstellen.

Verwenden Sie die [Endpunkte für Abo-Gruppen]({{site.baseurl}}/api/endpoints/subscription_groups), um die Abo-Gruppen, die Sie auf dem Braze-Dashboard gespeichert haben, programmatisch auf der Seite **Abo-Gruppen** zu verwalten.

### Erstellen einer Abonnementgruppe

1. Bitte gehen Sie zu **„Zielgruppe“** > **„Verwaltung der Abo-Gruppen**“.
2. Wählen Sie **E-Mail Abo-Gruppe erstellen**. 
3. Geben Sie Ihrer Abo-Gruppe einen Namen und eine Beschreibung.
4. Wählen Sie **Speichern**. 

Alle Abonnementgruppen werden automatisch zu Ihrem Präferenzcenter hinzugefügt.

![Felder, um eine Abonnementgruppe zu erstellen.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmentierung mit einer Abonnementgruppe

Wenn Sie Ihre Segmente erstellen, setzen Sie den Namen der Abo-Gruppe als Filter ein. Damit bestätigen Sie, dass die Benutzer, die sich für Ihre Gruppe entschieden haben, Ihre E-Mails erhalten. Dies eignet sich hervorragend für monatliche Newsletter, Gutscheine, Mitgliedschaftsstufen und mehr.

![Beispiel für das Targeting von Nutzer:innen im Segment „Inaktive Nutzer:innen“ mit dem Filter für Nutzer:innen in der Abo-Gruppe „Wöchentliche E-Mails“.]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Archivierung von Abonnementgruppen

Archivierte Abonnementgruppen können nicht bearbeitet werden und erscheinen nicht mehr in Segmentfiltern oder in Ihrem Präferenzcenter. Wenn Sie versuchen, eine Gruppe zu archivieren, die als Segmentfilter in einer E-Mail, einer Kampagne oder einem Canvas verwendet wird, erhalten Sie eine Fehlermeldung, die Sie daran hindert, die Gruppe zu archivieren, bis Sie alle Verwendungen der Gruppe entfernen.

Um Ihre Gruppe auf der Seite **Abo-Gruppen** zu archivieren, gehen Sie wie folgt vor:

1. Suchen Sie Ihre Gruppe in der Liste der Abo-Gruppen. 
2. Wählen Sie **Archiv** aus dem Dropdown-Menü <i class="fa-solid fa-ellipsis-vertical"></i>.

Braze verarbeitet keine Statusänderungen für Nutzer:innen in archivierten Gruppen. Wenn Sie beispielsweise die Abo-Gruppe 1 archivieren, während Alex diese abonniert hat, bleibt Alex weiterhin „abonniert“, auch wenn er auf einen Link zum Abmelden klickt. Dies ist nicht von Bedeutung, da die Abo-Gruppe 1 archiviert ist und Sie keine Nachrichten über diese Gruppe versenden können.

#### Anzeigen der Größe von Abonnementgruppen

Auf der Seite **Abo-Gruppen** können Sie das Diagramm **Abo-Gruppe Zeitreihe** referenzieren, um die Größe der Abo-Gruppe basierend auf der Anzahl der Nutzer:innen über einen bestimmten Zeitraum zu sehen. Diese Größen der Abo-Gruppen stimmen auch mit anderen Bereichen von Braze überein, z. B. mit der Berechnung der Segmentgröße.

![Eine Beispielgrafik „Abo-Gruppe Zeitreihe“ vom 2\. bis 11\. Dezember. Die Grafik zeigt einen Anstieg der Nutzerzahlen um ca. 10 Millionen vom 6\. zum 7.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### Anzeigen von Abonnementgruppen in der Kampagnenanalyse

Auf der Analytics-Seite einer bestimmten E-Mail-Kampagne können Sie die Anzahl der Nutzer:innen einsehen, die ihren Abonnementstatus (abonniert oder abgemeldet) geändert haben.

1. Scrollen Sie auf der Seite **Campaign Analytics** für Ihre Kampagne nach unten zum Abschnitt **E-Mail Nachricht Performance**.
2. Wählen Sie den Pfeil unter **Abo-Gruppen** aus, um die Gesamtzahl der Statusänderungen zu sehen, die von Ihren Kund:innen übermittelt wurden.

![Die Seite „E-Mail-Messaging-Performance“ zeigt die Gesamtzahl der von Kund:innen übermittelten Statusänderungen an.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### Überprüfung der E-Mail-Abo-Gruppe eines Nutzers

- **Benutzerprofil:** Auf einzelne Benutzerprofile können Sie über das Braze-Dashboard von der Seite [Benutzer suchen]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#access-profiles) aus zugreifen. Hier können Sie Benutzerprofile nach E-Mail-Adresse, Telefonnummer oder externer Benutzer-ID abrufen. Sie können die E-Mail-Abo-Gruppen eines Nutzers auch auf der Registerkarte **„Engagement“** einsehen.
- **Braze REST API:** Verwenden Sie den [Endpunkt „Abo-Gruppen des Nutzers auflisten“]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) oder [den Endpunkt „Abo-Gruppenstatus des Nutzers auflisten“,]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) um die Abo-Gruppen des Nutzerprofils anzuzeigen. 

## E-Mail-Präferenzzentrum

Über das E-Mail-Einstellungscenter können Sie verwalten, welche Nutzer:innen Newsletter von Abo-Gruppen erhalten. Sie finden es im Dashboard unter **„Abo-Gruppen**“. Jede Abo-Gruppe, die Sie erstellen, wird zur Liste der Präferenzzentren hinzugefügt. 

Wenn Sie mehr darüber erfahren möchten, wie Sie ein Präferenzzentrum hinzufügen oder anpassen können, lesen Sie den Abschnitt [Präferenzzentrum]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).

## Ändern von E-Mail-Abos {#changing-email-subscriptions}

In den meisten Fällen verwalten Nutzer:innen ihr E-Mail-Abo über Links, die in den erhaltenen E-Mails enthalten sind. Fügen Sie am Ende jeder E-Mail eine rechtskonforme Fußzeile mit einem Link zum Abmelden ein. Wenn Nutzer:innen die Abmelde-URL auswählen, melden sich Braze ab und zeigen eine Landing Page an, auf der die Änderung bestätigt wird. Bitte fügen Sie diesen Liquid-Tag ein: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Wenn eine Nutzer:in im Einstellungscenter „Alle oben genannten Arten von E-Mails abmelden“ auswählt, setzt Braze seinen globalen E-Mail-Abo-Status auf`unsubscribed`„Aus“ und meldet sie von allen Abo-Gruppen ab.

### Benutzerdefinierte Fußzeilen erstellen {#custom-footer}

Sollten Sie die Standard-Fußzeile nicht verwenden wollen, erstellen Sie bitte eine angepasste E-Mail-Fußzeile für den gesamten Workspace und fügen Sie diese mithilfe von einem Template {% raw %}`{{${email_footer}}}`{% endraw %}in jede E-Mail ein.

Dadurch können Sie vermeiden, für jedes E-Mail-Template oder jede E-Mail-Kampagne eine neue Fußzeile zu erstellen. Die einzelnen Schritte finden Sie unter [Benutzerdefinierte E-Mail-Fußzeile]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/).

#### Verwaltung des Abonnementstatus für chinesische IP-Adressen

Wenn Sie chinesische IP-Adressen erwarten, verlassen Sie sich bei der Pflege`unsubscribed`von Listen nicht ausschließlich auf einen Link zum Abmelden. Bitte stellen Sie alternative Möglichkeiten zum Abmelden zur Verfügung, wie beispielsweise ein Support-Ticket oder eine E-Mail-Adresse des Kundendienstes. 

### Erstellen einer angepassten Seite zum Abmelden

Wenn Nutzer:innen eine URL zum Abmelden auswählen, zeigt Braze eine Standard-Landingpage an, auf der die Änderung bestätigt wird.

Um eine angepasste Landing Page (anstelle der Standardseite) zu erstellen, die nach der Anmeldung angezeigt wird:

1. Gehen Sie zu **E-Mail-Einstellungen** > **Seiten und Fußzeilen für Abonnements**.
2. Stellen Sie das HTML für Ihre angepasste Landing Page zur Verfügung. 

Fügen Sie einen Link zum erneuten Abonnieren hinzu (z. B. {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}), damit Nutzer:innen sich erneut anmelden können, falls sie sich versehentlich abgemeldet haben.

![Angepasste Abmeldeseite mit einer Vorschau „Sorry, wir bedauern Ihr Ausscheiden“.]({% image_buster /assets/img/custom_unsubscribe.png %})

### Erstellen einer angepassten Opt-in-Seite

Verwenden Sie eine angepasste Opt-in-Seite, auf der Nutzer:innen vor dem Abonnement ihre Benachrichtigungseinstellungen bestätigen und steuern können. Diese zusätzliche Kommunikation kann dazu beitragen, dass E-Mail-Kampagnen nicht in Spam-Ordnern landen.

1. Gehen Sie zu **Einstellungen** > **E-Mail-Voreinstellungen**.
2. Wählen Sie **Abo-Seiten und Fußzeilen** aus.
3. Passen Sie das Styling im Abschnitt **Benutzerdefinierte Opt-in-Seite** an, um zu sehen, wie Ihre Nutzer:in darauf hingewiesen werden, dass sie abonniert wurden.

Nutzer:innen gelangen über den{% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}Tag auf diese Seite.

{% alert tip %}
Bitte verwenden Sie ein Double-Opt-in-Verfahren, um die Reichweite zu verbessern. Braze versendet eine zusätzliche Bestätigungs-E-Mail, in der der Nutzer:in seine Benachrichtigungseinstellungen über einen Link bestätigen kann. Nach der Bestätigung ist der Nutzer:in Opt-in.
{% endalert %}

![Individuell angepasste Opt-in-E-Mail mit der Nachricht „Wir freuen uns, dass Sie weiterhin von uns hören möchten“.]({% image_buster /assets/img/custom_optin.png %})

## Abos und Kampagnen-Targeting {#subscriptions-and-campaign-targeting}

Standardmäßig richtet Braze Kampagnen mit Push- oder E-Mail-Nachrichten an Nutzer:innen, die sich angemeldet oder für den Erhalt von E-Mails zugestimmt haben. Bitte ändern Sie dies in **der Zielgruppe,** indem Sie das Dropdown-Menü neben **„An diese Nutzer:innen senden:**“ auswählen****.

Braze unterstützt drei Targeting-Stufen:

- Nur Nutzer:innen mit Abo oder angemeldete Nutzer:innen (Standard)
- Nur angemeldete Nutzer:innen.
- Alle Nutzer:innen, einschließlich derer, die sich abgemeldet haben.

{% alert important %}
Es liegt in Ihrer Verantwortung, bei der Verwendung dieser Targeting-Einstellungen alle geltenden [Spam-Gesetze]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) einzuhalten.
{% endalert %}

## Segmentierung nach Benutzerabonnements {#segmenting-by-user-subscriptions}

Verwenden Sie die Filter „E-Mail-Abo-Status“ und „Push-Abo-Status“, um Nutzer:innen nach ihrem Abo-Status zu segmentieren.

Verwenden Sie diese Option, um eine Zielgruppe zusammenzustellen, die weder ein Opt-in noch eine Abmeldung vorgenommen hat, und ermutigen Sie sie zu einem ausdrücklichen Opt-in. Erstellen Sie ein Segment mit dem Filter „E-Mail-/Push-Abonnementstatus ist abonniert“ und versenden Sie Kampagnen an Nutzer:innen, die abonniert sind, aber nicht zum Opt-in zugestimmt haben.

![E-Mail Abo-Status, der als Segmentfilter verwendet wird.]({% image_buster /assets/img_archive/not_optin.png %})

