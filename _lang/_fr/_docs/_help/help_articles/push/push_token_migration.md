---
nav_title: Migration des Push Tokens
article_title: Migration des Push Tokens
page_order: 1
page_type: Solution
description: "Cet article couvre la façon de migrer les jetons push afin que vous puissiez continuer à envoyer des messages push à vos utilisateurs après avoir basculé vers Braze."
channel: Pousser
---

# Migration des jetons push

Un jeton push est une clé unique, créé et assigné par Apple ou Google pour créer une connexion entre une application et un appareil iOS, Android ou web. La migration de jetons Push est l'importation de ces clés déjà générées dans la plate-forme de Braze.

Braze les clients qui envoyaient précédemment des notifications push, soit seuls, soit avec un fournisseur différent, ont souvent une liste d'utilisateurs avec des jetons push enregistrés.

Pour continuer à envoyer des messages push à ces utilisateurs pendant le processus d'intégration de Braze SDK, vous pouvez importer ces jetons dans Braze et cibler ces utilisateurs en utilisant l'outil de campagne de Brase.

{% comment %}
Ces campagnes devront être configurées avec des paires de valeurs clés appropriées pour s'assurer que la configuration de notification push existante du client reconnaîtra et affichera la charge utile de push que nous envoyons aux appareils des utilisateurs. Tandis que nous enregistrerons le nombre de pousses que nous envoyons, aucune donnée sur les taux d'ouverture ou les événements de conversion n'est tracée car cela nécessite que le SDK de Braze soit intégré.
{% endcomment %}

## Migration via API

Les jetons Push peuvent être téléchargés pour les utilisateurs identifiés ou pour les utilisateurs anonymes. Cela signifie que soit un `external_id` doit être présent, ou les utilisateurs anonymes doivent avoir le drapeau `push_token_import` défini à `true`.

Le `app_id` requis peut être trouvé dans la **Console développeur**, sous l'onglet **Paramètres API** dans la section **Identification**. Chaque application (iOS, Android, Web, etc.) a son propre `app_id` - assurez-vous d'utiliser l' `app_id` de la plateforme correcte.

#### Migration si un ID externe est présent
```json
"attributes" : [
  {
    "push_token_import" : false,
    "external_id": "external_id1",
    "country": "US",
    "language": "en",
    "YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
    "push_tokens": [
      {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
    ]
  }
]
```

{% alert note %}
Lors de l'importation de jetons push depuis d'autres systèmes, un `external_id` n'est pas toujours disponible. Pour maintenir la communication avec ces utilisateurs pendant votre transition vers Braze, vous pouvez importer les jetons hérités pour les utilisateurs anonymes sans fournir `external_id` en spécifiant `push_token_import` comme `true`.
{% endalert %}

#### Migration si l'ID externe n'est pas présent

Ces jetons peuvent être migrés en [les important avec notre API]({{site.baseurl}}/api/endpoints/user_data/#push-token-import).

Pour ce faire, utilisez le point de terminaison `utilisateurs/piste` et publiez les informations suivantes :

```json
"attributes" : [
  {
    "push_token_import" : vrai,
    "push_tokens": [
      { "app_id": "", "jeton": "", "device_id": "" }

  }
]
```

##### Exemple

```json
"attributes": [ 
  {
    "push_token_import" : true,
    "email": "braze.test1@testbraze. om",
    "country": "US",
    "language": "fr",
    "VOTRE_CLIENT_ATTRIBUTE": "VOTRE_VALEUR",
    "push_tokens": [
      {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
    ]
  },

  {
    "push_token_import" : true,
    "email": "braze. est2@testbraze. om",
    "country": "US",
    "language": "fr",
    "VOTRE_CUSTOM_ATTRIBUTE_1": "VOTRE_VALUE",
    "VOTRE_CUSTOM_ATTRIBUTE_2": "VOTRE VALEUR",
    "push_tokens": [
      {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}  
    ]
  }
]
```

En spécifiant `push_token_import` comme `true`:

* `external_id` et `braze_id` ne doit __pas ętre spécifié__
* L'objet d'attribut __doit__ contenir un jeton push
* Si le jeton existe déjà au Brésil, la requête est ignorée ; sinon Braze créera un profil d'utilisateur temporaire et anonyme pour chaque jeton pour vous permettre de continuer à envoyer un message à ces personnes

Après l'importation, chaque utilisateur lance la version brésilienne de votre application, Braze déplacera automatiquement son jeton push importé vers son profil utilisateur Braze et nettoie le profil temporaire.

Braze vérifiera une fois par mois pour trouver un profil anonyme avec le drapeau `push_token_import` qui n'a pas de jeton push_token_import . Si le profil anonyme n'a plus de jeton push, nous supprimerons le profil. Cependant, si le profil anonyme a encore un jeton de push, suggérant que l'utilisateur actuel doit encore se connecter à l'appareil avec ce jeton push, nous ne ferons rien.

### Jetons de push Web
Les jetons de push Web contiennent des champs supplémentaires que les autres plates-formes ne contiennent pas. Par conséquent, nous vous recommandons d'intégrer push et de permettre à votre base de jetons de se repeupler naturellement.

## Envoi de push avant l'intégration de Braze SDK (Android uniquement)

{% alert warning %}
Cette solution ne s'applique qu'aux utilisateurs Android. Les utilisateurs d'iOS ne recevront pas de push avec cette méthode. iOS ne nécessite pas ces étapes car il n'y a qu'un seul framework pour afficher push. Les notifications push seront affichées immédiatement tant que Braze a les jetons push et les certificats nécessaires.
{% endalert %}

Si vous trouvez que vous devez envoyer une notification push à vos utilisateurs avant que l'intégration Braze SDK soit terminée, vous pouvez utiliser des paires clé-valeur pour valider les notifications push.

Vous devez avoir un récepteur pour gérer et afficher les charges push. Pour avertir le destinataire de la charge utile push, ajoutez les paires clés nécessaires à la campagne push. Les valeurs de ces paires dépendent du partenaire de poussée spécifique que vous avez utilisé avant Brésil.

{% alert note %}
Pour certains fournisseurs de notification push, Braze devra aplanir les paires clé-valeur afin qu'ils puissent être correctement interprétés. Pour aplanir les paires de valeurs clés pour une application Android spécifique, contactez votre Customer Onboarding ou Success Manager.
{% endalert %}

_Dernière mise à jour le 1er juin 2021_

