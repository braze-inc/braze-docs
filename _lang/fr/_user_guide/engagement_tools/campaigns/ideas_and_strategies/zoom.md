---
nav_title: Automatiser l’enregistrement Zoom
article_title: Automatiser l’enregistrement Zoom
page_order: 1
page_type: tutorial
description: "Cet article décrit comment automatiser l’enregistrement de participants Zoom dans vous campagnes par e-mail, notification push ou message in-app."
channel: 
  - e-mail
  - Notification push
  - messages In-App

---

# Automatiser l’enregistrement de participants Zoom

Les clients de Braze hébergent fréquemment des webinaires depuis ces dernières années. Lorsque vous hébergez un webinaire Zoom, les utilisateurs doivent saisir leurs informations sur une page d’accueil Zoom pour s’inscrire. Le flux utilisateur conseillé est décrit ci-dessous :

1. Planifiez un webinaire sur Zoom et générez un `meetingId`.
2. Utilisez Braze pour promouvoir les webinaires Zoom à l’aide des canaux e-mail, de notification push et de message in-app. 
3. Ajoutez un bouton d’appel à l’action dans ces communications ajoutant automatiquement les utilisateurs au webinaire.

Vous pouvez faire ceci en utilisant l’[API Zoom](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate) pour ajouter automatiquement un utilisateur à un webinaire à l’aide d’un clic de bouton dans un e-mail, une notification push ou un message In-App. Utilisez l’endpoint suivant en remplaçant l’ID de la réunion dans la requête API. 

POST: `/meetings/{meetingId}/registrants`

Consultez l’endpoint [Ajouter un participant à la réunion](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate) Zoom pour plus d’informations.<br><br>

{% tabs %}
{% tab Email %}

Créez une campagne par e-mail avec un bouton d’appel à l’action dans le corps du message. Une fois qu’un utilisateur clique sur le bouton, redirigez-le vers la page d’accueil du webinaire (en ajoutant les paramètres appropriés dans le lien de redirection). 

En utilisant les paramètres de l’URL pour transmettre les données utilisateur, construisez un appel API pour qu’il se déclenche lors du chargement de la page pour ajouter un utilisateur au webinaire.

![Message e-mail avec une modélisation Liquid pour ajouter le prénom, le nom, l’adresse e-mail et la ville.]({% image_buster /assets/img/zoom/zoom1.png %})

Les utilisateurs sont maintenant enregistrés pour le webinaire avec les détails existant déjà dans leur profil Braze.

{% endtab %}
{% tab Push %}

1. Créer une campagne de notification push<br><br>

	Définir le comportement lors du clic pour le bouton pour le lier à la page d’accueil du webinaire.<br>

	![Lier vers le webinaire lorsqu’un bouton est cliqué.]({% image_buster /assets/img/zoom/zoom2.png %})<br><br>

	Un exemple simple de page d’accueil pour les utilisateurs s’inscrivant à l’aide d’un clic de bouton d’une notification push. Communiquez à votre utilisateur la raison pour laquelle il s’est inscrit et confirmez leur enregistrement :<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. Créez une campagne webhook déclenchée par le message in-app ou le clic de bouton.<br><br>
 	Inscrivez l’utilisateur au webinaire en utilisant les données utilisateur existantes sur leur profil Braze.<br>

	![Une campagne par événement qui sera envoyée aux utilisateurs qui ont cliqué un bouton d’une campagne spécifique.]({% image_buster /assets/img/zoom/zoom6.png %})<br><br>

	Exemple d’appel webhook à l’endpoint Zoom.<br>

	![]({% image_buster /assets/img/zoom/zoom7.png %})<br>

3. Les utilisateurs sont maintenant enregistrés pour le webinaire avec les détails existant déjà dans leur profil Braze.

{% endtab %}
{% tab In-app message %}

1. Créer une campagne de communication In-App<br><br>

	Définir le comportement lors du clic pour le bouton pour le lier à la page d’accueil du webinaire<br>

	![Lier vers le webinaire lorsqu’un bouton est cliqué.]({% image_buster /assets/img/zoom/zoom3.png %})<br><br>

	Un exemple simple de page d’accueil pour les utilisateurs s’inscrivant à l’aide d’un clic de bouton d’un message in-app. Communiquez à votre utilisateur la raison pour laquelle il s’est inscrit et confirmez leur enregistrement :<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. Créez une campagne webhook déclenchée par le message in-app ou le clic de bouton.<br><br>
	Inscrivez l’utilisateur au webinaire en utilisant les données utilisateur existantes sur leur profil Braze.<br>

	![Une campagne par événement qui sera envoyée aux utilisateurs qui ont cliqué un bouton d’une campagne spécifique.]({% image_buster /assets/img/zoom/zoom5.png %})<br><br>

	Exemple d’appel webhook à l’endpoint Zoom.<br>

	![]({% image_buster /assets/img/zoom/zoom7.png %})<br>

3. Les utilisateurs sont maintenant enregistrés pour le webinaire avec les détails existant déjà dans leur profil Braze.

{% endtab %}
{% endtabs %}
