---
nav_title: Objets imbriqués
article_title: Objets personnalisés imbriqués dans les événements personnalisés
page_order: 1
page_type: reference
description: "Cet article décrit comment envoyer des données JSON imbriquées en tant que propriétés d'événements personnalisés et d'achats, et comment utiliser ces objets imbriqués dans votre envoi de messages."
---

# Objets imbriqués dans les événements personnalisés

> Cette page explique comment envoyer des données JSON imbriquées en tant que propriétés d'événements personnalisés et d'achats, et comment utiliser ces objets imbriqués dans votre envoi de messages.

Vous pouvez utiliser des objets imbriqués - des objets qui se trouvent à l'intérieur d'un autre objet - pour envoyer des données JSON imbriquées en tant que propriétés d'événements personnalisés et d'achats. Ces données imbriquées peuvent être utilisées pour modéliser des informations personnalisées dans les messages, déclencher l'envoi de messages et segmenter les utilisateurs.

## Limites

- Les données imbriquées sont prises en charge pour les [événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) et les [événements d'achat]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/), mais pas pour les autres types d'événements.
- Les objets de propriété d'événement qui contiennent des valeurs de tableau ou d'objet peuvent avoir une charge utile de propriété d'événement allant jusqu'à 100 Ko.
- Les schémas de propriétés d'événement ne peuvent pas être générés pour les propriétés d'achat.
- Les schémas de propriétés d'événements sont générés par l'échantillonnage des événements personnalisés des dernières 24 heures.

### Versions minimales du SDK

Les versions suivantes du SDK prennent en charge les objets imbriqués :

{% sdk_min_versions swift:5.0.0 android:1.0.0 web:3.3.0 %}

## Étape 1 : Générer un schéma

Vous pouvez accéder aux données imbriquées dans votre événement personnalisé en générant un schéma pour chaque événement avec des propriétés d'événement imbriqué. Pour générer un schéma :

1. Allez dans **Paramètres des données** > Événements personnalisés.
2. Sélectionnez **Gérer les propriétés** pour les événements comportant des propriétés imbriquées.
3. Sélectionnez le bouton <i class="fas fa-arrows-rotate"></i> pour générer le schéma. Pour visualiser le schéma, sélectionnez le bouton <i class="fas fa-plus"></i> plus.

\![]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

Si de nouvelles propriétés sont envoyées à l'avenir, elles ne figureront pas dans le schéma tant qu'il n'aura pas été régénéré. Les schémas peuvent être régénérés toutes les 24 heures.

## Étape 2 : Utiliser l'objet imbriqué

Vous pouvez faire référence aux données imbriquées lors de la segmentation et de la personnalisation. Notez qu'un schéma n'est pas nécessaire. Vous trouverez des exemples d'utilisation dans les sections suivantes :

- [Corps de la requête API](#api-request-body)
- [Modèle liquide](#liquid-templating)
- [Envoi déclenché de messages](#message-triggering)
- [Segmentation](#segmentation)
- [Personnalisation](#personalization)

### Corps de la requête API

{% tabs %}
{% tab Music Example %}

Voici un exemple de `/users/track` avec un événement personnalisé "Liste de lecture créée". Après la création d'une liste de lecture, capturez les propriétés de la liste de lecture en l'envoyant :
- Une demande d'API qui répertorie "songs" comme propriété
- Un tableau des propriétés imbriquées des chansons

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
{% tab Restaurant Example%}

Voici un exemple de `/users/track` avec un événement personnalisé "Ordered". Une fois qu'une commande a été complétée, saisissez les propriétés de cette commande en l'envoyant :
- Une requête API qui liste "r_details" comme propriété
- Les propriétés imbriquées de cet ordre

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

{% alert note %}
Pour les propriétés d'événement personnalisé imbriquées, si l'année est inférieure à 0 ou supérieure à 3000, Braze ne stocke pas ces valeurs sur l'utilisateur.
{% endalert %}

### Modèle liquide

L'exemple suivant montre comment créer un modèle Liquid qui fait référence aux propriétés imbriquées demandées dans la [requête API précédente.](#api-request-body)

{% tabs %}
{% tab Music Example %}
Templating in Liquid dans un message déclenché par l'événement "Liste de lecture créée" :

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "Nevermind"<br>
`{{event_properties.${songs}[1].title}}`: "While My Guitar Gently Weeps" (Ma guitare pleure doucement)
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
Templating in Liquid dans un message déclenché par l'événement "Ordered" :

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "Montclair
{% endraw %}

{% endtab %}
{% endtabs %}

### Envoi déclenché de messages

Pour utiliser ces propriétés afin de déclencher une campagne, sélectionnez votre événement personnalisé ou votre achat, puis ajoutez un filtre de **propriétés imbriquées**. Notez que le déclenchement des messages n'est pas encore pris en charge pour les messages in-app, mais les propriétés imbriquées dans la personnalisation Liquid dans les messages s'afficheront toujours.

{% tabs %}
{% tab Music Example %}

Déclenchement d'une campagne avec propriétés imbriquées à partir de l'événement "Liste de lecture créée" :

\![Un utilisateur choisissant une propriété imbriquée pour les filtres de propriétés sur un événement personnalisé.]({% image_buster /assets/img/nested_object2.png %})

La condition de déclenchement `songs[].album.yearReleased` "is" "1968" correspondra à un événement dans lequel l'une des chansons a un album sorti en 1968. Nous utilisons la notation entre crochets `[]` pour parcourir les tableaux, et nous vérifions si **un** élément du tableau parcouru correspond à la propriété de l'événement.

{% alert important %}
Le filtre " **does not equal"** ne s'applique que si aucune des propriétés de votre tableau n'est égale à la valeur fournie. <br><br>Par exemple, disons que le Canvas A a pour filtre de propriété imbriquée d **'** événement personnalisé basé sur l'action "smartwatch", et que le Canvas B a pour filtre de propriété imbriquée d'événement personnalisé basé sur l'action "simphone **".**  Si vous avez "smartwatch" et "simphone" dans vos propriétés, les deux canevas se déclencheront. Mais si vous avez "simphone" ou "sim only" dans une propriété, aucun des deux Canvas ne se déclenchera.
{% endalert %}

{% endtab %}
{% tab Restaurant Example %}

Déclenchement d'une campagne avec des propriétés imbriquées à partir de l'événement "Ordered" :

\![Un utilisateur ajoutant le filtre de propriété r_details.name est McDonalds pour un événement personnalisé.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "Mcdonalds"<br>
`r_details.location.city`: "Montclair
{% endtab %}
{% endtabs %}

{% alert note %}
Si votre propriété d'événement contient les caractères `[]` ou `.`, échappez-les en mettant le bloc entre guillemets. Par exemple, `"songs[].album".yearReleased` correspondra à un événement dont la propriété littérale est `"songs[].album"`.
{% endalert %}

### Segmentation

Pour segmenter les utilisateurs en fonction des propriétés d'événements imbriqués, vous devez utiliser les [extensions de segments.]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) Après avoir généré un schéma, l'explorateur d'objets imbriqués s'affiche dans la section segmentation. 

\![]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

La segmentation utilise la même notation que le déclenchement (voir [Déclenchement des messages](#message-triggering)).

Pour modifier ou créer des extensions de segments, vous devez disposer de l'autorisation "Modifier les segments".

### Personnalisation

Dans la fenêtre modale/boîte de dialogue **Ajouter une personnalisation**, sélectionnez **Propriétés d'événement avancées** comme type de personnalisation. Cela permet d'ajouter des propriétés d'événement imbriquées après la génération d'un schéma.

\![]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## Questions fréquemment posées

### L'utilisation d'objets imbriqués permet-elle d'enregistrer des points de données supplémentaires ?

L'ajout de cette fonctionnalité ne modifie en rien la manière dont nous enregistrons les points de données. La segmentation basée sur des objets imbriqués utilise les extensions de segments, qui n'utilisent pas de points de données supplémentaires.

### Combien de données imbriquées peuvent être envoyées ?

Si une ou plusieurs propriétés de l'événement contiennent des données imbriquées, la charge utile maximale pour toutes les propriétés combinées d'un événement est de 100 Ko. Toute demande dépassant cette limite sera rejetée.

