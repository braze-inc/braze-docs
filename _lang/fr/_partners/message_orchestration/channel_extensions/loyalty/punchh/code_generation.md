---
nav_title: Génération de code dynamique
article_title: Génération de code dynamique Punchh
page_order: 5
description: "Cet article de référence décrit comment utiliser la génération de code dynamique Punchh dans Braze."
page_type: partner
search_tag: Partenaire

---


# Génération de code de réduction dynamique Punchh dans Braze

Un code de réduction est un code unique qui peut être utilisé par un seul utilisateur (une seule ou plusieurs utilisations). Le cadre Punchh génère des codes de réduction, qui peuvent être traités dans une application mobile ou au POS.

En utilisant le cadre de réduction Punchh et Braze, les scénarios suivants peuvent être réalisés :
1. Générez un code de réduction lorsque le client clique sur un lien de génération de réduction dans un e-mail : Le code de réduction sera généré dynamiquement et affiché sur une page Web.
2. Générez un code de réduction lorsque le client ouvre un e-mail : Le code de réduction sera généré dynamiquement et affiché comme une image dans l’e-mail.

## Comment intégrer la génération de codes de réduction dynamiques Punchh

### Étape 1 : Créer une campagne de réduction dans Punchh

1. À l’aide d’une campagne de réductions Punchh, créez une campagne de réductions à génération dynamique comme indiqué sur l’image suivante.
2. Le cadre de réductions Punchh génère les paramètres suivants pour permettre la génération dynamique de réductions : 
    - Jeton de génération dynamique de réductions : Il s’agit d’un jeton de sécurité généré par le système pour le cryptage.
    - URL de génération de réduction dynamique : Cette URL sera intégrée dans l’e-mail en tant que lien ou image, comme l’exige l’entreprise.

![][2]{: style="max-width:60%;"}    

### Étape 2 : Générer une URL de signature et de construction

La bibliothèque JWT.IO est utilisée pour décoder, vérifier et générer des jetons Web JSON, une méthode ouverte et normalisée selon la norme du secteur RFC 7519 pour représenter en toute sécurité les réclamations entre deux parties. 

Les noms `ClaimType` mentionnés ci-dessous peuvent être utilisés pour garantir la singularité des clients et des réductions.
- `email` : représente l’adresse e-mail de l’utilisateur. 
- `campaign_id` : représente l’ID de campagne Punchh généré par le système. 
- `first_name` : capture le prénom de l’utilisateur. 
- `last_name` : capture le nom de famille de l’utilisateur.

Pour utiliser l’API de code de réductions dynamique Punchh, un jeton JWT doit être construit. Ce qui suit montre comment cela peut être réalisé à l’aide de Liquid au sein de Braze :

{% raw %}
```liquid
{% capture header %}{"typ":"JWT","alg":"HS256"}{% endcapture %}

{% capture payload %} {"email":"{{${email_address}}}","first_name":"{{${first_name}}}","last_name":"{{${last_name}}}","campaign_id":YOUR-CAMPAIGN-ID}{% endcapture %}

{% capture signature_structure %}{{header | base64_encode}}.{{payload | base64_encode}}{% endcapture %}

{% assign secret = "YOUR-DYNAMIC-COUPON-GENERATION-TOKEN" %}

{% assign final_signature = {{signature_structure | hmac_sha256_base64: {{secret}} %}

{% capture jwt %}{{signature_structure}}.{{final_signature | remove: '='}}{% endcapture %}
```
{% endraw %} 
### Étape 3 : Ajouter le code de réduction dans le contenu du courrier électronique

#### Lien vers la page Web de Punchh

En cliquant sur l’URL de réduction, l’utilisateur sera redirigé vers une page Web hébergée par Punchh, où la réduction générée sera affichée à l’utilisateur comme indiqué sur l’image suivante. Par exemple, 
`https://SERVER_NAME_GOES_HERE.punchh.com/request_coupons/YOUR-DYNAMIC-COUPON-GENERATION-TOKEN?sign={{jwt}}`

![][1]

#### Lien de l’image dans le contenu de l’e-mail

Le code de réduction s’affiche sous forme d’image dans l’e-mail. Par exemple, 
`<img src="https://SERVER_NAME_GOES_HERE.punchh.com/request_coupons/YOUR-DYNAMIC-COUPON-GENERATION-TOKEN.png?sign={{jwt}}">`

![][3]

## Messages d’erreur associés

| Code d’erreur | Message d’erreur | Description |
| --- | --- | --- |
| `coupon_code_expired` | Ce code promo a expiré | Le code est utilisé après sa date d’expiration configurée. |
| `coupon_code_success` | Félicitations, le code promotionnel a été appliqué avec succès. | Le code est utilisé avec succès. |
| `coupon_code_error` | Veuillez saisir un code promotionnel valide | Le code utilisé n’est pas valide. |
| `coupon_code_type_error` | Type de réduction incorrecte. Cette réduction ne peut être échangée que sur `%{coupon_type}`. | Cette erreur se produira lorsqu’un code censé être utilisé au point de vente est utilisé dans l’application Mobile. |
| `usage_exceeded` | L’utilisation de cette campagne de code de réduction est pleine. Veuillez essayer la prochaine fois. | L’utilisation du code dépasse le nombre d’utilisateurs autorisés à l’utiliser. Par exemple, si la configuration du tableau de bord permet d’utiliser un code par 3 000 utilisateurs et que le nombre d’utilisateurs dépasse 3 000, cette erreur se produira. |
| `usage_exceeded_by_guest` | Ce code promo a déjà été traité. | L’utilisation du code par un utilisateur dépasse le nombre de fois où un utilisateur peut l’utiliser. Par exemple, la configuration du tableau de bord permet d’utiliser un code unique trois fois pour un utilisateur. S’il est utilisé plus que cela, cette erreur se produira. |
| `already_used_by_other_guest` | Ce code promotionnel a déjà été utilisé par un autre invité. | Un autre utilisateur a déjà utilisé le code. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[1]: {% image_buster /assets/img/punchh/punchh7.png %}
[2]: {% image_buster /assets/img/punchh/punchh8.png %}
[3]: {% image_buster /assets/img/punchh/punchh9.png %}