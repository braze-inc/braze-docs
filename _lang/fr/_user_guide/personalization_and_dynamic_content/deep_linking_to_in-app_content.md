---
nav_title: Lien profond au contenu d’application
article_title: Lien profond au contenu d’application
page_order: 3
description: "Cet article de référence explique comment ajouter un lien profond dans le contenu de vos messages in-app."

---

# Lien profond vers le contenu in-app

## Qu’est-ce qu’un lien profond ?

Un lien profond est un moyen de lancer une application native et de fournir des informations supplémentaires qui lui permettent de réaliser des actions spécifiques ou d’afficher des contenus spécifiques.

Cela comporte trois parties :

1. Identifier l’application à lancer
2. Demander à l’application quelle action effectuer
3. Fournir l’action avec toutes les données supplémentaires dont elle aura besoin

Les liens profonds sont des URIs personnalisés qui sont liés à une partie spécifique de l’application et contiennent les trois de ces parties. La clé est de définir un schéma personnalisé. `http:` est le schéma que la plupart des gens connaissant, mais les schémas peuvent commencer par n’importe quel mot. Un schéma doit commencer par une lettre, mais peut ensuite contenir des lettres, des chiffres, des signes plus, des signes moins ou des points. Il n’existe pas de registre central pour éviter les conflits, il est donc recommandé d’inclure votre nom de domaine dans le schéma. Par exemple, `twitter://` est l’URI d’iOS pour lancer l’application mobile Twitter.

Tout ce qui se trouve après la virgule dans un lien profond, est un texte libre. C’est à vous de définir sa structure et son interprétation, cependant, une convention commune est de la modéliser après les `http:` URL, y compris un `//` de début et les paramètres de requête (par ex., `?foo=1&bar=2`). Pour l’exemple de Twitter, `twitter://user?screen_name=[id]` serait utilisé pour lancer un profil spécifique dans l’application.

{% alert important %}
Braze ne prend pas en charge l’utilisation d’un wrapper comme Flutter pour envoyer des liens profonds. Pour utiliser cette fonctionnalité, vous devrez configurer les liens profonds dans la couche native.
{% endalert %}


## Balises UTM et attribution de campagne

### Qu’est-ce qu’une balise UTM ?

Les [Balises UTM (Gestionnaire de trafic Urchin)][4] vous permettent d’inclure les détails d’attribution de campagne directement dans les liens. Les balises UTM sont utilisées par Google Analytics pour collecter les données d’attribution de campagne et peuvent être utilisées pour suivre les propriétés suivantes :

- `utm_source` : l’identifiant de la source du trafic (par ex., `my_app`)
- `utm_medium` : le support de campagne (par ex., `newsfeed`)
- `utm_campaign` : l’identifiant de la campagne (par ex., `spring_2016_campaign`)
- `utm_term` : l’identifiant d’un terme de recherche payé qui a amené l’utilisateur à votre application ou site Internet (par ex., `pizza`)
- `utm_content` : un identifiant pour le lien/contenu spécifique sur lequel l’utilisateur a cliqué (par ex., `toplink` ou `android_iam_button2`)

Les balises UTM peuvent être intégrées à des liens HTTP (Web) réguliers et des liens profonds et suivies à l’aide de Google Analytics.

### Utilisation des balises UTM avec Braze

Si vous souhaitez utiliser des balises UTM avec des liens HTTP (Web) réguliers, par exemple, pour faire l’attribution de campagne pour vos campagnes par e-mail, et que votre organisation utilise déjà Google Analytics, vous pouvez simplement utiliser [Le générateur d’URL de Google][6] pour générer des liens UTM. Ces liens peuvent être facilement intégrés à la campagne Braze, comme tout autre lien.

Pour utiliser les balises UTM en liens profonds vers votre application, votre application doit intégrer[SDK Google Analytics][5] et configurer correctement ces éléments [ pour gérer les liens profonds][7]. Vérifiez auprès de vos développeurs si vous avez des questions.

Une fois le SDK analytique intégré et configuré, les balises UTM peuvent être utilisées avec des liens profonds dans les campagnes Braze. Pour configurer des balises UTM pour votre campagne, incluez simplement les balises UTM nécessaires dans l’URL de destination ou les liens profonds. Les exemples suivants montrent comment utiliser les balises UTM dans les notifications push et les messages in-app.

#### L’attribution de la notification push s’ouvre avec les balises UTM

Pour inclure les balises UTM dans vos liens profonds pour les notifications push, définissez simplement le comportement du clic sur le message push comme un lien profond, écrivez l’adresse du lien profond et incluez les balises UTM souhaitées de la façon suivante :

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![][8]

#### Attribution de messages dans l’application avec des balises UTM

Vous pouvez inclure des balises UTM dans les liens profonds compris dans vos messages in-app en utilisant l’élément suivant.

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![][10]

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-links
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/#Android_Deep_Advance
[4]: https://support.google.com/analytics/answer/1033863?hl=en
[5]: https://developers.google.com/analytics/devguides/collection/
[6]: https://support.google.com/analytics/answer/1033867
[7]: https://developers.google.com/analytics/solutions/mobile-campaign-deep-link
[8]: {% image_buster /assets/img_archive/push_utm_tags.png %}
[9]: {% image_buster /assets/img_archive/news_feed_utm_tags.png %}
[10]: {% image_buster /assets/img_archive/iam_utm_tags.png %}
[11]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/
