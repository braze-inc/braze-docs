---
nav_title: Attributs personnalisés imbriqués
article_title: Attributs personnalisés imbriqués
alias: "/nested_custom_attribute_support/"
page_order: 1
page_type: reference
description: "Cet article de référence explique comment utiliser les attributs personnalisés imbriqués en tant que type de données pour des attributs personnalisés, avec les limitations et des exemples d’utilisation."
---

# Attributs personnalisés imbriqués

Les attributs personnalisés imbriqués vous permettent de définir un ensemble d'attributs en tant que propriété d'un autre attribut. En d'autres termes, lorsque vous définissez un objet d'attribut personnalisé, vous pouvez définir un ensemble d'attributs supplémentaires pour cet objet.

Par exemple, disons que vous souhaitez définir un attribut personnalisé sur le profil utilisateur appelé `favorite_book`. Cet attribut personnalisé peut être défini comme un objet ayant les attributs imbriqués `title`, `author`, et `publishing_date`, comme suit :

```json
"favorite_book": {
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
}
```

Ces données imbriquées vous permettent de créer des segments à l’aide d’informations à partir d’un objet d’attribut personnalisé, et de personnaliser vos messages avec un objet d’attribut personnalisé et Liquid.

Les objets d'attribut personnalisé peuvent contenir des [types de données][1], tels que :

- Chiffres
- Chaînes de caractères
- Booléens
- Tableaux
- Date
  - Lorsque vous filtrez un attribut personnalisé temporel imbriqué, vous pouvez choisir de filtrer en fonction du "jour de l'année" ou de l'"heure". "Jour de l'année" vérifiera uniquement le mois et le jour pour la comparaison. "Time" comparera l'horodatage complet, y compris l'année.
- Autres objets
- [Tableaux d’objets]({{site.baseurl}}/array_of_objects/)

## Limitations

- Les attributs personnalisés imbriqués sont destinés aux attributs personnalisés envoyés via le SDK ou l'API de Braze. 
- Les objets ont une taille maximale de 50 Ko.
- Les noms clés et les valeurs de chaîne de caractères ont une limite de taille de 255 caractères.
- Les noms de clé ne peuvent pas contenir d’espaces.
- Tous les partenaires Braze ne prennent pas en charge les attributs personnalisés imbriqués. Consultez la [documentation du partenaire]({{site.baseurl}}/partners/home) pour savoir si l'intégration prend en charge cette fonctionnalité.
- Les attributs personnalisés imbriqués ne peuvent pas être utilisés comme filtre lors d'un appel à l'API Connected Audience.

## Exemple d'API

{% tabs local %}
{% tab Créer %}
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
{% tab Mettre à jour %}
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

Une fois cette demande reçue, l’objet Attribut personnalisé ressemblera à ça :

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
Vous devez définir `_merge_objects` comme `true`, sinon vos objets seront écrasés. `_merge_objects` est `false` par défaut.
{% endalert %}

{% endtab %}
{% tab Supprimer %}
Pour supprimer un objet d’attribut personnalisé, envoyez un message POST à `users/track` avec l’objet Attribut personnalisé défini sur `null`.

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

## Exemple de SDK

{% sdk_min_versions android:25.0.0 ios:6.1.0 web:4.7.0 %}

{% tabs local %}
{% tab Android SDK %}

**Créer**
```kotlin
val json = JSONObject()
    .put("song_name", "Solea")
    .put("artist_name", "Miles Davis")
    .put("album_name", "Sketches of Spain")
    .put("genre", "Jazz")
    .put(
        "play_analytics",
        JSONObject()
            .put("count", 1000)
            .put("top_10_listeners", true)
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json)
}
```

**Mettre à jour**
```kotlin
val json = JSONObject()
    .put("year_released", 1960)

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json, true)
}
```

**Supprimer**
```kotlin
braze.getCurrentUser { user ->
    user.unsetCustomUserAttribute("most_played_song")
}
```

{% endtab %}
{% tab Swift SDK %}

**Créer**
```swift
let json: [String: Any?] = [
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": [
    "count": 1000,
    "top_10_listeners": true,
  ],
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json)
```

**Mettre à jour**
```swift
let json: [String: Any?] = [
  "year_released": 1960
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json, merge: true)
```

**Supprimer**
```swift
braze.user.unsetCustomAttribute(key: "most_played_song")
```

{% endtab %}
{% tab Web SDK %}

**Créer**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": {
    "count": 1000,
    "top_10_listeners": true
  }
};
braze.getUser().setCustomUserAttribute("most_played_song", json);
```

**Mettre à jour**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "year_released": 1960
};
braze.getUser().setCustomUserAttribute("most_played_song", json, true);

```

**Supprimer**
```javascript
import * as braze from "@braze/web-sdk";
braze.getUser().setCustomUserAttribute("most_played_song", null);
```

{% endtab %}
{% endtabs %}

## Capturer des dates en tant que propriétés d’objet

Pour capturer des dates en tant que propriétés d’objet, vous devez utiliser la clé `$time`. Dans l’exemple suivant, un objet « Dates importantes » est utilisé pour capturer l’ensemble des propriétés d’objet, `birthday` et `wedding_anniversary`. La valeur de ces dates est un objet avec une clé `$time`, qui ne peut pas être une valeur nulle.

{% alert note %}
Si vous n'avez pas capturé les dates en tant que propriétés de l'objet au départ, nous vous recommandons de renvoyer ces données à l'aide de la clé `$time` pour tous les utilisateurs. Dans le cas contraire, l'utilisation de l'attribut `$time` peut donner lieu à des segments incomplets.
{% endalert %}

```json
{
  "attributes": [ 
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01"},
        "wedding_anniversary": {"$time" : "2020-05-28"}
      }
    }
  ]
}
```

Notez que, pour les attributs personnalisés imbriqués, si l'année est inférieure à 0 ou supérieure à 3 000, Braze ne stocke pas ces valeurs sur l'utilisateur.

## Modèles Liquid

Les exemples de templating Liquid suivants montrent comment référencer les propriétés d’objet d’attribut personnalisées de la requête API précédente pour les utiliser dans vos communications Liquid.

Utilisez la balise de personnalisation `custom_attribute` et la notation par points pour accéder aux propriétés sur un objet. Spécifiez le nom de l’objet (et la position dans le tableau si vous référencez un tableau d’objets), suivi d’un point (période), suivi du nom de la propriété.

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` - Miles Davis
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` - Solea
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` - "1000"
{% endraw %}

![Utiliser Liquid pour utiliser dans un message le nom du morceau et le nombre de fois que l’utilisateur l’a écouté ][5]

## Segmentation

Vous pouvez créer des segments basés sur des attributs personnalisés imbriqués pour cibler encore plus précisément vos utilisateurs. Pour ce faire, filtrez votre segment en fonction de l’objet Attribut personnalisé, puis spécifiez le chemin vers le nom de propriété et la valeur associée que vous souhaitez segmenter. Si vous ne savez pas à quoi ressemble ce chemin, vous pouvez [générer un schéma](#generate-schema) et utiliser l'explorateur d'objets imbriqués pour demander à Braze de remplir ce chemin pour vous.

Après avoir ajouté un chemin d'accès à votre propriété, cliquez sur **Valider** pour vérifier que la valeur du champ chemin d'accès est valide.

![Filtrage basé sur un attribut personnalisé de la chanson la plus jouée, où un auditeur a écouté une chanson plus d’un nombre de fois spécifié][6]

Pour segmenter avec des attributs personnalisés imbriqués, sélectionnez le filtre **Attributs personnalisés imbriqués** pour afficher une liste déroulante dans laquelle vous pouvez sélectionner un attribut personnalisé imbriqué spécifique.

![][17]{: style="max-width:70%;"}

Quand vous travaillez sur la segmentation d’attributs personnalisés imbriqués, vous avez accès à un nouveau comparateur regroupé par type de données. Par exemple, comme `play_analytics.count` est un nombre, vous pouvez sélectionner un comparateur dans la catégorie **Nombre.** 

![Un utilisateur choisissant un opérateur basé sur le type de données pour l’attribut personnalisé imbriqué][7]

### Filtrage des types de données temporelles

Lorsque vous filtrez un attribut personnalisé temporel imbriqué, vous pouvez choisir de filtrer avec des opérateurs dans les catégories **Jour de l'année** ou **Heure** lors de la comparaison de la valeur de la date. 

Si vous sélectionnez un opérateur dans la catégorie **Jour de l'année**, seuls le mois et le jour seront vérifiés pour comparaison au lieu de l'horodatage complet de la valeur de l'attribut personnalisé imbriqué. La sélection d'un opérateur dans la catégorie **Temps** permet de comparer l'horodatage complet, y compris l'année.

### Segmentation sur plusieurs critères

Utilisez la **segmentation multicritères** pour créer un segment correspondant à plusieurs critères au sein d'un même objet. L’utilisateur est qualifié pour le segment s’il a au moins un tableau d’objets correspondant à tous les critères définis. Par exemple, les utilisateurs ne correspondront à ce segment que si leur clé n’est pas vide et que leur nombre est supérieur à 0.

Vous pouvez également utiliser la fonctionnalité **Copier le liquide pour le segment** pour générer un code liquide pour ce segment et l'utiliser dans un message. Par exemple, supposons que vous ayez un tableau d’objets de compte et un segment qui cible les clients avec des comptes imposables actifs. Pour que les clients contribuent à l’objectif du compte associé à l’un de leurs comptes actifs et imposables, vous devrez créer un message pour les encourager. 

![Un exemple de segment avec la case pour la segmentation sur plusieurs critères sélectionnée.][14]

Lorsque vous sélectionnez **Copier Liquid pour le segment**, Braze génère automatiquement un code Liquid qui renvoie un tableau d'objets ne contenant que des comptes actifs et imposables.

{% raw %}

```
{% assign segmented_nested_objects = '' | split: '' %}
{% assign obj_array = {{custom_attribute.${accounts}}} %}
{% for obj in obj_array %}
  {% if obj["account_type"] == 'taxable' and obj["active"] == true %}
    {% assign segmented_nested_objects = obj_array | slice: forloop.index0 | concat: segmented_nested_objects | reverse %}
  {% endif %}
{% endfor %}
```

À partir de là, vous pouvez utiliser les `segmented_nested_objects` et personnaliser votre message. Dans notre cas d’utilisation, nous voulons prendre un objectif du premier compte imposable actif et le personnaliser :

```
Get to your {{segmented_nested_objects[0].goal}} goal faster, make a deposit using our new fast deposit feature!
```

{% endraw %}

Ceci renvoie le message suivant à votre client : « Atteignez votre objectif de retraite plus rapidement, effectuez un dépôt à l’aide de notre nouvelle fonctionnalité de dépôt rapide ! »

### Générer un schéma à l’aide de l’explorateur d’objets imbriqué {#generate-schema}

Vous pouvez générer un schéma pour vos objets afin de créer des filtres de segment sans avoir besoin de mémoriser les chemins des objets imbriqués. Pour cela, suivez ces étapes.

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

Dans le tableau de bord de Braze, sélectionnez **Paramètres des données** > **Attributs personnalisés**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous trouverez les **attributs personnalisés** sous **Gérer les paramètres.**
{% endalert %}

Recherchez votre objet ou votre tableau d'objets. Dans la colonne **Nom de l'attribut**, cliquez sur **Générer le schéma**.

![][8]

{% alert tip %}
La génération du schéma peut prendre quelques minutes, en fonction de la quantité de données que vous nous avez envoyées.
{% endalert %}

Une fois le schéma généré, un nouveau bouton <i class="fas fa-plus"></i> plus apparaît à la place du bouton **Générer le schéma**. Vous pouvez cliquer dessus pour voir ce que Braze sait sur cet attribut personnalisé imbriqué. 

Pendant la génération du schéma, Braze examine les données envoyées précédemment et crée une représentation idéale de vos données pour cet attribut. Braze analyse également vos valeurs imbriquées et leur attribue un type de données. Pour ce faire, les données précédemment envoyées à Braze pour l'attribut imbriqué donné sont échantillonnées.

Pour notre tableau d’objets `accounts`, vous pouvez voir que dans le tableau d’objets, un objet contient ce qui suit :

- Type booléen avec une clé de `active` (indépendamment du fait que le compte soit actif ou non)
- Un type de numéro avec une clé `balance` (solde du compte)
- Un type de chaîne avec une clé `type` (compte imposable ou non imposable)

![][10]{: style="max-width:50%" }

Maintenant que nous avons analysé et créé une représentation des données, créons un segment.

#### Étape 2 : Créer un segment

Ciblons les clients qui ont un solde inférieur à 100 pour leur envoyer un message et les encourager à regarnir leur compte.

Créer un segment et ajouter le filtre `Nested Custom Attribute`, puis recherchez et sélectionnez votre objet ou votre tableau d’objets. Ici, nous avons ajouté le tableau d’objets `accounts`. 

![][11]

Cliquez sur le bouton Plus <i class="fas fa-plus"></i> du champ de chemin. Cela affichera une représentation de votre objet ou de votre tableau d’objets. Vous pouvez sélectionner un ou plusieurs des éléments répertoriés et Braze les insérera dans le champ de chemin pour vous. Pour notre cas d’utilisation, nous devons obtenir le solde. Sélectionnez le solde et le chemin (dans ce cas, `[].balance`) est automatiquement renseigné dans le champ du chemin.

![][12]{: style="max-width:70%" }

Vous pouvez cliquer sur **Valider** pour vérifier que le contenu du champ chemin d'accès est valide, puis créer le reste du filtre si nécessaire. Nous avons indiqué que le solde doit être inférieur à 100.

![][13]

Et voilà ! Vous venez de créer un segment à l’aide d’un attribut personnalisé imbriqué, sans avoir besoin de savoir comment les données sont structurées. L'explorateur d'objets imbriqués de Braze a généré une représentation visuelle de vos données et vous a permis d'explorer et de sélectionner exactement ce dont vous aviez besoin pour créer un segment.

### Déclencher les modifications d’attributs personnalisés imbriqués

Vous pouvez déclencher lorsqu’un objet d’attribut personnalisé imbriqué est modifié. Cette option n’est pas disponible pour les modifications apportées aux tableaux d’objets. Si vous ne voyez pas l’option pour afficher l’explorateur de chemin, vérifiez que vous avez généré un schéma. 

![][16]

Par exemple, dans la campagne par action suivante, vous pouvez ajouter une nouvelle action de déclenchement pour **Modifier la valeur de l'attribut personnalisé** afin de cibler les utilisateurs qui ont modifié leurs préférences en matière de bureau de quartier. 

![][15]

### Personnalisation

Grâce à la fenêtre modale/boîte de **personnalisation**, vous pouvez également insérer des attributs personnalisés imbriqués dans votre envoi de messages. Sélectionnez **Attributs personnalisés imbriqués** comme type de personnalisation. Ensuite, sélectionnez l’attribut de niveau supérieur et la clé d’attribut. 

Par exemple, dans le modal de personnalisation ci-dessous, cela insère l’attribut personnalisé imbriqué d’un bureau de quartier local basé sur les préférences d’un utilisateur.

![][9]{: style="max-width:70%" }

{% alert tip %}
Vérifiez qu’un schéma a été généré si vous ne voyez pas l’option d’insérer des attributs personnalisés imbriqués.
{% endalert %}

### Régénérez un schéma {#regenerate-schema}

Après qu’un schéma a été généré, il peut l’être à nouveau toutes les 24 heures. Cette section décrit comment régénérer votre schéma. Pour plus d'informations sur les schémas, reportez-vous à la section de cet article consacrée à la [génération d'un schéma](#generate-schema).

Pour régénérer le schéma de votre attribut personnalisé imbriqué :

1. Sélectionnez **Paramètres des données** > **Attributs personnalisés**.
2. Recherchez votre attribut personnalisé imbriqué.
3. Dans la colonne **Nom de** l'attribut correspondant à votre attribut, cliquez sur <i class="fas fa-plus"></i> pour gérer le schéma.
4. Une fenêtre modale apparaît. Cliquez sur **Régénérer le schéma**.

L'option de régénération du schéma sera désactivée s'il s'est écoulé moins de 24 heures depuis la dernière régénération du schéma. La régénération du schéma ne détectera que les nouveaux objets et ne supprimera pas les objets qui existent déjà dans le schéma.

{% alert important %}
Si vous souhaitez réinitialiser le schéma d'un tableau d'objets avec un objet existant, vous devez créer un nouvel attribut personnalisé. La régénération du schéma ne supprime pas les objets existants.
{% endalert %}

Si les données n'apparaissent pas comme prévu après la régénération du schéma, il se peut que l'attribut ne soit pas ingéré assez souvent. Les données de l'utilisateur sont échantillonnées sur les données précédentes envoyées à Braze pour l'attribut imbriqué donné. Si l'attribut n'est pas suffisamment ingéré, il ne sera pas pris en compte dans le schéma.

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
[17]: {% image_buster /assets/img_archive/nested_custom_attributes.png %}