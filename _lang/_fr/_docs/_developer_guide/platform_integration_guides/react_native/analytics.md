---
nav_title: Analyses
article_title: Analytiques pour React Natif
platform: React Natif
page_order: 5
description: "Cet article couvre la façon de mettre en place et de suivre les analyses de base dans l'application React Native."
---

# Analyses

Cet article couvre la façon de configurer et de suivre les analyses de base dans votre application React Native.

Avant de commencer, lisez notre article [Aperçu de l'analyse][] pour en savoir plus sur les analyses de Braze et ce qui est déjà suivi par défaut. Nous vous recommandons également de vous familiariser avec nos [conventions de nommage d'événement][1].

## Suivi de session

<!-- COPIED: Android/Analytics/Tracking Sessions -->

Le Braze SDK rapporte les données de session utilisées par le tableau de bord Braze pour calculer l'engagement des utilisateurs et d'autres analyses intégrales à la compréhension de vos utilisateurs. Basé sur la sémantique de session ci-dessous, notre SDK génère des points de données « démarrer la session » et « fermer la session » qui tiennent compte de la durée de la session et du nombre de sessions visibles dans le tableau de bord de Braze.

Pour définir un identifiant utilisateur ou démarrer une session, utilisez la méthode `changeUser` , qui prend un paramètre d'identifiant utilisateur.

```javascript
ReactAppboy.changeUser("user_id");
```

## Journalisation des événements personnalisés

<!-- Copied ios/android/analytics/tracking custom events -->

Vous pouvez enregistrer des événements personnalisés dans Braze pour en savoir plus sur les habitudes d'utilisation de votre application et pour segmenter vos utilisateurs par leurs actions dans le tableau de bord.

```javascript
ReactAppboy.logCustomEvent("react_native_custom_event");
```

Vous pouvez ajouter des métadonnées à propos de l'événement en passant un objet de propriétés avec votre événement personnalisé.

```javascript
reactAppboy.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```

## Logging des attributs personnalisés

<!-- Copied ios/android/analytics/setting custom attributes -->

Braze fournit des méthodes pour assigner des attributs aux utilisateurs. Vous pourrez filtrer et segmenter vos utilisateurs en fonction de ces attributs sur le tableau de bord.

### Attributs par défaut de l'utilisateur

Pour assigner automatiquement les attributs utilisateur collectés par Braze, vous pouvez utiliser les méthodes de setter fournies avec le SDK.

```javascript
ReactAppboy.setFirstName("Nom");
```

Les attributs suivants sont pris en charge :

- Prénom
- Nom de famille
- Sexe
- Date de naissance
- Ville natale
- Pays
- Numéro de téléphone
- Langue
- Courriel
- URL de l'image d'avatar pour les profils d'utilisateurs Braze
- Données Twitter
- Données Facebook

Toutes les valeurs de chaîne telles que le prénom, le nom de famille, le pays et la ville d'accueil sont limitées à 255 caractères. Les URL des images d'avatar sont limitées à 1024 caractères.

### Attributs utilisateur personnalisés

Au-delà des attributs ci-dessus, Braze vous permet également de définir des attributs personnalisés pour vos utilisateurs. Les types de données supportés pour les valeurs incluent `Date`, `Tableau`, `booléen`, `chaîne`, `nombre`, et `nombre flottant`. Les valeurs de chaîne de caractères ont une longueur maximale de 255 caractères.

```javascript
ReactAppboy.setCustomUserAttribute("attribute_key", "attribute_value", function(){
    // optionnel onResult callback
});
```

#### Annuler la définition d'un attribut personnalisé

```javascript
ReactAppboy.unsetCustomUserAttribute("attribute_key", function(){
    // callback onResult optionnel
});
```

## Achats de journalisation

<!-- Copied ios/android/analytics/logging purchases -->

Enregistrez vos achats dans l'application afin de pouvoir suivre vos revenus au fil du temps et à travers les sources de revenus. ainsi que segmenter vos utilisateurs par leur valeur à vie.

Braze prend en charge les achats dans plusieurs devises. Les achats que vous rapportez dans une devise autre que le dollar seront affichés dans le tableau de bord en USD en fonction du taux de change à la date à laquelle ils ont été déclarés.

```javascript
ReactAppboy.logPurchase(productId, prix, currencyCode, quantité, propriétés) ;
```

Par exemple :

```javascript
ReactAppboy.logPurchase("product_id", 9.99, "USD", 1, {
    key1: "value"
});
```

{% alert tip %}
Si vous passez une valeur de `10 USD` et une quantité de `3`, ceci enregistrera trois achats de 10 dollars pour un total de 30 dollars sur le profil de l'utilisateur. La quantité doit être inférieure ou égale à 100. Les valeurs d'achat peuvent être négatives.
{% endalert %}

### Clés réservées

The following keys are **reserved** and **cannot** be used as purchase properties:

- `Heure`
- `identifiant_produit`
- `Quantité`
- `nom_événement`
- `prix`
- `Devise`

[Aperçu de l'analyse]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/
[1]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/