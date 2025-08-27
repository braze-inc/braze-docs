---
nav_title: Lien profond au contenu d’application
article_title: Lien profond au contenu d’application
page_order: 3
description: "Cet article de référence explique comment ajouter un lien profond dans le contenu de vos messages in-app."

---

# Lien profond vers le contenu in-app

## Qu’est-ce qu’un lien profond ?

La création de liens profonds est un moyen de lancer une application native et de fournir des informations supplémentaires lui indiquant d'effectuer une action spécifique ou d'afficher un contenu spécifique.

Cela comporte trois parties :

1. Identifiez l'application à lancer.
2. Indiquer à l'application l'action à effectuer.
3. Fournissez à l'action toutes les données supplémentaires dont elle aura besoin.

Les liens profonds sont des URIs personnalisés qui sont liés à une partie spécifique de l’application et contiennent les trois de ces parties. La clé est de définir un schéma personnalisé. `http:` est le schéma que la plupart des gens connaissant, mais les schémas peuvent commencer par n’importe quel mot. Un schéma doit commencer par une lettre, mais peut ensuite contenir des lettres, des chiffres, des signes plus, des signes moins ou des points. Il n’existe pas de registre central pour éviter les conflits, il est donc recommandé d’inclure votre nom de domaine dans le schéma. Par exemple, `twitter://` est l'URI iOS pour lancer l'application mobile pour X, anciennement Twitter.

Tout ce qui se trouve après la virgule dans un lien profond, est un texte libre. C'est à vous de définir sa structure et son interprétation ; cependant, une convention courante consiste à s'inspirer des URL `http:`, en incluant un `//` initial et des paramètres de requête (par exemple, `?foo=1&bar=2`). Pour l'exemple précédent, `twitter://user?screen_name=[id]` serait utilisé pour lancer un profil spécifique dans l'application.

{% alert important %}
Braze ne permet pas d'utiliser un wrapper comme Flutter pour envoyer des liens profonds. Pour utiliser cette fonctionnalité, vous devez configurer les liens profonds au niveau de la couche native.
{% endalert %}

## Balises UTM et attribution de campagne

### Qu’est-ce qu’une balise UTM ?

Les balises [UTM (Urchin Traffic Manager)](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article) vous permettent d'inclure directement les détails d'attribution de la campagne dans les liens. Les balises UTM sont utilisées par Google Analytics pour collecter les données d’attribution de campagne et peuvent être utilisées pour suivre les propriétés suivantes :

- `utm_source` : L'identifiant de la source du trafic (par exemple,`my_app`)
- `utm_medium` : Le support de la campagne (par exemple,`newsfeed`)
- `utm_campaign` : L'identifiant de la campagne (par exemple,`spring_2016_campaign`).
- `utm_term` : Identifiant d'un terme de recherche d'utilisateurs payant qui a amené l'utilisateur à votre application ou site web (par exemple,`pizza`).
- `utm_content` : Un identifiant pour le lien ou le contenu spécifique sur lequel l'utilisateur a cliqué (par exemple,`toplink` ou `android_iam_button2`).

Les balises UTM peuvent être intégrées à des liens HTTP (Web) réguliers et des liens profonds et suivies à l’aide de Google Analytics.

### Utilisation des balises UTM avec Braze

Si vous souhaitez utiliser des balises UTM avec des liens HTTP (web) ordinaires (par exemple, pour attribuer des campagnes à vos e-mails) et que votre organisation utilise déjà Google Analytics, vous pouvez utiliser [le générateur d'URL de Google](https://ga-dev-tools.google/ga4/campaign-url-builder/) pour générer des liens UTM. Ces liens peuvent être facilement intégrés à la campagne Braze, comme tout autre lien.

Pour utiliser les balises UTM dans les liens profonds vers votre appli, celle-ci doit avoir le [SDK Google Analytics](https://developers.google.com/analytics/devguides/collection/) correspondant intégré et correctement configuré pour gérer les liens profonds. Vérifiez auprès de vos développeurs si vous avez des questions.

Une fois le SDK Analytics intégré et configuré, les balises UTM peuvent être utilisées avec les liens profonds dans les campagnes Braze. Pour implémenter des balises UTM pour votre campagne, incluez les étiquettes UTM nécessaires dans l'URL de destination ou les liens profonds. Les exemples suivants montrent comment utiliser les balises UTM dans les notifications push et les messages in-app.

#### L’attribution de la notification push s’ouvre avec les balises UTM

Pour inclure des balises UTM dans vos liens profonds pour les notifications push, définissez le comportement au clic du message push comme étant un lien profond, puis écrivez l'adresse du lien profond et incluez les balises UTM souhaitées de la manière suivante :

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![]({% image_buster /assets/img_archive/push_utm_tags.png %})

#### Attribution de messages dans l’application avec des balises UTM

Pour inclure des balises UTM dans les liens profonds de vos messages in-app, procédez comme suit :

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![]({% image_buster /assets/img_archive/iam_utm_tags.png %})

