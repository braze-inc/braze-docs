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

Braze verfügt über drei globale Abo-Status für E-Mail Nutzer:innen (in der folgenden Tabelle aufgeführt), die der letzte Gatekeeper zwischen Ihren Nachrichten und Ihren Nutzer:innen sind. Nutzer:innen, die als `unsubscribed` gelten, erhalten zum Beispiel keine Nachrichten, die auf den globalen Abo-Status `subscribed` oder `opted-in` ausgerichtet sind.

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

Wenn ein Benutzer eine oder mehrere Ihrer E-Mails als Spam markiert hat, sendet Braze nur Transaktions-E-Mails an diesen Benutzer. In diesem Fall beziehen sich Transaktions-E-Mails auf die Option **An alle Benutzer senden, auch an nicht angemeldete Benutzer**, die Sie im Schritt **Zielgruppe** ausgewählt haben.

{% alert tip %}
In unseren [IP-Warming]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/)-Best Practices finden Sie Hinweise, wie Sie Ihre Nutzer:innen effektiv erneuern können.
{% endalert %}

### Bounce-E-Mails und ungültige E-Mails

{% multi_lang_include metrics.md metric='Hard Bounce' %} {% multi_lang_include metrics.md metric='Soft Bounce' %} 

Wenn dieser Benutzer seine E-Mail-Adresse ändert, senden wir ihm wieder E-Mails, da seine neue E-Mail-Adresse gültig sein könnte. Soft Bounces werden automatisch 72 Stunden lang wiederholt.

### Aktualisierung des Status von E-Mail-Abos

Es gibt vier Möglichkeiten, den Status des E-Mail-Abos eines Nutzers:innen zu aktualisieren:

#### SDK-Integration

Verwenden Sie das Braze-SDK, um den Status des Abos eines Nutzers oder einer Nutzerin zu aktualisieren.

#### REST API

Verwenden Sie den [`/users/track`-Endpunkt][users-track] um das [`email_subscribe`][user_attributes_object]-Attribut für eine:n bestimmte:n Nutzer:in zu aktualisieren.

#### Benutzerprofil

1. Finden Sie den Benutzer über **Benutzer suchen**. 
2. Klicken Sie auf der Registerkarte **Engagement** auf die Schaltflächen **Abgemeldet**, **Abgemeldet** oder **Eingeschaltet**, um den Abonnementstatus des betreffenden Benutzers zu ändern. 

Falls verfügbar, zeigt das Nutzerprofil auch einen Zeitstempel an, wann das Abo des Nutzers:innen zuletzt geändert wurde.

#### Präferenzzentrum

[Das Preference Center](#email-preference-center) Liquid kann am Ende Ihrer E-Mails eingefügt werden, so dass die Benutzer sich für oder gegen E-Mails entscheiden können. Braze verwaltet die Updates des Abo-Status über das Präferenzzentrum.

### Status des E-Mail-Abonnements prüfen

![Benutzerprofil von John Doe, dessen E-Mail-Abonnementstatus auf Abonniert gesetzt ist.][3]{: style="float:right;max-width:35%;margin-left:15px;"}

Es gibt zwei Möglichkeiten, den Status des E-Mail-Abos eines Nutzers:innen mit Braze zu überprüfen:

1. **REST API-Export:** Verwenden Sie die Endpunkte [Nutzer:innen nach Segmenten exportieren][Segment] oder [Nutzer:innen nach Bezeichner exportieren][Bezeichner], um einzelne Nutzerprofile im JSON-Format zu exportieren.
2. **Benutzerprofil:** Suchen Sie das Profil des Benutzers auf der Seite [Benutzer suchen][5], und wählen Sie dann die Registerkarte **Engagement**, um den Abonnementstatus eines Benutzers anzuzeigen und manuell zu aktualisieren.

Wenn ein Benutzer seine E-Mail-Adresse aktualisiert, wird sein Abonnementstatus auf abonniert gesetzt, es sei denn, die aktualisierte E-Mail-Adresse existiert bereits an anderer Stelle in einem Braze-Arbeitsbereich. Sie können einzelne Nutzerprofile im JSON-Format exportieren, indem Sie die Endpunkte [Nutzer:innen nach Segmenten exportieren][Segment] oder [Nutzer:innen nach Bezeichner exportieren][Bezeichner] verwenden.

## Abo-Gruppen

Abo-Gruppen sind Segmentfilter, mit denen Sie Ihre Zielgruppe aus den [globalen Abo-Statusangaben](#subscription-states) weiter eingrenzen können. Sie können bis zu 350 Abonnementgruppen pro Arbeitsbereich hinzufügen. Mit diesen Gruppen können Sie den Endbenutzern detailliertere Abonnementoptionen anbieten.

Nehmen wir zum Beispiel an, Sie versenden mehrere Kategorien von E-Mail-Kampagnen (Werbung, Newsletter oder Produktaktualisierungen). In diesem Fall können Sie Abonnementgruppen verwenden, damit Ihre Kunden von einer einzigen Seite aus auswählen können, welche E-Mail-Kategorien sie abonnieren oder abbestellen möchten, indem Sie ein [E-Mail-Präferenzcenter](#email-preference-center) verwenden. Alternativ können Sie Abonnementgruppen verwenden, um Ihren Kunden die Wahl zu lassen, wie häufig sie E-Mails von Ihnen erhalten möchten, indem Sie Abonnementgruppen für tägliche, wöchentliche oder monatliche E-Mails erstellen.

Verwenden Sie die [Abonnementgruppen-Endpunkte][25], um die Abonnementgruppen, die Sie auf dem Braze Dashboard gespeichert haben, programmatisch auf der Seite **Abonnementgruppen** zu verwalten.

### Erstellen einer Abonnementgruppe

1. Gehen Sie zu **Publikum** > **Abonnements**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, befindet sich diese Seite unter **Benutzer** > **Abonnementgruppen**.
{% endalert %}

{: start="2"}
2\. Wählen Sie **\+ E-Mail-Abonnementgruppe erstellen**.
3\. Geben Sie Ihrer Abonnementgruppe einen Namen und eine Beschreibung, und klicken Sie auf **Speichern**. 

Alle Abonnementgruppen werden automatisch zu Ihrem Präferenzcenter hinzugefügt.

![Felder, um eine Abonnementgruppe zu erstellen.][26]{: height="50%" width="50%"}

### Segmentierung mit einer Abonnementgruppe

Wenn Sie Ihre Segmente erstellen, setzen Sie den Namen der Abo-Gruppe als Filter ein. Damit bestätigen Sie, dass die Benutzer, die sich für Ihre Gruppe entschieden haben, Ihre E-Mails erhalten. Dies eignet sich hervorragend für monatliche Newsletter, Gutscheine, Mitgliedschaftsstufen und mehr.

![GIF eines Benutzers, der den Namen einer Abonnementgruppe als Filter einstellt.][27]{: style="max-width:80%"}

### Archivierung von Abonnementgruppen

Archivierte Abonnementgruppen können nicht bearbeitet werden und erscheinen nicht mehr in Segmentfiltern oder in Ihrem Präferenzcenter. Wenn Sie versuchen, eine Gruppe zu archivieren, die als Segmentfilter in einer E-Mail, einer Kampagne oder einem Canvas verwendet wird, erhalten Sie eine Fehlermeldung, die Sie daran hindert, die Gruppe zu archivieren, bis Sie alle Verwendungen der Gruppe entfernen.

Sie können Ihre Gruppe auf der Seite **Abonnementgruppen** archivieren. Suchen Sie Ihre Gruppe in der Liste, klicken Sie dann auf das Zahnrad und wählen Sie **Archiv** aus dem Dropdown-Menü.

Braze wird keine Statusänderungen für Benutzer in archivierten Gruppen verarbeiten. Wenn Sie z.B. "Abonnementgruppe A" archivieren, während Susie `subscribed` dazugehört, bleibt sie "`subscribed`" zu dieser Gruppe, auch wenn sie auf einen Abmeldelink klickt (dies sollte Susie nichts ausmachen, da "Abonnementgruppe A" archiviert ist und Sie damit keine Nachrichten versenden können).

#### Anzeigen der Größe von Abonnementgruppen

Sie können sich auf der Seite **Abonnementgruppen** auf das Diagramm **Abonnementgruppen-Zeitreihe** beziehen, um die Größe der Abonnementgruppe anhand der Anzahl der Benutzer über einen bestimmten Zeitraum zu sehen. Diese Größen der Abo-Gruppen stimmen auch mit anderen Bereichen von Braze überein, z. B. mit der Berechnung der Segmentgröße.

![Eine Beispielgrafik „Abo-Gruppe Zeitreihe“ vom 2\. bis 11\. Dezember. Die Grafik zeigt einen Anstieg der Nutzerzahlen um ca. 10 Millionen vom 6\. zum 7.][10]

#### Anzeigen von Abonnementgruppen in der Kampagnenanalyse

Sie können die Anzahl der Benutzer, die ihren Abonnementstatus (abonniert oder abgemeldet) für eine bestimmte E-Mail-Kampagne geändert haben, auf der Analyseseite dieser Kampagne sehen.

Scrollen Sie auf der Seite **Kampagnenanalyse** für Ihre Kampagne nach unten zum Abschnitt **Leistung von E-Mail-Nachrichten** und klicken Sie auf den Pfeil unter **Abonnementgruppen**, um die Gesamtzahl der von Ihren Kunden übermittelten Statusänderungen anzuzeigen.

![Die Seite „E-Mail-Messaging-Performance“ zeigt die Gesamtzahl der von Kund:innen übermittelten Statusänderungen an.][30]

## E-Mail-Präferenzzentrum

Das E-Mail-Präferenzcenter ist eine einfache Möglichkeit zu verwalten, welche Benutzer bestimmte Gruppen von Newslettern erhalten. Sie finden es im Dashboard unter **Abonnementgruppen**. Jede Abo-Gruppe, die Sie erstellen, wird zur Liste der Präferenzzentren hinzugefügt. Wenn Sie mehr darüber erfahren möchten, wie Sie ein Präferenzzentrum hinzufügen oder anpassen können, lesen Sie den Abschnitt [Präferenzzentrum]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/preference_center/).

## Ändern von E-Mail-Abos {#changing-email-subscriptions}

In den meisten Fällen verwalten Ihre Benutzer ihr E-Mail-Abonnement über Abonnement-Links, die in den E-Mails enthalten sind, die sie erhalten. Sie müssen am Ende jeder E-Mail, die Sie versenden, eine rechtskonforme Fußzeile mit einem Link zum Abmelden einfügen. Wenn Nutzer:innen auf die Abmelde-URL in Ihrer Fußzeile klicken, sollten sie abgemeldet werden und auf eine Landing Page gelangen, die die Änderung ihres Abos bestätigt. Wir empfehlen, dieses Liquid-Tag einzubinden: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Beachten Sie, dass, wenn ein Benutzer im E-Mail-Einstellungscenter die Option "Alle oben genannten E-Mail-Typen abbestellen" auswählt, sein globaler E-Mail-Abonnementstatus auf `unsubscribed` aktualisiert und er aus allen Abonnementgruppen abgemeldet wird.

### Benutzerdefinierte Fußzeilen erstellen {#custom-footer}

Wenn Sie die standardmäßige Braze-Fußzeile in Ihren E-Mails nicht verwenden möchten, können Sie eine arbeitsbereichsweite benutzerdefinierte E-Mail-Fußzeile erstellen, die Sie mit dem Attribut {% raw %}`{{${email_footer}}}`{% endraw %} Liquid in jede E-Mail einfügen können.

Auf diese Weise müssen Sie nicht für jede E-Mail-Template oder E-Mail-Kampagne, die Sie verwenden, eine neue Fußzeile erstellen. Weitere Schritte finden Sie unter [Benutzerdefinierte E-Mail-Fußzeile]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/).

#### Verwaltung des Abonnementstatus für chinesische IP-Adressen

Wenn Sie davon ausgehen, dass Ihre Empfänger:innen eine chinesische IP-Adresse haben, sollten Sie sich nicht allein auf einen Abmelde-Link in Ihrer E-Mail verlassen, um Ihre `unsubscribed` Listen zu pflegen. Bieten Sie stattdessen alternative Möglichkeiten für Nutzer:innen an, sich einfach abzumelden, z.B. indem Sie ein Ticketing über Ihr Support-Portal öffnen oder eine E-Mail an eine Vertretung mailen. 

### Erstellen einer angepassten Seite zum Abmelden

Wenn Nutzer:innen in einer E-Mail auf eine URL zum Abmelden klicken, werden sie auf eine Standard-Landing Page weitergeleitet, die die Änderung ihres Abos bestätigt.

Um eine benutzerdefinierte Landing Page zu erstellen, zu der Benutzer bei der Anmeldung weitergeleitet werden (anstelle der Standardseite), gehen Sie zu **E-Mail-Einstellungen** > **Anmeldeseiten und Fußzeilen** und geben Sie den HTML-Code für Ihre benutzerdefinierte Landing Page ein. Wir empfehlen, auf der Landing Page einen Link zum erneuten Abonnieren (z. B. {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) einzubauen, damit die Nutzer die Möglichkeit haben, sich erneut anzumelden, falls sie sich versehentlich abgemeldet haben.

![E-Mail zum Abbestellen im Fenster „Angepasste Abmeldeseite“.][11]

### Erstellen einer angepassten Opt-in-Seite

Anstatt einen Benutzer sofort für Ihre E-Mail-Kampagnen anzumelden, können Sie ihm mit einer benutzerdefinierten Opt-in-Seite die Möglichkeit geben, seine Benachrichtigungspräferenzen zu bestätigen und zu kontrollieren. Diese zusätzliche Kommunikation kann auch dazu beitragen, dass Ihre E-Mail Kampagnen nicht im Spam-Ordner landen, denn Ihre Nutzer:innen haben sich für ein Opt-in entschieden. 

Gehen Sie zu **E-Mail-Einstellungen** > **Abo-Seiten und Fußzeilen** und passen Sie das Styling im Abschnitt **Benutzerdefinierte Opt-In-Seite** an, um zu sehen, wie Sie Ihren Nutzern anzeigen, dass sie abonniert wurden.

{% alert tip %}
Braze empfiehlt die Verwendung eines Double-Opt-In-Verfahrens, um Ihre E-Mail-Reichweite zu erhöhen. Bei diesem Vorgang wird eine zusätzliche Bestätigungs-E-Mail verschickt, in der der Benutzer seine Benachrichtigungseinstellungen über einen Link in der E-Mail noch einmal bestätigen kann. Zu diesem Zeitpunkt gilt der oder die Nutzer:in als angemeldet.
{% endalert %}

## Abos und Kampagnen-Targeting {#subscriptions-and-campaign-targeting}

Kampagnen mit Push- oder E-Mail-Nachrichten richten sich an Benutzer, die standardmäßig abonniert sind oder sich angemeldet haben. Sie können diese Zielgruppeneinstellung bei der Bearbeitung einer Kampagne ändern, indem Sie zum Schritt **Zielgruppe** gehen und auf das Dropdown-Menü neben **An diese Benutzer senden:** klicken.

Braze unterstützt drei Targeting-Stufen:

- Nur Nutzer:innen mit Abo oder angemeldete Nutzer:innen (Standard)
- Nur angemeldete Nutzer:innen.
- Alle Nutzer:innen, einschließlich derer, die sich abgemeldet haben.

{% alert important %}
Es liegt in Ihrer Verantwortung, die geltenden [Spam-Gesetze]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) einzuhalten, wenn Sie diese Zielgruppeneinstellungen verwenden.
{% endalert %}

![Beispiel für das Targeting von Nutzern:in, die im Abschnitt „Targeting-Optionen“ des Schritts „Zielgruppe“ abonniert oder optiert sind.][17]

## Segmentierung nach Benutzerabonnements {#segmenting-by-user-subscriptions}

Mit den Filtern `Email Subscription Status` und `Push Subscription Status` können Sie Ihre Nutzer:innen nach ihrem Abo-Status segmentieren.

Dies kann zum Beispiel nützlich sein, wenn Sie Nutzer ansprechen möchten, die sich weder an- noch abgemeldet haben, und sie ermutigen möchten, sich ausdrücklich für E-Mails oder Push-Nachrichten anzumelden. In diesem Fall würden Sie ein Segment mit einem Filter für "E-Mail/Push-Abonnement-Status ist abonniert" erstellen und Kampagnen an dieses Segment gehen an Benutzer, die abonniert sind, sich aber nicht angemeldet haben.

![E-Mail Abo-Status, der als Segmentfilter verwendet wird.][18]

[10]: {% image_buster /assets/img_archive/subscription_group_graph.png %}
[11]: {% image_buster /assets/img/custom_unsubscribe.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[16]: {% image_buster /assets/img_archive/user-profile-subscription-ui.png %}
[17]: {% image_buster /assets/img_archive/campaign-targeting-subscription-ui.png %}
[18]: {% image_buster /assets/img_archive/not_optin.png %}
[19]: {% image_buster /assets/img_archive/email_settings.png %}
[25]: {{site.baseurl}}/api/endpoints/subscription_groups
[26]: {% image_buster /assets/img/sub_group_create.png %}
[27]: {% image_buster /assets/img/sub_group_use.gif %}
[28]: {{site.baseurl}}/api/endpoints/preference_center/
[29]: {% image_buster /assets/img/user-sub-state-export.png %}
[30]: {% image_buster /assets/img/campaign_analytics_sub_groups.png %}
[users-track]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[user_attributes_object]: {{site.baseurl}}/api/objects_filters/user_attributes_object
[3]: {% image_buster /assets/img/push_example.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/
[Bezeichner]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[Segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
