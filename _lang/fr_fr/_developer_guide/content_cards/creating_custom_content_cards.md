---
nav_title: Création de cartes de contenu personnalisées
article_title: Création de cartes de contenu personnalisées
page_order: 5
description: "Cet article couvre les composants de la création d'une interface utilisateur de carte de contenu personnalisée."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Créer des cartes de contenu personnalisées

> Cet article présente l'approche de base que vous utiliserez lors de la mise en œuvre de cartes de contenu type bannière, ainsi que trois cas d'utilisation courants : des images de bannière, une boîte de réception de messages et un carrousel d'images. Il suppose que vous avez déjà lu les autres articles du guide de personnalisation de la carte de contenu pour comprendre ce qui peut être fait par défaut et ce qui nécessite un code personnalisé. Il s'agit surtout de comprendre comment [enregistrer les analyses]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics) pour vos cartes de contenu personnalisées. 

Braze propose différents [types de cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details) : `imageOnly`, `captionedImage`, `classic`, `classicImage` et `control`. Ceux-ci peuvent être utilisés comme point de départ pour vos implémentations, en modifiant leur aspect et leur présentation. 

Vous pouvez également afficher les cartes de contenu de manière totalement personnalisée en créant votre propre interface utilisateur de présentation alimentée par les données des modèles Braze. Analysez les objets des cartes de contenu et extrayez-en les données utiles. Ensuite, utilisez les données du modèle résultant pour alimenter votre interface utilisateur personnalisée - la phase d'exécution de l'[approche "crawl, walk, run" (ramper, marcher, exécuter).]({{site.baseurl}}/developer_guide/customization_guides/customization_overview)

{% alert note %}
Chaque type de carte de contenu par défaut est une sous-classe qui hérite de différentes propriétés de la classe de modèle générique de cartes de contenu. La compréhension de ces propriétés héritées sera utile lors de la personnalisation. Reportez-vous à la documentation de la classe de carte pour plus de détails[(Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard), [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)).
{% endalert %}


## Aperçu de la personnalisation

En fonction de votre cas d'utilisation, la mise en œuvre exacte de votre carte de contenu personnalisée variera quelque peu, mais vous voudrez suivre cette formule de base :

1. Créez votre propre interface utilisateur
2. Écouter les mises à jour des données
3. Enregistrez manuellement les analyses

### Étape 1 : Créer une IU personnalisée 

{% tabs %}
{% tab Android %}

Tout d'abord, créez votre propre fragment personnalisé. Le [`ContentCardFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) par défaut n'est conçu que pour gérer les types de cartes de contenu par défaut, mais il constitue un bon point de départ.

{% endtab %}
{% tab iOS %}

Tout d'abord, créez votre propre composant de contrôleur de visualisation personnalisé. Le [`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller) par défaut n'est conçu que pour gérer les types de cartes de contenu par défaut, mais il constitue un bon point de départ.

{% endtab %}
{% tab Web %}

Tout d'abord, créez votre composant HTML personnalisé qui sera utilisé pour afficher les cartes. 

{% endtab %}
{% endtabs %}

### Étape 2 : S'abonner aux mises à jour de la carte

Ensuite, enregistrez une fonction de rappel pour [vous abonner aux mises à jour des données]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#listening-for-card-updates) lorsque les cartes sont actualisées. 

### Étape 3 : Mettre en œuvre les analyses

Les impressions, les clics et les fermetures de carte de contenu ne sont pas automatiquement enregistrés dans votre vue personnalisée. Vous devez [mettre en œuvre chaque méthode respective]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/#logging-events) pour enregistrer correctement tous les indicateurs dans le tableau de bord analytique de Braze.

## Placements des cartes de contenu

Les cartes de contenu peuvent être utilisées de différentes manières. Trois applications courantes consistent à les utiliser comme centre de message, bannière publicitaire ou carrousel d'images. Pour chacun de ces placements, vous attribuerez des [paires clé-valeur]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) (la propriété `extras` dans le modèle de données) à vos cartes de contenu et, en fonction des valeurs, vous ajusterez dynamiquement le comportement, l'apparence ou la fonctionnalité de la carte au cours de l'exécution. 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Boîte de réception de messages

Les cartes de contenu peuvent être utilisées pour simuler un centre de messages. Dans ce format, chaque message est sa propre carte qui contient des [paires clé-valeur]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) qui alimentent les événements de type "on-click". Ces paires clé-valeur sont les identifiants clés que l'application examine pour décider où aller lorsque l'utilisateur clique sur un message de la boîte réception. Les valeurs des paires clé-valeur sont arbitraires. 

Voici un exemple de configuration du tableau de bord que vous pourriez utiliser pour créer deux cartes de message : un message est un appel à l'action pour qu'un utilisateur ajoute ses préférences afin de recevoir des recommandations de lecture ciblées, et un message fournit un code de coupon à un segment de nouveaux abonnés. 

![]({% image_buster /assets/img/content_cards/content-card-message-inbox-with-kvps.png %}){: style="max-width:20%;float:right;margin-left:15px;border:0px;"}

Voici quelques exemples de paires clé-valeur pour la carte de recommandation de lecture :

- corps : Ajoutez vos centres d'intérêt à votre profil Politer Weekly pour obtenir des recommandations de lecture personnalisées.
- style : info
- class_type : notification_center
- card_priority : 1

Voici quelques exemples de paires clé-valeur pour un coupon de nouvel utilisateur abonné :

- titre : Abonnez-vous pour bénéficier de jeux illimités
- corps : Offre spéciale de fin d'été - 10 % de réduction sur les jeux Politer
- buttonText : S'abonner
- style : promo
- class_type : notification_center
- card_priority : 2
- conditions : new_subscribers_only

Vos marketeurs peuvent rendre cette carte de contenu accessible uniquement à un segment de nouveaux utilisateurs. 

Vous devez traiter chacune des valeurs. Les clés telles que `body`, `title` et `buttonText` peuvent comporter des valeurs de chaînes de caractères simples que vos marketeurs peuvent définir. Les clés telles que `terms` peuvent avoir des valeurs qui fournissent une petite collection de phrases approuvées par votre service juridique. C'est vous qui décidez comment rendre `style` et `class_type` sur votre application ou votre site. 

{% details Plus d'explications pour Android %}

Dans le SDK Android et FireOS, la logique du centre de messages est pilotée par la valeur `class_type` qui est fournie par les paires clé-valeur de Braze. En utilisant la méthode [`createContentCardable`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/implementation_guide), vous pouvez filtrer et identifier ces types de classes.

{% tabs %}
{% tab Kotlin %}
**Utilisation de `class_type` pour le comportement au clic**<br>
Lorsque nous augmentons les données de la carte de contenu dans nos classes personnalisées, nous utilisons la propriété `ContentCardClass` des données pour déterminer quelle sous-classe concrète doit être utilisée pour stocker les données.

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass?): ContentCardable?{
        return when(type){
            ContentCardClass.AD -> Ad(metadata)
            ContentCardClass.MESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass.NOTIFICATION_CENTER -> FullPageMessage(metadata)
            ContentCardClass.ITEM_GROUP -> Group(metadata)
            ContentCardClass.ITEM_TILE -> Tile(metadata)
            ContentCardClass.COUPON -> Coupon(metadata)
            else -> null
        }
    }
```

Ensuite, lors de la manipulation de l’interaction utilisateur avec la liste des messages, nous pouvons utiliser le type de message pour déterminer la vue à afficher à l’utilisateur.

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //...
        listView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
           when (val card = dataProvider[position]){
                is WebViewMessage -> {
                    val intent = Intent(this, WebViewActivity::class.java)
                    val bundle = Bundle()
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.contentString)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
                is FullPageMessage -> {
                    val intent = Intent(this, FullPageContentCard::class.java)
                    val bundle = Bundle()
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.icon)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.messageTitle)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.cardDescription)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        }
    }
```
{% endtab %}
{% tab Java %}
**Utilisation de `class_type` pour le comportement au clic**<br>
Lorsque nous augmentons les données de la carte de contenu dans nos classes personnalisées, nous utilisons la propriété `ContentCardClass` des données pour déterminer quelle sous-classe concrète doit être utilisée pour stocker les données.

```java
private ContentCardable createContentCardable(Map<String, ?> metadata,  ContentCardClass type){
    switch(type){
        case ContentCardClass.AD:{
            return new Ad(metadata);
        }
        case ContentCardClass.MESSAGE_WEB_VIEW:{
            return new WebViewMessage(metadata);
        }
        case ContentCardClass.NOTIFICATION_CENTER:{
            return new FullPageMessage(metadata);
        }
        case ContentCardClass.ITEM_GROUP:{
            return new Group(metadata);
        }
        case ContentCardClass.ITEM_TILE:{
            return new Tile(metadata);
        }
        case ContentCardClass.COUPON:{
            return new Coupon(metadata);
        }
        default:{
            return null;
        }
    }
}

```

Ensuite, lors de la manipulation de l’interaction utilisateur avec la liste des messages, nous pouvons utiliser le type de message pour déterminer la vue à afficher à l’utilisateur.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        //...
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
               ContentCardable card = dataProvider.get(position);
               if (card instanceof WebViewMessage){
                    Bundle intent = new Intent(this, WebViewActivity.class);
                    Bundle bundle = new Bundle();
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.getContentString());
                    intent.putExtras(bundle);
                    startActivity(intent);
                }
                else if (card instanceof FullPageMessage){
                    Intent intent = new Intent(this, FullPageContentCard.class);
                    Bundle bundle = Bundle();
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.getIcon());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.getMessageTitle());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.getCardDescription());
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        });
    }
```

{% endtab %}
{% endtabs %}
{% enddetails %}

### Carrousel

Les cartes de contenu peuvent être placées dans un flux carrousel où l'utilisateur peut glisser horizontalement pour voir d'autres cartes en fonctionnalité. 

Pour créer un carrousel de cartes de contenu, implémentez une logique qui observe les [changements dans vos cartes de contenu]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed) et gère l'arrivée des cartes de contenu. Par défaut, les cartes de contenu sont triées par date de création (la plus récente en premier) et un utilisateur voit toutes les cartes auxquelles il est éligible. Mettez en œuvre une logique côté client pour afficher un nombre spécifique de cartes dans le carrousel à tout moment.

Cela dit, vous pouvez commander et appliquer une logique d'affichage supplémentaire de différentes manières. Par exemple, vous pouvez sélectionner les cinq premiers objets de la carte de contenu dans le tableau ou introduire des paires clé-valeur pour créer une logique conditionnelle.

Si vous implémentez un carrousel comme flux secondaire de cartes de contenu, reportez-vous à la section [Personnaliser le flux de cartes de contenu par défaut]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) pour savoir comment trier les cartes dans le flux approprié en fonction des paires clé-valeur.

### Bannière

Les cartes de contenu n'ont pas besoin de ressembler à des "cartes". Par exemple, les cartes de contenu peuvent prendre la forme d'une bannière dynamique qui s'affiche de manière continue sur votre page d'accueil ou en haut des pages désignées.

Pour ce faire, vos marketeurs créeront une campagne ou une étape du canvas avec un type de carte de contenu **Image Only.**  Ensuite, définissez les paires clé-valeur qui conviennent à l'utilisation des [cartes de contenu en tant que contenu supplémentaire]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content).


