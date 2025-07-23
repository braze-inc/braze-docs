---
nav_title: "Automatiser l'inscription Zoom"
article_title: "Automatiser l'inscription Zoom"
page_order: 1
page_type: tutorial
description: "Cet article décrit comment automatiser l’enregistrement de participants Zoom dans vous campagnes par e-mail, notification push ou message in-app."
channel: 
  - email
  - push
  - in-app messages

---

# Automatiser l’enregistrement Zoom

> Les clients de Braze hébergent fréquemment des webinaires depuis ces dernières années. Lorsque vous hébergez un webinaire Zoom, les utilisateurs doivent saisir leurs informations sur une page d’accueil Zoom pour s’inscrire. 

Le flux utilisateur conseillé est décrit ci-dessous :
1. Planifiez un webinaire sur Zoom et générez un `webinarId`.
2. Utilisez Braze pour promouvoir les webinaires Zoom à l’aide des canaux e-mail, de notification push et de message in-app. 
3. Ajoutez un bouton d’appel à l’action dans ces communications ajoutant automatiquement les utilisateurs au webinaire.

Cela peut être accompli en utilisant les [API Zoom](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate) pour ajouter automatiquement un utilisateur à un webinaire via un clic sur un bouton dans un e-mail, une notification push ou un message intégré à l'application. Utilisez l’endpoint suivant, en remplaçant l'ID du webinaire dans la requête d’API. 

POST : `/meetings/{webinarId}/registrants`

Pour plus d'informations, consultez l’endpoint [Ajouter un participant au webinaire](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate) de Zoom.<br><br>

{% tabs %}
{% tab E-mail %}

Créez une campagne par e-mail avec un bouton d’appel à l’action dans le corps du message. Lorsqu'un utilisateur clique sur le bouton, redirigez-le vers la page de destination du webinaire (avec les paramètres appropriés inclus dans le lien de redirection). 

En utilisant les paramètres de l’URL pour transmettre les données utilisateur, construisez un appel API pour qu’il se déclenche lors du chargement de la page pour ajouter un utilisateur au webinaire.

![Message e-mail avec modélisation Liquid pour inclure le prénom, le nom de famille, l'adresse e-mail et la ville.]({% image_buster /assets/img/zoom/zoom1.png %})

Les utilisateurs sont maintenant enregistrés pour le webinaire avec les détails existant déjà dans leur profil Braze.

{% endtab %}
{% tab Notification push %}

1. Créer une campagne de notification push<br><br>

	Définir le comportement lors du clic pour le bouton pour le lier à la page d’accueil du webinaire.<br>

	![Lien vers le webinaire en cas de clic sur un bouton.]({% image_buster /assets/img/zoom/zoom2.png %})<br><br>

	Un exemple simple de page d’accueil pour les utilisateurs s’inscrivant à l’aide d’un clic de bouton d’une notification push. Communiquez à votre utilisateur la raison pour laquelle il s’est inscrit et confirmez leur enregistrement :<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. Créez une campagne webhook déclenchée par le message in-app ou le clic de bouton.<br><br>
 	Inscrivez l’utilisateur au webinaire en utilisant les données utilisateur existantes sur leur profil Braze.<br>

	![Une campagne basée sur l'action qui sera envoyée aux utilisateurs ayant cliqué sur un bouton pour une campagne spécifique.]({% image_buster /assets/img/zoom/zoom6.png %})<br><br>

	Exemple d’appel webhook à l’endpoint Zoom.<br>
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

3. Les utilisateurs sont maintenant enregistrés pour le webinaire avec les détails existant déjà dans leur profil Braze.

{% endtab %}
{% tab Message dans l'application %}

1. Créer une campagne de communication in-app<br><br>

	Définissez le comportement du bouton au clic pour qu'il renvoie à la page d'atterrissage du webinaire.<br>

	![Lien vers le webinaire en cas de clic sur un bouton.]({% image_buster /assets/img/zoom/zoom3.png %})<br><br>

	Un exemple simple de page d’accueil pour les utilisateurs s’inscrivant à l’aide d’un clic de bouton d’un message in-app. Communiquez à votre utilisateur la raison pour laquelle il s’est inscrit et confirmez leur enregistrement :<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. Créez une campagne webhook déclenchée par le message in-app ou le clic de bouton.<br><br>
	Inscrivez l’utilisateur au webinaire en utilisant les données utilisateur existantes sur leur profil Braze.<br>

	![Une campagne basée sur l'action qui sera envoyée aux utilisateurs ayant cliqué sur un bouton pour une campagne spécifique.]({% image_buster /assets/img/zoom/zoom5.png %})<br><br>

	Exemple d’appel webhook à l’endpoint Zoom.<br>
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
3. Les utilisateurs sont maintenant enregistrés pour le webinaire avec les détails existant déjà dans leur profil Braze.

{% endtab %}
{% endtabs %}
