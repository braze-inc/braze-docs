---
nav_title: Tags de personnalisation pris en charge
article_title: Tags de personnalisation Liquid pris en charge
page_order: 1
description: "Cet article de référence couvre une liste complète des tags de personnalisation Liquid pris en charge."
---

# Tags de personnalisation pris en charge

Pour plus de commodité, un résumé des balises de personnalisation sont listées ci-dessous. Pour plus de détails sur chaque type de balises et les meilleures pratiques, continuez à lire.

{% raw %}

| Type d'étiquette de personnalisation                                                                    | Tags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Attributs par défaut                                                                                    | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${twitter_handle}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` |
| Attributs de l'appareil                                                                                 | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${windows_ad_id}}}`                                                                                                                |
| Attributs de la liste d'emails <br> (gagnez plus de [ici][43])                                    | `{{${set_user_to_unsubscribed_url}}}` <br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Attributs SMS <br> (Gagnez plus de [ici][48])                                                     | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Attributs de la campagne                                                                                | `{{campagne.${api_id}}}` <br> `{{campagne.${dispatch_id}}}` <br> `{{campagne.${name}}}` <br> `{{campagne.${message_name}}}` <br> `{{campagne.${message_api_id}}}`                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Attributs de la toile                                                                                   | `{{toile.${name}}}` <br> `{{toile.${api_id}}}` <br> `{{toile.${variant_name}}}` <br> `{{toile.${variant_api_id}}}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Attributs de pas de canvas                                                                              | `{{campagne.${api_id}}}` <br> `{{campagne.${dispatch_id}}}` <br> `{{campagne.${name}}}` <br> `{{campagne.${message_name}}}` <br> `{{campagne.${message_api_id}}}`                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Attributs de la carte                                                                                   | `{{card.${api_id}}}` <br> `{{card.${name}}}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Événements de géorepérage                                                                               | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Propriétés de l'événement <br> (Ces propriétés sont personnalisées à votre groupe d'application.) | `{{event_properties.${your_custom_event_property}}}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Attributs personnalisés <br> (Ces attributs sont personnalisés pour votre groupe d'application.)  | `{{custom_attribut.${your_custom_attribute}}}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}

{% alert important %}
Les attributs Campaign, Card et Canvas ne sont pris en charge que dans leurs modèles de messagerie correspondants (par exemple, `dispatch_id` n'est pas disponible dans les campagnes de messages dans l'application).
{% endalert %}

#### Différences de balises de toile et de campagne

Le comportement des tags suivants diffère entre Canvas et les campagnes :
{% raw %}
- `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les pas de Canvas (sauf les pas d'entrée, qui peuvent être programmés) en tant qu'événements déclenchés, même lorsqu'ils sont "programmés". [En savoir plus sur le comportement de `dispatch_id` dans Canvas et les campagnes ici]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- En utilisant la balise `{{campaign.${name}}}` avec Canvas affichera le nom de l'étape Canvas . Lorsque vous utilisez ce tag avec des campagnes, il affichera le nom de la campagne.
{% endraw %}

## Informations de l'appareil les plus récentes

Vous pouvez modéliser les attributs suivants pour le périphérique le plus récent de l'utilisateur sur toutes les plateformes. Si un utilisateur n'a pas utilisé votre application (par ex. vous avez importé l'utilisateur via REST API), alors ces valeurs seront toutes `null`.

{% raw %}

| Étiquette                                              | Libellé                                                                                                                                                                                                                                                            |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `{{most_recently_used_device.${browser}}}`             | Le navigateur le plus récemment utilisé sur le périphérique de l'utilisateur. Les exemples incluent "Chrome" et "Safari".                                                                                                                                          |
| `{{most_recently_used_device.${id}}}`                  | Il s'agit de l'identifiant de l'appareil de Brase. Sur iOS, il s'agit de l'Apple Identifier for Vendor (IDFV). Pour Android et d'autres plates-formes, c'est l'identifiant de l'appareil de Braze, un GUID généré aléatoirement.                                   |
| `{{most_recently_used_device.${carrier}}}`             | Le transporteur de services téléphoniques de l'appareil le plus récent, s'il est disponible. Des exemples incluent "Verizon" et "Orange".                                                                                                                          |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | Si l'appareil a activé ou non le suivi des annonces. C'est une valeur booléenne (`true` ou `false`).                                                                                                                                                               |
| `{{most_recently_used_device.${idfa}}}`                | Pour les appareils iOS, cette valeur sera l'Identificateur pour la publicité (IDFA) si votre application est configurée avec la [collection optionnelle IDFA][40] de Braze. Pour les appareils non-iOS, cette valeur sera nulle.                                   |
| `{{most_recently_used_device.${google_ad_id}}}`        | Pour les appareils Android, cette valeur sera l'identifiant Google Play Advertising Identifier si votre application est configurée avec la collection optionnelle de Google Play Advertising ID de Braze. Pour les appareils non Android, cette valeur sera nulle. |
| `{{most_recently_used_device.${roku_ad_id}}}`          | Pour les appareils Roku, cette valeur sera le Roku Advertising Identifier qui est collecté lorsque votre application est configurée avec Braze. Pour les appareils non-Roku, cette valeur sera nulle.                                                              |
| `{{most_recently_used_device.${windows_ad_id}}}`       | Pour les appareils Windows, cette valeur sera l'identifiant de publicité Windows qui est collecté lorsque votre application est configurée avec Braze. Pour les périphériques non-Windows, cette valeur sera nulle.                                                |
| `{{most_recently_used_device.${model}}}`               | Le nom du modèle de l'appareil, si disponible. Des exemples incluent "iPhone 6S" et "Nexus 6P" et "Firefox".                                                                                                                                                       |
| `{{most_recently_used_device.${os}}}`                  | Le système d'exploitation de l'appareil, s'il est disponible. Des exemples incluent "iOS 9.2.1" et "Android (Lollipop)" et "Windows".                                                                                                                              |
| `{{most_recently_used_device.${platform}}}`            | La plate-forme de l'appareil, si disponible. Si défini, la valeur sera parmi `ios`, `android`, `fenêtres`, `windows8`, `allumer`, `android_china`, `web`, ou `tvos`.                                                                                               |
{: .reset-td-br-1 .reset-td-br-2}


Parce qu'il existe une telle gamme de transporteurs de périphériques, de noms de modèles et de systèmes d'exploitation, Nous vous conseillons de tester minutieusement tout liquide qui dépend conditionnellement de l'une de ces valeurs. Ces valeurs seront `nulles` si elles ne sont pas disponibles sur un appareil particulier.

## Informations sur l'appareil ciblé

Pour les notifications push et les canaux de messages intégrés à l'application, vous pouvez modéliser les attributs suivants pour l'appareil vers lequel un message est envoyé. Autrement dit, une notification push ou un message dans l'application peuvent inclure des attributs de l'appareil sur lequel le message est en cours de lecture. Notez que ces attributs ne fonctionneront pas pour les cartes de contenu.

| Étiquette                             | Libellé                                                                                                                                                                                                                                                        |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{{targted_device.${id}}}`            | Il s'agit de l'identifiant de l'appareil de Brase. Sur iOS, il s'agit de l'Apple Identifier for Vendor (IDFV). Pour Android et d'autres plates-formes, c'est l'identifiant de l'appareil de Braze, un GUID généré aléatoirement.                               |
| `{{targted_device.${carrier}}}`       | Le transporteur de services téléphoniques de l'appareil le plus récent, s'il est disponible. Des exemples incluent "Verizon" et "Orange".                                                                                                                      |
| `{{targted_device.${idfa}}}`          | Pour les appareils iOS, cette valeur sera l'Identificateur pour la publicité (IDFA) si votre application est configurée avec la [collection optionnelle IDFA][40] de Braze. Pour les appareils non-iOS, cette valeur sera nulle.                               |
| `{{targted_device.${google_ad_id}}}`  | Pour les appareils Android, cette valeur sera l'identifiant Google Play Advertising Identifier si votre application est configurée avec la [collection facultative de Google Play Advertising ID]. Pour les appareils non Android, cette valeur sera nulle.    |
| `{{targted_device.${roku_ad_id}}}`    | Pour les appareils Roku, cette valeur sera le Roku Advertising Identifier qui est collecté lorsque votre application est configurée avec Braze. Pour les appareils non-Roku, cette valeur sera nulle.                                                          |
| `{{targted_device.${windows_ad_id}}}` | Pour les appareils Windows, cette valeur sera l'identifiant de publicité Windows qui est collecté lorsque votre application est configurée avec Braze. Pour les périphériques non-Windows, cette valeur sera nulle.                                            |
| `{{targted_device.${model}}}`         | Le nom du modèle de l'appareil, si disponible. Des exemples incluent "iPhone 6S" et "Nexus 6P" et "Firefox".                                                                                                                                                   |
| `{{targted_device.${os}}}`            | Le système d'exploitation de l'appareil, s'il est disponible. Des exemples incluent "iOS 9.2.1" et "Android (Lollipop)" et "Windows".                                                                                                                          |
| `{{targted_device.${platform}}}`      | La plate-forme de l'appareil, si disponible. Si défini, la valeur sera parmi `ios`, `android`, `fenêtres`, `windows8`, `allumer`, `android_china`, `web`, ou `tvos`. Vous pouvez également utiliser la balise de personnalisation `most_recently_used_device`. |
{: .reset-td-br-1 .reset-td-br-2}


{% endraw %}


Parce qu'il existe une telle gamme de transporteurs de périphériques, de noms de modèles et de systèmes d'exploitation, Nous vous conseillons de tester en profondeur toute logique qui dépend conditionnellement de l'une de ces valeurs. Ces valeurs seront `nulles` si elles ne sont pas disponibles sur un appareil particulier. En outre, pour les notifications push, il est possible que Braze ne soit pas en mesure de détecter l'appareil attaché à la notification push dans certaines circonstances, par exemple si le jeton push a été importé via API, les valeurs étant `null` pour ces messages.

!\[Personalization\]\[4\]

Dans certaines circonstances, vous pouvez choisir d'utiliser la [logique conditionnelle][17] au lieu de définir une valeur par défaut. La logique conditionnelle vous permet d'envoyer des messages qui diffèrent en fonction de la valeur d'un attribut personnalisé.

De plus, vous pouvez utiliser la logique conditionnelle pour [annuler les messages][18] aux clients avec des valeurs d'attributs nuls ou vides.

Par exemple, si vous envoyez une notification de solde de récompenses aux clients, il n'y a pas de bonne façon de comptabiliser pour les clients avec des soldes faibles et nuls en utilisant des valeurs par défaut.

Dans ce cas, il y a deux options qui peuvent fonctionner mieux que de définir une valeur par défaut :

1. Annuler le message pour les clients avec des soldes faibles, nuls et vierges.

    !\[NoBalanceAbort\]\[34\]


2. Envoyez un message complètement différent à ces clients, peut-être quelque chose comme suit :

{% raw %}

```liquid
{% if ${first_name} != vide et ${first_name} != null %}
Bonjour {{${first_name} | default: 'there'}}, merci de télécharger !
{% else %}
Merci pour le téléchargement !
{% endif %}
```
Dans cet exemple, un utilisateur avec un prénom vide ou nul recevra le message "Merci d'avoir téléchargé". Vous devez inclure une valeur par défaut [][47] pour le prénom afin de vous assurer que votre client ne voit pas Liquid en cas d'erreur.

{% endraw %}

## Tags de la variable

Vous pouvez utiliser la balise `assigner` pour créer une variable dans le composeur du message. Une fois que vous avez créé une variable, vous pouvez référencer cette variable dans votre logique de messagerie ou votre message.

Disons que vous permettez à vos clients d'encaisser dans leurs points de récompense des prix une fois qu'ils ont accumulé 100 points de récompense. Donc, vous ne voulez envoyer un message aux clients qui auraient un solde de points supérieur ou égal à 100 s'ils faisaient cet achat supplémentaire:

{% raw %}
```liquid
{% assignez new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Effectuez un achat pour apporter vos points de récompense à {{new_points_balance}} et en espèces aujourd'hui !
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
Cette balise est pratique lorsque vous voulez reformater le contenu qui est retourné à partir de notre fonctionnalité\[4\] \[Contenu connecté\]. Vous pouvez en savoir plus sur les balises variables [ici][31].

{% endraw %}

{% alert tip %}
Vous vous trouvez à assigner les mêmes variables dans chaque message ? Au lieu d'écrire encore et encore la balise `assigner` vous pouvez enregistrer ce tag en tant que bloc de contenu et le placer en haut de votre message à la place.

1. [Créer un bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Donnez un nom à votre Bloc de Contenu (sans espaces ni caractères spéciaux).
3. Cliquez sur **Modifier** au bas de la page.
4. Tapez vos tags `assigner`.

Tant que le bloc de contenu est en haut de votre message, chaque fois que la variable est insérée dans votre message en tant qu'objet, elle fera référence à l'attribut personnalisé que vous avez choisi !
{% endalert %}

## Tags d'itération

{% raw %}
Les balises d'itération peuvent être utilisées pour exécuter un bloc de code de façon répétée. Cet exemple présente la balise `pour`.

Disons que vous avez une vente sur les baskets Nike et que vous voulez envoyer des messages aux clients qui ont exprimé leur intérêt pour Nike. Vous avez une gamme de marques de produits consultées sur le profil de chaque client. Ce tableau peut contenir jusqu'à 25 marques de produits, mais vous voulez seulement envoyer un message aux clients qui ont vu un produit Nike comme l'une de leurs 5 vues les plus récentes des produits.

```liquid
{% pour les articles dans {{custom_attribute.{Brands Viewed}}} limite:5 %}
{% si {{items}} contient 'Convertir' %}
{% assign converse_viewer = true %}
{% endif %}
{% endfor %}
{% if converse_viewer == true %}
Vente en Convertissement!
{% else %}
{% abort_message() %}
{% endif %}
```

Dans cet exemple, nous vérifions les cinq premiers éléments des marques de sneaker vues tableau. Si l'un de ces éléments est converti, nous créons la variable converse_viewer et la définissons à true.

Ensuite, nous envoyons le message de vente lorsque converse_viewer est vrai. Sinon, nous annulons le message.

Ceci est un exemple simple de la façon dont les balises d'itération peuvent être utilisées dans le compositeur de message de Brase. Vous pouvez trouver plus d'informations [ici][32].

## Codes de statut HTTP {#http-personalization}

Vous pouvez utiliser le statut HTTP à partir d'un appel [Contenu Connecté][38] en le sauvegardant d'abord en tant que variable locale, puis en utilisant la clé `__http_status_code__`. Par exemple :

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```

{% alert tip %}
  Sachez que cette clé ne sera automatiquement ajoutée à l'objet Contenu connecté que si le point de terminaison renvoie un objet JSON. Si le point de terminaison retourne un tableau ou un autre type, alors cette clé ne peut pas être définie automatiquement dans la réponse.
{% endalert %}

## Envoi de messages en fonction de la langue, de la langue locale, et du fuseau horaire le plus récent

Dans certaines situations, vous pouvez vouloir envoyer des messages spécifiques à des locales particulières. Par exemple, le portugais brésilien est typiquement différent du portugais européen.

Voici un exemple de la façon dont vous pouvez utiliser la dernière locale pour localiser un message internationalisé.

```liquid
{% if ${language} == 'fr' %}
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
Message par défaut portugais
{% else %}
Message en langue par défaut
{% endif %}
```

Dans cet exemple, les clients ayant une locale la plus récente de 'pt_BR' recevront un message en portugais brésilien, les clients avec une locale la plus récente de 'pt_PT' recevront un message en portugais européen et les clients qui ne remplissent pas les deux premières conditions mais qui ont leur langue définie en portugais recevront un message dans ce que vous voulez que le type de langue par défaut soit le portugais.

Vous pouvez également cibler les utilisateurs en fonction de leur fuseau horaire. Par exemple, envoyez un message s'ils sont basés sur EST et un autre s'ils sont PST. Pour cela, économisez le temps actuel en UTC, et comparez une requête si/autre avec l'heure actuelle de l'utilisateur pour vous assurer que vous envoyez le bon message pour le bon fuseau horaire. Vous devriez configurer la campagne à envoyer dans le fuseau horaire local de l'utilisateur, pour vous assurer qu'il obtient la campagne au bon moment. Voir ci-dessous pour un exemple de comment écrire un message qui sortira entre 14h et 15h et qui aura un message spécifique pour chaque fuseau horaire.

```liquid
{% assigner hour_in_utc = 'maintenant' | date: '%H' | plus:0 %}
{% if hour_in_utc >= 19 && hour_in_utc < 20 %}
C'est entre 14:00:00:00 et 14:59:59:59pm ET!
{% elsif hour_in_utc >= 22 && hour_in_utc < 23 %}
C'est entre 14h00 et 14h59:59 pm PT!
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}
[4]: {% image_buster /assets/img_archive/personalized_firstname_.png %} [34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}

[31]: https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]: https://docs.shopify.com/themes/liquid/tags/iteration-tags
[38]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[17]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/
[43]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions
[47]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
[47]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
[48]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#trigger-messages-by-keyword
