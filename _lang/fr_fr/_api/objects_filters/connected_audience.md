---
nav_title: "Objet et filtre Audience connectée"
article_title: Objet Audience connectée de l'API
page_order: 3
page_type: reference
description: "Cet article explique l'objet Audience connectée, son fonctionnement, ses cas d'utilisation et les différents filtres qui le composent."

---

# Objet Audience connectée

> Une audience connectée est un filtre d'audience dynamique que vous définissez directement dans votre requête API, ce qui vous permet de cibler les bons utilisateurs au moment de l'envoi sans avoir à créer ou gérer des segments dans le tableau de bord de Braze.

Au lieu de créer à l'avance un segment pour chaque combinaison d'audience possible, vous transmettez les critères de filtrage directement dans le paramètre `audience` de votre appel API. Braze évalue chaque utilisateur par rapport à ces critères en temps réel et délivre le message uniquement aux utilisateurs correspondants. Ainsi, une seule campagne, un seul Canvas ou une seule définition de message API peut servir un nombre illimité de variations d'audience, entièrement piloté par votre logique métier.

## Fonctionnement

1. Définissez votre message en créant une campagne ou un Canvas déclenchés par API dans le tableau de bord de Braze, ou définissez le contenu du message entièrement en ligne à l'aide des [objets de messagerie]({{site.baseurl}}/api/objects_filters/#messaging-objects) dans votre requête API. Utilisez les [propriétés de déclenchement]({{site.baseurl}}/api/objects_filters/trigger_properties_object/) ou le [contexte Canvas]({{site.baseurl}}/api/objects_filters/context_object/) pour la personnalisation dynamique.
2. Appelez un endpoint compatible et incluez le paramètre `audience` avec vos critères de filtrage. Vous pouvez filtrer sur les attributs personnalisés, le statut d'abonnement aux notifications push, le statut d'abonnement aux e-mails et la date de dernière utilisation de l'application.
3. Braze évalue les filtres au moment de l'envoi et délivre le message uniquement aux utilisateurs correspondant à vos critères.

{% alert tip %}
Un `campaign_id` n'est pas requis lorsque vous utilisez le paramètre `audience`. Les endpoints [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) et [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) vous permettent de définir le contenu du message en ligne sans campagne préalablement créée. Toutefois, si vous souhaitez suivre les indicateurs au niveau de la campagne (tels que les envois, les clics ou les rebonds) dans le tableau de bord, incluez un `campaign_id`.
{% endalert %}

Comme l'audience est définie par requête, vos systèmes back-end peuvent déclencher des messages contextuellement pertinents en réponse à n'importe quel événement métier (un changement de prix, une alerte météo, une mise à jour de score en direct) sans intervention dans le tableau de bord.

### Endpoints compatibles

Vous pouvez utiliser l'objet Audience connectée avec le paramètre `audience` sur les endpoints suivants :

- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)

## Cas d'utilisation

Utilisez les audiences connectées dans les scénarios où vos systèmes back-end détectent un événement et doivent notifier un ensemble d'utilisateurs déterminé dynamiquement :

| Catégorie | Exemple |
| --- | --- |
| Alertes météo | Un fournisseur de données météorologiques détecte un événement météorologique grave et envoie des notifications push aux utilisateurs dont l'attribut `preferred_city` correspond à la zone touchée. |
| Sports et événements en direct | Une application sportive envoie des mises à jour de scores en temps réel ou des alertes de match aux utilisateurs dont l'attribut `favorite_team` correspond à l'une des équipes en jeu. |
| Contenu et divertissement | Un service de streaming notifie les utilisateurs dont le tableau `favorite_shows` inclut le titre d'une série dès qu'un nouvel épisode est disponible. |
| E-commerce | Un détaillant en ligne envoie des alertes de baisse de prix ou de retour en stock aux utilisateurs dont le tableau `wishlisted_products` inclut l'ID du produit concerné. |
| Voyage | Une application de voyage envoie des notifications de retard de vol aux utilisateurs dont l'attribut `booked_flight` correspond au numéro de vol affecté. |
| Services financiers | Une plateforme de trading alerte les utilisateurs dont le tableau `watchlist` inclut un symbole boursier ayant franchi un seuil de prix. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Dans chaque cas, une seule campagne ou définition de message API gère toutes les variations. Votre back-end détermine les valeurs de filtrage et les transmet dans la requête API, ce qui vous évite de créer un segment ou une campagne distinct(e) pour chaque produit, émission, équipe ou emplacement.

## Exemple de requête

L'exemple suivant utilise l'endpoint [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) pour cibler les utilisateurs ayant ajouté une émission spécifique à leurs favoris et ayant accepté les notifications push :

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_shows",
          "comparison": "includes_value",
          "value": "Example Show"
        }
      },
      {
        "push_subscription_status": {
          "comparison": "is",
          "value": "opted_in"
        }
      }
    ]
  },
  "trigger_properties": {
    "show_title": "Example Show",
    "episode_title": "Season 3, Episode 1",
    "deep_link": "https://example.com/shows/example-show/s3e1"
  },
  "broadcast": false
}
```

## Corps de l'objet

L'objet Audience connectée est composé soit d'un seul filtre d'audience connectée, soit de plusieurs filtres d'audience connectée combinés à l'aide des opérateurs `AND` et `OR`.

**Exemple avec plusieurs filtres :**

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

## Filtres d'audience connectée

Combinez plusieurs filtres avec les opérateurs `AND` et `OR` pour créer un filtre d'audience connectée.

### Filtre d'attribut personnalisé

Ce filtre vous permet de segmenter en fonction d'un attribut personnalisé de l'utilisateur. Il contient jusqu'à trois champs :

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

Le type de données de l'attribut personnalisé détermine les comparaisons valides pour un filtre donné.

| Type d'attribut personnalisé | Comparaisons autorisées |
| ---------------------| --------------- |
| Chaîne de caractères | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist` |
| Tableau | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist` |
| Numérique | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Valeur booléenne | `equals`, `not_equal`, `exists`, `does_not_exist` |
| Date | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Points d'attention sur les comparaisons d'attributs

| Comparaison | Remarques |
| --- | --- |
| `value` | Le champ `value` n'est pas requis avec les comparaisons `exists` ou `does_not_exist`. `value` doit être une chaîne datetime ISO 8601 avec les comparaisons `before` et `after`. |
|`matches_regex` | Avec la comparaison `matches_regex`, la valeur transmise doit être une chaîne de caractères. Pour en savoir plus sur l'utilisation des expressions régulières avec Braze, consultez [Expressions régulières]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze) et [Types de données d'attributs personnalisés]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Exemple d'attribut personnalisé

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
### Filtre d'abonnement aux notifications push

Ce filtre vous permet de segmenter en fonction du statut d'abonnement aux notifications push d'un utilisateur.

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

- **Comparaisons autorisées :** `is`, `is_not`
- **Valeurs autorisées :** `opted_in`, `subscribed`, `unsubscribed`

### Filtre d'abonnement aux e-mails

Ce filtre vous permet de segmenter en fonction du statut d'abonnement aux e-mails d'un utilisateur.

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

- **Comparaisons autorisées :** `is`, `is_not`
- **Valeurs autorisées :** `opted_in`, `subscribed`, `unsubscribed`

### Filtre de dernière utilisation de l'application

Ce filtre vous permet de segmenter en fonction de la dernière utilisation de l'application par l'utilisateur. Il contient deux champs :

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

- **Comparaisons autorisées :** `after`, `before`
- **Valeurs autorisées :** datetime (chaîne ISO 8601)

### Considérations

Les audiences connectées ne permettent pas de filtrer les utilisateurs en fonction d'attributs par défaut, d'événements personnalisés, de segments ou d'événements d'engagement liés aux messages. Pour utiliser ces filtres, nous vous recommandons de les intégrer dans un segment d'audience, puis de spécifier ce segment dans le paramètre `segment_id` de l'[endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters). Pour les autres endpoints, vous devrez d'abord ajouter le segment à la campagne déclenchée par l'API ou au Canvas dans le tableau de bord de Braze.