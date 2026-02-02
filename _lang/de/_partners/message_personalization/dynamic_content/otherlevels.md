---
nav_title: AndereLevels
article_title: AndereLevels
alias: /partners/otherlevels/
description: "Dieser Artikel behandelt die Integration zwischen OtherLevels Experience Platform und Braze."
page_type: partner
search_tag: OtherLevels

---

# AndereLevels

> Die [OtherLevels](https://www.otherlevels.com/) Experience Platform nutzt GenAI, um die Art und Weise zu verändern, wie Sportmarken, Verlage und Operatoren mit ihren Kund:innen in Kontakt treten, indem sie traditionelle Inhalte in markengerechte, personalisierte Video- und Rich-Media-Erlebnisse in großem Umfang umwandelt.

*Diese Integration wird von OtherLevels gepflegt.*

## Übersicht

Die Integration von Braze und OtherLevels ermöglicht es Ihnen, angepasste GenAI-Videos über API-Aufrufe an die OtherLevels Experience Platform zu erstellen und diese Videos dann als iOS Push-Videos über [Braze Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) an Ihre Nutzer:innen zu senden.

Bieten Sie Ihren Nutzer:innen ein besseres Erlebnis mit OtherLevels KI-gestützter Erfahrung. Transformieren Sie vorhandene und fremde Inhalte in hochskalierbare Videos und Rich Media für Zielgruppen, die bereits anders konsumieren und stark auf kontextuelle, personalisierte Erlebnisse reagieren.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung          | Beschreibung                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Ein OtherLevels-Konto   | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein OtherLevels-Konto.                                                                     |
| Ein Braze REST API-Schlüssel  | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Ein Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Diese Integration erfordert den Aufruf der OtherLevels Experience Platform API als Teil des Video-Generierungsprozesses, bevor Nachrichten von Braze an Ihre Nutzer:innen gesendet werden können. cURL-Beispiele werden als Teil dieser Dokumentation zur Verfügung gestellt, wir empfehlen jedoch die Verwendung von API-Clients wie Postman, um die API-Aufrufe zu automatisieren.

## Anwendungsfälle

Verwenden Sie GenAI Videos, die mit der OtherLevels Experience Platform erstellt wurden, um:
- Schaffen Sie bessere Erfahrungen für Sporteigentümer und -ligen, Fan-Engagement, Sportwetten, iGaming und Lotterien.
- Verstärken Sie Ihr Kundenmarketing, indem Sie textbasierte Inhalte in Rich Media und Video transformieren und so menschliche und engagierte Erlebnisse schaffen.
- Verbessern Sie die Ergebnisse von der Akquise bis zur Bindung, indem Sie Ihre bestehende Integration in Braze erweitern und nicht umrüsten.

## Integration der OtherLevels Experience Platform

### Schritt 1: Rufen Sie die OtherLevels Experience Platform API auf, um ein Video zu erstellen {#step-1}

Der erste Schritt der Integration besteht darin, die OtherLevels Experience Platform API aufzurufen, um ein neues Video zu erstellen. Beachten Sie, dass die Erzeugung von Videos nicht sofort erfolgt. Je nach Länge und Komplexität des Videos kann die Erstellung der Inhalte bis zu einer halben Stunde dauern. Planen Sie Ihre Zeitpläne für Messaging und API-Aufrufe entsprechend, damit die API-Aufrufe zur Erzeugung von Videos rechtzeitig vor dem geplanten Versand Ihrer Nachrichten von Braze erfolgen.

{% alert important %}
Die folgende Anfrage verwendet cURL. Für eine effizientere Verwaltung von API-Anfragen empfehlen wir die Verwendung eines API-Clients wie Postman.
{% endalert %}

Das folgende Beispiel referenziert, wie Sie Ihren API-Aufruf strukturieren sollten. Weitere Informationen zum Anpassen der Video-Spezifikationen und zur Strukturierung Ihres API-Aufrufs finden Sie unter [Anpassen des GenAI-Videos](#customizing-the-genai-video).

{% raw %}
```bash
curl --request POST \
  --url 'https://exp-platform-api.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media?=' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.0' \
  --data '{
    "task": {
        "type": "tasks",
        "tasks": {
            "image_video_overlay": {
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''",
                "color": "255,255,255,0",
                "y_pos": "0",
                "x_pos": "0",
                "image_input": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_replace_bg.mp4",
                "type": "compose.ImageVideoOverlay"
            },
            "resize_image": {
                "media_input": "= tasks.bg_image.jpg ?? tasks.bg_image.png",
                "type": "compose.MediaResize",
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''"
            },
            "bg_image": {
                "type": "load",
                "url": "BACKGROUND_IMAGE_URL",
                "refresh_interval": "12h"
            },
            "talking_head": {
                "test": false,
                "title": "INSERT_TITLE",
                "caption": false,
                "templateId": "TALENT_TEMPLATE",
                "type": "TALENT_MODEL",
                "variables": {
                    "script": {
                        "name": "script",
                        "properties": {
                            "content": "= tasks.translate_text.text"
                        },
                        "type": "text"
                    }
                }
            },
            "translate_text": {
                "type": "translate_text",
                "source": "en",
                "target": "en",
                "text": "INSERT_SCRIPT"
            },
            "talking_talent_speed": {
                "type": "compose.VideoSetSpeed",
                "speed": "1.0",
                "video_input": "= tasks.talking_head.mp4"
            },
            "talking_talent_replace_bg": {
                "type": "compose.VideoReplaceBg",
                "video_background": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_speed.mp4"
            }
        },
        "output": "image_video_overlay"
    }
}'
```
{% endraw %}

Ersetzen Sie Folgendes:

| Platzhalter          | Beschreibung                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `OTHERLEVELS_PROJECT_KEY`   | Ein OtherLevels-Projektschlüssel wird Ihnen zur Verfügung gestellt, wenn Sie ein OtherLevels-Konto eingerichtet haben.                                                                     |
| `BACKGROUND_IMAGE_URL`  | Eine HTTPS-URL für den Hintergrund des Videos. |
| `INSERT_TITLE` | Der Titel des Videos, dies ist eine interne Referenzierung und wird im Video nicht angezeigt.                                                 |
| `TALENT_TEMPLATE` | A Talent Template ID. OtherLevels wird mit Ihnen bei der Einrichtung Ihres Kontos zusammenarbeiten, um ein Talent (Avatar) zu erstellen. Sie erhalten eine oder mehrere Talent IDs, die Sie verwenden können.                                                 |
| `TALENT_MODEL` | A Talent Model ID. OtherLevels wird mit Ihnen bei der Einrichtung Ihres Kontos zusammenarbeiten, um ein Talent (Avatar) zu erstellen. Sie erhalten ein oder mehrere Talentmodelle, die Sie verwenden können.                                                 |
| `INSERT_SCRIPT` | Das genaue Skript, das der Sprecher während des Videos sagen soll.                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Als Teil der API-Antwort gibt OtherLevels eine JSON-Nutzlast zurück, die einen erfolgreichen API-Aufruf anzeigt. Die JSON-Datei enthält einen eindeutigen `recipe_id`, um das generierte Video zu identifizieren. Die `recipe_id` wird im nächsten Schritt benötigt.

Hier ist eine Beispielantwort der API:

{% raw %}
```bash
{"$schema":"https://exp-platform-api.prod.awsotherlevels.com/schemas/GenerateMediaResBody.json","message":"success","recipe_id":"LMINHWXV2BBD6JGV5VF3ZNZV7BDDRR7FH5FJH6MMX4BVLTPRKTWQ","media_short_id":"LMINHWX","status":"triggered"}
```
{% endraw %}

### Schritt 2: Einstellen der `recipe_id` als angepasstes Attribut

Die `recipe_id`, die Sie in [Schritt 1](#step-1) erhalten haben, ist nun als angepasstes Attribut von Braze für die Nutzer:innen eingestellt, an die Sie die Videos senden möchten.

Je nach Anwendungsfall haben Sie vielleicht ein einzelnes Video erstellt, das für eine große Zielgruppe bestimmt ist. In diesem Fall kann dasselbe `recipe_id` für mehrere Nutzer:innen eingestellt werden. Oder Sie haben mehrere eindeutige Videos erstellt, die jeweils auf einen anderen Nutzer:innen abzielen. In diesem Fall sollten Sie für jeden Nutzer:innen die angepassten Attribute von Braze unter `recipe_id` einstellen.

{% alert important %}
Die folgende Anfrage verwendet cURL. Für eine effizientere Verwaltung von API-Anfragen empfehlen wir die Verwendung eines API-Clients wie Postman.
{% endalert %}

{% raw %}
```bash
curl --location --request POST 'BRAZE_API_ENDPOINT/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer BRAZE_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "USER_ID",
      "olxpmedia": "RECIPE_ID"
    }
  ]
}'
```
{% endraw %}

Ersetzen Sie Folgendes:

| Platzhalter             | Beschreibung                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | Die URL des Braze REST-Endpunkts Ihrer aktuellen Braze-Instanz. Weitere Informationen finden Sie unter [REST-API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys). |
| `BRAZE_API_KEY`         | Ihr Braze REST API-Schlüssel mit der Berechtigung `users.track`.                                                                                                                                      |
| `USER_ID`              | Die ID des Nutzers:in, der dieses Video erhalten soll. Weitere Beispiele für die Bezeichner, die verwendet werden können, finden Sie unter [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users).                                                                                                                                                  |
| `RECIPE_ID`       | Die `recipe_id`, die Sie von der OtherLevels API Antwort in [Schritt 1](#step-1) erhalten haben.                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Schritt 3: Versenden über Braze Connected-Content

Um die GenAI Videos als iOS Push Nachrichten an Ihre Nutzer:innen zu senden, gehen Sie folgendermaßen vor:

1. Erstellen Sie eine Kampagne für Push-Benachrichtigungen für Braze iOS.
2. Gehen Sie bei der Erstellung Ihrer Kampagne in den Bereich **Assets** und fügen Sie die folgende Connected-Content-Syntax in das Feld **Von URL hinzufügen** ein.

{% raw %}
```
{% connected_content https://exp-platform-api-external.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media/{{custom_attribute.${olxpmedia}}} %}
```
{% endraw %}

Als nächstes ersetzen Sie `OTHERLEVELS_PROJECT_KEY` durch den von OtherLevels bereitgestellten Projektschlüssel.

{: start="3"}
3\. In der Dropdown-Liste für das **URL-Dateiformat** wählen Sie **MP4** aus.
4\. Konfigurieren Sie den Rest der Kampagne (z. B. den Inhalt der Nachrichten, den Zeitplan für den Versand und die Zielgruppen) nach Ihren Wünschen.

![Beispiel Asset-Felder für Connected-Content.]({% image_buster /assets/img/otherlevels/1.png %})

## Anpassen des GenAI Videos

### Videogröße und Attribute

Der Video-Hintergrund kann über die Taste `bg_image` festgelegt werden.

| Parameter             | Beschreibung                  |
|-------------------------|----------------------------|
| `url`    | HTTPS-URL für das Hintergrundbild. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Die Größe des Video-Hintergrunds kann über die Taste `resize_image` festgelegt werden. Wir empfehlen, dass das Hintergrundbild die gleiche Größe hat wie das, was hier konfiguriert ist.

| Parameter             | Beschreibung                  |
|-------------------------|----------------------------|
| `width`    | Breite des Hintergrundbildes, mit Optionen für Hoch- und Querformat. |
| `height`     | Höhe des Hintergrundbildes, mit Optionen für Hoch- und Querformat.                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Video Overlay Optionen können in der Taste `image_video_overlay` angegeben werden.

| Parameter             | Beschreibung                  |
|-------------------------|----------------------------|
| `width`    | Breite des Overlays, mit Optionen für Hoch- und Querformat. |
| `height`         | Höhe des Overlays, mit Optionen für Hoch- und Querformat.                                              |
| `color`              | Die Farbe des Overlays wird in RGB zusammen mit dem Video der Transparenz angegeben.                                                                   |
| `y_pos`       | Versatz der Y-Achse vom Zentrum.                                                              |
| `x_pos`    | Versatz der X-Achse vom Zentrum. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Talent und Drehbuch

Im Rahmen der Bereitstellung wird OtherLevels mit Ihnen zusammenarbeiten, um ein oder mehrere Talente (manchmal auch Avatare genannt) für die Verwendung in Ihren Videos zu erstellen. Je nach Anwendungsfall und Marke kann dies in Form eines Ihrer bestehenden Markenbotschafter oder einer eindeutigen Kreation erfolgen.

Nachdem diese erstellt wurden, erhalten Sie brauchbare `TALENT_TEMPLATE` und `TALENT_MODEL` IDs zur Verwendung mit unserer API. 

Das Sprachmodell, das zur Verarbeitung von Eingabeskripten verwendet wird, funktioniert am besten, wenn es ein natürliches Skript liefert, das ein Mensch lesen würde. In den meisten Fällen brauchen Sie keine zusätzliche Interpunktion, um das Skript manuell zu steuern. Wir empfehlen jedoch, alle Ihre Skripte zu testen, bevor Sie sie an eine echte Zielgruppe senden. Die Geschwindigkeit, mit der das Talent das Skript liest, kann über die Taste `talking_talent_speed` festgelegt werden.

| Parameter             | Beschreibung                  |
|-------------------------|----------------------------|
| `speed`    | Legen Sie die Geschwindigkeit fest, mit der das Talent das Skript lesen soll. Zum Beispiel: `1.5`.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Zusätzliche Überlegungen

- Nur die Plattform für Push-Benachrichtigungen von iOS unterstützt von Haus aus Video-Medien. Android Push-Benachrichtigungen unterstützen von Haus aus keine Videos, daher kann diese Integration nur für Ihre iOS Zielgruppe verwendet werden.
- Beim Empfang von Push-Benachrichtigungen für Videos auf iOS Geräten müssen Nutzer:innen die Push-Benachrichtigung gedrückt halten, damit das Video geladen und abgespielt werden kann. Dies ist ein Standardverhalten auf der iOS-Plattform und kann nicht angepasst werden.