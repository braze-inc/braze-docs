---
nav_title: "Filtre public connecté & objet"
article_title: API Connected Audience Object
page_order: 3
page_type: Référence
description: "Cet article explique les différents composants de l'objet public connecté et des filtres qui le créent."
---

# Spécification de l'objet public connecté

Un objet public connecté est un sélecteur qui identifie le public auquel envoyer le message. Il est composé soit d'un seul Filtre d'Audience Connecté soit de plusieurs Filtres d'Audience Connectée dans une expression logique utilisant soit les opérateurs `ET` ou `OU`.

Exemple de filtre multiple:

```json
{
  "AND":
    [
      Filtre public connecté,
      {
        "OU" :
          [
            Filtre public connecté,
            Filtre public connecté
          ]
      },
      Filtre Audience Connecté
    ]
}
```

## Filtres d'audience connectés

La combinaison de plusieurs filtres d'attributs personnalisés créera un filtre d'audience connecté, qui créera un filtre d'audience connecté lorsqu'il sera combiné avec les opérateurs `ET` et `OU`.

### Filtre d'attribut personnalisé

Ce filtre vous permet de segmenter en fonction de l'attribut personnalisé d'un utilisateur. Ces filtres contiennent jusqu'à trois champs :

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) le nom de l'attribut personnalisé sur lequel filtrer,
      "comparaison": (String) une des comparaisons autorisées à faire par rapport à la valeur fournie,
      "valeur": (String, Numérique, Booléen) la valeur à comparer en utilisant la comparaison fournie
    }
}
```

Le type de l'attribut personnalisé détermine les comparaisons qui sont valides pour un filtre donné.

| Type d'attribut personnalisé | Comparaisons autorisées                                                                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Chaîne de caractères         | `est égal à`, `not_equal`, `matches_regex`, `does_not_match_regex`, `existe`, `does _not_exist`                                                                                |
| Tableau                      | `includes_value`, `does_not_include_value`, `existe`, `does _not_exist`                                                                                                        |
| Numeric                      | `est égal à`, `not_equal`, `plus grand que`, `plus grand_than_or_equal_to`, `moins_than`, `less_than_or_equal_to`, `existe`, `n'existe_pas_existe`                             |
| Boolean                      | `est égal à`, `ne fait _not_equal`, `existe`, `ne fait pas_not_exist`                                                                                                          |
| Date et heure                | `less_than_x_days_ago`, `grandeur_than_x_days_ago`, `less_than_x_days_in_the_future`, `supérieur_than_x_days_in_the_future`, `après`, `avant`, `existe`, `n'existe_pas_existe` |
{: .reset-td-br-1 .reset-td-br-2}

#### Avertissements de comparaison d'attributs

| `valeur` - La valeur `` n'est pas demandée lors de l'utilisation de la `existe` ou `n_not_exist` comparaisons. `la valeur` doit ętre une chaîne de caractères ISO 8601 DateTime lors de l'utilisation des `avant` et `aprčs` comparaisons.<br><br>`matches_regex` - Lors de l'utilisation de la `matches_regex` comparaison, la valeur passée doit être une chaîne. Pour en savoir plus sur l'utilisation d'expressions régulières avec Braze, consultez notre documentation sur [Regex]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze) et les attributs personnalisés [types de données]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types). |
{: .reset-td-br-1}

#### Exemple d'attribut personnalisé

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparaison": "égal",
      "value": "blue"
    }
}

{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparaison": "includes_valeur",
    "value": "pizza"
  }


{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparaison": "less_than_x_days_ago",
    "value": 2
  }
}
```
### Filtre d'abonnement Push

Ce filtre vous permet de segmenter en fonction du statut d'abonnement à un utilisateur.

#### Filtrer le corps

```json
{
  "push_subscription_status":
  {
    "comparison": (String) l'une des deux comparaisons autorisées listées ci-dessous,
    "valeur": (chaîne de caractères) l'une des trois valeurs autorisées énumérées ci-dessous
  }
}
```

| Comparaisons autorisées | Valeurs autorisées                |
| ----------------------- | --------------------------------- |
| `est`, `is_not`         | `opted_in`, `abonné`, `désabonné` |
{: .reset-td-br-1 .reset-td-br-2}

### Filtre d'abonnement aux emails

Ce filtre vous permet de segmenter en fonction du statut d'abonnement à un utilisateur.

#### Filtrer le corps

```json
{
  "email_subscription_status":
  {
    "comparison": (String) l'une des deux comparaisons autorisées listées ci-dessous,
    "valeur": (chaîne de caractères) l'une des trois valeurs autorisées énumérées ci-dessous
  }
}
```

| Comparaisons autorisées | Valeurs autorisées                |
| ----------------------- | --------------------------------- |
| `est`, `is_not`         | `opted_in`, `abonné`, `désabonné` |
{: .reset-td-br-1 .reset-td-br-2}

### Dernier filtre d'application utilisé

Ce filtre vous permet de segmenter en fonction du moment où l'utilisateur a utilisé l'application pour la dernière fois. Ces filtres contiennent deux champs :

#### Filtrer le corps
```json
{
  "last_used_app":
  {
    "comparison": (String) une des comparaisons autorisées listées ci-dessous,
    "valeur": (String) la valeur à comparer en utilisant la comparaison fournie
  }
}
```

| Comparaisons autorisées | Valeurs autorisées         |
| ----------------------- | -------------------------- |
| `après`, `avant`        | DateTime (chaîne ISO 8601) |
{: .reset-td-br-1 .reset-td-br-2}
