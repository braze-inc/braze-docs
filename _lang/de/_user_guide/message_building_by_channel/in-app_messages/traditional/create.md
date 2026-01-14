---
nav_title: In-App-Nachrichten erstellen
article_title: In-App-Nachrichten erstellen
page_order: 1
description: "Dieser Artikel beschreibt, wie Sie mit Braze In-App-Nachrichten per Kampagne oder Canvas erstellen."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
toc_headers: h2
---

# In-App-Nachrichten erstellen

> In Braze können Sie In-App- und In-Browser-Nachrichten per Kampagne, Canvas oder API-Kampagne erstellen. Wir empfehlen Ihnen dringend, Ihre Nachrichten zu planen und alle Materialien im Voraus vorzubereiten, indem Sie unseren praktischen [In-App-Leitfaden zur Nachrichtenvorbereitung]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) verwenden.

## Schritt 1: Entscheiden Sie, wo Sie die Nachricht erstellen {#create-new-campaign-in-app}

Sie sind sich nicht sicher, ob Ihre Nachricht über eine Kampagne oder ein Canvas versendet werden soll? Kampagnen eignen sich eher für einzelne einfache Messaging-Kampagnen, während Canvases besser für mehrstufige User Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}

1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**.
2. Wählen Sie **In-App-Nachricht**. Beachten Sie, dass In-App-Nachrichten bei Multichannel-Kampagnen nicht möglich sind.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu.
   * Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen. Wenn Sie zum Beispiel den [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.
5. Fügen Sie so viele Varianten hinzu, wie Sie für Ihre Kampagne benötigen, und benennen Sie sie. Sie können für jede hinzugefügte Variante verschiedene Plattformen, Nachrichtentypen und Layouts auswählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Kampagne ähnlich sind oder den gleichen Inhalt haben, sollten Sie Ihre Nachricht verfassen, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann aus der Dropdown-Liste **Variante hinzufügen** die Option **Aus Variante kopieren** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) mit dem Canvas Composer.
2. Wenn Sie den Canvas eingerichtet haben, fügen Sie im Canvas Builder einen Schritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie einen [Zeitplan für den Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) und geben Sie bei Bedarf eine Verzögerung an. Beachten Sie, dass Schritte mit In-App-Nachrichten nicht aktionsbasiert sein können.
4. Filtern Sie ggf. Ihre Zielgruppe für diesen Schritt. Sie können den Empfängerkreis mit Segmenten und zusätzlichen Filtern weiter eingrenzen. Die Zielgruppen-Optionen werden nach dem Delay, zum Zeitpunkt des Versands der Nachrichten, überprüft.
5. Legen Sie das [Fortschrittsverhalten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) fest.
6. Wählen Sie weitere Messaging-Kanäle für Ihre Nachricht aus.

{% alert important %}
Sie können nicht mehrere Varianten von In-App-Nachrichten in einem einzigen Schritt haben.
{% endalert %}

Weitere Canvas-spezifische Informationen finden Sie unter [In-App-Nachrichten in Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Schritt 2: Zustellungsplattformen angeben

Wählen Sie zunächst aus, welche Plattformen die Nachricht erhalten sollen. Mit dieser Auswahl können Sie die Zustellung von Kampagnen auf bestimmte Apps beschränken. Sie könnten zum Beispiel **Webbrowser** für eine In-Browser-Nachricht wählen, die den Nutzer dazu auffordert, Ihre mobile App herunterzuladen, um sicherzustellen, dass er die Nachricht nicht erhält, nachdem er Ihre App bereits erhalten hat. Da die Plattformauswahl variantenspezifisch ist, können Sie das Engagement so auch auf den einzelnen Plattformen prüfen.

| Plattform                        | Zustellung        |
|---------------------------------|-------------------------|
| Mobile Apps                     | iOS & Android SDKs      |
| Webbrowser                    | Web SDK                 |
| Beide Mobile Apps & Webbrowser | iOS, Android & Internet SDKs |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Schritt 3: Nachrichtentyp auswählen

Sobald Sie eine Versandplattform ausgewählt haben, können Sie passende Nachrichtentypen, Layouts und andere Optionen durchsuchen. Erfahren Sie mehr über das erwartete Verhalten und das Aussehen jeder dieser Nachrichten auf unserer Seite [Kreative Details]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/), oder indem Sie auf die verlinkten Nachrichtentypen in den folgenden Tabellen klicken.

Wenn Sie sich für einen Nachrichtentyp entscheiden, bedenken Sie, wie viel Platz Ihre Nachricht beansprucht und wie störend sie sich auf die Nutzer:innen auswirken kann.

- **Slideup** Nachrichten sind am wenigsten aufdringlich, da sie unauffällig erscheinen, ohne Inhalte zu blockieren.
- **Modale** Nachrichten sitzen in der Mitte - prominent genug, um Aufmerksamkeit zu erregen, ohne den Bildschirm vollständig einzunehmen.
- Nachrichten **im Vollbildmodus** sind am aufmerksamkeitsstärksten und eignen sich am besten für wichtige Ankündigungen oder Aktionen.

Je komplexer Ihre Inhalte sind, desto mehr Platz benötigen Sie - und desto wahrscheinlicher ist es, dass Ihre Nachricht den Fluss der Nutzer:innen unterbricht.

### Nachrichtentypen

Diese In-App-Nachrichten werden sowohl von mobilen Apps als auch von Webanwendungen akzeptiert.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Nachrichtentyp</th>
    <th>Typ</th>
    <th>Verfügbare Layouts</th>
    <th>Andere Optionen</th>
    <th>Empfohlene Verwendung</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen'>Vollbild</a></td>
    <td>Nachrichten, die den gesamten Bildschirm mit einem Nachrichtenblock bedecken.</td>
    <td>
      <ul>
      <li>Bild und Text</li>
      <li>Nur Bild</li>
      </ul>
    </td>
    <td>Erzwungene Geräteausrichtung (Hoch- oder Querformat)</td>
    <td>Dick und deutlich Verwenden Sie diese Funktion, wenn Sie sicherstellen möchten, dass Ihre Nutzer Ihre Inhalte sehen, z. B. bei Ihren wichtigsten Kampagnen, wichtigen Benachrichtigungen oder umfangreichen Werbeaktionen.<br><br>Beachten Sie, dass Nachrichten im Hoch- und Querformat auf mobilen Geräten nicht angezeigt werden, wenn die Ausrichtung des Geräts nicht mit der Ausrichtung der Nachricht übereinstimmt.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal'>Modal</a></td>
    <td>Nachrichten, die den gesamten Bildschirm mit einem Bildschirm-Overlay und einem Nachrichtenblock bedecken.</td>
    <td>
      <ul>
      <li>Text (mit optionalem Bild)</li>
      <li>Nur Bild</li>
      </ul>
    </td>
    <td>--</td>
    <td>Ein guter Mittelweg. Verwenden Sie diese Option, wenn Sie die Aufmerksamkeit Ihrer Nutzer auf eine offensichtliche Art und Weise auf sich ziehen möchten, z. B. um sie zu ermutigen, eine neue Funktion auszuprobieren oder eine Werbeaktion zu nutzen.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup'>Slideup</a></td>
    <td>Nachrichten, die an einer bestimmten Stelle eingeblendet werden, ohne den Rest des Bildschirms zu verdecken.</td>
    <td>--</td>
    <td>--</td>
    <td>Unauffällig - nimmt so wenig Platz wie möglich auf dem Bildschirm ein. Verwenden Sie diese Option, wenn Sie Benutzer auf kleine Informationsschnipsel aufmerksam machen möchten, z. B. auf neue Funktionen, Ankündigungen, die Verwendung von Cookies usw.<br></td>
  </tr>
</tbody>
</table>

### Erweiterte Nachrichtentypen

Diese In-App-Nachrichten sind an Ihre Bedürfnisse anpassbar.

<table class="tg">
<thead>
  <tr>
    <th>Nachrichtentyp</th>
    <th>Typ</th>
    <th>Verfügbare Layouts</th>
    <th>Anforderungen</th>
    <th>Empfohlene Verwendung</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages'>Benutzerdefinierte HTML-Nachricht</a></td>
    <td>Benutzerdefinierte Nachrichten, die sich so verhalten, wie in Ihrem benutzerdefinierten Code (HTML, CSS und/oder JavaScript) definiert.</td>
    <td>--</td>
    <td>Muss eingestellt werden <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> auf <code>true setzen</code>, damit Ihre In-App-Nachricht funktioniert.</td>
    <td>Dies ist eine gute Option, wenn Sie alle Vorteile von IAMs nutzen möchten, aber zusätzliche Funktionen benötigen oder das Erscheinungsbild zu Ihrer Marke passen soll. Sie können jedes kleine Detail der Nachricht ändern - Schriftart, Farbe, Form, Größe, Schaltflächen usw. <br><br>Anwendungsfälle sind z.B. die Abfrage von Nutzer:innen für App-Feedback, E-Mail-Erfassungsformulare oder paginierte Nachrichten.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>Formular zur E-Mail-Erfassung</a></td>
    <td>Wird in der Regel verwendet, um die E-Mail-Adresse des Betrachters zu erfassen.</td>
    <td>--</td>
    <td>Muss eingestellt werden <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> auf <code>true setzen</code>, damit Ihre In-App-Nachricht funktioniert.</td>
    <td>Wenn Sie Nutzer:innen auffordern, ihre E-Mail Adresse anzugeben.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css'>Web-Modal mit CSS</a></td>
    <td>Modale Nachrichten für das Web mit anpassbarem CSS.</td>
    <td>
      <ul>
      <li>Text (mit optionalem Bild)</li>
      <li>Nur Bild</li>
      </ul>
    </td>
    <td>Web Modal mit CSS ist einzigartig für das Web SDK und kann nur nach Auswahl von <b>Web Browsern</b> verwendet werden.</td>
    <td>Wenn Sie benutzerdefinierte CSS hochladen oder schreiben möchten, um schöne, rundum individuell gestaltete Nachrichten zu erstellen. </td>
  </tr>
</tbody>
</table>

{% alert important %}
Wenn Braze feststellt, dass Ihr Code keine Schaltfläche zum Schließen oder Verlassen enthält, fordern wir Sie auf, eine solche hinzuzufügen. Zu Ihrer Erleichterung haben wir ein Snippet bereitgestellt, das Sie kopieren und in Ihren Code einfügen können: <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Schritt 4: Verfassen Sie Ihre In-App-Nachricht

Auf der Registerkarte **Verfassen** können Sie alle Aspekte des Inhalts und Verhaltens Ihrer Nachricht bearbeiten.

![Eine beispielhafte In-App-Nachricht einer Marke, um neue Kunden zu begrüßen und sie aufzufordern, ein Nutzerprofil einzurichten.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

Der Inhalt der Registerkarte **Verfassen** hängt von den im vorherigen Schritt gewählten Nachrichtenoptionen ab, kann aber eine der folgenden Optionen enthalten:

### Sprache

Wählen Sie **Sprachen hinzufügen** und wählen Sie die gewünschten Sprachen aus der vorgegebenen Liste aus. Dadurch wird [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) in Ihre Nachricht eingefügt. Wir empfehlen, die Sprachen auszuwählen, bevor Sie den Inhalt verfassen, damit Sie Ihren Text dort einfügen können, wo er im Liquid hingehört. Sehen Sie sich unsere [vollständige Liste der verfügbaren Sprachen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported) an.

### Bild

Je nach Art Ihrer Nachricht können Sie **ein Bild hochladen**, **ein Abzeichen auswählen** oder **Font Awesome** verwenden. Um ein Bild hochzuladen, klicken Sie auf **Bild hinzufügen** oder geben Sie eine Bild-URL an. Wenn Sie auf **Bild hinzufügen** klicken, öffnet sich die **Mediathek**, in der Sie ein zuvor hochgeladenes Bild auswählen oder ein neues Bild hinzufügen können. Die Empfehlungen zu Maßen und Anforderungen können je nach Nachrichtentyp und Plattform unterschiedlich sein. Überprüfen Sie diese, bevor Sie ein Bild in Auftrag geben oder selbst eines erstellen.

### Kopfzeile und Körper

Werden Sie kreativ! Fügen Sie vollständig angepasste Texte ein (oft mit angepassten HTML-Funktionen) mit der Möglichkeit, [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) und andere Arten der Personalisierung einzubinden. Je schneller Sie Ihre Botschaft vermitteln und Ihren Kunden zum Klicken bringen können, desto besser! Wir empfehlen klare und prägnante Überschriften und Nachrichteninhalte.

Einige Nachrichtentypen benötigen keine Kopfzeilen und fragen daher auch nicht nach diesen.

#### Tipps 

##### KI-Kopie generieren

Benötigen Sie Hilfe bei der Erstellung überzeugender Texte? Versuchen Sie es mit dem [KI-Textwerkstatt-Assistenten]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Geben Sie einen Produktnamen oder eine Beschreibung ein und die KI generiert menschenähnliche Marketingtexte für Ihre Werbebotschaften.

![KI Copywriter Button starten, der sich im Nachrichten-Feld des In-App-Nachricht-Editors befindet.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Erstellen von Nachrichten von rechts nach links

Benötigen Sie Hilfe bei der Erstellung von Nachrichten von rechts nach links für Sprachen wie Arabisch und Hebräisch? Lesen Sie den Abschnitt [Erstellen von Nachrichten von rechts nach links]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) für bewährte Verfahren.

### Button-Text {#buttons}

Sofern für den jeweiligen Nachrichtentyp verfügbar, können Sie bis zu zwei Buttons unter dem Text anzeigen. Sie können benutzerdefinierte Schaltflächentexte und -farben erstellen und bearbeiten. Sie können auch einen Link zu den Nutzungsbedingungen in E-Mail-Erfassungsformulare einfügen.

Wenn Sie sich entscheiden, nur eine Schaltfläche zu verwenden, wird diese automatisch so angepasst, dass sie den verfügbaren Platz am unteren Rand Ihrer Nachricht einnimmt, anstatt Platz für eine weitere Schaltfläche zu lassen.

#### Hauptschaltflächen auswählen

Wenn Sie sich dafür entscheiden, diese Schaltflächen mit Ihren eigenen Farben zu formatieren, empfehlen wir Ihnen, Schaltfläche 2 zu verwenden, um ein besseres Ergebnis zu erzielen.

Mit anderen Worten: Wenn Sie möchten, dass Ihr Benutzer mehr auf eine Schaltfläche klickt als auf eine andere, stellen Sie sicher, dass sie sich auf der rechten Seite befindet. Die rechte Schaltfläche hat oft ein größeres Potenzial, angeklickt zu werden, insbesondere wenn sie sich farblich vom Rest der Nachricht abhebt oder anderweitig hervorsticht. Dies gilt umso mehr, wenn der Button auf der linken Seite optisch stark mit der Nachricht harmoniert.

![Primäre und sekundäre Buttons in einer In-App-Nachricht]({% image_buster /assets/img/primary-secondary-buttons.png %})

### Anklickverhalten {#button-actions}

Wird ein Button in Ihrer In-App-Nachricht angeklickt, sind folgende Aktionen möglich: 

| Aktion | Beschreibung |
|---|---|
| Weiterleitung zu Web-URL | Öffnen Sie eine nicht-native Webseite. |
| [Deeplink in die App]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Setzt einen Deeplink in einen Bildschirminhalt der App. |
| Nachricht schließen | Schließt die derzeit aktive Nachricht. |
| Angepasstes Event protokollieren | Wählen Sie ein [benutzerdefiniertes Ereignis]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) zum Auslösen. Kann verwendet werden, um eine weitere In-App-Nachricht anzuzeigen oder eine zusätzliche Benachrichtigung auszulösen. |
| Angepasstes Attribut protokollieren | Wählen Sie ein [benutzerdefiniertes Attribut]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), das für den aktuellen Benutzer festgelegt werden soll. |
| Push-Einwilligung anfordern | Zeigt die native Push-Erlaubnis an. Lesen Sie mehr über [Push-Priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) und die [besten Methoden]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#best-practices), um Benutzer auf Push vorzubereiten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Hinweis: Die Optionen __Push-Erlaubnis anfordern__, __Benutzerdefiniertes Ereignis protokollieren__ und __Benutzerdefiniertes Attribut protokollieren__ erfordern die folgenden SDK-Mindestversionen:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### Optionen für iOS-Geräte

Sie können In-App-Nachrichten auch nur an iOS-Geräte senden. Klicken Sie dazu auf **Ändern** und wählen Sie **Nur an iOS-Geräte senden**.

### Schließen der Nachricht

Wählen Sie zwischen den folgenden Optionen:
 
- **Automatisch ausblenden:** Wählen Sie aus, wie viele Sekunden die Nachricht auf dem Bildschirm bleiben soll.
- **Swipe oder Berührung abwarten:** Erfordert eine Option zum Verlassen oder Schließen.

### Position nach oben schieben

Diese Einstellung gilt nur für den Nachrichtentyp Slideup. Wählen Sie, ob Ihr Slideup **vom unteren Rand des App-Bildschirms** oder **vom oberen Rand des App-Bildschirms** angezeigt werden soll.

### HTML und Assets

Diese Einstellung gilt nur für den Nachrichtentyp Benutzerdefinierter Code. Kopieren und fügen Sie HTML in das freie Feld ein und laden Sie Ihre Assets als ZIP-Datei hoch.

### Platzhalter für die E-Mail-Erfassung

Diese Einstellung gilt nur für den Nachrichtentyp E-Mail-Erfassungsformular. Geben Sie einen Platzhaltertext für das E-Mail-Eingabefeld ein. Die Standardeinstellung ist "Geben Sie Ihre E-Mail-Adresse ein".

## Schritt 5: In-App-Nachricht gestalten

Auf der Registerkarte **Stil** können Sie alle visuellen Aspekte Ihrer Nachricht anpassen. Laden Sie ein Bild oder ein Abzeichen hoch, oder wählen Sie ein vorgefertigtes Abzeichen-Symbol. Ändern Sie die Farben der Kopfzeile, des Textes, der Schaltflächen und des Hintergrunds, indem Sie aus einer Palette auswählen oder einen Hex-, RGB- oder HSB-Code eingeben.

Der Inhalt der Registerkarte **Stil** hängt von den im vorherigen Schritt gewählten Nachrichtenoptionen ab, kann aber eine der folgenden Optionen enthalten:

| Formatieren | Eingabe | Beschreibung |
|---|---|---|
|[Farbprofil]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css) | Übernehmen Sie aus der Galerie der In-App-Nachricht-Vorlagen. | Wählen Sie **Template anwenden** und wählen Sie aus der Galerie. Wählen Sie dann **Speichern**. |
|Textausrichtung | Links, Mitte, oder Rechts.  | Nur für neuere Braze SDK-Versionen verfügbar. |
|Header | HEX-Farbcode. | Ihre gewünschte HEX-Farbe wird angezeigt. Sie können auch die Deckkraft der Farbe auswählen.  |
|Text | HEX-Farbcode. | Ihre gewünschte HEX-Farbe wird angezeigt. Sie können auch die Deckkraft der Farbe auswählen. |
|Buttons | HEX-Farbcode. | Ihre gewünschten HEX-Farben werden angezeigt. Sie können auch die Deckkraft der Farben auswählen. Sie können Farben wählen für: den Hintergrund der Schaltfläche Schließen der Nachricht sowie für den Hintergrund, den Text und die Umrandung der einzelnen Schaltflächen. |
| Schaltfläche Rand | HEX-Farbcode. | Neu! Auf diese Weise können Sie Ihre primären und sekundären Schaltflächen voneinander abgrenzen. Wir empfehlen, die Buttons mit kontrastierenden Farben zu umranden. |
|Hintergrundfarbe | HEX-Farbcode. | Ihre gewünschte HEX-Farbe wird angezeigt. Sie können auch die Deckkraft der Farbe auswählen. Sie bildet den Hintergrund der Nachricht und wird deutlich hinter Ihrem Textkörper angezeigt. |
|Display-Overlay | HEX-Farbcode. | Ihre gewünschte HEX-Farbe wird angezeigt. Sie können auch die Deckkraft der Farbe auswählen. Nur für neuere Braze SDK-Versionen verfügbar. Dies ist der Rahmen für die gesamte Nachricht. |
|Guillemets oder andere "Nachricht schließen"-Option | HEX-Farbcode. | Ihre gewünschte HEX-Farbe wird angezeigt. Sie können auch die Deckkraft der Farbe auswählen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Testen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) Sie Ihre Nachricht immer in der Vorschau, bevor Sie sie versenden.

{% alert important %}
Einige In-App-Nachrichtentypen haben keine Möglichkeit zur Gestaltung, die über das Hochladen von benutzerdefiniertem HTML (oder CSS oder JavaScript) und Assets in einer ZIP-Datei hinausgeht. Im [Web-Modal mit CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) können Sie eigene CSS hochladen oder schreiben, um individuell gestaltete Nachrichten zu erstellen.
{% endalert %}

## Schritt 6: Konfigurieren Sie zusätzliche Einstellungen (optional)

### Schlüssel-Wert-Paare

Sie können [Schlüssel-Wert-Paare]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) hinzufügen, um zusätzliche angepasste Felder an Nutzer:innen zu senden.

## Schritt 7: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas

{% tabs %}
{% tab Campaign %}

Erstellen Sie den Rest Ihrer Kampagne. In den folgenden Abschnitten finden Sie weitere Anleitungen, wie Sie unsere Tools zur Erstellung von In-App-Nachrichten am besten nutzen.

#### Wählen Sie einen Auslöser

Wählen Sie die Aktion, bei der Sie Ihre Nachricht auslösen möchten, sowie die Start- und Endzeit für Ihre Kampagne oder Ihr Canvas.

{% alert important %}
Beachten Sie, dass das angepasste Event über das SDK gesendet werden muss, wenn Sie Ihre In-App-Nachricht durch ein angepasstes Event triggern möchten.
{% endalert %}

![Aktionsbasierte Kampagne, bei der die Aktion triggern auf "Sitzung starten" eingestellt ist.]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

Die Zustellung von In-App-Nachrichten basiert ausschließlich auf den folgenden Aktionsauslösern:

- Kauf
- Öffnen der App/Webseite
- Ausführung eines angepassten Events (nur bei Events, die über das SDK gesendet werden)
- Öffnen einer bestimmten Push-Nachricht
- Planen Sie Kampagnen automatisch so, dass sie zu einer bestimmten Zeit unter Berücksichtigung der Ortszeit jedes Ihrer Nutzer versendet werden.
- Die Nachrichten können auch so konfiguriert werden, dass sie täglich, wöchentlich (optional an bestimmten Tagen) oder monatlich wiederkehren.

Anfangsdatum und Uhrzeit müssen ausgewählt werden, das Abschlussdatum ist optional. Ein Abschlussdatum verhindert, dass die In-App-Nachricht nach dem angegebenen Datum/Uhrzeit auf den Geräten angezeigt wird.

Informationen zur [serverseitigen Auslösung von Ereignissen]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web) und zur [lokalen Zustellung von In-App-Nachrichten]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages) finden Sie in unserer Entwicklerdokumentation.

##### Online- und Offlinetrigger

In-App-Nachrichten funktionieren, indem sie die Nachricht und die Auslöser an das Gerät des Nutzers senden. In-App-Nachrichten werden erst dann auf dem Gerät angezeigt, wenn die Triggerbedingung erfüllt ist. Wenn die In-App-Nachrichten bereits auf dem Gerät des Benutzers zwischengespeichert sind, können Sie In-App-Nachrichten sogar offline auslösen, ohne dass eine Verbindung zu Braze besteht (z. B. im Flugzeugmodus).

{% alert important %}
Sobald eine In-App-Nachricht gestoppt wurde, kann es sein, dass einige Nutzer:innen die Nachricht weiterhin sehen, wenn sie eine Sitzung begonnen haben, bevor die Nachricht gestoppt wurde und anschließend das Trigger-Ereignis ausführen. Diese Nutzer:innen werden auch nach Beendigung der Kampagne als eindeutige Impressionen gezählt.
{% endalert %}

#### Wählen Sie eine Priorität

Wenn Sie die Aktion ausgewählt haben, die die In-App-Nachricht auslöst, sollten Sie ihre Priorität festlegen. Wenn zwei Nachrichten durch dieselbe Aktion ausgelöst werden, werden die Nachrichten mit hoher Priorität vor den Nachrichten mit niedrigerer Priorität auf den Geräten der Benutzer angezeigt. 

Sie können zwischen den folgenden Nachrichtenprioritäten wählen:

- Niedrige Priorität (wird nach anderen Nachrichten angezeigt)
- Mittlere Priorität
- Hohe Priorität (wird vor anderen Nachrichten angezeigt)

Die hohe, mittlere und niedrige Nachrichtenpriorität sind als Buckets zu verstehen, sodass mehrere Nachrichten dieselbe Priorität haben können. Um die Prioritäten innerhalb dieser Bereiche festzulegen, klicken Sie auf **Genaue Priorität festlegen** und Sie können die Kampagnen per Drag & Drop nach der richtigen Priorität ordnen.

![Ein Beispiel für die Prioritätensetzung bei einer In-App-Nachricht-Kampagne und Canvas.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### Zielgruppe auswählen

Als Nächstes müssen Sie mithilfe von Segmenten oder Filtern eine [Zielgruppe erstellen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/). Sie erhalten automatisch einen Überblick über die ungefähre Zusammensetzung dieses Segments. Denken Sie daran, dass die genaue Segmentzugehörigkeit immer erst kurz vor dem Versand der Nachricht berechnet wird.

{% alert note %}
Wenn es bei der In-App-Nachricht zu einer Verzögerung kommt, wird die Segmentierung erst danach ermittelt. Wenn der Nutzer:innen berechtigt ist, wird die In-App-Nachricht bei der nächsten verfügbaren Sitzung synchronisiert.
{% endalert %}

##### Kampagneneignung und Liquid evaluieren

In einigen Szenarien möchten Sie vielleicht die Berechtigung eines Nutzers neu bewerten, wenn er eine In-App-Nachricht triggert, die angezeigt werden soll. Beispiele hierfür sind Kampagnen, die auf ein benutzerdefiniertes Attribut abzielen, das sich häufig ändert, oder Nachrichten, die kurzfristige Profiländerungen widerspiegeln sollen.

![Kontrollkästchen für "Eignung der Kampagne vor der Anzeige neu bewerten" ausgewählt.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

Wenn Sie die Option **Kampagnenberechtigung vor der Anzeige neu bewerten** auswählen, wird eine zusätzliche Anfrage an Braze gestellt, um zu bestätigen, dass der Benutzer vor dem Versand noch für diese Nachricht berechtigt ist. Außerdem werden alle [Liquid-Variablen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) oder [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) in diesem Moment vor der Anzeige der Nachricht als Vorlage verwendet.

Dadurch wird verhindert, dass In-App-Nachrichten an Benutzer innerhalb abgelaufener oder archivierter Kampagnen gesendet werden. Wenn Sie die Berechtigung eines Benutzers nicht neu bewerten, erhält der Benutzer die In-App-Nachricht auch dann noch, wenn die Kampagne bereits abgelaufen ist oder archiviert wurde, weil die Nachricht in Ihrem SDK liegt und darauf wartet, dass Benutzer sie auslösen.

{% alert note %}
Die Aktivierung dieser Option führt zu einer leichten Verzögerung (< 100ms) zwischen dem Zeitpunkt, an dem ein Nutzer:in eine In-App-Nachricht triggert und dem Zeitpunkt, an dem die Nachricht angezeigt wird, aufgrund der zusätzlichen Anfrage für die Berechtigung und das Template.
<br><br>
Verwenden Sie diese Option nicht für Nachrichten, die ausgelöst werden können, während ein Nutzer:innen offline ist, oder wenn die Berechtigung und die Liquid-Neubewertung nicht erforderlich sind.
{% endalert %}

#### Wählen Sie Konversionsereignisse aus

Mit Braze können Sie nachverfolgen, wie oft Benutzer nach Erhalt einer Kampagne bestimmte Aktionen, d.h. [Conversion Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), durchführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen zuzulassen, in dem eine Konversion gezählt wird, wenn der Nutzer:innen die angegebene Aktion durchführt.

{% endtab %}
{% tab Canvas %}

Falls noch nicht geschehen, füllen Sie die restlichen Abschnitte der Canvas-Komponente aus. Weitere Einzelheiten zum Aufbau des restlichen Canvas, zur Implementierung von multivariaten Tests und intelligenter Auswahl und mehr finden Sie im Schritt [Aufbau Ihres Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) in unserer Canvas-Dokumentation.

Informationen zu den Canvas-spezifischen In-App-Nachrichtenoptionen finden Sie unter [In-App-Nachrichten in Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Schritt 8: Überprüfen und einsetzen

Nachdem Sie den letzten Teil Ihrer Kampagne oder Ihres Canvas erstellt haben, überprüfen Sie die Details, [testen Sie sie]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) und senden Sie sie ab!

Sehen Sie sich als nächstes die [In-App-Nachrichtenberichte]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) an, um zu erfahren, wie Sie auf die Ergebnisse Ihrer Nachrichtenkampagnen zugreifen können.

## Was Sie wissen sollten

### Limits für aktive In-App-Nachricht-Kampagnen

Braze legt Wert auf Zuverlässigkeit und Geschwindigkeit. Deshalb empfehlen wir, immer nur die Daten an Braze zu senden, die Sie tatsächlich benötigen. Und genauso sollten Sie auch Kampagnen deaktivieren, die Ihnen keinen Mehrwert mehr bieten.

Die Verarbeitung aktionsbasierter In-App-Nachrichtenkampagnen, die noch aktiv sind, aber keine Nachrichten mehr senden oder nicht mehr benötigt werden, verlangsamt die Gesamtleistung der Braze-Dienste für Sie und andere Kunden. Diese zusätzliche Zeit, die für die Verarbeitung dieser großen Anzahl von inaktiven Kampagnen benötigt wird, bedeutet, dass In-App-Nachrichten länger brauchen, um auf den Geräten der Endbenutzer zu erscheinen, was sich auf das Erlebnis der Endbenutzer auswirkt.

{% alert important %}
Bis zu 200 aktive aktionsbasierte In-App-Kampagnen pro Workspace sind möglich, um das Zustellungstempo zu optimieren und Zeitüberschreitungen zu vermeiden. Dies gilt nicht für Leinwände.
{% endalert %}

Die Zahl 200 bezieht sich auf laufende In-App-Nachrichtenkampagnen, die noch nicht abgeschlossen sind oder kein Abschlussdatum enthalten. Laufende In-App-Nachrichtenkampagnen, deren Abschlussdatum bereits verstrichen ist, werden nicht gezählt. Der durchschnittliche Braze-Kunde hat insgesamt 26 Kampagnen gleichzeitig aktiv - es ist also unwahrscheinlich, dass sich diese Einschränkung auf Sie auswirken wird.


