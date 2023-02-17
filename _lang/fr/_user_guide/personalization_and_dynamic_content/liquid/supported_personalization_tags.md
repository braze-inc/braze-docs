---
nav_title: Balises de personnalisation prises en charge
article_title: Balises de personnalisation prises en charge
page_order: 1
description: "Le présent article de référence couvre une liste complète des balises de personnalisation Liquid prises en charge."
search_rank: 1
---

# Balises de personnalisation prises en charge

Un résumé des balises de personnalisation prises en charge est fourni. Pour des précisions sur chaque type de balise et les meilleures pratiques, continuez à lire.

{% raw %}

|Type de balise de personnalisation | Balise |
| -------------  | ---- |
| Attributs Standards (par défaut) | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${twitter_handle}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| Attributs de l’appareil | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| [Attributs de la liste d’e-mails][43] | `{{${set_user_to_unsubscribed_url}}}` <br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}`|
| [Attributs SMS][48] | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| Campagne attribuée | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Attributs de Canvas | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| Attributs de Canvas Step | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Attributs de la carte | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| Événements de geofence | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| Propriétés de l’événement <br> (spécifiques à votre groupe d'apps).| `{{event_properties.${your_custom_event_property}}}` |
| Propriétés d’entrées de Canvas| `{{canvas_entry_properties}}` |
| Attributs personnalisés <br> (spécifiques à votre groupe d'apps). | `{{custom_attribute.${your_custom_attribute}}}` |
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}

Consultez le présent article d’aide pour en savoir plus sur [comment certains de ces attributs diffèrent entre les sources de Braze]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/).

{% alert important %}
Les attributs Campagne, Carte et Canvas sont uniquement pris en charge dans leurs modèles de messagerie correspondants (par exemple, `dispatch_id` n’est pas disponible dans les campagnes de messages dans l’application).
{% endalert %}

#### Différences entre les balises de Campagne et de Canvas 

Le comportement des balises suivantes diffère entre Canvas et campagnes :
{% raw %}
- `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les Canvas Step comme des événements déclenchés, même lorsqu'elles sont « planifiées » (à l'exception des Entry Steps, qui peuvent être planifiées). Pour en savoir plus, consultez [Comportement de l’ID Dispatch]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- Utiliser la balise `{{campaign.${name}}}` avec Canvas va afficher le nom du composant Canvas. Lorsque vous utilisez cette balise avec des campagnes, elle affiche le nom de la campagne.
{% endraw %}

## Informations sur les appareils les plus récemment utilisées

Vous pouvez modéliser les attributs suivants pour l’appareil le plus récent de l’utilisateur sur toutes les plateformes. Si un utilisateur n’a pas utilisé votre application (par ex., vous avez importé l’utilisateur via l’API REST), ces valeurs seront toutes `null`.

{% raw %}

|Balise | Description |
|---|---|
|`{{most_recently_used_device.${browser}}}` | Le navigateur le plus récemment utilisé sur l’appareil de l’utilisateur. Par exemple, « Chrome » et « Safari ». |
|`{{most_recently_used_device.${id}}}` | Il s’agit de l’identifiant de l’appareil Braze. Sur iOS, il s’agit de l’identifiant Apple pour le fournisseur (IDFV) ou un UUID. Pour Android et d’autres plateformes, il s’agit d’un UUID généré aléatoirement. |
| `{{most_recently_used_device.${carrier}}}` | Le fournisseur de téléphonie le plus récemment utilisé, le cas échéant. Par exemple, « Verizon » et « Orange ». |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | Si le traçage de publicité est activé ou non sur l’appareil. Il s’agit d’une valeur booléenne (`true` ou `false`). |
| `{{most_recently_used_device.${idfa}}}` | Pour les appareils iOS, cette valeur sera l’identifiant de publicité (IDFA) si votre application est configurée avec [collection IDFA facultative de Braze][40]. Pour les périphériques non iOS, cette valeur sera nulle. |
| `{{most_recently_used_device.${google_ad_id}}}` | Pour les appareils Android, cette valeur sera l'identifiant publicitaire Google Play si votre application est configurée avec la collection facultative d'ID publicitaires Google Play de Braze. Pour les périphériques non Android, cette valeur sera nulle. |
| `{{most_recently_used_device.${roku_ad_id}}}` | Pour les appareils Roku, cette valeur sera l’identifiant Roku Advertising collectée configurée lorsque votre application est configurée avec Braze Pour les périphériques non Roku, cette valeur sera nulle. |
| `{{most_recently_used_device.${model}}}` | Le nom du modèle du dispositif, si disponible. Par exemple, « iPhone 6S » et « Nexus 6P » et « Firefox ». |
| `{{most_recently_used_device.${os}}}` | Le système d’exploitation du dispositif, si disponible. Par exemple, « iOS 9.2.1 » et « Android (Lollipop) » et « Windows ». |
| `{{most_recently_used_device.${platform}}}` | La plate-forme de l’appareil, si disponible. Si cette valeur est définie, la valeur va correspondre à `ios`, `android`, `kindle`, `android_china`, `web` ou `tvos`. |
{: .reset-td-br-1 .reset-td-br-2}


Étant donné qu’il existe une large gamme de supports de dispositifs, de noms de modèles et de systèmes d’exploitation, nous vous conseillons de tester minutieusement tout Liquid qui dépend de manière conditionnelle de l’une de ces valeurs. Ces valeurs seront `null` s’ils ne sont pas disponibles sur un appareil particulier.

## Informations sur les dispositifs ciblés

Pour les canaux de notification push et les Messages in-app, vous pouvez modéliser les attributs suivants pour l’appareil auquel un message est envoyé. C’est-à-dire, une notification push ou un message in-app peut inclure des attributs de périphérique de l’appareil sur lequel le message est lu. Veuillez remarquer que ces attributs ne fonctionnent pas pour les cartes de contenu. 

|Balise | Description |
|------------------|---|
| `{{targeted_device.${id}}}` | Il s’agit de l’identifiant de l’appareil Braze. Sur iOS, il s’agit de l’identifiant Apple pour le fournisseur (IDFV) ou un UUID. Pour Android et d’autres plateformes, il s’agit d’un UUID généré aléatoirement. |
| `{{targeted_device.${carrier}}}` | Le fournisseur de téléphonie le plus récemment utilisé, le cas échéant. Par exemple, « Verizon » et « Orange ». |
| `{{targeted_device.${idfa}}}` | Pour les appareils iOS, cette valeur sera l’identifiant de publicité (IDFA) si votre application est configurée avec [collection IDFA facultative de Braze][40]. Pour les périphériques non iOS, cette valeur sera nulle. |
| `{{targeted_device.${google_ad_id}}}` | Pour les appareils Android, cette valeur sera l’identifiant Google Play Advertising si votre application est configurée avec [Collection Google Play Advertising ID facultative] de Braze. Pour les périphériques non Android, cette valeur sera nulle. |
| `{{targeted_device.${roku_ad_id}}}` | Pour les appareils Roku, cette valeur sera l’identifiant Roku Advertising collectée configurée lorsque votre application est configurée avec Braze Pour les périphériques non Roku, cette valeur sera nulle. |
| `{{targeted_device.${model}}}` | Le nom du modèle du dispositif, si disponible. Par exemple, « iPhone 6S » et « Nexus 6P » et « Firefox ». |
| `{{targeted_device.${os}}}` | Le système d’exploitation du dispositif, si disponible. Par exemple, « iOS 9.2.1 » et « Android (Lollipop) » et « Windows ». |
| `{{targeted_device.${platform}}}` | La plate-forme de l’appareil, si disponible. Si cette valeur est définie, la valeur va correspondre à `ios`, `android`, `kindle`, `android_china`, `web` ou `tvos`. Vous pouvez également utiliser la balise de personnalisation `most_recently_used_device`. |
| `{{targeted_device.${foreground_push_enabled}}}` | Cette valeur sera `true` lorsque le dispositif ciblé est activé pour la notification push de premier plan, `false` autrement. |
{: .reset-td-br-1 .reset-td-br-2}


{% endraw %}


Étant donné qu’il existe une large gamme de supports de dispositifs, de noms de modèles et de systèmes d’exploitation, nous vous conseillons de tester minutieusement toute logique qui dépend de manière conditionnelle de l’une de ces valeurs. Ces valeurs seront `null` si elles ne sont pas disponibles sur un appareil particulier. De plus, pour les notifications push, il est possible que Braze ne puisse pas discerner le dispositif joint à la notification push dans certaines circonstances, comme si le jeton de pression a été importé via API, ce qui a entraîné des valeurs `null` pour ces messages.

![Exemple d’utilisation d’une valeur par défaut de « là » lors de l’utilisation d’une variable de prénom dans un message de notification push.][4]

Dans certains cas, vous pouvez choisir d’utiliser la [logique conditionnelle][17] au lieu de définir une valeur par défaut. La logique conditionnelle vous permet d’envoyer des messages qui diffèrent selon la valeur d’un attribut personnalisé.

De plus, vous pouvez utiliser la logique conditionnelle pour [interrompre des messages][18] aux clients avec des valeurs d’attribut nulles ou vierges.

Par exemple, si vous envoyez une notification de solde de récompense aux clients, il n’existe pas de bon moyen de tenir compte des clients dont les soldes sont faibles et nuls à l’aide de valeurs par défaut.

Dans ce cas, il existe deux options qui peuvent mieux fonctionner que la définition d’une valeur par défaut :

1. Abandonnez le message pour les clients dont les soldes sont faibles, nuls et vides.

{% raw %}

   ```Liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Votre solde de récompenses est {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. Envoyez un message complètement différent à ces clients, peut-être quelque chose comme :

{% raw %}

   ```Liquid
   {% if ${first_name} != blank and ${first_name} != null %}
Bonjour {{${first_name} | default: ' '}}, merci d’avoir téléchargé notre appli !
   {% else %}
Merci d’avoir téléchargé notre appli !
   {% endif %}
   ```

Dans cet exemple, un utilisateur avec un prénom vide ou nul recevra le message « Merci de votre téléchargement ». Vous devez inclure une [valeur par défaut][47] pour le prénom pour être sûr que votre client ne voit pas le Liquid en cas d’erreur.

{% endraw %}

## Variables Balises

Vous pouvez utiliser la balise `assign` pour créer une variable dans le compositeur de message. Une fois que vous avez créé une variable, vous pouvez référencer cette variable dans votre logique de messagerie ou votre message.

Disons que vous permettez à vos clients de gagner des points dans leurs points de récompense, une fois qu’ils auront accumulé 100 points de récompense. Donc, vous ne voulez envoyer que des messages aux clients ayant un solde de points supérieur ou égal à 100 s’ils ont fait cet achat supplémentaire :

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Faites un achat pour monter vos points de récompense à {{new_points_balance}} et encaisser dès aujourd'hui !
{% else %}
{% abort_message('nombre points insuffisant') %}
{% endif %}
```
Cette balise est pratique lorsque vous souhaitez reformater le contenu retourné de notre [Contenu connecté][4]. Vous pouvez en lire davantage dans la documentation de Shopify sur les [balises variables][31].

{% endraw %}

{% alert tip %}
Vous envoyez les mêmes variables dans chaque message ? Au lieu d’écrire la balise `assign` sans arrêt vous pouvez enregistrer cette balise comme un bloc de contenu et la placer en haut de votre message.

1. [Créer un bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block)
2. Donnez un nom à votre bloc de contenu (aucun espace ni caractère spécial).
3. Cliquez sur **Modifier** au bas de la page.
4. Saisisse votre balise `assign` .

Tant que le bloc de contenu est en haut de votre message, chaque fois que la variable est insérée dans votre message comme objet, elle se rapporte à l’attribut personnalisé que vous avez choisi !
{% endalert %}

## Balises d’itération

{% raw %}
Les balises d’itération peuvent être utilisées pour exécuter un bloc de code à plusieurs reprises. Cet exemple présente la balise `for`.

Disons que vous avez une vente sur les baskets Nike et que vous souhaitez envoyer des messages aux clients qui ont exprimé leur intérêt pour Nike. Vous disposez d’un éventail de marques de produits consultées sur le profil de chaque client. Cette baie peut contenir jusqu’à 25 marques de produits, mais vous ne voulez envoyer que des messages aux clients qui ont vu un produit Nike en tant que leurs 5 vues de produits les plus récentes.

```liquid
{% for items in {{custom_attribute.${Brands Viewed}}} limit:5 %}
{% if {{items}} contains 'Converse' %}
{% assign converse_viewer = true %}
{% endif %}
{% endfor %}
{% if converse_viewer == true %}
Vente sur Converse !
{% else %}
{% abort_message() %}
{% endif %}
```

Dans cet exemple, nous vérifions les cinq premiers articles de la gamme de baskets vues. Si l’un de ces articles est Converse, nous créons la variable de visualisation converse_viewer et la paramétrons sur Vrai.

Ensuite, nous envoyons le message de vente lorsque converse_viewer est vrai. Sinon, nous abandonnons le message.

Il s’agit d’un simple exemple de la manière dont les balises d’itération peuvent être utilisées dans le compositeur de messages de Braze. Vous trouverez plus d’informations dans la documentation de Shopify sur [balises d’itération][32].

## Balises Syntax

Les balises Syntax peuvent être utilisées pour contrôler le rendu de Liquid. La balise `echo` permet de renvoyer une expression. Cette opération est identique à l'habillage d'une expression à l'aide d'accolades, sauf que vous pouvez utiliser cette balise dans les balises Liquid. Vous pouvez également utiliser la balise `Liquid` pour disposer d'un bloc Liquid sans séparateur sur chaque balise. Chaque étiquette doit être sur sa propre ligne lors de l'utilisation de la balise `Liquid`. Consultez la documentation de Shopify sur les [balises de syntaxe][33] pour plus d'informations et d'exemples.

Avec le [contrôle des espaces blancs][49], vous pouvez supprimer les espaces blancs autour de vos balises, ce qui vous aide à mieux contrôler l'aspect de la sortie Liquid.

## Balise de thème

Les balises de thème peuvent affecter du contenu qui fait partie de votre thème. Braze prend actuellement en charge la balise `render`, qui vous permet de rendre un extrait de code ou un bloc d'application. Pour plus d'informations, consultez la documentation de Shopify sur les [balises `render`][30].

## Codes de statut HTTP {#http-personalization}

Vous pouvez utiliser l’état HTTP d’un appel de [Contenu connecté][38] en l’enregistrant d’abord comme variable locale, puis en utilisant la clé`__http_status_code__` . Par exemple :

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Le contenu connecté a renvoyé un code d'état autre que 200') %}
{% endif %}
```
{% endraw %}

{% alert note %}
  Cette clé ne sera ajoutée automatiquement à l’objet Contenu connecté que si l’endpoint renvoie un objet JSON. Si l’endpoint renvoie une baie ou un autre type, cette clé ne peut alors pas être définie automatiquement dans la réponse.
{% endalert %}

## Envoi de messages en fonction de la langue, des paramètres régionaux les plus récents et du fuseau horaire

Dans certains cas, vous pouvez envoyer des messages spécifiques à des paramètres régionaux particuliers. Par exemple, le portugais brésilien est généralement différent du portugais européen.

Voici un exemple de la façon dont vous pouvez utiliser le paramètre régional le plus récente pour mieux localiser un message internationalisé.

{% raw %}

```liquid
{% if ${language} == 'en' %}
Message en anglais
{% elsif  ${language} == 'fr' %}
Message en français
{% elsif  ${language} == 'ja' %}
Message en japonais
{% elsif  ${language} == 'ko' %}
Message en coréen
{% elsif  ${language} == 'ru' %}
Message en russe
{% elsif ${most_recent_locale} == 'pt_BR' %}
Message en portugais brésilien
{% elsif ${most_recent_locale} == 'pt_PT' %}
Message en portugais européen
{% elsif  ${language} == 'pt' %}
Message en portugais
{% else %}
Message dans la langue par défaut
{% endif %}
```

Dans cet exemple, les clients ayant « pt BR » comme dernier paramètre régional  recevront un message en portugais brésilien, les clients ayant « pt PT » comme dernier paramètre régional recevront un message en portugais européen et les clients qui ne répondent pas aux deux premières conditions, mais qui ont leur langue définie sur Portugais recevront un message dans la langue portugaise par défaut que vous avez définie.

Vous pouvez également cibler les utilisateurs en fonction de leur fuseau horaire. Par exemple, envoyer un message s’ils sont situés dans EST et un autre s’ils sont situés dans PST. Pour ce faire, enregistrez l’heure actuelle dans UTC et comparez une déclaration if/else avec l’heure actuelle de l’utilisateur pour vous assurer que vous envoyez le bon message pour le bon fuseau horaire. Vous devez définir la campagne à envoyer dans le fuseau horaire local de l’utilisateur, afin de vous assurer qu’il reçoit la campagne au bon moment. Voir l’exemple suivant pour savoir comment écrire un message qui partira entre 14h et 15h et un message spécifique pour chaque fuseau horaire.

```liquid
{% assign hour_in_utc = 'now' | date: '%H' | plus:0 %}
{% if hour_in_utc >= 19 && hour_in_utc < 20 %}
Il est entre 14:00:00 et 14:59:59 (Heure de l’Est) !
{% elsif hour_in_utc >= 22 && hour_in_utc < 23 %}
Il est entre 14:00:00 et 14:59:59 (Heure de l’Est) !
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

[30]: https://shopify.dev/api/liquid/tags#syntax-tags
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[33]: https://shopify.dev/api/liquid/tags#syntax-tags
[38]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[4]: {% image_buster /assets/img_archive/personalized_firstname_.png %}
[17]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/
[43]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[47]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
[48]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#trigger-messages-by-keyword
[49]: https://shopify.github.io/liquid/basics/whitespace/
