---
nav_title: WhatsApp-Nachrichten erstellen
article_title: WhatsApp-Nachrichten erstellen
page_order: 4
description: "In diesem Referenzartikel werden die einzelnen Schritte zur Erstellung einer WhatsApp-Nachricht beschrieben."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# WhatsApp-Nachrichten erstellen

> WhatsApp-Kampagnen eignen sich hervorragend, um Ihre Kunden direkt zu erreichen und programmgesteuert mit ihnen zu kommunizieren. Sie können Liquid und andere dynamische Inhalte verwenden, um ein persönliches Erlebnis mit Ihren Nutzern zu schaffen und eine Umgebung zu schaffen, die ein unaufdringliches Nutzererlebnis mit Ihrer Marke fördert und verbessert. 

## Voraussetzungen


  - Richtlinien, Einschränkungen und Inhaltsregeln bestätigen
  - Richten Sie Ihre WhatsApp-Verbindung ein
  - Erstellen Sie erste Vorlagen in Meta, die Sie in Ihren Nachrichten verwenden können.

## 

### Schritt 1: Wählen Sie, wo Sie Ihre Botschaft aufbauen möchten

{% alert note %}
WhatsApp erstellt für jede Sprache unterschiedliche [Nachrichtenvorlagen](#template-messages). Entweder erstellen Sie für jede Sprache eine Kampagne mit Segmentierung, um den Benutzern die richtige Vorlage zu liefern, oder Sie verwenden Canvas.
{% endalert %}

Sie sind sich nicht sicher, ob Ihre Nachricht über eine Kampagne oder ein Canvas versendet werden soll? Kampagnen eignen sich eher für einzelne einfache Messaging-Kampagnen, während Canvases besser für mehrstufige User Journeys geeignet sind.

{% tabs %}
{% tab Kampagne %}

**Schritte:**

1. Gehen Sie auf die Seite **Kampagnen** und klicken Sie auf <i class="fas fa-plus"></i> **Kampagne erstellen**.
2. Gehen Sie auf **WhatsApp** oder für Multichannel-Kampagnen auf **Multichannel-Kampagne**.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu.
   * Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen. Wenn Sie zum Beispiel den [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.
5. Fügen Sie so viele Varianten hinzu, wie Sie für Ihre Kampagne benötigen, und benennen Sie sie. Sie können für jede hinzugefügte Variante verschiedene Plattformen, Nachrichtentypen und Layouts auswählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Kampagne ähnlich sind oder den gleichen Inhalt haben, verfassen Sie Ihre Nachricht, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann aus der Dropdown-Liste **Variante hinzufügen** die Option **Aus Variante kopieren** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Schritte:**

1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) mit dem Canvas Composer.
2. Wenn Sie den Canvas eingerichtet haben, fügen Sie im Canvas Builder einen Schritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie einen [Zeitplan für den Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) und geben Sie bei Bedarf eine Verzögerung an.
4. Filtern Sie Ihre Zielgruppe für diesen Schritt nach Bedarf. Sie können den Empfängerkreis mit Segmenten und zusätzlichen Filtern weiter eingrenzen. Die Zielgruppenoptionen werden mit einer gewissen Verzögerung zum Versandzeitpunkt überprüft.
5. Legen Sie das [Fortschrittsverhalten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) fest.
6. Wählen Sie andere Messaging-Kanäle, die Sie mit Ihrer Nachricht verbinden möchten.

{% alert tip %}
Wenn ein aktionsbasiertes Canvas durch eine eingehende WhatsApp-Nachricht ausgelöst wird, können Sie in jedem Canvas-Schritt bis zum nächsten Aktionspfad WhatsApp-Eigenschaften referenzieren.
{% endalert %}

{% endtab %}
{% endtabs %}

### Schritt 2: Verfassen Sie Ihre WhatsApp-Nachricht

Wählen Sie, ob Sie eine [WhatsApp-Vorlage](#template-messages) oder eine Antwortnachricht erstellen möchten, je nach Anwendungsfall. Jede geschäftlich initiierte Konversation muss von einer genehmigten Vorlage ausgehen, wohingegen Antwortnachrichten innerhalb eines Zeitfensters von 24 Stunden als Antwort auf eingehende Nachrichten von Benutzern verwendet werden können.

![Unter Nachrichtenvarianten können Sie eine Abo-Gruppe und eine von zwei Nachrichtentypen auswählen: WhatsApp-Vorlage Nachricht und Antwortnachricht.][5]{: style="max-width:80%;"}

#### Template-Nachrichten

Mit [genehmigten Template-Nachrichten für WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates
) können Sie Gespräche auf WhatsApp anstoßen. Diese Nachrichten werden im Voraus zur Genehmigung des Inhalts an WhatsApp übermittelt, was bis zu 24 Stunden dauern kann. Änderungen am Text müssen bearbeitet und erneut an WhatsApp gesendet werden.

Deaktivierte Textfelder (grau unterlegt) können nicht bearbeitet werden, da sie Teil der genehmigten WhatsApp-Vorlage sind. Um Aktualisierungen am deaktivierten Text vorzunehmen, müssen Sie Ihre Vorlage bearbeiten und erneut genehmigen lassen.

##### Sprachen

Jede Vorlage hat eine zugewiesene Sprache, so dass Sie für jede Sprache eine Kampagne oder einen Canvas-Schritt erstellen müssen, um den Benutzerabgleich korrekt einzurichten. Wenn Sie z.B. ein Canvas erstellen, das Vorlagen verwendet, die mit Indonesisch und Englisch belegt sind, müssen Sie einen Canvas-Schritt für die indonesische Vorlage und einen Canvas-Schritt für die englische Vorlage erstellen.

![Template-Liste mit Nachrichteninhalt, zugewiesenen Sprachen und Genehmigungsstatus.][8]{: style="max-width:80%;"}

Wenn Sie Texte in einer Sprache hinzufügen, die von rechts nach links geschrieben ist, beachten Sie, dass das endgültige Aussehen von Nachrichten von rechts nach links weitgehend davon abhängt, wie die Dienste sie darstellen. 

##### Variablen

Wenn Sie bei der Erstellung der WhatsApp-Vorlage im Meta Business Manager Variablen hinzugefügt haben, werden diese Variablen im Message Composer als Leerstellen angezeigt. Ersetzen Sie diese Leerzeichen durch Liquid oder einfachen Text. Um reinen Text zu verwenden, benutzen Sie das Format "Text hier", das von doppelten Klammern umgeben ist. Wenn Sie sich bei der Erstellung Ihrer Vorlage für Bilder entschieden haben, können Sie Bilder aus der Mediathek hochladen oder hinzufügen, indem Sie auf eine Bild-URL verweisen.

Beachten Sie, dass deaktivierte Textfelder (grau unterlegt) nicht bearbeitet werden können, da sie Teil der genehmigten WhatsApp-Vorlage sind. Wenn Sie Änderungen am deaktivierten Text vornehmen möchten, müssen Sie Ihre Vorlage bearbeiten und erneut genehmigen lassen.

{% alert tip %}
{% raw %}
Wenn Sie Liquid verwenden möchten, stellen Sie sicher, dass Sie einen Standardwert für die von Ihnen gewählte Personalisierung angeben, damit der Empfänger keine Nachricht erhält, falls sein Benutzerprofil unvollständig ist. 
{% endraw %}
{% endalert %}

![Das Tool Personalisierung hinzufügen mit dem Attribut "first_name" und dem Standardwert "you".][2]{: style="max-width:80%;"}

#### Dynamische Links 

CTA-URLs können Variablen enthalten. Meta verlangt jedoch, dass diese wie bei `{% raw %}https://example.com/{{variable}}{% endraw %}` am Ende der URL stehen, wo sie dann in Braze durch Liquid ersetzt werden kann. Links können auch als Teil des Textes in Templates aufgenommen werden. Zur Zeit kann keiner dieser Links gekürzt werden. 

#### Responsive Nachrichten

Mit responsiven Nachrichten können Sie auf eingehende Nutzeranfragen antworten. Sie werden in Braze erstellt und können jederzeit bearbeitet werden. Sie können Liquid verwenden, um die Formulierung der responsiven Nachrichten anzupassen.

Es gibt drei Layouts für Nachrichten, die Sie verwenden können:
- Quick Reply
- Textnachricht
- Mediennachricht

![Der Nachrichten-Editor für eine Antwortnachricht mit mit einem Rabattcode für Neuanmeldungen.][6]{: style="max-width:80%;"}

### Schritt 3: Nachricht prüfen und testen

Braze empfiehlt Ihnen, Ihre Nachricht vor dem Versenden in der Vorschau anzusehen und zu testen. Wechseln Sie auf die Registerkarte **Test**, um eine Test-WhatsApp-Nachricht an [Inhaltstestgruppen]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) oder einzelne Benutzer zu senden, oder um eine Vorschau der Nachricht als Benutzer direkt in Braze anzuzeigen.

![Eine Vorschaunachricht für einen bestehenden Benutzer namens Suzanne.][3]{: style="max-width:80%;"}

{% alert note %}
Ein Konversationsfenster ist erforderlich, um Antwort- und Testnachrichten zu senden. Um ein Konversationsfenster zu initiieren, senden Sie eine WhatsApp-Nachricht an die Telefonnummer, die mit der Abonnementgruppe verbunden ist, die Sie für diese Nachricht verwenden. Die zugehörige Telefonnummer wird in der Benachrichtigung auf der Registerkarte **Test** aufgeführt.
{% endalert %}

![Eine Meldung, die besagt: "Öffnen Sie für Tests zunächst ein Konversationsfenster, indem Sie eine WhatsApp Nachricht an +1 631-202-0907 senden. Senden Sie dann Ihre Antwortnachricht an den Testbenutzer."][7]{: style="max-width:80%;"}

### Schritt 4: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas

{% tabs %}
{% tab Kampagne %}

Nun bauen Sie die weitere Kampagne auf. In den folgenden Abschnitten finden Sie weitere Einzelheiten darüber, wie Sie unsere Tools am besten für die Erstellung von WhatsApp-Nachrichten verwenden.

#### Wählen Sie einen Zustellungszeitplan oder einen Auslöser

WhatsApp-Nachrichten können anhand von Zeitplan, Aktion oder API-Trigger zugestellt werden. Mehr dazu erfahren Sie unter [Planen Ihrer Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Für die aktionsbasierte Zustellung können Sie auch die Dauer der Kampagne und die [Ruhezeiten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) festlegen.

In diesem Schritt können Sie auch Zustellungskontrollen festlegen, z. B. dass Nutzer:innen [wieder für]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) den Empfang der Kampagne [zugelassen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) werden oder [Frequency-Capping-Regeln]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) aktiviert werden.

#### Wählen Sie Benutzer als Zielgruppe aus

Als Nächstes müssen Sie mithilfe von Segmenten oder Filtern eine [Zielgruppe erstellen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/). Sie sollten bereits die Abonnementgruppe ausgewählt haben, die die Nutzer nach der Ebene oder Kategorie der Kommunikation mit Ihnen eingrenzt. In diesem Schritt wählen Sie die größere Zielgruppe aus Ihren Segmenten aus und grenzen dieses Segment mit unseren Filtern weiter ein. Sie erhalten automatisch einen Überblick über die ungefähre Zusammensetzung dieses Segments. Denken Sie daran, dass die genaue Segmentzugehörigkeit immer erst kurz vor dem Nachrichtenversand berechnet wird.

#### Wählen Sie Konversionsereignisse aus

 Sie können ein Zeitfenster von bis zu 30 Tagen zulassen, in dem eine Konversion gezählt wird, wenn die angegebene Aktion durchgeführt wird.

Sie können auch benutzerdefinierte Konvertierungsereignisse für Ihren speziellen Anwendungsfall festlegen. Werden Sie kreativ und überlegen Sie, wie Sie den Erfolg dieser Kampagne wirklich messen wollen.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, füllen Sie die restlichen Abschnitte der Canvas-Komponente aus. Weitere Einzelheiten zum Aufbau des restlichen Canvas, zur Implementierung von multivariaten Tests und intelligenter Auswahl und mehr finden Sie im Schritt [Aufbau Ihres Canvas]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/) in unserer Canvas-Dokumentation.

Da Konversationsfenster nur 24 Stunden pro eingehender Nachricht dauern können, prüft Braze, ob zwischen einer eingehenden Nachricht und einer Antwortnachricht eine Verzögerung von mehr als 24 Stunden besteht. 

{% endtab %}
{% endtabs %}

### Schritt 5: Überprüfen und einsetzen

Nachdem Sie den letzten Teil Ihrer Kampagne oder Ihres Canvas erstellt haben, überprüfen Sie die Details, testen Sie sie und senden Sie sie ab!

Sehen Sie sich als nächstes die [WhatsApp-Berichterstattung]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics/) an, um zu erfahren, wie Sie auf die Ergebnisse Ihrer WhatsApp-Kampagnen zugreifen können.

## Unterstützte WhatsApp-Funktionen

### Ausgehende Nachrichten



|  | Details |  |  |
| ------- | ------- | ------------- | ---------------------- |
|  |  |  | 
| Haupttext |  |  |  |
| Text in der Fußzeile |  |  |  |
|  |   |  |  |
|  |   |  |  |
|  |   |  |  |
|  |   |  |  |
|  |   |  |  |


 

### Eingehende Nachrichten



|  | Details |  |
| ------- | ------- | ------------------ |
| Haupttext |  |  |
|  |   |  |
| Audio |   |  |
| Dokumente |  |  |
| Video | Nur H.264 Video Codec und AAC Audio Codec werden unterstützt.  |  |
|  |   |  |


### 



| CTA-Typ    | Details |
| ----------- |---------------- | 
| Website besuchen | Maximal eine Taste (einschließlich variabler Parameter). |
| Telefonnummer anrufen | Nur für Nachrichtenvorlagen verfügbar. <br>Maximal eine Taste. |
| Benutzerdefinierte Schnellantwort-Schaltflächen | Maximal drei Tasten. |
| Opt-in Button für Marketing |   |
| Nachrichtenvorlagen für Gutscheincodes | Nur für Nachrichtenvorlagen verfügbar. <br>Diese können wie andere Nachrichtenvorlagen geöffnet und bearbeitet werden und sind mit Liquid- und Braze-Aktionscodes kompatibel. |
| CTA-Antwortnachrichten  | Erstellen Sie eine Nachricht mit einem Aktionsbutton. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[1]: {% image_buster /assets/img/whatsapp/whatsapp6.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp7.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp8.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp_plain_text.png %}
[5]: {% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}
[6]: {% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}
[7]: {% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}
[8]: {% image_buster /assets/img/whatsapp/whatsapp_templates.png %}
