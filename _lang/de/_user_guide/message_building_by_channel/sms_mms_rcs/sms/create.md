---
nav_title: Erstellen einer SMS-Nachricht
article_title: Erstellen einer SMS-Nachricht
page_order: 5
description: "In diesem Referenzartikel werden die einzelnen Schritte zur Erstellung einer SMS-Nachricht beschrieben."
page_type: reference
alias: /create_sms_message/
tool:
  - Campaigns
channel:
  - SMS
search_rank: 1
---

# Erstellen einer SMS-Nachricht

> SMS-Kampagnen eignen sich hervorragend, um Ihre Kunden direkt zu erreichen und programmgesteuert mit ihnen zu kommunizieren. Sie können Liquid und andere dynamische Inhalte verwenden, um ein persönliches Erlebnis mit Ihren Nutzern zu schaffen und eine Umgebung zu schaffen, die ein unaufdringliches Nutzererlebnis mit Ihrer Marke fördert und verbessert. 

## Schritt 1: Wählen Sie, wo Sie Ihre Botschaft aufbauen möchten

Sie sind sich nicht sicher, ob Ihre Nachricht über eine Kampagne oder ein Canvas versendet werden soll? Kampagnen eignen sich eher für einzelne einfache Messaging-Kampagnen, während Canvases besser für mehrstufige User Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}

**Schritte:**

1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**.
2. Wählen Sie **SMS**, oder für Kampagnen, die auf mehrere Kanäle abzielen, wählen Sie **Multichannel**.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu.
   * Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen. Wenn Sie zum Beispiel den [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.
5. Fügen Sie so viele Varianten hinzu, wie Sie für Ihre Kampagne benötigen, und benennen Sie sie. Sie können für jede hinzugefügte Variante verschiedene Plattformen, Nachrichtentypen und Layouts auswählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
6. Wählen Sie eine [Abonnementgruppe]({{site.baseurl}}/sms_rcs_subscription_groups/), um sicherzustellen, dass Sie Ihre Nachricht an die richtigen Benutzer senden. Wenn Sie eine Abo-Gruppe auswählen, fügt Braze automatisch einen Filter zur Segmentierung hinzu, der sicherstellt, dass nur Nutzer:innen die Kampagne erhalten. Nur lange Codes und kurze Codes, die zu dieser Abonnementgruppe gehören, werden für den Versand von SMS an die Zielbenutzer verwendet.

{% alert tip %}
Wenn alle Nachrichten in Ihrer Kampagne ähnlich sind oder den gleichen Inhalt haben, sollten Sie Ihre Nachricht verfassen, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann aus der Dropdown-Liste **Variante hinzufügen** die Option **Aus Variante kopieren** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Schritte:**

1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) mit dem Canvas Composer.
2. Wenn Sie den Canvas eingerichtet haben, fügen Sie im Canvas Builder einen Schritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie einen [Zeitplan für den Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) und geben Sie bei Bedarf eine Verzögerung an.
4. Filtern Sie Ihre Zielgruppe für diesen Schritt nach Bedarf. Sie können den Empfängerkreis mit Segmenten und zusätzlichen Filtern weiter eingrenzen. Die Zielgruppenoptionen werden mit einer gewissen Verzögerung zum Versandzeitpunkt überprüft.
5. Legen Sie das [Fortschrittsverhalten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) fest.
6. Wählen Sie weitere Messaging-Kanäle für Ihre Nachricht aus.

{% endtab %}
{% endtabs %}

## Schritt 2: Verfassen Sie Ihre SMS-Nachricht

Schreiben Sie Ihre Nachricht in der gewünschten Sprache und mit der gewünschten Personalisierung (Liquid, Connected Content und Emojis). Achten Sie darauf, dass Sie unsere Obergrenzen für Nachrichtenkopien einhalten, um das Risiko von Mehrkosten zu verringern.

{% alert important %}
Bevor Sie fortfahren, lesen Sie unsere Richtlinien für [SMS-Nachrichtensegmente und Kopier-Limits]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/). SMS-Nachrichtensegmente sind die Zeichenpakete, die die Telefongesellschaften zur Messung von Textnachrichten verwenden. Nachrichten werden pro Nachrichtensegment abgerechnet. Es ist also eine gute Idee, die Feinheiten der Aufteilung von Nachrichten zu verstehen.
{% endalert %}

![SMS-Komponist in Braze mit der Nachricht "Hallo first_name, wir schätzen Ihre Unterstützung! Warum kommen Sie nicht in eine unserer Filialen und zeigen diese SMS vor, um einen exklusiven Rabatt zu erhalten? Antworten Sie STOP, um keine Nachrichten mehr von uns zu erhalten."]({% image_buster /assets/img/sms_campaign_compose.png %})

### Hinzufügen einer Kontaktkarte

Sie können Ihrer SMS Nachricht eine Kontaktkarte hinzufügen, damit Ihre Kund:innen Ihr Unternehmen und Ihre Kontaktinformationen einfach zu ihren Kontakten hinzufügen können. Sie können diesen Karten allgemeine Eigenschaften zuweisen, z. B. den Namen Ihres Unternehmens, Telefonnummer, Adresse, E-Mail und ein kleines Foto. Weitere Informationen finden Sie unter [Kontaktkarten]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/).

### Tipps

#### Liquid verwenden

{% raw %}
Wenn Sie Liquid verwenden möchten, stellen Sie sicher, dass Sie einen Standardwert für die von Ihnen gewählte Personalisierung angeben, damit der Empfänger im Falle eines unvollständigen Benutzerprofils nicht einen leeren Platzhalter `Hi, !` anstelle seines Namens oder eines zusammenhängenden Satzes erhält.
{% endraw %}

#### KI-Kopie generieren

Benötigen Sie Hilfe bei der Erstellung überzeugender Texte? Versuchen Sie es mit dem [KI-Textwerkstatt-Assistenten]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Geben Sie einen Produktnamen oder eine Beschreibung ein und die KI generiert menschenähnliche Marketingtexte für Ihre Werbebotschaften.

![KI Copywriter Button starten, der sich im Nachrichten-Feld des SMS-Editors befindet.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### Erstellen von Nachrichten von rechts nach links

Wie Nachrichten von rechts nach links letztendlich aussehen, hängt weitgehend davon ab, wie die Diensteanbieter sie darstellen. Bewährte Methoden zur Erstellung von Nachrichten, die so genau wie möglich angezeigt werden, finden Sie unter [Erstellen von Nachrichten von]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) rechts nach links.

## Schritt 3: Nachricht in der Vorschau anzeigen und testen

Braze empfiehlt immer, Ihre Nachricht vor dem Versand in der Vorschau zu prüfen. Wechseln Sie auf die Registerkarte **Test**, um eine Test-SMS an [Inhaltstestgruppen]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) oder einzelne Benutzer zu senden, oder um eine Vorschau der Nachricht als Benutzer direkt in Braze anzuzeigen.

Vorschau der SMS-Kopie auf dem Tab Test des Composers. Im Profilbereich ist das Feld „Vorname“ auf „James“ eingestellt. In der Vorschau lautet die SMS jetzt "Hallo James, wir wissen Ihre Unterstützung zu schätzen!"]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert tip %}
Wenn Sie testen möchten, in wie viele Segmente Ihre SMS aufgeteilt werden kann, testen Sie die Länge Ihres Textes mit unserem [SMS-Segment-Rechner]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).
{% endalert %}

## Schritt 4: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas

{% tabs %}
{% tab Campaign %}

Als Nächstes erstellen Sie den Rest Ihrer Kampagne. In den folgenden Abschnitten erfahren Sie mehr darüber, wie Sie unsere Tools zur Erstellung von SMS-Nachrichten am besten einsetzen.

#### Wählen Sie einen Zeitplan für die Zustellung oder triggern Sie

SMS-Nachrichten können basierend auf einer geplanten Zeit, einer Aktion oder einem API-Auslöser zugestellt werden. Mehr dazu erfahren Sie unter [Planen Ihrer Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Für die aktionsbasierte Zustellung können Sie auch die Dauer der Kampagne und die [Ruhezeiten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) festlegen.

In diesem Schritt können Sie auch Zustellungskontrollen festlegen, z. B. dass Nutzer:innen wieder für den Empfang der Kampagne [zugelassen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) werden oder [Frequency-Capping-Regeln]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) aktiviert werden.

#### Wählen Sie Benutzer als Zielgruppe aus

Als Nächstes müssen Sie mithilfe von Segmenten oder Filtern eine [Zielgruppe erstellen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/). Sie sollten bereits die Abonnementgruppe ausgewählt haben, die die Nutzer nach der Ebene oder Kategorie der Kommunikation mit Ihnen eingrenzt. 

{% multi_lang_include target_audiences.md %}

In diesem Schritt wählen Sie die größere Zielgruppe aus Ihren Segmenten aus und grenzen dieses Segment mit unseren Filtern weiter ein, wenn Sie möchten. Sie erhalten automatisch eine Vorschau darauf, wie die ungefähre Anzahl der Segmente im Moment aussieht. Denken Sie daran, dass die genaue Segmentzugehörigkeit immer erst kurz vor dem Versand der Nachricht berechnet wird.

{% alert tip %}
Interessieren Sie sich für SMS-Retargeting? Besuchen Sie unseren [Artikel über SMS-Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/), um mehr zu erfahren.
{% endalert %}

#### Wählen Sie Konversionsereignisse aus

Mit Braze können Sie nachverfolgen, wie oft Benutzer nach Erhalt einer Kampagne bestimmte Aktionen, d.h. [Conversion Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), durchführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen zuzulassen, in dem eine Konversion gezählt wird, wenn der Nutzer:innen die angegebene Aktion durchführt.

Konversions-Events helfen Ihnen, den Erfolg Ihrer Kampagnen zu messen. Zum Beispiel:

- Wenn Sie Geotargeting verwenden, um eine SMS Nachricht auszulösen, deren Endziel ein Kauf durch den Nutzer:innen ist, setzen Sie das Konversions-Event auf `Purchase`.
- Wenn Sie versuchen, den Nutzer:innen zu Ihrer App zu bringen, setzen Sie das Konversions-Event auf `Starts Session`.

Sie können auch benutzerdefinierte Konvertierungsereignisse für Ihren speziellen Anwendungsfall festlegen. Werden Sie kreativ und überlegen Sie, wie Sie den Erfolg dieser Kampagne wirklich messen wollen.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, füllen Sie die restlichen Abschnitte der Canvas-Komponente aus. Weitere Einzelheiten zum Aufbau des restlichen Canvas, zur Implementierung von multivariaten Tests und intelligenter Auswahl und mehr finden Sie im Schritt [Aufbau Ihres Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) in unserer Canvas-Dokumentation.

{% endtab %}
{% endtabs %}

## Schritt 5: Überprüfen und einsetzen

Nachdem Sie den letzten Teil Ihrer Kampagne oder Ihres Canvas erstellt haben, überprüfen Sie die Details, testen Sie sie und senden Sie sie ab!

Sehen Sie sich als nächstes die [SMS-Berichterstattung]({{site.baseurl}}/sms_mms_rcs_reporting/) an, um zu erfahren, wie Sie auf die Ergebnisse Ihrer SMS-Kampagnen zugreifen können.
