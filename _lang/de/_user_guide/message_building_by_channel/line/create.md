---
nav_title: Erstellen einer LINE Nachricht
article_title: Erstellen einer LINE-Nachricht
page_order: 1
description: "Dieser Artikel beschreibt, wie Sie eine LINE Nachrichten-Kampagne oder ein Canvas erstellen."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# Erstellen einer LINE Nachricht

> Mit LINE-Kampagnen können Sie Ihre Kunden direkt erreichen und programmgesteuert mit ihnen chatten. Sie können Liquid und andere dynamische Inhalte verwenden, um ein persönliches Erlebnis mit Ihren Nutzern zu schaffen und eine Umgebung zu schaffen, die ein unaufdringliches Nutzererlebnis mit Ihrer Marke fördert und verbessert.

## Voraussetzungen

Bevor Sie eine LINE-Nachricht erstellen, gehen Sie wie folgt vor:

1. Lesen Sie die LINE-Übersicht.
2. Erkennen Sie Richtlinien, Einschränkungen und Inhaltsregeln an.
3. [Richten Sie Ihre LINE-Verbindung ein]({{site.basesurl}}/user_guide/message_building_by_channel/line/line_setup/).

Wenn Sie LINE-Nachrichten von Braze aus versenden, wird das Nachrichtenguthaben Ihres Kontos verbraucht.

## Schritt 1: Wählen Sie, wo Sie Ihre Botschaft aufbauen möchten

Sie sind sich nicht sicher, ob Ihre Nachricht über eine Kampagne oder ein Canvas versendet werden soll? Kampagnen eignen sich eher für einzelne einfache Messaging-Kampagnen, während Canvases besser für mehrstufige User Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}

**Schritte:**

1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**.
2. Wählen Sie **LINE**, oder für Kampagnen, die auf mehrere Kanäle abzielen, wählen Sie **Multichannel-Kampagne**.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu.
   * Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen.
5. Fügen Sie so viele Varianten hinzu, wie Sie für Ihre Kampagne benötigen, und benennen Sie sie. Sie können für jede hinzugefügte Variante verschiedene Plattformen, Nachrichtentypen und Layouts auswählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

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

## Schritt 2: Verfassen Sie Ihre LINE-Nachricht

Schreiben Sie Ihre Nachricht nach Bedarf mit Personalisierung (z. B. Liquid oder Connected-Content). LINE lässt bis zu fünf Sprechblasen pro Nachricht zu, die in einem der verfügbaren Nachrichten-Layouts erscheinen können: Text, Bild, Rich oder Card-based.

![LINE-Editor mit einer Nachricht, die in der Vorschau angezeigt wird.]({% image_buster /assets/img/line/line_composer.png %})

### Tipps

#### Liquid verwenden

Wenn Sie Liquid verwenden möchten, stellen Sie sicher, dass Sie einen Standardwert für Ihre Personalisierung angeben. Dadurch wird verhindert, dass Empfänger mit unvollständigen Benutzerprofilen einen leeren Platzhalter erhalten. Zum Beispiel könnte ein:e Nutzer:in statt der Nachricht "Hallo!" die Nachricht "Hallo, neue:r Abonnent:in!" erhalten.

#### Erstellen von Nachrichten von rechts nach links

Wie Nachrichten von rechts nach links letztendlich aussehen, hängt weitgehend davon ab, wie die Diensteanbieter sie darstellen. Bewährte Methoden zur Erstellung von Nachrichten, die so genau wie möglich angezeigt werden, finden Sie unter [Erstellen von Nachrichten von]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) rechts nach links.

## Schritt 3: Vorschau und Test Ihrer Nachricht

Wechseln Sie auf die Registerkarte **Test**, um eine Test-LINE-Nachricht an Inhaltstestgruppen oder einzelne Benutzer zu senden oder eine Vorschau der Nachricht als Benutzer direkt in Braze anzuzeigen.

![Der Tab "Tests" zeigt eine Vorschau auf eine Testnachricht an.]({% image_buster /assets/img/line/test_preview.png %})

## Schritt 4: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas

{% tabs %}
{% tab Campaign %}

Bauen Sie den Rest Ihrer Kampagne auf. In den folgenden Abschnitten erfahren Sie mehr darüber, wie Sie unsere Tools zur Erstellung von LINE-Nachrichten am besten einsetzen.

### Wählen Sie einen Zeitplan für die Zustellung oder triggern Sie

LINE-Nachrichten können basierend auf einer geplanten Zeit, einer Aktion oder einem API-Auslöser zugestellt werden. Weitere Informationen über Zeitpläne und Trigger-Optionen finden Sie unter [Ihre Kampagne planen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Sie können die Zustellung steuern, z. B. indem Sie Nutzer:innen erlauben, [sich erneut für den Empfang der Kampagne zu qualifizieren]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns), oder indem Sie [Frequency-Capping-Regeln]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) einschalten. Für die aktionsbasierte Zustellung können Sie auch die Dauer der Kampagne und die [Ruhezeiten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) festlegen.

### Wählen Sie Nutzer:innen als Zielgruppe aus

[Stellen Sie Nutzer:innen durch die Auswahl von Segmenten oder Filtern gezielt zusammen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/), um Ihre Zielgruppe einzugrenzen. Sie sollten bereits die Abonnementgruppe ausgewählt haben, die die Nutzer nach der Ebene oder Kategorie der Kommunikation mit Ihnen eingrenzt. 

Wählen Sie die größere Zielgruppe aus Ihren Segmenten aus und grenzen Sie dieses Segment optional mit unseren [Filtern]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) weiter ein. Sie erhalten automatisch einen Überblick über die ungefähre Zusammensetzung dieses Segments. Denken Sie daran, dass die genaue Segmentzugehörigkeit immer erst kurz vor dem Versand der Nachricht berechnet wird.

### Wählen Sie Konversions-Events aus

Mit Braze können Sie nachverfolgen, wie oft Benutzer nach Erhalt einer Kampagne bestimmte Aktionen, d.h. [Conversion Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), durchführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen zuzulassen, in dem eine Konversion gezählt wird, wenn der Nutzer:innen die angegebene Aktion durchführt.

Konversions-Events helfen Ihnen, den Erfolg Ihrer Kampagnen zu messen. Zum Beispiel:

- Wenn Sie Geotargeting verwenden, um eine LINE-Nachricht zu triggern, deren Ziel es ist, dass die:der Nutzer:in einen Kauf tätigt, setzen Sie das Konversions-Event auf ein `Purchase`.
- Wenn Sie versuchen, die:den Nutzer:in zu Ihrer App zu bringen, setzen Sie das Konversions-Event auf `Starts Session`.

Sie können auch benutzerdefinierte Konvertierungsereignisse für Ihren speziellen Anwendungsfall festlegen. Werden Sie kreativ und überlegen Sie, wie Sie den Erfolg dieser Kampagne messen wollen.

{% endtab %}
{% tab Canvas %}

Falls Sie das noch nicht getan haben, füllen Sie die restlichen Abschnitte Ihres Canvas aus. Weitere Einzelheiten zum Aufbau des restlichen Canvas, zur Verwendung von multivariaten Tests und intelligenter Auswahl und mehr finden Sie unter [Erstellen eines Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

{% endtab %}
{% endtabs %}

## Schritt 5: Überprüfen und einsetzen

Nachdem Sie den letzten Teil Ihrer Kampagne oder Ihres Canvas erstellt haben, überprüfen Sie die Details, testen Sie sie und senden Sie sie ab!

Sehen Sie sich als nächstes die [LINE-Berichterstattung]({{site.baseurl}}/line/reporting/) an, um zu erfahren, wie Sie auf die Ergebnisse Ihrer LINE-Kampagnen zugreifen können.


