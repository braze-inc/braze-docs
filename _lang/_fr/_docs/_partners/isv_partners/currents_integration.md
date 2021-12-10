---
nav_title: Connecteur de courants personnalisés
alias: /connecteur_courants/
hidden: vrai
---

# Connecteur de courants personnalisés des partenaires

## Sérialisation et format de données

Le format de données cible sera JSON via HTTPS. Les événements seront regroupés en lots d'événements, dont la taille est configurable, et envoyé à l'extrémité en tant que tableau JSON contenant tous les événements. Les lots seront envoyés dans le format suivant :

`{"événements": [event1, event2, event3, etc...]}`

par ex. Il y aura un objet JSON de niveau supérieur avec les "événements" clés qui correspond à un tableau d'autres objets JSON, chacun représentant un seul événement.

Les exemples ci-dessous sont pour _événements individuels_ (i.e. ils faisaient juste partie du plus grand tableau d'objets JSON tel que décrit ci-dessus, avec chaque objet JSON représentant un seul événement dans le lot).

### Événements associés à la campagne

Voici quelques exemples de payloads d'événements pour divers événements, comme ils apparaîtraient si ils étaient associés à une campagne:

```
// Click Message In-App : users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage. lick",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "temps": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "fuseau horaire": "Amérique/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Campagne de test",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "platform": "android",
     "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

```
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification. fin",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "temps": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "fuseau horaire": "Amérique/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "plate-forme": "ios",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Campagne de test",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

```
// Courriel Open: users.messages.email.Open
{
  "event_type": "users.messages.email. pen",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "propriétés": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Campagne de test",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "email_address": "test@test. om",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5. (Macintosh ; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, comme Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

```
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms. elivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "propriétés": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Campagne de test",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Événements associés à des toiles

Voici quelques exemples de payloads d'événements pour divers événements, comme ils apparaîtraient s'ils étaient associés à un Canvas:
```
// Click Message In-App : users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage. lick",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "fuseau horaire": "Amérique/Chicago"
  },
  "propriétés": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "platform": "android",
    "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

```
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification. fin",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "temps": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "fuseau horaire": "Amérique/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "plate-forme": "ios",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

```
// Courriel Open: users.messages.email.Open
{
  "event_type": "users.messages.email. pen",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "propriétés": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "email_address": "test@test. om",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5. (Macintosh ; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, comme Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

```
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms. elivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "temps": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "fuseau horaire": "Amérique/Chicago"
  },
  "propriétés": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Autres événements

Voici quelques exemples de charges utiles pour divers autres événements qui ne sont associés ni à des campagnes ni à des Canvasses :

```
// Événement personnalisé: users.behaviors.CustomEvent
{
  "event_type": "users.behaviors. ustomEvent",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id"
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "fuseau horaire": "Amérique/Chicago"
  },
  "propriétés": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "plate-forme": "ios",
    "os_version": "iOS 10. .1",
    "device_model": "iPhone 7 Plus",
    "name": "nom de l'événement personnalisé",
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "custom_properties": {
      "string property name": "a",
      "nombre nom de la propriété": 1,
      "nom de la propriété liste" : ["a", "b"]
    }
  }
}
```

```
// Événement d'achat: users.behaviors.Purchase
{
  "event_type": "users.behaviors. urchase",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id"
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "fuseau horaire": "Amérique/Chicago"
  },
  "propriétés": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "plate-forme": "ios",
    "os_version": "iOS 10. .1",
    "device_model": "iPhone 7 Plus",
    "product_id": "1234",
    "prix": 12. 4,
    "currency": "AED,
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": vrai,
    "purchase_properties": {
      "string property name": "a",
      "nombre nom de la propriété": 1,
      "nom de la propriété liste" : ["a", "b"]
    }
  }
}
```

```
// Début de la session: users.behaviors.app.SessionStart
{
  "event_type": "users.behaviors.app. essionStart",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210"
  },
  "propriétés": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "plate-forme": "ios",
    "os_version": "iOS 10. .1",
    "device_model": "iPhone 7 Plus",
    "session_id": "b1234567-89ab-cdef-0123-456789abcdef"
  }
}
```

## Authentification

Si nécessaire, l'authentification sera effectuée en passant un jeton dans l'en-tête HTTP `Authorization` , via le schéma d'autorisation `Bearer` tel que spécifié dans [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). Ceci est également automatiquement compatible avec n'importe quel schéma d'authentification personnalisé que nous pourrions choisir d'implémenter dans le futur. car l'utilisation de l'en-tête `Authorization` nous permettrait de passer à un schéma d'autorisation par paire personnalisée (unique au Brésil) conforme à la [RFC 7235](https://tools.ietf.org/html/rfc7235) (qui est comme e. Le système d'authentification personnalisée d'AWS fonctionne) si nous le choisissons dans le futur.

Conformément à la RFC 6750, le jeton sera une valeur encodée en Base64 d'au moins un caractère. (Il est évident que nous devons examiner nos partenaires et nos clients afin de savoir qu’ils sont peu susceptibles de choisir des jetons incroyablement faibles). Une curiosité notable de la RFC 6750 est qu'elle permet au jeton de contenir les caractères suivants en plus des caractères normaux Base64 : '-', '. , '_', et '~'. Puisque le contenu exact du jeton ne fait aucune différence pour aucun de nos systèmes, nous ne nous soucierons pas si nos partenaires décident d'inclure ces caractères dans leur jeton ou non.

Par RFC 6750, l'en-tête sera construit en utilisant le format suivant :

`"Authorization: Bearer " + <token>`

Ainsi, par exemple, si le jeton de l'API est `0p3n5354m3==`, l'en-tête d'autorisation ressemblera à ceci :

`Autorisation : Bearer 0p3n5354m3==`

## Versioning

Toutes les requêtes de nos Connecteurs HTTP Intégrables seront envoyées avec un en-tête personnalisé désignant la version de la demande de courant en cours :

`Version actuelle: 1`

La version sera toujours 1 à moins que nous ne fassions des changements sévèrement incompatibles avec la charge utile de la requête ou la sémantique. Nous ne nous attendons pas à incrémenter ce nombre très souvent, si jamais.

Les événements individuels suivront les mêmes règles d'évolution que nos schémas Avro existants. C'est-à-dire que les champs de chaque événement seront garantis d'être rétrocompatibles avec les versions antérieures de l'événement, selon la définition Avro de la compatibilité ascendante, y compris les règles suivantes :

- Des champs d'événements spécifiques sont garantis d'avoir toujours le même type de données au fil du temps.
- Tous les nouveaux champs qui sont ajoutés à la charge utile au fil du temps doivent être considérés comme facultatifs par toutes les parties.
- Les champs obligatoires ne seront jamais supprimés.
  - Ce qui est considéré comme "obligatoire" sera spécifié par la documentation que nous allons probablement vouloir générer automatiquement à partir de nos schémas Avro la source centrale de la vérité. Cela nous demandera d'annoter les champs du schéma Avro avec quelques métadonnées, et un script spécial qui peut lire ces métadonnées pour générer la documentation.

## Gestion des erreurs et réessayez le mécanisme

En cas d'erreur, Braze va mettre en file d'attente et réessayer la requête en se basant sur le code de retour HTTP reçu.

{% alert important %}
Si notre mécanisme de réessai ne parvient pas à livrer les événements à leur point de terminaison pendant plus de 24 heures, il y aura perte de données.
{% endalert %}

Les codes de statut HTTP suivants seront reconnus par notre client connecteur:
- __2XX__ – Réussite
  - Les données de l'événement ne seront pas renvoyées.<br><br>
- __5XX__ — Serverside error
  - Les données d'événement seront ré-envoyées dans un motif de backoff exponentiel avec jitter. Si les données ne sont pas envoyées avec succès dans les 24 heures, elles seront supprimées.<br><br>
- __400__ – Erreur côté client
  - Notre connecteur a envoyé au moins un événement malformé. Si cela se produit, les données de l'événement seront divisées en lots de taille 1 et ré-envoyées. Tous les événements de ces lots de taille 1 qui reçoivent une réponse HTTP 400 supplémentaire seront abandonnés de façon permanente. Les partenaires et/ou les clients devraient être encouragés à nous faire savoir s'ils détectent que cela se produit à leur fin.<br><br>
- __401__ (non autorisé) ou __403__ (interdit)
  - Le connecteur a été configuré avec des identifiants invalides. La tâche du connecteur arrêtera l'envoi et sera marquée comme "Échec". Les données d'événement seront renvoyées après un délai de 2 à 5 minutes (ceci est géré par le redémarrage de la tâche Connecter). Si ce problème n'est pas résolu par le client dans les 48 heures, les données de l'événement seront supprimées.<br><br>
- __413__ – Charge trop grande
  - Les données d'événement seront divisées en petits lots et ré-envoyées.<br><br>
- __429__ – Trop de requêtes
  - Indique la limitation de débit. Les données d'événement seront ré-envoyées dans un motif de backoff exponentiel avec jitter. Si les données ne sont pas envoyées avec succès dans les 24 heures, elles seront supprimées.