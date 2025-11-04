---
nav_title: Tags de personnalisation pris en charge
article_title: Tags de personnalisation Liquid pris en charge
page_order: 1
description: "Cet article de référence présente une liste complète des étiquettes de personnalisation Liquid prises en charge."
search_rank: 1
---

# Tags de personnalisation pris en charge

> Cet article de référence présente une liste complète des étiquettes de personnalisation Liquid prises en charge.

## Résumé des étiquettes prises en charge

Pour plus de commodité, un résumé des tags de personnalisation pris en charge est fourni. Pour plus de détails sur chaque type d'étiquette et sur les meilleures pratiques, poursuivez votre lecture.

{% raw %}

| Type d'étiquette de personnalisation | Tags |
| -------------  | ---- |
| Attributs standard (par défaut) | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| Attributs de l'appareil | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions'>Attributs de la liste d'e-mails</a> | `{{${set_user_to_unsubscribed_url}}}` <br>Ce tag remplace l'ancienne étiquette `{{${unsubscribe_url}}}`. Bien que l'ancienne étiquette fonctionne toujours dans les e-mails créés précédemment, nous vous recommandons d'utiliser la nouvelle étiquette à la place. <br><br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}`|
| <a href='/docs/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/#trigger-messages'>Attributs du SMS</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/'>Attributs de WhatsApp</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` |
| Attributs de la campagne | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Attributs du canvas | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| Attributs de l'étape du canvas | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Attributs de la carte | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| Événements de géorepérage | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| Propriétés d'événement <br> (Ceux-ci sont personnalisés en fonction de votre espace de travail).| `{{event_properties.${your_custom_event_property}}}` |
| Variables de contexte Canvas | `{{context}}` |
| Attributs personnalisés <br> (Ceux-ci sont personnalisés en fonction de votre espace de travail). | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object/'>Propriétés du déclencheur API</a> |`{{api_trigger_properties}}` |
| Propriétés de l'entrée dans le canevas | `{{canvas_entry_properties.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### Attributs pris en charge

Les attributs Campaign, Card et Canvas ne sont pris en charge que dans les modèles d'envoi de messages correspondants (par exemple, `dispatch_id` n'est pas disponible dans les campagnes de messages in-app).

Consultez cet article d'aide pour en savoir plus sur [la manière dont certains de ces attributs diffèrent d'une source à l'autre dans Braze]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/).

### Différences entre les étiquettes de canvas et de campagne 

Le comportement des tags suivants diffère selon qu'il s'agit de Canvas ou de campagnes :
{% raw %}
- `dispatch_id` Le comportement diffère parce que Braze traite les étapes du canvas comme des événements déclenchés, même lorsqu'elles sont "planifiées" (à l'exception des étapes d'entrée, qui peuvent être planifiées). Pour en savoir plus, reportez-vous à la rubrique [Comportement de l'ID de répartition]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- L'utilisation de l'étiquette `{{campaign.${name}}}` avec Canvas affichera le nom du composant Canvas. Lorsque cette étiquette est utilisée avec des campagnes, elle affiche le nom de la campagne.
{% endraw %}

## Informations sur l'appareil le plus récemment utilisé

Vous pouvez modéliser les attributs suivants pour l'appareil le plus récent de l'utilisateur sur toutes les plateformes. Si un utilisateur n'a pas utilisé votre application (par exemple, vous avez importé l'utilisateur via l'API REST), ces valeurs seront toutes `null`.

{% raw %}

|Tags | Description |
|---|---|
|`{{most_recently_used_device.${browser}}}` | Le navigateur le plus récemment utilisé sur l'appareil de l'utilisateur. Les exemples incluent "Chrome" et "Safari". |
|`{{most_recently_used_device.${id}}}` | L'identifiant de l'appareil de Braze. Sur iOS, il peut s'agir de l'identifiant Apple pour le fournisseur (IDFV) ou d'un UUID. Pour Android et d'autres plateformes, il s'agit d'un UUID généré de manière aléatoire. |
| `{{most_recently_used_device.${carrier}}}` | L'opérateur du service téléphonique de l'appareil le plus récemment utilisé, s'il est disponible. Les exemples incluent "Verizon" et "Orange". |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | Si le suivi publicitaire est activé ou non sur l'appareil. Il s'agit d'une valeur booléenne (`true` ou `false`). |
| `{{most_recently_used_device.${idfa}}}` | Pour les appareils iOS, cette valeur sera l'identifiant pour la publicité (IDFA) si votre application est configurée avec notre [collection IDFA optionnelle]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/). Pour les appareils non-iOS, cette valeur sera nulle. |
| `{{most_recently_used_device.${google_ad_id}}}` | Pour les appareils Android, cette valeur sera l'identifiant publicitaire Google Play si votre application est configurée avec notre collecte facultative d'identifiants publicitaires Google Play. Pour les appareils non Android, cette valeur sera nulle. |
| `{{most_recently_used_device.${roku_ad_id}}}` | Pour les appareils Roku, cette valeur sera l'identifiant publicitaire Roku qui est collecté lorsque votre application est configurée avec Braze. Pour les appareils autres que Roku, cette valeur sera nulle. |
| `{{most_recently_used_device.${model}}}` | Le nom du modèle de l'appareil, s'il est disponible. Les exemples incluent "iPhone 6S" et "Nexus 6P" et "Firefox". |
| `{{most_recently_used_device.${os}}}` | Le système d'exploitation de l'appareil, s'il est disponible. Les exemples incluent "iOS 9.2.1" et "Android (Lollipop)" et "Windows". |
| `{{most_recently_used_device.${platform}}}` | La plate-forme de l'appareil, si elle est disponible. Si elle est définie, la valeur sera l'une des suivantes : `ios`, `android`, `kindle`, `android_china`, `web`, ou `tvos`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

En raison de la grande diversité des supports d'appareils, des noms de modèles et des systèmes d'exploitation, nous vous conseillons de tester minutieusement tout liquide dépendant conditionnellement de l'une de ces valeurs. Ces valeurs seront `null` si elles ne sont pas disponibles sur un appareil particulier.

## Informations ciblées sur l'application

Pour les messages in-app, vous pouvez utiliser les attributs d'app suivants dans Liquid. Les valeurs sont basées sur la clé API du SDK que vos applications utilisent pour demander l'envoi de messages.

|Tags | Description |
|------------------|---|
| `{{app.${api_id}}}` | La clé API de l'application qui demande le message. Par exemple, vous utilisez cette clé en conjonction avec `abort_message()` Liquid pour éviter d'envoyer des messages in-app à certaines apps, telles que les plateformes TV ou les builds de développement qui utilisent une clé API SDK distincte.|
| `{{app.${name}}}` | Le nom de l'application (tel que défini dans le tableau de bord de Braze) qui demande le message. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Par exemple, ce code Liquid annulera un message in-app si l'application demandeuse n'est pas l'une des deux clés API de la liste :

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## Informations ciblées sur les appareils

Pour les notifications push et les canaux de messages in-app, vous pouvez insérer dans le modèle les attributs suivants pour l'appareil auquel un message est envoyé. Autrement dit, une notification push ou un message in-app peut inclure les attributs de l'appareil sur lequel le message est lu. Notez que ces attributs ne fonctionnent pas pour les cartes de contenu. 

|Tags | Description |
|------------------|---|
| `{{targeted_device.${id}}}` | Il s'agit de l'identifiant de l'appareil de Braze. Sur iOS, il peut s'agir de l'identifiant Apple pour le fournisseur (IDFV) ou d'un UUID. Pour Android et d'autres plateformes, il s'agit d'un UUID généré de manière aléatoire. Par exemple, si un utilisateur possède cinq appareils, une tentative d'envoi a lieu pour les cinq appareils, chacun utilisant l'identifiant de l'appareil correspondant. Si un message est configuré pour être envoyé à l'appareil le plus récemment utilisé par l'utilisateur, une seule tentative d'envoi sera effectuée vers l'appareil le plus récemment utilisé, identifié par Braze. |
| `{{targeted_device.${carrier}}}` | L'opérateur du service téléphonique de l'appareil le plus récemment utilisé, s'il est disponible. Les exemples incluent "Verizon" et "Orange". |
| `{{targeted_device.${idfa}}}` | Pour les appareils iOS, cette valeur sera l'identifiant pour la publicité (IDFA) si votre application est configurée avec notre [collection IDFA optionnelle]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/). Pour les appareils non-iOS, cette valeur sera nulle. |
| `{{targeted_device.${google_ad_id}}}` | Pour les appareils Android, cette valeur sera l'identifiant publicitaire Google Play si votre application est configurée avec notre [collecte facultative de l'identifiant publicitaire Google Play]. Pour les appareils non Android, cette valeur sera nulle. |
| `{{targeted_device.${roku_ad_id}}}` | Pour les appareils Roku, cette valeur sera l'identifiant publicitaire Roku qui est collecté lorsque votre application est configurée avec Braze. Pour les appareils autres que Roku, cette valeur sera nulle. |
| `{{targeted_device.${model}}}` | Le nom du modèle de l'appareil, s'il est disponible. Les exemples incluent "iPhone 6S" et "Nexus 6P" et "Firefox". |
| `{{targeted_device.${os}}}` | Le système d'exploitation de l'appareil, s'il est disponible. Les exemples incluent "iOS 9.2.1" et "Android (Lollipop)" et "Windows". |
| `{{targeted_device.${platform}}}` | La plate-forme de l'appareil, si elle est disponible. Si elle est définie, la valeur sera l'une des suivantes : `ios`, `android`, `kindle`, `android_china`, `web`, ou `tvos`. Vous pouvez également utiliser l'étiquette de personnalisation `most_recently_used_device`. |
| `{{targeted_device.${foreground_push_enabled}}}` | Cette valeur sera `true` si l'appareil ciblé est activé pour la poussée au premier plan, `false` dans le cas contraire. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

En raison de la diversité des supports d'appareils, des noms de modèles et des systèmes d'exploitation, nous vous conseillons de tester minutieusement toute logique conditionnelle à l'une ou l'autre de ces valeurs. Ces valeurs seront `null` si elles ne sont pas disponibles sur un appareil particulier. 

En outre, pour les notifications push, il est possible que Braze ne soit pas en mesure de discerner l'appareil lié à la notification push dans certaines circonstances, par exemple si le jeton push a été importé via l'API, ce qui entraîne l'envoi de valeurs à `null` pour ces messages.

Exemple d'utilisation d'une valeur par défaut "là" lors de l'utilisation d'une variable prénom dans un envoi message.]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### Utiliser une logique conditionnelle au lieu d'une valeur par défaut

Dans certaines circonstances, vous pouvez opter pour une [logique conditionnelle]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/) au lieu de définir une valeur par défaut. La logique conditionnelle vous permet d'envoyer des messages différents en fonction de la valeur d'un attribut personnalisé. En outre, vous pouvez utiliser une logique conditionnelle pour [interrompre les messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) destinés aux clients dont les valeurs d'attribut sont nulles ou vides. 

#### Cas d'utilisation

Par exemple, supposons que vous envoyiez une notification de solde de récompenses à vos clients. Il n'y a pas de bonne façon de prendre en compte les clients dont le solde est faible ou nul en utilisant les valeurs par défaut.

Dans ce cas, deux options peuvent s'avérer plus efficaces que la définition d'une valeur par défaut :

1. Abandonnez le message pour les clients dont le solde est faible, nul ou vierge.

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. Envoyez un message complètement différent à ces clients, comme par exemple :

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

Dans ce cas d'utilisation, un utilisateur dont le prénom est vide ou nul recevra le message "Merci d'avoir téléchargé". Vous devriez inclure une [valeur par défaut]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/) pour le prénom afin de vous assurer que votre client ne voit pas Liquid en cas d'erreur.

{% endraw %}

## Tags de variables

Vous pouvez utiliser l'étiquette `assign` pour créer une variable dans le compositeur de messages. Nous vous recommandons d'utiliser un nom unique pour votre variable. Si vous créez une variable dont le nom est similaire à celui des étiquettes de personnalisation prises en charge (telles que `language`), cela peut affecter votre logique d'envoi de messages.

Après avoir créé une variable, vous pouvez y faire référence dans votre logique d'envoi de messages ou dans votre message. Cette étiquette est utile lorsque vous souhaitez reformater le contenu renvoyé par notre fonctionnalité [Connected Content]({% image_buster /assets/img_archive/personalized_firstname_.png %}) ]. Vous pouvez en savoir plus dans la documentation de Shopify sur les [tags variables](https://docs.shopify.com/themes/liquid/tags/variable-tags).

{% alert tip %}
Vous vous retrouvez à assigner les mêmes variables dans chaque message ? Au lieu d'écrire la balise `assign` à plusieurs reprises, vous pouvez enregistrer cette balise en tant que bloc de contenu et la placer en haut de votre message.

1. [Créez un bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Donnez un nom à votre bloc de contenu (sans espaces ni caractères spéciaux).
3. Sélectionnez **Modifier** en bas de la page.
4. Saisissez vos étiquettes `assign`.

Tant que le bloc de contenu se trouve en haut de votre message, chaque fois que la variable est insérée dans votre message en tant qu'objet, elle fera référence à l'attribut personnalisé que vous avez choisi !
{% endalert %}

### Cas d'utilisation

Supposons que vous permettiez à vos clients d'échanger leurs points de fidélité contre des prix après avoir accumulé 100 points de fidélité. Vous ne voulez donc envoyer un message qu'aux clients dont le solde de points serait supérieur ou égal à 100 s'ils effectuaient cet achat supplémentaire :

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
{% endraw %}

## Tags Iterate

{% raw %}
Les tags d'itération peuvent être utilisés pour exécuter un bloc de code de manière répétée. Le cas d'utilisation ci-dessous fait appel à l'étiquette `for`.

### Cas d'utilisation

Supposons que vous organisiez une vente de chaussures Nike et que vous souhaitiez envoyer des messages aux clients qui ont manifesté leur intérêt pour cette marque. Vous disposez d'un éventail de marques de produits visualisées sur le profil de chaque client. Ce tableau peut contenir jusqu'à 25 marques de produits, mais vous ne souhaitez envoyer des messages qu'aux clients qui ont vu un produit Nike parmi leurs 5 dernières consultations de produits.

```liquid
{% for items in {{custom_attribute.${Brands Viewed}}} limit:5 %}
{% if {{items}} contains 'Converse' %}
{% assign converse_viewer = true %}
{% endif %}
{% endfor %}
{% if converse_viewer == true %}
Sale on Converse!
{% else %}
{% abort_message() %}
{% endif %}
```

Dans ce cas d'utilisation, nous vérifions les cinq premiers éléments du tableau des marques de baskets consultées. Si l'un de ces éléments est la conversion, nous créons la variable `converse_viewer` et lui attribuons la valeur "true".

Ensuite, nous envoyons le message de vente lorsque `converse_viewer` est vrai. Dans le cas contraire, nous abandonnons le message.

Il s'agit d'un exemple simple de l'utilisation des tags Iterate dans le compositeur de messages Braze. Vous trouverez plus d'informations dans la documentation de Shopify sur les [tags d'itération](https://docs.shopify.com/themes/liquid/tags/iteration-tags).

## Tags de syntaxe

Les étiquettes syntaxiques peuvent être utilisées pour contrôler le rendu du Liquid. Vous pouvez utiliser l'étiquette `echo` pour renvoyer une expression. C'est la même chose que d'envelopper une expression avec des crochets, sauf que vous pouvez utiliser cette étiquette à l'intérieur des étiquettes Liquid. Vous pouvez également utiliser l'étiquette `liquid` pour obtenir un bloc d'étiquettes Liquid sans aucun délimiteur sur chaque étiquette. Chaque tag doit être placé sur sa propre ligne lorsque vous utilisez l'étiquette `liquid`. Consultez la documentation de Shopify sur les [tags de syntaxe](https://shopify.dev/api/liquid/tags#syntax-tags) pour plus d'informations et d'exemples.

Avec le [contrôle des espaces](https://shopify.github.io/liquid/basics/whitespace/) blancs, vous pouvez supprimer les espaces autour de vos étiquettes, ce qui vous permet de mieux contrôler l'aspect de la sortie Liquid.

## Codes d'état HTTP {#http-personalization}

Vous pouvez utiliser le statut HTTP d'un appel au [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) en l'enregistrant d'abord dans une variable locale, puis en utilisant la touche `__http_status_code__`. Par exemple :

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
Cette clé ne sera automatiquement ajoutée à l'objet Contenu connecté que si l'endpoint renvoie un objet JSON. Si l'endpoint renvoie un tableau ou un autre type, cette clé ne peut pas être définie automatiquement dans la réponse.
{% endalert %}

## Envoi de messages en fonction de la langue, du lieu le plus récent et du fuseau horaire

Dans certaines situations, vous pouvez souhaiter envoyer des messages spécifiques à certaines localités. Par exemple, le portugais brésilien est typiquement différent du portugais européen.

### Cas d'utilisation : Localiser en fonction des paramètres locaux récents

Voici un exemple de la façon dont vous pouvez utiliser les paramètres régionaux les plus récents pour localiser davantage un message internationalisé.

{% raw %}

```liquid
{% if ${language} == 'en' %}
Message in English
{% elsif  ${language} == 'fr' %}
Message in French
{% elsif  ${language} == 'ja' %}
Message in Japanese
{% elsif  ${language} == 'ko' %}
Message in Korean
{% elsif  ${language} == 'ru' %}
Message in Russian
{% elsif ${most_recent_locale} == 'pt_BR' %}
Message in Brazilian Portuguese
{% elsif ${most_recent_locale} == 'pt_PT' %}
Message in European Portuguese
{% elsif  ${language} == 'pt' %}
Message in default Portuguese
{% else %}
Message in default language
{% endif %}
```

Dans ce cas d'utilisation, les clients dont le lieu de résidence le plus récent est `pt_BR` recevront un message en portugais brésilien, et les clients dont le lieu de résidence le plus récent est `pt_PT` recevront un message en portugais européen. Les clients qui ne remplissent pas les deux premières conditions mais dont la langue est le portugais recevront un message dans le type de langue portugaise que vous aurez choisi par défaut.

### Cas d'utilisation : Cibler les utilisateurs en fonction du fuseau horaire

Vous pouvez également cibler les utilisateurs en fonction de leur fuseau horaire. Par exemple, envoyez un message si la personne est basée en EST et un autre si elle est en PST. Pour ce faire, enregistrez l'heure actuelle en UTC et comparez une instruction if/else avec l'heure actuelle de l'utilisateur afin d'envoyer le bon message pour le bon fuseau horaire. Vous devez paramétrer la campagne pour qu'elle soit envoyée dans le fuseau horaire local de l'utilisateur, afin qu'il reçoive la campagne au bon moment. 

Consultez le cas d'utilisation suivant pour savoir comment rédiger un message qui sera envoyé entre 14 et 15 heures et qui contiendra un message spécifique pour chaque fuseau horaire.

```liquid
{% assign hour_in_utc = 'now' | date: '%H' | plus:0 %}
{% if hour_in_utc >= 19 && hour_in_utc < 20 %}
It is between 2:00:00 pm and 2:59:59 pm ET!
{% elsif hour_in_utc >= 22 && hour_in_utc < 23 %}
It is between 2:00:00 pm and 2:59:59 pm PT!
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
