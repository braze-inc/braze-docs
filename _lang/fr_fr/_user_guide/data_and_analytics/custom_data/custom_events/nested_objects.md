---
nav_title: Objets imbriqués
article_title: Objets personnalisés imbriqués dans les événements personnalisés
page_order: 1
page_type: reference
description: "Cet article décrit comment envoyer des données JSON imbriquées en tant que propriétés d'événements personnalisés et d'achats, et comment utiliser ces objets imbriqués dans votre envoi de messages."
---

# Objets imbriqués dans les événements personnalisés

> Cet article décrit comment envoyer des données JSON imbriquées en tant que propriétés d'événements personnalisés et d'achats, et comment utiliser ces objets imbriqués dans votre envoi de messages.

Vous pouvez utiliser des objets imbriqués (c.-à-d. des objets qui se trouvent à l’intérieur d’un autre objet) pour envoyer des données JSON imbriquées en tant que propriétés d’événements personnalisés et d’achats. Ces données imbriquées peuvent être utilisées pour définir des informations personnalisées dans les messages, pou déclencher des envois de message et pour la segmentation.

## Limitations

- Les données imbriquées sont prises en charge pour les [événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) et les [événements d'achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/), mais pas pour les autres types d'événements.
- Les objets de propriété d'événement qui contiennent des valeurs de tableau ou d'objet peuvent avoir une charge utile de propriété d'événement allant jusqu'à 100 Ko.
- Les schémas de propriétés d'événement ne peuvent pas être générés pour les propriétés d'achat.
- Les schémas de propriétés d'événements sont générés par l'échantillonnage des événements personnalisés des dernières 24 heures.

### Versions minimales du SDK

Les versions SDK suivantes prennent en charge les objets imbriqués :

{% sdk_min_versions swift:5.0.0 android:1.0.0 web:3.3.0 %}

## Étape 1 : Générez un schéma

Pour accéder aux données imbriquées dans votre événement personnalisé, générez un schéma pour chaque événement avec des propriétés d'événement imbriqué. Pour générer un schéma, procédez comme suit :

1. Sélectionnez **Paramètres des données** > **Événements personnalisés**.
2. Sélectionnez **Gérer les propriétés** pour les événements comportant des propriétés imbriquées.
3. Sélectionnez le bouton <i class="fas fa-arrows-rotate"></i> pour générer le schéma. Pour visualiser le schéma, sélectionnez le bouton <i class="fas fa-plus"></i> plus.

![][6]{: style="max-width:80%;"}

## Étape 2 : Utiliser l'objet imbriqué

Après avoir généré un schéma, vous pouvez référencer les données imbriquées lors de la segmentation et de la personnalisation. Vous trouverez des exemples d'utilisation dans les sections suivantes :

- [Corps de la requête API](#api-request-body)
- [Modèles Liquid](#liquid-templating)
- [Déclenchement du message](#message-triggering)
- [Segmentation](#segmentation)
- [Personnalisation](#personalization)

### Corps de la requête API

{% tabs %}
{% tab Exemple de musique %}

Voici un exemple d’événement personnalisé `/users/track` « Liste de lecture créée ». Après la création d'une liste de lecture, pour capturer les propriétés de la liste de lecture, nous enverrons une requête API qui répertorie "chansons" comme propriété, et un tableau des propriétés imbriquées des chansons.

```
...
"properties": {
  "songs": [
    {
      "title": "Smells Like Teen Spirit",
      "artist": "Nirvana",
      "album": {
        "name": "Nevermind",
        "yearReleased": "1991"
      }
    },
    {
      "title": "While My Guitar Gently Weeps",
      "artist": "the Beatles",
      "album": {
        "name": "The Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab Exemple de restaurant%}

Voici un exemple d’événement personnalisé `/users/track` « Commandé ». Une fois la commande terminée, pour capturer les propriétés de cette commande, nous enverrons une requête API qui répertorie "r_details" en tant que propriété, ainsi que les propriétés imbriquées de cette commande.

```
...
"properties": {
  "r_details": {
    "name": "McDonalds",
    "identifier": "12345678",
    "location" : {
      "city": "Montclair",
      "state": "NJ"
    }
  }
}
...
```
{% endtab %}
{% endtabs %}

### Modèles Liquid

Les exemples de templating Liquid suivants montrent comment référencer les propriétés imbriquées de la requête API précédente pour les utiliser dans vos communications Liquid. À l’aide de Liquid et de la notation par points, parcourez les données imbriquées pour trouver le nœud spécifique que vous souhaitez inclure dans vos messages.

{% tabs %}
{% tab Exemple de musique %}
Modèle Liquid dans un message déclenché par l’événement « Liste de lecture créée » :

{% raw %}
`{{event_properties.${songs}[0].album.name}}` : « Nevermind »<br>
`{{event_properties.${songs}[1].title}}` : "While My Guitar Gently Weeps" (Ma guitare pleure doucement)
{% endraw %}

{% endtab %}
{% tab Exemple de restaurant %}
Modèle Liquid dans un message déclenché par l’événement  « Commandé » :

{% raw %}
`{{event_properties.${r_details}.location.city}}` : "Montclair
{% endraw %}

{% endtab %}
{% endtabs %}

### Déclenchement du message

Pour utiliser ces propriétés afin de déclencher une campagne, sélectionnez votre événement personnalisé ou votre achat, puis ajoutez un filtre de **propriétés imbriquées**. Notez que le déclenchement des messages n'est pas encore pris en charge pour les messages in-app, mais les propriétés imbriquées dans la personnalisation Liquid dans les messages s'afficheront toujours.

{% tabs %}
{% tab Exemple de musique %}

Déclenchement d’une campagne avec des propriétés imbriquées à partir de l’événement « Liste de lecture créée » :

![Un utilisateur choisit une propriété imbriquée pour les filtres de propriété sur un événement personnalisé.]({% image_buster /assets/img/nested_object2.png %})

L’état de déclenchement `songs[].album.yearReleased` « is » (est) « 1968 » correspond à un événement où l’une des chansons est dans un album publié en 1968. Nous utilisons la notation entre crochets `[]` pour parcourir les tableaux, et nous vérifions si **un** élément du tableau parcouru correspond à la propriété de l'événement.<br>
{% endtab %}
{% tab Exemple de restaurant %}

Déclenchement d’une campagne avec des propriétés imbriquées à partir de l’événement « Commandé » :

![Un utilisateur ajoutant le filtre de propriété r_details.name est McDonalds pour un événement personnalisé.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name` : "Mcdonalds"<br>
`r_details.location.city` : "Montclair
{% endtab %}
{% endtabs %}

{% alert note %}
Si votre propriété d’événement contient les caractères `[]` or `.`, faites un échappement HTML en les entourant de guillemets doubles. Par exemple, `"songs[].album".yearReleased` correspondra à un événement avec la propriété littérale `"songs[].album"`.
{% endalert %}

### Segmentation

Pour segmenter les utilisateurs en fonction des propriétés d'événements imbriqués, vous devez utiliser les [extensions de segments.]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) Une fois que vous avez généré un schéma, l’explorateur d’objets imbriqués s’affiche dans la section Segmentation. 

![][4]

La segmentation utilise la même notation que le déclenchement (voir [Déclenchement des messages](#message-triggering)).

### Personnalisation

Dans la fenêtre modale/boîte de dialogue **Ajouter une personnalisation**, sélectionnez **Propriétés d'événement avancées** comme type de personnalisation. Ceci permet d'ajouter des propriétés d'événements imbriqués après la génération d'un schéma.

![][5]{: style="max-width:70%;"}

## Foire aux questions

### L'utilisation d'objets imbriqués consomme-t-elle des points de données supplémentaires ?

Il n’y a pas de changement dans la façon dont nous facturons les points de données suite à l’ajout de cette capacité. La segmentation basée sur des objets imbriqués utilise les extensions de segments, ce qui n'entraîne pas l'utilisation de points de données supplémentaires.

### Combien de données imbriquées peuvent être envoyées ?

Si une ou plusieurs propriétés de l'événement contiennent des données imbriquées, la charge utile maximale pour toutes les propriétés combinées d'un événement est de 100 Ko. Toute requête dépassant cette limite de taille sera rejetée.

[4]: {% image_buster /assets/img_archive/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/img_archive/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/img_archive/schema_generation_example.png %}