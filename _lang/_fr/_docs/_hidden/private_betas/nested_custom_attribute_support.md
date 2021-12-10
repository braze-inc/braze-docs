---
nav_title: Attributs personnalisés imbriqués
permalink: "/index_custom_attribute_support/"
hidden: vrai
---

# Attributs personnalisés imbriqués

Vous pouvez utiliser des attributs personnalisés imbriqués pour envoyer des objets comme un nouveau type de données pour les attributs personnalisés. Ces données imbriquées vous permettent de créer des segments en utilisant des informations à partir d'un objet d'attribut personnalisé, et personnalisez vos messages en utilisant un objet d'attribut personnalisé et Liquid.

Les objets peuvent contenir des [types de données existants][1], tels que:

- Numéros
- Chaînes de caractères
- Booléens
- Tableaux
- Autres objets
- [Tableaux d'objets]({{site.baseurl}}/array_of_objects/)

{% alert important %}
La prise en charge des attributs personnalisés imbriqués est actuellement en accès anticipé. Veuillez contacter votre responsable de compte Braze si vous êtes intéressé à participer à l'accès anticipé.
{% endalert %}

## Limitation

- Disponible sur les attributs personnalisés envoyés via l'API uniquement, les SDK Braze ne sont pas encore pris en charge.
- Les partenaires ne supportent pas encore les attributs personnalisés imbriqués. Tant que cette fonctionnalité n'est pas prise en charge, nous vous recommandons de ne pas utiliser cette fonctionnalité avec des groupes d'applications qui ont des intégrations de partenaires activées.
- Les dates ne sont pas prises en charge dans les objets.
- Les objets ont une taille maximale de 50 Ko.
- Les noms de clés et les chaînes de caractères ont une limite de 255 caractères.

## Exemples d'utilisation

### Corps de la requête API

{% tabs local %}
{% tab Create %}
Montré ci-dessous est un exemple de `/users/track` avec un objet « Chanson la plus jouée ». Pour capturer les propriétés de la chanson, nous enverrons une requête API listant `most_played_song` comme objet, avec un ensemble de propriétés d'objet.

```
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
          "song_name": "Solea",
          "artist_name": "Miles Davis",
          "album_name": "Croquis d'Espagne",
          "genre": "Jazz",
          "play_analytics": {
              "count": 1000,
              "top_10_listeners": vrai
          }
      }
    }
  ]
}
```

{% endtab %}
{% tab Update %}
Pour mettre à jour un objet existant, envoyez un POST à `utilisateurs/piste` avec le paramètre `_merge_objects` dans la requête. Cela fusionnera profondément votre mise à jour avec les données de l'objet existant. La fusion profonde assure que tous les niveaux d'un objet sont fusionnés dans un autre objet au lieu du premier niveau. Dans cet exemple, nous avons déjà un objet `most_played_song` au Brésil, et maintenant nous ajoutons un nouveau champ, `year_released`, à l'objet `most_played_song`.

```
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objets": vrai,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

Après réception de la requête ci-dessus, l'objet d'attribut personnalisé ressemblera maintenant à ceci :

```
"most_played_song": {
    "song_name": "Solea",
    "artist_name" : "Miles Davis",
    "album_name": "Esquisses d'Espagne",
    "year_released": 1960,
    "genre": "Jazz",
    "play_analytics": {
        "count": 1000,
        "top_10_listeners": vrai
}
```

{% alert warning %}
Vous devez définir `_merge_objects` à true, sinon vos objets seront écrasés. `_merge_objects` est faux par défaut.
{% endalert %}

{% endtab %}
{% tab Delete %}
Pour supprimer un objet attribut personnalisé, envoyez un POST à `utilisateurs/trace` avec l'objet attribut personnalisé défini à `null`.

```
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": null
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### Templating Liquide

L'exemple de modèle Liquid ci-dessous montre comment référencer les propriétés de l'objet d'attribut personnalisé enregistrées à partir de la requête de l'API ci-dessus et les utiliser dans votre messagerie.

Utilisez la balise de personnalisation `custom_attribute` et la notation par point pour accéder aux propriétés d'un objet. Spécifiez le nom de l'objet, suivi d'un point (points), suivi du nom de la propriété.

{% raw %}
`{{custom_attribute.${most_played_song}.artist_name}}` — "Miles Davis" <br> `{{custom_attribute.${most_played_song}. ong_name}}` — "Solea" <br> `{{custom_attribute.${most_played_song}.play_analytics.count}}` — "50"
{% endraw %}

!\[Exemple de notification pour la dernière fois jouée\]\[5\]

### Segmentation

Vous pouvez construire des Segments en fonction d'attributs personnalisés imbriqués pour cibler davantage vos utilisateurs. Pour ce faire, filtrez votre Segment en fonction de l'objet attribut personnalisé, puis spécifiez le nom de la propriété et la valeur associée sur laquelle vous voulez segmenter.

!\[Dernier segment de musique\]\[6\]

Lorsque vous travaillez avec la segmentation d'attributs personnalisés imbriqués, vous aurez accès à un nouveau comparateur regroupé par type de données. Par exemple, puisque `play_analytics.count` est un nombre, vous pouvez sélectionner un comparateur dans la catégorie **Nombre**.

![Comparateur de segment NCA[7]

## Points de données

Toute clé mise à jour consomme un point de données. Par exemple, cet objet initialisé dans le profil de l'utilisateur compte comme sept (7) points de données :

```
{
  "attributes": [
    {
      "external_id": "user_id",
       "most_played_song": {
          "song_name": "Solea",
          "artist_name": "Miles Davis",
          "album_name": "Croquis d'Espagne",
          "year_released": 1960,
          "genre": "Jazz",
          "play_analytics": {
              "count": 1000,
              "top_10_listeners": vrai
      }
    }
  ]
}
```

{% alert note %}
La mise à jour d'un objet d'attribut personnalisé à `null` consomme également un point de données.
{% endalert %}
[5]: {% image_buster /assets/img_archive/nca_liquid_2.png %} [6]: {% image_buster /assets/img_archive/nca_segmentation_2.png %} [7]: {% image_buster /assets/img_archive/nca_comparator.png %}


[1]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
