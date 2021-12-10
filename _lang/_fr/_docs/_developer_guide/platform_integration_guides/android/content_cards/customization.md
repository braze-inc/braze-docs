---
nav_title: Personnalisation
article_title: Personnalisation de la carte de contenu pour Android/FireOS
page_order: 2
platform:
  - Android
  - Pare-feu
description: "Cet article couvre les options de personnalisation de vos Cartes de Contenu dans votre application Android."
channel:
  - cartes de contenu
---

# Personnalisation

## Default styling {#default-styling-for-android}

Braze In-App Messages et Cartes de Contenu sont fournis avec un look et une sensation par défaut qui correspond aux directives de l'interface utilisateur standard d'Android et fournissent une expérience transparente. Vous pouvez voir ces styles par défaut dans le fichier [`res/values/styles.xml`][42] dans la distribution Braze SDK.

```xml
  <! - Exemple de Cartes de Contenu -->
  <style name="Braze.ContentCards.CaptionedImage.Description">
    <item name="android:textColor">@color/com_appboy_description</item>
    <item name="android:textSize">15. sp</item>
    <item name="android:includeFontPadding">faux</item>
    <item name="android:paddingBottom">8. dp</item>
    <item name="android:layout_marginLeft">10. dp</item>
    <item name="android:layout_marginRight">10.0dp</item>
    <item name="android:layout_marginTop">8. dp</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:layout_below">@id/com_appboy_content_cards_captioned_image_title_container</item>
  </style>
```

## Overriding styles {#overriding-styles-for-android}

Si vous préférez, vous pouvez remplacer ces styles pour créer un look et une sensation qui convient mieux à votre application. Pour remplacer un style, copiez-le dans son intégralité dans le fichier `styles.xml` de votre projet et apportez des modifications. Le style entier doit être copié dans votre fichier local `styles.xml` pour que tous les attributs soient correctement définis.

### Surcharge de style correcte {#correct-style-override-for-android}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/menthe</item>
  <item name="android:cacheColorHint">@color/menthe</item>
  <item name="android:divider">@android:color/transparent</item>
  <item name="android:dividerHeight">16. dp</item>
  <item name="android:paddingLeft">12.5dp</item>
  <item name="android:paddingRight">5. dp</item>
  <item name="android:scrollbarStyle">outsideInset</item>
</style>
```

### Surcharge de style incorrecte {#incorrect-style-override-for-android}

```xml
<style name="Braze.ContentCardsDisplay">
  <item name="android:background">@color/menthe</item>
  <item name="android:cacheColorHint">@color/menthe</item>
</style>
```

## Personnalisation du flux de carte de contenu par défaut {#content-cards-fragment-customization}

Cette section couvre la personnalisation du [ContentCardsFragment][49] dont la source peut être trouvée [ici][54].

### Personnalisation du message d'erreur de connexion réseau

Si le [ContentCardsFragment][49] détermine qu'une mise à jour de la carte de contenu a échoué, elle affichera un message d'erreur de connexion réseau.

Un adaptateur spécial, l' [AppboyEmptyContentCardsAdapter][50] remplace le standard [AppboyCardAdapter][53] pour afficher le message d'erreur. Pour définir le message personnalisé lui-même, remplacez la ressource de chaîne `com_appboy_feed_empty`.

Le style utilisé pour afficher ce message peut être trouvé via [`Appboy.ContentCardsDisplay.Empty`][52] et est reproduit ci-dessous.

```xml
<style name="Braze.ContentCardsDisplay.Empty">
  </item>. dp</item>
  <item name="android:text">@string/com_appboy_feed_empty</item>
  <item name="android:textColor">@color/com_appboy_title</item>
  <item name="android:textSize">18. sp</item>
  <item name="android:gravity">centre</item>
  <item name="android:layout_height">match_parent</item>
  <item name="android:layout_width">match_parent </item>
</style>
```

Pour personnaliser complètement le comportement des erreurs réseau, vous pouvez étendre la variable [ContentCardsFragment][54] et définir la variable `mShowNetworkUnavailableRunnable` pour effectuer une autre action.

## Éléments de style des Cartes de Contenu {#content-cards-style-elements-for-android}

### Custom font {#setting-a-custom-font-for-android}

Braze permet de définir une police personnalisée en utilisant le guide de la famille de polices [][40]. Pour l'utiliser, remplacez un style pour les cartes et utilisez l'attribut `fontFamily` pour demander à Braze d'utiliser votre famille de polices personnalisée.

Par exemple, pour mettre à jour la police sur tous les titres des Cartes d'images sous-titrées, remplacez le style `Appboy.ContentCards.CaptionedImage.Title` et faites référence à votre famille de polices personnalisées. La valeur de l'attribut doit pointer vers une famille de polices dans votre répertoire `res/font`.

Voici un exemple tronqué avec une famille de polices personnalisées, `my_custom_font_family`, référencé sur la dernière ligne:

```xml
  <style name="Braze.ContentCards.CaptionedImage.Title">
    <item name="android:layout_width">wrap_content</item>
...
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

### Icône épinglée personnalisée {#setting-a-custom-pinned-icon-for-android}

Pour définir une icône personnalisée épinglée, remplacez le style `Appboy.ContentCards.PinnedIcon`. Votre image personnalisée doit être déclarée dans l'élément `android:src`.

### Personnalisation de la commande de la carte affichée {#customizing-displayed-card-order-for-android}

Les `ContentCardsFragment` s'appuient sur un [`IContentCardsUpdateHandler`][44] pour gérer tout tri ou modification des Cartes de Contenu avant qu'elles ne soient affichées dans le flux. Un gestionnaire de mise à jour personnalisé peut être défini via [`setContentCardUpdateHandler`][45] sur votre [`ContentCardsFragment`][49].

Filtrer les cartes de contenu avant qu'elles n'atteignent le flux de l'utilisateur est un cas d'utilisation courant et pourrait être réalisé en lisant les paires de valeur clé définies sur le tableau de bord via la carte [`. etExtras()`][36] et exécutant toute logique que vous voudriez dans le gestionnaire de mise à jour.

Ce qui suit est la valeur par défaut `IContentCardsUpdateHandler` et peut être utilisé comme point de départ pour les personnalisations.

{% tabs %}
{% tab JAVA %}

```java
la classe publique DefaultContentCardsUpdateHandler implémente IContentCardsUpdateHandler {

  // Interface qui doit être implémentée et fournie en tant que champ public CREATOR
  // qui génère des instances de votre classe Parcelable à partir d'un Parcel.
  public statique final Parcelable.Creator<DefaultContentCardsUpdateHandler> CREATOR = new Parcelable. reator<DefaultContentCardsUpdateHandler>() {
    public DefaultContentCardsUpdateHandler createFromParcel(Parcel in) {
      return new DefaultContentCardsUpdateHandler();
    }

    public DefaultContentCardsUpdateHandler[] newArray(int size) {
      return new DefaultContentCardsUpdateHandler[size];
    }
  };

  @Override
  liste publique<Card> handleCardUpdate(ContentCardsUpdatedEvent event) {
    liste<Card> tritedCards = événement. Toutes les cartes();
    // Trier par épinglé, puis par l'horodatage 'updated' descendant de
    // épinglé avant non épinglé
    Collections. ort(triezCards, nouveau comparateur<Card>() {
      @Override
      compare(Card cardA, Carte de carteB) {
        // Un affichage au-dessus de B
        si (cardA. etIsPinned() && !cardB. etIsPinned()) {
          return -1;
        }

        // B affiche au dessus de A
        if (! Arda. etIsPinned() && cartes. etIsPinned()) {
          return 1;
        }

        // À ce stade, Les deux A & B sont épinglés ou les deux A & B ne sont pas épinglés
        // A affiche au-dessus de B puisque A est plus récent
        si (cardA. etUpdated() > cartes. etUpdated()) {
          return -1;
        }

        // B s'affiche au-dessus de A puisque A est plus récent
        if (cardA. etUpdated() < carte. etUpdated()) {
          return 1;
        }

        // À ce stade, chaque champ triable correspond donc gardez l'ordre naturel
        retour 0;
      }
    });

    retours triés par cartes;
  }

  // Méthode d'interface Parcelable
  @Override
  public int describeContents() {
    return 0;
  }

  // Méthode d'interface Parcelable
  @Override
  public void writeToParcel(Parcel dest, int flags) {
    // Aucun état n'est conservé dans cette classe, donc le colis est laissé non modifié
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class DefaultContentCardsUpdateHandler : IContentCardsUpdateHandler {
  override fun handleCardUpdate(event: ContentCardsUpdatedEvent): List<Card> {
    val sortedCards = event. llCards
    // Trier par épinglé, puis par l'horodatage 'updated' descendant
    // épinglé avant les triées non épinglées
    . ortWith(Comparator sort@{ cardA: Carte, cardB: Card ->
      // A affiche au dessus de B
      si (cardA. Épinglé && !cardB. spinned) {
        return@sort -1
      }

      // B s'affiche au-dessus de A
      if (! Arda. Épinglé && carteB. spinned) {
        return@sort 1
      }

      // À ce stade, Les deux A & B sont épinglés ou les deux A & B ne sont pas épinglés
      // A affiche au-dessus de B puisque A est plus récent
      si (cardA. pdé > carteB. pdated) {
        return@sort -1
      }

      // B s'affiche au-dessus de A puisque A est plus récent
      if (cardA. pdé < carteB. pdated) {
        return@sort 1
      }
      0
    })
    return sortedCards
  }

  // méthode d'interface Parcelable
  override fun describeContents(): Int {
    return 0
  }

  // méthode d'interface Parcelable
  override fun writeToParcel(dest: Parcel, flags: Int) {
    // Aucun état n'est conservé dans cette classe, donc le colis est laissé non modifié
  }

  objet compagnon {
    // Interface qui doit être implémentée et fournie en tant que champ CREATOR public
    // qui génère des instances de votre classe Parcelable à partir d'un Parcel.
    val CREATOR: Parcelable.Creator<DefaultContentCardsUpdateHandler?> = object : Parcelable.Creator<DefaultContentCardsUpdateHandler?> {
      override fun createFromParcel(`in`: Parcel): DefaultContentCardsUpdateHandler? {
        return DefaultContentCardsUpdateHandler()
      }

      override fun newArray(size: Int): Tableau<DefaultContentCardsUpdateHandler?> {
        return arrayOfNulls(size)
      }
    }
  }
 } } } } } } } } }
```

{% endtab %}
{% endtabs %}

> Ce code peut également être trouvé ici, [DefaultContentCardsUpdateHandler][46].

Et voici comment utiliser la classe ci-dessus :

{% tabs %}
{% tab JAVA %}

```java
IContentCardsUpdateHandler cardUpdateHandler = new DefaultContentCardsUpdateHandler();

fragment ContentCardsFragment = getMyCustomFragment();
fragment.setContentCardUpdateHandler(cardUpdateHandler);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val cardUpdateHandler = DefaultContentCardsUpdateHandler()

val fragment = getMyCustomFragment()
fragment.setContentCardUpdateHandler(cardUpdateHandler)
```

{% endtab %}
{% endtabs %}

### Personnalisation du rendu de la carte {#customizing-card-rendering-for-android}

Voici des informations sur la façon de modifier le rendu d'une carte dans la vue recyclée. L'interface `IContentCardsViewBindingHandler` définit comment toutes les cartes de contenu sont rendues. Vous pouvez personnaliser ceci pour changer tout ce que vous voulez.

{% tabs %}
{% tab JAVA %}

```java
la classe publique DefaultContentCardsViewBindingHandler implémente IContentCardsViewBindingHandler {
  // Interface qui doit être implémentée et fournie en tant que champ public CREATOR
  // qui génère des instances de votre classe Parcelable à partir d'un colis.
  public statique final Parcelable.Creator<DefaultContentCardsViewBindingHandler> CREATOR = new Parcelable. reator<DefaultContentCardsViewBindingHandler>() {
    public DefaultContentCardsViewBindingHandler createFromParcel(Parcel in) {
      return new DefaultContentCardsViewBindingHandler();
    }

    public DefaultContentCardsViewBindingHandler[] newArray(int size) {
      return new DefaultContentCardsViewBindingHandler[size];
    }
  };

  /**
   * Une cache pour les vues utilisées dans la liaison des éléments dans l'android {@link. upport.v7.widget.RecyclerView}.
   */
  carte finale privée<CardType, BaseContentCardView> mContentCardViewCache = new HashMap<CardType, BaseContentCardView>();

  @Override
  public ContentCardViewHolder onCreateViewHolder(Contexte contextuel Lister<Card> cartes, ViewGroup viewGroup, int viewType) {
    CardType cardType = CardType. romValue(viewType);
    return getContentCardsViewFromCache(context cardType). ReateViewHolder(viewGroup);
  }

  @Override
  public void onBindViewHolder(Contexte contextuel, Liste<Card> cartes, ContentCardViewHolder viewHolder, int adapterPosition) {
    Card cardAtPosition = cartes. et(adapterPosition);
    BaseContentCardView contentCardView = getContentCardsViewFromCache(context cardAtPosition.getCardType());
    contentCardView. indViewHolder(viewHolder, cardAtPosition);
  }

  @Override
  public int getItemViewType(Contexte contextuel, Liste<Card> cartes, int adapterPosition) {
    carte = cartes. et(adapterPosition);
    return card.getCardType(). etValue();
  }

  /**
   * Obtient une instance en cache d'un {@link BaseContentCardView} pour création/binding de vue pour un {@link CardType} donné.
   * Si le {@link CardType} n'est pas trouvé dans la cache, puis une implémentation de liaison de vue pour que {@link CardType}
   * soit créé et ajouté à la cache.
   */
  @VisibleForTesting
  BaseContentCardView getContentCardsViewFromCache(Context context CardType cardType) {
    if (!mContentCardViewCache. ontainsKey(cardType)) {
      // Créer la vue ici
      BaseContentCardView contentCardView;
      interrupteur (cardType) {
        cas BANNER :
          contentCardView = new BannerImageContentCardView(context);
          pause;
        cas CAPTIONED_IMAGE :
          contentCardView = new CaptionedImageContentCardView(context);
          pause;
        cas SHORT_NEWS :
          contentCardView = new ShortNewsContentCardView(contexte);
          pause;
        cas TEXT_ANNOUNCEMENT :
          contentCardView = new TextAnnouncementContentCardView(contexte);
          pause;
        par défaut :
          contentCardView = new DefaultContentCardView(context);
          pause;
      }
      mContentCardViewCache. ut(cardType, contentCardView);
    }
    return mContentCardViewCache. et(cardType);
  }

  // Méthode d'interface Parcelable
  @Override
  public int describeContents() {
    return 0;
  }

  // Méthode d'interface Parcelable
  @Override
  public void writeToParcel(Parcel dest, int flags) {
    // Garder les vues à travers une transition peut conduire à une fuite de ressource
    // afin que le colis soit laissé non modifié
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class DefaultContentCardsViewBindingHandler : IContentCardsViewBindingHandler {
  // Interface qui doit être implémentée et fournie en tant que champ public CREATOR
  // qui génère des instances de votre classe Parcelable à partir d'un Parcel.
  val CREATOR: Parcelable.Creator<DefaultContentCardsViewBindingHandler?> = object : Parcelable.Creator<DefaultContentCardsViewBindingHandler?> {
    override fun createFromParcel(`in`: Parcel): DefaultContentCardsViewBindingHandler? {
      return DefaultContentCardsViewBindingHandler()
    }

    override fun newArray(size: Int): Array<DefaultContentCardsViewBindingHandler?> {
      return arrayOfNulls(size)
    }
  }

  /**
    * Un cache pour les vues utilisées dans la liaison des éléments dans le [RecyclerView].
    */
  private val mContentCardViewCache: MutableMap<CardType, BaseContentCardView<*>?> = HashMap()

  override fun onCreateViewHolder(context: Context?, cards: List<Card?>?, viewGroup: ViewGroup?, viewType: Int): ContentCardViewHolder? {
    val cardType = CardType.fromValue(viewType)
    return getContentCardsViewFromCache(context cardType)!!. reateViewHolder(viewGroup)
  }

  surcharge fun onBindViewHolder(context: Context?, cartes: List<Card>, viewHolder: ContentCardViewHolder? adapterPosition: Int) {
    if (adapterPosition < 0 || adapterPosition >= cartes. Taille) {
      return
    }
    carte val cardAtPosition = cartes[adapterPosition]
    val contentCardView = getContentCardsViewFromCache(context cardAtPosition. ardType)
    if (viewHolder != null) {
      contentCardView!!. indViewHolder(viewHolder, cardAtPosition)
    }
  }

  remplacent getItemViewType(contexte: Context? cartes: Liste<Card>, adapterPosition: Int): Int {
    if (adapterPosition < 0 || adapterPosition >= cartes. Taille) {
      return -1
    }
    carte val = cartes[adapterPosition]
    retour card.cardType. alue
  }

  /**
    * Obtient une instance en cache d'une [BaseContentCardView] pour la création/liaison de vue pour un [CardType].
    * Si le [CardType] n'est pas trouvé dans la cache, alors une implémentation de liaison de vue pour que [CardType]
    * soit créée et ajoutée au cache.
    */
  @VisibleForTesting
  fun getContentCardsViewFromCache(contexte: Context?, cardType: CardType): BaseContentCardView<Card>? {
    if (!mContentCardViewCache. ontainsKey(cardType)) {
      // Créer la vue ici
      val contentCardView: BaseContentCardView<*> = when (cardType) {
        CardType. ANNER -> BannerImageContentCardView(contexte)
        CardType. APTIONED_IMAGE -> CaptionedImageContentCardView(contexte)
        CardType. HORT_NEWS -> ShortNewsContentCardView(contexte)
        CardType. EXT_ANNOUNCEMENT -> TextAnnouncementContentCardView(contexte)
        else -> DefaultContentCardView(context)
      }
      mContentCardViewCache[cardType] = contentCardView
    }
    return mContentCardViewCache[cardType] as BaseContentCardView<Card>?
  }

  // Méthode d'interface Parcelable
  surchargeant fun describeContents(): Int {
    return 0
  }

  // Méthode d'interface Parcelable
  écraser fun writeToParcel(dest: Parcel? flags: Int) {
    // Garder les vues à travers une transition peut conduire à une fuite de ressource
    // afin que le colis reste intact
  }

```

{% endtab %}
{% endtabs %}

> Ce code peut également être trouvé ici, [DefaultContentCardsViewBindingHandler][56].

Et voici comment utiliser la classe ci-dessus :

{% tabs %}
{% tab JAVA %}

```java
IContentCardsViewBindingHandler viewBindingHandler = new DefaultContentCardsViewBindingHandler();

ContentCardsFragment fragment = getMyCustomFragment();
fragment.setContentCardsViewBindingHandler(viewBindingHandler);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val viewBindingHandler = DefaultContentCardsViewBindingHandler()

fragment val = getMyCustomFragment()
fragment.setContentCardsViewBindingHandler(viewBindingHandler)
```

{% endtab %}
{% endtabs %}

Il y a des ressources supplémentaires pertinentes sur ce sujet disponibles [ici](https://medium.com/google-developers/android-data-binding-recyclerview-db7c40d9f0e4).

### Cartes de contenu personnalisées cliquées sur l'écouteur

Vous pouvez gérer manuellement les clics des Cartes de Contenu en définissant un écouteur de clic personnalisé. Cela permet d'utiliser des cas tels que l'utilisation sélective du navigateur web natif pour ouvrir des liens Web.

#### Étape 1 : Implémenter un clic sur écouteur de cartes de contenu

Créez une classe qui implémente [IContentCardsActionListener][43] et enregistrez-le avec `BrazeContentCardsManager`. Implémenter la méthode `onContentCardClicked()` , qui sera appelée lorsque l'utilisateur clique sur une carte de contenu.

#### Étape 2 : Instructer Braze pour utiliser votre écouteur de clic de carte de contenu

Vous pouvez voir un exemple des étapes 1 et 2 ici:

{% tabs %}
{% tab JAVA %}

```java
BrazeContentCardsManager.getInstance(). etContentCardsActionListener(new IContentCardsActionListener() {
  @Override
  public boolean onContentCardClicked(Contexte contextuel, Carte de carte, Action de carte IAction) {
    retour faux ;
  }

  @Override
  public vide, onContentCardDismissed(Contexte de la carte) {

  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeContentCardsManager.getInstance(). ontentCardsActionListener = objet : IContentCardsActionListener {
  outrepasser le fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Booléen {
    return false
  }

  surcharge fun onContentCardDismissed(contexte: Contexte, carte: Card) {

  }
}
```

{% endtab %}
{% endtabs %}

### Personnalisation du thème sombre

Par défaut, les affichages des cartes de contenu répondront automatiquement aux changements de thème sur l'appareil avec un ensemble de couleurs et de modifications de mise en page.

Pour remplacer ce comportement, remplacez les valeurs `values-night` dans `android-sdk-ui/src/main/res/values-night/colors.xml` et `android-sdk-ui/src/main/res/values-night/dimens.xml`.

### Affichage de la carte de contenu entièrement personnalisé {#fully-custom-content-card-display-for-android}

Si vous souhaitez afficher les Cartes de Contenu d'une manière totalement personnalisée, il est possible de le faire en utilisant vos propres vues remplies de données de nos modèles. Pour obtenir les modèles de Cartes de Contenu de Braze, vous devez vous abonner aux mises à jour de la fiche de contenu et utiliser les données du modèle qui en résultent pour remplir vos vues. Vous devrez également enregistrer les analyses sur les objets du modèle lorsque les utilisateurs interagissent avec vos vues.

#### Partie 1 : S'abonner aux mises à jour de la carte de contenu

Tout d'abord, déclarez une variable privée dans votre classe personnalisée pour conserver votre abonné :

{% tabs %}
{% tab JAVA %}

```java
// variable d'abonné
privée IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
private var mContentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

{% endtab %}
{% endtabs %}

Ensuite, ajoutez le code suivant pour vous abonner aux mises à jour de la carte de contenu Braze, généralement à l'intérieur de l'activité de votre carte de contenu personnalisée `Activity.onCreate()`:

{% tabs %}
{% tab JAVA %}

```java
// Supprimez l'abonné précédent avant de reconstruire un nouveau avec notre nouvelle activité.
Braze.getInstance(context).removeSingleSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent. laiton);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
    @Override
    public void trigger(ContentCardsUpdatedEvent event) {
        // Liste de toutes les fiches de contenu
        Liste<Card> allCards = event. etAllCards();

        // Votre logique ci-dessous
    }
};
Braze.getInstance(contexte). Inscrit à la mise à jour des cartes de contenu (mContentCardsUpdatedSubscriber);
Braze.getInstance(context).requestContentCardsRefresh(true);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Supprimez l'abonné précédent avant de reconstruire un nouveau avec notre nouvelle activité.
Braze.getInstance(context).removeSingleSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class ava)
mContentCardsUpdatedSubscriber = IEventSubscriber { event ->
  // Liste de toutes les fiches de contenu
  allCards valables = événement. llCards

  // Votre logique ci-dessous
}
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

{% endtab %}
{% endtabs %}

Nous vous recommandons également de vous désabonner lorsque votre activité personnalisée se déconnecte. Add the following code to your activity's `onDestroy()` lifecycle method:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).removeSingleSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).removeSingleSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endtab %}
{% endtabs %}

#### Partie 2 : Analyses de la journalisation

Lorsque vous utilisez des vues personnalisées, vous devrez également enregistrer manuellement les analytiques, car les analyses ne sont gérées automatiquement que lorsque vous utilisez les vues Braze.

Pour enregistrer l'affichage des Cartes de Contenu, appelez [`Appboy.logContentCardsDisplayed()`][41].

Pour enregistrer une impression ou cliquer sur une carte, appelez [`Card.logClick()`][7] ou [`Card.logImpression()`][8] respectivement.

Pour les campagnes utilisant des cartes de contrôle pour les tests A/B, vous pouvez utiliser la carte [`. sControl()`][55] pour déterminer si une carte est vide, et utilisée uniquement à des fins de suivi.

#### Rejeter manuellement une carte de contenu

Vous pouvez enregistrer manuellement ou définir une carte de contenu comme "rejetée" sur Braze [pour une carte particulière avec `setIsDismissed`](https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#setIsDismissed-boolean-).

Si une carte est déjà marquée comme rejetée, elle ne peut plus être marquée comme rejetée.

## Désactivation du glissement pour rejeter

La désactivation des fonctionnalités de glissement vers rejet se fait par carte via la méthode [`card.setIsDismissibleByUser()`][48]. Les cartes peuvent être interceptées avant d'être affichées en utilisant la méthode [`ContentCardsFragment.setContentCardUpdateHandler()`][45].

## Paires clé-valeur

`Les objets` de la carte peuvent éventuellement transporter des paires clé-valeur sous la forme `d'extras`. Celles-ci peuvent être utilisées pour envoyer des données avec une carte `` pour une gestion ultérieure par l'application.

Consultez le [Javadoc][36] pour plus d'informations.

{% alert note %}
Les cartes de contenu ont une taille maximale de 2 Ko pour le contenu que vous entrez dans le tableau de bord Braze. Ceci inclut le texte du message, les URL de l'image, les liens et les paires clé-valeur. Le dépassement de ce montant empêchera l'envoi de la carte.
{% endalert %}

## GIFs {#gifs-news-content-cards}

{% alert note %}
Cette section s'applique aux intégrations qui utilisent le fragment ou les vues de cartes de contenu par défaut du Braze SDK pour afficher les cartes de contenu.
{% endalert %}

{% include archive/android/gifs.md channel="Cartes de contenu" %}

[7]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#logClick--
[8]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#logImpression--
[36]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#getExtras--
[36]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#getExtras--
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[41]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/Appboy.html#logContentCardsDisplayed--
[42]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml
[43]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/contentcards/listeners/IContentCardsActionListener.html
[44]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/ui/contentcards/handlers/IContentCardsUpdateHandler.html
[45]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/ui/contentcards/ContentCardsFragment.html#setContentCardUpdateHandler-com.appboy.ui.contentcards.handlers.IContentCardsUpdateHandler-
[45]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/ui/contentcards/ContentCardsFragment.html#setContentCardUpdateHandler-com.appboy.ui.contentcards.handlers.IContentCardsUpdateHandler-
[46]: https://github.com/Appboy/appboy-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsUpdateHandler.java
[48]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#setIsDismissibleByUser-boolean-
[49]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/ui/contentcards/ContentCardsFragment.html
[49]: https://appboy.github.io/appboy-android-sdk/javadocs/com/braze/ui/contentcards/ContentCardsFragment.html
[50]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/contentcards/AppboyEmptyContentCardsAdapter.html
[52]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml#L552-L560
[53]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/ui/contentcards/AppboyCardAdapter.html
[54]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.java
[54]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/braze/ui/contentcards/ContentCardsFragment.java
[55]: https://appboy.github.io/appboy-android-sdk/javadocs/com/appboy/models/cards/Card.html#isControl--
[56]: https://github.com/Appboy/appboy-android-sdk/blob/v11.0.0/android-sdk-ui/src/main/java/com/appboy/ui/contentcards/handlers/DefaultContentCardsViewBindingHandler.java
