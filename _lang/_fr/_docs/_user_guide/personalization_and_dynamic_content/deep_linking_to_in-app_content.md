---
nav_title: Liaison profonde vers le contenu de l'application
article_title: Liaison profonde vers le contenu de l'application
page_order: 2
description: "Un lien profond est un moyen de lancer une application native et de fournir des informations supplémentaires lui demandant de faire une action spécifique ou d'afficher un contenu spécifique. Cet article de référence couvre la façon de créer un lien profond dans le contenu de votre message dans l'application."
---

# Liaison profonde vers le contenu de l'application

## Qu'est-ce que le lien profond?

Un lien profond est un moyen de lancer une application native et de fournir des informations supplémentaires lui demandant de faire une action spécifique ou d'afficher un contenu spécifique.

Il y a trois parties à cela:

1. Identifier quelle application à lancer
2. Indiquer à l'application quelle action effectuer
3. Fournir à l'action toutes les données supplémentaires dont elle aura besoin

Les liens profonds sont des URIs personnalisés qui lien vers une partie spécifique de l'application et contiennent toutes les parties ci-dessus. La clé est de définir un schéma personnalisé. `http:` est le schéma avec lequel presque tout le monde est familier mais les schémas peuvent commencer par n'importe quel mot. Un schéma doit commencer par une lettre, mais peut ensuite contenir des lettres, des chiffres, des signes de plus, des signes de moins ou des points. Pratiquement parlant, il n'y a pas de registre central pour prévenir les conflits, donc il est préférable d'inclure votre nom de domaine dans le schéma. Par exemple, `twitter://` est l'URI iOS pour lancer l'application mobile de Twitter.

Tout après le deux-point dans un lien profond est texte de forme libre. C'est à vous de définir sa structure et son interprétation, cependant, une convention commune est de la modéliser après `http:` URLs, y compris les paramètres de `//` et de la requête (e. . `?foo=1&bar=2`). Pour l'exemple Twitter, `twitter://user?screen_name=[id]` serait utilisé pour lancer un profil spécifique dans l'application.

Ces liens profonds sont un outil puissant lorsqu'il est utilisé en tandem avec le Flux d'Actualités [Braze][11]. Fournir des liens profonds comme URI dans les éléments du flux d'actualités vous permet d'utiliser le fil d'actualité comme outil de navigation personnalisé pour diriger les utilisateurs vers le contenu de votre application. Ils peuvent également être utilisés pour diriger les utilisateurs depuis [les notifications push][1] et les messages dans l'application vers les sections et le contenu de l'application concernées.

{% alert note %}
Gardez à l'esprit que l'activation de ces liens profonds nécessite une configuration supplémentaire dans votre application. Veuillez consulter notre documentation sur les [liens profonds pour iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-links) et sur la façon de [lien profond vers le flux d'actualités pour Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/#Android_Deep_Advance) pour comprendre les exigences d'implémentation.
{% endalert %}

## Tags UTM et attribution de campagne

### Qu'est-ce qu'une balise UTM ?

[Les balises UTM (Urchin Traffic Manager)][4] vous permettent d'inclure les détails d'attribution de la campagne directement dans les liens. Les tags UTM sont utilisés par Google Analytics pour collecter des données d'attribution de campagne, et peuvent être utilisés pour suivre les propriétés suivantes:

- `utm_source`: l'identifiant de la source du trafic (par exemple `my_app`)
- `utm_medium`: le média de la campagne (par exemple `le fil d'actualité`)
- `utm_campaign`: l'identifiant de la campagne (par exemple `spring_2016_campaign`)
- `utm_term`: identifiant pour un terme de recherche payant qui a amené l'utilisateur sur votre application ou votre site web (par exemple `pizza`)
- `utm_content`: un identifiant pour le lien/contenu spécifique sur lequel l'utilisateur a cliqué (par exemple `toplink` ou `android_iam_button2`)

Les balises UTM peuvent être intégrées à la fois dans des liens HTTP (web) réguliers et dans des liens profonds et suivies à l'aide de Google Analytics.

### Utiliser des balises UTM avec Braze

Si vous voulez utiliser des balises UTM avec des liens HTTP (web), par exemple, pour faire l'attribution de la campagne pour vos campagnes de messagerie — et votre organisation utilise déjà Google Analytics, vous pouvez simplement utiliser [le constructeur d'URL de Google][6] pour générer des liens UTM. Ces liens peuvent être facilement intégrés dans la copie de campagne Braze comme tout autre lien.

Afin d'utiliser les balises UTM dans les liens profonds vers votre application, votre application doit avoir intégré le [SDK Google Analytics][5] pertinent et [correctement configuré pour gérer les liens profonds][7]. Vérifiez avec vos développeurs si vous n'êtes pas sûr de cela.

Une fois que le SDK Analytics est intégré et configuré, les balises UTM peuvent être utilisées avec des liens profonds dans les campagnes de Braze. Pour configurer les balises UTM pour votre campagne, il vous suffit d'inclure les balises UTM nécessaires dans l'URL de destination ou les liens profonds. Les exemples ci-dessous montrent comment utiliser les balises UTM dans les notifications push, les cartes de News Feed et les messages dans l'application.

#### Attribuer un push s'ouvre avec des tags UTM

Pour inclure les tags UTM dans vos liens profonds pour les notifications push, définissez simplement le comportement de clic du message push comme un lien profond, écrire l'adresse du lien profond et inclure les balises UTM désirées de la manière suivante:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

!\[Tags UTM in Push Message\]\[8\]

#### Attribuer des clics sur le fil d'actualité avec des tags UTM

Les éléments du flux d'actualités profondément liés à votre application peuvent également être configurés pour utiliser les balises UTM. Notez que vous pouvez utiliser `utm_content` pour séparer les liens profonds sur différents systèmes d'exploitation.

!\[Tags UTM in News Fe\]\[9\]

#### Attribuer des clics de message dans l'application avec des tags UTM

De la même manière que les notifications push et les cartes News Feed, vous pouvez inclure des balises UTM dans les liens profonds inclus dans vos messages dans l'application.

!\[UTM Tags in In-App Message\]\[10\]
[8]: {% image_buster /assets/img_archive/push_utm_tags.png %} [9]: {% image_buster /assets/img_archive/news_feed_utm_tags.png %} [10]: {% image_buster /assets/img_archive/iam_utm_tags.png %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
[4]: https://support.google.com/analytics/answer/1033863?hl=en
[5]: https://developers.google.com/analytics/devguides/collection/
[6]: https://support.google.com/analytics/answer/1033867
[7]: https://developers.google.com/analytics/solutions/mobile-campaign-deep-link
[11]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/
