---
nav_title: Attributs personnalisés imbriqués
article_title: Attributs personnalisés imbriqués
alias: "/nested_custom_attribute_support/"
page_order: 1
page_type: reference
description: "Cet article de référence explique comment utiliser les attributs personnalisés imbriqués en tant que type de données pour des attributs personnalisés, avec les limitations et des exemples d’utilisation."
---

# Attributs personnalisés imbriqués

Vous pouvez utiliser des attributs personnalisés imbriqués pour envoyer des objets en tant que nouveau type de données pour des attributs personnalisés. Ces données imbriquées vous permettent de créer des segments à l’aide d’informations à partir d’un objet d’attribut personnalisé, et de personnaliser vos messages avec un objet d’attribut personnalisé et Liquid.

Les objets peuvent contenir des [types de données][1] existants, comme :

- Chiffres
- Chaînes de caractères
- Booléens
- Arrays
- Date
- Autres objets
- [Tableaux d’objets]({{site.baseurl}}/array_of_objects/)

## Limitations

- Les attributs personnalisés imbriqués sont destinés aux attributs personnalisés envoyés via l’API. Ils ne sont pas pris en charge pour une utilisation avec les SDK Braze.
- Les partenaires ne prennent pas en charge les tableaux d’objets. Nous vous déconseillons d’utiliser cette fonctionnalité avec des groupes d’applications ayant activé des intégrations partenaires.
- Les objets ont une taille maximale de 50 Ko.
- Les noms clés et les valeurs de chaîne de caractères ont une limite de taille de 255 caractères.
- Les noms de clé ne peuvent pas contenir d’espaces.

## Corps de la requête API

{% tabs %}
{% tab Create %}
Voici un `/users/track` exemple avec un objet « Chanson la plus jouée ». Pour capturer les propriétés de la chanson, nous enverrons une demande API qui répertorie `most_played_song` en tant qu’objet, avec un ensemble de propriétés.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Update %}
Pour mettre à jour un objet existant, envoyez un message POST à `users/track` avec le paramètre `_merge_objects` dans la demande. Cela va fusionner en profondeur (deep merge) votre mise à jour avec les données d’objet existantes. Le deep merge (ou fusion profonde) garantit que tous les niveaux d’un objet sont fusionnés dans un autre objet, et pas juste le premier niveau. Dans cet exemple, nous avons déjà un objet `most_played_song` dans Braze, et maintenant nous ajoutons un nouveau champ `year_released`, à l’objet `most_played_song`.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

Une fois cette demande reçue, l’objet d’attribut personnalisé ressemblera à ça :

```json
"most_played_song": {
  "song_name": "Solea",
  "artist_name" : "Miles Davis",
  "album_name": "Sketches of Spain",
  "year_released": 1960,
  "genre": "Jazz",
  "play_analytics": {
     "count": 1000,
     "top_10_listeners": true
  }
}
```

{% alert warning %}
Vous devez définir `_merge_objects` sur True (vrai) ou vos objets seront écrasés. Par défaut,`_merge_objects` est défini sur False (faux).
{% endalert %}

{% endtab %}
{% tab Delete %}
Pour supprimer un objet d’attribut personnalisé, envoyez un message POST à `users/track` avec l’objet d’attribut personnalisé défini sur `null`.

```json
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

#### Capturer des dates en tant que propriétés d’objet

Pour capturer des dates en tant que propriétés d’objet, vous devez utiliser la clé `$time`. Dans l’exemple suivant, un objet « Dates importantes » est utilisé pour capturer l’ensemble des propriétés d’objet, `birthday` et `wedding_anniversary`. La valeur de ces dates est un objet avec une clé`$time`.

```json
{
  "attributes": [ 
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01T19:20:30Z"},
        "wedding_anniversary": {"$time" : "2020-05-28T19:20:30Z"}
      }
    }
  ]
}
```

## Modèles Liquid

Les exemples de templating Liquid suivants montrent comment référencer les propriétés d’objet d’attribut personnalisées de la requête API précédente pour les utiliser dans vos communications Liquid.

Utilisez la balise de personnalisation`custom_attribute` et notation par points pour accéder aux propriétés sur un objet. Spécifiez le nom de l’objet (et la position dans le tableau si vous référencez un tableau d’objets), suivi d’un point (période), suivi du nom de la propriété.

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` — "Miles Davis"
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` — "Solea"
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` — "50"
{% endraw %}

![Utiliser Liquid pour utiliser dans un message le nom du morceau et le nombre de fois que l’utilisateur l’a écouté ][5]

## Segmentation

Vous pouvez créer des segments basés sur des attributs personnalisés imbriqués pour cibler encore plus précisément vos utilisateurs. Pour ce faire, filtrez votre segment en fonction de l’objet d’attribut personnalisé, puis spécifiez le chemin vers le nom de propriété et la valeur associée que vous souhaitez segmenter. Si vous n’êtes pas sûr de ce chemin, vous pouvez [générer un schéma](#generate-schema) et utilisez l’explorateur d’objets imbriqué pour que Braze remplisse automatiquement ce champ à votre place.

Après avoir ajouté un chemin à votre propriété, cliquez sur **Validate (Valider)** pour vérifier que la valeur du champ Chemin est bien valide.

![Filtrage basé sur un attribut personnalisé de la chanson la plus jouée, où un auditeur a écouté une chanson plus d’un nombre de fois spécifié][6]

Quand vous travaillez sur la segmentation d’attributs personnalisés imbriqués, vous avez accès à un nouveau comparateur regroupé par type de données. Par exemple, comme `play_analytics.count` est un nombre, vous pouvez sélectionner un comparateur sous la catégorie **Nombre**.

![Un utilisateur choisissant un opérateur basé sur le type de données pour l’attribut personnalisé imbriqué][7]

### Segmentation sur plusieurs critères

Utilisez la **segmentation** sur plusieurs critères pour créer un segment qui correspond à plusieurs critères au sein d’un même objet. L’utilisateur est qualifié pour le segment s’il a au moins un tableau d’objets correspondant à tous les critères définis. Par exemple, les utilisateurs ne correspondront à ce segment que si leur clé n’est pas vide et que leur nombre est supérieur à 0.

![Un exemple de segment avec la case pour la segmentation sur plusieurs critères sélectionnée.][14]

### Générer un schéma à l’aide de l’explorateur d’objets imbriqué {#generate-schema}

Vous pouvez générer un schéma pour vos objets afin de créer des filtres de segment sans avoir besoin de mémoriser les chemins des objets imbriqués. Pour cela, suivez ces étapes :.

#### Étape 1 : Générez un schéma

Dans cet exemple, supposons que nous avons `accounts` un tableau d’objets que nous venons de transmettre à Braze :

```json
"accounts": [
  {"type": "taxable",
  "balance": 22500,
  "active": true},
  {"type": "non-taxable",
  "balance": 0,
  "active": true},
 ]
```

Dans le tableau de bord de Braze, naviguez jusqu’à **Manage Settings (Gérer les paramètres)** > **Custom Attributes (Attributs personnalisés)**. Recherchez votre objet ou votre tableau d’objets. Dans la colonne **Nom de l’attribut**, cliquez sur **Generate Schema (Générer un schéma)**.

![][8]

{% alert tip %}
La génération du schéma peut prendre quelques minutes, en fonction de la quantité de données que vous nous avez envoyées.
{% endalert %}

Une fois le schéma généré, un nouveau <i class="fas fa-plus"></i> bouton Plus apparaît à la place du bouton **Générer un schéma**. Vous pouvez cliquer dessus pour voir ce que Braze sait sur cet attribut personnalisé imbriqué. 

Pendant la génération du schéma, Braze examine les données envoyées précédemment et crée une représentation idéale de vos données pour cet attribut. Braze analyse également vos valeurs imbriquées et leur attribue un type de données.

Pour notre `accounts` d’objets, vous pouvez voir que dans le tableau d’objets, un objet contient ce qui suit :

- Type booléen avec une clé de `active` (indépendamment du fait que le compte soit actif ou non)
- Un type de numéro avec une clé `balance` (solde du compte)
- Un type de chaîne avec une clé `type` (compte imposable ou non imposable)

![][10]{: style="max-width:50%" }

Maintenant que nous avons analysé et construit une représentation des données, créons un segment.

#### Étape 2 : Construire un segment

Ciblons les clients qui ont un solde inférieur à 100 pour leur envoyer un message et les encourager à regarnir leur compte.

Créez un segment et ajouter le filtre `Attribut personnalisé imbriqué`, puis recherchez et sélectionnez votre objet ou votre tableau d’objets. Ici, nous avons ajouté le tableau d’objets `accounts`. 

![][11]

Cliquez sur le <i class="fas fa-plus"></i> bouton Plus du champ de chemin. Cela affichera une représentation de votre objet ou de votre tableau d’objets. Vous pouvez sélectionner un ou plusieurs des éléments répertoriés et Braze les insérera dans le champ de chemin pour vous. Pour notre cas d’utilisation, nous devons obtenir le solde. Sélectionnez le solde et le chemin (dans ce cas, `[].balance`) est automatiquement renseigné dans le champ du chemin.

![][12]{: style="max-width:70%" }

Vous pouvez cliquer sur **Validate (Valider)** pour vérifier que la valeur du champ de chemin est valide, puis construisez le reste du filtre selon les besoins. Nous avons indiqué que le solde doit être inférieur à 100.

![][13]

Et voilà ! Vous venez de créer un segment à l’aide d’un attribut personnalisé imbriqué, sans avoir besoin de savoir comment les données sont structurées. L’explorateur d’objets imbriqués de Braze a généré une représentation visuelle de vos données et vous a permis d’explorer et de sélectionner exactement ce dont vous aviez besoin pour créer le segment.

### Déclencher les modifications d’attributs personnalisés imbriqués

Vous pouvez déclencher lorsqu’un objet d’attribut personnalisé imbriqué est modifié. Cette option n’est pas disponible pour les modifications apportées aux matrices d’objets. Si vous ne voyez pas l’option pour afficher l’explorateur de chemin, vérifiez que vous avez généré un schéma. 

![][16]

Par exemple, dans la campagne basée sur les actions suivantes, vous pouvez ajouter une nouvelle action de déclenchement pour **Modifier la valeur d’attribut personnalisée** pour cibler les utilisateurs qui ont modifié leurs préférences de bureau de quartier. 

![][15]

### Personnalisation

Utiliser le modal **Add Personalization (Ajouter une personnalisation)**, vous pouvez également insérer des attributs personnalisés imbriqués dans votre envoi de messages. Sélectionner **Nested Custom Attributes (Attributs personnalisés imbriqués)** comme type de personnalisation. Ensuite, sélectionnez l’attribut de niveau supérieur et la clé d’attribut. 

Par exemple, dans le modal de personnalisation ci-dessous, cela insère l’attribut personnalisé imbriqué d’un bureau de quartier local basé sur les préférences d’un utilisateur.

![][9]{: style="max-width:70%" }

{% alert tip %}
Vérifiez qu’un schéma a été généré si vous ne voyez pas l’option d’insérer des attributs personnalisés imbriqués.
{% endalert %}

### Générez un schéma {#regenerate-schema}

Après qu’un schéma a été généré, il peut l’être à nouveau toutes les 24 heures. Localisez votre attribut personnalisé et cliquez sur le bouton plus <i class="fas fa-plus"></i> pour afficher le schéma actuel. Cliquez ensuite sur <i class="fas fa-arrows-rotate"></i> **Regenerate Schema (Régénérer un schéma)**. Cette option sera désactivée si le schéma a été régénéré pour la dernière fois il y a moins de 24 heures.

## Points de données

Toute clé mise à jour consomme un point de données. Par exemple, cet objet initialisé dans le profil utilisateur consomme sept (7) points de données :

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "year_released": 1960,
        "genre": "Jazz",
        "play_analytics": {
          "count": 1000,
          "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% alert note %}
La mise à jour d’un objet d’attribut personnalisé vers `null` consomme également un point de données.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[4]: https://calendly.com/d/w9y6-qq9c/feedback-on-nested-custom-attributes?month=2021-07
[5]: {% image_buster /assets/img_archive/nca_liquid_2.png %} 
[6]: {% image_buster /assets/img_archive/nca_segmentation_2.png %}
[7]: {% image_buster /assets/img_archive/nca_comparator.png %}
[8]: {% image_buster /assets/img_archive/nca_generate_schema.png %}
[9]:{% image_buster /assets/img_archive/nca_personalization.png %}
[10]: {% image_buster /assets/img_archive/nca_schema.png %}
[11]: {% image_buster /assets/img_archive/nca_segment_schema.png %}
[12]: {% image_buster /assets/img_archive/nca_segment_schema2.png %}
[13]: {% image_buster /assets/img_archive/nca_segment_schema_3.png %}
[14]: {% image_buster /assets/img_archive/nca_multi_criteria.png %}
[15]: {% image_buster /assets/img_archive/nca_triggered_changes.png %}
[16]: {% image_buster /assets/img_archive/nca_triggered_changes2.png %}
