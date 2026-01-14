---
nav_title: API-Kampagnen
article_title: API-Kampagnen
page_order: 5
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie eine Kampagnen-ID generieren, die Sie in Ihre API-Aufrufe aufnehmen können, und wie Sie diese Kampagne konfigurieren."
page_type: reference
tool: Campaigns

---
# API Kampagnen

> In diesem referenzierten Artikel erfahren Sie, wie Sie eine `campaign_id` generieren, die Sie in Ihre API-Aufrufe einbinden können, und wie Sie diese Kampagne konfigurieren.

API-Kampagnen werden in der Regel für transaktionsbezogene Nachrichten verwendet. Bei der Erstellung von API-Kampagnen (nicht [von APIs getriggerten Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)) wird das Braze-Dashboard nur verwendet, um ein `campaign_id` zu erstellen, mit dem Sie Analytics für die Kampagnenberichterstattung verfolgen können. Sie können auch eine ID für Nachrichtenvariationen erstellen, die für jede Variante Ihrer Kampagne unterschiedlich ist. 

Diese Informationen senden Sie dann an Ihr Entwickler:in Team, um sie in der API-Anfrage zu verwenden, zusammen mit:
- Texte für die Kampagne
- Mitgliedschaft der Zielgruppe
- Assets

Nachdem die Kampagne begonnen hat, können Sie die Ergebnisse im Dashboard einsehen. API-Kampagnen verwenden die [Messaging-APIs]({{site.baseurl}}/api/endpoints/messaging/) von Braze, die über die gleichen detaillierten Berichts- und Retargeting-Optionen verfügen wie Kampagnen, die vollständig über das Dashboard erstellt wurden.

{% alert warning %}
Da API-Kampagnen in der Regel transaktionsbezogen sind, kommen alle Nutzer:innen für API-Kampagnen in Frage, auch diejenigen in Ihrer globalen Kontrollgruppe. Eine Kopfzeile zum [Abmelden der Liste mit einem Klick]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe) wird diesen Sendungen nicht hinzugefügt. Wenn Sie allen API Kampagnen mit einem Klick eine Kopfzeile zum Abmelden von Listen hinzufügen möchten, wenden Sie sich an Ihren Customer-Success-Manager:in.
{% endalert %}

## Erstellen Sie eine neue Kampagne

Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**, dann wählen Sie **API-Kampagnen**. Jetzt können Sie mit der Konfiguration Ihrer API Kampagne fortfahren.

Eine [API-getriggerte Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) unterscheidet sich von einer API-Kampagne.

## Konfigurieren Sie Ihre Kampagne

Um Ihre Kampagne zu konfigurieren, führen Sie die folgenden Schritte aus:

1. Fügen Sie einen beschreibenden Titel hinzu, damit Sie die Ergebnisse auf unserer Kampagnen-Seite finden können, nachdem Sie Ihre Nachrichten versendet haben.
2. Klicken Sie auf **Nachricht hinzufügen** und fügen Sie die Arten von Nachrichten hinzu, die in Ihre API-Kampagne aufgenommen werden sollen. Damit können Sie eine `campaign_id` und eine ID für Nachrichtenvariationen erstellen, die für jeden Kanal, den Sie einbeziehen, unterschiedlich ist. 
3. Optional können Sie ein Konversions-Event hinzufügen, um die Konversionen der Nutzer:innen für eine bestimmte Aktion oder ein Kampagnenziel zu tracken.
4. Klicken Sie auf **Kampagne speichern** und schon können Sie mit Ihrer API Kampagne beginnen!

## API-Aufrufe

Nachdem Sie Ihre API Kampagne gespeichert haben, fügen Sie die folgenden Angaben in Ihre API Anfrage ein: 
- Die generierten `campaign_id` Felder mit Ihrer API-Anfrage wurden in den [Endpunkten für das Senden von Nachrichten]({{site.baseurl}}/api/endpoints/messaging/#send-endpoints) vermerkt.
- Ein [Nachrichten-Objekt]({{site.baseurl}}/api/objects_filters/#messaging-objects) für jede in der Kampagne enthaltene Plattform. Geben Sie im Nachrichtenobjekt die ID der Nachrichtenvariation an. Damit legen Sie fest, dass die Statistiken unter dieser Variante gesammelt und angezeigt werden sollen. Die folgenden Nachrichten-Objekte werden unterstützt: Android, Content-Cards, E-Mail, iOS, Kindle, SMS/MMS, Web-Push und Webhook.


