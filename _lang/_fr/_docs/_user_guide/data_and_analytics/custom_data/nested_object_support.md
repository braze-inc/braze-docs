---
nav_title: Objets imbriqués
article_title: Objets imbriqués pour les propriétés d'événement personnalisé
page_order: 4
alias: /imbriqué_object_support/
page_type: Référence
description: "Cet article de référence décrit les objets imbriqués pour les propriétés d'événement personnalisées, et inclut des cas d'utilisation d'exemple, des limitations et des questions fréquemment posées."
---

# Objets imbriqués pour les propriétés d'événement personnalisées

Vous pouvez utiliser des objets imbriqués - des objets qui sont à l'intérieur d'un autre objet - pour envoyer des données JSON imbriquées comme propriétés d'événements personnalisés et d'achats. Ces données imbriquées peuvent être utilisées pour modéliser des informations personnalisées dans les messages, pour déclencher les envois de messages et pour la segmentation.

{% alert important %}
Cette fonctionnalité est généralement disponible, mais le déclenchement des messages et la segmentation des utilisateurs sur la base de ces données sont en accès anticipé. Pour plus d'informations, veuillez contacter votre responsable de compte Braze.
{% endalert %}

## Limitation

- Les données imbriquées ne peuvent être envoyées qu'avec [les événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) et [les événements d'achat]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/). Ceci n'est pas encore pris en charge avec les attributs de l'utilisateur.
- Les objets de propriété événement qui contiennent des valeurs de tableau ou d'objet peuvent avoir une charge utile de propriété événement allant jusqu'à 50 Ko.
- Les versions suivantes du SDK prennent en charge les objets imbriqués :

{% sdk_min_versions web:3.3.0 ios:4.3.1 android:1.0.0 %}

## Exemples d'utilisation

### Corps de la requête API

{% tabs %}
{% tab Music Example %}

Montré ci-dessous est un exemple de `/users/track` avec un événement personnalisé "Created Playlist" . Une fois qu'une playlist a été créée, pour capturer les propriétés de la playlist, nous enverrons une requête API qui répertorie "songs" comme propriété et un tableau des propriétés imbriquées des morceaux.

```
...
"properties": {
  "songs": [
    {
      "title": "Fait comme un esprit adolescent",
      "artiste": "Nirvana",
      "album": {
        "name": "Jamais",
        "yearReleased": "1991"
      }
    },
    {
      "title": "Alors que ma guitare pleuve doucement",
      "artiste": "les Beatles",
      "album": {
        "name": "Les Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab Restaurant Example%}

Montré ci-dessous est un exemple de `/users/track` avec un événement personnalisé "Ordéré". Une fois qu'une commande est terminée, pour capturer les propriétés de cet ordre, nous enverrons une requête API qui liste "r_details" en tant que propriété, et les propriétés imbriquées de cet ordre.

```
...
"properties": {
  "r_details": {
    "name": "McDonalds",
    "identifiant": "12345678",
    "localisation" ; {
      "city": "Montclair",
      "state": "NJ"
    }
  }

...
```
{% endtab %}
{% endtabs %}

### Modèle de liquide

Les exemples de modèles Liquid ci-dessous montrent comment référencer les propriétés imbriquées enregistrées à partir de la requête de l'API ci-dessus et les utiliser dans votre message Liquid. En utilisant la notation Liquid et point, traversez les données imbriquées pour trouver le nœud spécifique que vous souhaitez inclure dans vos messages.

{% tabs local %}
{% tab Music Example %}
Templating in Liquid in a message triggered by the "Created Playlist" event:

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "Nevermind"<br> `{{event_properties.${songs}[1].title}}`: "While My Guitar Gently Weeps"
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
Templating in Liquid dans un message déclenché par l'événement "Ordéré" :

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### Déclenchement du message

Pour utiliser ces propriétés pour déclencher une campagne, sélectionnez votre événement personnalisé ou votre achat, et ajoutez un filtre __Propriété imbriquée__. Notez que le déclenchement de messages n'est pas encore pris en charge pour les messages dans l'application.

{% alert important %}
Les objets imbriqués sont généralement disponibles, cependant les messages déclenchants et la segmentation des utilisateurs basés sur ces données sont en accès anticipé. Pour plus d'informations, veuillez contacter votre responsable de compte Braze.
{% endalert %}

{% tabs %}
{% tab Music Example %}

Déclenchement d'une campagne avec des propriétés imbriquées à partir de l'événement "Liste de lecture créée":

![Déclenchement de la campagne]({% image_buster /assets/img/nested_object2.png %})

La condition de déclenchement `songs[].album.yearReleased` "est" "1968" correspond à un événement où l'une des chansons a un album sorti en 1968. Nous utilisons la notation des accolades `[]` pour parcourir les tableaux, et faire correspondre si __un élément__ dans le tableau parcouru correspond à la propriété de l'événement.<br>
{% endtab %}
{% tab Restaurant Example %}

Déclenchement d'une campagne avec des propriétés imbriquées à partir de l'événement "Commandé" :

![Déclenchement de la campagne]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "Mcdonalds"<br> `r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %} Si votre propriété événement contient les `[]` ou `.` caractères, échappez-les en enveloppant le chunk en guillemets doubles. Par exemple, `"songs[].album".yearReleased` fera correspondre un événement à la propriété littérale `"songs[].album"`.  {% endalert %}

### Segmentation

Utilisez [extensions de segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) pour segmenter les utilisateurs en fonction des propriétés d'événement imbriquées. La segmentation utilise la même notation que le déclenchement (décrit ci-dessus).

## Foire aux questions

### Cela consomme-t-il des points de données supplémentaires ?

Il n'y a aucun changement dans la façon dont nous facturons les points de données en raison de l'ajout de cette capacité.

### Combien de données imbriquées peuvent être envoyées ?

Si une ou plusieurs propriétés de l'événement contiennent des données imbriquées, la charge utile maximale pour toutes les propriétés combinées d'un événement est de 50 KB. Toute demande dépassant cette limite de taille sera rejetée.
[1]: {% image_buster /assets/img/nested_object1.png %} [2]: {% image_buster /assets/img/nested_object2.png %}

