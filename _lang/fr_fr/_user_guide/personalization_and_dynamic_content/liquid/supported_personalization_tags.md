---
nav_title: Balises de personnalisation prises en charge
article_title: Balises de personnalisation Liquid prises en charge
page_order: 1
description: "Cet article de référence présente la liste complète des balises de personnalisation Liquid prises en charge."
search_rank: 1
---

# Balises de personnalisation prises en charge

> Cet article de référence présente la liste complète des balises de personnalisation Liquid prises en charge.

## Résumé des balises prises en charge

Voici un résumé des balises de personnalisation prises en charge. Pour plus de détails sur chaque type de balise et sur les bonnes pratiques, poursuivez votre lecture.

{% raw %}

| Type de balise de personnalisation | Balises |
| -------------  | ---- |
| Attributs standard (par défaut) | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| Attributs de l'appareil | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions'>Attributs de la liste d'e-mails</a> | `{{${set_user_to_unsubscribed_url}}}` <br>Cette balise remplace l'ancienne balise `{{${unsubscribe_url}}}`. Bien que l'ancienne balise fonctionne toujours dans les e-mails créés précédemment, nous vous recommandons d'utiliser la nouvelle à la place. <br><br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}`|
| <a href='/docs/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/#trigger-messages'>Attributs SMS</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/'>Attributs WhatsApp</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` <br> `{{whats_app.${inbound_flow_response}}}` <br> `{{whats_app.${inbound_product_id}}}` <br> `{{whats_app.${inbound_catalog_id}}}` |
| Attributs de campagne et attributs d'étape du Canvas | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Attributs Canvas | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| Attributs de la carte | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| Événements de géorepérage | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| Propriétés d'événement <br> (Personnalisées en fonction de votre espace de travail.)| `{{event_properties.${your_custom_event_property}}}` |
| Variables de contexte Canvas | `{{context}}` |
| Attributs personnalisés <br> (Personnalisés en fonction de votre espace de travail.) | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object/'>Propriétés du déclencheur API</a> |`{{api_trigger_properties}}` |
| Propriétés d'entrée Canvas | `{{context.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### Attributs pris en charge

Les attributs de campagne, de carte et de Canvas ne sont pris en charge que dans les modèles d'envoi de messages correspondants (par exemple, `dispatch_id` n'est pas disponible dans les campagnes de messages in-app).

Consultez cet article d'aide pour en savoir plus sur [la manière dont certains de ces attributs diffèrent d'une source à l'autre dans Braze]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/).

### Différences entre les balises Canvas et campagne 

Le comportement des balises suivantes diffère entre Canvas et les campagnes :
{% raw %}
- Le comportement de `dispatch_id` diffère parce que Braze traite les étapes du Canvas comme des événements déclenchés, même lorsqu'elles sont « planifiées » (à l'exception des étapes d'entrée, qui peuvent être planifiées). Pour en savoir plus, consultez [Comportement de l'ID de répartition]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- La balise `{{campaign.${name}}}` utilisée avec Canvas affiche le nom du composant Canvas. Utilisée avec des campagnes, elle affiche le nom de la campagne.
{% endraw %}

## Informations sur l'appareil le plus récemment utilisé

Vous pouvez utiliser les attributs suivants comme modèles pour l'appareil le plus récent de l'utilisateur, toutes plateformes confondues. Si un utilisateur n'a pas utilisé votre application (par exemple, si vous l'avez importé via l'API REST), ces valeurs seront toutes `null`.

{% raw %}

|Balise | Description |
|---|---|
|`{{most_recently_used_device.${browser}}}` | Le navigateur le plus récemment utilisé sur l'appareil de l'utilisateur. Par exemple, « Chrome » ou « Safari ». |
|`{{most_recently_used_device.${id}}}` | L'identifiant d'appareil Braze. Sur iOS, il peut s'agir de l'identifiant Apple pour le fournisseur (IDFV) ou d'un UUID. Pour Android et les autres plateformes, il s'agit d'un UUID généré aléatoirement. |
| `{{most_recently_used_device.${carrier}}}` | L'opérateur téléphonique de l'appareil le plus récemment utilisé, le cas échéant. Par exemple, « Verizon » ou « Orange ». |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | Indique si le suivi publicitaire est activé ou non sur l'appareil. Il s'agit d'une valeur booléenne (`true` ou `false`). |
| `{{most_recently_used_device.${idfa}}}` | Pour les appareils iOS, cette valeur correspond à l'identifiant publicitaire (IDFA) si votre application est configurée avec notre [collecte IDFA optionnelle]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/). Pour les appareils non iOS, cette valeur sera null. |
| `{{most_recently_used_device.${google_ad_id}}}` | Pour les appareils Android, cette valeur correspond à l'identifiant publicitaire Google Play si votre application est configurée avec notre collecte facultative d'identifiants publicitaires Google Play. Pour les appareils non Android, cette valeur sera null. |
| `{{most_recently_used_device.${roku_ad_id}}}` | Pour les appareils Roku, cette valeur correspond à l'identifiant publicitaire Roku collecté lorsque votre application est configurée avec Braze. Pour les appareils non Roku, cette valeur sera null. |
| `{{most_recently_used_device.${model}}}` | Le nom du modèle de l'appareil, si disponible. Par exemple, « iPhone 6S », « Nexus 6P » ou « Firefox ». |
| `{{most_recently_used_device.${os}}}` | Le système d'exploitation de l'appareil, si disponible. Par exemple, « iOS 9.2.1 », « Android (Lollipop) » ou « Windows ». |
| `{{most_recently_used_device.${platform}}}` | La plateforme de l'appareil, si disponible. La valeur sera l'une des suivantes : `ios`, `android`, `kindle`, `android_china`, `web` ou `tvos`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Étant donné la grande diversité des opérateurs, des noms de modèles et des systèmes d'exploitation, nous vous conseillons de tester minutieusement tout code Liquid dont la logique conditionnelle dépend de l'une de ces valeurs. Ces valeurs seront `null` si elles ne sont pas disponibles sur un appareil donné.

## Informations sur l'application ciblée

Pour les messages in-app, vous pouvez utiliser les attributs d'application suivants dans Liquid. Les valeurs sont basées sur la clé API du SDK que vos applications utilisent pour demander l'envoi de messages.

|Balise | Description |
|------------------|---|
| `{{app.${api_id}}}` | La clé API de l'application qui demande le message. Par exemple, vous pouvez utiliser cette clé avec `abort_message()` en Liquid pour éviter d'envoyer des messages in-app à certaines applications, comme les plateformes TV ou les builds de développement qui utilisent une clé API SDK distincte.|
| `{{app.${name}}}` | Le nom de l'application (tel que défini dans le tableau de bord de Braze) qui demande le message. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Par exemple, ce code Liquid annulera un message si l'application à l'origine de la demande ne correspond pas à l'une des deux clés API de la liste :

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## Informations sur l'appareil ciblé

Pour les notifications push, les messages in-app et les bannières, vous pouvez utiliser les attributs suivants comme modèles pour l'appareil qui reçoit le message. Une notification push, un message in-app ou une bannière peuvent inclure des attributs de l'appareil sur lequel l'utilisateur lit le message. Ces attributs ne fonctionnent pas avec les cartes de contenu ni les e-mails. Pour les e-mails, les messages sont générés avant l'envoi : l'appareil sur lequel l'utilisateur ouvrira l'e-mail est donc inconnu à ce moment-là.

|Balise | Description |
|------------------|---|
| `{{targeted_device.${id}}}` | L'identifiant d'appareil Braze. Sur iOS, il peut s'agir de l'identifiant Apple pour le fournisseur (IDFV) ou d'un UUID. Pour Android et les autres plateformes, il s'agit d'un UUID généré aléatoirement. Par exemple, si un utilisateur possède cinq appareils, une tentative d'envoi a lieu pour chacun des cinq appareils, avec l'identifiant correspondant. Si un message est configuré pour être envoyé à l'appareil le plus récemment utilisé, une seule tentative d'envoi sera effectuée vers cet appareil, tel qu'identifié par Braze. |
| `{{targeted_device.${carrier}}}` | L'opérateur téléphonique de l'appareil le plus récemment utilisé, le cas échéant. Par exemple, « Verizon » ou « Orange ». |
| `{{targeted_device.${idfa}}}` | Pour les appareils iOS, cette valeur correspond à l'identifiant publicitaire (IDFA) si votre application est configurée avec notre [collecte IDFA optionnelle]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/). Pour les appareils non iOS, cette valeur sera null. |
| `{{targeted_device.${google_ad_id}}}` | Pour les appareils Android, cette valeur correspond à l'identifiant publicitaire Google Play si votre application est configurée avec notre [collecte facultative de l'identifiant publicitaire Google Play]. Pour les appareils non Android, cette valeur sera null. |
| `{{targeted_device.${roku_ad_id}}}` | Pour les appareils Roku, cette valeur correspond à l'identifiant publicitaire Roku collecté lorsque votre application est configurée avec Braze. Pour les appareils non Roku, cette valeur sera null. |
| `{{targeted_device.${model}}}` | Le nom du modèle de l'appareil, si disponible. Par exemple, « iPhone 6S », « Nexus 6P » ou « Firefox ». |
| `{{targeted_device.${os}}}` | Le système d'exploitation de l'appareil, si disponible. Par exemple, « iOS 9.2.1 », « Android (Lollipop) » ou « Windows ». |
| `{{targeted_device.${platform}}}` | La plateforme de l'appareil, si disponible. La valeur sera l'une des suivantes : `ios`, `android`, `kindle`, `android_china`, `web` ou `tvos`. Vous pouvez également utiliser la balise de personnalisation `most_recently_used_device`. |
| `{{targeted_device.${foreground_push_enabled}}}` | Cette valeur sera `true` lorsque l'appareil ciblé est activé pour les notifications push de premier plan, `false` dans le cas contraire. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

Étant donné la grande diversité des opérateurs, des noms de modèles et des systèmes d'exploitation, nous vous conseillons de tester minutieusement toute logique conditionnelle qui dépend de l'une de ces valeurs. Ces valeurs seront `null` si elles ne sont pas disponibles sur un appareil donné. 

De plus, pour les notifications push, il est possible que Braze ne puisse pas déterminer l'appareil associé à la notification dans certaines circonstances, par exemple si le jeton de notification push a été importé via l'API. Les valeurs seront alors `null` pour ces messages.

![Exemple d'utilisation d'une valeur par défaut « there » lors de l'utilisation d'une variable de prénom dans un message de notification push.]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### Utiliser la logique conditionnelle au lieu d'une valeur par défaut

Dans certains cas, il peut être préférable d'utiliser une [logique conditionnelle]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/) plutôt que de définir une valeur par défaut. La logique conditionnelle vous permet d'envoyer des messages différents selon la valeur d'un attribut personnalisé. Vous pouvez également l'utiliser pour [interrompre les messages]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) destinés aux clients dont les valeurs d'attribut sont nulles ou vides. 

#### Cas d'utilisation

Supposons que vous envoyiez une notification de solde de récompenses à vos clients. Il n'existe pas de bonne méthode pour gérer les clients dont le solde est faible ou nul à l'aide de valeurs par défaut.

Dans ce cas, deux options peuvent être plus adaptées que la définition d'une valeur par défaut :

1. Interrompre le message pour les clients dont les soldes sont faibles, nuls ou vides.

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. Envoyer un message complètement différent à ces clients, par exemple :

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

Dans ce cas d'utilisation, un utilisateur dont le prénom est vide ou null recevra le message « Thanks for downloading! ». Pensez à inclure une [valeur par défaut]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/) pour le prénom afin de vous assurer que votre client ne voit pas de code Liquid en cas d'erreur.

{% endraw %}

## Balises de variables

Vous pouvez utiliser la balise `assign` pour créer une variable dans le compositeur de message. Nous vous recommandons de choisir un nom unique pour votre variable. Si vous créez une variable dont le nom est similaire à celui des balises de personnalisation prises en charge (comme `language`), cela peut affecter votre logique d'envoi de messages.

Une fois la variable créée, vous pouvez y faire référence dans votre logique d'envoi de messages ou dans votre message. Cette balise est particulièrement utile lorsque vous souhaitez reformater le contenu renvoyé par notre fonctionnalité de [contenu connecté]({% image_buster /assets/img_archive/personalized_firstname_.png %}). Pour en savoir plus, consultez la documentation de Shopify sur les [balises de variables](https://docs.shopify.com/themes/liquid/tags/variable-tags).

{% alert tip %}
Vous vous retrouvez à assigner les mêmes variables dans chaque message ? Au lieu de réécrire la balise `assign` à chaque fois, vous pouvez l'enregistrer comme bloc de contenu et la placer en haut de votre message.

1. [Créez un bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Donnez un nom à votre bloc de contenu (sans espaces ni caractères spéciaux).
3. Sélectionnez **Modifier** en bas de la page.
4. Saisissez vos balises `assign`.

Tant que le bloc de contenu se trouve en haut de votre message, chaque fois que la variable est insérée dans votre message comme objet, elle fera référence à l'attribut personnalisé que vous avez choisi !
{% endalert %}

### Cas d'utilisation

Supposons que vous permettiez à vos clients d'échanger leurs points de fidélité contre des prix après avoir accumulé 100 points. Vous ne souhaitez donc envoyer des messages qu'aux clients dont le solde de points serait supérieur ou égal à 100 s'ils effectuaient cet achat supplémentaire :

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

## Balises d'itération

{% raw %}
Les balises d'itération permettent d'exécuter un bloc de code de manière répétée. Le cas d'utilisation ci-dessous illustre l'utilisation de la balise `for`.

### Cas d'utilisation

Supposons que vous ayez une promotion sur les baskets Nike et que vous souhaitiez envoyer des messages aux clients qui ont exprimé leur intérêt pour Nike. Vous disposez d'un tableau de marques de produits consultées sur le profil de chaque client. Ce tableau peut contenir jusqu'à 25 marques, mais vous ne voulez envoyer des messages qu'aux clients qui ont vu un produit Nike parmi leurs 5 consultations les plus récentes.

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

Dans ce cas d'utilisation, nous examinons les cinq premiers éléments du tableau des marques de baskets consultées. Si l'un de ces éléments est Converse, nous créons la variable `converse_viewer` et la définissons sur true.

Ensuite, nous envoyons le message de promotion lorsque `converse_viewer` est true. Sinon, nous interrompons le message.

Ceci est un exemple simple d'utilisation des balises d'itération dans le compositeur de messages de Braze. Pour en savoir plus, consultez la documentation de Shopify sur les [balises d'itération](https://docs.shopify.com/themes/liquid/tags/iteration-tags).

## Balises de syntaxe

Les balises de syntaxe permettent de contrôler le rendu du Liquid. Vous pouvez utiliser la balise `echo` pour renvoyer une expression. Cela revient à entourer une expression avec des accolades, sauf que vous pouvez utiliser cette balise à l'intérieur d'autres balises Liquid. Vous pouvez également utiliser la balise `liquid` pour écrire un bloc Liquid sans délimiteur sur chaque balise. Chaque balise doit alors figurer sur sa propre ligne. Consultez la documentation de Shopify sur les [balises de syntaxe](https://shopify.dev/api/liquid/tags#syntax-tags) pour plus d'informations et d'exemples.

Grâce au [contrôle des espaces](https://shopify.github.io/liquid/basics/whitespace/), vous pouvez supprimer les espaces autour de vos balises et ainsi mieux maîtriser l'apparence de la sortie Liquid.

## Codes de statut HTTP {#http-personalization}

Vous pouvez exploiter le statut HTTP d'un appel au [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) en l'enregistrant d'abord dans une variable locale, puis en utilisant la clé `__http_status_code__`. Par exemple :

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
Cette clé n'est ajoutée automatiquement à l'objet de contenu connecté que si l'endpoint renvoie un objet JSON. Si l'endpoint renvoie un tableau ou un autre type, cette clé ne peut pas être définie automatiquement dans la réponse.
{% endalert %}

## Envoyer des messages en fonction de la langue, des paramètres régionaux les plus récents et du fuseau horaire

Dans certaines situations, vous pouvez souhaiter envoyer des messages spécifiques à certaines locales. Par exemple, le portugais brésilien est généralement différent du portugais européen.

### Cas d'utilisation : Localiser en fonction des paramètres régionaux récents

Voici un exemple montrant comment utiliser les paramètres régionaux les plus récents pour affiner la localisation d'un message internationalisé.

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

Dans ce cas d'utilisation, les clients dont la locale la plus récente est `pt_BR` recevront un message en portugais brésilien, et ceux dont la locale la plus récente est `pt_PT` recevront un message en portugais européen. Les clients qui ne remplissent pas les deux premières conditions mais dont la langue est le portugais recevront un message dans le type de portugais que vous aurez choisi par défaut.

### Cas d'utilisation : Cibler les utilisateurs par fuseau horaire

Vous pouvez également cibler les utilisateurs en fonction de leur fuseau horaire. Par exemple, envoyer un message aux utilisateurs situés dans le fuseau EST et un autre à ceux du fuseau PST. Pour ce faire, enregistrez l'heure actuelle en UTC et comparez-la avec l'heure de l'utilisateur via une instruction if/else afin d'envoyer le bon message pour le bon fuseau horaire. Pensez à configurer la campagne pour qu'elle soit envoyée dans le fuseau horaire local de l'utilisateur, afin qu'il la reçoive au moment opportun. 

Voici un exemple de message envoyé entre 14 h et 15 h, avec un contenu spécifique pour chaque fuseau horaire.

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

## Envoyer des messages avec un nombre aléatoire

{% raw %}
La balise `{% random %}` renvoie un nombre aléatoire. Vous pouvez l'utiliser pour une logique de type A/B, un échantillonnage ou pour varier le contenu des messages.

| Balise | Description |
|-------|--------------|
| `{% random %}` | Un nombre à virgule flottante entre 0 et 1 (0 inclus, 1 exclu). |
| `{% random 10 %}` (argument entier) | Un entier allant de 0 jusqu'à l'entier spécifié (exclu). Par exemple, `{% random 10 %}` renvoie un entier de 0 à 9. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### Cas d'utilisation : Envoyer des variantes aléatoires aux utilisateurs

{% raw %}
```liquid
{% capture roll_str %}{% random %}{% endcapture %}
{% assign roll = roll_str | plus: 0 %}
{% if roll < 0.5 %}
Show variant A
{% else %}
Show variant B
{% endif %}
```
{% endraw %}


[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags