---
nav_title: DOTS.ECO
article_title: DOTS.ECO
description: "Cet article de référence décrit l'intégration de Braze et de DOTS.ECO."
alias: /partners/dots.eco/
page_type: partner
search_tag: Partner
---

# DOTS.ECO

> [DOTS.ECO](https://dots.eco) vous permet de récompenser les utilisateurs qui ont un impact environnemental réel grâce à des certificats numériques traçables. Chaque certificat peut inclure des métadonnées telles qu'une URL de certificat et une URL d'image partageables, afin que les utilisateurs puissent voir (et revoir) leur preuve d'impact.

_Cette intégration est maintenue par DOTS.ECO._

## À propos de cette intégration

Braze et DOTS.ECO connectent les parcours d'engagement client à des récompenses d'impact dans le monde réel. À partir d'une étape de Braze Canvas ou d'une campagne, vous pouvez déclencher une demande de création de certificat DOTS.ECO à l'aide de Connected Content. DOTS.ECO renvoie des métadonnées de certificat (telles que `certificate_url` et `certificate_image_url`) que vous pouvez stocker sur le profil utilisateur en tant qu'attributs personnalisés et réutiliser sur des canaux tels que les messages in-app, les notifications push et les messages in-app.

## Cas d’utilisation

- Déclenchez un certificat d'impact lorsqu'un utilisateur réalise un événement clé (achat, achèvement d'un niveau, abonnement, recommandation).
- Affichez une image de certificat personnalisé dans un message in-app après la réussite de l'étape Contenu connecté.
- Ajoutez une carte de contenu "Voir votre certificat" avec l'URL du certificat pour un accès ultérieur.
- Stockez les métadonnées des certificats (telles que `certificate_url`, `certificate_image_url`, `certificate_header`, et `greeting`) en tant qu'attributs personnalisés pour les réutiliser dans des envois de messages ultérieurs.
- Attribuez des certificats à l'aide d'un ID d'utilisateur distant afin que les utilisateurs puissent réclamer et visualiser leur impact ultérieurement.
- Effectuez des tests A/B sur les messages d'impact (différentes copies/images) tout en conservant le même flux de mise à jour de l'utilisateur DOTS.ECO.


## Conditions préalables

Avant de commencer, vous devez disposer des éléments suivants :

| Prérequis | Description |
|---|---|
| DOTS.ECO compte | DOTS.ECO l'accès au compte. |
| DOTS.ECO titres de compétences | La demande présentée dans cet article nécessite un jeton d'app DOTS.ECO, une clé API et un ID d'attribution. Pour les récupérer, contactez votre gestionnaire de la satisfaction client DOTS.ECO. |
| Clé d'API REST Braze | Une clé API Braze REST avec des autorisations `users.track`. Créez cette clé dans le tableau de bord de Braze sous **Paramètres** > **Clés API**. |
| Endpoint REST Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration DOTS.ECO

### Étape 1 : Créez un canvas et ajoutez une étape de mise à jour de l'utilisateur.

Dans le tableau de bord de Braze, créez un nouveau Canvas qui se déclenche lorsqu'un utilisateur réalise un événement clé (tel qu'un achat, un abonnement ou un jalon).

Ajoutez une étape de mise à jour de l'utilisateur juste après l'étape d'entrée. Cette étape servira à appeler l'API DOTS.ECO via le contenu connecté et à stocker les données de certificat renvoyées dans le profil utilisateur.

Utilisez cette étape pour appeler l'API DOTS.ECO via le contenu connecté et stocker les données de certificat renvoyées sur le profil utilisateur.

### Étape 2 : Composez du JSON avancé : Faites une demande POST à DOTS.ECO en utilisant le contenu connecté

À l'étape de la **mise à jour de l'utilisateur**, passez à l'**éditeur JSON avancé** et utilisez le contenu connecté pour effectuer une demande POST à l'API du certificat DOTS.ECO.

Utilisez l'étiquette `capture` et une demande de contenu connecté pour appeler l'endpoint de certificat de DOTS.ECO. Enregistrez ensuite la réponse dans le profil utilisateur en tant qu'attributs personnalisés.

**Exemple de contenu connecté et de mise à jour par l'utilisateur**  
{% raw %}
```  
{% capture post_body %} 
{  
  "remote_user_email": "{{${email_address} | default: 'braze+nadav@dots.eco'}}",  
  "app_token": "YOUR_DOTS.ECO_APP_TOKEN",  
  "impact_qty": 1,  
  "remote_user_id": "{{${user_id} | default: ${braze_id}}}",  
  "allocation_id": "YOUR_DOTS.ECO_ALLOCATION_ID"  
}  
{% endcapture %}

{% connected_content https://impact.dots.eco/api/v1/certificate/add?format=sdk  
  :method post  
  :headers { "auth-token": "YOUR_DOTS.ECO_AUTH_TOKEN" }  
  :body {{post_body}}  
  :content_type application/json  
  :save result  
%}

{  
  "attributes": [  
    {  
      "certificate_image_url": "{{result.certificate_image_url}}",  
      "certificate_url": "{{result.certificate_url}}",  
      "certificate_id": "{{result.certificate_id}}"  
    }  
  ]  
}  
```
{% endraw %}

Envoyez la demande à `https://impact.dots.eco/api/v1/certificate/add?format=sdk`.

![DOTS.ECO Étape de mise à jour de l'utilisateur.]({% image_buster /assets/img/dots_eco/dotseco_user_update.png %})

{% alert important %}  
Cette intégration utilise le contenu connecté à l'intérieur d'une étape du canvas de **mise à jour de l'utilisateur** pour appeler l'API DOTS.ECO. Testez d'abord les demandes avec un client API (par exemple, Postman) pour valider votre jeton et votre charge utile.  
{% endalert %}

### Étape 3 : Afficher le certificat dans les messages

Lorsque les attributs du certificat sont stockés dans le profil utilisateur, ils peuvent être référencés dans les étapes du message canvas en aval.

![DOTS.ECO flux.]({% image_buster /assets/img/dots_eco/dots.eco_flow.png %})

![DOTS.ECO Envoi de messages.]({% image_buster /assets/img/dots_eco/dotseco_messages.png %})

![DOTS.ECO la section de composition des messages.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose.png %})

Par exemple :  
- Affichez l'image du certificat dans un message in-app à l'aide de la fonction {% raw %}`{{custom_attribute.${certificate_image_url}}}`{% endraw %}  
- Lien vers le certificat hébergé à l'aide de {% raw %}`{{custom_attribute.${certificate_url}}}`{% endraw %}

![DOTS.ECO le comportement du message au moment du clic.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose_onclickbehavior.png %})


Vous pouvez ainsi personnaliser les messages in-app, les cartes de contenu ou les notifications push avec confirmation d'impact.

## Résolution des problèmes

Passez en revue les erreurs de contenu connecté dans le tableau de bord de Braze, sous **Paramètres** > **Journal d'activité des messages.**

- **Le contenu connecté renvoie un message vide**: Confirmez que `:save result` est défini et que vous faites référence aux champs de réponse attendus.
- **Les attributs n'apparaissent pas dans l'étape Message :**
  - Confirmez que les noms des attributs personnalisés dans Braze correspondent exactement aux attributs que vous avez définis à l'étape Mise à jour de l'utilisateur.
  - Dans l'étape Mise à jour de l'utilisateur, utilisez l'onglet **Prévisualisation et test** pour confirmer que les attributs sont bien renseignés. Ensuite, envoyez un test à un utilisateur et confirmez que les attributs sont enregistrés sur son profil utilisateur.
- **`422` erreur (entité non traitable)**: Confirmez que votre jeton d'application et votre quantité d'impact sont valides.
- **`401` erreur**: Confirmez que le jeton d'authentification est présent et correct.
- **Pas de prévisualisation de l'image dans l'étape Message :** Sélectionnez **Envoyer le test à l'utilisateur** dans l'étape Mise à jour de l'utilisateur, puis prévisualisez le message en utilisant ce même utilisateur.