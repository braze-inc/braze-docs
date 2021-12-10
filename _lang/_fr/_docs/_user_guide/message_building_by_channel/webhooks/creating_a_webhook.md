---
nav_title: Création d'un Webhook
article_title: Création d'un Webhook
page_order: 1
channel:
  - webhooks
description: "Cet article de référence couvre la façon de créer et de configurer un webhook, ainsi que la façon de les utiliser avec certains partenaires technologiques de Braze."
---

# Création d'un webhook

## Aperçu des fonctionnalités

La création d'une campagne de webhook ou l'inclusion d'un webhook dans une campagne multicanal vous permet de déclencher des actions non applicables. Plus spécifiquement, les [webhooks][14] peuvent être utilisés pour fournir d'autres systèmes et applications avec des informations en temps réel. Vous pouvez utiliser des webhooks pour envoyer des informations à des systèmes tels que Salesforce ou Marketo. Vous pouvez également utiliser des webhooks pour envoyer des informations à vos systèmes d'administration. Par exemple, vous pourriez vouloir créditer les comptes de vos clients avec une promotion une fois qu'ils ont effectué un événement personnalisé un certain nombre de fois.

## Étape 1 : Configurez un webhook

Ajouter un nouveau message webhook à une campagne ou à Canvas. Vous pouvez ensuite choisir de construire un webhook à partir de zéro ou utiliser un de nos modèles existants.

## Étape 2 : Entrez l'URL de votre webhook

### URL HTTP

Entrez l'URL HTTP. Cette URL HTTP spécifie votre terminal. Le point de terminaison est l'endroit où vous allez envoyer les informations que vous capturez dans le webhook. Si vous souhaitez envoyer des informations à un vendeur, le vendeur doit fournir cette URL dans sa documentation API. Si vous envoyez des informations à vos propres systèmes, vérifiez avec votre équipe de développement ou d'ingénierie pour vous assurer que vous utilisez l'URL correcte. Braze n'autorise que les URLs qui communiquent sur les ports standard 80 (HTTP) et 443 (HTTPS).

### Personnalisation

[La personnalisation][15] est prise en charge dans nos URLs HTTP. Parfois, certains terminaux peuvent vous obliger à identifier un utilisateur ou à fournir des informations spécifiques à l'utilisateur dans le cadre de votre URL. Vous voudrez être sûr d'inclure une valeur [par défaut][19] pour chaque élément d'information spécifique à l'utilisateur que vous utilisez dans votre URL.

### Internationalisation

[L'internationalisation][16] est prise en charge dans l'URL et le corps de la requête. Pour internationaliser votre message, cliquez sur **Ajouter des langues** et remplissez le flyout.

## Étape 3 : Créer le corps de la requête

Créez le corps de votre demande de webhook. Il s'agit des informations qui seront envoyées à l'URL que vous avez spécifiée. Il y a deux façons de créer le corps de votre demande de webhook :

### Paires clé-valeur JSON

Les paires clé-valeur JSON vous permettent d'écrire facilement une requête pour un point de terminaison qui attend un format JSON. Notez que vous ne pouvez utiliser cette fonctionnalité qu'avec un point de terminaison qui attend une requête JSON. Par exemple, si votre clé est "message_body", la valeur correspondante pourrait être "Votre commande vient d'arriver." Une fois que vous avez entré votre paire clé-valeur, le compositeur configurera votre requête en syntaxe JSON, et un aperçu de votre requête JSON se remplira automatiquement.

!\[Webhook_JSON\]\[21\]

### Texte brut

L'option texte brut vous donne la flexibilité d'écrire une requête pour un point de terminaison qui attend un corps de n'importe quel format. Par exemple, vous pouvez utiliser cette fonctionnalité pour écrire une requête pour un point de terminaison qui attend que votre requête soit au format XML.

!\[webhook_rawtext\]\[22\]

### Personnalisation

[La personnalisation][15] est prise en charge à la fois dans l'option des paires de clés JSON et dans l'option texte brut. Vous pouvez inclure n'importe quel attribut utilisateur, [attribut personnalisé][17]ou [propriété événement][18] dans votre requête. Par exemple, vous pouvez inclure le prénom et le courriel d'un client dans votre demande. N'oubliez pas d'inclure une valeur [par défaut][19] pour chaque attribut.

### Internationalisation

[L'internationalisation][16] est prise en charge en texte brut.

## Étape 4: En-têtes de requête et méthode HTTP

Certains terminaux peuvent nécessiter que vous incluiez des en-têtes dans votre requête. Dans la section Paramètres du compositeur, vous pouvez ajouter autant d'en-têtes que vous le souhaitez. Les cas d'utilisation courants des en-têtes de requête incluent une spécification de type contenu (par ex. XML ou JSON) et les en-têtes d'autorisation qui contiennent vos identifiants avec votre fournisseur ou votre système. Les spécifications du type de contenu ont la clé "Content-Type" et les valeurs communes sont "application/json" ou "application/x-www-form-urlencoded".

La méthode HTTP que vous devez utiliser varie selon le point de terminaison vers lequel vous envoyez des informations. La plupart du temps, vous utiliserez POST.

!\[Webhook_Request_Header\]\[26\]

## Étape 5 : Tester envoyer votre message

Avant de mettre en ligne votre campagne, vous pouvez tester le webhook pour vous assurer que la demande est formatée correctement. Pour ce faire, accédez à l'onglet Aperçu et envoyez le webhook de test. Vous pouvez tester le webhook pour un utilisateur aléatoire, un utilisateur spécifique (en saisissant son adresse e-mail de l'identifiant d'utilisateur externe), ou un utilisateur personnalisé avec les attributs de votre choix.  Si la demande est réussie, un petit message apparaîtra en haut de votre écran. Si la demande de webhook est infructueuse, une modale apparaîtra avec le message de réponse d'erreur. La capture d'écran ci-dessous est un exemple de réponse d'un webhook avec une URL de webhook invalide.

!\[Fonctionnalité de test Webhook\]\[64\]

## Étape 6 : Poursuivre la création de la campagne

Continuer à créer votre campagne comme vous le feriez normalement. Comme pour tous nos types de messages, vous pouvez prévisualiser ce à quoi votre demande ressemblera pour un utilisateur en particulier, utilisateur aléatoire, ou utilisateur avec des attributs spécifiques dans la section d'aperçu du compositeur de webhook.

## Erreurs, réessayer la logique et les délais

Les Webhooks s'appuient sur les serveurs de Braze qui font des requêtes vers un point de terminaison externe, et la syntaxe et d'autres erreurs peuvent survenir. La première étape pour éviter les erreurs de webhook est de tester votre campagne de webhook pour détecter des erreurs de syntaxe et de s'assurer que les variables personnalisées ont une valeur par défaut. Cependant, les webhooks peuvent toujours échouer en raison de problèmes tels que des clés API expirées, des limites de débit ou des erreurs de serveur inattendues. Si votre webhook ne parvient pas à envoyer, un message d'erreur est enregistré dans la [Console développeur][42], sous « Journal d'activité des messages ». Cette description contient le moment où l'erreur est survenue, le nom de l'application, et le message d'erreur :

!\[Erreur Webhook\]\[43\]

Si le corps du message n'est pas assez clair par rapport à la source de l'erreur, vous devriez vérifier la documentation du point de terminaison de l'API que vous utilisez. Ils fournissent généralement une explication des codes d'erreur que le endpoint utilise ainsi que de ce qu'ils provoquent habituellement.

Comme les autres campagnes, Braze suit la livraison de vos campagnes de webhook et les conversions qui en résultent. Lorsque la demande de webhook est envoyée, le serveur d'accueil renvoie un code de réponse indiquant ce qui s'est passé avec la requête. La table ci-dessous résume les différentes réponses que le serveur peut envoyer, comment ils impacteront les analyses de campagne et si, en cas d'erreurs, Braze tentera de relivrer la campagne:

| Code de réponse                     | Marqué comme reçu? | Tentatives ? |
| ----------------------------------- | ------------------ | ------------ |
| 20 x (succès)                       | Oui                | N/A          |
| 30x (redirection)                   | Non                | Non          |
| 408 (délai d'attente de la demande) | Non                | Oui          |
| 429 (taux limité)                   | Non                | Oui          |
| Autre 4xx (erreur client)           | Non                | Non          |
| 5xx (erreur de serveur)             | Non                | Oui          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Lors d'une nouvelle tentative, Braze effectuera cinq tentatives en utilisant un backoff exponentiel pendant une période d'environ 30 minutes avant d'interrompre l'appel individuel au webhook.

Chaque webhook est autorisé 90 secondes avant son expiration.

## IP sur liste blanche

Lorsqu'un webhook est envoyé depuis Braze, les serveurs Braze font des demandes de réseau à nos clients ou à des serveurs tiers.

Avec la whitelisting, vous pouvez vérifier que les requêtes Webhooks proviennent réellement de Braze, ajoutant une couche de sécurité supplémentaire.

Braze enverra des Webhooks depuis les plages IP ci-dessous.

{% alert important %}
  Si vous faites un webhook Brase-to-Braze et que vous utilisez une liste blanche, vous devriez mettre en liste blanche toutes les adresses IP listées ci-dessus, y compris `127.0.0.1`.
{% endalert %}

| Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`et `US-06`: |
| ------------------------------------------------------------------------- |
| `127.0.0.1`                                                               |
| `23.21.118.191`                                                           |
| `34.206.23.173`                                                           |
| `50.16.249.9`                                                             |
| `52.4.160.214`                                                            |
| `54.87.8.34`                                                              |
| `54.156.35.251`                                                           |
| `52.54.89.238`                                                            |
| `18.205.178.15`                                                           |

| Pour les instances `EU-01` et `EU-02`: |
| -------------------------------------- |
| `127.0.0.1`                            |
| `52.58.142.242`                        |
| `52.29.193.121`                        |
| `35.158.29.228`                        |
| `18.157.135.97`                        |
| `3.123.166.46`                         |
| `3.64.27.36`                           |
| `3.65.88.25`                           |
| `3.68.144.188`                         |
| `3.70.107.88`                          |

| Pour l'instance `US-08`: |
| ------------------------ |
| `52.151.246.51`          |
| `52.170.163.182`         |
| `40.76.166.157`          |
| `40.76.166.170`          |
| `40.76.166.167`          |
| `40.76.166.161`          |
| `40.76.166.156`          |
| `40.76.166.166`          |
| `40.76.166.160`          |
| `40.88.51.74`            |
| `52.154.67.17`           |
| `40.76.166.80`           |
| `40.76.166.84`           |
| `40.76.166.85`           |
| `40.76.166.81`           |
| `40.76.166.71`           |
| `40.76.166.144`          |
| `40.76.166.145`          |

## Utilisation de webhooks

Il y a plusieurs façons d'utiliser les webhooks, et avec les partenaires technologiques de Braze (alliages), vous pouvez utiliser des webhooks pour diffuser votre communication directement avec vos clients et vos utilisateurs.

Départ :
* [Messager]({{site.baseurl}}/partners/additional_channels/instant_chat/messenger/)
* [Rafraîchir]({{site.baseurl}}/partners/advertising_technologies/retargeting/remerge/)
* [Lob.com]({{site.baseurl}}/partners/additional_channels/direct_mail/lob/)
* Et bien plus de nos [partenaires technologiques]({{site.baseurl}}/partners/home/)!
[21]: {% image_buster /assets/img/webhook_JSON1.png %} [22]: {% image_buster /assets/img_archive/webhook_rawtext.png %} [26]: {% image_buster /assets/img_archive/Webhook_Request_Header. ng %} [43]: {% image_buster /assets/img_archive/webhook-error.png %} [64]: {% image_buster /assets/img_archive/webhook_test_send.png %}

[14]: https://sendgrid.com/blog/whats-webhook
[15]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[16]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#additional-notes-and-best-practices
[18]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[42]: https://dashboard-01.braze.com/app_settings/developer_console/
