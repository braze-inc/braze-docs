---
nav_title: Génération dynamique de code
article_title: Génération de code dynamique Punchh
page_order: 2
description: "Cet article de référence explique comment utiliser la génération de code dynamique Punchh dans Braze."
page_type: partner
search_tag: Partner
---

# Génération de code dynamique avec Punchh

> Un code de coupon est un code unique qui peut être utilisé par un seul utilisateur (soit une seule fois, soit plusieurs fois). Le cadre Punchh génère des codes de coupon, qui peuvent être traités dans une application mobile ou au système de point de vente (POS).

_Cette intégration est maintenue par Punchh._

## À propos de l'intégration

En utilisant le cadre de coupon Punchh et Braze, vous pouvez réaliser les scénarios suivants :

- Générez un code de coupon lorsque l'invité clique sur un lien de génération de coupon dans un e-mail: Le code du coupon sera généré dynamiquement et affiché sur une page web.
- Générez un code de coupon lorsque l'invité ouvre un e-mail: Le code de coupon sera généré dynamiquement et affiché comme une image dans l'e-mail.

## Intégration de la génération de code de coupon dynamique

### Étape 1 : Créer une campagne de coupons

1. À l'aide d'une campagne de coupons Punchh, créez une campagne de génération dynamique de coupons comme indiqué dans l'image suivante.
2. Le cadre de coupon Punchh générera les paramètres suivants pour permettre la génération dynamique de coupons :
    - Génération dynamique de jeton de coupon : Il s’agit d’un jeton de sécurité généré par le système pour le cryptage.
    - URL de génération de coupon dynamique : Cette URL sera intégrée dans l'e-mail sous forme de lien ou d'image, selon les besoins de l'entreprise.

![Le formulaire de création d'une campagne de coupons dans Punchh.]({% image_buster /assets/img/punchh/punchh8.png %}){: style="max-width:60%;"}

### Étape 2 : Générer une signature et construire une URL

La bibliothèque JWT.IO décode, vérifie et génère des jetons web JSON, une méthode ouverte et standard de l'industrie RFC 7519 pour représenter des revendications de manière sécurisée entre deux parties. 

Les noms `ClaimType` suivants peuvent être utilisés pour garantir l'unicité des invités et des coupons :

- `campaign_id` : représente l'ID de campagne Punchh généré par le système.
- `email` : représente l'adresse e-mail de l'utilisateur. 
- `first_name`: capture le prénom de l'utilisateur. 
- `last_name` : capture le nom de famille de l'utilisateur.

Pour utiliser l'API de code de coupon dynamique Punchh, un jeton JWT doit être créé. Ajoutez le modèle liquid suivant à votre tableau de bord de Braze dans le corps du message du canal que vous souhaitez utiliser :

{% raw %}
```liquid
{% assign header = '{"alg":"HS256","typ":"JWT"}' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% capture payload_raw %}

{
  "campaign_id": "CAMPAIGN_ID",
  "email": "{{${email_address}}}",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}"
}

{% endcapture %}

{% assign payload = payload_raw | replace: ' ', '' | replace: '\n', '' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign unsigned_token = header | append: "." | append: payload %}

{% assign secret = "DYNAMIC_COUPON_GENERATION_TOKEN" %}

{% assign signature_raw = unsigned_token | hmac_sha256_base64: secret %}

{% assign signature = signature_raw | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign jwt = unsigned_token | append: "." | append: signature %}

```
{% endraw %}


Remplacez les éléments suivants :

| Marque substitutive        | Description                                          |
|--------------------|------------------------------------------------------|
| `DYNAMIC_COUPON_GENERATION_TOKEN` | Votre jeton de génération de coupon dynamique. |
| `CAMPAIGN_ID`                     | Votre ID de campagne.                     |

### Étape 3 : Ajouter le code du coupon au corps du message

#### Lien vers la page Web Punchh

Pour créer un lien vers une page web hébergée par Puncch, ajoutez `{% raw %}{{jwt}}{% endraw %}` à l'URL de génération dynamique [que vous avez créée précédemment](#step-1-create-a-coupon-campaign-in-punchh). Votre lien doit être similaire à ce qui suit : 

{% raw %}
```
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX?sign={{jwt}}
```
{% endraw %}

Lorsqu'un utilisateur clique sur l'URL du coupon, il sera redirigé vers une page web hébergée par Punchh, où son coupon généré sera affiché.

![Exemple de message de confirmation après qu'un utilisateur a généré avec succès un code de coupon.]({% image_buster /assets/img/punchh/punchh7.png %})

#### Extraction de code via JSON en tant que texte brut

Pour renvoyer une réponse JSON, ajoutez `{% raw %}{{jwt}}{% endraw %}` à l'URL de génération dynamique [que vous avez créée plus tôt](#step-1-create-a-coupon-campaign-in-punchh), puis ajoutez `.json` après le jeton dans la chaîne de caractères de l'URL. Votre lien doit être similaire à ce qui suit :

{% raw %}
```liquid
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}}
```
{% endraw %}

Vous pourriez alors tirer parti du [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) pour insérer le code en tant que texte brut dans le corps de tout message. Par exemple:

{% raw %}
```liquid
{% connected_content https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}} :save punchh_coupon %}
{{punchh_coupon.coupon}}
````
{% endraw %}

#### Liaison d'une image dans le contenu de l'e-mail

Pour lier le code de coupon à l'intérieur d'une image :

1. Ajoutez `{% raw %}{{jwt}}{% endraw %}` à l'URL de génération dynamique [que vous avez créée plus tôt](#step-1-create-a-coupon-campaign-in-punchh).
2. Ajoutez `.png` après le jeton dans la chaîne de caractères de l'URL.
3. Intégrez votre lien dans une étiquette HTML {% raw %}`<img>`{% endraw %}.

{% tabs local %}
{% tab exemple de saisie %}
{% raw %}
```liquid
<img src="https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.png?sign={{jwt}}">
````
{% endraw %}
{% endtab %}

{% tab exemple de sortie %}
![Restitution de la balise de l’image du code de coupon.]({% image_buster /assets/img/punchh/punchh9.png %})
{% endtab %}
{% endtabs %}

## Messages d'erreur

| code d'erreur | Message d'erreur | Description |
| --- | --- | --- |
| `coupon_code_expired` | Ce code promo a expiré | Le code est utilisé après sa date d'expiration configurée. |
| `coupon_code_success` | Félicitations, Code promo appliqué avec succès. | Le code est utilisé avec succès. |
| `coupon_code_error` | Veuillez entrer un code promo valide | Le code utilisé est invalide. |
| `coupon_code_type_error` | Type de coupon incorrect. Ce coupon ne peut être utilisé qu'à `%{coupon_type}`. | Lorsqu'un code censé être utilisé au point de vente est utilisé dans l'application mobile, cette erreur est générée. |
| `usage_exceeded` | L'utilisation de cette campagne de code de coupon est complète. Veuillez essayer la prochaine fois. | L'utilisation du code dépasse le nombre d'utilisateurs autorisés à l'utiliser. Par exemple, si la configuration du tableau de bord permet à un code d'être utilisé par 3 000 utilisateurs et que le nombre d'utilisateurs dépasse 3 000, cette erreur sera générée. |
| `usage_exceeded_by_guest` | Ce code promo a déjà été traité. | L'utilisation du code par un utilisateur dépasse le nombre de fois qu'un utilisateur peut l'utiliser. Par exemple, la configuration du tableau de bord permet à un seul code d'être utilisé trois fois par un utilisateur. Si le code est utilisé plus fréquemment, cette erreur est générée. |
| `already_used_by_other_guest` | Ce code promo a déjà été utilisé par un autre invité. | Un autre utilisateur a déjà utilisé le code. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

