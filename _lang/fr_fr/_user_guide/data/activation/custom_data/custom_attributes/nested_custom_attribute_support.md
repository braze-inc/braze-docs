---
nav_title: Attributs personnalisés imbriqués
article_title: Attributs personnalisés imbriqués
alias: "/nested_custom_attribute_support/"
page_order: 1
page_type: reference
description: "Cet article de référence traite de l'utilisation des attributs personnalisés imbriqués comme type de données pour les attributs personnalisés, y compris les limitations et les exemples d'utilisation."
---

# Attributs personnalisés imbriqués

> Cette page traite des attributs personnalisés imbriqués, qui vous permettent de définir un ensemble d'attributs en tant que propriété d'un autre attribut. En d'autres termes, lorsque vous définissez un objet d'attribut personnalisé, vous pouvez définir un ensemble d'attributs supplémentaires pour cet objet.

{% multi_lang_include nested_attribute_objects/about_nested_attributes.md %}

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Limites

- Les attributs personnalisés imbriqués sont destinés aux attributs personnalisés envoyés via le SDK ou l'API de Braze. 
- Les objets ont une taille maximale de 100 Ko.
- Les noms de clés et les valeurs de chaînes de caractères sont limités à 255 caractères.
- Les noms de clés ne peuvent pas contenir d'espaces.
- Les points (`.`) et les signes de dollar (`$`) ne sont pas des caractères pris en charge dans une charge utile API si vous tentez d'envoyer un attribut personnalisé imbriqué à un profil utilisateur.
- Tous les partenaires Braze ne prennent pas en charge les attributs personnalisés imbriqués. Reportez-vous à la [documentation du partenaire]({{site.baseurl}}/partners/home) pour savoir si les intégrations spécifiques du partenaire prennent en charge cette fonctionnalité.
- Les attributs personnalisés imbriqués ne peuvent pas être utilisés comme filtre lors d'un appel à l'API Connected Audience.

## Exemple d'API

{% tabs local %}
{% tab Create %}
Voici un exemple de `/users/track` avec un objet "Most Played Song" (chanson la plus écoutée). Pour capturer les propriétés de la chanson, nous enverrons une requête API qui répertorie `most_played_song` en tant qu'objet, ainsi qu'un ensemble de propriétés de l'objet.

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
Pour mettre à jour un objet existant, envoyez un POST à `users/track` avec le paramètre `_merge_objects` dans la requête. Cette opération permet de fusionner en profondeur votre mise à jour avec les données de l'objet existant. La fusion en profondeur garantit que tous les niveaux d'un objet sont fusionnés dans un autre objet au lieu de se limiter au premier niveau. Dans cet exemple, nous avons déjà un objet `most_played_song` dans Braze, et nous ajoutons maintenant un nouveau champ, `year_released`, à l'objet `most_played_song`.

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

Après réception de cette demande, l'objet attribut personnalisé se présente comme suit :

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
{% tab Delete %}
Pour supprimer un objet d'attribut personnalisé, envoyez un POST à `users/track` avec l'objet d'attribut personnalisé défini à `null`.

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

{% alert note %}
Cette approche ne peut pas être utilisée pour supprimer une clé imbriquée dans un [tableau d'objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects).
{% endalert %}

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

**Mise à jour**
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

**Mise à jour**
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

**Mise à jour**
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

## Saisir les dates en tant que propriétés d'un objet

Pour capturer des dates en tant que propriétés d'objet, vous devez utiliser la clé `$time`. Dans l'exemple suivant, un objet "Dates importantes" est utilisé pour capturer l'ensemble des propriétés de l'objet, `birthday` et `wedding_anniversary`. La valeur de ces dates est un objet avec une clé `$time`, qui ne peut pas être une valeur nulle.

{% alert note %}
Si vous n'avez pas capturé les dates en tant que propriétés de l'objet au départ, nous vous recommandons de renvoyer ces données à l'aide de la clé `$time` pour tous les utilisateurs. Dans le cas contraire, l'utilisation de l'attribut `$time` peut donner lieu à des segments incomplets. Toutefois, si la valeur de `$time` dans un attribut personnalisé imbriqué n'est pas formatée correctement, l'ensemble de l'attribut personnalisé imbriqué ne sera pas mis à jour.
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

{% alert note %}
Pour les attributs personnalisés imbriqués, si l'année est inférieure à 0 ou supérieure à 3000, Braze ne stocke pas ces valeurs sur l'utilisateur.
{% endalert %}

## Modèle liquide

L'exemple de modèle Liquid suivant montre comment référencer les propriétés de l'objet attribut personnalisé enregistrées à partir de la requête API précédente et les utiliser dans votre envoi de messages.

Utilisez l'étiquette de personnalisation `custom_attribute` et la notation par points pour accéder aux propriétés d'un objet. Spécifiez le nom de l'objet (et sa position dans le tableau si vous faites référence à un tableau d'objets), suivi d'un point, puis du nom de la propriété.

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` - Miles Davis
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` - Solea
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` - "1000"
{% endraw %}

Utilisation de Liquid pour insérer dans un message le nom d'une chanson et le nombre de fois qu'un auditeur a écouté cette chanson.]({% image_buster /assets/img_archive/nca_liquid_2.png %})

## Segmentation

Vous pouvez créer des segmentations basées sur des attributs personnalisés imbriqués pour mieux cibler vos utilisateurs. Pour ce faire, filtrez votre segment en fonction de l'objet attribut personnalisé, puis indiquez le chemin d'accès au nom de votre propriété et à la valeur associée sur laquelle vous souhaitez segmenter. Si vous ne savez pas à quoi ressemble ce chemin, vous pouvez [générer un schéma](#generate-schema) et utiliser l'explorateur d'objets imbriqués pour demander à Braze de remplir ce chemin pour vous.

Après avoir ajouté un chemin d'accès à votre propriété, sélectionnez **Valider** pour vérifier que la valeur du champ chemin d'accès est valide.

Filtrage basé sur un attribut personnalisé de la chanson la plus écoutée lorsqu'un auditeur a écouté une chanson plus d'un certain nombre de fois.]({% image_buster /assets/img_archive/nca_segmentation_2.png %})

Pour segmenter avec des attributs personnalisés imbriqués, sélectionnez le filtre **Attributs personnalisés imbriqués** pour afficher une liste déroulante dans laquelle vous pouvez sélectionner un attribut personnalisé imbriqué spécifique.

\![]({% image_buster /assets/img_archive/nested_custom_attributes.png %}){: style="max-width:70%;"}

Lorsque vous travaillez avec la segmentation par attributs personnalisés imbriqués, vous avez accès à un nouveau comparateur groupé par type de données. Par exemple, comme `play_analytics.count` est un nombre, vous pouvez sélectionner un comparateur dans la catégorie **Nombre.** 

L'utilisateur choisit un opérateur en fonction du type de données de l'attribut personnalisé imbriqué.]({% image_buster /assets/img_archive/nca_comparator.png %})

### Filtrage des types de données temporelles

Lors du filtrage d'un attribut personnalisé temporel imbriqué, vous pouvez choisir de filtrer avec des opérateurs dans les catégories **Jour de l'année** ou **Heure** lors de la comparaison de la valeur de la date. 

Si vous sélectionnez un opérateur dans la catégorie **Jour de l'année**, seuls le mois et le jour seront vérifiés pour comparaison au lieu de l'horodatage complet de la valeur de l'attribut personnalisé imbriqué. La sélection d'un opérateur dans la catégorie **Temps** permet de comparer l'horodatage complet, y compris l'année.

### Segmentation multicritères

Utilisez la **segmentation multicritères** pour créer un segment correspondant à plusieurs critères au sein d'un même objet. L'utilisateur est ainsi qualifié pour le segment s'il possède au moins un tableau d'objets correspondant à tous les critères spécifiés. Par exemple, les utilisateurs ne correspondront à ce segment que si leur clé n'est pas vide et si leur numéro est supérieur à 0.

Vous pouvez également utiliser la fonctionnalité **Copier le liquide pour le segment** pour générer un code liquide pour ce segment et l'utiliser dans un message. Par exemple, supposons que vous disposiez d'un tableau d'objets de compte et d'un segment qui cible les clients ayant un compte taxable actif. Pour inciter les clients à contribuer à l'objectif du compte associé à l'un de leurs comptes actifs et imposables, vous devez créer un message qui les incite à le faire. 

\![Un exemple de segment avec la case à cocher sélectionnée pour la segmentation multicritères.]({% image_buster /assets/img_archive/nca_multi_criteria.png %})

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

À partir de là, vous pouvez utiliser `segmented_nested_objects` et personnaliser votre message. Dans cet exemple, nous voulons prendre un objectif du premier compte taxable actif et le personnaliser :

```
Get to your {{segmented_nested_objects[0].goal}} goal faster, make a deposit using our new fast deposit feature!
```

{% endraw %}

Le message suivant est envoyé à votre client : "Atteignez plus rapidement votre objectif de retraite, faites un dépôt en utilisant notre nouvelle fonctionnalité de dépôt rapide !"

### Générer un schéma à l'aide de l'explorateur d'objets imbriqués {#generate-schema}

Vous pouvez générer un schéma pour vos objets afin de créer des filtres de segmentation sans avoir à mémoriser les chemins d'accès aux objets imbriqués. Pour ce faire, procédez comme suit.

#### Étape 1 : Générer un schéma

Pour cet exemple, supposons que nous ayons un tableau d'objets `accounts` que nous venons d'envoyer à Braze :

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

Dans le tableau de bord de Braze, accédez à **Paramètres des données** > Attributs personnalisés.

Recherchez votre objet ou tableau d'objets. Dans la colonne **Nom de l'attribut**, sélectionnez **Générer un schéma.**

\![]({% image_buster /assets/img_archive/nca_generate_schema.png %})

{% alert tip %}
La génération de votre schéma peut prendre quelques minutes, en fonction de la quantité de données que vous nous avez envoyées.
{% endalert %}

Une fois le schéma généré, un nouveau bouton <i class="fas fa-plus"></i> plus apparaît à la place du bouton **Générer le schéma**. Vous pouvez cliquer dessus pour voir ce que Braze sait de cet attribut personnalisé imbriqué. 

Lors de la génération du schéma, Braze examine les données précédemment envoyées et crée une représentation idéale de vos données pour cet attribut. Braze analyse et ajoute également un type de données pour vos valeurs imbriquées. Pour ce faire, les données précédemment envoyées à Braze pour l'attribut imbriqué donné sont échantillonnées.

Pour notre tableau d'objets `accounts`, vous pouvez voir qu'à l'intérieur du tableau d'objets, il y a un objet qui contient ce qui suit :

- Un type booléen avec une clé de `active` (que le compte soit actif ou non).
- Un type de nombre avec une clé de `balance` (montant du solde du compte)
- Une chaîne de caractères dont la clé est `type` (compte non imposable ou imposable).

\![]({% image_buster /assets/img_archive/nca_schema.png %}){: style="max-width:50%" }

Maintenant que nous avons analysé et créé une représentation des données, construisons une segmentation.

#### Étape 2 : Créer un segment

Ciblons les clients dont le solde est inférieur à 100 afin de leur envoyer un message les incitant à effectuer un dépôt.

Créez un segment et ajoutez le filtre `Nested Custom Attribute`, puis recherchez et sélectionnez votre objet ou votre tableau d'objets. Ici, nous avons ajouté le tableau d'objets `accounts`. 

\![]({% image_buster /assets/img_archive/nca_segment_schema.png %})

Sélectionnez le bouton <i class="fas fa-plus"></i> plus dans le champ du chemin d'accès. Vous obtiendrez une représentation de votre objet ou tableau d'objets. Vous pouvez sélectionner n'importe quel élément de la liste et Braze l'insérera pour vous dans le champ du chemin. Dans cet exemple, nous devons obtenir le solde. Sélectionnez la balance et le chemin d'accès (dans ce cas, `[].balance`) est automatiquement rempli dans le champ du chemin d'accès.

\![]({% image_buster /assets/img_archive/nca_segment_schema2.png %}){: style="max-width:70%" }

Vous pouvez sélectionner **Valider** pour vérifier que le contenu du champ chemin d'accès est valide, puis créer le reste du filtre si nécessaire. Ici, nous avons spécifié que le solde doit être inférieur à 100.

\![]({% image_buster /assets/img_archive/nca_segment_schema_3.png %})

C'est tout ! Vous venez de créer un segment à l'aide d'un attribut personnalisé imbriqué, le tout sans avoir besoin de savoir comment les données sont structurées. L'explorateur d'objets imbriqués de Braze a généré une représentation visuelle de vos données et vous a permis d'explorer et de sélectionner exactement ce dont vous aviez besoin pour créer un segment.

### Déclencher des modifications d'attributs personnalisés imbriqués

Vous pouvez déclencher un déclencheur en cas de modification d'un objet d'attribut personnalisé imbriqué. Cette option n'est pas disponible pour les modifications apportées aux tableaux d'objets. Si vous ne voyez pas d'option pour afficher l'explorateur de chemin, vérifiez que vous avez généré un schéma. 

\![]({% image_buster /assets/img_archive/nca_triggered_changes2.png %})

Par exemple, dans la campagne par action suivante, vous pouvez ajouter une nouvelle action de déclenchement pour **Modifier la valeur de l'attribut personnalisé** afin de cibler les utilisateurs qui ont modifié leurs préférences en matière de bureau de quartier. 

\![]({% image_buster /assets/img_archive/nca_triggered_changes.png %})

### Personnalisation

Grâce à la fenêtre modale/boîte de **personnalisation**, vous pouvez également insérer des attributs personnalisés imbriqués dans votre envoi de messages. Sélectionnez **Attributs personnalisés imbriqués** comme type de personnalisation. Sélectionnez ensuite l'attribut de premier niveau et la clé d'attribut. 

Par exemple, dans la fenêtre modale/boîte de dialogue de personnalisation ci-dessous, l'attribut personnalisé imbriqué d'un bureau de quartier local est inséré en fonction des préférences de l'utilisateur.

\![]({% image_buster /assets/img_archive/nca_personalization.png %}){: style="max-width:70%" }

{% alert tip %}
Vérifiez qu'un schéma a été généré si vous ne voyez pas l'option permettant d'insérer des attributs personnalisés imbriqués.
{% endalert %}

### Régénérer les schémas {#regenerate-schema}

Une fois qu'un schéma a été généré, il peut être régénéré une fois toutes les 24 heures. Cette section décrit comment régénérer votre schéma. Pour plus d'informations sur les schémas, reportez-vous à la section de cet article consacrée à la [génération d'un schéma](#generate-schema).

Pour régénérer le schéma de votre attribut personnalisé imbriqué :

1. Allez dans **Paramètres des données** > Attributs personnalisés.
2. Recherchez votre attribut personnalisé imbriqué.
3. Dans la colonne **Nom de** l'attribut, sélectionnez <i class="fas fa-plus"></i> pour gérer le schéma.
4. Une fenêtre modale/boîte de dialogue apparaît. Sélectionnez **Régénérer le schéma**.

L'option de régénération du schéma sera désactivée s'il s'est écoulé moins de 24 heures depuis la dernière régénération du schéma. La régénération du schéma ne détectera que les nouveaux objets et ne supprimera pas les objets qui existent déjà dans le schéma.

{% alert important %}
Pour réinitialiser le schéma d'un tableau d'objets avec un objet existant, vous devez créer un nouvel attribut personnalisé. La régénération du schéma ne supprime pas les objets existants.
{% endalert %}

Si les données n'apparaissent pas comme prévu après la régénération du schéma, il se peut que l'attribut ne soit pas ingéré assez souvent. Les données de l'utilisateur sont échantillonnées sur les données précédentes envoyées à Braze pour l'attribut imbriqué donné. Si l'attribut n'est pas suffisamment ingéré, il ne sera pas pris en compte dans le schéma.

## Points de données

Toute clé envoyée consomme un point de données. Par exemple, cet objet initialisé dans le profil utilisateur compte pour sept (7) points de données :

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
La mise à jour d'un objet d'attribut personnalisé sur `null` consomme également un point de données.
{% endalert %}

