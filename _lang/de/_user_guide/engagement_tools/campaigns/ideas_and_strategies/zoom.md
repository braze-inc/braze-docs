---
nav_title: Automatisieren Sie die Zoom-Registrierung
article_title: Zoom-Registrierung automatisieren
page_order: 1
page_type: tutorial
description: "Dieser Artikel beschreibt, wie Sie die Registrierung von Zoom-Teilnehmern in Ihren E-Mail-, Push- und In-App-Kampagnen automatisieren können."
channel: 
  - email
  - push
  - in-app messages

---

# Automatisieren Sie die Zoom-Registrierung

> Webinare sind für Braze-Kunden in den letzten Jahren zu einer festen Einrichtung geworden. Wenn Sie ein Zoom-Webinar veranstalten, müssen Nutzer:innen ihre Daten auf einer Zoom-Landing-Page eingeben, um sich zu registrieren. 

Im Folgenden wird ein empfohlener Benutzerablauf skizziert:
1. Planen Sie ein Webinar in Zoom und erstellen Sie eine `webinarId`.
2. Nutzen Sie Braze, um Zoom Webinare über E-Mail-, Push- und In-App-Nachricht-Kanäle zu bewerben. 
3. Fügen Sie in diese Mitteilungen einen Aktions-Button ein, der Nutzer:innen automatisch zum Webinar hinzufügt.

Dazu können Sie die [Zoom-APIs](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate) verwenden, um einen Benutzer automatisch zu einem Webinar hinzuzufügen, indem Sie auf eine Schaltfläche in einer E-Mail, einer Push-Nachricht oder einer In-App-Nachricht klicken. Verwenden Sie den folgenden Endpunkt und ersetzen Sie dabei die Webinar ID in der API-Anfrage. 

POST: `/meetings/{webinarId}/registrants`

Weitere Informationen finden Sie unter dem [Endpunkt Webinar-Anmelder hinzufügen von](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate) Zoom.<br><br>

{% tabs %}
{% tab Email %}

Erstellen Sie eine E-Mail-Kampagne mit einer Call-to-Action-Schaltfläche im Nachrichtentext. Wenn ein:e Nutzer:in auf den Button klickt, leiten Sie ihn auf die Webinar-Landing-Page um (mit den entsprechenden Parametern im Umleitungslink). 

Verwenden Sie die Parameter in der URL, um Nutzerdaten zu übergeben, und erstellen Sie einen API-Aufruf, der beim Laden der Seite ausgelöst wird, um die:den Nutzer:in zum Webinar hinzuzufügen.

![E-Mail Nachricht mit Liquid-Template, das Vorname, Nachname, E-Mail-Adresse und Ort enthält.]({% image_buster /assets/img/zoom/zoom1.png %})

Nutzer:innen sind nun für das Webinar mit den Angaben registriert, die bereits in ihrem Braze-Profil vorhanden sind.

{% endtab %}
{% tab Push %}

1. Erstellen Sie eine Push-Kampagne<br><br>

	Legen Sie das On-Click-Verhalten für den Button fest, um einen Link zur Webinar-Landing-Page zu erstellen.<br>

	![Verlinkung zum Webinar, wenn ein Button angeklickt wird.]({% image_buster /assets/img/zoom/zoom2.png %})<br><br>

	Ein einfaches Beispiel für eine Landing Page für Benutzer, die sich per Klick auf eine Schaltfläche aus einem Push-Mailing anmelden. Teilen Sie dem Benutzer mit, wofür er sich angemeldet hat und bestätigen Sie seine Anmeldung:<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. Erstellen Sie eine Webhook-Kampagne, die durch eine In-App-Nachricht oder einen Klick auf einen Button getriggert wird.<br><br>
 	Melden Sie die Nutzer:innen anhand der bestehenden Nutzerdaten in ihrem Braze Profil für das Webinar an.<br>

	![Eine aktionsbasierte Kampagne, die an Nutzer:innen gesendet wird, die auf einen Button für eine bestimmte Kampagne geklickt haben.]({% image_buster /assets/img/zoom/zoom6.png %})<br><br>

	Beispiel für einen Webhook-Aufruf an den Zoom-Endpunkt.<br>
	{% raw %}
	```json
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}

3. Nutzer:innen sind nun für das Webinar mit den Angaben registriert, die bereits in ihrem Braze-Profil vorhanden sind.

{% endtab %}
{% tab In-app message %}

1. In-App-Nachrichtenkampagne erstellen<br><br>

	Legen Sie das On-Click-Verhalten für den Button fest, der auf die Webinar-Landing-Page verweist<br>

	![Verlinkung zum Webinar, wenn ein Button angeklickt wird.]({% image_buster /assets/img/zoom/zoom3.png %})<br><br>

	Ein einfaches Beispiel für eine Landing Page für Benutzer, die sich per Klick auf eine Schaltfläche in einer In-App-Nachricht anmelden. Teilen Sie dem Benutzer mit, wofür er sich angemeldet hat und bestätigen Sie seine Anmeldung:<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. Erstellen Sie eine Webhook-Kampagne, die durch eine In-App-Nachricht oder einen Klick auf einen Button getriggert wird.<br><br>
	Melden Sie die Nutzer:innen anhand der bestehenden Nutzerdaten in ihrem Braze Profil für das Webinar an.<br>

	![Eine aktionsbasierte Kampagne, die an Nutzer:innen gesendet wird, die auf einen Button für eine bestimmte Kampagne geklickt haben.]({% image_buster /assets/img/zoom/zoom5.png %})<br><br>

	Beispiel für einen Webhook-Aufruf an den Zoom-Endpunkt.<br>
	{% raw %}
	```json
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}
3. Nutzer:innen sind nun für das Webinar mit den Angaben registriert, die bereits in ihrem Braze-Profil vorhanden sind.

{% endtab %}
{% endtabs %}
