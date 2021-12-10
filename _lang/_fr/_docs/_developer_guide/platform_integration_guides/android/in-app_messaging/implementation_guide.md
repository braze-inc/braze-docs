---
nav_title: Implémentation avancée (facultatif)
article_title: Guide d'implémentation de messages dans l'application pour Android (facultatif)
platform: Android
page_order: 6
description: "Ce guide de mise en œuvre avancé couvre les considérations de code de message dans l'application Android, trois cas d'utilisation construits par notre équipe et des extraits de code qui l'accompagnent."
channel:
  - messages intégrés à l'application
---

{% alert important %}
Vous cherchez le guide d'intégration des développeurs de messages dans l'application? Trouvez-le [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/).
{% endalert %}

# Guide d'implémentation de la messagerie intégrée

> Ce guide d'implémentation optionnel et avancé couvre les considérations de code de message dans l'application, trois cas d'utilisation personnalisés construits par notre équipe, et des extraits de code qui l'accompagnent. Visitez notre dépôt de démo de Braze [ici](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Veuillez noter que ce guide d'implémentation est centré sur une implémentation de Kotlin, mais des extraits de code Java sont fournis pour ceux qui sont intéressés.  Vous cherchez des implémentations HTML ? Jetez un coup d'oeil à notre [dépôt de modèles HTML](https://github.com/braze-inc/in-app-message-templates)!

## Considérations de code

Le guide suivant offre une intégration personnalisée optionnelle de développeurs à utiliser en plus des messages intégrés hors de la boîte de réception. Les composants de vue personnalisés et les usines sont inclus selon les besoins ci-dessous dans chaque cas d'utilisation, offrant des exemples pour étendre les fonctionnalités et personnaliser nativement l'apparence de vos messages dans l'application. Dans certains cas, il existe plusieurs façons d'obtenir des résultats similaires. La mise en œuvre optimale dépendra du cas d'utilisation spécifique.

### Usines personnalisées

Le SDK Braze permet aux développeurs de remplacer un certain nombre de valeurs par défaut par l'utilisation d'objets d'usine personnalisés. Ils peuvent être enregistrés avec le Braze SDK si nécessaire pour obtenir les résultats souhaités. Dans la plupart des cas, cependant, si vous décidez de remplacer une usine, vous devrez soit vous reporter explicitement à la valeur par défaut, soit réimplémenter la fonctionnalité fournie par défaut de Braze. Le snippet de code ci-dessous illustre comment fournir des implémentations personnalisées des interfaces `IInAppMessageViewFactory` et `IInAppMessageViewWrapperFactory`. Une fois que vous avez une bonne compréhension des concepts qui sous-tendent les usines par défaut de Brase, Consultez nos [cas d'utilisation](#sample-use-cases) ci-dessous pour commencer à implémenter une fonctionnalité de messagerie personnalisée dans l'application.

{% tabs %}
{% tab Kotlin %}
__Types de messages dans l'application__<br>

```kotlin
class BrazeDemoApplication : Application(){
 override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(AppboyLifecycleCallbackListener(true, true))
    AppboyInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
    AppboyInAppMessageManager.getInstance().setCustomInAppMessageViewFactory(CustomInAppMessageViewFactory())
  }

```
{% endtab %}
{% tab Java %}
__Types de messages dans l'application__<br>

```java
la classe publique BrazeDemoApplication étend l'application {
  @Override
  public void onCreate{
    super. nCreate();
    registerActivityLifecycleCallbacks(new AppboyLifecycleCallbackListener(true, true));
    AppboyInAppMessageManager. etInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
    AppboyInAppMessageManager.getInstance().setCustomInAppMessageViewFactory(new CustomInAppMessageViewFactory());
  }
}
```
{% endtab %}
{% endtabs %}

## Exemple de cas d'utilisation

Il y a trois exemples de cas d'utilisation des clients fournis. Chaque échantillon a des extraits de code et un aperçu de l'apparence et de l'utilisation des messages dans l'application dans le tableau de bord de Braze :
- [Message personnalisé dans l'application](#custom-slideup-in-app-message)
- [Message personnalisé dans l'application modale](#custom-modal-in-app-message)
- [Message In-App personnalisé](#custom-full-in-app-message)

### Message de glissement personnalisé dans l'application

Lors de la création de votre message glissant vers le haut dans l'application, il se peut que vous ne puissiez pas modifier le placement du message. Bien que cette option ne soit pas explicitement proposée en dehors de la liste, la modification de ce type est rendue possible en sous-classant la classe `DefaultInAppMessageViewWrapper` pour ajuster les paramètres de mise en page. Vous pouvez ajuster la position finale sur l'écran en écrasant la méthode `getLayoutParams` , renvoyant le `LayoutParams modifié` avec vos propres valeurs de positionnement personnalisées. Visitez le [CustomSlideUpInAppMessageViewWrapper](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/slideup/CustomSlideUpInAppMessageViewWrapper.kt) pour commencer.

#### Gestionnaire de vue personnalisée<br><br>

{% tabs %}
{% tab Kotlin %}
__Remplacer et Retourner les paramètres personnalisés de mise en page__<br> Dans la méthode `getLayoutParams` , vous pouvez utiliser la méthode de superclasse pour accéder à l'original `LayoutParameters` pour le message dans l'application. Ensuite, vous pouvez ajuster la position en ajoutant ou en soustrayant comme vous le souhaitez.

```kotlin
class CustomSlideUpInAppMessageViewWrapper(inAppMessageView: View?,
                                           inAppMessage: IInAppMessage?,
                                           inAppMessageViewLifecycleListener: IInAppMessageViewLifecycleListener?,
                                           configurationProvider: BrazeConfigurationProvider?,
                                           openingAnimation: Animation?,
                                           closingAnimation: Animation?,
                                           clickableInAppMessageView: View?) : DefaultInAppMessageViewWrapper(inAppMessageView,
    inAppMessage,
    inAppMessageViewLifecycleListener,
    configurationProvider,
    Animation d'ouverture,
    animation de fermeture,
    clickableInAppMessageView) {

    écraser getLayoutParams(inAppMessage: IInAppMessage? : Voir le groupe. ayoutParams {
        params val = super. etLayoutParams(inAppMessage) comme FrameLayout.LayoutParams
        paramètres. ottomMargin = paramètres. ottomMargin + 500 //déplacer la vue vers le haut de 500 pixels
        paramètres de retour
    }
}
```
{% endtab %}
{% tab Java %}
__Remplacer et Retourner les paramètres personnalisés de mise en page__<br> Dans la méthode `getLayoutParams` , vous pouvez utiliser la méthode de superclasse pour accéder à l'original `LayoutParameters` pour le message dans l'application. Ensuite, vous pouvez ajuster la position en ajoutant ou en soustrayant comme vous le souhaitez.

```java
classe CustomSlideUpInAppMessageViewWrapper étend DefaultInAppMessageViewWrapper {

    public CustomInAppMessageViewWrapper(View inAppMessageView,
                                           IInAppMessage inAppMessage,
                                           IInAppMessageViewLifecycleListener inAppMessageViewLifecycleListener,
                                           BrazeConfigurationProvider de configurationProvider,
                                           Animation d'ouvertureAnimation,
                                           Animation fermetureAnimation,
                                           Voir clickableInAppMessageView){
        super(inAppMessageView,
                dans AppMessage,
                dans AppMessageViewLifecycleListener,
                configurationProvider,
                animation d'ouverture,
                fermetureAnimation,
                clickableInAppMessageView)

    }

    @Override
    public ViewGroup. ayoutParams getLayoutParams(IInAppMessage inAppMessage){
        FrameLayout.LayoutParams params = (FrameLayout.LayoutParams)super. etLayoutParams(inAppMessage)
        params.bottomMargin = paramètres. ottomMargin + 500 //déplacer la vue vers le haut de 500 pixels
        paramètres de retour
    }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
__Fournissez une fabrique personnalisée pour retourner votre Wrapper__<br> Afin de vous assurer que le Braze SDK utilise votre emballage personnalisé, vous devez également fournir une implémentation personnalisée `IInAppMessageViewWrapperFactory` qui retourne votre wrapper personnalisé. Vous pouvez soit implémenter directement `IInAppMessageViewWrapperFactory` ou sous-classe `AppboyInAppMessageViewWrapperFactory` et ne remplacer que la méthode `createInAppMessageViewWrapper`:

```kotlin
class CustomInAppMessageViewWrapperFactory : AppboyInAppMessageViewWrapperFactory() {

    override fun createInAppMessageViewWrapper(
        inAppMessageView: View?
        dans AppMessage: IInAppMessage?
        inAppMessageViewLifecycleListener: IInAppMessageViewLifecycleListener?,
        configurationProvider: BrazeConfigurationProvider?
        openingAnimation : Animation ?,
        closingAnimation : Animation ?
        clickableInAppMessageView: Voir?
    ): IInAppMessageViewWrapper {
        return if (inAppMessage is InAppMessageSlideup) {
            CustomSlideUpInAppMessageViewWrapper( //return our custom view wrapper only for slideups
                inAppMessageView,
                dans AppMessage,
                dans AppMessageViewLifecycleListener,
                configurationProvider,
                Animation d'ouverture,
                fermetureAnimation,
                clickableInAppMessageView
            )
        } autre {
            super. reateInAppMessageViewWrapper( //reportez à l'implémentation par défaut pour tous les autres types IAM
                inAppMessageView,
                dans AppMessage,
                dans AppMessageViewLifecycleListener,
                configurationProvider,
                animation d'ouverture,
                fermetureAnimation,
                clickableInAppMessageView
            )
        }
    }
}
```
{% endtab %}
{% tab Java %}
__Fournissez une fabrique personnalisée pour retourner votre Wrapper__<br> Afin de vous assurer que le Braze SDK utilise votre emballage personnalisé, vous devez également fournir une implémentation personnalisée `IInAppMessageViewWrapperFactory` qui retourne votre wrapper personnalisé. Vous pouvez soit implémenter directement `IInAppMessageViewWrapperFactory` ou sous-classe `AppboyInAppMessageViewWrapperFactory` et ne remplacer que la méthode `createInAppMessageViewWrapper`:

```java
La classe CustomInAppMessageViewWrapperFactory étend AppboyInAppMessageViewWrapperFactory {
    @Override
    public IInAppMessageViewWrapper createInAppMessageViewWrapper(View inAppMessageView, 
        IInAppMessage inAppMessage, 
        IInAppMessageViewLifecycleListener inAppMessageViewLifecycleListener, 
        BrazeConfigurationProvider configurationProvider, 
        Animation ouverteAnimationAnimation 
        Animation fermetureAnimationAnimation, 
        Voir clickableInAppMessageView){
        if (inAppMessage instanceof InAppMessageSlideup){
            return new CustomSlideUpInAppMessageViewWrapper( //return our custom view wrapper only for slideups
                inAppMessageView,
                dans AppMessage,
                dans AppMessageViewLifecycleListener,
                configurationProvider,
                animation d'ouverture,
                animation de fermeture,
                clickableInAppMessageView);
        }else{
            return super. reateInAppMessageViewWrapper(//reportez à l'implémentation par défaut pour tous les autres types IAM
                inAppMessageView,
                dans AppMessage,
                dans AppMessageViewLifecycleListener,
                configurationProvider,
                ouvertureAnimation
                animation de fermeture,
                clickableInAppMessageView);
        }
    }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
__Enregistrez votre usine avec Braze__<br> Une fois que vous avez créé votre usine de wrapper personnalisée, enregistrez-le avec le Braze SDK via le `AppboyInAppMessageManager`:

```kotlin
AppboyInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
```
{% endtab %}
{% tab Java %}
__Enregistrez votre usine avec Braze__<br> Une fois que vous avez créé votre usine de wrapper personnalisée, enregistrez-le avec le Braze SDK via le `AppboyInAppMessageManager`:

```java
AppboyInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
```
{% endtab %}
{% endtabs %}

### Message modal personnalisé dans l'application

Un `AppboyInAppMessageModalView` peut être sous-classé pour tirer parti d'un `Spinner` offrant des moyens engageants de collecter des attributs utilisateur précieux. L'exemple ci-dessous montre comment vous pouvez utiliser le Contenu Connecté pour capturer des attributs personnalisés à partir d'une liste dynamique d'éléments. Visitez le [TeamPickerView](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/modal/TeamPickerView.kt) pour commencer.

{% tabs %}
{% tab Kotlin %}
__En utilisant `view_type` pour le comportement d'affichage de l'IU__<br> L'objet `IInAppMessage` a un dictionnaire `extras` que nous pouvons demander pour trouver la clé `view_type` (le cas échéant) et afficher le bon type de vue. Il est important de noter que les messages dans l'application sont configurés par message, de sorte que les vues modales personnalisées et hors de la boîte peuvent fonctionner harmonieusement.

```kotlin
override fun createInAppMessageView(activity: Activity, inAppMessage: IInAppMessage): Voir {
  return when {
      inAppMessage. xtras?. et("view_type") == "picker" -> {
          getCustomPickerView(activité, inAppMessage)
      }
      //...
      else -> {
          //Défer par défaut
          AppboyInAppMessageManager
              .getInstance()
              .getDefaultInAppMessageViewFactory(inAppMessage).createInAppMessageView(activity, inAppMessage)
      }
  }
 } }
```
{% endtab %}
{% tab Java %}
__En utilisant `view_type` pour le comportement d'affichage de l'IU__<br> L'objet `IInAppMessage` a un dictionnaire `extras` que nous pouvons demander pour trouver la clé `view_type` (le cas échéant) et afficher le bon type de vue. Il est important de noter que les messages dans l'application sont configurés par message, de sorte que les vues modales personnalisées et hors de la boîte peuvent fonctionner harmonieusement.

```java
@Override
public View createInAppMessageView(Activité d’activité, IInAppMessage inAppMessage) {
    if("picker".equals(inAppMessage.getExtras(). et("view_type")){
        return getCustomPickerView(activity, inAppMessage);
    } else {
        //Defer à la valeur par défaut
        AppboyInAppMessageManager
          . etInstance()
          .getDefaultInAppMessageViewFactory(inAppMessage)
          . reateInAppMessageView(activité, inAppMessage);
    }
}
```
{% endtab %}
{% endtabs %}

__Remplacer et fournir une vue personnalisée__<br> fournit une mise en page qui imite le message standard modal dans l'application. mais fournissez votre vue en tant qu'elment racine, puis gonflez cette mise en page
```xml
<com.braze.advancedsamples.inapp.modal.TeamPickerView xmlns:android="http://schemas.android.com/apk/res/android"
                                                      xmlns:tools="http://schemas.android.com/tools"
                                                      android:layout_width="match_parent"
                                                      android:layout_height="match_parent"
                                                      android:padding="0.0dp"
                                                      android:id="@+id/team_picker_view">
    <!-- ... -->
    <Spinner android:layout_width="match_parent" android:layout_height="wrap_content"
                     android:id="@+id/team_spinner"/>
    <!-- ... -->                                                      
</com.braze.advancedsamples.inapp.modal.TeamPickerView>
```

{% tabs %}
{% tab Kotlin %}
__Infler et personnaliser la vue__<br> avant de recharger les composants `Spinner` , la variable de message `inAppMessage` est affichée sous la forme d'une _String_. Ce message doit être formaté comme un tableau d'éléments à afficher correctement. À titre d'exemple, cela peut être réalisé en utilisant `String.split(",")`.

```kotlin
private fun getCustomView(activity: Activity, inAppMessage: IInAppMessage): TeamPickerView {
        vue val = activity.layoutInflater.inflate(R.layout. eam_picker_dialog, null) en tant que TeamPickerView
        équipes val = inAppMessage.message. vue plit(",")
        . etTeams(équipes)
        vue retour
}
```
{% endtab %}
{% tab Java %}
__Infler et personnaliser la vue__<br> avant de recharger les composants `Spinner` , la variable de message `inAppMessage` est affichée sous la forme d'une _String_. Ce message doit être formaté comme un tableau d'éléments à afficher correctement. À titre d'exemple, cela peut être réalisé en utilisant `String.split(",")`.

```java
TeamPickerView privé getCustomView(Activité d’activité, IInAppMessage inAppMessage) {
        TeamPickerView view = (TeamPickerView) activity.getLayoutInflater().inflate(R.layout. eam_picker_dialog, null);
        String[] équipes = inAppMessage.getMessage(). vue plit(",");
        . etTeams(équipes);
        vue retour
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
__Assigner un attribut personnalisé__<br> En utilisant la sous-classe de vue, après que l'utilisateur ait appuyé sur soumettre, passer l'attribut avec sa valeur sélectionnée correspondante à Braze et rejeter le message dans l'application en appelant `messageClickableView. erformClick()`.

```kotlin
    outrepasser le fun onClick(v: Voir?) {
        val selectedTeam = spinner.selectedItem as String;
        Appboy.getInstance(ctx).getCurrentUser<AppboyUser>()?.setCustomUserAttribute("FavoriteTeam", selectedTeam)
        messageClickableView.performClick()
}
```
{% endtab %}
{% tab Java %}
__Assigner un attribut personnalisé__<br> En utilisant la sous-classe de vue, après que l'utilisateur ait appuyé sur soumettre, passer l'attribut avec sa valeur sélectionnée correspondante à Braze et rejeter le message dans l'application en appelant `messageClickableView. erformClick()`.

```java
    @Override
    public void onClick(View v) {
        String selectedTeam = (String)spinner.selectedItem ;
        Appboy.getInstance(ctx).getCurrentUser().setCustomUserAttribute("FavoriteTeam", selectedTeam)
        messageClickableView.performClick()
}
```
{% endtab %}
{% endtabs %}

### Message complet dans l'application personnalisé
Implémenter un message immersif (plein écran) entièrement personnalisé dans l'application implique une approche similaire décrite ci-dessus pour implémenter un message modal personnalisé dans l'application. Dans ce cas, cependant, il suffit d'étendre `AppboyInAppMessageFullView` et de personnaliser au besoin. Rappelez-vous que la vue sera affichée sur l'interface utilisateur de l'application, et les vues dans Android par défaut sont transparentes. Cela signifie que vous devrez définir un arrière-plan de sorte que le message dans l'application masque le contenu derrière lui. En étendant `AppboyInAppMessageFullView`, le Braze SDK gérera les événements tactiles sur la vue et prendra les mesures appropriées. Comme dans l'exemple de la modalité, vous pouvez remplacer ce comportement par certains contrôles (comme `Switch` contrôles) pour recueillir les commentaires de l'utilisateur.

{% tabs %}
{% tab Kotlin %}
__En utilisant `view_type` pour le comportement d'affichage de l'interface utilisateur__<br> Nous allons ajouter un autre `view_type` supplémentaire pour notre nouvelle personnalisation immersive. Revisite de la méthode `createInAppMessageView` , ajoutez une option pour l'interface utilisateur "switches":

```kotlin
outrepasser le fun createInAppMessageView(activité: Activité, inAppMessage: IInAppMessage): Voir {
    return when {
        inAppMessage. xtras?. et("view_type") == "picker" -> {
            getCustomPickerView(activité, inAppMessage)
        }
        inAppMessage. xtras?. et("view_type") == "switches" -> {
            getCustomImmersiveView(activité, inAppMessage) // new customization
        }
        else -> {
            //Defer to default
            AppboyInAppMessageManager
                . etInstance()
                .getDefaultInAppMessageViewFactory(inAppMessage). reateInAppMessageView(activité, inAppMessage)
        }
    }
}
```
{% endtab %}
{% tab Java %}
__En utilisant `view_type` pour le comportement d'affichage de l'interface utilisateur__<br> Nous allons ajouter un autre `view_type` supplémentaire pour notre nouvelle personnalisation immersive. Revisite de la méthode `createInAppMessageView` , ajoutez une option pour l'interface utilisateur "switches":

```java
@Override
public View createInAppMessageView(Activité d’activité, IInAppMessage inAppMessage) {
    if("picker".equals(inAppMessage.getExtras(). et("view_type")){
        return getCustomPickerView(activity, inAppMessage);
    } else if ("switches".equals(inAppMessage.getExtras(). et("view_type"))) {
        return getCustomImmersiveView(activity, inAppMessage); // nouvelle personnalisation
    } else {
        //Déposer par défaut
        AppboyInAppMessageManager
          . etInstance()
          .getDefaultInAppMessageViewFactory(inAppMessage)
          . reateInAppMessageView(activité, inAppMessage);
    }
}
```
{% endtab %}
{% endtabs %}

__Remplacer et fournir une vue personnalisée__<br> fournit une mise en page qui imite le message standard modal dans l'application. mais fournissez votre vue en tant qu'elment racine, puis gonflez cette mise en page
```xml
<?xml version="1.0" encoding="utf-8"?>
<com.braze.advancedsamples.immersive.CustomImmersiveInAppMessage
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
        android:layout_height="wrap_content">
    <!-- donner à la disposition du parent une couleur de fond blanche masquera l'application derrière l'IAM. Vous pouvez également le faire dans votre vue personnalisée -->
    <LinearLayout android:background="@color/white" android:layout_width="match_parent" android:layout_height="match_parent" android:gravity="center"> 
        <! - ... -->
        <androidx.recyclerview.widget.RecyclerView android:layout_width="match_parent"
                                                       android:layout_height="wrap_content"
                                                       android:id="@+id/option_list"/>
        <! - . . ->
    </LinearLayout>
</com.braze.advancedsamples.immersive.CustomImmersiveInAppMessage>
```

{% tabs %}
{% tab Kotlin %}
__Infler et personnaliser la vue__<br> Avant de définir les options du composant `RecyclerView` , la variable de message `inAppMessage` est affichée sous la forme d'une _String_. Ce message doit être formaté comme un tableau d'éléments à afficher correctement. À titre d'exemple, cela peut être réalisé en utilisant `String.split(",")`. Les `titres` et `sous-titres` sont également extraits du lot `extras`.

```kotlin
private fun getCustomImmersiveView(activité: Activité, inAppMessage: IInAppMessage): CustomImmersiveInAppMessage{
    vue val = activité. ayoutInflater.inflate(R.layout.full_screen_iam, null) comme CustomImmersiveInAppMessage
    options val = inAppMessage. essage.split(",")
    view.setOptions(options)
    inAppMessage.extras?.get("title").let { view. etTitle(it) }
    inAppMessage.extras?.get("sous-title").let {view.setSubtitle(it) }
    return view
}
```
{% endtab %}
{% tab Java %}
__Infler et personnaliser la vue__<br> Avant de définir les options du composant `RecyclerView` , la variable de message `inAppMessage` est affichée sous la forme d'une _String_. Ce message doit être formaté comme un tableau d'éléments à afficher correctement. À titre d'exemple, cela peut être réalisé en utilisant `String.split(",")`. Les `titres` et `sous-titres` sont également extraits du lot `extras`.

```java
private CustomImmersiveInAppMessage getCustomImmersiveView(Activité d’activité, IInAppMessage inAppMessage) {
    CustomImmersiveInAppMessage view = (CustomImmersiveInAppMessage) activité. ayoutInflater.inflate(R.layout.full_screen_iam, null);
    String[] options = inAppMessage.message. plit(",");
    view.setOptions(options);
    String title = inAppMessage.getExtras().get("title");
    vue. etTitle(titre);
    Sous-titre de chaîne = inAppMessage.getExtras(). et("sous-titre"); 
    view.setSubtitle(sous-titre);
    vue retour ;
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
__Assigner un attribut personnalisé__<br> en utilisant la sous-classe de vue, après qu'un utilisateur bascule l'un des commutateurs, passe l'attribut associé et le statut bascule vers Braze.

```kotlin
fun logClick(value:String, checked:Boolean){
    Appboy.getInstance(ctx).logCustomEvent("SwitchChanged", BrazeProperties())
}

inner class OptionViewHolder(item: View): RecyclerView. iewHolder(item), View.OnClickListener{

    valeur var : String = ""

    override fun onClick(p0: View?) {
        if (p0 est Switch){
            val vérifié = p0. sChecked
            p0.isChecked = !p0. sChecked
            logClick(valeur, coché)
        }
    }
}
surcharger fun onCreateViewHolder(parent: ViewGroup, viewType: Int): OptionViewHolder {
    return OptionViewHolder(mInflater. nflate(R.layout.switch_cell, null))
}

surcharger fun onBindViewHolder(holder: OptionViewHolder, position: Int) {
    holder. temView.findViewById<TextView>(R.id.label).text = options[position]
    holder.value = options[position]
}
```
{% endtab %}
{% tab Java %}
__Assigner un attribut personnalisé__<br> en utilisant la sous-classe de vue, après qu'un utilisateur bascule l'un des commutateurs, passe l'attribut associé et le statut bascule vers Braze.

```java
private void logClick(String value, boolean checked){
    Appboy.getInstance(ctx).logCustomEvent("SwitchChanged", new BrazeProperties());
}

private class OptionViewHolder extends RecyclerView.ViewHolder, implémente View. nClickListener{

    valeur privée de chaîne = "";

    public OptionViewHolder(Voir l'élément){
        super(élément);
    }


    @Override
    null public onClick(Voir la vue) {
        if (voir le commutateur d'instanceof de l'interrupteur){
            Switch switchView = (Switch) view;
            booléen vérifié = switchView. sChecked;
            switchView.isChecked = !switchView. sChecked;
            logClick(valeur, vérifié)
        }
    }
}

@Override
public OptionViewHolder onCreateViewHolder(ViewGroup parent, Int viewType) {
    return new OptionViewHolder(mInflater. nflate(R.layout.switch_cell, null));
}

@Override
public void onBindViewHolder(OptionViewHolder holder, Int position) {
    ((TextView)holder. etItemView().findViewById(R.id.label)).setText(options.get(position));
    holder.value = options.get(position);
}
```
{% endtab %}
{% endtabs %}

#### Interception du message dans l'application
!\[Touches\]\[1\]{: style="float:right;max-width:30%;margin-left:10px;border:0"} Intercepter les touches de message dans l'application est crucial pour que les boutons de message personnalisés fonctionnent correctement. Par défaut, toutes les vues de messages dans l'application ajoutent `auditeur en clic` au message, afin que les utilisateurs puissent rejeter les messages sans boutons. Lorsque vous ajoutez des contrôles personnalisés qui devraient répondre à la saisie de l'utilisateur (comme des boutons personnalisés), vous pouvez enregistrer un écouteur `onClick` avec la vue normale. Toute touche en dehors des contrôles personnalisés rejettera le message dans l'application, comme d'habitude, lorsque les touches reçues par les contrôles personnalisés invoqueront votre écouteur `onClick`.
[1]: {% image_buster /assets/img/iam_implementation_guide_android.png %}
