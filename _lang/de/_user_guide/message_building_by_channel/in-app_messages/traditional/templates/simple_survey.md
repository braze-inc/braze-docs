---
nav_title: "Einfache Umfrage"
article_title: Einfache Umfrage In-App-Nachricht
page_order: 1.5
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie mit Hilfe der Umfragen für In-App-Nachrichten Benutzerattribute, Erkenntnisse und Vorlieben sammeln, um Ihre Kampagnenstrategie zu unterstützen."
channel:
  - in-app messages
tool:
  - Templates
---

# Einfache Umfrage

> Verwenden Sie die In-App-Nachrichtenvorlage **Simple Survey**, um Benutzerattribute, Erkenntnisse und Vorlieben zu sammeln, die Ihre Kampagnenstrategie unterstützen. 

Fragen Sie die Nutzer zum Beispiel, wie sie Ihre App verwenden möchten, erfahren Sie mehr über ihre persönlichen Vorlieben oder fragen Sie sie nach ihrer Zufriedenheit mit einer bestimmten Funktion.

![Drei einfache Nachrichten für Umfragen: Benachrichtigungspräferenzen, Ernährungspräferenzen und eine Umfrage zur Kundenzufriedenheit. Die ausgewählten Optionen in den Umfragen entsprechen den angepassten Attributen, die für diese Nutzer:innen protokolliert werden.]({% image_buster /assets/img/iam/iam-survey.png %})

## SDK-Anforderungen {#supported-sdk-versions}

Diese In-App-Nachricht wird nur an Geräte ausgeliefert, die [Flex CSS](https://caniuse.com/flexbox) unterstützen und mindestens die folgenden [SDK-Versionen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) haben müssen. 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Um In-App-Nachrichten im HTML-Format über das Internet SDK zu aktivieren, müssen Sie Braze die Initialisierungsoption `allowUserSuppliedJavascript` zur Verfügung stellen.
{% endalert %}

## Eine Umfrage erstellen {#create}

Wenn Sie eine [In-App-Nachricht]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) erstellen, wählen Sie **Einfache Umfrage** als **Nachrichtentyp**.

Diese Umfragevorlage wird sowohl für mobile Apps als auch für Webbrowser unterstützt. Vergewissern Sie sich, dass Ihre SDKs über die für dieses Feature erforderlichen [Mindestversionen](#supported-sdk-versions) verfügen.

### Schritt 1: Ihre Umfragefrage hinzufügen

Um mit der Erstellung Ihrer Umfrage zu beginnen, fügen Sie Ihre Frage in das Feld **Überschrift der** Umfrage ein. Falls gewünscht, können Sie eine optionale **Nachricht** hinzufügen, die unter der Frage Ihrer Umfrage erscheint.

![Tab des einfachen Umfrage-Editors mit Feldern für eine Überschrift, einen optionalen Textkörper und einen optionalen Hilfstext.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:90%"}

{% alert tip %}
Diese Felder können sowohl Liquid als auch Emojis enthalten, also lassen Sie sich etwas einfallen!
{% endalert %}

### Schritt 2: Auswahlen konfigurieren {#single-multiple-choice}

Sie können bis zu 12 Auswahlmöglichkeiten in einer Umfrage hinzufügen.

Wählen Sie entweder **Single-Choice-Auswahl** oder **Multiple-Choice-Auswahl**. Der **Hilfetext** wird automatisch aktualisiert, wenn Sie zwischen den beiden Optionen wechseln, damit die Nutzer:innen wissen, wie viele Möglichkeiten sie auswählen können. 

Legen Sie dann fest, ob Sie [angepasste Attribute](#custom-attributes) oder [nur Protokollantworten](#no-attributes) sammeln wollen.

![Wählen Sie aus dem Dropdown-Menü die Option "Attribute bei Übermittlung protokollieren" aus.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### Angepasste Attribute sammeln {#custom-attributes}

Wählen Sie **Attribute bei der Einreichung protokollieren** auswählen, um Attribute basierend auf der Übermittlung der Nutzerin oder des Nutzers zu sammeln. Mit dieser Option können Sie neue Segmente und Retargeting Kampagnen erstellen. Bei einer [Umfrage zur Zufriedenheit](#user-satisfaction) könnten Sie beispielsweise eine E-Mail an alle Nutzer:innen senden, die nicht zufrieden waren.

Um jeder Auswahl ein benutzerdefiniertes Attribut hinzuzufügen, wählen Sie den Namen eines benutzerdefinierten Attributs aus dem Dropdown-Menü (oder erstellen Sie ein neues) und geben Sie dann den Wert ein, der bei der Übermittlung dieser Auswahl gesetzt werden soll. Sie können auch ein neues angepasstes Attribut auf Ihrer [Einstellungsseite]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) erstellen.

Der Datentyp Ihrer benutzerdefinierten Attribute hängt davon ab, wie Sie Ihre Umfrage eingerichtet haben.

- **Auswahl im Multiple-Choice-Verfahren:** Der Datentyp des benutzerdefinierten Attributs muss ein Array sein. Wenn das angepasste Attribut auf einen anderen Datentyp eingestellt ist, werden die Antworten nicht protokolliert.
- **Einzelne Auswahlmöglichkeiten:** Der Datentyp des angepassten Attributs _darf kein_ Array sein. Die Antworten werden nicht protokolliert, wenn das Attribut ein Array ist.

{% alert important %}
Wenn die Sammlung von benutzerdefinierten Attributen aktiviert ist, werden Auswahlmöglichkeiten, die denselben benutzerdefinierten Attributnamen haben, in einem Array zusammengefasst.
{% endalert %}

##### Beispiel 

In einer [Umfrage zu den Benachrichtigungspräferenzen](#notification-preferences) könnten Sie beispielsweise jeder Auswahl ein boolesches (wahr/falsch) Attribut zuweisen, damit die Nutzer:in auswählen können, welche Themen sie interessieren. Wenn ein Benutzer die Option "Sonderangebote" ankreuzt, wird sein [Benutzerprofil]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) aktualisiert und das benutzerdefinierte Attribut `Promotions Topic` auf `true` gesetzt. Wenn Sie die Option nicht markieren, bleibt dasselbe Attribut unverändert.

Sie können dann den Filter `Custom Attribute` verwenden, um ein Segment für Nutzer:innen mit dem angepassten Attribut `Promotions Topic` `is` `true` zu erstellen, um sicherzustellen, dass nur Nutzer:innen, die an Ihren Aktionen interessiert sind, die entsprechenden Kampagnen erhalten.

#### Nur Antworten protokollieren {#no-attributes}

Alternativ können Sie auch **nur die Antworten protokollieren (ohne Attribute)**. Wenn diese Option ausgewählt ist, werden Umfragebeantwortungen als Schaltflächenklicks protokolliert, aber benutzerdefinierte Attribute werden nicht im Profil eines Benutzers gespeichert. Das bedeutet, dass Sie weiterhin die Klick-Metriken für jede Umfrageoption sehen können (siehe [Analytics](#analytics)), aber diese Auswahl wird nicht in ihrem Benutzerprofil angezeigt.

Diese Klick-Metriken sind für Retargeting nicht verfügbar.

### Schritt 4: Einreichungsverhalten wählen

Sobald ein Benutzer seine Antwort abgeschickt hat, können Sie optional eine Bestätigungsseite anzeigen oder die Nachricht einfach schließen.

Eine Bestätigungsseite ist ein guter Ort, um sich bei den Nutzern für ihre Zeit zu bedanken oder zusätzliche Informationen bereitzustellen. Sie können den Call-to-Action auf dieser Seite anpassen, um Nutzer:innen auf eine andere Seite Ihrer App oder Website zu leiten.

Bearbeiten Sie den Text der Schaltfläche und das On-Click-Verhalten im Abschnitt **Schaltfläche einreichen** unten auf der Registerkarte **Umfrage**:

![Verhalten bei Klick auf "Antworten abschicken und Bestätigungsseite anzeigen" eingestellt.]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Wenn Sie eine Bestätigungsseite hinzufügen möchten, wechseln Sie zur Registerkarte **Bestätigungsseite**, um Ihre Nachricht anzupassen:

![Registerkarte Bestätigungsseite des einfachen Umfrage-Editors. Die verfügbaren Felder sind Überschrift, optionaler Textkörper, Button-Text und das Verhalten des Buttons beim Klick.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:90%"}

Wenn Sie Benutzer auf eine andere Seite Ihrer App oder Website leiten möchten, ändern Sie das **On-Click-Verhalten** des Buttons.

### Schritt 5: Gestalten Sie Ihre Nachricht (optional) {#styling}

Sie können die Schriftfarbe und die Akzentfarbe der Nachricht mit dem **Farbthema-Picker** anpassen.

![Tab "Verfassen" des einfachen Editors für Umfragen mit ausgeklappter Farbauswahl, nachdem ein Nutzer:innen auf die Farbpalette geklickt hat.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analysieren Sie die Ergebnisse {#analytics}

Sobald Ihre Kampagne gestartet ist, können Sie die Ergebnisse in Echtzeit analysieren, um die Aufschlüsselung jeder ausgewählten Wahl zu sehen. Wenn Sie die [Erfassung von benutzerdefinierten Attributen](#custom-attributes) aktiviert haben, können Sie auch neue Segmente oder Folgekampagnen für Benutzer erstellen, die die Umfrage eingereicht haben.

{% alert note %}
Gelöschte Umfrageoptionen erscheinen weiterhin in der Analyse, werden aber neuen Benutzern nicht mehr als Auswahlmöglichkeit angezeigt.
{% endalert %}

Sie finden Ihre Metriken zur Umfrage Performance, indem Sie das Dropdown-Menü **Ergebnisse** für eine bestimmte Variante im Abschnitt **In-App-Nachricht Performance** der Analytics erweitern. Hier ist eine Aufschlüsselung dessen, was Sie sehen werden:

- **Das Engagement bei Umfragen** zeigt, wie Nutzer:innen mit der Umfrage insgesamt interagiert haben, einschließlich der Gesamtzahl der Einsendungen, Ablehnungen und Klicks innerhalb des Nachrichtentextes.
- **Die Ergebnisse der Umfrage** zeigen eine Aufschlüsselung der Anzahl der Nutzer:innen, die die einzelnen Antwortoptionen ausgewählt haben, sowie den prozentualen Anteil an der Gesamtzahl der Einsendungen für jede Option.
- **Die Metriken für die Bestätigungsseite** (falls aktiviert) geben an, wie viele Nutzer:innen den Bestätigungsbildschirm angesehen, auf den Button geklickt oder ihn ohne Interaktion verlassen haben.

Definitionen der Umfragemetriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/) und filtern Sie nach "In-App-Nachricht".

Sehen Sie sich die [In-App-Nachrichtenberichte]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) an, um eine Aufschlüsselung Ihrer Kampagnenmetriken zu erhalten.

### Currents {#currents}

Die ausgewählten Optionen fließen automatisch in Currents ein, und zwar unter dem Menüpunkt [**In-App-Nachricht Klick-Events**]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe) `button_id` Feld. Jede Auswahl wird mit ihrem universell eindeutigen Identifikator (UUID) gesendet.

## Anwendungsfälle

{% tabs %}
{% tab User satisfaction %}

### Zufriedenheit der Nutzer:innen

**Das Ziel:** Messen Sie die Kundenzufriedenheit und senden Sie Win-Back-Kampagnen an Nutzer, die schlechte Bewertungen hinterlassen haben.

Verwenden Sie dazu eine Umfrage mit einer Auswahl von fünf Optionen, die von "😡 Sehr unzufrieden" bis "😍 Sehr zufrieden" reichen. Jede Auswahl wird dem angepassten Attribut `customer_satisfaction` mit einem numerischen Wert von 1 bis 5 zugeordnet, wobei 1 für die geringste Zufriedenheit und 5 für die höchste Zufriedenheit steht.

| Auswahl                                | Attribute              | Wert |
|---------------------------------------|------------------------|-------|
| 😡 Sehr unzufrieden                  | `customer_satisfaction` | (1 %)     |
| 😟 Unzufrieden                       | `customer_satisfaction` | (2 %)     |
| 🙂 Weder zufrieden noch unzufrieden | `customer_satisfaction` | 3     |
| 😊 Zufrieden                          | `customer_satisfaction` | (4 %)     |
| 😍 Sehr zufrieden                     | `customer_satisfaction` | (5 %)     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Wenn ein Nutzer:innen die Umfrage abschickt, wird sein ausgewählter Wert als angepasstes Attribut protokolliert. Anschließend können Sie mithilfe von Zielgruppen-Filtern Folgekampagnen erstellen. Richten Sie beispielsweise Nachrichten zur Rückgewinnung an Nutzer:innen, deren Attribut `customer_satisfaction` auf 1 oder 2 steht.

{% endtab %}
{% tab Notification preferences %}

### Präferenzen für Benachrichtigungen

**Das Ziel:** Lassen Sie Nutzer:innen sich für bestimmte Arten von Benachrichtigungen entscheiden.

Verwenden Sie dazu eine Umfrage mit Multiple-Choice-Auswahl, bei der jede Auswahl ein Benachrichtigungsthema darstellt. Anstatt dasselbe Attribut mit unterschiedlichen Werten zu belegen, wird jede Auswahl einem bestimmten booleschen Attribut abgebildet, das das Interesse des Nutzers:in an diesem Thema widerspiegelt. Wenn ein Nutzer:innen eine Auswahl trifft, wird das entsprechende Attribut auf `true` gesetzt. Wenn Sie diese Option nicht wählen, bleibt das Attribut unverändert.

| Auswahl             | Attribute              | Wert  |
|--------------------|------------------------|--------|
| Produkt Updates    | `wants_product_updates`| `true` |
| Aktionen         | `wants_promotions`     | `true` |
| Event-Einladungen      | `wants_event_invites`  | `true` |
| Umfragen & Feedback | `wants_surveys`        | `true` |
| Tipps & Tutorials   | `wants_tips`           | `true` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Identify customer goals %}

### Ziele der Kund:in identifizieren

**Das Ziel:** Ermitteln Sie die Hauptgründe, warum Benutzer Ihre App besuchen.

Verwenden Sie dazu eine Umfrage mit nur einer Auswahlmöglichkeit, wobei jede Option ein gemeinsames Ziel oder eine Absicht darstellt. Jede Auswahl wird dem angepassten Attribut `product_goal` mit einem Wert zugeordnet, der der ausgewählten Absicht des Nutzers:in entspricht.

| Auswahl                     | Attribute       | Wert     |
|----------------------------|------------------|-----------|
| Status abfragen            | `product_goal`   | `status`  |
| Mein Konto upgraden       | `product_goal`   | `upgrade` |
| Zeitplan für einen Termin  | `product_goal`   | `schedule`|
| Kund:in Unterstützung           | `product_goal`   | `support` |
| Nur stöbern              | `product_goal`   | `browse`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Wenn ein Nutzer die Umfrage abschickt, wird der ausgewählte Wert als angepasstes Attribut in seinem Profil protokolliert. Sie können diese Daten dann verwenden, um zukünftige Erlebnisse zu personalisieren oder Nutzer:innen auf der Grundlage ihres Hauptziels zu segmentieren.

{% endtab %}
{% tab Improve conversion rates %}

### Verbessern Sie die Konversionsraten

**Das Ziel:** Verstehen Sie, warum Kunden nicht upgraden oder kaufen.

Verwenden Sie dazu eine Umfrage mit nur einer Auswahlmöglichkeit, wobei jede Option ein gängiges Hindernis für ein Upgrade darstellt. Jede Auswahl wird dem angepassten Attribut `upgrade_reason` mit einem entsprechenden Wert zugeordnet, der die Auswahl des Nutzers:innen widerspiegelt.

| Choice              | Attribute        | Value       |
|---------------------|------------------|-------------|
| Too Expensive       | `upgrade_reason` | `expensive` |
| Not Valuable        | `upgrade_reason` | `value`     |
| Difficult To Use    | `upgrade_reason` | `difficult` |
| Using a Competitor  | `upgrade_reason` | `competitor`|
| Other Reason        | `upgrade_reason` | `other`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

When a user submits the survey, the selected value is saved to their profile. You can then target these users with campaigns tailored to their specific objection, like discount offers or usability improvements.

{% endtab %}
{% tab Favorite features %}

### Bevorzugte Features

**Das Ziel:** Verstehen Sie, welche Funktionen Kunden gerne nutzen.

To set this up, use a multiple-choice selection survey where each option represents a feature of your app. Each choice is mapped to the custom attribute `favorite_features`, and when the user submits the survey, the attribute is set to an array of the selected values.

| Choice            | Attribute          | Value        |
|-------------------|--------------------|--------------|
| Bookmarks         | `favorite_features`| `bookmarks`  |
| Mobile App        | `favorite_features`| `mobile`     |
| Sharing Posts     | `favorite_features`| `sharing`    |
| Customer Support  | `favorite_features`| `support`    |
| Customization     | `favorite_features`| `custom`     |
| Price / Value     | `favorite_features`| `value`      |
| Community         | `favorite_features`| `community`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Because this survey uses multiple-choice selection, the user's profile will be updated with a list of all selected feature values.

{% endtab %}
{% endtabs %}
