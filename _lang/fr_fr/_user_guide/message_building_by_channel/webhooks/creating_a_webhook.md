---
nav_title: "Création d'un webhook"
article_title: "Création d'un webhook"
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

## Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé par le biais d'une campagne ou d'un canvas ? Les campagnes sont plus adaptées aux campagnes d'envoi de messages simples et uniques, tandis que les Canevas sont plus adaptés aux parcours utilisateurs en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

**Les étapes :**

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne.**
2. Sélectionnez **Webhook** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multichannel**.
3. Donnez à votre campagne un nom clair et significatif.
4. (Facultatif) Ajoutez une description pour décrire comment cette campagne sera utilisée.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire.
   * Les étiquettes facilitent la recherche de vos campagnes et permettent de créer des rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer par des étiquettes particulières.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir des modèles de webhook différents pour chacune des variantes que vous avez ajoutées. Pour en savoir plus sur ce sujet, reportez-vous aux [tests multivariés et aux tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne seront similaires ou auront le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans la liste déroulante **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Les étapes :**

1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre canvas, ajoutez une étape dans le générateur de canvas. Donnez à votre démarche un nom clair et significatif.
3. Choisissez une [planification des étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape si nécessaire. Vous pouvez encore affiner les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience seront vérifiées après le délai au moment de l'envoi des messages.
5. Choisissez votre [comportement en matière d'avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Créez votre webhook

Vous pouvez choisir de créer un webhook à partir de zéro, d'utiliser un modèle existant ou d'utiliser l'un de nos modèles existants. Ensuite, créez votre webhook dans l'onglet **Compose** de l'éditeur.

L'onglet **Composer** comprend les champs suivants :

- Langue
- URL du webhook
- Méthode HTTP
- Corps de la demande

\![L'onglet "Compose" avec un exemple de modèle de webhook.]({% image_buster /assets/img_archive/webhook_compose.png %})

#### Langue {#internationalization}

L'[internationalisation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) est prise en charge dans l'URL et le corps de la requête. Pour internationaliser votre message, sélectionnez **Ajouter des langues** et remplissez les champs requis. 

Nous vous recommandons de sélectionner vos langues avant de rédiger votre contenu afin de pouvoir remplir votre texte à l'endroit voulu dans le Liquid. Pour obtenir la liste complète des langues que vous pouvez utiliser, reportez-vous à la section [Langues prises en charge.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported)

Si vous ajoutez du texte dans une langue qui s'écrit de droite à gauche, notez que l'aspect final des messages écrits de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les meilleures pratiques en matière d'élaboration de messages de droite à gauche qui s'affichent le plus précisément possible, reportez-vous à la section [Création de messages de droite à gauche.]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)

#### URL du webhook

L'URL du webhook, ou URL HTTP, spécifie votre endpoint. L'endpoint est l'endroit où vous enverrez les informations que vous capturez dans le webhook. 

Si vous souhaitez envoyer des informations à un fournisseur, celui-ci doit fournir cette URL dans la documentation de son API. Si vous envoyez des informations à vos propres systèmes, vérifiez auprès de votre équipe de développement ou d'ingénierie que vous utilisez l'URL correcte. 

Braze n'autorise que les URL qui communiquent sur les ports standard `80` (HTTP) et `443` (HTTPS).

##### Utilisation du liquide

Vous pouvez personnaliser les URL de vos webhooks à l'aide de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/). Parfois, certains endpoints peuvent vous demander d'identifier un utilisateur ou de fournir des informations spécifiques à l'utilisateur dans le cadre de votre URL. Lorsque vous utilisez Liquid, veillez à inclure une [valeur par défaut]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) pour chaque information spécifique à l'utilisateur que vous utilisez dans votre URL.

#### Méthode HTTP

La [méthode HTTP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#methods) que vous devez utiliser varie en fonction de l'endpoint auquel vous envoyez des informations. Dans la plupart des cas, vous utiliserez POST.

#### Corps de la demande

Le corps de la requête est l'information qui sera envoyée à l'URL que vous avez spécifiée. Vous pouvez créer le corps de votre demande de webhook avec des paires clé-valeur JSON ou du texte brut.

##### Paires clé-valeur JSON

Les paires clé-valeur JSON vous permettent d'écrire facilement une requête pour un endpoint qui attend un format JSON. Vous ne pouvez l'utiliser qu'avec un endpoint qui attend une requête JSON. Par exemple, si votre clé est `message_body`, la valeur correspondante peut être `Your order just arrived!`. Après avoir saisi votre paire clé-valeur, le compositeur configurera votre demande en syntaxe JSON, et un aperçu de votre demande JSON s'affichera automatiquement.

\![Le corps de la demande est constitué de paires clé-valeur JSON.]({% image_buster /assets/img/webhook_json_1.png %})

Vous pouvez personnaliser vos paires clé-valeur à l'aide de Liquid, par exemple en incluant tout attribut utilisateur, [attribut personnalisé]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#additional-notes-and-best-practices) ou [propriété d'événement]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) dans votre requête. Par exemple, vous pouvez inclure le prénom et l'e-mail d'un client dans votre demande. Veillez à inclure une [valeur par défaut]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) pour chaque attribut.

##### Texte brut

L'option texte brut vous permet d'écrire une requête pour un endpoint qui attend un corps de n'importe quel format. Par exemple, vous pouvez l'utiliser pour écrire une requête pour un endpoint qui s'attend à ce que votre requête soit au format XML. 

La [personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) et l'[internationalisation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) à l'aide de Liquid sont prises en charge dans le texte brut.

Un exemple de corps de requête avec du texte brut utilisant Liquid.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

Si vous attribuez la valeur `application/x-www-form-url-encoded` à l'[en-tête de requête](#request-headers-optional) `Content-Type`, le corps de la requête doit être formaté sous la forme d'une chaîne de caractères codée en URL. Par exemple :

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

\![Chaîne de caractères codée en URL dans le corps de la requête.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## Étape 3 : Configurer des paramètres supplémentaires

#### En-têtes de la requête (optionnel)

Certains endpoints peuvent exiger que vous incluiez des en-têtes dans votre demande. Dans la section **Composer** du compositeur, vous pouvez ajouter autant d'en-têtes que nécessaire.

Exemples d'en-têtes de requête pour les clés "Authorization" et "Content-Type".]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

Les en-têtes de requête les plus courants sont les spécifications `Content-Type` (qui décrivent le type de données à attendre dans le corps, comme XML ou JSON) et les en-têtes d'autorisation qui contiennent vos informations d'identification auprès de votre fournisseur ou de votre système. 

Les spécifications de type de contenu doivent utiliser la clé `Content-Type`. Les valeurs courantes sont `application/json` ou `application/x-www-form-urlencoded`.

Les en-têtes d'autorisation doivent utiliser la clé `Authorization`. Les valeurs courantes sont {% raw %} `Bearer {{YOUR_TOKEN}}` ou `Basic {{YOUR_TOKEN}}` {% endraw %}, où `YOUR_TOKEN` correspond aux informations d'identification fournies par votre fournisseur ou votre système.

## Étape 4 : Testez l'envoi de votre message

Avant de mettre votre campagne en ligne/instantanée, Braze vous recommande de tester le webhook pour vous assurer que la demande est formatée correctement.

Pour ce faire, passez à l'onglet **Test** et envoyez un webhook de test. Vous pouvez tester le webhook en tant qu'utilisateur aléatoire, utilisateur spécifique (en saisissant son adresse e-mail ou son ID externe) ou utilisateur personnalisé avec les attributs de votre choix.  

Après avoir envoyé le webhook de test, une boîte de dialogue s'affiche avec le message de réponse. Si la demande de webhook n'aboutit pas, consultez le message d'erreur pour obtenir de l'aide dans la résolution des problèmes de votre webhook. L'exemple suivant détaille la réponse d'un webhook dont l'URL n'est pas valide.

```json
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

## Étape 5 : Créez le reste de votre campagne ou Canvas

{% tabs %}
{% tab Campaign %}

Ensuite, créez le reste de votre campagne. Consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des webhooks.

#### Choisissez la planification ou le déclencheur de la réception/distribution

Les webhooks peuvent être délivrés en fonction d'une heure planifiée, d'une action ou d'un déclencheur API. Pour en savoir plus, reportez-vous à la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour la réception/distribution par événement, vous pouvez également définir la durée de la campagne et les heures calmes.

C'est également à cette étape que vous pouvez spécifier les contrôles de réception/distribution, par exemple en autorisant les utilisateurs à se [réinscrire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne ou en activant les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisissez les utilisateurs à cibler

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en choisissant des segments ou des filtres pour réduire votre audience. Au cours de cette étape, vous sélectionnerez l'audience la plus large à partir de vos segments, et vous restreindrez davantage ce segment à l'aide de nos filtres, si vous le souhaitez. Vous obtiendrez automatiquement un aperçu de ce à quoi ressemble actuellement cette segmentation approximative de la population. N'oubliez pas que l'appartenance exacte à un segment est toujours calculée juste avant l'envoi du message.

{% multi_lang_include target_audiences.md %}

#### Choisissez des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}

{% tab Canvas %}

Si vous ne l'avez pas encore fait, complétez les sections restantes de votre étape du canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les tests multivariés et la sélection intelligente, et plus encore, reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation sur le Canvas.

{% endtab %}
{% endtabs %}

## Étape 6 : Examiner et déployer

Une fois que vous avez fini de créer la dernière partie de votre campagne ou de votre canvas, passez en revue ses détails, testez-le, puis envoyez-le !

## Ce qu'il faut savoir

### Erreurs, logique de réessai et délais d'attente

Les webhooks reposent sur les serveurs Braze qui effectuent des requêtes vers un endpoint externe, et des erreurs peuvent occasionnellement se produire. Les erreurs les plus courantes sont les erreurs de syntaxe, les clés API expirées, les limites de débit et les problèmes inattendus côté serveur. Avant d'envoyer une campagne webhook :

- Testez votre webhook pour détecter les erreurs de syntaxe
- Veillez à ce que les variables personnalisées aient des valeurs par défaut

Si votre webhook ne parvient pas à être envoyé, un message d'erreur est enregistré dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) et contient des informations telles que l'horodatage de l'erreur, le nom de l'application et des détails sur l'erreur.

Erreur de webhook avec le message "Un jeton d'accès actif doit être utilisé pour demander des informations sur l'utilisateur actuel".]({% image_buster /assets/img_archive/webhook-error.png %})

Si le message d'erreur n'est pas suffisamment clair quant à la source de l'erreur, vous devez consulter la documentation du point de terminaison de l'API que vous utilisez. Elles fournissent généralement une explication des codes d'erreur utilisés par l'endpoint, ainsi que de leur cause habituelle.

#### Codes de réponse et logique de relance

Lorsque la demande de webhook est envoyée, le serveur destinataire renvoie un code de réponse indiquant ce qui s'est passé avec la demande. Le tableau suivant résume les différentes réponses que le serveur peut envoyer, l'impact qu'elles ont sur l'analyse/analytique de la campagne et si, en cas d'erreur, Braze tentera de rediffuser la campagne :

| Code de réponse | Marqué comme reçu ? | Répétitions ? |
|---------------|-----------|----------|
| `20x` (succès)  | Oui |   N/A  |
| `30x` (redirection)  | Non | Non |
| `408` (délai d'attente de la demande)  | Non | Oui |
| `429` (limite de débit)  | Non | Oui |
| `Other 4XX` (erreur du client)  | Non | Non |
| `5XX` (erreur de serveur)   | Non | Oui |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Braze retente les codes d'état ci-dessus jusqu'à cinq fois en l'espace de 30 minutes en utilisant des délais exponentiels. Si nous ne parvenons pas à atteindre votre endpoint, les tentatives peuvent s'étaler sur une période de 24 heures.<br><br>Chaque webhook dispose de 90 secondes avant d'expirer.
{% endalert %}

#### Résolution des problèmes et détails supplémentaires sur les erreurs

Pour obtenir des explications détaillées, des étapes de dépannage et des conseils sur la résolution d'erreurs spécifiques de webhook, reportez-vous à la section [Dépannage des demandes de webhook et de contenu connecté.]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors/) Vous trouverez également plus d'explications sur le fonctionnement de notre système de détection des hôtes malsains et sur la manière dont Braze fournit des notifications d'erreur par le biais d'e-mails automatisés et d'une journalisation supplémentaire dans Braze Currents.

### Liste d'autorisation IP {#ip-allowlisting}

Lorsqu'un webhook est envoyé par Braze, les serveurs de Braze adressent des demandes de réseau à nos clients ou à des serveurs tiers. Grâce à l'IP allowlisting, vous pouvez vérifier que les demandes de webhook proviennent bien de Braze, ce qui ajoute une couche de sécurité.

Braze enverra des webhooks à partir des adresses IP suivantes. Les adresses IP répertoriées sont automatiquement et dynamiquement ajoutées à toutes les clés API qui ont fait l'objet d'un abonnement à l'inscription sur la liste d'exclusion.

{% alert important %}
Si vous créez un webhook Braze à Braze et que vous utilisez allowlisting, vous devez autoriser toutes les IP suivantes, y compris `127.0.0.1`.
{% endalert %}

{% multi_lang_include data_centers.md datacenters='ips' %}

### Utiliser les webhooks avec les partenaires de Braze {#utilizing-webhooks}

Il existe de nombreuses façons d'utiliser les webhooks, et avec nos partenaires technologiques (Alloys), vous pouvez utiliser les webhooks pour améliorer votre communication directement avec vos clients et utilisateurs.

Vérifiez :
* [Messager]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/remerge/)
* [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/)
* Et bien d'autres de nos [partenaires technologiques]({{site.baseurl}}/partners/home/)!


