---
nav_title: Récupérer des données grâce au Contenu connecté
article_title: Récupérer des données grâce au Contenu connecté avec Voucherify
page_order: 2
alias: /partners/voucherify/connected_content/
description: "Cet article explique comment récupérer les données de l'API Voucherify via le contenu connecté de Braze et envoyer des messages à des segments Braze spécifiques."
page_type: partner
search_tag: Partenaire
---

# Récupérer des données grâce au Contenu connecté

> Avec le contenu connecté Braze, vous pouvez récupérer des données de l'API Voucherify et envoyer des messages à des segments Braze spécifiques. Cet article vous montrera comment configurer les scripts de Contenu connecté pour publier des coupons Voucherify, inviter de nouveaux parrains, récupérer le solde des cartes de fidélité, et plus encore.

Le schéma de base du script se présente comme suit :
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

Consultez le [référentiel GitHub](https://github.com/voucherifyio/braze-connected-content) de Voucherify pour voir des exemples de scripts de Contenu connecté.

## Paramètres de sécurité

Si les paramètres suivants ne sont pas définis, chaque fois qu'un message de Contenu connecté est déclenché, il appelle l'API Voucherify au moins deux fois. Ces paramètres réduisent le nombre d'appels d'API facturés à Braze et réduisent le risque d'atteindre la limite de blocage de l'API qui peut interrompre la livraison des messages.

{% tabs %}
{% tab Rate Limiter %}

**Limiteur de débit**

Assurez-vous de [limiter le nombre de messages]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) envoyés par Braze par minute. Cela sécurise les API Braze et Voucherify contre le trafic trop important de votre campagne. Lorsque vous ciblez des utilisateurs lors de la configuration de la campagne, limitez le taux d'envoi à 500 messages par minute.

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

{% endtab %}
{% tab Caching %}

**Mise en cache dans les appels POST**

Les appels de Contenu connecté effectués via HTTP POST ne sont pas mis en cache par défaut et effectueront deux requêtes API pour chaque code publié. Ce comportement peut réduire les limites de votre API. Le mécanisme de mise en cache vous permettra de limiter cela à un appel API par publication de bon. 

{% alert important %}
Tous les exemples de Contenu connecté dans ce didacticiel incluent la mise en cache par défaut pour réduire le nombre d'appels d'API déclenchés par Braze.
{% endalert %}

Pour ajouter la mise en cache aux appels POST :

1. Ajouter un {% raw %}`:cache_max_age`{% endraw %} attribut. Par défaut, la durée de mise en cache est de 5 minutes. Vous pouvez personnaliser la durée en utilisant des secondes. Elle peut être réglée entre 5 minutes et 4 heures. Exemple : {% raw %}`:cache_max_age 3600`{% endraw %} sera mis en cache pour 1 heure.
2. Fournir une clé de mise en cache {% raw %}`cache_id={{cache_id}}`{% endraw %} dans le paramètre de requête de l’endpoint de destination afin que Braze puisse identifier une publication unique. Tout d'abord, définissez la variable, puis ajoutez la chaîne de caractères de requête unique à votre endpoint. Cela permettra de différencier chaque publication par le {% raw %}`source_id`{% endraw %}.

![]({% image_buster /assets/img/voucherify/voucherify_cc_cache.png %})

_Notez les conséquences :_ Braze met en cache les appels d'API sur la base de l'URL. La chaîne de caractères unique utilisée comme paramètre de requête est ignorée par Voucherify, mais elle distingue les différentes requêtes API pour Braze et permet de mettre en cache chaque tentative unique séparément. Sans ce paramètre de requête, chaque client recevra le même code de réduction pour la durée du cache.

{% endtab %}
{% tab Retry attribute %}

**Attribut de répétition**

Le contenu connecté ne valide pas la réponse Voucherify, c’est pourquoi nous recommandons d'ajouter un attribut de [répétition]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries) dans le script de Contenu connecté. La logique de Contenu connecté essaiera de réessayer cinq fois avant d'abandonner le message (elle respectera le limiteur de débit). Cette méthode permettra d'éviter les cas d'échec de la publication du code lorsqu'il faut un peu plus de temps pour récupérer les données de Voucherify.

Si vous n’utilisez pas {% raw %}`:retry`{% endraw %}, alors, quelle que soit la réponse renvoyée par Voucherify, Braze tentera d'envoyer la distribution, ce qui peut entraîner la génération d'e-mails sans code publié.

![]({% image_buster /assets/img/voucherify/voucherify_cc_retry.png %})

{% endtab %}
{% tab Unique publications %}

**Publication unique par client**

Le paramètre {% raw %}`source_id`{% endraw %} dans le corps du script prévoit que chaque client ne peut recevoir qu'un seul code unique par campagne Braze. Par conséquent, même si Braze multiplie involontairement la demande, chaque utilisateur recevra le même code unique qui lui a été communiqué dans le premier message.

![]({% image_buster /assets/img/voucherify/voucherify_cc_sourceId_unique_publication.png %})

Vous pouvez modifier {% raw %}`{{source_id}}`{% endraw %} et son effet sur les publications en utilisant les configurations suivantes :

| Configuration | Effet |
| ------------- | ------ |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} | Garantit que tous les clients d'un même envoi utiliseront la même publication. |
| {% raw %}`{{campaign.${api_id}}}`{% endraw %} | Garantit que tous les clients d'une même campagne utiliseront la même publication. |
| {% raw %}`{{${user_id}}}`{% endraw %} ou {% raw %}`{{${braze_id}}}`{% endraw %} | Garantit que chaque client utilisera la même publication, quelle que soit la campagne envoyée (vous pouvez utiliser {% raw %}`${user_id}`{% endraw %} qui est un {% raw %}`external_id`{% endraw %} et {% raw %}`${braze_id}`{% endraw %} qui est un identifiant interne). |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} et {% raw %}`{{campaign.${user_id}}}`{% endraw %} | Chaque client d'un même envoi utilisera la même publication unique. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Join-once %}

**Inscription unique**

Si votre campagne Voucherify est limitée aux _clients qui ne peuvent s'inscrire qu'une seule fois_, supprimez l'identifiant de la source de publication du corps du script. Voucherify veillera à ce que chaque message Braze destiné au même client délivre le même code publié en premier lieu.

![]({% image_buster /assets/img/voucherify/voucherify_cc_join_once.png %}){: style="max-width:50%;"}

Votre script de Contenu connecté doit être le suivant :

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

## Exemples

Gardez à l'esprit que tous les exemples ci-dessous utilisent l'ID de la source de publication de Voucherify et les paramètres de cache et de relance de Braze pour limiter les appels API invoqués par une campagne Braze. Vous devez être conscient des implications suivantes :

- Il n'est pas possible de publier et d'envoyer différents codes au même client dans une même campagne Braze.
- Si votre campagne Voucherify utilise la _fonctionnalité d’inscription unique_, vous devez supprimer `source_id` du corps du contenu connecté comme décrit dans l'onglet « Inscription unique » ci-dessus.

Consultez le [référentiel GitHub](https://github.com/voucherifyio/braze-connected-content) de Voucherify pour voir des exemples de scripts de Contenu connecté.

### Publier et envoyer un code de coupon unique

Dans cet exemple, le script de Contenu connecté appelle l'API Voucherify pour publier un code de coupon unique et l'envoyer dans le message Braze. Chaque utilisateur de Braze ne reçoit qu'un seul code unique.

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

### Invitez de nouveaux parrains

Si vous souhaitez qu'un client adhère à un programme de parrainage, vous devez attribuer un code de recommandation à cette personne. Le contenu connecté reste le même que dans l'exemple précédent. Ce script de contenu connecté vous permet de publier et d'envoyer des codes de recommandation uniques à des utilisateurs Braze sélectionnés. Chaque utilisateur ne reçoit qu'un seul code de recommandation pour le partager avec d'autres utilisateurs et obtenir de nouvelles recommandations. 

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

### Récupérer le solde de la carte de fidélité

Voici un exemple de script de Contenu connecté qui extrait le solde de fidélité actuel en fonction du code de la carte de fidélité qui a été envoyé au préalable à Braze en tant qu'attribut personnalisé. Notez que vous devez stocker le code de la carte de fidélité comme un attribut personnalisé dans le profil utilisateur Braze avant d'utiliser ce script.

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

Le Contenu connecté est un outil puissant qui permet d'introduire des scénarios créatifs. Vous pouvez créer un code de coupon personnalisé en fonction des informations du profil client.

Voici un exemple d'extrait de code qui prendra en compte le numéro de téléphone du client pour générer un code unique. Dans cet exemple, le script de Contenu connecté appelle l'API Voucherify pour publier un code de coupon personnalisé.

1.  Tout d'abord, définissez toutes les variables nécessaires. Ensuite, créez un code de coupon commençant par le préfixe "SummerTime-" et le reste du code sera le numéro de téléphone du client. Vous pouvez décider de l'attribut personnalisé sur lequel vous souhaitez baser vos codes de réduction.  
    
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
    
2.  Ensuite, demandez à Voucherify de générer un seul code dans la campagne. Nous fournissons le nom du code promo à créer dans l'URL :  
    
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

3.  Enfin, publiez le code que vous venez de créer. L'extrait de code est presque identique à celui que vous avez utilisé pour générer un bon d'achat aléatoire à partir d'une campagne. Cependant, nous ciblons cette fois un code de bon spécifique.  
    
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

## Afficher les données extraites dans les messages Braze

Nous supposons que vous avez déjà une campagne Braze ou un Canvas dans lequel vous souhaitez utiliser le script de Contenu connecté.

### Étape 1 : Ajouter le script de Contenu connecté au modèle de message

1.  Copiez et collez le script de Contenu connecté sous la balise  {% raw %}`<body>`{% endraw %} dans un modèle HTML de message. Remplacez **CAMPAIGN_ID** par un Voucherify {% raw %}`campaign_id`{% endraw %} copié depuis l’adresse URL du tableau de bord de la campagne Voucherify.<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_campaignId.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}  
    ```
    assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce"
    ```
    {% endraw %}

2. Fournissez votre endpoint API Voucherify. Si vous ne savez pas quel est votre endpoint API, vous pouvez le vérifier dans **Project settings** > **General** > **API endpoint** (Paramètres du projet > Général > Endpoint API).<br>
    {% raw %}
    ```
    YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
    ```
    {% endraw %}
    
    | Cluster partagé   | Endpoint pour Contenu connecté Braze          |
    | ---------------- | --------------------------------------------- |
    | Europe (par défaut) | https://api.voucherify.io/v1/publications     |
    | États-Unis    | https://us1.api.voucherify.io/v1/publications |
    | Asie (Singapour) | https://as1.api.voucherify.io/v1/publications |
    {: .reset-td-br-1 .reset-td-br-2}
    
3.  Ajoutez vos clés API pour l'authentification. Vous pouvez trouver `Voucherify-App-Id` et `Voucherify-App-Token` dans **Project Settings > General >Application Keys.** (Paramètres de votre projet > Général > Clés d'application).<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_app_keys.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}
    ```
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
    ```
    {% endraw %}
    
Votre script de Contenu connecté est maintenant prêt à être utilisé.

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

### Étape 2 : Créer un extrait de code pour afficher les données récupérées

Les réponses de l'API Voucherify sont stockées par le Contenu connecté sous la valeur du paramètre {% raw %}`:save`{% endraw %} . Par exemple :

{% raw %}

```liquid
:save member
```
{% endraw %}

Cela vous permet de récupérer et d'afficher les données d'une réponse Voucherify dans des messages Braze.

Vous pouvez créer des extraits de code qui affichent le code publié, le solde de la carte de fidélité, la date d'expiration et d'autres paramètres inclus dans la réponse au format JSON de l'API Voucherify.

Par exemple, pour afficher le code publié dans un modèle de message, vous devez créer un extrait de code qui récupère un code unique à partir de l'objet coupon.

Script de Contenu connecté :

![Le script de Contenu connecté montre comment sauvegarder une réponse Voucherify à la fin de l'appel de Contenu connecté]({% image_buster /assets/img/voucherify/voucherify_cc_save_parameter.png %})

Extrait de code dans le modèle de message Braze :

{% raw %}

```liquid
{{publication.voucher.code}}
```

{% endraw %}

Ainsi, chaque client reçoit un message avec un code unique automatiquement attribué à son profil. Chaque fois qu'un code est reçu par l'utilisateur, il est publié sur son profil dans Voucherify.

Pour afficher le solde d'une carte de fidélité récupéré à partir de l'API Voucherify, vous devez créer l’extrait de code suivant :

{% raw %}

```liquid
{{member.loyalty_card.balance}}
```

{% endraw %}

où le membre est une valeur du paramètre {% raw %}`:save`{% endraw %} dans le script Contenu connecté.

{% raw %}

```liquid
:save member
```

{% endraw %}

Nous vous conseillons vivement de ne pas dépendre entièrement du « Preview mode » (Mode aperçu) et d'envoyer plusieurs messages de test pour confirmer que tout fonctionne normalement.

### Étape 3 : Configurer le limiteur de débit

Lors de la définition de la cible d'une campagne, utilisez les paramètres avancés pour limiter le nombre de messages envoyés par minute.

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

En savoir plus sur le limiteur de débit et la limite de fréquence dans la [documentation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) de Braze.
