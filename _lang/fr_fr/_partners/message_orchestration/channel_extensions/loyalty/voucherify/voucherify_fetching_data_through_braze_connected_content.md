---
nav_title: Récupérer des données grâce au contenu connecté
article_title: Récupérer des données via le contenu connecté avec Voucherify
page_order: 2
alias: /partners/voucherify/connected_content/
description: "Cet article de référence explique comment vous pouvez récupérer des données de l'API Voucherify via Braze Connected Content et envoyer des messages à des segments Braze spécifiques."
page_type: partner
search_tag: Partner
---

# Récupérer des données grâce au contenu connecté

> Avec Braze Connected Content, vous pouvez récupérer des données de l'API Voucherify et envoyer des messages à des segments Braze spécifiques. Cet article de référence vous montrera comment mettre en place des scripts de contenu connecté pour publier des coupons Voucherify, inviter de nouvelles recommandations, récupérer le solde des cartes de fidélité, et plus encore.

_Cette intégration est gérée par Voucherify._

## À propos de l'intégration

Le schéma de base du script est le suivant :
{% raw %}
```json
{% connected content
  "voucherify-API-ENDPOINT-url"
  :method post
  :headers {
    "X-App-Id": "Voucherify-API-key",
    "X-App-Token": "Voucherify-Secret-key",
  }
  :content_type application/json
  :retry
  :save {{result_variable}}
}
```
{% endraw %}

Visitez le [dépôt GitHub](https://github.com/voucherifyio/braze-connected-content) de Voucherify pour voir des exemples de scripts de contenu connecté.

## Paramètres de sécurité

Si les paramètres suivants ne sont pas définis chaque fois qu'un message de contenu connecté est déclenché, l'API Voucherify sera appelée au moins deux fois. Ces paramètres réduisent le nombre d'appels à l'API facturés à Braze et diminuent le risque d'atteindre la limite de blocage de l'API, ce qui pourrait interrompre la distribution des messages.

{% tabs %}
{% tab Limite de débit %}

**Limite de débit**

Veillez à [limiter le nombre de messages]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) envoyés par Braze par minute. Cela permet de sécuriser les API de Braze et de Voucherify contre l'impact d'une trop grande quantité de trafic provenant de votre campagne. Lors du ciblage des utilisateurs pendant la configuration de la campagne, limitez le débit d'envoi à 500 messages par minute.

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

{% endtab %}
{% tab Mise en cache %}

**Mise en cache dans les appels POST**

Les appels au contenu connecté effectués via HTTP POST ne sont pas mis en cache par défaut et effectueront deux requêtes API pour chaque code publié. Ce comportement peut mettre à rude épreuve les limites de votre API. Le mécanisme de mise en cache vous permettra de limiter cette opération à un appel à l'API par publication de bons. 

{% alert important %}
Tous les exemples de contenu connecté présentés dans ce tutoriel incluent une mise en cache par défaut afin de réduire le nombre d'appels d'API déclenchés par Braze.
{% endalert %}

Pour ajouter la mise en cache aux appels POST :

1. Ajoutez un attribut {% raw %}`:cache_max_age`{% endraw %}. Par défaut, la durée de la mise en cache est de 5 minutes. Vous pouvez personnaliser la durée en secondes. Elle peut être réglée entre 5 minutes et 4 heures. Exemple : {% raw %}`:cache_max_age 3600`{% endraw %} sera mis en cache pendant 1 heure.
2. Fournissez une clé de cache {% raw %}`cache_id={{cache_id}}`{% endraw %} dans le paramètre de requête de l'endpoint de destination afin que Braze puisse identifier une publication unique. Définissez d'abord la variable, puis ajoutez la chaîne de caractères unique à votre endpoint. Cela permettra de différencier chaque publication par le paramètre {% raw %}`source_id`{% endraw %}.

![]({% image_buster /assets/img/voucherify/voucherify_cc_cache.png %})

_Notez les conséquences :_ Braze met en cache les appels API en fonction de l'URL. La chaîne de caractères unique utilisée comme paramètre de requête est ignorée par Voucherify, mais elle distingue les différentes requêtes d'API pour Braze et permet de mettre en cache chaque tentative unique séparément. Sans ce paramètre de requête, chaque client recevra le même code personnalisé pour la durée de la mise en cache.

{% endtab %}
{% tab Attribut retry %}

**Attribut retry**

Le contenu connecté ne valide pas la réponse Voucherify, c'est pourquoi nous vous recommandons d'ajouter un attribut [retry]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries) dans le script du contenu connecté. La logique du contenu connecté essaiera de réessayer cinq fois avant d'abandonner le message (elle respectera la limite de débit). Cette méthode permettra d'éviter les cas d'échec de la publication du code lorsqu'il faut un peu plus de temps pour récupérer les données de Voucherify.

Si vous n'utilisez pas {% raw %}`:retry`{% endraw %}, indépendamment de la réponse renvoyée par Voucherify, Braze tentera d'envoyer la distribution, ce qui peut entraîner la génération d'e-mails sans code publié.

![]({% image_buster /assets/img/voucherify/voucherify_cc_retry.png %})

{% endtab %}
{% tab Publications uniques %}

**Publication unique par client**

Le paramètre {% raw %}`source_id`{% endraw %} dans le corps du script prévoit que chaque client ne peut recevoir qu'un seul code unique dans une même campagne Braze. Par conséquent, même si Braze multiplie involontairement la requête, chaque utilisateur recevra le même code unique qui lui a été publié dans le premier message.

![]({% image_buster /assets/img/voucherify/voucherify_cc_sourceId_unique_publication.png %})

Vous pouvez modifier {% raw %}`{{source_id}}`{% endraw %} et son effet sur les publications en utilisant les configurations suivantes :

| Configuration | Effet |
| ------------- | ------ |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} | Les clients d'un même envoi utiliseront la même publication. |
| {% raw %}`{{campaign.${api_id}}}`{% endraw %} | Tous les clients d'une même campagne utiliseront la même publication. |
| {% raw %}`{{${user_id}}}`{% endraw %} ou {% raw %}`{{${braze_id}}}`{% endraw %} | Vérifie que chaque client utilisera la même publication quelle que soit la campagne envoyée (vous pouvez utiliser {% raw %}`${user_id}`{% endraw %} qui est un {% raw %}`external_id`{% endraw %} et {% raw %}`${braze_id}`{% endraw %} qui est un ID interne). |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} et {% raw %}`{{campaign.${user_id}}}`{% endraw %} | Chaque client d'un même envoi utilisera la même publication unique. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Rejoindre une fois %}

**Rejoindre une fois**

Si votre campagne Voucherify est limitée à une _seule participation des clients_, supprimez l'identifiant de la source de publication dans le corps du script. Voucherify confirmera que chaque message de Braze adressé au même client délivrera le même code publié en premier lieu.

![]({% image_buster /assets/img/voucherify/voucherify_cc_join_once.png %}){: style="max-width:50%;"}

Votre script de contenu connecté doit être le suivant :

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign cache_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}

{% connected_content
   https://api.voucherify.io/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}
{% endtab %}
{% endtabs %}

## Cas d'utilisation

Gardez à l'esprit que tous les cas d'utilisation ci-dessous utilisent l'ID de la source de publication Voucherify et les paramètres de cache et de relance de Braze pour limiter les appels API invoqués par une campagne Braze. Vous devez être conscient des conséquences suivantes :

- Il n'est pas possible de publier et d'envoyer différents codes au même client dans une seule campagne Braze.
- Si votre campagne Voucherify utilise la _fonctionnalité "join only once_, vous devez supprimer `source_id` du corps du contenu connecté comme décrit dans l'onglet "join-once" ci-dessus.

Visitez le [dépôt GitHub](https://github.com/voucherifyio/braze-connected-content) de Voucherify pour voir des exemples de scripts de contenu connecté.

### Publier et envoyer un code de coupon unique

Dans ce cas d'utilisation, le script de contenu connecté appelle l'API Voucherify pour publier un code de coupon unique et l'envoyer dans le message Braze. Chaque utilisateur de Braze reçoit un code unique.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### Inviter de nouveaux référents

Si vous souhaitez qu'un client adhère à un programme de recommandation, vous devez lui attribuer un code de recommandation. Le contenu connecté reste le même que dans l'exemple précédent. Ce script de contenu connecté vous permet de publier et d'envoyer des codes de recommandation uniques à des utilisateurs sélectionnés de Braze. Chaque utilisateur reçoit un seul code de recommandation qu'il peut partager avec d'autres utilisateurs et obtenir de nouvelles recommandations. 

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### Consulter le solde de la carte de fidélité

Voici un cas d'utilisation d'un script de contenu connecté qui tire le solde de fidélité actuel en fonction du code de la carte de fidélité qui a été envoyé au préalable à Braze en tant qu'attribut personnalisé. Notez que vous devez enregistrer le code de la carte de fidélité en tant qu'attribut personnalisé dans le profil utilisateur de Braze avant d'utiliser ce script.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/loyalties/members/{{custom_attribute.${loyalty.card}}}?cache_id={{cache_id}}
   :method get
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :content_type application/json
   :cache_max_age
   :retry
   :save member
 %}
```

{% endraw %}

### Créer un code personnalisé

Le contenu connecté est un outil puissant permettant d'introduire des scénarios créatifs. Vous pouvez créer un code de coupon personnalisé sur la base des informations du profil du client.

Voici un extrait de code qui prendra en compte le numéro de téléphone du client pour générer un code unique. Dans ce cas d'utilisation, le script de contenu connecté appelle l'API Voucherify pour publier un code de coupon personnalisé.

1.  Définissez d'abord toutes les variables nécessaires. Créez ensuite un code de réduction commençant par le préfixe "REST", le reste du code étant le numéro de téléphone du client. Vous pouvez décider de l'attribut personnalisé sur lequel vous souhaitez baser vos codes de coupon.  
    
    {% raw %}
    
    ```liquid
    {% assign braze_campaign_id = {{campaign.${dispatch_id}}} %}
    {% assign customer_id = {{${user_id}}} %}
    {% assign phoneNumber = {{${phone_number}}} %}
    {% assign source_id = braze_campaign_id | append: customer_id %}
    {% assign cache_id = source_id %}
    {% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
    {% assign prefix = "SummerTime-" %}
    ```
    
    {% endraw %}
    
2.  Ensuite, demandez à Voucherify de générer un seul code dans la campagne. Nous indiquons le nom du code de coupon à créer dans l'URL :  
    
    {% raw %}
    
    ```liquid
    {% connected_content
       YOUR-API-ENDPOINT/v1/campaigns/{{voucherify_campaign_id}}/vouchers/{{prefix}}{{phoneNumber}}?cache_id={{cache_id}}
       :method post
       :headers {
            "X-App-Id": "VOUCHERIFY-APP-ID",
            "X-App-Token": "VOUCHERIFY-APP-TOKEN"
       }
       :content_type application/json
       :cache_max_age 
       :save voucher_created
       :retry
    %}  
    ```  
    
    {% endraw %}  

3.  Enfin, publiez le code que vous venez de créer. L'extrait de code est presque le même que celui que vous avez utilisé pour générer un bon aléatoire à partir d'une campagne. Toutefois, cette fois-ci, nous ciblons un code de bon spécifique.  
    
    {% raw %}  
    
    ```liquid
    {% connected_content
       YOUR-API-ENDPOINT/v1/publications?cache_id={{cache_id}}
       :method post
       :headers {
           "X-App-Id": "VOUCHERIFY-APP-ID",
           "X-App-Token": "VOUCHERIFY-APP-TOKEN"
       }
       :body voucher={{prefix}}{{phoneNumber}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
       :content_type application/json
       :cache_max_age 
       :save publication
       :retry
    %}
    ```
    
    {% endraw %}

En conséquence, le client reçoit l'e-mail suivant :  

![]({% image_buster /assets/img/voucherify/voucherify_cc_custom_code_email.png %})

Voici l'extrait de code complet utilisé dans cet exemple :

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${dispatch_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign phoneNumber = {{${phone_number}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign cache_id = source_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign prefix = "Your Prefix" %}

{% connected_content
   YOUR-API-ENDPOINT/v1/campaigns/{{voucherify_campaign_id}}/vouchers/{{prefix}}{{phoneNumber}}?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :content_type application/json
   :cache_max_age 
   :save voucher_created
   :retry
%} 

{% connected_content
   YOUR-API-ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
       "X-App-Id": "VOUCHERIFY-APP-ID",
       "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body voucher={{prefix}}{{phoneNumber}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age 
   :save publication
   :retry
%}
```

{% endraw %}

## Afficher les données récupérées dans les messages de Braze

Nous supposons que vous disposez déjà d'une campagne Braze ou d'un Canvas dans lequel vous souhaitez utiliser le script Contenu connecté.

### Étape 1 : Ajouter un script de contenu connecté au modèle de message

1.  Copiez et collez le script de contenu connecté sous l'étiquette {% raw %}`<body>`{% endraw %} dans un modèle de message HTML. Remplacez **CAMPAIGN_ID** par une adresse {% raw %}`campaign_id`{% endraw %} copiée à partir de l'adresse URL du tableau de bord de la campagne Voucherify.<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_campaignId.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}  
    ```
    assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce"
    ```
    {% endraw %}

2. Indiquez votre endpoint API Voucherify. Si vous ne connaissez pas votre endpoint API, vous pouvez le vérifier dans les **paramètres du projet** > **Général** > **Endpoint API**.<br>
    {% raw %}
    ```
    YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
    ```
    {% endraw %}
    
    | Cluster partagé   | Endpoint pour le contenu connecté de Braze          |
    | ---------------- | --------------------------------------------- |
    | Europe (par défaut) | https://api.voucherify.io/v1/publications     |
    | États-Unis    | https://us1.api.voucherify.io/v1/publications |
    | Asie (Singapour) | https://as1.api.voucherify.io/v1/publications |
    {: .reset-td-br-1 .reset-td-br-2 role="presentation" }
    
3.  Ajoutez vos clés API pour l'authentification. Vous trouverez `Voucherify-App-Id` et `Voucherify-App-Token` dans les **paramètres de votre projet > Général > Clés d'application.**<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_app_keys.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}
    ```
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
    ```
    {% endraw %}
    
Votre script de contenu connecté est maintenant prêt à fonctionner.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce" %}
{% assign cache_id = source_id %}

{% connected_content
   https://api.voucherify.io/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "490a3fb6-a",
        "X-App-Token": "328099d5-a"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### Étape 2 : Créez un extrait de code pour afficher les données récupérées.

Les réponses de l'API Voucherify sont stockées par le contenu connecté sous la valeur du paramètre {% raw %}`:save`{% endraw %}. Par exemple :

{% raw %}

```liquid
:save member
```
{% endraw %}

Cela vous permet de récupérer et d'afficher les données d'une réponse Voucherify dans des messages Braze.

Vous pouvez créer des extraits qui affichent le code publié, le solde de la carte de fidélité, la date d'expiration et d'autres paramètres inclus dans la réponse au format JSON de l'API Voucherify.

Par exemple, pour afficher le code publié dans un modèle de message, vous devez créer un extrait qui récupère un code unique dans l'objet du bon.

Script de contenu connecté :

![Script du contenu connecté permettant d'enregistrer une réponse Voucherify à la fin de l'appel au contenu connecté]({% image_buster /assets/img/voucherify/voucherify_cc_save_parameter.png %})

Extrait de code dans le modèle de message de Braze :

{% raw %}

```liquid
{{publication.voucher.code}}
```

{% endraw %}

Ainsi, chaque client reçoit un message avec un code unique automatiquement attribué à son profil. Chaque fois qu'un code est reçu par l'utilisateur, il est publié sur son profil dans Voucherify.

Pour afficher le solde d'une carte de fidélité récupéré depuis l'API de Voucherify, vous devez créer l'extrait de code suivant :

{% raw %}

```liquid
{{member.loyalty_card.balance}}
```

{% endraw %}

où le membre est une valeur du paramètre {% raw %}`:save`{% endraw %} dans le script de contenu connecté.

{% raw %}

```liquid
:save member
```

{% endraw %}

Nous vous conseillons vivement de ne pas dépendre entièrement du "mode aperçu" et d'envoyer plusieurs messages de test pour confirmer que tout fonctionne comme il se doit.

### Étape 3 : Configuration d'une limite de débit

Lors de la définition d'une cible de campagne, utilisez les paramètres avancés pour limiter le nombre de messages envoyés par minute.

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

Pour en savoir plus sur le limiteur de débit et la limite de fréquence, consultez la [documentation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) Braze.

