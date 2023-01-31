---
nav_title: Connecteur Currents personnalisé
alias: /currents_connector/
hidden: true
---

# Connecteur Currents personnalisé du partenaire

## Sérialisation et format des données

Le format de données cible sera JSON sur HTTPS. Les événements seront regroupés en lots d’événements, dont la taille est configurable et envoyée à l’endpoint en tant que matrice JSON contenant tous les événements. Les lots seront envoyés au format suivant :

`{"events": [event1, event2, event3, etc...]}`

Il y aura un objet JSON de haut niveau avec les « événements » clés qui mappe à un tableau d’objets JSON supplémentaires, chacun représentant un seul événement.

Les exemples suivants concernent des événements _individuels_ (c.-à-d., qu’ils font partie du plus grand tableau d’objets JSON, avec chaque objet JSON représentant un seul événement dans le lot).

### Événements associés à la campagne

Voici quelques exemples de charges utiles d’événements pour divers événements, comme ils apparaîtraient si associés à une campagne :

```
// Clics des messages in-app : users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "Amérique/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Campagne de test",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Tester la variation de message",
    "platform": "android",
     "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

```
// Notification push envoyée : users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "Amérique/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Campagne de test",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Tester la variation de message",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

```
// Ouverture des e-mails : users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "Amérique/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Campagne de test",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Tester la variation de message",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh ; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, comme Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

```
// SMS livré : users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "Amérique/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Campagne de test",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Tester la variation de message",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Événements associés à Canvas

Voici quelques exemples de charges utiles d’événements pour divers événements, comme ils apparaîtraient si associés à un Canvas :
```
// Clics des messages in-app : users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "Amérique/Chicago"
  },
  "properties": {
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
// Notification push envoyée : users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "Amérique/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
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
// Ouverture des e-mails : users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "Amérique/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh ; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, comme Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

```
// SMS livré : users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "Amérique/Chicago"
  },
  "properties": {
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

Voici quelques exemples de charges utiles d’événements pour divers autres événements qui ne sont pas associés à des campagnes ou à des Canvas :

```
// Événement personnalisé : users.behaviors.CustomEvent
{
  "event_type": "users.behaviors.CustomEvent",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "Amérique/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "name": "custom nom de l’événement",
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "custom_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

```
// Événement d’achat : users.behaviors.Purchase
{
  "event_type": "users.behaviors.Purchase",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id"
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "Amérique/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "product_id": "1234",
    "price": 12.34,
    "currency": "AED,
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "purchase_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

```
// Démarrage de la session : users.behaviors.app.SessionStart
{
  "event_type": "users.behaviors.app.SessionStart",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "session_id": "b1234567-89ab-cdef-0123-456789abcdef"
  }
}
```

## Authentification

Si nécessaire, l’authentification sera effectuée en passant un jeton dans l’en-tête d’`autorisation`  HTTP, via le schéma d’autorisation `Bearer` (détenteur), comme indiqué dans [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). Cela est également automatiquement compatible avec tout schéma d’authentification personnalisé que nous pouvons choisir de mettre en œuvre à l’avenir, à partir du moment où l’utilisation de l’en-tête d’`autorisation` nous permettrait de passer à un schéma d’autorisation de paires clé-valeur personnalisées (uniques dans Braze) conformes à [RFC 7235](https://tools.ietf.org/html/rfc7235) (p. ex., la manière dont le programme d’authentification personnalisé AWS fonctionne) si nous le faisons à l’avenir.

Conformément à la RFC 6750, le jeton sera une valeur encodée Base64 d’au moins un caractère. (Il est évident que nous devons, toutefois, consulter avec nos partenaires et nos clients pour nous assurer qu’ils ne choisissent pas un incroyablement faible tokens.) Une anomalie notable de RFC 6750 est qu’il permet au jeton de contenir les caractères suivants, en plus des caractères Base64 normaux : '-', '.', '_' et '~'. Étant donné que le contenu exact du jeton ne fait absolument aucune différence pour aucun de nos systèmes, nous ne nous soucierons pas de savoir si nos partenaires décident d’inclure ces caractères dans leur jeton ou non.

Selon RFC 6750, l’en-tête sera construit en utilisant le format suivant :

`"Authorization: Bearer " + <token>`

Par exemple, si le jeton API est `0p3n5354m3==`, l’en-tête Autorisation ressemblera à ceci :

`Authorization: Bearer 0p3n5354m3==`

## Contrôle des versions

Toutes les demandes de nos connecteurs HTTP intégrables seront envoyées avec un en-tête personnalisé désignant la version de la demande Currents effectuée :

`Braze-Currents-Version: 1`

La version sera toujours 1 à moins que nous fassions des changements substantiels incompatibles avec le passé à la charge utile ou à la sémantique de la demande. Nous ne prévoyons pas d’augmenter ce nombre très souvent, le cas échéant. 

Les événements individuels suivront les mêmes règles d’évolution que nos schémas Avro existants. Cela signifie que les champs de chaque événement seront rétrocompatibles avec les versions antérieures des charges utiles de l’événement selon la définition Avro de la rétrocompatibilité, y compris les règles suivantes :

- Les champs d’événements spécifiques sont garantis de toujours avoir le même type de données dans le temps.
- Tous les nouveaux champs ajoutés à la charge utile au fil du temps doivent être considérés comme facultatifs par toutes les parties.
- Les champs obligatoires ne seront jamais supprimés.
  - Ce qui est considéré comme « requis » sera spécifié par la documentation que nous voulons probablement générer automatiquement de nos schémas Avro comme source centrale de vérité. Cela nous oblige à annoter les champs de schéma Avro avec certaines métadonnées et un script spécial qui peut lire les métadonnées pour générer la documentation.

## Gestion des erreurs et mécanisme de nouvelle tentative

En cas d’erreur, Braze mettra la demande en file d’attente et la réessaiera en fonction du code de retour HTTP reçu.

{% alert important %}
Si notre mécanisme de relance ne parvient pas à livrer des événements à leur endpoint pendant plus de 24 heures, il y aura une perte de données.
{% endalert %}

Les codes d’état HTTP suivants seront reconnus par notre client connecteur :
- **2XX** — Réussite
  - Les données d’événement ne seront pas renvoyées.<br><br>
- **5XX** — Erreur côté serveur
  - Les données d’événements seront renvoyées dans un modèle de délais exponentiel avec gigue. Si les données n’ont pas été envoyées avec succès dans les 24 heures, elles seront abandonnées.<br><br>
- **400** — Erreur côté client
  - Notre connecteur a envoyé au moins un événement malformé. Dans ce cas, les données d’événements seront divisées en lots de taille 1 et renvoyées. Tous les événements de ces lots de taille 1 qui reçoivent une réponse supplémentaire de HTTP 400 seront supprimés de façon permanente. Les partenaires et/ou les clients doivent être encouragés à nous faire savoir s’ils détectent que cela se produit de leur côté.<br><br>
- **401** (Non autorisé) ou **403** (Interdit)
  - Le connecteur a été configuré avec des informations d’identification non valides. La tâche du connecteur arrête l’envoi et sera marquée comme « Failed » (Échec). Les données d’événements seront renvoyées après un délai de 2 à 5 minutes (ceci est géré par le rebond de tâche Connect). Si ce problème n’est pas résolu par le client dans les 48 heures, les données de l’événement seront perdues.<br><br>
- **413** — Charge utile trop grande
  - Les données d’événements seront divisées en petits lots et renvoyées.<br><br>
- **429** — Trop de demandes
  - Indique la limitation du débit. Les données d’événements seront renvoyées dans un modèle de délais exponentiel avec gigue. Si les données n’ont pas été envoyées avec succès dans les 24 heures, elles seront abandonnées.