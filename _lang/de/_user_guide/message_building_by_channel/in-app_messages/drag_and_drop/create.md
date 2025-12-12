---
nav_title: In-App-Nachrichten erstellen
article_title: "Erstellen einer In-App-Nachricht mit Drag-and-Drop"
description: "Dieser Artikel erläutert die Erstellung von In-App-Nachrichten per Drag-and-Drop-Editor sowie Voraussetzungen, kreative Details und mehr."
alias: "/create_dnd_iam/"
page_order: 1
local_redirect: #set-message-level-styles, #add-a-custom-font, #drag-and-drop-in-app-message-components, #creative-details
  set-message-level-styles: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-level-styles'
  add-a-custom-font: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#custom-fonts'
  drag-and-drop-in-app-message-components: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components'
  creative-details: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#creative-details'
---

# Erstellen einer In-App-Nachricht per Drag-and-Drop

> Mit dem Drag-and-Drop-Editor können Sie vollständig angepasste und personalisierte In-App-Nachrichten in Kampagnen und Canvasen erstellen.


{% multi_lang_include video.html id="j94omgo73o" align="right" source="wistia" %}

Wenn Sie Ihre vorhandenen benutzerdefinierten HTML-Vorlagen oder von Dritten erstellte Vorlagen verwenden möchten, müssen diese im Drag-and-Drop-Editor neu erstellt werden.

Sie sind sich nicht sicher, ob Ihre In-App-Nachricht über eine Kampagne oder ein [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) gesendet werden soll? Kampagnen eignen sich eher für einzelne einfache Messaging-Kampagnen, während Canvases besser für mehrstufige User Journeys geeignet sind. Nachdem Sie den Ort ausgewählt haben, an dem Sie Ihre Nachricht erstellen möchten, lassen Sie uns nun die einzelnen Schritte zur Erstellung einer In-App-Nachricht per Drag-and-Drop erläutern.

## Voraussetzungen

### SDK-Anforderungen

| Minimale SDK-Version                                                          | Empfohlene SDK-Version                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% details More information on minimum SDKs %}

Nachrichten, die mit dem Drag-and-Drop-Editor erstellt wurden, können nur an Nutzer:innen mit den Mindestversionen des SDK (siehe Tabelle oben) versendet werden. Wenn ein Nutzer:innen seine App nicht aktualisiert hat (d.h. mit einer älteren SDK-Version arbeitet), wird er die In-App-Nachricht nicht erhalten.

Um alle Features des Drag-and-Drop-Editors nutzen zu können, aktualisieren Sie Ihre SDKs auf die empfohlenen SDK-Versionen. Dadurch können Sie die folgenden zusätzlichen Funktionen nutzen:

- Textlinks, die die Nachricht nicht ausblenden
- Button-Aktion zur Anfrage von Push Primer

Hier die jeweiligen SDK-Mindestanforderungen für diese Features:

| Textlinks*                                                         | Anfrage Push Primer                                                           |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions web:4.8.1 swift:6.5.0 android:26.0.0 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\*Wenn Sie in Ihrer In-App-Nachricht einen Link einfügen, der zu einer URL weiterleitet, und der Endbenutzer nicht über die angegebene SDK-Mindestversion verfügt, wird die Nachricht durch Auswahl des Links geschlossen und der Benutzer kann nicht zur Nachricht zurückkehren, um das Formular abzuschicken.

{% enddetails %}

### Zusätzliche Voraussetzungen

- Im Web-SDK muss die Initialisierungsoption [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) auf `true` gesetzt werden. Die Option `enableHtmlInAppMessages` ermöglicht ebenfalls die Funktion dieser Nachrichten, ist aber veraltet und sollte auf `allowUserSuppliedJavascript` aktualisiert werden.
- Wenn Sie den Google Tag Manager verwenden, müssen Sie in der GTM-Konfiguration "In-App-Nachrichten in HTML zulassen" aktivieren.

## Schritt 1: In-App-Nachricht erstellen

Erstellen Sie eine neue In-App-Nachricht oder einen Canvas-Schritt und wählen Sie dann den **Drag-and-Drop-Editor** als Bearbeitungsmethode.

## Schritt 2: Wählen Sie Ihre Vorlage

Wenn Sie den Drag-and-Drop-Editor als Bearbeitungsmethode ausgewählt haben, haben Sie die Wahl:

- Beginnen Sie mit einer leeren modalen Vorlage
- Verwenden Sie eine Braze Drag-and-Drop-Vorlage für In-App-Nachrichten
- Wählen Sie eine gespeicherte Drag-and-Drop-Vorlage für In-App-Nachrichten aus.

Wählen Sie **Nachricht erstellen**, um mit dem Entwurf Ihrer In-App-Nachricht im Drag-and-Drop-Editor zu beginnen.

![Der Bereich Braze Templates, in dem Sie ein einfaches Template, ein Hintergrundbild, eine Telefonnummer oder ein leeres Template auswählen können.]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

Sie können auf alle Vorlagen auch über den Bereich **Vorlagen** im Dashboard zugreifen.

## Schritt 3: Zusätzliche Seiten hinzufügen (optional) {#multi-page}

Durch das Hinzufügen von Seiten zu Ihrer In-App-Nachricht können Sie Nutzer:innen durch einen sequentiellen Ablauf leiten, z.B. ein Onboarding oder eine Willkommensreise. Sie können Seiten im Bereich **Seiten** der Registerkarte **Erstellen** verwalten.

![Eine In-App-Nachricht für ein Unternehmen aus dem Gesundheitswesen, die aus drei Seiten besteht.]({% image_buster /assets/img_archive/dnd_iam_mockup.png %})

{% tabs %}
{% tab Adding pages %}

In-App-Nachrichten beginnen standardmäßig mit einer Seite. Um eine neue Seite hinzuzufügen:

1. Wählen Sie **\+ Seite hinzufügen**.
2. Wählen Sie aus der Liste der benutzerdefinierten oder von Braze zur Verfügung gestellten Vorlagen.
3. Geben Sie der Seite einen aussagekräftigen Namen. Das hilft Ihnen, wenn Sie Seiten miteinander verbinden.

{% alert tip %}
Sie können bis zu 10 Seiten pro In-App-Nachricht hinzufügen.
{% endalert %}

So duplizieren Sie eine vorhandene Seite:

1. Bewegen Sie den Mauszeiger über die Seite in der Liste und wählen Sie <i class="fas fa-ellipsis-vertical"></i>, um weitere Optionen zu öffnen.
2. Wählen Sie **Duplizieren**.
3. Geben Sie der Seite einen aussagekräftigen Namen. Das hilft Ihnen, wenn Sie Seiten miteinander verbinden.

{% endtab %}
{% tab Deleting or renaming pages %}

So löschen oder benennen Sie eine Seite um:

1. Bewegen Sie den Mauszeiger über die Seite in der Liste und wählen Sie <i class="fas fa-ellipsis-vertical"></i>, um weitere Optionen zu öffnen.
2. Wählen Sie **Umbenennen** oder **Löschen**.

{% endtab %}
{% endtabs %}

### Schritt 3a: Seiten miteinander verbinden

Mehrseitige In-App-Nachrichten sind sequentiell, können also durch Anklicken oder Antippen durchlaufen werden.

Um Seiten miteinander zu verbinden:

1. Wählen Sie Ihre Startseite.
2. Wählen Sie eine Schaltfläche oder ein Bildelement im Canvas aus.
3. Legen Sie das **Verhalten bei Klick** auf **Gehe zu Seite** fest.
4. Wählen Sie die Seite, auf die Sie verlinken möchten, von der Startseite aus.
5. Fahren Sie fort, bis alle Seiten verlinkt sind.

![Ein Nutzer:innen bearbeitet den primären Aktions-Button, um zu Seite 2 der In-App-Nachricht zu gelangen.]({% image_buster/assets/img_archive/dnd_iam_multipage.gif %})

Wenn eine Seite mit keiner anderen Seite verknüpft ist, kann die Nachricht nicht gestartet werden.

{% alert note %}
Mit dem Button X kann die Nachricht jederzeit geschlossen werden. Diese Schaltfläche kann nicht entfernt werden.
{% endalert %}

## Schritt 4: In-App-Nachricht erstellen und gestalten

Hier kann Ihre Botschaft über den Laufsteg stolzieren, gekleidet in den typischen Stil Ihrer Marke. Mit einer Kombination aus Editorblöcken und Stileinstellungen können Sie Ihre In-App-Nachricht anpassen und gestalten.

- Eine Liste der verfügbaren Editorblöcke und ihrer Eigenschaften finden Sie unter [Editorblöcke]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).
- Hilfe bei der Anpassung des Aussehens Ihrer Nachricht finden Sie unter [Stil-Einstellungen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/).
- Bewährte Verfahren zur Erstellung von Nachrichten von rechts nach links finden Sie unter [Erstellen von Nachrichten von rechts nach links]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Schritt 5: Testen Sie Ihre In-App-Nachricht

Im Bereich **Vorschau & Test** können Sie eine Vorschau Ihrer In-App-Nachrichten auf verschiedenen Geräten anzeigen und eine Testnachricht an Ihr Gerät senden. Hier können Sie sicherstellen, dass die Details Ihrer Drag-and-Drop-Kampagne für In-App-Nachrichten auf all Ihren Plattformen aufeinander abgestimmt sind. 

Es ist wichtig, dass Sie Ihre In-App-Nachrichten immer testen, bevor Sie Ihre Kampagnen versenden, damit Sie sich ein Bild davon machen können, wie Ihre endgültige Nachricht aus Sicht des Nutzers aussehen wird.

### Nachrichtenvorschau aus Nutzerperspektive

{% alert warning %}
Um einen Test entweder an Inhaltstestgruppen oder einzelne Nutzer:innen zu senden, muss Push auf Ihren Testgeräten vor dem Senden aktiviert werden.
{% endalert %}

Auf dem Tab **Vorschau & Test** können Sie eine Vorschau der Nachrichten anzeigen, so als wären Sie ein Nutzer:innen. Sie können einen bestimmten, einen zufälligen oder einen angepassten Nutzer auswählen bzw. erstellen:

- **Zufälliger Benutzer:** Braze wählt nach dem Zufallsprinzip einen Benutzer aus der Datenbank aus und zeigt eine Vorschau der In-App-Nachricht auf der Grundlage seiner Attribute oder Ereignisinformationen an.
- **Nutzerauswahl:** Sie können einen bestimmten Benutzer anhand seiner E-Mail-Adresse oder `external_id` auswählen. Die Vorschau auf die In-App-Nachricht basiert auf den nutzerspezifischen Attributen und Ereignisinformationen.
- **Angepasste Nutzer:innen:** Sie können einen Benutzer individuell anpassen. Braze wird Eingaben für alle verfügbaren Attribute und Ereignisse anbieten. Geben Sie alle Informationen ein, die Sie in der Vorschau-E-Mail sehen möchten.

### Test-Checkliste

Beachten Sie folgende Erwägungen, wenn Sie Ihre In-App-Nachricht testen:

- Haben Sie die Nachricht auf verschiedenen Geräten getestet?
- Werden die Bilder und Medien angezeigt und verhalten sie sich wie erwartet?
- Funktioniert das Liquid wie erwartet? Haben Sie einen Standard-Attributwert für den Fall vorgesehen, dass das Liquid keine Informationen liefert?
- Ist Ihr Text klar, prägnant und korrekt?
- Zeigen Ihre Schaltflächen dem Benutzer, wohin er gehen soll?

## Häufig gestellte Fragen

#### Warum werden Klicks auf den Haupttext nicht unter Analytics angezeigt?

Für In-App-Nachrichten, die mit dem Drag-and-Drop-Editor erstellt wurden, werden Klicks auf den Textkörper nicht automatisch erfasst. Weitere Details finden Sie in den SDK Changelogs für [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) und [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

#### Kann ich auf der Grundlage von Schaltflächenklicks segmentieren?

Ja, die Segmentierung auf Grundlage von Button-Klicks ist für bis zu zwei Buttons in Ihrer Nachricht möglich. Setzen Sie dazu den **Berichtsbezeichner** Ihrer Buttons auf "0" und "1", was den Segmentierungsfiltern "Auf In-App-Nachricht-Button 1 geklickt" bzw. "Auf In-App-Nachricht-Button 2 geklickt" entspricht.

![Das Feld "Bezeichner für die Berichterstattung" mit einem Wert von "0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

#### Kann ich meine In-App-Nachrichten mit benutzerdefiniertem HTML oder JavaScript anpassen oder bestehende HTML-Nachrichten in den Editor übertragen?

Sie können vorhandene HTML-Nachrichten nicht direkt in den Editor übertragen, aber rohes HTML, CSS und JavaScript in einen angepassten Code-Block einfügen. Sie können angepasste Code-Blöcke verwenden, um Videos von Drittanbietern und erweitertes Liquid wie Connected-Content oder bedingte Anweisungen einzubetten.

#### Wie kann ich eine In-App-Nachricht mit einem Slideup erstellen?

Derzeit ist der Editor nur auf modale und bildschirmfüllende Nachrichten beschränkt. Sie können im Abschnitt **Nachrichtencontainer** des Bedienfelds **Nachrichtenstile** zwischen den Anzeigearten wechseln.

#### Kann ich meine In-App-Nachricht als Vorlage speichern, nachdem ich sie in meiner Kampagne oder im Canvas erstellt habe?

Ja Jede In-App-Nachricht, die Sie in einer zukünftigen Kampagne oder einem Canvas-Schritt wiederverwenden möchten, können Sie über die Schaltfläche **Als Vorlage speichern**, die nach dem Verlassen des Editors verfügbar ist, als eigene Vorlage speichern. Bevor Sie sie als Vorlage speichern können, müssen Sie die Kampagne zunächst starten ODER als Entwurf speichern.

![Eine Vorschau auf eine In-App-Nachricht für eine Produkt-Tour.]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

Sie können auch In-App-Nachrichtenvorlagen erstellen und speichern, indem Sie zu **Vorlagen** > **In-App-Nachrichtenvorlagen** navigieren.
