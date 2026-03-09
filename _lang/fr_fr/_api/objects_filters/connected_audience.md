---
nav_title: "Objet et filtre Audience connectée"
article_title: Objet Audience connectée de l’API
page_order: 3
page_type: reference
description: "Cet article explique les différents composants de l’objet Audience connectée et les filtres qui le créent."

---

# Objet Audience connectée

> Un objet public connecté identifie l’audience de votre message. Par exemple, si vous utilisez des tableaux d'attributs personnalisés pour suivre toutes les catégories et émissions de télévision qu'un utilisateur a ajoutées à ses favoris, vous pouvez utiliser les audiences connectées pour envoyer automatiquement une notification push ou un e-mail à toute personne ayant ajouté une émission à ses favoris dès qu'un nouvel épisode est diffusé, sans avoir à configurer un segment pour chaque émission.

Cet objet est composé soit d'un seul filtre d'audience connectée, soit de plusieurs filtres d'audience connectée dans une expression logique utilisant des opérateurs `AND` ou `OR`.

**Exemple de filtre multiple :**

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

La combinaison de plusieurs filtres d'attributs personnalisés avec`AND`les`OR`opérateurs crée un filtre d'audience connecté.

### Filtre d’attribut personnalisé

Ce filtre vous permet de segmenter en fonction de l’attribut personnalisé d’un utilisateur. Ces filtres contiennent jusqu’à trois champs :

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) the name of the custom attribute to filter on,
      "comparison": (String) one of the allowed comparisons to make against the provided value,
      "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
    }
}
```

#### Comparaisons autorisées par type de données

Le type de données de l’attribut personnalisé détermine les comparaisons qui sont valides pour un filtre donné.

| Type d’attribut personnalisé | Comparaisons autorisées |
| ---------------------| --------------- |
| Chaîne de caractères | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist` |
| Tableau | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist` |
| Numérique | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Valeur booléenne | `equals`, `not_equal`, `exists`, `does_not_exist` |
| Date | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Mises en garde dans la comparaison des attributs

| Comparaison | Considérations supplémentaires |
| --- | --- |
| `value` | Le `value` n'est pas nécessaire lors de l'utilisation des comparaisons `exists` ou `does_not_exist`. `value` doit être une chaîne datetime ISO 8601 lors de l'utilisation des comparaisons `before` et `after`. |
|`matches_regex` | Lors de l’utilisation de la comparaison `matches_regex`, la valeur transmise doit être une chaîne de caractères. Pour en savoir plus sur l'utilisation des expressions régulières avec Braze, consultez [Expressions régulières]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze) et [Types de données d'attributs personnalisés]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}
```

```json
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
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Comparaisons autorisées :** `is`, `is_not`
- **Valeurs autorisées :** `opted_in`, `subscribed`, `unsubscribed`

### Filtre d’abonnement aux e-mails

Ce filtre vous permet de segmenter en fonction du statut d’abonnement aux e-mails d’un utilisateur.

#### Corps du filtre

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Comparaisons autorisées :** `is`, `is_not`
- **Valeurs autorisées :** `opted_in`, `subscribed`, `unsubscribed`

### Dernier filtre d’application utilisé

Ce filtre vous permet de segmenter en fonction de la dernière utilisation de l'application par l'utilisateur. Ces filtres contiennent deux champs :

#### Corps du filtre
```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **Comparaisons autorisées :** `after`, `before`
- **Valeurs autorisées :** datetime (chaîne ISO 8601)

### Considérations

Les audiences connectées ne peuvent pas filtrer les utilisateurs en fonction d'attributs par défaut, d'événements personnalisés, de segments ou d'événements d'engagement aux messages. Pour utiliser ces filtres, nous vous recommandons de les intégrer à un segment d'audience, puis de spécifier ce segment dans le`segment_id`paramètre pour [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters)l'[endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters). Lorsque vous utilisez d'autres endpoints, il est nécessaire d'ajouter le segment à la campagne déclenchée par l'API ou à Canvas dans le tableau de bord de Braze au préalable.
