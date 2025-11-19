---
nav_title: Transaktions-E-Mail-Kampagnen
article_title: Transaktionsbezogene E-Mail-Kampagnen
page_order: 10

description: "In diesem Referenzartikel erfahren Sie, wie Sie eine neue Kampagne für Transaktions-E-Mails von Braze erstellen und konfigurieren."
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# Transaktionsbezogene E-Mail-Kampagnen

> Braze Transaktions-E-Mails werden versendet, um eine vereinbarte Transaktion zwischen einem Absender und einem Empfänger zu erleichtern. In diesem Referenzartikel erfahren Sie, wie Sie eine transaktionale E-Mail-Kampagne im Braze Dashboard erstellen und eine `campaign_id` generieren, die Sie in Ihre API-Aufrufe für unseren [`/transactional/v1/campaigns/{campaign_id}/send` Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) einbinden können.

{% alert important %}
Braze Transactional Email ist nur im Rahmen ausgewählter Braze-Pakete verfügbar. Wenden Sie sich an Ihren Braze Customer Success Manager oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/) für weitere Informationen.
{% endalert %}

Die transaktionale E-Mail-Kampagne wurde speziell für den Versand automatisierter, nicht werblicher E-Mail-Nachrichten entwickelt, um eine vereinbarte Transaktion zwischen Ihnen und Ihren Kunden zu erleichtern. Dazu gehören Informationen wie z. B.:

- Auftragsbestätigungen
- Passwort zurücksetzen
- Warnmeldungen zur Rechnungsstellung
- Versandwarnungen

Kurz gesagt, Sie können Transaktions-E-Mails verwenden, um geschäftskritische Benachrichtigungen zu versenden, die von Ihrem Dienst für einen einzelnen Nutzer:innen stammen, bei dem Schnelligkeit von größter Bedeutung ist. 

{% alert important %}
Transaktions-E-Mails unterscheiden sich von Transaktionskampagnen, mit denen Sie Ihre Nutzer ohne zusätzliche Kosten ansprechen können. Transaktionskampagnen können zum Beispiel Nachrichten enthalten, die gesendet werden, nachdem ein Nutzer einen Artikel in seinen Warenkorb gelegt hat. Weitere Informationen finden Sie unter [Optionen für die Zielgruppenansprache]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/).
{% endalert %}

## Schritt 1: Erstellen Sie eine neue Kampagne

Um eine neue Transaktions-E-Mail-Kampagne zu erstellen, erstellen Sie eine Kampagne und wählen Sie **Transaktions-E-Mail** als Nachrichtenkanal.

![Dropdown-Menü Kampagne erstellen mit der hervorgehobenen Option für Transaktions-E-Mails.]({% image_buster /assets/img/transactional_email_campaign.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Jetzt können Sie mit der Konfiguration Ihrer transaktionalen E-Mail-Kampagne fortfahren.

## Schritt 2: Konfigurieren Sie Ihre Kampagne

Der Ablauf der Kampagnenerstellung für Transaktions-E-Mail-Kampagnen ist im Vergleich zu dem einer [Standard-E-Mail-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) vereinfacht, um sicherzustellen, dass Ihre geschäftskritischen Transaktions-E-Mails alle Benutzer erreichen können.

Daher werden Sie feststellen, dass einige Einstellungen, die Sie vielleicht von anderen Braze-Kampagnentypen kennen, bei der Einrichtung dieses Kampagnentyps nicht erforderlich sind:

- Der Schritt **Lieferung** wurde vereinfacht, um die Terminierungsoptionen zu entfernen. Transaktions-E-Mails werden immer über die Braze REST API unter Verwendung der Kampagnen-ID ausgelöst, die auf der Seite **Zustellung** angezeigt wird. Zusätzliche Einstellungen, wie die Kontrolle der Wiederzulassung und Frequency-Capping-Einstellungen, wurden ebenfalls entfernt, um sicherzustellen, dass alle Nutzer:innen für diese kritischen Transaktionsmeldungen erreichbar sind, wenn Ihr Dienst eine Sendeanfrage triggert.
- Der Schritt **Targeting Zielgruppen** wurde entfernt. Da Transaktions-E-Mails Ihre gesamte Nutzerbasis als berechtigt registrieren (einschließlich abgemeldeter Nutzer:innen), müssen Sie keine Filter oder Segmente festlegen. Wenn Sie also eine Logik dafür haben, wer diese Nachricht erhalten soll, empfehlen wir Ihnen, diese Logik anzuwenden, bevor Sie entscheiden, ob Sie die API-Anfrage an Braze stellen, um die Nachricht an einen bestimmten Nutzer:innen auszulösen.
- Der Schritt **Conversions** wurde entfernt. Transaktions-E-Mails unterstützen zur Zeit kein Tracking von Konversions-Events.

![Workflow zum Verfassen, Zustellen und Bestätigen einer Kampagne für Transaktions-E-Mails.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: style="max-width:80%;"}

Um Ihre Transaktions-E-Mail-Kampagne zu konfigurieren, gehen Sie folgendermaßen vor:

1. Fügen Sie einen beschreibenden Namen hinzu, damit Sie die Ergebnisse auf Ihrer **Kampagnenseite** finden können, nachdem Sie Ihre Nachrichten verschickt haben.
2. Verfassen Sie Ihre E-Mail oder wählen Sie aus einer Vorlage.
3. Notieren Sie sich Ihre `campaign_id`. Nachdem Sie Ihre API-Kampagne gespeichert haben, müssen Sie die generierten `campaign_id` Felder in Ihre API-Anfrage aufnehmen, wie im Artikel [Endpunkt für Transaktions-E-Mails]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) beschrieben.
4. Klicken Sie auf **Kampagne speichern**, und schon können Sie Ihre API-Kampagne starten!

{% alert note %}
Die Einstellung für das Abmelden von Listen mit einem Klick ist für Transaktions-E-Mail-Kampagnen standardmäßig auf **Workspace-Standard verwenden** eingestellt, ähnlich wie bei anderen E-Mail-Kampagnen. Da dies für transaktionale Nachrichten gedacht ist, fügt Braze keine Ein-Klick-Abmeldung hinzu. Um eine Ein-Klick-Abmeldung zu diesem Kampagnentyp hinzuzufügen, [bearbeiten Sie diese Einstellung]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#message-level-one-click-list-unsubscribe) unter **Sendeinfo**.
{% endalert %}

### Unzulässige Tags in Transaktions-E-Mails

Die Tags `Connected Content` und `Promotion Code` Liquid sind in transaktionalen E-Mail-Kampagnen nicht verfügbar.

Die Verwendung des Tags `Connected Content` erfordert, dass Braze während des Sendevorgangs eine ausgehende API-Anfrage stellt, was den Versand von Nachrichten verlangsamen kann, wenn der von uns angefragte externe Dienst eine Latenz aufweist. Auch der Tag `Promotion Code` erfordert eine zusätzliche Verarbeitung durch Braze, um die Verfügbarkeit einer Aktion vor dem Versand zu prüfen, was den Versandprozess verlangsamen kann, wenn keine Aktion verfügbar ist.

Aus diesem Grund unterstützen wir keine `Connected Content` oder `Promotion Code` Tags in einem Feld Ihrer Transaktions-E-Mail-Kampagnen.


