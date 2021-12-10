---
nav_title: Un
article_title: Un
alias: /fr/partners/talonone/
description: "Cet article décrit le partenariat entre Braze et Talon. , un moteur de promotion qui vous permet de lancer rapidement et efficacement des campagnes contextuelles de coupon, de recommandation, de rabais et de fidélisation."
page_type: partenaire
search_tag: Partenaire
---

# Un

> [Serre ne](https://talon.one/) propose des incitations personnalisées pour votre CRM marketing mobile et vous donne la possibilité de lancer un coupon contextuel de 1 à 1, campagnes de référence, de réduction et de fidélisation rapidement et efficacement.

L'intégration de Braze et de Talon.One peut aider à faire passer votre programme de fidélité ou de coupon au niveau supérieur en envoyant des codes générés par Talon. ne à votre auditoire via Braze Connected Content.

## Pré-requis

| Exigences         | Libellé                                                                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Un compte         | Un compte Talon.One est requis pour profiter de ce partenariat.                                                                                                                            |
| Clé API Talon.One | Les détails sur la génération d'une clé API Talon.One peuvent être trouvés [dans la documentation de la Talon.One API docs](https://docs.talon.one/management-api/#section/Authentication) |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
Talon.One **_nécessite_** une limite de 500 messages par minute. Cette limite de taux peut être modifiée []({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting) dans le tableau de bord de Braze.
{% endalert %}

## Intégration

### Étape 1 : Mettre en place des coupons à Talon.One

Sur la plateforme Talon.One, accédez au générateur de code coupon de votre campagne trouvé dans **Campagne > Paramètres > Générateur de code coupon**. Ce générateur fournira les champs nécessaires pour inclure dans le point de terminaison de la Talon.One `createcoupon`.

![Paramètres du coupon Talon.One]({% image_buster /assets/img/talonone_coupon_settings.png %})

#### Utilisation du point de terminaison

Un point de terminaison personnalisé `coupon de création` Talon.One doit être utilisé pour convertir la Griffe. Une donnée en chaînes. Ce point de terminaison contient les propriétés intégrées suivantes :

- `applicationID` (obligatoire)
- `campaignID` (obligatoire)
- Identifiant `` (obligatoire)
- `ID d’intégration`
- `startDate`
- `expiryDate`

{% tabs %}
{% tab Required properties %}
#### Exemple 1: Seulement les propriétés requises

```bash
boucler https://demo.talon. ne/v2/integration/braze/createcoupon \
 -X POST \
 -H 'Authorization: ApiKey-v1 <YOUR_API_KEY>' \
 -d '{
        "applicationID": "1",
        "campaignID: "1",
        "identifiant": "an-exemple-identifiant"
}'
```
{% endtab %}
{% tab All built-in properties %}
#### Exemple 2: Toutes les propriétés intégrées

```bash
boucler https://demo.talon. ne/v2/integration/braze/createcoupon \
 -X POST \
 -H 'Authorization: ApiKey-v1 <YOUR_API_KEY>' \
 -d '{
        "applicationID": "1",
        "campaignID": "1",
        "identifiant": "an-exemple-identifiant",
        "integrationID": "an-example-integrationID",
        "startDate": "2019-06-12T09:00:00Z",
        "expiryDate": "2019-06-13T09:00:00Z"
}'
```
{% endtab %}
{% tab Custom Attributes %}
#### Exemple 3 : Attributs personnalisés

Les attributs personnalisés peuvent également être passés directement tant qu'ils sont notés avec un préfixe de point et restent enveloppés dans une chaîne, comme indiqué ci-dessous.

```bash
boucler https://demo.talon. ne/v2/integration/braze/createcoupon \
 -X POST \
 -H 'Authorization: ApiKey-v1 <YOUR_API_KEY>' \
 -d '{
        "applicationID": "1",
        "campaignID": "1",
        "identifiant": "an-exemple-identifiant"
        ". tringAtrrName": "exemplaires",
        ".listOfNumbers": "[1,2,3,4,5,6,7,8,9,10]",
}'
```
{% endtab %}
{% endtabs %}

### Étape 2 : Créer un appel de contenu connecté

Utilisez Braze [Contenus connectés]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/) pour déclencher l'événement de création de coupons. Placez et mettez à jour le code snippet suivant dans votre message de campagne ou message de Canvas pour appeler Talon.One coupons dans votre message.

{% raw %}
```liquid
{% connected_content https://[YOUR_SUBDOMAIN].talon. ne/v2/integration/braze/createcoupon

:headers {
  "authorization": "ApiKey-v1 <YOUR_API_KEY>"
 } 
:method post 
:body applicationID=[YOUR_APPLICATION_ID]&campaignID=[YOUR_CAMPAIGN_ID]&identifier={{campaign.${message_api_id}}}&intégrationID={{${user_id}}}
:content_type application/json 
:save result
%}

{{result.value}}
```
{% endraw %}

1. Ajoutez votre sous-domaine Talon.One à l'URL de terminal.<br><br>
2. Ajoute l'en-tête d'autorisation et la méthode POST de la requête. Plus de détails sur la génération d'une clé API Talon.One peuvent être trouvés dans la documentation [Talon.One API docs](https://docs.talon.one/management-api/#section/Authentication).<br><br>
3. Ajoutez les détails du code de coupon mentionnés à l'étape 1 au corps de la requête. Le paramètre **identifiant** est nécessaire pour empêcher la création de coupons multiples pour un message, et chaque paramètre doit être séparé par un "&" comme indiqué ci-dessus.<br><br>
4. Stocke le résultat de la Serre.1. Utilisez le paramètre `save` à la fin pour stocker la Talon.One réponse en tant que variable Braze. <br><br>
5. Afficher la valeur du code dans le message. Utilisez Liquid pour afficher la valeur du message généré.

{% alert tip %}
Vous pouvez accéder au code promo avec {% raw %} `{{result.value}}` {% endraw %} comme indiqué ci-dessus, qui retournera la valeur générée similaire à `44D4-U4PL`.

Vous pouvez également accéder à toute la réponse de Talon. ne en accédant à {% raw %} `{{result}}` {% endraw %} directement, qui ressemblera à `{"id"=>1548040, "valeur"=>"44D4-U4PL", "__http_status_code__"=>200}`.
{% endalert %}

## Dépannage

Assurez-vous que votre syntaxe de contenu connecté est correcte (comme en utilisant les bonnes balises Liquid pour un Canvas ou une campagne, ainsi que le référencement de la bonne valeur dans la réponse `json`.

Soyez conscient de la limite de 500 messages par minute que vous voulez mettre en œuvre dans la campagne Braze ou Canvas. Si la limite de taux n'est pas respectée, on ne peut pas garantir que chaque code sera généré ou que la réponse sera là à temps.
