---
nav_title: Créer un webhook
article_title: Créer un webhook
page_order: 1
channel:
  - Webhooks
description: "Cet article de référence décrit comment créer et configurer un webhook ainsi que la manière de les utiliser avec certains Technology Partners de Braze."
search_rank: 2
---

# Créer un webhook

Créer une campagne webhook ou inclure un webhook dans une campagne multicanale vous permet de déclencher des actions en-dehors de l’application. Plus précisément, les [webhooks][14] peuvent être utilisés pour transmettre à d’autres systèmes et applications avec des informations en temps réel. Vous pouvez utiliser les webhooks pour envoyer des informations à des systèmes comme Salesforce et Marketo. Vous pouvez également utiliser les webhooks pour envoyer des informations à vos systèmes backend. Par exemple, vous pourriez désirer créditer les comptes de vos clients avec une promotion une fois qu’ils ont effectué un événement personnalisé un certain nombre de fois.

Si vous désirez en apprendre plus concernant les webhooks et leur utilisation dans Braze, consultez la section [À propos des webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) avant de continuer.

## Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont préférables pour des messages simples, tandis que les Canvas se prêtent davantage aux expériences utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campagne %}

**Étapes :**

1. Sur la page **Campagne**, cliquez sur <i class="fas fa-plus"></i>**Créer une campagne**
2. Sélectionnez **Webhook**, ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Campagne multicanales**.
3. Donnez un nom clair et significatif à votre campagne.
4. Si nécessaire, ajoutez des [Équipes]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) et des [Tags.]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)
   * Les tags facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [Créateur de rapports]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), vous pouvez filtrer les éléments en fonction de tags spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez utiliser différents modèles de webhook pour chacune des variantes que vous ajoutez. Pour plus d’informations sur ce sujet, consultez [Tests A/B et Tests multivariés]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d’ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Étapes :**

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l’aide de l’Assistant Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le Créateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Choisissez une [planification des étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et indiquez un délai si besoin est.
4. Filtrez votre audience pour cette étape si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant plus de filtres. Les options d’audience seront vérifiées après le délai au moment de l’envoi des messages.
5. Choisissez votre [comportement d’avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de messagerie que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Composer votre webhook

Vous pouvez choisir entre construire un webhook depuis le départ ou utiliser un de nos modèles existants. Construisez ensuite votre Webhook dans l’onglet **Composer** de l’éditeur.

![Onglet Composer lors de la création d’un webhook dans Braze]({% image_buster /assets/img_archive/webhook_compose.png %})

L’onglet **Composer** comprend les champs suivants :

#### Language {#internationalization}

L’[Internationalisation][16] est prise en charge dans l’URL et dans le corps de la requête. Pour internationaliser votre message, cliquez sur **Ajouter des langues** et remplissez le menu déroulant. Nous vous recommandons de sélectionner vos langues avant d’écrire votre contenu afin que vous puissiez remplir votre texte dans le Liquid. Consultez notre [liste complète des langues disponibles]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

#### URL du webhook

L’URL du webhook, ou l’URL HTTP, définit votre endpoint. L’endpoint est l’endroit où vous enverrez les informations que vous capturez dans le webhook. Si vous désirez envoyer une information à un vendeur, le vendeur doit fournir cette URL dans la documentation de son API. Si vous envoyez l’information à nos propres systèmes, consultez votre équipe de développement ou d’ingénierie pour vous assurer d’utiliser la bonne URL. 

Braze autorise uniquement les URL qui communiquent sur les ports `80` (HTTP) et `443` (HTTPS) standard.

Vous pouvez personnaliser les URL de votre webhook en utilisant [Liquid][15]. Il peut parfois arriver que certains endpoints vous demandent d’identifier un utilisateur pour fournir une information qui lui est spécifique au sein de l’URL. Lorsque vous utilisez Liquid, assurez-vous d’inclure une [valeur par défaut][19] pour chaque élément spécifique à l’utilisateur que vous utilisez dans votre URL.

#### Corps de la demande

Le corps de la requête est l’information qui sera envoyée à l’URL que vous avez définie. Il existe deux manières pour construire le corps de la requête de votre webhook :

##### Paires clé-valeur JSON

Les paires clé-valeur JSON vous permettent d’écrire facilement une requête pour un endpoint qui attend un format JSON. Vous ne pouvez utiliser cette fonctionnalité qu’avec un endpoint qui attend une requête JSON. Par exemple, si votre clé est `message_body`, la valeur correspondante pourrait être `Your order just arrived!`. Après avoir entré la paire clé-valeur, le composeur configurera votre requête en syntaxe JSON et une prévisualisation de votre requête JSON se remplira automatiquement.

![Corps de requête défini sur des paires clé-valeur][21]

Vous pouvez personnaliser vos paires clé-valeur en utilisant du [Liquid][15], en ajoutant par exemple un attribut utilisateur, un [attribut personnalisé][17] ou une [propriété d’événement][18] dans votre requête. Vous pouvez par exemple ajouter le prénom et l’e-mail d’un client dans votre requête. N’oubliez pas d’ajouter une [valeur par défaut][19] pour chaque attribut !

##### Texte brut

L’option de texte brut permet une flexibilité pour écrire une requête pour un endpoint qui attend un corps de n’importe quel format. Vous pouvez, par exemple, utiliser cette fonctionnalité pour écrire une requête pour un endpoint qui attend que votre requête soit au format XML. La [personnalisation][15] et l’[internationalisation][16] utilisant du Liquid sont prises en charge par le texte brut.

![Corps de requête défini en texte brut][22]

## Étape 3 : Configurer des paramètres supplémentaires

#### En-têtes de requête (optionnel)

Certains endpoints peuvent nécessiter d’ajouter des en-têtes à vos requêtes. Vous pouvez ajouter autant d’en-têtes que vous le désirez dans la section **Paramètres** du composeur. Les en-têtes de requêtes fréquents sont les spécifications de types de contenu (qui décrivent quel type de données attendre dans le corps, tels que du XML ou du JSON) et les en-têtes de permissions qui contiennent vos identifiants auprès du vendeur ou du système. 

Les spécifications de type de contenu doivent utiliser la clé `Content-Type`. Des valeurs fréquentes sont `application/json` ou `application/x-www-form-urlencoded`.

Les en-têtes de permission doivent utiliser la clé `Authorization`. Des valeurs fréquentes sont {% raw %} `Bearer {{YOUR_TOKEN}}` or `Basic {{YOUR_TOKEN}}` {% endraw %} où `YOUR_TOKEN` représente les identifiants fournis par cotre vendeur ou votre système.

#### Méthode HTTP

La [méthode HTTP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#methods) que vous devez utiliser varie en fonction de l’endpoint auquel vous envoyez des informations. La plupart du temps, vous utiliserez POST.

![Définir les en-têtes de requêtes et la méthode HTTP dans l’onglet Paramètres du composeur][26]

## Étape 4 : Tester l’envoi de votre message

Avant de déployer votre campagne, Braze recommande de tester le webhook pour vous assurer que la requête est formatée correctement.

Pour ce faire, basculez sur l’onglet **Test** et envoyez un test de webhook. Vous pouvez tester le webhook en tant qu’utilisateur aléatoire, utilisateur spécifique (en saisissant son adresse e-mail ou son ID utilisateur externe) ou un utilisateur personnalisé avec les attributs de votre choix.  

Après avoir envoyé le test de webhook, un dialogue s’affichera avec le message en réponse. Si la requête webhook échoue, consultez le message d’erreur pour obtenir de l’aide pour la résolution des problèmes de votre webhook. L’exemple suivant détaille la réponse d’un webhook ayant une URL de webhook invalide.

```json
404 Page introuvable

{
  "error": {
    "message": "URL de la requête non reconnue. Veuillez consulter https://lob.com/docs ou nous envoyer un e-mail à l’adresse support@lob.com. ",
    "status_code": 404
  }
}

```

## Étape 5 : Créer le reste de votre campagne ou Canvas

{% tabs %}
{% tab Campagne %}

Concevez ensuite le reste de votre campagne. Consultez les sections suivantes pour plus de détails sur la façon de mieux utiliser nos outils pour créer des webhooks.

#### Choisir un calendrier ou un déclencheur pour la livraison

Les webhooks peuvent être livrés en fonction d’un calendrier, d’un événement ou d’un déclencheur API. Pour en savoir plus, consultez la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour une livraison par événement, vous pouvez également définir la durée de la campagne et les [Heures calmes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

Cette étape permet également de spécifier les contrôles de livraison, comme permettre aux utilisateurs de devenir [rééligibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne ou activer les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler vos utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) en choisissant des segments ou des filtres pour préciser votre public. Au cours de cette étape, vous allez sélectionner une audience plus importante dans vos segments et allez restreindre peut-être davantage ce segment à l’aide de nos filtres. Vous recevez automatiquement un aperçu de ce à quoi ressemble la population approximative du segment à ce moment-là. Gardez à l’esprit que l’appartenance précise à un segment est toujours calculée juste avant l’envoi du message.

#### Sélectionner des événements de conversion

Braze vous permet de suivre à quelle fréquence les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d’autoriser une fenêtre allant jusqu’à 30 jours pendant laquelle une conversion sera comptée si l’utilisateur entreprend l’action spécifiée.

{% endtab %}

{% tab Canvas %}

Si vous ne l’avez pas déjà fait, terminez les sections restantes de votre Canvas Step. Pour plus d’informations sur la manière de mettre en place le reste de votre Canvas, d’implémenter un test multivarié et une sélection intelligente, référez-vous à l’étape [Construire votre Canvas Step]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.

{% endtab %}
{% endtabs %}

## Étape 6 : Revue et déploiement

Après avoir terminé votre campagne ou votre Canvas, consultez-en les détails, faites un test et procédez à son envoi.

## Choses à savoir

### Erreurs, logique de nouvel essai et temporisation

Les webhooks se fondent sur le fait que Braze effectue des requêtes à un endpoint externe et des erreurs de syntaxe, ou autres, peuvent se produire. La première étape pour éviter les erreurs de webhooks est de tester d’éventuelles erreurs de syntaxe dans vos campagnes webhooks et de vous assurer que les variables personnalisées ont une valeur par défaut. Cependant, les webhooks peuvent quand même échouer en raison de problèmes comme des clés API ayant expiré, des limites de débit ou des erreurs inattendues du serveur. Si vos webhooks n’arrivent pas à se lancer, un message d’erreur est enregistré dans la [Developer Console][42], dans le **Journalisation d’activité de messages**. Cette description comprend l’heure à laquelle l’erreur est survenue, le nom de l’application et le message d’erreur :

![Erreur webhook avec le message « Un jeton d’accès actif doit être utilisé pour demander des informations sur l’utilisateur actuel »][43]

Si le corps du message n’est pas assez clair au sujet de la source du problème, vous devriez consulter la documentation de l’endpoint d’API que vous utilisez. Elle fournit généralement une explication des codes d’erreur utilisés par l’endpoint ainsi que ce qui les entraîne le plus souvent.

Comme pour les autres campagnes, Braze suit la livraison de vos campagnes webhook et les conversions qui en résultent. Lorsque la requête webhook est envoyée, le serveur qui la reçoit renverra un code de réponse indiquant ce qui est arrivé à la requête. Le tableau suivant résume les différents types de réponses pouvant être envoyées par le serveur, leur impact sur les analytiques de campagne et si Braze essaiera de livrer à nouveau la campagne en cas d’erreur :

| Code de réponse | Marqué comme reçu ? | Nouvel essai ? |
|---------------|-----------|----------|
| 20x (réussite)  | Oui |   S.O.  |
| 30x (redirection)  | Non | Non |
| 408 (temporisation de la requête)  | Non | Oui |
| 429 (limité par le débit)  | Non | Oui |
| Autres 4xx (erreur du client)  | Non | Non |
| 5xx (erreur côté serveur)   | Non | Oui |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Lors de nouveaux essais, Braze effectuera cinq tentatives en utilisant des délais exponentiels pendant environ 30 minutes avant d’abandonner l’appel webhook donné.

Chaque webhook a 90 secondes avant qu’il ne s’arrête.

### Passer une IP en liste blanche {#ip-whitelisting}

Lorsqu’un webhook est envoyé par Braze, les serveurs Braze effectuent des requêtes réseau aux serveurs de nos clients ou tiers. Avec la liste blanche d’IP, vous pouvez vérifier que les requêtes webhook proviennent réellement de Braze, ajoutant ainsi une couche de sécurité supplémentaire.

Braze enverra des webhooks depuis les plages IP suivantes. Les plages répertoriées sont automatiquement et dynamiquement ajoutées à toutes les clés API qui ont été choisies pour la whitelist.

{% alert important %}
Si vous mettez en place un webhook Braze à Braze et utilisez des listes blanches, vous devriez placer les IP suivantes en liste blanche, y compris `127.0.0.1`.
{% endalert %}

| Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05` et `US-06` : |
|---|
| `127.0.0.1`
| `23.21.118.191`
| `34.206.23.173`
| `50.16.249.9`
| `52.4.160.214`
| `54.87.8.34`
| `54.156.35.251`
| `52.54.89.238`
| `18.205.178.15`

| Pour les instances `EU-01` et `EU-02`: |
|---|
| `127.0.0.1`
| `52.58.142.242`
| `52.29.193.121`
| `35.158.29.228`
| `18.157.135.97`
| `3.123.166.46`
| `3.64.27.36`
| `3.65.88.25`
| `3.68.144.188`
| `3.70.107.88` 

| Pour l’Instance `US-08`: |
|---|
| `52.151.246.51`
| `52.170.163.182`
| `40.76.166.157`
| `40.76.166.170`
| `40.76.166.167`
| `40.76.166.161`
| `40.76.166.156`
| `40.76.166.166`
| `40.76.166.160`
| `40.88.51.74`
| `52.154.67.17`
| `40.76.166.80`
| `40.76.166.84`
| `40.76.166.85`
| `40.76.166.81`
| `40.76.166.71`
| `40.76.166.144`
| `40.76.166.145`

### Utiliser des webhooks avec les partenaires de Braze {#utilizing-webhooks}

Il existe de nombreuses manières d’utiliser les webhooks et, avec les partenaires technologiques de Braze (Alloys), vous pouvez les employer pour élever votre communication directement avec vos clients et utilisateurs.

Consultez :
* [Messenger]({{site.baseurl}}/partners/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/advertising_technologies/retargeting/remerge/)
* [Lob.com]({{site.baseurl}}/partners/additional_channels/direct_mail/lob/)
* Et bien plus de nos [partenaires technologiques]({{site.baseurl}}/partners/home/) !

[14]: https://sendgrid.com/blog/whats-webhook
[15]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[16]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#additional-notes-and-best-practices
[18]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[21]: {% image_buster /assets/img/webhook_json_1.png %}
[22]: {% image_buster /assets/img_archive/webhook_rawtext.png %}
[26]: {% image_buster /assets/img_archive/webhook_request_header.png %}
[42]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/
[43]: {% image_buster /assets/img_archive/webhook-error.png %}
