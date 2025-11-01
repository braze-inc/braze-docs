---
nav_title: "Automatiser l'enregistrement de Zoom"
article_title: "Automatiser l'enregistrement de Zoom"
page_order: 1
page_type: tutorial
description: "Cet article décrit comment automatiser l'inscription des participants à Zoom dans vos campagnes d'e-mails, de push et de messages in-app."
channel: 
  - email
  - push
  - in-app messages

---

# Automatiser l'enregistrement de Zoom

> Depuis quelques années, les clients de Braze organisent de plus en plus souvent des webinaires. Lors de l'organisation d'un webinaire Zoom, les utilisateurs doivent saisir leurs informations sur une page de renvoi Zoom pour s'inscrire. 

Un flux d'utilisateurs recommandé est présenté ci-dessous :
1. Planifiez un webinaire dans Zoom et générez un `webinarId`.
2. Utilisez Braze pour promouvoir les webinaires Zoom via des canaux d'e-mail, de push et de messages in-app. 
3. Incluez dans ces communications un bouton d'appel à l'action qui ajoute automatiquement les utilisateurs au webinaire.

Pour ce faire, vous pouvez utiliser les [API de Zoom](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate) pour ajouter automatiquement un utilisateur à un webinaire grâce à un clic sur un bouton dans un e-mail, un push ou un message in-app. Utilisez l'endpoint suivant, en remplaçant l'ID du webinaire dans la requête API. 

POST : `/meetings/{webinarId}/registrants`

Pour plus d'informations, reportez-vous au [point de terminaison](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate) Zoom [Ajouter une personne inscrite à un webinaire](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate).<br><br>

{% tabs %}
{% tab Email %}

Créez une campagne e-mail avec un bouton d'appel à l'action dans le corps du message. Lorsqu'un utilisateur clique sur le bouton, redirigez-le vers la page d'atterrissage du webinaire (avec les paramètres appropriés inclus dans le lien de redirection). 

En utilisant les paramètres de l'URL pour transmettre les données de l'utilisateur, créez un appel API à lancer au chargement de la page pour ajouter l'utilisateur au webinaire.

\![Message e-mail avec Liquid templating utilisé pour inclure le prénom, le nom, l'adresse e-mail et la ville.]({% image_buster /assets/img/zoom/zoom1.png %})

Les utilisateurs sont maintenant inscrits au webinaire avec les détails qui existent déjà sur leur profil Braze.

{% endtab %}
{% tab Push %}

1. Créer une campagne de push<br><br>

	Définissez le comportement du bouton au clic pour qu'il renvoie à la page d'atterrissage du webinaire.<br>

	Lien vers le webinaire lorsqu'un bouton est cliqué.]({% image_buster /assets/img/zoom/zoom2.png %})<br><br>

	Un exemple simple de page d'atterrissage pour les utilisateurs qui s'inscrivent via un clic de bouton à partir d'un push. Indiquez à l'utilisateur ce pour quoi il s'est inscrit et confirmez son inscription :<br>

	\![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. Créez une campagne webhook déclenchée par le message in-app ou le clic sur le bouton.<br><br>
 	À l'aide des données existantes sur le profil utilisateur de Braze, inscrivez l'utilisateur au webinaire.<br>

	!Une campagne basée sur une action qui sera envoyée aux utilisateurs qui ont cliqué sur un bouton d'une campagne spécifique.]({% image_buster /assets/img/zoom/zoom6.png %})<br><br>

	Exemple d'appel webhook vers l'endpoint Zoom.<br>
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

3. Les utilisateurs sont maintenant inscrits au webinaire avec les détails qui existent déjà sur leur profil Braze.

{% endtab %}
{% tab In-app message %}

1. Créer une campagne de messages in-app<br><br>

	Définissez le comportement du bouton au clic pour qu'il renvoie à la page d'atterrissage du webinaire.<br>

	Lien vers le webinaire lorsqu'un bouton est cliqué.]({% image_buster /assets/img/zoom/zoom3.png %})<br><br>

	Un exemple simple de page d'atterrissage pour les utilisateurs qui s'inscrivent via un clic sur un bouton à partir d'un message in-app. Indiquez à l'utilisateur ce pour quoi il s'est inscrit et confirmez son inscription :<br>

	\![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. Créez une campagne webhook déclenchée par le message in-app ou le clic sur le bouton.<br><br>
	À l'aide des données existantes sur le profil utilisateur de Braze, inscrivez l'utilisateur au webinaire.<br>

	Une campagne basée sur une action qui sera envoyée aux utilisateurs qui ont cliqué sur un bouton d'une campagne spécifique.]({% image_buster /assets/img/zoom/zoom5.png %})<br><br>

	Exemple d'appel webhook vers l'endpoint Zoom.<br>
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
3. Les utilisateurs sont maintenant inscrits au webinaire avec les détails qui existent déjà sur leur profil Braze.

{% endtab %}
{% endtabs %}
