# Cas d’utilisation : Système d'e-mail de rappel de réservation

> Braze est une plateforme complète d'engagement client conçue pour être hautement programmable. Dans ce cas d'utilisation, nous démontrons quelques façons dont Braze offre des fonctionnalités que vous pouvez intégrer dans des cas d'utilisation qui se situent à l'intersection du produit et du marketeur, tels que les systèmes de réservation.

Ce cas d'utilisation montre comment vous pouvez utiliser les fonctionnalités de Braze pour créer un service d'envoi de messages e-mail de rappel de réservation. Le service permettra aux utilisateurs de prendre des rendez-vous et leur enverra des messages pour leur rappeler leurs rendez-vous à venir. Bien que ce cas d'utilisation utilise des messages e-mail, vous pouvez envoyer des messages dans n'importe quel canal, ou dans plusieurs, sur la base d'une seule mise à jour d'un profil utilisateur.

La création de ce service présente d'autres avantages :
- Les messages envoyés feront l'objet d'un suivi et d'un rapport complets.
- Le contenu des messages peut être mis à jour par des utilisateurs non techniques de Braze.
- Les messages obéissent aux statuts "opt-in" et "opt-out" sur les profils utilisateurs par configuration de la campagne.
- Les données de réservation et les données d'interaction avec les messages peuvent être utilisées pour segmenter et cibler les utilisateurs en vue d'un envoi de messages supplémentaires. Par exemple, vous pouvez recibler les personnes qui n'ont pas ouvert le message de rappel initial en leur envoyant un rappel supplémentaire avant leur rendez-vous.

Suivez les étapes suivantes pour réaliser ce cas d'utilisation :
1. [Inscrire les données relatives aux réservations à venir dans un profil utilisateur Braze](#step-1)
2. [Configurer et lancer un message de rappel de réservation](#step-2)
3. [Traiter les réservations et les annulations mises à jour](#step-3)

## Étape 1 : Inscrire les données relatives aux réservations à venir dans un profil utilisateur Braze {#step-1}

Utilisez le point de terminaison Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour écrire un [attribut personnalisé imbriqué]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/) dans le profil d'un utilisateur à chaque fois qu'une réservation est effectuée. Assurez-vous que l'attribut personnalisé imbriqué contient toutes les informations nécessaires à l'envoi et à la personnalisation du message de rappel. Dans ce cas d'utilisation, nous nommerons l'attribut personnalisé imbriqué "voyages".

### Ajouter une réservation

Lorsqu'un utilisateur crée une réservation, utilisez la structure suivante pour le tableau d'objets afin d'envoyer les données à Braze via l'endpoint `/users/track`.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": [
               {"trip_id":"1","name":"London Trip","start_date"{$time:"2025-11-11"}},
               {"trip_id":"2","name":"Sydney Trip","start_date"{$time:"2025-11-11"}}
           ]
       }
   ]
}
```
{% endraw %}

L'attribut personnalisé imbriqué "voyages" s'affichera dans le profil utilisateur de la manière suivante.

![Deux attributs personnalisés imbriqués pour un voyage à Londres et un voyage à Sydney.][1]{: style="max-width:70%;"}

### Mise à jour des réservations
Lorsqu'un utilisateur met à jour une réservation, utilisez la structure suivante pour le tableau d'objets afin d'envoyer les données à Braze via l'endpoint `/users/track`.

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$update:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value":"1",
                       "$new_object":{"trip_id":"1","name":"London Trip","start_date":{"$time":"2025-11-11"}}
                   }
               ]
           }
       }
 ]
}
```
{% endraw %}

### Supprimer la réservation

{% tabs %}
{% tab /users/track endpoint %}
#### Envoyer des données via l'endpoint `/users/track` 
Lorsqu'un utilisateur supprime une réservation, utilisez la structure suivante pour le tableau d'objets afin d'envoyer les données à Braze via l'endpoint `/users/track`.

{% raw %}
```json

{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$remove:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value": "1"
                   }
               ]
           }
       }
   ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}
#### Inscrire des attributs imbriqués dans les profils utilisateurs via le SDK

Si vous collectez des prises de rendez-vous avec votre appli, votre site web ou les deux et que vous souhaitez écrire ces données directement dans un profil utilisateur, vous pouvez utiliser le SDK de Braze pour transmettre ces données. Voici un exemple utilisant le SDK Web :

{% raw %}
```json
const json = [{
  "id": 1,
  "name": "London Trip",
  "start_date": {"$time”: “2025-05-08”}
}, {
  "id": 1,
  "name": "Sydney Trip",
  "start_date": {"$time”: “2025-11-11”}
}];
braze.getUser().setCustomUserAttribute("trips", json);
```
{% endraw %}
{% endtab %}
{% endtabs %}

La réservation spécifiée sera supprimée de l'attribut personnalisé imbriqué dans le profil utilisateur et affichera toutes les réservations restantes.

![Un attribut personnalisé imbriqué pour un voyage à Londres.]({% image_buster /assets/img/use_cases/1_nested_attribute.png %}){: style="max-width:70%;"}

## Étape 2 : Configurer et lancer un message de rappel de réservation {#step-2}

### Étape 2a : Créer une audience ciblée
Créez une audience cible pour recevoir des rappels à l'aide d'une segmentation multicritères. Par exemple, si vous souhaitez envoyer un rappel deux jours avant la date de réservation, sélectionnez les éléments suivants :

- Une date de début **dans plus d'un jour** et
- Une date de début **dans moins de 2 jours** 

![Un attribut personnalisé imbriqué "voyages" avec des critères pour une date de début supérieure à un jour et inférieure à deux jours.][3]

### Étape 2b : Créez votre message

Créez le message de rappel par e-mail en suivant les étapes de la section [Création d'un e-mail avec HTML personnalisé]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/). Utilisez Liquid pour personnaliser le message avec les données de l'attribut personnalisé du client que vous avez créé ("voyages"), comme dans cet exemple.

{% raw %}
```liquid
{% assign dates = {{custom_attribute.${trips}}} %}
{% assign today = "now" | date: "%s" %}
{% assign two_days = today | plus: 172800 | date: "%F" %}
You have the following booked in 2 days! Check the information below:
{% for date in dates %}
{% if date.start_date == two_days %}
{{date.trip_id}} 
{{date.name}}
{% endif %}
{% endfor %}
```
{% endraw %}

### Étape 2c : Lancez votre campagne

Lancez la campagne pour l'envoi du message e-mail de rappel. Désormais, chaque fois que Braze recevra l'attribut personnalisé "voyages", un message sera planifié en fonction des données incluses dans l'objet de la réservation concernée.

## Étape 3 : Traiter les mises à jour des réservations et les annulations {#step-3}

Maintenant que vous envoyez des messages de rappel, vous pouvez configurer des messages de confirmation à envoyer lorsque les réservations sont mises à jour ou annulées.

### Étape 3a : Envoyer les données mises à jour

{% tabs %}
{% tab /users/track %}

#### Envoyer des données via l'endpoint `/users/track` 
Utilisez le point de terminaison Braze [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour envoyer un événement personnalisé lorsqu'un utilisateur met à jour ou annule une réservation. Dans ce cas, mettez les données nécessaires dans les propriétés d'événement qui confirmeront le changement. 

Supposons que dans ce cas d'utilisation, un utilisateur ait mis à jour la date de son voyage à Sydney. L'événement se présenterait comme suit :

{% raw %}
```json
{
  "events": [
    {
      "external_id": "user_id",
      "name": "trip_updated",
      "time": "2025-03-07T08:19:23+01:00",
      "properties": {
        "id": 2,
        "name": "Sydney Trip",
        "old_time": "2025-11-12"
        "new_time": "2026-01-21"
      }
    }
  ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}

#### Inscrire des attributs imbriqués dans les profils utilisateurs via le SDK

Envoyez des événements personnalisés au profil utilisateur via le SDK. Par exemple, si vous utilisez le SDK web, vous pouvez envoyer :

{% raw %}
```json
braze.logCustomEvent("trip_updated", { 
  id: 2,
  name: "Sydney Trip",
  old_time: "2025-11-12",
  new_time: "2026-01-21"
});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Étape 3b : Créer un message pour confirmer la mise à jour

Créez une [campagne basée sur des actions]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) pour envoyer à l'utilisateur une confirmation de sa réservation mise à jour. Vous pouvez [utiliser Liquid pour créer des propriétés d'événement]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) qui reflètent le nom, l'ancienne heure et la nouvelle heure de la réservation (ou seulement le nom s'il s'agit d'une annulation) dans le message lui-même.

Par exemple, vous pouvez rédiger le message suivant :

{% raw %}
```liquid
Hi {{${first_name}}}, you have successfully updated the date of your trip, {{event_properties.${name}}}, from {{event_properties.${old_time}}} to {{event_properties.${new_time}}}
```
{% endraw %}

### Étape 3c : Modifier le profil utilisateur pour refléter la mise à jour

Enfin, pour envoyer les rappels de réservation des étapes 1 et 2 sur la base des données les plus récentes, mettez à jour les attributs personnalisés imbriqués afin de refléter la modification ou l'annulation de la réservation.

#### Mise à jour des réservations

Si l'utilisateur de ce cas d'utilisation mettait à jour son voyage à Sydney, vous utiliseriez l'endpoint `/users/track` pour modifier la date avec un appel comme celui-ci :

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "trips": {
	  "$update": [
	    {
            "$identifier_key": "id",
            "$identifier_value": 2,
            "$new_object": {
              "start_date": "2026-01-21"
            }
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

#### Réservation annulée

Si l'utilisateur de ce cas d'utilisation annule son voyage Syndey, vous enverrez l'appel suivant à l'endpoint `/users/track`:

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "trips": {
	  "$remove": [
	   {
            "$identifier_key": "id",
            "$identifier_value": 2
          }
         ]
      }
    }
  ]
}
```
{% endraw %}

Après l'envoi de ces appels et la mise à jour du profil utilisateur, les messages de rappel de réservation refléteront les données les plus récentes concernant les dates de réservation de l'utilisateur.

[1]: {% image_buster /assets/img/use_cases/2_nested_attributes.png %}
[3]: {% image_buster /assets/img/use_cases/custom_nested_attribute.png %}