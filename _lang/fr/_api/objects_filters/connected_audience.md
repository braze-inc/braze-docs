---
nav_title: "Objet et filtre d’audience connectée"
article_title: Objet d’audience connectée de l’API
page_order: 3
page_type: reference
description: "Cet article explique les différents composants de l’objet d’audience connectée et les filtres qui le créent."

---

# Spécification de l’objet d’audience connectée

Un objet d’audience connectée est un sélecteur qui identifie l’audience à laquelle envoyer le message. Il est composé d’un seul filtre d’audience connectée ou de plusieurs filtres d’audience connectée dans une expression logique à l’aide des opérateurs `AND` ou `OR`.

Exemple de filtre multiple :

```json
{
  "AND":
    [
      Connected Audience Filter,
      {
        "OR" :
          [
            Connected Audience Filter,
            Connected Audience Filter
          ]
      },
      Connected Audience Filter
    ]
}
```

## Filtres d’audience connectée

L’association de plusieurs filtres d’attributs personnalisés crée un filtre d’audience connectée, qui crée lui-même un filtre d’audience connectée lorsqu’il est combiné avec les opérateurs `AND` et `OR`.

### Filtre d’attribut personnalisé

Ce filtre vous permet de segmenter en fonction de l’attribut personnalisé d’un utilisateur. Ces filtres contiennent jusqu’à trois champs :

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (string) le nom de l’attribut personnalisé sur lequel filtrer,
      "comparison": (string) une des comparaisons autorisées à réaliser par rapport à la valeur fournie,
      "value": (String, Numeric, Boolean) la valeur devant être comparée en utilisant la comparaison fournie
    }
}
```

#### Comparaisons autorisées par type de données

Le type de données de l’attribut personnalisé détermine les comparaisons qui sont valides pour un filtre donné.

| Type d’attribut personnalisé | Comparaisons autorisées |
| ---------------------| --------------- |
| String | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist` |
| Array | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist` |
| Numeric | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Boolean | `equals`, `does_not_equal`, `exists`, `does_not_exist` |
| Time | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` | 
{: .reset-td-br-1 .reset-td-br-2}

#### Mises en garde dans la comparaison des attributs

| Comparaison | Considérations supplémentaires |
| --- | --- |
| `value` | La `value` n’est pas nécessaire lors de l’utilisation des comparaisons `exists` ou `does_not_exist`. `value` doit être une chaîne de caractères ISO 8601 DateHeure lors de l’utilisation des comparaisons `before` et `after`.
|`matches_regex` | Lors de l’utilisation de la comparaison `matches_regex`, la valeur transmise doit être une chaîne de caractères. Pour en savoir plus sur l’utilisation des expressions régulières avec Braze, consultez notre documentation sur les [expressions régulières]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze) et les [types de données]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types) des attributs personnalisés. |
{: .reset-td-br-1 .reset-td-br-2}

#### Exemple d’attribut personnalisé

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}

{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}

{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```
### Filtre d’abonnement aux notifications push

Ce filtre vous permet de segmenter en fonction du statut d’abonnement aux notifications push d’un utilisateur.

#### Corps du filtre

```json
{
  "push_subscription_status":
  {
    "comparison": (string) une des comparaisons suivantes autorisées,
    "value": (String) une des valeurs autorisées suivantes
  }
}
```

- **Comparaisons autorisées : **[`Retrait en magasin`]`is`, `is_not`
- **Valeurs autorisées : **[`Retrait en magasin`]`opted_in`, `subscribed`, `unsubscribed`

### Filtre d’abonnement aux e-mails

Ce filtre vous permet de segmenter en fonction du statut d’abonnement aux e-mails d’un utilisateur.

#### Corps du filtre

```json
{
  "email_subscription_status":
  {
    "comparison": (string) une des comparaisons suivantes autorisées,
    "value": (String) une des valeurs autorisées suivantes
  }
}
```

- **Comparaisons autorisées : **[`Retrait en magasin`]`is`, `is_not`
- **Valeurs autorisées : **[`Retrait en magasin`]`opted_in`, `subscribed`, `unsubscribed`

### Dernier filtre d’application utilisé

Ce filtre vous permet de segmenter en fonction du moment où l’utilisateur a utilisé l’application pour la dernière fois. Ces filtres contiennent deux champs :

#### Corps du filtre
```json
{
  "last_used_app":
  {
    "comparison": (string) une des comparaisons autorisées listées,
    "value": (String) la valeur devant être comparée en utilisant la comparaison fournie
  }
}
```

- **Comparaisons autorisées : **[`Retrait en magasin`]`after`, `before`
- **Valeurs autorisées :** DateTime (chaîne de caractères ISO 8601)

