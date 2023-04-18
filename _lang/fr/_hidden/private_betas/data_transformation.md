---
nav_title: Transformation des données Braze
permalink: "/data_transformation/"
hidden: true
layout: dev_guide
---

# Transformation des données Braze

La transformation des données chez Braze vous permet de configurer et d’automatiser une intégration directe depuis diverses plateformes externes à Braze en utilisant des webhooks. Une fois que ces webhooks sont envoyés à Braze, ils peuvent être transformés en données utilisateur pertinentes, telles que des attributs, des événements ou des achats sur les profils utilisateur de Braze. Vous pouvez ensuite utiliser ces données utilisateur pour alimenter vos cas d’utilisation marketing.

{% alert important %}
La transformation des données est actuellement en accès anticipé. Contactez votre CSM Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

Le résultat de l’utilisation de la transformation des données est une solution low-code pour créer des intégrations entre la plateforme externe que vous désirez et Braze. Cela peut contribuer à remplacer le besoin qu’aurait votre équipe d’effectuer des appels API manuels, utiliser des outils d’intégration ou de plateforme de données client.

## Fonctionnement

![Une plateforme source externe à Braze est transférée dans Braze à l’aide de webhooks en utilisant la transformation des données et met à jour les profils utilisateurs.][8]

Dans Braze, vous définirez d’abord une transformation, qui est un mappage entre le contenu attendu d’un webhook entrant et les attributs, événements ou achats de Braze. Vous pouvez mélanger et faire correspondre ce que le webhook fournit avec la façon dont vous voulez que cela apparaisse dans Braze. Pour vous y aider, vous pouvez définir la transformation en parallèle avec un webhook reçu récemment.

Une fois votre transformation définie, vous pouvez configurer les webhooks de votre plateforme externe pour les envoyer directement à Braze. Votre transformation s’appliquera à chaque webhook ingéré et votre intégration directe sera terminée.

{% alert important %}
À partir de décembre 2022, l’équipe de transformation des données examinera et approuvera les transformations soumises.
{% endalert %}

## Créer une transformation

Tout d’abord, identifiez une plateforme externe que vous souhaitez connecter à Braze. Vérifiez que la plateforme propose des webhooks ou des notifications API. Ensuite, suivez ces étapes pour créer une transformation de données avec Braze.

1. Accédez au tableau de bord de Braze et sélectionnez la page **Transformations** dans la section **Data (Données)**, dans la barre de navigation de gauche. Cliquez sur **Créer une transformation**.![][5]<br><br>
2. Utilisation d’un exemple de charge utile de webhook de votre plateforme externe. Nous vous recommandons d’envoyer un webhook de test à Braze. Sur votre plateforme externe, saisissez l’URL du webhook comme destination. Si vous y êtes invité, choisissez une requête POST non authentifiée. Si la plate-forme externe a une capacité d’« envoi test », utilisez-la et appuyez sur **Refresh (Actualiser)** dans Braze pour afficher ce que Braze vient de recevoir.<br><br>
3. Trouvez les champs qui seront mappés aux champs Braze suivants :
- Un utilisateur Braze (`external_id`, `user_alias`, `braze_id` ou `email`)
- Attributs personnalisés (facultatif)
- Événements personnalisés (facultatif)
- Événements d’achat (facultatif)<br><br>
Par exemple, dans cet exemple de charge utile, l’`user_id` correspond à l’`external_id` de Braze et un champ webhook est défini comme un attribut personnalisé de Braze :<br>![][2]<br><br>
4. Sur la page des détails de la transformation de Braze, écrivez votre transformation qui mappe les valeurs de votre plateforme vers Braze. Par exemple, `user_id` peut être mappé à l’`external_id` de Braze. Vous pouvez utiliser des crochets pour référencer des éléments dans le webhook.<br><br>Dans l’exemple de charge utile, une telle transformation permettrait d’obtenir le mappage souhaité à partir de l’étape précédente :
- `user_id` en tant qu’`external_id` de Braze
- `form_response.answers[0].text` en tant qu’attribut personnalisé<br>![][7]
<br><br>
5. Cliquez sur **Soumettre pour approbation** et votre transformation sera envoyée à l’équipe de transformation des données de Braze pour être examinée. Après avoir reçu l’approbation, vous pouvez activer les webhooks à partir de votre plateforme externe.

## Cas d’utilisation

Imaginons qu’il existe une société de logiciels de création de formulaires et d’enquête en ligne. À l’aide d’une combinaison de webhooks et de transformation de données, vous pouvez diriger les webhooks directement vers Braze chaque fois qu’une enquête est soumise. Voici d’autres cas d’utilisation à envisager.

- Synchroniser l’événement d’un utilisateur qui répond à l’enquête en tant qu’événement personnalisé Braze. Cela vous permet d’identifier et de recibler les utilisateurs qui n’ont pas répondu à l’enquête.
- Synchroniser les réponses soumises dans une enquête en tant qu’attributs personnalisés. Les réponses d’un client sont des données first-party précieuses qui peuvent alimenter des expériences de communication personnalisées pour une utilisation future.

## Rédiger votre transformation

Le code que vous écrivez pour la transformation des données doit renvoyer un objet Hachage au format accepté par l’endpoint `/users/track`. 

Toute fonctionnalité prise en charge dans `/users/track` est prise en charge par la transformation des données, y compris les objets Attributs utilisateur, Événement et Achat. Les attributs imbriqués et les propriétés de l’événement sont également pris en charge. Les transformations ont accès à une variable de « charge utile ».

{% alert note %}
La transformation des données de Braze accepte actuellement le code dans le langage de programmation Ruby. Tout flux de contrôle Ruby standard, tel que la logique if/else, est pris en charge.
{% endalert %}

Voici un modèle par défaut qui inclut des attributs, des événements et des achats pour vous aider à démarrer :

```
return {
	"attributes": [ 
	{
		"external_id": payload["user_id"],
		"_update_existing_only" : true,
		"attribute_1": payload["attribute_1"]
	}
	],
	"events": [
	{
		"external_id": payload["user_id"],
		"_update_existing_only" : true,
		"name": payload["event_1"]",
		"time": Time.now,
		"properties": {
			"property_1": payload["event_1"]["property_1"]
		}
	}  
	],
	"purchases": [
	{
		"external_id": payload["user_id"],
		"_update_existing_only" : true,
		"product_id": payload["product_id"],
		"currency": payload["currency"],
		"price": payload["price"],
		"quantity": payload["quantity"],
		"time": payload["timestamp"],
		"properties": {
			"property_1": payload["purchase_1"]["property_1"]
		}
	}
  ]
}'
```

## Exemples supplémentaires

Considérez cet exemple de charge utile de la plateforme d’enquête Typeform, qui se déclenche chaque fois qu’une réponse à l’enquête est reçue.

![][3]

{% tabs local %}
{% tab Basic transformation %}

Ce cas d’utilisation simple prend certaines de ces réponses comme attributs et écrit un événement pour indiquer que l’enquête a été réalisée :

```
{
  "attributes": [ 
    {
      "external_id": payload["form_response"]["hidden"]["user_id"],
      "_update_existing_only": true,
      "home_city": payload["form_response"]["answers"][0]["text"],
      "home_weather_rating": payload["form_response"]["answers"][1]["number"],
    }
  ],
   "events": [ 
    {
      "external_id": payload["form_response"]["hidden"]["user_id"],
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": Time.now,
      "properties": {
        "form_id": payload["form_response"]["form_id"]
      }
    }
  ]
}
```
{% endtab %}
{% tab Intermediate transformation %}

Ce cas d’utilisation intermédiaire s’appuie sur le cas d’utilisation simple en introduisant une déclaration « if » sur l’une des réponses pour catégoriser l’utilisateur.

```
if
payload["form_response"]["answers"][1]["number"] < 7
NPS_category == "Detractor"
elsif
payload["form_response"]["answers"][1]["number"] == 7 
payload["form_response"]["answers"][1]["number"] == 8
NPS_category == "Passive"
elsif
payload["form_response"]["answers"][1]["number"] > 8
NPS_category == "Promoter"
end

{
  "attributes": [ 
    {
      "external_id": payload["form_response"]["hidden"]["user_id"],
      "_update_existing_only": true,
      "home_city": payload["form_response"]["answers"][0]["text"],
      "home_weather_NPS_category": NPS_category
    }
  ],
  "events": [
    {
      "external_id": payload["form_response"]["hidden"]["user_id"],
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": Time.now,
      "properties": {
        "form_id": payload["form_response"]["form_id"]
      }
    }
  ]
}
```
{% endtab %}
{% tab Advanced transformation %}

Ce cas d’utilisation avancé implique le scénario dans lequel la réponse à l’enquête pourrait provenir d’un utilisateur qui n’existe pas encore dans Braze. Pour résoudre ce problème, la fonction d’aide `get_user_by_email` est utilisée.

Si l’utilisateur existe, le profil existant est mis à jour. Si ce n’est pas le cas, un nouvel utilisateur avec uniquement un alias est créé.

```
user = get_user_by_email(payload["form_response"]["hidden"]["email_address"])
#get_user_by_email is a Braze function that takes an email_address to see if any Braze user profiles return.
#If a profile is returned, you have the entire user object to work with (see our /export/ids documentation).
#If multiple profiles with the same email exist, we will randomly return one user object for you to work with.


if user
braze_id = user["braze_id"]
{
  "attributes": [ 
    {
      "braze_id": braze_id,
      "home_city": payload["form_response"]["answers"][0]["text"],
      "home_weather_rating": payload["form_response"]["answers"][1]["number"]
    }
  ],
  "events": [
    {
      "braze_id": braze_id,
      "name": "weather_survey_completed",
      "time": Time.now,
      "properties": {
        "form_id": payload["form_response"]["form_id"]
      }
    }
  ]
}
else
{
  "attributes": [ 
    {
      "user_alias": { "alias_label": "email", "alias_name": payload["form_response"]["hidden"]["email_address"] },
      "_update_existing_only": false,
      "home_city": payload["form_response"]["answers"][0]["text"],
      "home_weather_rating": payload["form_response"]["answers"][1]["number"]
    }
  ],
  "events": [
    {
      "user_alias": { "alias_label": "email", "alias_name": payload["form_response"]["hidden"]["email_address"] },
      "_update_existing_only": false,
      "name": "weather_survey_completed",
      "time": Time.now,
      "properties": {
        "form_id": payload["form_response"]["form_id"]
      }
    }
  ]
}
End
```
{% endtab %}
{% endtabs %}

## À propos des fonctions d’aide

`get_user_by_email(email)` est une fonction d’aide que vous pouvez appeler dans votre code de transformation pour transformer une adresse e-mail en objet Profil d’utilisateur Braze. Cela peut être utile lorsqu’une plateforme externe envoie une adresse e-mail comme identifiant.

**Entrée :** `get_user_by_email(email)` fonctionne en acceptant une chaîne de caractères d’adresse e-mail comme saisie entre les parenthèses. Vous pouvez créer un modèle dans le champ d’e-mail du webhook entrant entre les parenthèses. Par exemple, ```get_user_by_email(payload["email_address"])```.

Si un profil Braze existe avec cette adresse e-mail, l’[objet Exportation utilisateur tout entier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/#sample-user-export-file-output) est renvoyé en tant que hachage. Tous les champs de l’objet Exportation utilisateur peuvent être utilisés. Si plusieurs profils existent avec le même e-mail, un seul objet Exportation utilisateur est renvoyé.

**Sortie :** Par exemple, si vous aviez ```user = get_user_by_email(payload["email_address"])``` et qu’un profil existe pour cette adresse e-mail, l’utilisateur contiendra l’objet Exportation utilisateur tout entier. Donc, `user["braze_id"]` renverra le `braze_id` de l’utilisateur correspondant. Si aucun profil n’existe avec cette adresse e-mail, l’utilisateur sera `nil`.

Vous pouvez également utiliser la logique if/else dans votre transformation pour effectuer une action si un utilisateur avec l’adresse e-mail existe, où

- ```User["braze_id"].present?```
- ```!user["braze_id"].nil?``` OU
- ```user["braze_id"] != nil)```

Et une autre action si aucun utilisateur n’existe avec cette adresse e-mail, où
- ```user["braze_id"].nil?``` ou 
- ```user["braze_id"] == nil)```

Consultez « Transformation avancée » dans [Exemples supplémentaires](#additional-examples) pour y trouver un exemple.

## Foire aux questions

#### Qu’est-ce qui est synchronisé avec la transformation des données ?

Toutes les données que la plateforme externe met à disposition dans un webhook peuvent être synchronisées avec Braze. Plus une plateforme externe envoie via webhooks, plus il existe d’options pour choisir ce qui est synchronisé.

#### Je suis marketeur. Ai-je besoin de ressources de développement pour utiliser la transformation des données ?

Bien que nous serions ravis que les développeurs utilisent également cette fonctionnalité, vous n’avez pas besoin d’en être un pour l’utiliser ! Nous avons vu des marketeurs mettre en place avec succès des transformations sans ressources de développement.

#### Puis-je toujours utiliser la transformation des données si ma plateforme externe ne donne que l’adresse e-mail d’un utilisateur dans ses webhooks sans ID utilisateur correspondant dans Braze ?

Oui. Dans votre transformation, vous pouvez utiliser la fonction `get_user_by_email` pour que Braze prenne une adresse e-mail et renvoie un profil d’utilisateur à mapper dessus. Consultez l’exemple de la transformation avancée.

#### Comment puis-je vérifier que la transformation de mes données est correcte ?

Partagez votre ébauche de code de transformation avec l’équipe de transformation des données de Braze à l’adresse [data-transformation@braze.com](mailto:data-transformation@braze.com). 


[1]: {% image_buster /assets/img_archive/data_transformation1.png %}
[2]: {% image_buster /assets/img/data_transformation/data_transformation1.jpg %}
[3]: {% image_buster /assets/img/data_transformation/data_transformation2.png %}
[5]: {% image_buster /assets/img/data_transformation/data_transformation4.png %}
[6]: {% image_buster /assets/img/data_transformation/data_transformation5.png %}
[7]: {% image_buster /assets/img/data_transformation/data_transformation6.jpg %}
[8]: {% image_buster /assets/img/data_transformation/data_transformation7.png %}
