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

> Braze Transaktions-E-Mails werden versendet, um eine vereinbarte Transaktion zwischen einem Sender und dem/der Empfänger:in zu ermöglichen. In diesem Referenzartikel erfahren Sie, wie Sie eine transaktionale E-Mail-Kampagne im Braze-Dashboard erstellen und eine `campaign_id` generieren, die Sie in Ihre API-Aufrufe für unseren [`/transactional/v1/campaigns/{campaign_id}/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) einbinden können.

{% alert important %}
Braze Transactional Email ist nur im Rahmen ausgewählter Braze-Pakete verfügbar. Kontaktieren Sie Ihren Customer-Success-Manager von Braze oder öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/) für weitere Informationen.
{% endalert %}

Die transaktionale E-Mail-Kampagne wurde speziell für den Versand automatisierter, nicht werblicher E-Mail-Nachrichten entwickelt, um eine vereinbarte Transaktion zwischen Ihnen und Ihren Kund:innen zu ermöglichen. Dazu gehören Informationen wie z. B.:

- Auftragsbestätigungen
- Passwortzurücksetzungen
- Rechnungsbenachrichtigungen
- Versandbenachrichtigungen

Kurz gesagt: Sie können Transaktions-E-Mails verwenden, um geschäftskritische Benachrichtigungen zu versenden, die von Ihrem Dienst für eine:n einzelne:n Nutzer:in stammen, bei denen Schnelligkeit von größter Bedeutung ist. 

{% alert important %}
Transaktions-E-Mails unterscheiden sich von Transaktionskampagnen, mit denen Sie Ihre Nutzer:innen ohne zusätzliche Kosten ansprechen können. Transaktionskampagnen können zum Beispiel Nachrichten enthalten, die gesendet werden, nachdem eine Nutzer:in einen Artikel in den Warenkorb gelegt hat. Weitere Informationen finden Sie unter [Optionen für die Zielgruppenansprache]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/).
{% endalert %}

{% alert note %}
Transaktions-E-Mail-API-Sendungen unterstützen die Nachrichtenarchivierung. Wenn die Nachrichtenarchivierung für E-Mails in Ihrem Workspace aktiviert ist, speichert Braze eine gerenderte Kopie jeder Transaktions-E-Mail-Sendung. Weitere Informationen finden Sie unter [Nachrichtenarchivierung]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving/).
{% endalert %}

## 1. Schritt: Erstellen Sie eine neue Kampagne

Um eine neue Transaktions-E-Mail-Kampagne zu erstellen, erstellen Sie eine Kampagne und wählen Sie **Transaktions-E-Mail** als Messaging-Kanal.

![Dropdown-Menü „Kampagne erstellen" mit der hervorgehobenen Option für Transaktions-E-Mails.]({% image_buster /assets/img/transactional_email_campaign.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Jetzt können Sie mit der Konfiguration Ihrer transaktionalen E-Mail-Kampagne fortfahren.

## 2. Schritt: Konfigurieren Sie Ihre Kampagne

Der Ablauf der Kampagnenerstellung für Transaktions-E-Mail-Kampagnen ist im Vergleich zu dem einer [Standard-E-Mail-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) vereinfacht, um sicherzustellen, dass Ihre geschäftskritischen Transaktions-E-Mails alle Nutzer:innen erreichen können.

Daher werden Sie feststellen, dass einige Einstellungen, die Sie vielleicht von anderen Braze-Kampagnentypen kennen, bei der Einrichtung dieses Kampagnentyps nicht erforderlich sind:

- Der Schritt **Zustellung** wurde vereinfacht, um die Planungsoptionen zu entfernen. Transaktions-E-Mails werden immer über die Braze REST API unter Verwendung der Kampagnen-ID ausgelöst, die auf der Seite **Zustellung** angezeigt wird. Zusätzliche Einstellungen, wie die Kontrolle der Wiederzulassung und Frequency-Capping-Einstellungen, wurden ebenfalls entfernt, um sicherzustellen, dass alle Nutzer:innen für diese kritischen Transaktionsmeldungen erreichbar sind, wenn Ihr Dienst eine Sendeanfrage triggert.
- Der Schritt **Zielgruppen** wurde entfernt. Da Transaktions-E-Mails Ihre gesamte Nutzerbasis als berechtigt registrieren (einschließlich abgemeldeter Nutzer:innen), müssen Sie keine Filter oder Segmente festlegen. Wenn Sie also eine Logik dafür haben, wer diese Nachricht erhalten soll, empfehlen wir Ihnen, diese Logik anzuwenden, bevor Sie entscheiden, ob Sie die API-Anfrage an Braze stellen, um die Nachricht an eine:n bestimmte:n Nutzer:in auszulösen.
- Der Schritt **Konversionen** wurde entfernt. Transaktions-E-Mails unterstützen derzeit kein Tracking von Konversions-Events.

![Verfassen, Zustellung und Bestätigen – Workflow zur Erstellung einer Transaktions-E-Mail-Kampagne.]({% image_buster /assets/img/transactional_campaign_compose.png %}){: style="max-width:80%;"}

Um Ihre Transaktions-E-Mail-Kampagne zu konfigurieren, gehen Sie folgendermaßen vor:

1. Fügen Sie einen beschreibenden Namen hinzu, damit Sie die Ergebnisse auf Ihrer **Kampagnen**-Seite finden können, nachdem Sie Ihre Nachrichten versendet haben.
2. Verfassen Sie Ihre E-Mail oder wählen Sie ein Template aus.
3. Notieren Sie sich Ihre `campaign_id`. Nachdem Sie Ihre API-Kampagne gespeichert haben, müssen Sie die generierten `campaign_id`-Felder in Ihre API-Anfrage aufnehmen, wie im Artikel [Endpunkt für Transaktions-E-Mails]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) beschrieben.
4. Klicken Sie auf **Kampagne speichern**, und schon können Sie Ihre API-Kampagne starten!

{% alert note %}
Die Einstellung für das Abmelden von Listen mit einem Klick ist für Transaktions-E-Mail-Kampagnen standardmäßig auf **Workspace-Standard verwenden** eingestellt, ähnlich wie bei anderen E-Mail-Kampagnen. Da dies für transaktionales Messaging gedacht ist, fügt Braze keine Ein-Klick-Abmeldung hinzu. Um eine Ein-Klick-Abmeldung zu diesem Kampagnentyp hinzuzufügen, [bearbeiten Sie diese Einstellung]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#message-level-one-click-list-unsubscribe) unter **Sendeinfo**.
{% endalert %}

### Unzulässige Tags in Transaktions-E-Mails

Die Liquid-Tags `Connected Content` und `Promotion Code` sind in transaktionalen E-Mail-Kampagnen nicht verfügbar.

Die Verwendung des `Connected Content`-Tags erfordert, dass Braze während des Sendevorgangs eine ausgehende API-Anfrage stellt, was den Nachrichtenversand verlangsamen kann, wenn der angefragte externe Dienst eine Latenz aufweist. Ebenso erfordert der `Promotion Code`-Tag eine zusätzliche Verarbeitung durch Braze, um die Verfügbarkeit einer Aktion vor dem Versand zu prüfen, was den Versandprozess verlangsamen kann, wenn keine Aktion verfügbar ist.

Aus diesem Grund unterstützen wir keine `Connected Content`- oder `Promotion Code`-Tags in einem Feld Ihrer Transaktions-E-Mail-Kampagne.