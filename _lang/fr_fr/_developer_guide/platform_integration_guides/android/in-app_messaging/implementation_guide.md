---
nav_title: Guide d’implémentation avancée (facultatif)
article_title: Guide d’implémentation des messages in-app pour Android (facultatif)
platform: Android
page_order: 6
description: "Ce guide d’implémentation avancé couvre les considérations du code relatives messages in-app pour Android et FireOS, trois cas d’usage créés par notre équipe et les extraits de code qui vont avec."
channel:
  - in-app messages
---
<br>
{% alert important %}
Vous recherchez le guide d’intégration de base du développeur de messages in-app ? Trouvez-le [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/#in-app-messaging-integration).
{% endalert %}

# Guide d’implémentation avancé

> Ce Guide d’implémentation avancé optionnel couvre les considérations du code des messages in-app, trois cas d’utilisation personnalisés créés par notre équipe et les extraits de code qui l’accompagnent. Visitez notre dépôt de démonstration Braze [ici](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Notez que ce guide d’implémentation est centré autour d’une implémentation Kotlin, mais les extraits de code Java sont fournis aux personnes intéressées. Vous recherchez des implémentations HTML ? Jetez un coup d'œil à notre [référentiel de modèles HTML](https://github.com/braze-inc/in-app-message-templates)!

## Considérations du code

Le guide suivant propose une intégration de développeur personnalisée facultative à utiliser en plus des messages in-app par défaut. Les composants et les fabriques de vue personnalisée sont compris selon les besoins de chaque cas d’usage, en offrant des exemples pour étendre la fonctionnalité et personnaliser nativement l’apparence et la convivialité de vos messages in-app. Dans certains cas, il existe plusieurs manières d’obtenir des résultats similaires. L’implémentation optimale dépendra du cas d’usage spécifique.

### Fabriques personnalisées

Le SDK Braze permet aux développeurs de remplacer un certain nombre de valeurs par défaut par des objets de fabriques personnalisés. Ces derniers peuvent être enregistrés avec le SDK Braze, selon les besoins, pour obtenir les résultats souhaités. Dans la plupart des cas, cependant, si vous décidez de remplacer une fabrique, vous devrez soit différer explicitement la valeur par défaut, soit remettrez la fonctionnalité fournie par Braze par défaut. L’extrait de code suivant illustre comment fournir des implémentations personnalisées des interfaces `IInAppMessageViewFactory` et `IInAppMessageViewWrapperFactory`. Après avoir bien compris les concepts qui sous-tendent la modification de nos usines par défaut, consultez nos [cas d'utilisation](#sample-use-cases) pour commencer à mettre en œuvre des fonctionnalités d'envoi de messages in-app personnalisées.

{% tabs %}
{% tab Kotlin %}
**Types de messages in-app**<br>

```kotlin
class BrazeDemoApplication : Application(){
 override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(true, true))
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory(CustomInAppMessageViewFactory())
  }
}
```
{% endtab %}
{% tab Java %}
**Types de messages in-app**<br> 

```java
public class BrazeDemoApplication extends Application {
  @Override
  public void onCreate{
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(true, true));
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory(new CustomInAppMessageViewFactory());
  }
}
```
{% endtab %}
{% endtabs %}

## Cas d’utilisation

Vous trouverez ci-dessous trois cas d'utilisation. Chaque cas d'utilisation comporte des extraits de code et un aperçu de l'aspect et de l'utilisation des messages in-app dans le tableau de bord de Braze :
- [Message in-app slideup personnalisé](#custom-slideup-in-app-message)
- [Message in-app modal personnalisé](#custom-modal-in-app-message)
- [Message in-app complet personnalisé](#custom-full-in-app-message)

### Message in-app personnalisé à glissement vers le haut

Lors de la création de votre message in-app à glissement vers le haut, vous remarquerez peut-être que vous ne pouvez pas modifier l’emplacement du message à l’aide des méthodes par défaut. Une telle modification est rendue possible en sous-classant la classe `DefaultInAppMessageViewWrapper` pour ajuster les paramètres de mise en page. Vous pouvez ajuster la position finale à l’écran en écrasant la méthode `getLayoutParams` retournant le `LayoutParams` modifié par vos propres valeurs de positionnement personnalisées. Visitez le [CustomSlideUpInAppMessageViewWrapper](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/slideup/CustomSlideUpInAppMessageViewWrapper.kt) pour commencer.

#### Wrapper de vue personnalisé<br><br>

{% tabs %}
{% tab Kotlin %}
**Remplacer et renvoyer les paramètres de mise en page personnalisés**<br>
Dans la méthode `getLayoutParams` vous pouvez utiliser la méthode de superclasse pour accéder au `LayoutParameters` d’origine pour le message in-app. Ensuite, vous pouvez ajuster la position en ajoutant ou en soustrayant comme vous le souhaitez.

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
    openingAnimation,
    closingAnimation,
    clickableInAppMessageView) {

    override fun getLayoutParams(inAppMessage: IInAppMessage?): ViewGroup.LayoutParams {
        val params = super.getLayoutParams(inAppMessage) as FrameLayout.LayoutParams
        params.bottomMargin = params.bottomMargin + 500 //move the view up by 500 pixels
        return params
    }
}
```
{% endtab %}
{% tab Java %}
**Remplacer et renvoyer les paramètres de mise en page personnalisés**<br>
Dans la méthode `getLayoutParams` vous pouvez utiliser la méthode de superclasse pour accéder au `LayoutParameters` d’origine pour le message in-app. Ensuite, vous pouvez ajuster la position en ajoutant ou en soustrayant comme vous le souhaitez.

```java
class CustomSlideUpInAppMessageViewWrapper extends DefaultInAppMessageViewWrapper {

    public CustomInAppMessageViewWrapper(View inAppMessageView,
                                           IInAppMessage inAppMessage,
                                           IInAppMessageViewLifecycleListener inAppMessageViewLifecycleListener,
                                           BrazeConfigurationProvider configurationProvider,
                                           Animation openingAnimation,
                                           Animation closingAnimation,
                                           View clickableInAppMessageView){
        super(inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView)

    }
    
    @Override
    public ViewGroup.LayoutParams getLayoutParams(IInAppMessage inAppMessage){
        FrameLayout.LayoutParams params = (FrameLayout.LayoutParams)super.getLayoutParams(inAppMessage)
        params.bottomMargin = params.bottomMargin + 500 //move the view up by 500 pixels
        return params
    }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
**Fournissez une fabrique personnalisée pour renvoyer votre wrapper personnalisé**<br>
Pour que le SDK Braze puisse utiliser votre wrapper personnalisé, vous devez également fournir une implémentation `IInAppMessageViewWrapperFactory` personnalisée qui renvoie votre wrapper personnalisé. Vous pouvez soit implémenter `IInAppMessageViewWrapperFactory` directement ou sous-classer `BrazeInAppMessageViewWrapperFactory` et ne remplacer que la méthode `createInAppMessageViewWrapper` :

```kotlin
class CustomInAppMessageViewWrapperFactory : BrazeInAppMessageViewWrapperFactory() {

    override fun createInAppMessageViewWrapper(
        inAppMessageView: View?,
        inAppMessage: IInAppMessage?,
        inAppMessageViewLifecycleListener: IInAppMessageViewLifecycleListener?,
        configurationProvider: BrazeConfigurationProvider?,
        openingAnimation: Animation?,
        closingAnimation: Animation?,
        clickableInAppMessageView: View?
    ): IInAppMessageViewWrapper {
        return if (inAppMessage is InAppMessageSlideup) {
            CustomSlideUpInAppMessageViewWrapper( //return our custom view wrapper only for slideups
                inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView
            )
        } else {
            super.createInAppMessageViewWrapper( //defer to the default implementation for all other IAM types
                inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView
            )
        }
    }
}
```
{% endtab %}
{% tab Java %}
**Fournissez une fabrique personnalisée pour renvoyer votre wrapper personnalisé**<br>
Pour que le SDK Braze puisse utiliser votre wrapper personnalisé, vous devez fournir une implémentation `IInAppMessageViewWrapperFactory` personnalisée qui renvoie votre wrapper personnalisé. Vous pouvez soit implémenter `IInAppMessageViewWrapperFactory` directement ou sous-classer `BrazeInAppMessageViewWrapperFactory` et ne remplacer que la méthode `createInAppMessageViewWrapper` :

```java
class CustomInAppMessageViewWrapperFactory extends BrazeInAppMessageViewWrapperFactory {
    @Override
    public IInAppMessageViewWrapper createInAppMessageViewWrapper(View inAppMessageView, 
        IInAppMessage inAppMessage, 
        IInAppMessageViewLifecycleListener inAppMessageViewLifecycleListener, 
        BrazeConfigurationProvider configurationProvider, 
        Animation openingAnimation, 
        Animation closingAnimation, 
        View clickableInAppMessageView){
        if (inAppMessage instanceof InAppMessageSlideup){
            return new CustomSlideUpInAppMessageViewWrapper( //return our custom view wrapper only for slideups
                inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView);
        }else{
            return super.createInAppMessageViewWrapper(//defer to the default implementation for all other IAM types
                inAppMessageView,
                inAppMessage,
                inAppMessageViewLifecycleListener,
                configurationProvider,
                openingAnimation,
                closingAnimation,
                clickableInAppMessageView);
        }
    }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
**Enregistrez votre fabrique auprès de Braze**<br>
Une fois que vous avez créé votre fabrique de wrapper personnalisée, enregistrez-la avec le SDK Braze via le `BrazeInAppMessageManager` :

```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
```
{% endtab %}
{% tab Java %}
**Enregistrez votre fabrique auprès de Braze**<br>
Une fois que vous avez créé votre fabrique de wrapper personnalisée, enregistrez-la avec le SDK Braze via le `BrazeInAppMessageManager` :

```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
```
{% endtab %}
{% endtabs %}

### Message in-app modal personnalisé

Un `BrazeInAppMessageModalView` peut être sous-classé pour tirer parti d’un `Spinner` offrant des façons intéressantes de collecter de précieux attributs d’utilisateur. L’exemple suivant montre comment utiliser le contenu connecté pour capturer des attributs personnalisés à partir d’une liste dynamique d’éléments. Visitez le site [`TeamPickerView`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/modal/TeamPickerView.kt) pour commencer.

{% tabs %}
{% tab Kotlin %}
**Utilisation de `view_type` pour le comportement d'affichage de l'interface utilisateur**<br>
L’objet `IInAppMessage` possède un dictionnaire `extras` que nous pouvons interroger pour trouver la clé `view_type` (le cas échéant) et afficher le type de vue approprié. Il est important de noter que les messages in-app sont configurés par message, de sorte que les vues modales personnalisées et par défaut puissent fonctionner harmonieusement.

```kotlin
override fun createInAppMessageView(activity: Activity, inAppMessage: IInAppMessage): View {
  return when {
      inAppMessage.extras?.get("view_type") == "picker" -> {
          getCustomPickerView(activity, inAppMessage)
      }
      //...
      else -> {
          //Defer to default
          BrazeInAppMessageManager
              .getInstance()
              .getDefaultInAppMessageViewFactory(inAppMessage).createInAppMessageView(activity, inAppMessage)
      }
  }
}
```
{% endtab %}
{% tab Java %}
**Utilisation de `view_type` pour le comportement d'affichage de l'interface utilisateur**<br>
L’objet `IInAppMessage` possède un dictionnaire `extras` que nous pouvons interroger pour trouver la clé `view_type` (le cas échéant) et afficher le type de vue approprié. Il est important de noter que les messages in-app sont configurés par message, de sorte que les vues modales personnalisées et par défaut puissent fonctionner harmonieusement.

```java
@Override
public View createInAppMessageView(Activity activity, IInAppMessage inAppMessage) {
    if("picker".equals(inAppMessage.getExtras().get("view_type"))){
        return getCustomPickerView(activity, inAppMessage);
    } else {
        //Defer to default
        BrazeInAppMessageManager
          .getInstance()
          .getDefaultInAppMessageViewFactory(inAppMessage)
          .createInAppMessageView(activity, inAppMessage);
    }
}
```
{% endtab %}
{% endtabs %}

**Remplacer et fournir une vue personnalisée**<br>
Indiquez une mise en page qui reproduit le message in-app modal standard, mais indiquez votre vue en tant qu’élément racine, puis augmentez cette disposition 
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
**Augmenter et personnaliser la vue**<br>
Avant de recharger les composants `Spinner`, la variable de message `inAppMessage` sort en tant que chaîne de caractères. Ce message doit être formaté comme un ensemble d’éléments à afficher correctement. Par exemple, cela peut être effectué en utilisant `String.split(",")`.

```kotlin
private fun getCustomView(activity: Activity, inAppMessage: IInAppMessage): TeamPickerView {
        val view = activity.layoutInflater.inflate(R.layout.team_picker_dialog, null) as TeamPickerView
        val teams = inAppMessage.message.split(",")
        view.setTeams(teams)
        return view
    }
```
{% endtab %}
{% tab Java %}
**Augmenter et personnaliser la vue**<br>
Avant de recharger les composants de `Spinner`, la variable de message `inAppMessage` est éditée sous la forme d'une _chaîne de caractères_. Ce message doit être formaté comme un ensemble d’éléments à afficher correctement. Par exemple, cela peut être effectué en utilisant `String.split(",")`.

```java
private TeamPickerView getCustomView(Activity activity, IInAppMessage inAppMessage) {
        TeamPickerView view = (TeamPickerView) activity.getLayoutInflater().inflate(R.layout.team_picker_dialog, null);
        String[] teams = inAppMessage.getMessage().split(",");
        view.setTeams(teams);
        return view
    }
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
**Attribuer un attribut personnalisé**<br>
En utilisant la sous-classe de vue, après qu’un utilisateur appuie sur Envoyer, transmettez vers Braze l’attribut avec sa valeur sélectionnée correspondante et rejetez le message in-app en appelant `messageClickableView.performClick()`.

```kotlin
    override fun onClick(v: View?) {
        val selectedTeam = spinner.selectedItem as String
        messageClickableView.performClick()
        Braze.getInstance(ctx).getCurrentUser { brazeUser ->
            brazeUser?.setCustomUserAttribute("FavoriteTeam", selectedTeam)
        }
    }
```
{% endtab %}
{% tab Java %}
**Attribuer un attribut personnalisé**<br>
En utilisant la sous-classe de vue, après qu’un utilisateur appuie sur Envoyer, transmettez vers Braze l’attribut avec sa valeur sélectionnée correspondante et rejetez le message in-app en appelant `messageClickableView.performClick()`.

```java
    @Override
    public void onClick(View v) {
        String selectedTeam = (String) spinner.getSelectedItem();
        messageClickableView.performClick();
        Braze.getInstance(ctx).getCurrentUser(brazeUser -> {
            brazeUser.setCustomUserAttribute("FavoriteTeam", selectedTeam);
        });
    }
```
{% endtab %}
{% endtabs %}

### Message in-app complet personnalisé
La mise en œuvre d'un message in-app immersif (plein écran) entièrement personnalisé implique une approche similaire à celle décrite dans la section relative à la mise en œuvre d'un [message in-app modal personnalisé.](#custom-modal-in-app-message) Dans ce cas, il suffit toutefois d’étendre `BrazeInAppMessageFullView` et de personnaliser si nécessaire. Rappelez-vous que la vue va s’afficher sur l’IU de l’application et que les vues d’Android par défaut sont transparentes. Cela signifie que vous devrez définir un arrière-plan de sorte que le message in-app obscurcisse le contenu derrière-lui. En étendant `BrazeInAppMessageFullView`, le SDK Braze traitera les événements tactiles interceptés sur la vue et prendra l’action appropriée. Comme avec l’exemple modal, vous pouvez écraser ce comportement pour certains types de contrôles (comme les contrôles `Switch`) pour recueillir les commentaires de l’utilisateur.

{% tabs %}
{% tab Kotlin %}
**Utilisation de `view_type` pour le comportement d'affichage de l'interface utilisateur**<br>
Nous ajouterons une autre `view_type` pour notre nouvelle personnalisation immersive. Retournez sur la méthode `createInAppMessageView` et ajoutez une option pour les « bascules » de l’IU :

```kotlin
override fun createInAppMessageView(activity: Activity, inAppMessage: IInAppMessage): View {
    return when {
        inAppMessage.extras?.get("view_type") == "picker" -> {
            getCustomPickerView(activity, inAppMessage)
        }
        inAppMessage.extras?.get("view_type") == "switches" -> {
            getCustomImmersiveView(activity, inAppMessage) // new customization
        }
        else -> {
            //Defer to default
            BrazeInAppMessageManager
                .getInstance()
                .getDefaultInAppMessageViewFactory(inAppMessage).createInAppMessageView(activity, inAppMessage)
        }
    }
}
```
{% endtab %}
{% tab Java %}
**Utilisation de `view_type` pour le comportement d'affichage de l'interface utilisateur**<br>
Nous ajouterons une autre `view_type` pour notre nouvelle personnalisation immersive. Retournez sur la méthode `createInAppMessageView` et ajoutez une option pour les « bascules » de l’IU :

```java
@Override
public View createInAppMessageView(Activity activity, IInAppMessage inAppMessage) {
    if("picker".equals(inAppMessage.getExtras().get("view_type"))){
        return getCustomPickerView(activity, inAppMessage);
    } else if ("switches".equals(inAppMessage.getExtras().get("view_type"))) {
        return getCustomImmersiveView(activity, inAppMessage); // new customization
    } else {
        //Defer to default
        BrazeInAppMessageManager
          .getInstance()
          .getDefaultInAppMessageViewFactory(inAppMessage)
          .createInAppMessageView(activity, inAppMessage);
    }
}
```
{% endtab %}
{% endtabs %}

**Remplacer et fournir une vue personnalisée**<br>
Indiquez une mise en page qui reproduit le message in-app modal standard, mais indiquez votre vue en tant qu’élément racine, puis augmentez cette disposition 
```xml
<?xml version="1.0" encoding="utf-8"?>
<com.braze.advancedsamples.immersive.CustomImmersiveInAppMessage
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
        android:layout_height="wrap_content">
    <!-- giving the parent layout a white backround color will obscure the app behind the IAM. You could also do this within your custom view -->
    <LinearLayout android:background="@color/white" android:layout_width="match_parent" android:layout_height="match_parent" android:gravity="center"> 
        <!-- ... -->
        <androidx.recyclerview.widget.RecyclerView android:layout_width="match_parent"
                                                       android:layout_height="wrap_content"
                                                       android:id="@+id/option_list"/>
        <!-- ... -->
    </LinearLayout>
</com.braze.advancedsamples.immersive.CustomImmersiveInAppMessage>
```

{% tabs %}
{% tab Kotlin %}
**Augmenter et personnaliser la vue**<br>
Avant de définir les options du composant `RecyclerView`, la variable de message `inAppMessage` est envoyée sous forme de _chaîne de caractères_. Ce message doit être formaté comme un ensemble d’éléments à afficher correctement. Par exemple, cela peut être effectué en utilisant `String.split(",")`. Les `title` et `subtitle` sont également extraits de l’ensemble `extras`.

```kotlin
private fun getCustomImmersiveView(activity: Activity, inAppMessage: IInAppMessage): CustomImmersiveInAppMessage{
    val view = activity.layoutInflater.inflate(R.layout.full_screen_iam, null) as CustomImmersiveInAppMessage
    val options = inAppMessage.message.split(",")
    view.setOptions(options)
    inAppMessage.extras?.get("title").let { view.setTitle(it) }
    inAppMessage.extras?.get("subtitle").let {view.setSubtitle(it) }
    return view
}
```
{% endtab %}
{% tab Java %}
**Augmenter et personnaliser la vue**<br>
Avant de définir les options du composant `RecyclerView`, la variable de message `inAppMessage` est envoyée sous forme de _chaîne de caractères_. Ce message doit être formaté comme un ensemble d’éléments à afficher correctement. Par exemple, cela peut être effectué en utilisant `String.split(",")`. Les `title` et `subtitle` sont également extraits de l’ensemble `extras`.

```java
private CustomImmersiveInAppMessage getCustomImmersiveView(Activity activity, IInAppMessage inAppMessage) {
    CustomImmersiveInAppMessage view = (CustomImmersiveInAppMessage) activity.layoutInflater.inflate(R.layout.full_screen_iam, null);
    String[] options = inAppMessage.message.split(",");
    view.setOptions(options);
    String title = inAppMessage.getExtras().get("title");
    view.setTitle(title);
    String subtitle = inAppMessage.getExtras().get("subtitle"); 
    view.setSubtitle(subtitle);
    return view;
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab Kotlin %}
**Attribuer un attribut personnalisé**<br>
À l’aide de la sous-classe de vue, après qu’un utilisateur bascule un des commutateurs, transférez l’attribut associé et le statut de la bascule à Braze.

```kotlin
fun logClick(value:String, checked:Boolean){
    Braze.getInstance(ctx).logCustomEvent("SwitchChanged", BrazeProperties())
}

inner class OptionViewHolder(item: View): RecyclerView.ViewHolder(item), View.OnClickListener{

    var value: String = ""

    override fun onClick(p0: View?) {
        if (p0 is Switch){
            val checked = p0.isChecked
            p0.isChecked = !p0.isChecked
            logClick(value, checked)
        }
    }
}
override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): OptionViewHolder {
    return OptionViewHolder(mInflater.inflate(R.layout.switch_cell, null))
}

override fun onBindViewHolder(holder: OptionViewHolder, position: Int) {
    holder.itemView.findViewById<TextView>(R.id.label).text = options[position]
    holder.value = options[position]
}
```
{% endtab %}
{% tab Java %}
**Attribuer un attribut personnalisé**<br>
À l’aide de la sous-classe de vue, après qu’un utilisateur bascule un des commutateurs, transférez l’attribut associé et le statut de la bascule à Braze.

```java
private void logClick(String value, boolean checked){
    Braze.getInstance(ctx).logCustomEvent("SwitchChanged", new BrazeProperties());
}

private class OptionViewHolder extends RecyclerView.ViewHolder, implements View.OnClickListener{

    private String value = "";

    public OptionViewHolder(View item){
        super(item);
    }

   
    @Override
    public void onClick(View view) {
        if (view instanceof Switch){
            Switch switchView = (Switch) view;
            boolean checked = switchView.isChecked;
            switchView.isChecked = !switchView.isChecked;
            logClick(value, checked)
        }
    }
}

@Override
public OptionViewHolder onCreateViewHolder(ViewGroup parent, Int viewType) {
    return new OptionViewHolder(mInflater.inflate(R.layout.switch_cell, null));
}

@Override
public void onBindViewHolder(OptionViewHolder holder, Int position) {
    ((TextView)holder.getItemView().findViewById(R.id.label)).setText(options.get(position));
    holder.value = options.get(position);
}
```
{% endtab %}
{% endtabs %}

#### Interception des touches de message in-app
![Un appareil Android affichant des lignes de paramètres et de bascule. La vue personnalisée gère les boutons, et tout contact en dehors des boutons est traité par le message in-app et le fait disparaître.]({% image_buster /assets/img/iam_implementation_guide_android.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
L’interception des touchés de message in-app est essentielle pour que les boutons du message in-app personnalisé complet fonctionnent correctement. Par défaut, toutes les vues de messages in-app sont ajoutées en tant qu’écouteurs `onClick` sur le message, afin que les utilisateurs puissent ignorer les messages sans boutons. Lorsque vous ajoutez des contrôles personnalisés qui doivent répondre à une entrée par l’utilisateur (comme les boutons personnalisés), vous pouvez enregistrer un écouteur `onClick` avec la vue habituelle. Tout touché en dehors des commandes personnalisées rejettera le message in-app comme d’habitude, tandis que les touchés reçus par les contrôles personnalisés feront appel à votre écouteur `onClick`. 

