---
nav_title: Connecteur Currents personnalisé
alias: /currents_connector/
hidden: true
---

# connecteur Currents personnalisé Partner

## Sérialisation et format des données

Le format de données cible est JSON sur HTTPS. Les événements seront regroupés par lots de 100 événements par défaut, et envoyés à l'endpoint sous la forme d'un tableau JSON contenant tous les événements. Les lots seront envoyés dans le format suivant :

`{"events": [event1, event2, event3, etc...]}`

Il y aura un objet JSON de niveau supérieur avec les « événements » clés qui correspondent à un tableau d'autres objets JSON, chacun représentant un événement unique.

Les exemples suivants concernent des événements _individuels_ (tels qu'ils feraient partie du tableau plus large d'objets JSON, chaque objet JSON représentant un événement unique dans le lot).

### Événements liés à la campagne

Voici quelques exemples de charges utiles pour différents événements, telles qu'elles apparaîtraient s'ils étaient associés à une campagne :

```
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
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
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

```
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

```
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Événements associés à CANVAS

Voici quelques exemples de charges utiles d'événements pour différents événements, telles qu'elles apparaîtraient si elles étaient associées à un Canvas :

```
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
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
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
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
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

```
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
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

Voici quelques exemples de charges utiles d'événements pour divers autres événements qui ne sont associés ni à des campagnes ni à des Canvases :

```
// Custom Event: users.behaviors.CustomEvent
{
  "event_type": "users.behaviors.CustomEvent",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "name": "custom event name",
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
// Purchase Event: users.behaviors.Purchase
{
  "event_type": "users.behaviors.Purchase",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id"
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
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
// Session Start: users.behaviors.app.SessionStart
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
    "device_model": "iPhone 7 Plus",
    "session_id": "b1234567-89ab-cdef-0123-456789abcdef"
  }
}
```

## Authentification

Si nécessaire, l'authentification est réalisée en transmettant un jeton dans l'en-tête HTTP `Authorization`, via le schéma d'autorisation `Bearer`, comme spécifié dans la [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). À l'avenir, Braze pourra choisir d'utiliser l'en-tête `Authorization` pour mettre en œuvre un schéma d'autorisation par paire clé-valeur personnalisé (unique à Braze) conforme à la [RFC 7235](https://tools.ietf.org/html/rfc7235) (c'est ainsi que fonctionne, par exemple, le schéma d'authentification personnalisé d'AWS).

Conformément à la RFC 6750, le jeton doit être une valeur codée en Base64 d'au moins un caractère. Une particularité notable du document RFC 6750 est qu'il permet au jeton de contenir les caractères suivants en plus des caractères Base64 normaux : '-', ' . ',' _ 'et '~'. Les partenaires et les clients sont libres d'inclure ou non ces caractères dans leur jeton. Notez que les clients doivent fournir ce jeton sous forme de Base64 ; Braze n'effectuera pas cet encodage de notre côté.

Conformément à la RFC 6750, l'en-tête, s'il est présent, sera construit selon le format suivant :

`"Authorization: Bearer " + <token>`

Ainsi, par exemple, si le jeton d'API est`0p3n5354m3==`, l'en-tête Authorization ressemblera à ceci :

`Authorization: Bearer 0p3n5354m3==`

## Versionnage

Toutes les requêtes provenant de nos connecteurs HTTP intégrables seront envoyées avec un en-tête personnalisé désignant la version de la requête Currents en cours :

`Braze-Currents-Version: 1`

La version sera toujours `1`, à moins que nous n'apportions des modifications gravement incompatibles avec le passé à la charge utile ou à la sémantique de la demande. Nous prévoyons d'augmenter ce chiffre rarement, voire jamais.

Les événements individuels suivront les mêmes règles d'évolution que nos schémas S3 Avro existants pour l'exportation des données sur les courants. En d'autres termes, la rétrocompatibilité des champs de chaque événement avec les versions précédentes des charges utiles de l'événement sera garantie conformément à la définition de rétrocompatibilité d'Avro, y compris les règles suivantes :

- Il est garanti que les champs d'événements spécifiques auront toujours le même type de données au fil du temps.
- Tous les nouveaux champs ajoutés à la charge utile au fil du temps doivent être considérés comme facultatifs par toutes les parties.
- Les champs obligatoires ne seront jamais supprimés.

## Gestion des erreurs et mécanisme de nouvelle tentative

En cas d'erreur, Braze mettra la requête en file d'attente et réessaiera en fonction du code de retour HTTP reçu. Tout code d'erreur HTTP non répertorié ci-dessous sera traité comme une erreur HTTP 5XX.

{% alert important %}
Si notre mécanisme de nouvelle tentative ne parvient pas à transmettre les événements à leur endpoint pendant plus de 24 heures, il y aura une perte de données.
{% endalert %}

Les codes d'état HTTP suivants seront reconnus par notre client de connecteur :
- **2XX — Succès**
  - Les données relatives à l'événement ne seront pas renvoyées.<br><br>
- **5XX** — Erreur côté serveur
  - Les données des événements seront renvoyées selon un schéma de délais exponentiels avec variation aléatoire. Si les données ne sont pas envoyées avec succès dans les 24 heures, elles seront supprimées.<br><br>
- **400** — Erreur côté client
  - Notre connecteur a d'une manière ou d'une autre envoyé au moins un événement mal formé. Dans ce cas, les données d'événement seront divisées en lots de taille 1 et renvoyées. Tous les événements de ces lots de taille 1 qui reçoivent une réponse HTTP 400 supplémentaire seront définitivement supprimés. Les partenaires et/ou les clients sont invités à nous informer s'ils détectent ce phénomène chez eux.<br><br>
- **401** (non autorisé), **403** (interdit), **404**
  - Le connecteur a été configuré avec des informations d'identification non valides. Les données relatives à l'événement seront envoyées à nouveau après un délai compris entre 2 et 5 minutes. Si ce problème n'est pas résolu par le client dans les 48 heures, les données relatives à l'événement seront supprimées.<br><br>
- **413** — Charge utile trop importante
  - Les données relatives à l'événement seront divisées en lots plus petits et renvoyées.<br><br>
- **429** — Trop de requêtes
  - Indique la limite de débit. Les données des événements seront renvoyées selon un schéma de délais exponentiels avec variation aléatoire. Si les données ne sont pas envoyées avec succès dans les 24 heures, elles seront supprimées.