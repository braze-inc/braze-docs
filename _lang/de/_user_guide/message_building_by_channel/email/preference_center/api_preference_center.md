---
nav_title: API-E-Mail-Einstellungscenter
article_title: API-E-Mail-Einstellungscenter
page_order: 1
description: "Dieser Artikel beschreibt das API-E-Mail-Einstellungscenter und wie Sie es anpassen können."
channel:
  - email
---

# API-E-Mail-Einstellungscenter

> Die Einrichtung eines Einstellungscenters bietet Ihren Nutzer:innen eine zentrale Anlaufstelle zur Bearbeitung und Verwaltung ihrer Benachrichtigungseinstellungen für Ihre [E-Mail-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/email/). Dieser Artikel enthält Schritte zur Erstellung eines API-generierten Einstellungscenters. Sie können ein Einstellungscenter aber auch mit dem [Drag-and-Drop-Editor]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/) erstellen.

Gehen Sie im Braze-Dashboard zu **Zielgruppe** > **E-Mail-Einstellungscenter**.

Hier können Sie jede Abo-Gruppe verwalten und einsehen. Jede Abo-Gruppe, die Sie erstellen, wird zu dieser Einstellungscenter-Liste hinzugefügt. Sie können mehrere Einstellungscenter erstellen.

{% alert important %}
Das Einstellungscenter ist für die Verwendung innerhalb des E-Mail-Kanals von Braze vorgesehen. Die Links zum Einstellungscenter sind für jede:n Nutzer:in dynamisch und können nicht extern gehostet werden.
{% endalert %}

## Erstellen eines Einstellungscenters mit API

Mit den [Braze-Endpunkten für das Preference Center]({{site.baseurl}}/api/endpoints/preference_center) können Sie ein Einstellungscenter erstellen – eine von Braze gehostete Website, die den Abo-Status und den Abo-Gruppenstatus Ihrer Nutzer:innen anzeigen kann. Mithilfe von HTML und CSS kann Ihr Entwickler:innen-Team das Einstellungscenter so gestalten, dass das Styling der Seite Ihren Markenrichtlinien entspricht.

Mit Liquid können Sie die Namen Ihrer Abo-Gruppen und den Status der einzelnen Nutzer:innen abrufen. Auf diese Weise speichert und ruft Braze diese Daten ab, wenn die Seite geladen wird.

### Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Aktiviertes Einstellungscenter | Ihr Braze-Dashboard verfügt über die Berechtigung zur Nutzung der Einstellungscenter-Funktion. |
| Gültiger Workspace mit einer E-Mail-, SMS- oder WhatsApp-Abo-Gruppe | Ein funktionierender Workspace mit gültigen Nutzer:innen und einer E-Mail-, SMS- oder WhatsApp-Abo-Gruppe. |
| Gültige:r Nutzer:in | Ein:e Nutzer:in mit einer E-Mail-Adresse und einer externen ID. |
| Generierter API-Schlüssel mit Einstellungscenter-Berechtigungen | Gehen Sie im Braze-Dashboard zu **Einstellungen** > **API-Schlüssel**, um zu bestätigen, dass Sie Zugriff auf einen API-Schlüssel mit Einstellungscenter-Berechtigungen haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 1. Schritt: Verwenden Sie den Endpunkt „Einstellungscenter erstellen"

Beginnen Sie mit der Erstellung eines Einstellungscenters, indem Sie den [Endpunkt „Einstellungscenter erstellen"]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/) verwenden. Um Ihr Einstellungscenter anzupassen, können Sie HTML, das Ihrem Branding entspricht, in das Feld `preference_center_page_html` und das Feld `confirmation_page_html` einfügen.

Der [Endpunkt „URL des Einstellungscenters generieren"]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/) ermöglicht es Ihnen, die URL des Einstellungscenters für eine:n bestimmte:n Nutzer:in außerhalb einer über Braze gesendeten E-Mail abzurufen.

### 2. Schritt: In Ihre E-Mail-Kampagne einbinden

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Um einen Link zum Einstellungscenter in Ihren E-Mails zu platzieren, verwenden Sie den folgenden Liquid-Tag an der gewünschten Stelle in Ihrer E-Mail – ähnlich wie Sie URLs zum Abmelden einfügen würden.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Sie können auch eine Kombination aus HTML und Liquid verwenden. Sie können zum Beispiel Folgendes als URL entweder im HTML-Editor oder im Drag-and-Drop-Editor einfügen. Dies zeigt das grundlegende Einstellungscenter-Layout, in dem alle E-Mail-Abo-Gruppen automatisch aufgelistet werden. Wenn Sie [Link Aliasing]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/) verwenden, fügen Sie nach dem Liquid-Tag ein abschließendes Fragezeichen (`?`) hinzu, damit Braze Tracking-Parameter anhängen kann.

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}?">Edit your preferences</a>
```
{%endraw%}

Das Einstellungscenter verfügt über ein Kontrollkästchen, mit dem sich Ihre Nutzer:innen von allen E-Mails abmelden können. Beachten Sie, dass Sie diese Einstellungen nicht speichern können, wenn sie als Testnachricht gesendet werden.

{% alert important %}
Der obige Liquid-Tag funktioniert nur beim Starten einer Kampagne oder eines Canvas. Beim Senden einer Test-E-Mail wird kein gültiger Link erzeugt. Um den Einstellungscenter-Link zu überprüfen, starten Sie die Nachricht in einer Kampagne, die nur auf Ihr Testprofil ausgerichtet ist.
{% endalert %}

#### Bearbeiten eines Einstellungscenters

Sie können Ihr Einstellungscenter über den [Endpunkt „Einstellungscenter aktualisieren"]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) bearbeiten und aktualisieren. 

#### Identifizieren von Einstellungscentern und Details

Um Ihre Einstellungscenter zu identifizieren, verwenden Sie den [Endpunkt „Details für Einstellungscenter anzeigen"]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/), um zugehörige Informationen wie den Zeitstempel des letzten Updates, die Einstellungscenter-ID und mehr abzurufen.

## Anpassung

Braze verwaltet die Abo-Status-Updates vom Einstellungscenter aus, wodurch das Einstellungscenter synchron gehalten wird. Sie können jedoch auch Ihr eigenes Einstellungscenter erstellen und hosten, indem Sie die [APIs für Abo-Gruppen]({{site.baseurl}}/api/endpoints/subscription_groups/) mit den folgenden Optionen verwenden.

### Option 1: Link mit String-Abfrageparametern

Verwenden Sie Abfrage-String-Feld-Wert-Paare im Hauptteil der URL, um die Nutzer-ID und die E-Mail-Kategorie an die Seite zu übergeben, sodass Nutzer:innen nur ihre Wahl zum Abmelden bestätigen müssen. Diese Option eignet sich für diejenigen, die einen Nutzer-Bezeichner in einem Hash-Format speichern und noch kein Abo-Center haben.

Bei dieser Option muss für jede E-Mail-Kategorie ein eigener Link zum Abmelden angegeben werden:<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
Es ist auch möglich, die externe ID der/des Nutzer:in beim Senden mithilfe eines Liquid-Filters zu hashen. Damit wird die `user_id` beispielsweise in einen MD5-Hash-Wert umgewandelt:
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### Option 2: Authentifizierung mit JSON-Web-Token

Verwenden Sie ein [JSON-Web-Token](https://auth0.com/learn/json-web-tokens/), um Nutzer:innen bei einem Teil Ihres Webservers zu authentifizieren (z. B. bei den Kontoeinstellungen), der sich normalerweise hinter einer Authentifizierungsschicht wie der Anmeldung mit Benutzername und Passwort befindet. 

Bei diesem Ansatz sind keine in die URL eingebetteten Abfrage-String-Wert-Paare erforderlich, da diese z. B. in der Nutzlast des JSON-Web-Tokens übergeben werden können:

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": "offers"
}
```

## Häufig gestellte Fragen

### Ich habe kein Einstellungscenter erstellt. Warum sehe ich „PreferenceCenterBrazeDefault" in meinem Dashboard?

Dies wird verwendet, um das Einstellungscenter zu rendern, wenn das veraltete Liquid {%raw%}`${preference_center_url}`{%endraw%} verwendet wird. Das bedeutet, dass Canvas-Schritte oder Templates, die auf {%raw%}`${preference_center_url}` oder `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} verweisen, nicht funktionieren. Dies gilt auch für zuvor gesendete Nachrichten, die das veraltete Liquid oder „PreferenceCenterBrazeDefault" als Teil der Nachricht enthielten. 

Wenn Sie in einer neuen Nachricht erneut auf {%raw%}`${preference_center_url}`{%endraw%} verweisen, wird erneut ein Einstellungscenter mit dem Namen „PreferenceCenterBrazeDefault" erstellt.

### Unterstützen Einstellungscenter mehrere Sprachen?

Nein. Sie können jedoch Liquid nutzen, wenn Sie das HTML für angepasste Opt-in- und Opt-out-Seiten schreiben. Wenn Sie dynamische Links verwenden, um Abmeldungen zu verwalten, handelt es sich um einen einzelnen Link. 

Wenn Sie z. B. die Abmeldungsrate für spanischsprachige Nutzer:innen tracken möchten, müssen Sie entweder separate Kampagnen verwenden oder Analytics rund um Currents nutzen (z. B. nachsehen, wann sich Nutzer:innen abmelden, und die bevorzugte Sprache dieser Nutzer:innen überprüfen).

Ein weiteres Beispiel: Um die Abmeldungsraten spanischsprachiger Nutzer:innen zu tracken, könnten Sie der Abmelde-URL einen Query-Parameter-String wie `?Spanish=true` hinzufügen, wenn die Sprache der Nutzer:innen Spanisch ist, und einen regulären Abmeldelink verwenden, wenn dies nicht der Fall ist:

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

Dann könnten Sie über Currents herausfinden, welche Nutzer:innen Spanisch sprechen und wie viele Klick-Events es für diesen Abmeldelink gab.

### Sind sowohl Abmelde-Links als auch E-Mail-Einstellungscenter für den Versand erforderlich?

Nein. Wenn Sie beim Verfassen einer E-Mail-Kampagne die Nachricht „Ihr E-Mail-Text enthält keinen Abmeldelink" sehen, ist diese Warnung zu erwarten, wenn sich Ihr Abmeldelink in einem Content-Block befindet.

### Wie kann ich das Standard-Browser-Symbol aktualisieren?

Standardmäßig wird für das Symbol neben dem Namen des Browser-Tabs (Favicon) das Braze-Logo verwendet. Um ein angepasstes Favicon hinzuzufügen, legen Sie es über das Attribut `links-tags` in Ihrem API-Aufruf zum Erstellen oder Aktualisieren des [Preference Center]({{site.baseurl}}/api/endpoints/preference_center) fest. Braze fügt dann den {% raw %}`<link rel="icon" ...>`{% endraw %}-Tag für Sie in die gehostete Seite ein.

{% raw %}
```
{
  "name": "MyPreferenceCenter",
  "preference_center_title": "Email Preferences",
  "preference_center_page_html": "<!doctype html> ...",
  "confirmation_page_html": "<!doctype html> ...",
  "state": "active",
  "options": {
    "links-tags": [
      {
        "rel": "icon",
        "type": "image/png",
        "sizes": "32x32",
        "href": "https://yourcdn.com/path/to/favicon-32x32.png"
      },
      {
        "rel": "shortcut icon",
        "type": "image/x-icon",
        "href": "https://yourcdn.com/path/to/favicon.ico"
      },
      {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://yourcdn.com/path/to/apple-touch-icon.png"
      }
    ]
  }
}
```
{% endraw %}