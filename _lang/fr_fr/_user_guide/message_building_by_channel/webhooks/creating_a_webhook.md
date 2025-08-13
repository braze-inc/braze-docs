---
nav_title: Créer un webhook
article_title: Créer un webhook
page_order: 1
channel:
  - webhooks
description: "Cet article de référence explique comment créer et configurer une campagne webhook."
search_rank: 2
---

# Créer une campagne webhook

> La création d'une campagne webhook ou l'inclusion d'un webhook dans une campagne multicanal vous permet de déclencher des actions non liées à l'application en fournissant à d'autres systèmes et applications des informations en temps réel. 

Vous pouvez utiliser les webhooks pour envoyer des informations à des systèmes, tels que Salesforce ou Marketo, ou à vos systèmes dorsaux. Par exemple, vous pourriez vouloir créditer les comptes de vos clients d'une promotion après qu'ils aient effectué un événement personnalisé un certain nombre de fois.

{% alert tip %}
Pour en savoir plus sur ce que sont les webhooks et sur la manière dont vous pouvez les utiliser dans Braze, consultez la rubrique [À propos des webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) avant de poursuivre.
{% endalert %}

## Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont mieux adaptées aux campagnes de communication simples et uniques, tandis que les Canvas sont mieux adaptés aux parcours client en plusieurs étapes.

{% tabs %}
{% tab Campagne %}

**Étapes :**

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne**.
2. Sélectionnez **Webhook** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multichannel**.
3. Donnez un nom clair et significatif à votre campagne.
4. (Facultatif) Ajoutez une description pour décrire comment cette campagne sera utilisée.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire.
   * Les balises facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer les éléments en fonction de certaines étiquettes spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez utiliser différents modèles de webhook pour chacune des variantes que vous ajoutez. Pour plus d'informations sur ce sujet, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d’ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans la liste déroulante **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Étapes :**

1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le Créateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Choisissez un [calendrier par étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d’audience seront vérifiées après le délai au moment de l’envoi des messages.
5. Choisissez votre [comportement d'avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Créez votre webhook

Vous pouvez choisir de créer un webhook à partir de zéro, d'utiliser un modèle existant ou d'utiliser l'un de nos modèles existants. Ensuite, créez votre webhook dans l'onglet **Compose** de l'éditeur.

L'onglet **Composer** comprend les champs suivants :

- Langue
- URL du webhook
- Méthode HTTP
- Corps de la demande

![L'onglet "Compose" avec un exemple de modèle de webhook.]({% image_buster /assets/img_archive/webhook_compose.png %})

#### Langue {#internationalization}

L'[internationalisation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) est prise en charge dans l'URL et le corps de la requête. Pour internationaliser votre message, sélectionnez **Ajouter des langues** et remplissez les champs requis. 

Nous vous recommandons de sélectionner vos langues avant d’écrire votre contenu afin que vous puissiez remplir votre texte dans Liquid. Pour obtenir la liste complète des langues que vous pouvez utiliser, reportez-vous à la section [Langues prises en charge.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported)

Si vous ajoutez du texte dans une langue qui s'écrit de droite à gauche, notez que l'aspect final des messages écrits de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les meilleures pratiques en matière d'élaboration de messages de droite à gauche qui s'affichent le plus précisément possible, reportez-vous à la section [Création de messages de droite à gauche.]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)

#### URL du webhook

L’URL du webhook, ou l’URL HTTP, définit votre endpoint. L’endpoint est l’endroit où vous enverrez les informations que vous capturez dans le webhook. 

Si vous désirez envoyer une information à un vendeur, le vendeur doit fournir cette URL dans la documentation de son API. Si vous envoyez des informations à vos propres systèmes, vérifiez auprès de votre équipe de développement ou d'ingénierie que vous utilisez l'URL correcte. 

Braze autorise uniquement les URL qui communiquent sur les ports `80` (HTTP) et `443` (HTTPS) standard.

##### Utilisation de Liquid

Vous pouvez personnaliser les URL de vos webhooks à l'aide de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/). Il peut parfois arriver que certains endpoints vous demandent d’identifier un utilisateur pour fournir une information qui lui est spécifique au sein de l’URL. Lorsque vous utilisez Liquid, veillez à inclure une [valeur par défaut]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) pour chaque information spécifique à l'utilisateur que vous utilisez dans votre URL.

#### Méthode HTTP

La [méthode HTTP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#methods) que vous devez utiliser varie en fonction de l'endpoint auquel vous envoyez des informations. Dans la plupart des cas, vous utiliserez POST.

#### Corps de la demande

Le corps de la requête est l’information qui sera envoyée à l’URL que vous avez définie. Vous pouvez créer le corps de votre demande de webhook avec des paires clé-valeur JSON ou du texte brut.

##### Paires clé-valeur JSON

Les paires clé-valeur JSON vous permettent d’écrire facilement une requête pour un endpoint qui attend un format JSON. Vous ne pouvez l'utiliser qu'avec un endpoint qui attend une requête JSON. Par exemple, si votre clé est `message_body`, la valeur correspondante pourrait être `Your order just arrived!`. Après avoir entré la paire clé-valeur, le composeur configurera votre requête en syntaxe JSON et une prévisualisation de votre requête JSON se remplira automatiquement.

![Le corps de la requête est constitué de paires clé-valeur JSON.]({% image_buster /assets/img/webhook_json_1.png %})

Vous pouvez personnaliser vos paires clé-valeur à l'aide de Liquid, par exemple en incluant tout attribut utilisateur, [attribut personnalisé]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#additional-notes-and-best-practices) ou [propriété d'événement]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) dans votre requête. Vous pouvez par exemple ajouter le prénom et l’e-mail d’un client dans votre requête. Veillez à inclure une [valeur par défaut]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) pour chaque attribut.

##### Texte brut

L’option de texte brut permet une flexibilité pour écrire une requête pour un endpoint qui attend un corps de n’importe quel format. Par exemple, vous pouvez l'utiliser pour écrire une requête pour un endpoint qui s'attend à ce que votre requête soit au format XML. 

La [personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) et l'[internationalisation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) à l'aide de Liquid sont prises en charge dans le texte brut.

![Exemple d'un corps de requête avec du texte brut utilisant Liquid.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

Si vous attribuez la valeur `application/x-www-form-url-encoded` à l'[en-tête de requête](#request-headers-optional) `Content-Type`, le corps de la requête doit être formaté sous la forme d'une chaîne de caractères codée en URL. Par exemple :

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![Corps de la requête avec une chaîne de caractères codée en URL.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## Étape 3 : Configurer des paramètres supplémentaires

#### En-têtes de requête (optionnel)

Certains endpoints peuvent nécessiter d’ajouter des en-têtes à vos requêtes. Dans la section **Composer** du compositeur, vous pouvez ajouter autant d'en-têtes que nécessaire.

![Exemples d'en-têtes de requête pour les clés "Authorization" et "Content-Type".]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

Les en-têtes de requête les plus courants sont les spécifications `Content-Type` (qui décrivent le type de données à attendre dans le corps, comme XML ou JSON) et les en-têtes d'autorisation qui contiennent vos informations d'identification auprès de votre fournisseur ou de votre système. 

Les spécifications de type de contenu doivent utiliser la clé `Content-Type`. Des valeurs fréquentes sont `application/json` ou `application/x-www-form-urlencoded`.

Les en-têtes de permission doivent utiliser la clé `Authorization`. Les valeurs courantes sont {% raw %} `Bearer {{YOUR_TOKEN}}` ou `Basic {{YOUR_TOKEN}}` {% endraw %}, où `YOUR_TOKEN` correspond aux identifiants communiqués par votre fournisseur ou votre système.

## Étape 4 : Tester l’envoi de votre message

Avant de déployer votre campagne, Braze recommande de tester le webhook pour vous assurer que la requête est formatée correctement.

Pour ce faire, passez à l'onglet **Test** et envoyez un webhook de test. Vous pouvez tester le webhook en tant qu’utilisateur aléatoire, utilisateur spécifique (en saisissant son adresse e-mail ou son ID utilisateur externe) ou un utilisateur personnalisé avec les attributs de votre choix.  

Après avoir envoyé le test de webhook, un dialogue s’affichera avec le message en réponse. Si la requête webhook échoue, consultez le message d’erreur pour obtenir de l’aide pour la résolution des problèmes de votre webhook. L’exemple suivant détaille la réponse d’un webhook ayant une URL de webhook invalide.

```json
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

## Étape 5 : Créer le reste de votre campagne ou de votre Canvas

{% tabs %}
{% tab Campagne %}

Concevez ensuite le reste de votre campagne. Consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des webhooks.

#### Choisir un calendrier ou un déclencheur pour la livraison

Les webhooks peuvent être livrés en fonction d’un calendrier, d’un événement ou d’un déclencheur API. Pour en savoir plus, reportez-vous à la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour une livraison basée sur l'action, vous pouvez également définir la durée de la campagne et les [Heures de silence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

C'est également à cette étape que vous pouvez spécifier les contrôles de réception/distribution, par exemple en autorisant les utilisateurs à se [réinscrire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne ou en activant les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en choisissant des segments ou des filtres pour réduire votre audience. Au cours de cette étape, vous allez sélectionner une audience plus importante dans vos segments et allez restreindre peut-être davantage ce segment à l’aide de nos filtres. Vous recevez automatiquement un aperçu de ce à quoi ressemble la population approximative du segment à ce moment-là. Gardez à l’esprit que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.

#### Sélectionner des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d’autoriser une fenêtre allant jusqu’à 30 jours pendant laquelle une conversion sera comptée si l’utilisateur entreprend l’action spécifiée.

{% endtab %}

{% tab Canvas %}

Si vous ne l’avez pas déjà fait, terminez les sections restantes de votre étape de Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les tests multivariés et la sélection intelligente, et plus encore, reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation sur le Canvas.

{% endtab %}
{% endtabs %}

## Étape 6 : Revue et déploiement

Quand vous avez fini de concevoir votre campagne ou votre Canvas, vérifiez ses détails, testez-le et envoyez-le !

## Choses à savoir

### Erreurs, logique de nouvel essai et temporisation

Les webhooks reposent sur les serveurs Braze qui effectuent des requêtes vers un endpoint externe, et des erreurs peuvent occasionnellement se produire. Les erreurs les plus courantes sont les erreurs de syntaxe, les clés API expirées, les limites de débit et les problèmes inattendus côté serveur. Avant d'envoyer une campagne webhook :

- Testez votre webhook pour détecter les erreurs de syntaxe
- Veillez à ce que les variables personnalisées aient des valeurs par défaut

Si votre webhook ne parvient pas à être envoyé, un message d'erreur est enregistré dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) et contient des informations telles que l'horodatage de l'erreur, le nom de l'application et des détails sur l'erreur.

![Erreur webhook avec le message "Un jeton d'accès actif doit être utilisé pour demander des informations sur l'utilisateur actuel".]({% image_buster /assets/img_archive/webhook-error.png %})

Si le message d'erreur n'est pas suffisamment clair quant à la source de l'erreur, vous devez consulter la documentation du point de terminaison de l'API que vous utilisez. Elle fournit généralement une explication des codes d’erreur utilisés par l’endpoint ainsi que ce qui les entraîne le plus souvent.

#### Codes de réponse et logique de relance

Lorsque la requête webhook est envoyée, le serveur qui la reçoit renverra un code de réponse indiquant ce qui est arrivé à la requête. Le tableau suivant résume les différentes réponses que le serveur peut envoyer, l'impact qu'elles ont sur l'analyse/analytique de la campagne et si, en cas d'erreur, Braze tentera de rediffuser la campagne :

| Code de réponse | Marqué comme reçu ? | Nouvel essai ? |
|---------------|-----------|----------|
| `20x` (succès)  | Oui |   N/A  |
| `30x` (redirection)  | Non | Non |
| `408` (délai d'attente de la demande)  | Non | Oui |
| `429` (limite de débit)  | Non | Oui |
| `Other 4XX` (erreur du client)  | Non | Non |
| `5XX` (erreur de serveur)   | Non | Oui |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Braze retente les codes d'état ci-dessus jusqu'à cinq fois en l'espace de 30 minutes en utilisant des délais exponentiels. Si nous ne parvenons pas à atteindre votre endpoint, les tentatives peuvent s'étaler sur une période de 24 heures.<br><br>Chaque webhook a 90 secondes avant qu’il ne s’arrête.
{% endalert %}

#### Résolution des problèmes et détails supplémentaires sur les erreurs

Pour obtenir des explications détaillées, des étapes de dépannage et des conseils sur la résolution d'erreurs spécifiques de webhook, reportez-vous à la section [Dépannage des demandes de webhook et de contenu connecté.]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors/) Vous trouverez également plus d'explications sur le fonctionnement de notre système de détection des hôtes malsains et sur la manière dont Braze fournit des notifications d'erreur par le biais d'e-mails automatisés et d'une journalisation supplémentaire dans Braze Currents.

### Liste d'adresses IP autorisées {#ip-allowlisting}

Lorsqu'un webhook est envoyé par Braze, les serveurs de Braze adressent des demandes de réseau à nos clients ou à des serveurs tiers. Grâce à la liste des adresses IP autorisées, vous pouvez vérifier que les demandes de webhook proviennent réellement de Braze, ce qui ajoute une couche de sécurité.

Braze enverra des webhooks depuis les adresses IP suivantes. Les adresses IP répertoriées sont automatiquement et dynamiquement ajoutées à toutes les clés API qui ont fait l'objet d'un abonnement à l'inscription sur la liste d'exclusion.

{% alert important %}
Si vous créez un webhook Braze à Braze et que vous utilisez la liste des adresses IP autorisées, vous devez autoriser toutes les adresses IP suivantes, y compris `127.0.0.1`.
{% endalert %}

{% multi_lang_include data_centers.md datacenters='ips' %}

### Utilisation des webhooks avec les partenaires de Braze {#utilizing-webhooks}

Il existe de nombreuses façons d'utiliser les webhooks, et avec nos partenaires technologiques (Alloys), vous pouvez utiliser les webhooks pour améliorer votre communication directement avec vos clients et utilisateurs.

Consultez :
* [Messenger]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/remerge/)
* [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/)
* Et bien d'autres de nos [partenaires technologiques]({{site.baseurl}}/partners/home/) !


