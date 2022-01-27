---
nav_title: Personnalisation
article_title: Personnalisation des messages In-App pour Android/FireOS
page_order: 2
platform:
  - Android
  - Pare-feu
description: "Cet article de référence couvre les options de personnalisation de la messagerie dans l'application pour votre application Android."
channel:
  - messages intégrés à l'application
---

# Personnalisation {#in-app-message-customization}

Tous les types de messages dans l'application de Braze sont hautement personnalisables à travers les messages, les images, les icônes [Font Awesome][15] , cliquez sur actions, analytique, style modifiable, options d'affichage personnalisées et options de livraison personnalisées. Plusieurs options peuvent être configurées par message dans l'application à partir de [dans le tableau de bord]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/). Braze offre en outre de multiples niveaux de personnalisation avancée pour satisfaire une variété de cas d'utilisation et de besoins.

## Suppléments de la paire Key-value

Les objets de message intégrés peuvent transporter des paires clé-valeur comme `extras`. Ils sont spécifiés sur le tableau de bord sous « Paramètres avancés » lors de la création d'une campagne de message dans l'application. Celles-ci peuvent être utilisées pour envoyer des données en même temps qu'un message dans l'application pour une gestion ultérieure de l'application.

Appelez ce qui suit lorsque vous obtenez un objet de message dans l'application pour récupérer ses extras :

{% tabs %}
{% tab JAVA %}
```java
Carte<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
extras : Carte<String, String>
```
{% endtab %}
{% endtabs %}

Consultez le [KDoc][44] pour plus d'informations.

## Style personnalisé

Les éléments de Braze UI sont fournis avec un look et une sensation par défaut qui correspond aux directives de l'interface utilisateur standard d'Android et fournit une expérience transparente. Vous pouvez voir ces styles par défaut dans le fichier [`styles.xml`][6] du Braze SDK.

```xml
  <style name="Braze"/>
  <style name="Braze.InAppMessage"/>
  <style name="Braze.InAppMessage.Header">
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:padding">0.0dp</item>
    <item name="android:background">@android:color/transparent</item>
    <item name="android:textColor">@color/com_braze_inappmessage_header_text</item>
    <item name="android:textSize">20.0sp</item>
    <item name="android:lineSpacingMultiplier">1.3</item>
    <item name="android:gravity">center</item>
    <item name="android:textStyle">bold</item>
    <item name="android:layout_centerHorizontal">true</item>
  </style>
```

Si vous préférez, vous pouvez remplacer ces styles pour créer un look et une sensation qui convient mieux à votre application.

Pour remplacer un style, copiez-le dans son intégralité dans le fichier `styles.xml` de votre projet et apportez des modifications. Le style entier doit être copié dans votre fichier local `styles.xml` pour que tous les attributs soient correctement définis. Veuillez noter que ces styles personnalisés sont pour les modifications apportées aux éléments de l'interface utilisateur individuels, et non pour les modifications en gros des mises en page. Les changements au niveau de la mise en page doivent être traités avec des vues personnalisées.

### Utiliser un style personnalisé pour définir une police personnalisée

Braze permet de définir une police personnalisée en utilisant le guide de la famille de polices [][79]. Pour l'utiliser, remplacez le style pour le texte du message, les en-têtes, et/ou le texte du bouton et utilisez l'attribut `fontFamily` pour demander à Braze d'utiliser votre famille de polices personnalisée.

Par exemple, pour mettre à jour la police sur le texte du bouton de votre message dans l'application, remplacez le style `Braze.InAppMessage.Button` et référencez votre famille de polices personnalisées. La valeur de l'attribut doit pointer vers une famille de polices dans votre répertoire `res/font`.

Voici un exemple tronqué avec une famille de polices personnalisées, `my_custom_font_family`, référencé sur la dernière ligne:

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

En dehors du style `Braze.InAppMessage.Button` pour le texte du bouton, le style pour le texte du message est `Braze. nAppMessage.Message` et le style des en-têtes de message est `Braze.InAppMessage.Header`. Si vous voulez utiliser votre famille de police personnalisée pour tout le texte de message dans l'application, vous pouvez définir votre famille de polices sur le `Braze. style nAppMessage` , qui est le style parent pour tous les messages dans l'application.

{% alert important %}
Comme pour les autres styles personnalisés, le style entier doit être copié dans vos styles `locaux. ml` fichier pour que tous les attributs soient correctement définis.
{% endalert %}

## Paramétrage des écouteurs personnalisés

Avant de personnaliser les messages dans l'application avec des auditeurs personnalisés, il est important de comprendre le [`BrazeInAppMessageManager`][34], qui gère la majorité de la gestion des messages dans l'application. Comme décrit dans [Étape 1][5], il doit être enregistré pour que les messages dans l'application fonctionnent correctement.

`BrazeInAppMessageManager` gère l'affichage des messages dans l'application sur Android.  Il contient des instances de classes d'aide qui l'aident à gérer le cycle de vie et l'affichage des messages dans l'application. Toutes ces classes ont des implémentations standards et la définition de classes personnalisées est complètement optionnelle. Cependant, cela peut ajouter un autre niveau de contrôle sur l'affichage et le comportement des messages dans l'application.  Ces classes personnalisables incluent :

- [`IInAppMessageManagerListener`][21] - Implémenter [la gestion personnalisée de l'affichage et du comportement des messages dans l'application](#setting-a-custom-manager-listener).
- [`IInAppMessageViewFactory`][42] - Implémenter pour [construire des vues de messages personnalisés dans l'application](#setting-a-custom-view-factory).
- [`IInAppMessageAnimationFactory`][20] - Implémenter pour [définir des animations de messages personnalisés dans l'application](#setting-a-custom-animation-factory).
- [`IHtmlInAppMessageActionListener`][86] - Implémenter à [gérer l'affichage et le comportement des messages HTML dans l'application](#setting-a-custom-html-in-app-message-action-listener).
- [`IInAppMessageViewWrapperFactory`][88] - Implémenter à [gérer sur mesure l'interaction hiérarchique de la vue des messages dans l'application](#setting-a-custom-view-wrapper-factory).

### Écouteur de gestionnaire personnalisé

Le `BrazeInAppMessageManager` gère automatiquement l'affichage et le cycle de vie des messages dans l'application.  Si vous avez besoin de plus de contrôle sur le cycle de vie d'un message, définir un gestionnaire d'écoute personnalisé vous permettra de recevoir l'objet de message dans l'application à différents points du cycle de vie des messages dans l'application, vous permettant de gérer votre affichage vous-même, d'effectuer un traitement supplémentaire, de réagir au comportement de l'utilisateur, de traiter les [Extras][14]de l'objet , et bien plus encore.

#### Étape 1 : Implémenter un gestionnaire de messages dans l'application

Créer une classe qui implémente [`IInAppMessageManagerListener`][21].

Les fonctions de rappel dans votre `IInAppMessageManagerListener` seront appelées à différents points du cycle de vie des messages dans l'application.

Par exemple, si vous définissez un gestionnaire d'écoute personnalisé quand un message dans l'application est reçu de Braze, la méthode `beforeInAppMessageDisplayed()` sera appelée. Si votre implémentation de cette méthode retourne [`InAppMessageOperation. ISCARD`][83], qui signale à Braze que le message dans l'application sera géré par l'application hôte et ne devrait pas être affiché par Braze. Si `InAppMessageOperation.DISPLAY_NOW` est retourné, Braze tentera d'afficher le message dans l'application. Cette méthode doit être utilisée si vous choisissez d'afficher le message dans l'application d'une manière personnalisée.

`IInAppMessageManagerListener` inclut également des méthodes déléguées pour les clics sur le message lui-même ou sur l'un des boutons.  Un cas d'utilisation courant consiste à intercepter un message lorsqu'un bouton ou un message est cliqué pour en faire un traitement.

#### Étape 2 : Brancher dans la vue du cycle de vie des messages dans l'application (facultatif)

L'interface [`IInAppMessageManagerListener`][21] possède des méthodes d'affichage de messages dans l'application qui sont appelées à des points distincts du cycle de vie de la vue des messages dans l'application. Ces méthodes sont appelées dans l'ordre suivant :

- [beforeInAppMessageViewOpened][92] - Appelé juste avant que le message dans l'application ne soit ajouté à la vue Activity. Le message dans l'application n'est pas encore visible pour l'utilisateur en ce moment.
- [afterInAppMessageViewOpened][93] - Appelé juste après l'ajout du message dans l'application à la vue Activity. Le message dans l'application est maintenant visible pour l'utilisateur en ce moment.
- [beforeInAppMessageViewClosed][94] - Appelé juste avant que le message dans l'application ne soit retiré de la vue Activité. Le message dans l'application est toujours visible pour l'utilisateur en ce moment.
- [afterInAppMessageViewClosed][95] - Appelé juste après la suppression du message dans l'application de la vue Activité. Le message dans l'application n'est plus visible pour l'utilisateur en ce moment.

Pour plus de contexte, le temps entre [afterInAppMessageViewOpened][93] et [beforeInAppMessageViewClosed][94] est quand la vue du message dans l'application est à l'écran, visible par l'utilisateur.

{% alert note %}
  Aucune mise en œuvre de ces méthodes n'est requise. Ils sont simplement fournis pour suivre/informer du cycle de vie de la vue des messages dans l'application. Il est acceptable de laisser ces implémentations de méthodes vides sur le plan fonctionnel.
{% endalert %}

#### Étape 3 : Instructer Braze à utiliser votre écouteur de gestionnaire de messages intégré

Une fois que votre `IInAppMessageManagerListener` est créé, appelez `BrazeInAppMessageManager.getInstance(). etCustomInAppMessageManagerListener()` de demander à `BrazeInAppMessageManager` d'utiliser votre propre `IInAppMessageManagerListener` au lieu de l'écouteur par défaut.

Nous vous recommandons de définir votre `IInAppMessageManagerListener` dans votre [`Application.onCreate()`][82] avant tout autre appel vers Braze. Cela permettra de s'assurer que l'écouteur personnalisé est défini avant tout message dans l'application.

##### In-Profondeur : Modifier les messages dans l'application avant l'affichage

Lorsqu'un nouveau message dans l'application est reçu, et qu'un message dans l'application est déjà affiché, le nouveau message sera placé en haut de la pile et pourra être affiché ultérieurement.

Cependant, s'il n'y a pas de message affiché dans l'application, la méthode de délégué suivante dans `IInAppMessageManagerListener` sera appelée :

{% tabs %}
{% tab JAVA %}
```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessageBase) {
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessageBase: IInAppMessageMessage): InAppMessageOperation {
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

La valeur de retour `InAppMessageOperation()` peut être utilisée pour contrôler quand le message doit être affiché. L'utilisation suggérée de cette méthode serait de retarder les messages dans certaines parties de l'application en retournant `DISPLAY_LATER` lorsque les messages dans l'application seraient distrayant à l'expérience de l'utilisateur.

| `InAppMessageOperation` valeur de retour | Comportement                                                                                   |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `Afficher maintenant`                    | Le message sera affiché                                                                        |
| `AFFICHER_TITLE`                         | Le message sera retourné à la pile et sera affiché lors de la prochaine opportunité disponible |
| `DÉSACTIVER`                             | Le message sera supprimé                                                                       |
| `null`                                   | Le message sera ignoré. Cette méthode doit __PAS__ retourner `nulle`                           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Voir [`InAppMessageOperation.java`][45] pour plus de détails.

{% alert tip %}
Si vous choisissez de `DÉSACTIVER` le message dans l'application et de le remplacer par votre propre vue de message dans l'application, vous devrez vous connecter manuellement aux clics et aux impressions des messages de l'application.
{% endalert %}

Sur Android, cela se fait en appelant `logClick` et `logImpression` sur les messages dans l'application, et `logButtonClick` sur les messages immersifs dans l'application.

{% alert tip %}
Une fois qu'un message intégré a été placé sur la pile, vous pouvez demander qu'il soit récupéré et affiché à tout moment en appelant [`BrazeInAppMessageManager. etInstance().requestDisplayInAppMessage()`][98]. Appeler cette méthode demande à Braze d'afficher le prochain message disponible dans l'application depuis la pile.
{% endalert %}

#### Étape 4 : Personnalisation du comportement du thème sombre (facultatif) {#android-in-app-message-dark-theme-customization}

Dans la logique `IInAppMessageManagerListener` par défaut, dans `beforeInAppMessageDisplayed()`, les paramètres du système sont vérifiés et activent conditionnellement le style du thème sombre sur le message avec le code suivant :

{% tabs %}
{% tab JAVA %}
```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  if (inAppMessage instanceof IInAppMessageThemeable && ViewUtils. sDeviceInNightMode(BrazeInAppMessageManager.getInstance().getApplicationContext())) {
    ((IInAppMessageThemeable) inAppMessage).enableDarkTheme();
  }
  return InAppMessageOperation.DISPLAY_NOW;
 } }
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  if (inAppMessage est IInAppMessageThemeable && ViewUtils.isDeviceInNightMode(BrazeInAppMessageManager.getInstance().applicationContext!!)) {
    (inAppMessage as IInAppMessageThemeable).enableDarkTheme()
  }
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

Si vous souhaitez utiliser votre propre logique conditionnelle, alors vous pouvez appeler [`enableDarkTheme`][97] à n'importe quelle étape du processus de pré-affichage.

### Usine de vue personnalisée

La suite de types de messages intégrés à l'application Braze est suffisamment polyvalente pour couvrir la grande majorité des cas d'utilisation personnalisée. Cependant, si vous souhaitez définir complètement l'apparence visuelle de vos messages dans l'application au lieu d'utiliser un type par défaut, Braze rend cela possible en définissant une usine de vision personnalisée.

#### Étape 1 : Implémenter une usine de visualisation de message dans l'application

Créer une classe qui implémente [`IInAppMessageViewFactory`][87].

{% tabs %}
{% tab JAVA %}
```java
la classe publique CustomInAppMessageViewFactory implémente IInAppMessageViewFactory {
  @Override
  public View createInAppMessageView(Activité de l'activité) IInAppMessage inAppMessage) {
    // Utilise une vue personnalisée pour les diapositives, les modaux, et les messages complets dans l'application.
    // Les messages HTML dans l'application et tous les autres types utiliseront le commutateur de l'affichage des messages par défaut dans l'application
    (inAppMessage. etMessageType()) {
      case SLIDEUP:
      case MODAL:
      FULL:
        // Utilisez une vue personnalisée de votre choix
        return createMyCustomInAppMessageView();
      par défaut:
        // Utiliser les usines de messages par défaut dans l'application
        final IInAppMessageViewFactory defaultInAppMessageViewFactory = BrazeInAppMessageManager. etInstance().getDefaultInAppMessageViewFactory(inAppMessage);
        return defaultInAppMessageViewFactory.createInAppMessageView(activity, inAppMessage);
    }
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageViewFactory : IInAppMessageViewFactory {
  outrepasser le fun createInAppMessageView(activity: Activity, inAppMessage: IInAppMessage): View {
    // Utilise une vue personnalisée pour les diapositives, les modaux, et les messages complets dans l'application.
    // Les messages HTML dans l'application et tous les autres types utiliseront les usines d'affichage de message par défaut de Braze dans l'application
    quand (inAppMessage. essageType) {
      MessageType.SLIDEUP, MessageType.MODAL, MessageType. ULL ->
        // Utilisez une vue personnalisée de votre choix
        return createMyCustomInAppMessageView()
      else -> {
        // Utilisez les usines de messages par défaut dans l'application
        val defaultInAppMessageViewFactory = BrazeInAppMessageManager. etInstance().getDefaultInAppMessageViewFactory(inAppMessage)
        return defaultInAppMessageViewFactory!!. reateInAppMessageView(activity, inAppMessage)
      }
    }
  }
}
```
{% endtab %}
{% endtabs %}

#### Étape 2 : Instructer Braze à utiliser l'usine de visualisation de votre message dans l'application

Une fois que votre `IInAppMessageViewFactory` est créé, appelez `BrazeInAppMessageManager.getInstance(). etCustomInAppMessageViewFactory()` de demander à `BrazeInAppMessageManager` d'utiliser votre custom `IInAppMessageViewFactory` au lieu de l'usine de vue par défaut.

{% alert tip %}
Nous vous recommandons de définir votre `IInAppMessageViewFactory` dans votre `Application.onCreate()` avant tout autre appel à Braze. Cela permettra de s'assurer que l'usine de vue personnalisée est définie avant tout message dans l'application.
{% endalert %}

##### In-depth: Implémentation d'une interface de vue Braze

Braze's `slideup` dans la vue des messages de l'application implémente [`IInAppMessageView`][25].  Les vues de type message de `plein` et `modal` de Braze implémentent [`IInAppMessageImmersiveView`][24].  Implémenter une de ces classes permettra à Braze d'ajouter des écouteurs de clics à votre vue personnalisée le cas échéant.  Toutes les classes de vue Braze étendent la classe [View][18] d'Android.

Implémenter `IInAppMessageView` vous permet de définir une certaine portion de votre vue personnalisée comme cliquable. Implémentation de [`IInAppMessageImmersiveView`][24] vous permet de définir les vues des boutons de message et une vue du bouton de fermeture.

### Usine d'animation personnalisée

Les messages intégrés ont un comportement d'animation prédéfini. `Faire glisser` les messages de type </code> vers l'écran ; `les messages pleins` et `les messages modaux` s'estompent et sortent.  Si vous souhaitez définir des comportements d'animation personnalisés pour vos messages dans l'application, Braze le permet en définissant une usine d'animation personnalisée.

#### Étape 1 : Implémenter une usine d'animation de message dans l'application

Créer une classe qui implémente [`IInAppMessageAnimationFactory`][20]

{% tabs %}
{% tab JAVA %}
```java
La classe publique CustomInAppMessageAnimationFactory implémente IInAppMessageAnimationFactory {

  @Override
  public Animation getOpeningAnimation(IInAppMessage inAppMessage) {
    Animation = new AlphaAnimation(0, 1);
    animation. etInterpolator(new AccelerateInterpolator());
    animation. etDurée(2000L);
    animation de retour ;
  }

  @Override
  Animation publique getClosingAnimation(IInAppMessage inAppMessage) {
    Animation animation = new AlphaAnimation(1, 0);
    Animation. etInterpolator(new DecelerateInterpolator());
    animation.setDuration(2000L);
    animation de retour;
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageAnimationFactory : IInAppMessageAnimationFactory {
  override fun getOpeningAnimation(inAppMessage: IInAppMessage): Animation {
    val animation: Animation = AlphaAnimation(0, 1)
    animation. nterpolator = Animation AccelerateInterpolator()
    . uration = 2000L
    return animation
  }

  écraser getClosingAnimation(inAppMessage: IInAppMessage): Animation {
    animation val : Animation = AlphaAnimation(1, 0)
    animation. nterpolator = DecelerateInterpolator()
    animation.duration = 2000L
    animation de retour
  }
}
```
{% endtab %}
{% endtabs %}

#### Étape 2 : Instructer Braze à utiliser l'usine de visualisation de votre message dans l'application

Une fois que votre `IInAppMessageAnimationFactory` est créé, appelez `BrazeInAppMessageManager.getInstance(). etCustomInAppMessageAnimationFactory()` de demander à `BrazeInAppMessageManager` d'utiliser votre custom `IInAppMessageAnimationFactory` au lieu de l'usine d'animation par défaut.

Nous vous recommandons de définir votre `IInAppMessageAnimationFactory` dans votre [`Application.onCreate()`][82] avant tout autre appel à Braze. Cela permettra de s'assurer que l'usine d'animation personnalisée est définie avant tout message dans l'application.

### Écouteur de message HTML personnalisé dans l'application

Le SDK Braze possède une classe `DefaultHtmlInAppMessageActionListener` par défaut qui est utilisée si aucun listener personnalisé n'est défini et prend automatiquement les mesures appropriées. Si vous avez besoin de plus de contrôle sur la façon dont un utilisateur interagit avec différents boutons dans un message personnalisé HTML dans l'application, implémente une classe personnalisée `IHtmlInAppMessageActionListener`.

#### Étape 1 : Implémenter un écouteur d'action HTML personnalisé dans l'application

Créer une classe qui implémente [`IHtmlInAppMessageActionListener`][86].

Les fonctions de rappel dans votre `IHtmlInAppMessageActionListener` seront appelées chaque fois que l'utilisateur initiera l'une des actions suivantes dans le message HTML de l'application:
- Cliquez sur le bouton fermer.
- Cliquez sur le bouton Flux d'actualités.
- Tire un événement personnalisé.
- Cliquez sur une URL dans le message HTML dans l'application.

{% tabs %}
{% tab JAVA %}
```java
la classe publique CustomHtmlInAppMessageActionListener implémente IHtmlInAppMessageActionListener {
  Contexte final privé mContext;

  public CustomHtmlInAppMessageActionListener(Contexte contexte) {
    mContext = contexte;
  }

  @Override
  public vide onCloseClicked(IInAppMessage inAppMessage, URL de chaîne, bundle queryBundle) {
    Toast. akeText(mContext, "HTML In App Message closed", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance(). ideActuellementAffichagedans l'AppMessage(false);
  }

  @Override
  boolean public onCustomEventFired(IInAppMessage inAppMessage inAppMessage, URL de chaîne, bundle queryBundle) {
    Toast. akeText(mContext, "Événement personnalisé activé. Ignoring.", Toast.LENGTH_LONG).show();
    return true;
  }

  @Override
  public boolean onNewsfeedClicked(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Newsfeed button pressed. Ignorant.", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance(). ideCurrentlyDisplayingInAppMessage(false);
    retourne true;
  }

  @Override
  boolean public onOtherUrlAction(IInAppMessage inAppMessage, URL de chaîne, bundle queryBundle) {
    Toast. akeText(mContext, "URL personnalisée pressée: " + url + " . Ignorant", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
    return true;
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomHtmlInAppMessageActionListener(private val mContext: Context) : IHtmlInAppMessageActionListener {

    surcharge fun onCloseClicked(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle) {
        Toast. akeText(mContext, "HTML In App Message closed", Toast.LENGTH_LONG). how()
        BrazeInAppMessageManager.getInstance(). ideCurrentlyDisplayingInAppMessage(false)
    }

    surchargent fun onCustomEventFired(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast. akeText(mContext, "Événement personnalisé activé. Ignoring.", Toast.LENGTH_LONG).show()
        return true
    }

    override fun onNewsfeedClicked(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Bouton Newsfeed pressé. Ignorant.", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance(). ideCurrentlyDisplayingInAppMessage(false)
        return true
    }

    override fun onOtherUrlAction(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast. akeText(mContext, "URL personnalisée pressée: $url. Ignorant", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        retourner vrai
    }
}
```
{% endtab %}
{% endtabs %}

#### Étape 2 : Instructer Braze à utiliser votre écouteur d'action HTML dans l'application

Une fois que votre `IHtmlInAppMessageActionListener` est créé, appelez `BrazeInAppMessageManager.getInstance(). etCustomHtmlInAppMessageActionListener()` de demander à `BrazeInAppMessageManager` d'utiliser votre `IHtmlInAppMessageActionListener` personnalisé au lieu de l'écouteur d'action par défaut.

Nous vous recommandons de définir votre `IHtmlInAppMessageActionListener` dans votre [`Application.onCreate()`][82] avant tout autre appel vers Braze. Cela permettra de s'assurer que l'écouteur d'action personnalisé est défini avant tout message dans l'application.

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(new CustomHtmlInAppMessageActionListener(context));
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(CustomHtmlInAppMessageActionListener(context))
```
{% endtab %}
{% endtabs %}

### Usine de wrapper de vue personnalisée

Le `BrazeInAppMessageManager` gère automatiquement le placement du modèle de message dans l'application dans la hiérarchie de vue d'activité existante par défaut en utilisant [`DefaultInAppMessageViewWrapper`][89]. If you need to customize how in-app messages are placed into the view hierarchy, you should use a custom [`IInAppMessageViewWrapperFactory`][88].

#### Étape 1 : Implémenter une usine de gestion de la vue de message dans l'application

Créez une classe qui implémente [`IInAppMessageViewWrapperFactory`][88] et retourne un [IInAppMessageViewWrapper][90].

Cette usine est appelée immédiatement après la création de la vue de message dans l'application. La façon la plus simple d'implémenter un [IInAppMessageViewWrapper][90] personnalisé est simplement d'étendre la valeur par défaut [`DefaultInAppMessageViewWrapper`][89].

{% tabs %}
{% tab JAVA %}
```java
la classe publique CustomInAppMessageViewWrapper étend DefaultInAppMessageViewWrapper {
  public CustomInAppMessageViewWrapper(View inAppMessageView,
                                       IInAppMessage inAppMessage,
                                       IInAppMessageViewLifecycleListener inAppMessageViewLifecycleListener,
                                       BrazeConfigurationProvider brazeConfigurationProvider,
                                       Animation d'ouvertureAnimation,
                                       Animation fermetureAnimation, Voir clickableInAppMessageView) {
    super(inAppMessageView,
        inAppMessage,
        inAppMessageViewLifecycleListener,
        brazeConfigurationProvider,
        OuvertureAnimation,
        Animation de fermeture,
        clickableInAppMessageView);
  }

  @Override
  public void open(@Activité NonNull) {
    super. pen(activité);
    Toast.makeText(activity.getApplicationContext(), "Message ouvert dans l'application", Toast. ENGTH_SHORT).show();
  }

  @Override
  public void close() {
    super. lose();
    Toast.makeText(mInAppMessageView.getContext().getApplicationContext(), "Fermé dans l'application", Toast.LENGTH_SHORT).show();
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
classe CustomInAppMessageViewWrapper(inAppMessageView: Affichage,
                                    dans AppMessage: IInAppMessage,
                                    dans AppMessageViewLifecycleListener : IInAppMessageViewLifecycleListener,
                                    brazeConfigurationProvider: BrazeConfigurationProvider,
                                    Animation d'ouverture : Animation,
                                    closingAnimation : Animation, clickableInAppMessageView: View) : 
    DefaultInAppMessageViewWrapper(inAppMessageView, 
        inAppMessage, 
        dans AppMessageViewLifecycleListener, 
        brazeConfigurationProvider, 
        Animation d'ouverture, 
        animation de fermeture, 
        clickableInAppMessageView) {

  remplace open(activity: Activity) {
    super. pen(activité)
    Toast.makeText(activity.applicationContext, "Message ouvert dans l'application", Toast. ENGTH_SHORT).show()
  }

  surcharge fun close() {
    super. lose()
    Toast.makeText(mInAppMessageView.context.applicationContext, "Fermé dans l'application", Toast.LENGTH_SHORT).show()
  }
}
```
{% endtab %}
{% endtabs %}

#### Étape 2 : Instructez Braze à utiliser votre usine de wrapper de vue personnalisée

Une fois votre [IInAppMessageViewWrapper][90] créé, appelez [`BrazeInAppMessageManager.getInstance(). etCustomInAppMessageViewWrapperFactory()`][91] de demander à `BrazeInAppMessageManager` d'utiliser votre custom [`IInAppMessageViewWrapperFactory`][88] au lieu de l'usine de wrapper de vue par défaut.

Nous vous recommandons de définir votre [`IInAppMessageViewWrapperFactory`][88] dans votre [`Application.onCreate()`][82] avant tout autre appel vers Braze. Cela permettra de s'assurer que l'usine du wrapper de vue personnalisée est définie avant que tout message dans l'application ne soit affiché.

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapper());
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapper())
```
{% endtab %}
{% endtabs %}

## Réglage de l'orientation fixe

Pour définir une orientation fixe pour un message dans l'application, d'abord [définissez un écouteur de gestionnaire de messages personnalisé dans l'application][19]. Ensuite, appelez `setOrientation()` sur l'objet `IInAppMessage` dans la méthode déléguée `beforeInAppMessageDisplayed()`.

{% tabs %}
{% tab JAVA %}
```java
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Définit l'orientation vers le portrait
  inAppMessage.setOrientation(Orientation.PORTRAIT);
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  // Définit l'orientation au portrait
  inAppMessage.orientation = Orientation.PORTRAIT
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

Pour les appareils *tablettes* , les messages dans l'application apparaîtront dans le style de l'orientation préférée de l'utilisateur, quelle que soit l'orientation réelle de l'écran.

## Désactivation du bouton retour

Par défaut, le bouton de retour matériel rejette les messages In-App de Braze. Ce comportement peut être désactivé par message via [`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`][96].

Dans l'exemple suivant, `disable_back_button` est une paire de valeurs clés personnalisée définie sur le message In-App qui indique si le message doit permettre au bouton Retour de rejeter le message.

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(new DefaultInAppMessageManagerListener() {
  @Override
  public void beforeInAppMessageViewOpened(View inAppMessageView, IInAppMessage inAppMessage) {
    super. eforeInAppMessageViewOpened(inAppMessageView, inAppMessage);
    carte finale<String, String> extras = inAppMessage. etExtras();
    if (extras != null && extras. ontainsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance(). etBackButtonDismissesInAppMessageView(false);
    }
  }

  @Override
  public void afterInAppMessageViewClosed(IInAppMessage inAppMessage) {
    super. fterInAppMessageViewClosed(inAppMessage);
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true);
  }
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : DefaultInAppMessageManagerListener() {
  override fun beforeInAppMessageViewOpened(inAppMessageView: View, inAppMessage: IInAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage)
    val extras = inAppMessage.extras
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false)
    }
  }

  override fun afterInAppMessageViewClosed(inAppMessage: IInAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage)
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true)
  }
})
```
{% endtab %}
{% endtabs %}

{% alert note %}
Notez que si cette fonctionnalité est désactivée, le comportement par défaut du bouton de retour matériel de l'activité hôte sera utilisé à la place. Cela peut conduire au bouton retour au lieu de fermer l'application au lieu du message affiché dans l'application.
{% endalert %}

## Rejeter la fenêtre modale sur appui extérieur

La valeur par défaut et historique est `false`, ce qui signifie que les clics en dehors de la modale ne ferment pas la modale. Si vous définissez cette valeur à `true` , le message modal dans l'application sera rejeté lorsque l'utilisateur cliquera en dehors du message dans l'application. Ce comportement peut être activé en appelant :

```java
AppboyInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

## GIFs {#gifs-IAMs}

{% include archive/android/gifs.md channel="Messages dans l'application" %}

## Android dialogs

Braze ne prend pas en charge l'affichage des messages dans l'application dans [Dialogues Android][85] pour le moment.

## Demande de revue Google Play dans l'application

En raison des limitations et des restrictions définies par Google, les invites de revue Google Play personnalisées ne sont pas actuellement prises en charge par Braze. Alors que certains utilisateurs ont été en mesure d'intégrer ces invites avec succès, d'autres ont montré de faibles taux de réussite en raison des [quotas Google Play](https://developer.android.com/guide/playcore/in-app-review#quotas). Veuillez vous intégrer à vos propres risques. Vous pouvez trouver de la documentation sur les demandes d'évaluation Google Play dans l'application [ici](https://developer.android.com/guide/playcore/in-app-review).

## YouTube dans les messages HTML dans l'application

YouTube et d'autres contenus HTML5 peuvent être lus dans des messages HTML dans l'application. Cela nécessite que l'accélération matérielle soit activée dans l'activité où le message dans l'application est affiché, veuillez consulter le [guide des développeurs Android][84] pour plus de détails. L'accélération matérielle n'est disponible que sur Android API versions 11 et supérieures.

Ce qui suit est un exemple de vidéo YouTube intégrée dans un extrait HTML :

```html
<body>
    <div class="box">
        <div class="relativeTopRight">
            <a href="appboy://close">X</a>
        </div>
        <iframe width="60%" height="50%" src="https://www.youtube.com/embed/_x45EB3BWqI">
        </iframe>
    </div>
</body>
```

[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/#step-1-braze-in-app-message-manager-registration
[6]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml
[14]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/key-value_pairs/
[15]: http://fortawesome.github.io/Font-Awesome/
[18]: http://developer.android.com/reference/android/view/View.html
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#setting-custom-listeners
[20]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.inappmessage/-i-in-app-message-animation-factory/index.html
[21]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html
[24]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html
[25]: https://github.com/Appboy/appboy-android-sdk/blob/master/android-sdk-ui/src/main/java/com/appboy/ui/inappmessage/IInAppMessageView.java
[34]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html
[42]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.inappmessage/-i-in-app-message-view-factory/index.html
[44]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/get-extras.html
[45]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html
[79]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[79]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization
[82]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[83]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html#DISCARD
[84]: https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling
[85]: https://developer.android.com/guide/topics/ui/dialogs.html
[86]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html
[88]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html
[89]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html
[90]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy.ui.inappmessage/-i-in-app-message-view-wrapper/index.html
[91]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html
[92]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html#beforeInAppMessageViewOpened-android.view.View-com.braze.models.inappmessage.IInAppMessage-
[93]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html#afterInAppMessageViewOpened-android.view.View-com.braze.models.inappmessage.IInAppMessage-
[94]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html#beforeInAppMessageViewClosed-android.view.View-com.braze.models.inappmessage.IInAppMessage-
[95]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html#afterInAppMessageViewClosed-com.braze.models.inappmessage.IInAppMessage-
[96]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html
[97]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html
[98]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html#requestDisplayInAppMessage--
