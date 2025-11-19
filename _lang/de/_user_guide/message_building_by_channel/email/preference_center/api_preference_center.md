---
nav_title: API-E-Mail-Einstellungszentrum
article_title: API-E-Mail-Einstellungszentrum
page_order: 1
description: "Dieser Artikel beschreibt das API-E-Mail-Einstellungszentrum und wie Sie es anpassen können."
channel:
  - email
---

# API-E-Mail-Einstellungszentrum

> Die Einrichtung eines Präferenzzentrums bietet Ihren Benutzern eine zentrale Anlaufstelle zur Bearbeitung und Verwaltung ihrer Benachrichtigungspräferenzen für Ihre [E-Mail-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/email/). Dieser Artikel enthält Schritte zur Erstellung eines API-generierten Präferenzzentrums. Allerdings können Sie ein Präferenzzentrum auch mit dem [Drag-and-Drop-Editor]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/) erstellen.

Gehen Sie im Braze-Dashboard zu **Zielgruppe** > **E-Mail-Präferenzzentren**.

Hier können Sie jede Abonnementgruppe verwalten und einsehen. Jede Abo-Gruppe, die Sie erstellen, wird zu dieser Liste der Präferenzzentren hinzugefügt. Sie können mehrere Präferenzzentren erstellen.

{% alert important %}
Das Präferenzzentrum ist für die Verwendung innerhalb des E-Mail-Kanals von Braze vorgesehen. Die Links zum Einstellungscenter sind für jeden Benutzer dynamisch und können nicht extern gehostet werden.
{% endalert %}

## Erstellen eines Präferenzzentrums mit API

Mit den [Braze-Endpunkten für das Preference Center]({{site.baseurl}}/api/endpoints/preference_center) können Sie ein Preference Center erstellen, eine von Braze gehostete Website, die den Abonnementstatus und den Status der Abonnementgruppen Ihrer Benutzer anzeigen kann. Ihr Entwickler-Team kann das Präferenzzentrum mit Hilfe von HTML und CSS so gestalten, dass das Styling der Seite Ihren Markenrichtlinien entspricht.

Mit Liquid können Sie die Namen Ihrer Abonnementgruppen und den Status der einzelnen Benutzer abrufen. Auf diese Weise speichert Braze diese Daten und ruft sie ab, wenn die Seite geladen wird.

### Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Aktiviertes Präferenzzentrum | Ihr Braze Dashboard verfügt über die Berechtigung zur Nutzung der Einstellungscenter-Funktion. |
| Gültiger Arbeitsbereich mit einer E-Mail-, SMS- oder WhatsApp-Abonnementgruppe | Ein Arbeitsbereich mit gültigen Benutzern und einer E-Mail-, SMS- oder WhatsApp-Abonnementgruppe. |
| Gültiger Benutzer | Ein Benutzer mit einer E-Mail-Adresse und einer externen ID. |
| Erstellter API-Schlüssel mit Berechtigungen für das Einstellungszentrum | Gehen Sie im Braze-Dashboard zu **Einstellungen** > **API-Schlüssel**, um zu bestätigen, dass Sie Zugriff auf einen API-Schlüssel mit Berechtigungen für das Einstellungszentrum haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Schritt 1: Verwenden Sie den Endpunkt „Präferenzzentrum erstellen“

Beginnen Sie mit der Erstellung eines Präferenzzentrums, indem Sie den [Endpunkt „Präferenzzentrum erstellen“]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/) verwenden. Um Ihr Präferenzzentrum anzupassen, können Sie HTML in das `preference_center_page_html`-Feld und das `confirmation_page_html`-Feld einfügen, das Ihrem Branding entspricht.

Der [Endpunkt URL des Einstellungszentrums generieren]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/) ermöglicht es Ihnen, die URL des Einstellungszentrums für einen bestimmten Benutzer außerhalb einer über Braze gesendeten E-Mail zu erfassen.

### Schritt 2: In Ihrer E-Mail-Kampagne berücksichtigen

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Um einen Link zum Einstellungscenter in Ihren E-Mails zu platzieren, verwenden Sie den folgenden Liquid-Tag an der gewünschten Stelle in Ihrer E-Mail, ähnlich wie Sie URLs zum Abbestellen einfügen würden.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Sie können auch eine Kombination aus HTML und Liquid verwenden. Sie können zum Beispiel die folgende URL entweder im HTML-Editor oder im Drag-and-Drop-Editor einfügen. Dies zeigt die grundlegende Layout-Einstellung des Präferenzentrums, in dem alle E-Mail-Abonnementgruppen automatisch aufgelistet werden. 

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}">Edit your preferences</a>
```
{%endraw%}

Das Einstellungscenter verfügt über ein Kontrollkästchen, mit dem sich Ihre Benutzer von allen E-Mails abmelden können. Beachten Sie, dass Sie diese Einstellungen nicht speichern können, wenn sie als Testnachricht gesendet werden.

{% alert important %}
Der obige Liquid-Tag funktioniert nur, wenn Sie eine Kampagne oder ein Canvas starten. Beim Senden einer Test-E-Mail wird kein gültiger Link erzeugt.
{% endalert %}

#### Bearbeiten eines Präferenzzentrums

Sie können Ihr Präferenzzentrum über den [Endpunkt „Präferenzzentrum aktualisieren“]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) bearbeiten und aktualisieren. 

#### Identifizieren von Präferenzzentren und Details

Um Ihre Präferenzzentren zu identifizieren, verwenden Sie den [Endpunkt „Details für Präferenzzentrum anzeigen“]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/), um zugehörige Informationen wie den Zeitstempel des letzten Updates, die ID des Präferenzzentrums und mehr zu erhalten.

## Anpassung

Braze verwaltet die Updates des Abo-Status vom Präferenzzentrum aus, wodurch das Präferenzzentrum synchronisiert wird. Sie können jedoch auch Ihr eigenes Einstellungszentrum erstellen und hosten, indem Sie die [APIs für Abonnementgruppen]({{site.baseurl}}/api/endpoints/subscription_groups/) mit den folgenden Optionen verwenden.

### Option 1: Link mit String-Abfrageparametern

Verwenden Sie Abfrage-String-Feld-Wert-Paare im Hauptteil der URL, um die Nutzer-ID und die E-Mail-Kategorie an die Seite zu übergeben, sodass Nutzer:innen nur ihre Wahl zum Abbestellen bestätigen müssen. Diese Option eignet sich für diejenigen, die einen Nutzer-Bezeichner in einem Hash-Format speichern und noch kein Abo-Center haben.

Bei dieser Option muss für jede E-Mail-Kategorie ein eigener Link zum Abmelden angegeben werden:<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
Es ist auch möglich, die externe ID des Nutzers oder der Nutzerin beim Senden mit Hilfe eines Liquid-Filters mit einem Hash zu versehen. Damit wird die Adresse `user_id` beispielsweise in einen MD5-Hash-Wert umgewandelt:
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### Option 2: Authentifizierung mit JSON-Web-Token

Verwenden Sie ein [JSON-Web-Token](https://auth0.com/learn/json-web-tokens/), um Benutzer bei einem Teil Ihres Webservers zu authentifizieren (z. B. bei den Kontoeinstellungen), der sich normalerweise hinter einer Authentifizierungsschicht wie der Anmeldung mit Benutzername und Passwort befindet. 

Bei diesem Ansatz sind keine in die URL eingebetteten Abfrage-String-Wert-Paare erforderlich, da diese z. B. in der Nutzlast des JSON-Web-Tokens übergeben werden können:

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": offers
}
```

## Häufig gestellte Fragen

### Ich habe kein Einstellungscenter erstellt. Warum sehe ich "PreferenceCenterBrazeDefault" auf meinem Dashboard?

Dies wird verwendet, um das Einstellungscenter zu rendern, wenn das alte Liquid {%raw%}`${preference_center_url}`{%endraw%} verwendet wird. Das bedeutet, dass Canvas-Schritte oder Vorlagen, die entweder auf {%raw%}`${preference_center_url}` oder `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} verweisen, nicht funktionieren. Dies gilt auch für zuvor gesendete Nachrichten, die das Legacy Liquid oder "PreferenceCenterBrazeDefault" als Teil der Nachricht enthielten. 

Wenn Sie in einer neuen Nachricht erneut auf {%raw%}`${preference_center_url}`{%endraw%} verweisen, wird erneut ein Einstellungscenter mit dem Namen "PreferenceCenterBrazeDefault" erstellt.

### Unterstützen die Präferenzzentren mehrere Sprachen?

Nein. Sie können jedoch Liquid nutzen, wenn Sie das HTML für angepasste Opt-in und Opt-out Seiten schreiben. Wenn Sie dynamische Links verwenden, um Abmeldungen zu verwalten, ist dies ein einzelner Link. 

Wenn Sie z.B. die Abmelderate für spanischsprachige Nutzer:innen tracken möchten, müssen Sie entweder separate Kampagnen verwenden oder Analytics rund um Currents nutzen (z.B. nachsehen, wann sich ein Nutzer:innen abmeldet und die bevorzugte Sprache dieses Nutzers überprüfen).

Ein weiteres Beispiel: Um die Abmelderaten spanischsprachiger Nutzer zu tracken, könnten Sie der Abmelde-URL einen Query-Parameter-String wie `?Spanish=true` hinzufügen, wenn die Sprache der Nutzer:innen Deutsch ist, und einen regulären Abmeldelink verwenden, wenn dies nicht der Fall ist:

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

Dann könnten Sie über Currents herausfinden, welche Nutzer:innen Spanisch sprechen und wie viele Klicks auf den Abmeldelink erfolgten.

### Sind sowohl Abmelde-Links als auch E-Mail-Präferenzzentren für den Versand erforderlich?

Nein. Wenn Sie beim Verfassen einer E-Mail-Kampagne die Nachricht "Ihr E-Mail-Text enthält keinen Abmeldelink" sehen, wird diese Warnung erwartet, wenn sich Ihr Abmeldelink in einem Content-Block befindet.
