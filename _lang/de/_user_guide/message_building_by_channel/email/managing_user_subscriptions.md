---
nav_title: E-Mail-Abonnements
article_title: E-Mail-Abonnements
page_order: 6
description: "Dieser Referenzartikel behandelt die verschiedenen Abonnementstatus der Benutzer, die Erstellung und Verwaltung von Abonnementgruppen und die Segmentierung von Benutzern auf der Grundlage ihrer Abonnements."
channel:
  - email

---

# E-Mail-Abonnements

> Erfahren Sie mehr über die verschiedenen Abonnementstatus der Benutzer, wie Sie Abonnementgruppen erstellen und verwalten und wie Sie Benutzer auf der Grundlage ihrer Abonnements segmentieren können.

Dieses Dokument dient nur zu Informationszwecken. Sie dienen nicht der Rechtsberatung und dürfen auch nicht als solche angesehen werden. Das Versenden von Marketing- und Transaktions-E-Mails kann bestimmten rechtlichen Anforderungen unterliegen. Um sicherzustellen, dass Sie dabei alle für Ihr Unternehmen geltenden Gesetze, Regeln und Vorschriften einhalten, sollten Sie sich von Ihrem Rechtsbeistand und/oder Ihrem Compliance-Team beraten lassen.

## Abo-Status {#subscription-states}

Braze verfügt über drei globale Abo-Status für E-Mail-Nutzer:innen (in der folgenden Tabelle aufgeführt), die die endgültigen Gatekeeper zwischen Ihren Nachrichten und Ihren Nutzer:innen sind. Nutzer:innen, die als `unsubscribed` gelten, erhalten zum Beispiel keine Nachrichten, die auf den globalen Abo-Status `subscribed` oder `opted-in` ausgerichtet sind.

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

Braze meldet jeden Benutzer, der sich manuell von Ihrer E-Mail abmeldet, automatisch über eine [benutzerdefinierte Fußzeile]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer) ab. Wenn der Benutzer seine E-Mail-Adresse aktualisiert und die Option **Benutzer bei Aktualisierung der E-Mail-Adresse erneut anmelden** in den Einstellungen für **die Sendekonfiguration** aktiviert ist, wird der normale E-Mail-Versand wieder aufgenommen.

Wenn ein Benutzer eine oder mehrere Ihrer E-Mails als Spam markiert hat, sendet Braze nur Transaktions-E-Mails an diesen Benutzer. In diesem Fall referenzieren Transaktions-E-Mails auf die im Schritt **Targeting** ausgewählte Option **An alle Nutzer:innen senden, auch an nicht abgemeldete Nutzer:innen**.

{% alert tip %}
In unseren [IP-Warming]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)-Best Practices finden Sie Hinweise, wie Sie Ihre Nutzer:innen effektiv erneuern können.
{% endalert %}

### Bounce-E-Mails und ungültige E-Mails

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} 

Wenn eine E-Mail Adresse hart gebounct wird, wird der Status des Abos des Nutzers:innen nicht automatisch auf "abgemeldet" gesetzt. Wenn eine E-Mail-Adresse "hard bounce" ist (z.B. wenn eine E-Mail ungültig ist oder nicht existiert), markieren wir die E-Mail-Adresse des Nutzers:innen als ungültig und versuchen nicht, weitere E-Mails an diese E-Mail-Adresse zu senden. Wenn dieser Benutzer seine E-Mail-Adresse ändert, senden wir ihm wieder E-Mails, da seine neue E-Mail-Adresse gültig sein könnte. Soft Bounces werden automatisch 72 Stunden lang wiederholt.

### Aktualisierung des Status von E-Mail-Abos

Es gibt vier Möglichkeiten, den Status des E-Mail-Abos eines Nutzers:innen zu aktualisieren:

#### SDK-Integration

Verwenden Sie das Braze-SDK, um den Status des Abos eines Nutzers oder einer Nutzerin zu aktualisieren.

#### REST API

Verwenden Sie den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), um das [Attribut`email_subscribe` ]({{site.baseurl}}/api/objects_filters/user_attributes_object) für einen bestimmten Nutzer:innen zu aktualisieren.

#### Benutzerprofil

1. Finden Sie den Benutzer über **Benutzer suchen**. 
2. Wählen Sie auf dem Tab **Engagement** die Buttons **Abgemeldet**, **Abonniert** oder **Opt-in** aus, um den Status des Abonnements des Nutzers:in zu ändern. 

Falls verfügbar, zeigt das Nutzerprofil auch einen Zeitstempel an, wann das Abo des Nutzers:innen zuletzt geändert wurde.

#### Präferenzzentrum

[Das Preference Center](#email-preference-center) Liquid kann am Ende Ihrer E-Mails eingefügt werden, so dass die Benutzer sich für oder gegen E-Mails entscheiden können. Braze verwaltet die Updates des Abo-Status über das Präferenzzentrum.

### Status des E-Mail-Abonnements prüfen

Nutzerprofil für John Doe, dessen E-Mail Abonnent:in auf Abonniert gesetzt wurde.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Es gibt zwei Möglichkeiten, den Status des E-Mail-Abos eines Nutzers:innen mit Braze zu überprüfen:

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

\![Felder zum Erstellen einer Abo-Gruppe.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmentierung mit einer Abonnementgruppe

Wenn Sie Ihre Segmente erstellen, setzen Sie den Namen der Abo-Gruppe als Filter ein. Damit bestätigen Sie, dass die Benutzer, die sich für Ihre Gruppe entschieden haben, Ihre E-Mails erhalten. Dies eignet sich hervorragend für monatliche Newsletter, Gutscheine, Mitgliedschaftsstufen und mehr.

\![Beispiel für das Targeting von Nutzern:innen im Segment "Verlorene Nutzer" mit dem Filter für Nutzer:innen in der Abo-Gruppe "Wöchentliche E-Mails".]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Archivierung von Abonnementgruppen

Archivierte Abonnementgruppen können nicht bearbeitet werden und erscheinen nicht mehr in Segmentfiltern oder in Ihrem Präferenzcenter. Wenn Sie versuchen, eine Gruppe zu archivieren, die als Segmentfilter in einer E-Mail, einer Kampagne oder einem Canvas verwendet wird, erhalten Sie eine Fehlermeldung, die Sie daran hindert, die Gruppe zu archivieren, bis Sie alle Verwendungen der Gruppe entfernen.

Um Ihre Gruppe auf der Seite **Abo-Gruppen** zu archivieren, gehen Sie wie folgt vor:

1. Suchen Sie Ihre Gruppe in der Liste der Abo-Gruppen. 
2. Wählen Sie **Archiv** aus dem Dropdown-Menü <i class="fa-solid fa-ellipsis-vertical"></i>.

Braze wird keine Statusänderungen für Benutzer in archivierten Gruppen verarbeiten. Wenn Sie z.B. die Abo-Gruppe 1 archivieren, während Susie sie abonniert hat, bleibt sie in dieser Gruppe "abonniert", auch wenn sie auf einen Abmelde-Link klickt (dies sollte Susie nichts ausmachen, da die Abo-Gruppe 1 archiviert ist und Sie damit keine Nachrichten mehr versenden können).

#### Anzeigen der Größe von Abonnementgruppen

Auf der Seite **Abo-Gruppen** können Sie das Diagramm **Abo-Gruppe Zeitreihe** referenzieren, um die Größe der Abo-Gruppe basierend auf der Anzahl der Nutzer:innen über einen bestimmten Zeitraum zu sehen. Diese Größen der Abo-Gruppen stimmen auch mit anderen Bereichen von Braze überein, z. B. mit der Berechnung der Segmentgröße.

\![Eine Beispielgrafik "Abo-Gruppe Zeitreihe" vom 2\. bis 11\. Dezember. Die Grafik zeigt einen Anstieg der Nutzerzahlen um ca. 10 Millionen vom 6\. zum 7.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### Anzeigen von Abonnementgruppen in der Kampagnenanalyse

Sie können die Anzahl der Benutzer, die ihren Abonnementstatus (abonniert oder abgemeldet) für eine bestimmte E-Mail-Kampagne geändert haben, auf der Analyseseite dieser Kampagne sehen.

1. Scrollen Sie auf der Seite **Campaign Analytics** für Ihre Kampagne nach unten zum Abschnitt **E-Mail Nachricht Performance**.
2. Wählen Sie den Pfeil unter **Abo-Gruppen** aus, um die Gesamtzahl der Statusänderungen zu sehen, die von Ihren Kund:innen übermittelt wurden.

\![Die Seite "Performance von E-Mail-Nachrichten" zeigt die Gesamtzahl der von Kund:in übermittelten Statusänderungen an.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### Überprüfen der E-Mail Abo-Gruppe eines Nutzers:innen

- **Benutzerprofil:** Auf einzelne Benutzerprofile können Sie über das Braze-Dashboard von der Seite [Benutzer suchen]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#access-profiles) aus zugreifen. Hier können Sie Benutzerprofile nach E-Mail-Adresse, Telefonnummer oder externer Benutzer-ID abrufen. Auf dem Tab **Engagement** können Sie auch die E-Mail Abo-Gruppen eines Nutzers:innen einsehen.
- **Braze REST API:** Verwenden Sie den [Endpunkt Abo-Gruppen des Nutzers auflisten]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) oder [Abo-Gruppenstatus des Nutzers auflisten]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/), um die Abo-Gruppen der einzelnen Nutzerprofile anzuzeigen. 

## E-Mail-Präferenzzentrum

Das E-Mail-Präferenzcenter ist eine einfache Möglichkeit zu verwalten, welche Benutzer bestimmte Gruppen von Newslettern erhalten. Sie finden es im Dashboard unter **Abonnementgruppen**. Jede Abo-Gruppe, die Sie erstellen, wird zur Liste der Präferenzzentren hinzugefügt. 

Wenn Sie mehr darüber erfahren möchten, wie Sie ein Präferenzzentrum hinzufügen oder anpassen können, lesen Sie den Abschnitt [Präferenzzentrum]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).

## Ändern von E-Mail-Abos {#changing-email-subscriptions}

In den meisten Fällen verwalten Ihre Benutzer ihr E-Mail-Abonnement über Abonnement-Links, die in den E-Mails enthalten sind, die sie erhalten. Sie müssen am Ende jeder E-Mail, die Sie versenden, eine rechtskonforme Fußzeile mit einem Link zum Abmelden einfügen. Wenn Nutzer:innen die Abmelde-URL in Ihrer Fußzeile auswählen, sollten sie abgemeldet werden und auf eine Landing Page gelangen, die die Änderung ihres Abos bestätigt. Wir empfehlen, dieses Liquid-Tag einzubinden: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Beachten Sie, dass, wenn ein Benutzer im E-Mail-Einstellungscenter die Option "Alle oben genannten E-Mail-Typen abbestellen" auswählt, sein globaler E-Mail-Abonnementstatus auf `unsubscribed` aktualisiert und er aus allen Abonnementgruppen abgemeldet wird.

### Benutzerdefinierte Fußzeilen erstellen {#custom-footer}

Wenn Sie die standardmäßige Braze-Fußzeile in Ihren E-Mails nicht verwenden möchten, können Sie eine arbeitsbereichsweite benutzerdefinierte E-Mail-Fußzeile erstellen, die Sie mit dem Attribut {% raw %}`{{${email_footer}}}`{% endraw %} Liquid in jede E-Mail einfügen können.

Auf diese Weise müssen Sie nicht für jede E-Mail-Template oder E-Mail-Kampagne, die Sie verwenden, eine neue Fußzeile erstellen. Weitere Schritte finden Sie unter [Benutzerdefinierte E-Mail-Fußzeile]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/).

#### Verwaltung des Abonnementstatus für chinesische IP-Adressen

Wenn Sie davon ausgehen, dass Ihre Empfänger:innen eine chinesische IP-Adresse haben, sollten Sie sich nicht allein auf einen Abmelde-Link in Ihrer E-Mail verlassen, um Ihre `unsubscribed` Listen zu pflegen. Bieten Sie stattdessen alternative Möglichkeiten für Nutzer:innen an, sich einfach abzumelden, z.B. indem Sie ein Ticketing über Ihr Support-Portal öffnen oder eine E-Mail an eine Vertretung mailen. 

### Erstellen einer angepassten Seite zum Abmelden

Wenn Nutzer:innen in einer E-Mail eine URL zum Abmelden auswählen, werden sie auf eine Standard-Landingpage weitergeleitet, die die Änderung ihres Abos bestätigt.

So erstellen Sie eine angepasste Landing Page, zu der Nutzer:in nach dem Abschluss eines Abonnements weitergeleitet werden (anstelle der Standard-Seite):

1. Gehen Sie zu **E-Mail-Einstellungen** > **Seiten und Fußzeilen für Abonnements**.
2. Stellen Sie das HTML für Ihre angepasste Landing Page zur Verfügung. 

Wir empfehlen, auf der Landing Page einen Link zum erneuten Abonnieren (z. B. {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) einzubauen, damit die Nutzer die Möglichkeit haben, sich erneut anzumelden, falls sie sich versehentlich abgemeldet haben.

\![Angepasste Abmeldeseite mit einer Vorschau "Sorry, dass Sie gehen!".]({% image_buster /assets/img/custom_unsubscribe.png %})

### Erstellen einer angepassten Opt-in-Seite

Anstatt einen Benutzer sofort für Ihre E-Mail-Kampagnen anzumelden, können Sie ihm mit einer benutzerdefinierten Opt-in-Seite die Möglichkeit geben, seine Benachrichtigungspräferenzen zu bestätigen und zu kontrollieren. Diese zusätzliche Kommunikation kann auch dazu beitragen, dass Ihre E-Mail Kampagnen nicht im Spam-Ordner landen, denn Ihre Nutzer:innen haben sich für ein Opt-in entschieden. 

1. Gehen Sie zu **Einstellungen** > **E-Mail-Voreinstellungen**.
2. Wählen Sie **Abo-Seiten und Fußzeilen** aus.
3. Passen Sie das Styling im Abschnitt **Benutzerdefinierte Opt-in-Seite** an, um zu sehen, wie Ihre Nutzer:in darauf hingewiesen werden, dass sie abonniert wurden.

Nutzer:innen werden über den Tag {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} auf diese Seite geleitet.

{% alert tip %}
Braze empfiehlt die Verwendung eines Double-Opt-In-Verfahrens, um Ihre E-Mail-Reichweite zu erhöhen. Bei diesem Vorgang wird eine zusätzliche Bestätigungs-E-Mail verschickt, in der der Benutzer seine Benachrichtigungseinstellungen über einen Link in der E-Mail noch einmal bestätigen kann. Zu diesem Zeitpunkt gilt der oder die Nutzer:in als angemeldet.
{% endalert %}

\![Angepasste Opt-in E-Mail mit der Nachricht "Schön, dass Sie immer noch von uns hören wollen".]({% image_buster /assets/img/custom_optin.png %})

## Abos und Kampagnen-Targeting {#subscriptions-and-campaign-targeting}

Standardmäßig richten sich Kampagnen mit Push- oder E-Mail-Nachrichten an Nutzer:innen, die ein Abonnent:in sind oder ein Opt-in haben. Sie können diese Targeting-Präferenz bei der Bearbeitung einer Kampagne ändern, indem Sie zum Schritt **Zielgruppe** gehen und das Dropdown-Menü neben **An diese Nutzer:innen senden** auswählen:.

Braze unterstützt drei Targeting-Stufen:

- Nur Nutzer:innen mit Abo oder angemeldete Nutzer:innen (Standard)
- Nur angemeldete Nutzer:innen.
- Alle Nutzer:innen, einschließlich derer, die sich abgemeldet haben.

{% alert important %}
Es liegt in Ihrer Verantwortung, bei der Verwendung dieser Targeting-Einstellungen alle geltenden [Spam-Gesetze]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) einzuhalten.
{% endalert %}

## Segmentierung nach Benutzerabonnements {#segmenting-by-user-subscriptions}

Mit den Filtern "E-Mail Abo-Status" und "Push Abo-Status" können Sie Ihre Nutzer:innen nach ihrem Abo-Status segmentieren.

Dies kann nützlich sein, wenn Sie Nutzer:innen ansprechen möchten, die sich weder für noch gegen ein Opt-in entschieden haben, und sie auffordern, sich explizit für E-Mail oder Push zu entscheiden. In diesem Fall würden Sie ein Segment mit einem Filter für "E-Mail/Push-Abonnement-Status ist abonniert" erstellen und Kampagnen an dieses Segment gehen an Benutzer, die abonniert sind, sich aber nicht angemeldet haben.

\![E-Mail Abo Status als Segment Filter verwendet.]({% image_buster /assets/img_archive/not_optin.png %})

