---
nav_title: WhatsApp-Einrichtung
article_title: WhatsApp-Einrichtung
alias: /partners/whatsapp/
description: "In diesem Artikel erfahren Sie, wie Sie den WhatsApp-Kanal von Braze einrichten, einschließlich der Voraussetzungen und der empfohlenen nächsten Schritte."
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - WhatsApp
search_rank: 2
---

# WhatsApp-Einrichtung

> [WhatsApp](https://www.whatsapp.com/) Business Messaging ist eine beliebte Peer-to-Peer-Messaging-Plattform, die weltweit genutzt wird und gesprächsbasierte Nachrichten für Unternehmen bietet.	

## Voraussetzungen

Bestätigen Sie die folgenden Punkte, bevor Sie mit der Integration fortfahren:

- **Opt-in-Richtlinie:** WhatsApp verlangt von den Unternehmen, dass sich die Kunden für den Nachrichtenversand entscheiden.
- **WhatsApp-Content-Regeln:** WhatsApp hat mehrere [Content-Regeln](https://www.whatsapp.com/legal/commerce-policy?l=en), die befolgt werden müssen.
- **Compliance:** Beachten Sie alle geltenden Braze- und Meta-Dokumentationen sowie alle geltenden [Meta-Richtlinien](https://www.whatsapp.com/legal/?lang=en).
- **24-Stunden-Konversationslimits:** Nachdem ein Unternehmen eine erste vorgefertigte Nachricht gesendet hat oder ein Benutzer eine Nachricht gesendet hat, gibt es ein 24-Stunden-Fenster, in dem die beiden Parteien Nachrichten hin und her senden können. 
- **Ein Gespräch beginnen:** Benutzer können jederzeit ein Gespräch beginnen. Ein Unternehmen kann eine Konversation nur über eine genehmigte Nachrichtenvorlage einleiten.
<br><br>

| Anforderung| Beschreibung|
| ---| --- |
| Meta Business Manager Konto | Um diesen Messaging-Kanal nutzen zu können, ist ein Meta Business-Konto erforderlich. |
| WhatsApp-Business-Konto | Um diesen Nachrichtenkanal zu nutzen, benötigen Sie ein WhatsApp Business-Konto. |
| WhatsApp-Telefonnummer | Sie müssen eine Telefonnummer erwerben, die den Anforderungen von WhatsApp für die [Cloud-API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) oder die [On-Premises-API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) für die Nutzung des Messaging-Kanals entspricht.  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: WhatsApp Messenger mit Braze verbinden

Gehen Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und suchen Sie nach **WhatsApp**.

Auf der WhatsApp-Partnerseite wählen Sie **Integration beginnen**.

![WhatsApp Partnerseite mit einem Button, um die Integration zu beginnen.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:70%;"}

In dem sich öffnenden Fenster wählen Sie **Weiter**, bis die Schaltfläche **Integration beginnen** erscheint. Wählen Sie den Button aus, um die Integration zu starten.

![Anleitung zur Verbindung von Braze mit WhatsApp.]({% image_buster /assets/img/whatsapp/instructions.png %}){: style="max-width:50%;"}

### Schritt 2: WhatsApp-Einrichtung

Als Nächstes werden Sie durch den Braze-Setup-Workflow geführt. Eine Schritt-für-Schritt-Anleitung finden Sie bei der [eingebetteten WhatsApp-Anmeldung]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/). 

Innerhalb dieses Workflows führen Sie folgende Aktionen durch:
1. Erstellen oder wählen Sie Ihre Meta- und WhatsApp Business-Konten. Beachten Sie unbedingt die [Richtlinien für WhatsApp-Anzeigenamen](https://www.facebook.com/business/help/757569725593362). <br><br>Wahrscheinlich haben Sie bereits mindestens ein Meta Business-Konto in Ihrem Unternehmen. Wenn dies der Fall ist, wählen Sie das Konto aus, in dem Sie Ihr WhatsApp Business-Konto einrichten möchten. Die Benutzerberechtigungen und die geschäftliche Verifizierung für WhatsApp werden zentral in Ihrem Meta Business-Konto gesteuert.<br><br>
2. Erstellen Sie Ihr WhatsApp Business-Profil.
3. Überprüfen Sie Ihre WhatsApp Business-Nummer.<br><br>

Nachdem die Einrichtung abgeschlossen ist, wird eine spezielle WhatsApp-Abonnementgruppe für Ihre Benutzer erstellt.

### Schritt 3: WhatsApp-Vorlagen erstellen

Nur genehmigte WhatsApp-Nachrichtenvorlagen können verwendet werden, um Konversationen mit Kunden zu initiieren. WhatsApp-Vorlagen können mit dem [Meta Business Manager](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343) erstellt werden. Eine Liste der von Braze unterstützten WhatsApp-Nachrichtenfunktionen finden Sie unter [Unterstützte WhatsApp-Funktionen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#supported-whatsapp-features).

1. **Navigieren Sie zum [Template-Manager](https://business.facebook.com/wa/manage/message-templates)**<br>
Wählen Sie im Meta Business Manager unter **Konto-Tools** die Option **Nachrichtenvorlagen**.
Wählen Sie dann **Vorlagen erstellen**.<br><br>![WhatsApp Manager:in mit einer Liste von Templates für Nachrichten.]({% image_buster /assets/img/whatsapp/whatsapp2.png %}){: style="max-width:100%;"}<br><br>
2. **Nachrichteneinstellungen**<br>
Wählen Sie im Composer für neue Nachrichtenvorlagen die Kategorie Ihrer Nachricht aus, benennen Sie Ihre Vorlage und wählen Sie die Sprachen, die Sie unterstützen möchten. Sie können später weitere Sprachen löschen oder hinzufügen.<br><br> 
	Die folgenden Kategorien von Nachrichtenvorlagen sind verfügbar:
	- Marketing: Senden Sie Werbeangebote, Produktankündigungen und mehr, um die Bekanntheit und das Engagement zu steigern.
	- Utility: Senden Sie Updates zu Konten, Bestellungen, Warnungen und mehr, um wichtige Informationen weiterzugeben.
	- Authentifizierung: Senden Sie Codes, mit denen Ihre Kunden auf ihre Konten zugreifen können<br><br> 
	![Nachrichten-Template-Editor mit Kategorien für Marketing, Nützlichkeit und Authentifizierung.]({% image_buster /assets/img/whatsapp/whatsapp3.png %}){: style="max-width:100%;"}<br><br>
3. **Template bearbeiten**<br>
Als nächstes erstellen Sie Ihr Template für Nachrichten. <br><br>Sie können eine Text- oder Medienüberschrift, den Textkörper, eine Fußzeile für die Nachricht und Buttons bereitstellen. Beachten Sie, dass Video- und Dokumentenkopfzeilen derzeit nicht verfügbar sind und die Kopfzeilen entweder als Text oder als Bild vorliegen müssen. Alle Medien, die Sie hinzufügen, dienen als Beispiel für den Überprüfungsprozess und **sind nicht** in der Template Nachricht enthalten. Die Medien müssen in Braze hinzugefügt werden. Eine Vorschau Ihrer Nachricht wird in einem Panel angezeigt. <br><br>Meta unterstützt zwar kein Liquid, aber Sie können eine Vorlage für Variablen erstellen, die später in Braze durch Liquid-Variablen ersetzt werden können. Wählen Sie dazu die Schaltfläche **\+ Variable hinzufügen**.<br><br>![Template composer.]({% image_buster /assets/img/whatsapp/whatsapp4.png %}){: style="max-width:100%;"}

Sobald Sie Ihre Vorlage fertiggestellt haben, drücken Sie auf **Senden**. 

#### Zeit für die Genehmigung einer Vorlage

Sie können den Genehmigungsstatus Ihrer Nachrichtenvorlage entweder auf der Seite **Nachrichtenvorlage** im Meta Business Manager oder beim Erstellen einer Kampagne oder eines Canvas in Braze überprüfen. Zusätzlich können Sie je nach Ihren Benachrichtigungsberechtigungen vom WhatsApp-Team per E-Mail benachrichtigt werden. 

{% alert note %}
Genehmigte Vorlagen können in beliebig vielen Kampagnen und Canvases verwendet werden. Sie können auch an beliebig viele Opt-in-Nutzer:innen gesendet werden. Dies gilt, solange die Qualität der Vorlage nicht abnimmt.
{% endalert %}

### Schritt 4: Erstellen Sie eine WhatsApp-Kampagne

Sobald die WhatsApp-Vorlagen genehmigt wurden, können Sie zum Dashboard wechseln, um ein [WhatsApp Canvas oder eine Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/) zu erstellen. 

{% alert note %}
Nachdem Ihr WhatsApp Business-Konto erstellt wurde, legt Meta Ihr anfängliches Nachrichtenlimit fest. Wenn Sie mehr erfahren möchten, lesen Sie den Abschnitt [Durchsatz]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/#throughput).
{% endalert %}

## Nächste Schritte

Nach Abschluss der Integration empfehlen wir Ihnen, die beiden folgenden Meta-Prozesse abzuschließen:
- [Unternehmensverifizierung](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- Möglicherweise haben Sie bereits eine Unternehmensverifizierung, wenn Sie einen bestehenden Meta Business Manager verwendet haben. 
- [Offizielles Geschäftskonto](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

Wir empfehlen Ihnen außerdem, sich über die [Telefonnummern der Benutzer]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) zu informieren und alle Benutzer hinzuzufügen, die [in Ihrem Unternehmen](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143) Zugang zur Erstellung von [Nachrichtenvorlagen](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143) benötigen.

### WhatsApp Cloud API Lokaler Speicher

Braze unterstützt den [lokalen Speicher der Cloud-API](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5) von WhatsApp. Wenn Sie diese Funktion aktivieren möchten, wenden Sie sich an Ihren Braze-Kundenbetreuer.

