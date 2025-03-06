---
nav_title: API-Kampagnen
article_title: API-Kampagnen
page_order: 5
description: "In diesem Referenzartikel erfahren Sie, wie Sie eine Kampagnen-ID erzeugen, die Sie in Ihre API-Aufrufe aufnehmen können, und wie Sie diese Kampagne konfigurieren."
page_type: reference
tool: Campaigns

---
# API-Kampagnen

> In diesem Referenzartikel erfahren Sie, wie Sie eine `campaign_id` generieren, die Sie in Ihre API-Aufrufe einbinden können, und wie Sie diese Kampagne konfigurieren.

API-Kampagnen werden in der Regel für Transaktionsnachrichten verwendet. Bei der Erstellung von API-Kampagnen (nicht [von API-ausgelösten Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)) wird das Braze-Dashboard nur verwendet, um eine `campaign_id` zu generieren, mit der Sie Analysen für die Kampagnenberichterstattung verfolgen können. Sie können auch eine ID für Nachrichtenvariationen erstellen, die für jede Variante in Ihrer Kampagne unterschiedlich ist. 

Diese Informationen senden Sie dann an Ihr Entwicklungsteam, um sie in der API-Anfrage zu verwenden, zusammen mit:
- Werbetext
- Zugehörigkeit zum Publikum
- Vermögenswerte

Nachdem die Kampagne begonnen hat, können Sie die Ergebnisse im Dashboard einsehen. API-Kampagnen verwenden die Braze [Messaging-APIs]({{site.baseurl}}/api/endpoints/messaging/), die über die gleichen detaillierten Berichts- und Retargeting-Optionen verfügen wie Kampagnen, die vollständig über das Dashboard erstellt wurden.

{% alert warning %}
Da API-Kampagnen in der Regel transaktionsbezogen sind, sind alle Benutzer für API-Kampagnen berechtigt, auch die in Ihrer globalen Kontrollgruppe. Eine Kopfzeile zum [Abbestellen der Liste mit einem Mausklick]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe) wird diesen Sendungen nicht hinzugefügt. Wenn Sie allen API-Kampagnen eine Kopfzeile zum Abbestellen der Liste mit einem Klick hinzufügen möchten, wenden Sie sich an Ihren Kundenerfolgsmanager.
{% endalert %}

## Erstellen Sie eine neue Kampagne

Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**, dann wählen Sie **API-Kampagnen**. Jetzt können Sie mit der Konfiguration Ihrer API-Kampagne fortfahren.

Eine [API-ausgelöste Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) unterscheidet sich von einer API-Kampagne.

## Konfigurieren Sie Ihre Kampagne

Um Ihre Kampagne zu konfigurieren, führen Sie die folgenden Schritte aus:

1. Fügen Sie einen beschreibenden Titel hinzu, damit Sie die Ergebnisse auf unserer Kampagnenseite finden können, nachdem Sie Ihre Nachrichten verschickt haben.
2. Klicken Sie auf **Nachricht hinzufügen** und fügen Sie die Nachrichtentypen hinzu, die in Ihre API-Kampagne aufgenommen werden sollen. Auf diese Weise können Sie eine `campaign_id` und eine ID für Nachrichtenvariationen erstellen, die für jeden Kanal, den Sie einbeziehen, unterschiedlich ist. 
3. Optional können Sie ein Konvertierungsereignis hinzufügen, um die Konvertierung eines Benutzers für eine bestimmte Aktion oder ein Kampagnenziel zu verfolgen.
4. Klicken Sie auf **Kampagne speichern** und schon können Sie Ihre API-Kampagne starten!

## API-Aufrufe

Nachdem Sie Ihre API-Kampagne gespeichert haben, fügen Sie die folgenden Angaben in Ihre API-Anfrage ein: 
- Die generierten `campaign_id` Felder mit Ihrer API-Anfrage wurden in den [Send Messages Endpoints][2] vermerkt.
- Ein [Nachrichtenobjekt]({{site.baseurl}}/api/objects_filters/#messaging-objects) für jede in der Kampagne enthaltene Plattform. Geben Sie im Nachrichtenobjekt die ID der Nachrichtenvariation an. Damit legen Sie fest, dass die Statistiken unter dieser Variante gesammelt und angezeigt werden sollen. Die folgenden Nachrichtenobjekte werden unterstützt: Android, Content Cards, E-Mail, iOS, Kindle, SMS/MMS, Web-Push und Webhook.

[2]: {{site.baseurl}}/api/endpoints/messaging/#send-endpoints

