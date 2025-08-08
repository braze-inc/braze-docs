# Beispiele für die Umsetzung

> Dieser optionale, fortgeschrittene Implementierungsleitfaden enthält Hinweise zur Code-Anpassung von In-App-Nachricht, drei speziell von unserem Team entwickelte Anwendungsfälle und begleitende Code-Snippets. Besuchen Sie unser Braze Demo Repository [hier](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Beachten Sie, dass sich dieser Implementierungsleitfaden auf eine Kotlin-Implementierung konzentriert. Für Interessierte werden jedoch Java-Snippets bereitgestellt. Suchen Sie nach HTML-Implementierungen? Werfen Sie einen Blick auf unser [HTML-Template-Repository](https://github.com/braze-inc/in-app-message-templates)!

## Code-Überlegungen

Die folgende Anleitung bietet eine optionale angepasste Integration, die Sie zusätzlich zu standardmäßigen In-App-Nachrichten verwenden können. Zu jedem Anwendungsfall werden je nach Bedarf angepasste Ansichtskomponenten und Factories mitgeliefert, mit denen Sie die Funktionalität erweitern und das Aussehen Ihrer In-App-Nachrichten nativ anpassen können. In manchen Instanzen gibt es mehrere Möglichkeiten, ähnliche Ergebnisse zu erzielen. Die optimale Implementierung hängt von dem jeweiligen Anwendungsfall ab.

### Angepasste Factorys

Das Braze SDK erlaubt es Entwicklern, bestimmte Standardeinstellungen durch angepasste Factory-Objekte außer Kraft zu setzen. Diese können nach Bedarf mit dem Braze SDK registriert werden, um die gewünschten Ergebnisse zu erzielen. In den meisten Fällen müssen Sie jedoch entweder explizit den Standard aussetzen oder die vom Braze-Standard bereitgestellten Funktionen neu implementieren. Der folgende Code-Snippet veranschaulicht, wie Sie angepasste Implementierungen der Schnittstellen `IInAppMessageViewFactory` und `IInAppMessageViewWrapperFactory` bereitstellen können. Nachdem Sie ein solides Verständnis der Konzepte hinter dem Außerkraftsetzen unserer Standard-Factorys erworben haben, sehen Sie sich unsere [Anwendungsfälle](#sample-use-cases) an, um mit der Implementierung angepasster In-App-Nachrichten zu beginnen.

{% tabs %}
{% tab Kotlin %}
**Arten von In-App-Nachrichten**<br>

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
**Arten von In-App-Nachrichten**<br> 

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

## Anwendungsfälle

Im Folgenden finden Sie drei Anwendungsbeispiele. Jeder Anwendungsfall enthält Code-Snippets und einen Blick darauf, wie In-App-Nachrichten im Braze-Dashboard aussehen und verwendet werden können:
- [Beispiele für die Umsetzung](#implementation-examples)
  - [Code-Überlegungen](#code-considerations)
    - [Angepasste Factorys](#custom-factories)
  - [Anwendungsfälle](#use-cases)
    - [Benutzerdefinierte In-App-Nachricht zum Hochschieben](#custom-slide-up-in-app-message)
      - [Angepasster Wrapper für die Ansicht](#custom-view-wrapper)
    - [Benutzerdefinierte modale In-App-Nachricht](#custom-modal-in-app-message)
    - [Angepasste In-App-Nachricht des Typs "Full"](#custom-full-in-app-message)
      - [Touch-Events in der In-App-Nachricht abfangen](#intercepting-in-app-message-touches)

### Benutzerdefinierte In-App-Nachricht zum Hochschieben

Bei der Erstellung Ihrer Slide-up-Nachricht werden Sie feststellen, dass Sie die Platzierung der Nachricht mit den Standardmethoden nicht ändern können. Eine solche Änderung wird durch eine Unterklasse der Klasse `DefaultInAppMessageViewWrapper` ermöglicht, um die Layoutparameter anzupassen. Sie können die endgültige Position auf dem Bildschirm anpassen, indem Sie die Methode `getLayoutParams` überschreiben, die die geänderte `LayoutParams` mit Ihren eigenen angepassten Positionierungswerten zurückgibt. Besuchen Sie den [CustomSlideUpInAppMessageViewWrapper](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/slideup/CustomSlideUpInAppMessageViewWrapper.kt), um loszulegen.

#### Angepasster Wrapper für die Ansicht<br><br>

{% tabs %}
{% tab Kotlin %}
**Angepasste Layout-Parameter außer Kraft setzen und zurückgeben**<br>
Innerhalb der Methode `getLayoutParams` können Sie die Superklassenmethode verwenden, um auf die ursprüngliche `LayoutParameters` für die In-App-Nachricht zuzugreifen. Dann können Sie die Position anpassen, indem Sie nach Belieben addieren oder subtrahieren.

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
**Angepasste Layout-Parameter außer Kraft setzen und zurückgeben**<br>
Innerhalb der Methode `getLayoutParams` können Sie die Superklassenmethode verwenden, um auf die ursprüngliche `LayoutParameters` für die In-App-Nachricht zuzugreifen. Dann können Sie die Position anpassen, indem Sie nach Belieben addieren oder subtrahieren.

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
**Angepasste Factory für angepassten Wrapper bereitstellen**<br>
Damit das Braze SDK Ihren angepassten Wrapper verwenden kann, müssen Sie auch eine angepasste `IInAppMessageViewWrapperFactory` Implementierung bereitstellen, die Ihren angepassten Wrapper zurückgibt. Sie können entweder `IInAppMessageViewWrapperFactory` direkt implementieren oder `BrazeInAppMessageViewWrapperFactory` unterklassifizieren und nur die Methode `createInAppMessageViewWrapper` überschreiben:

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
**Angepasste Factory für angepassten Wrapper bereitstellen**<br>
Damit das Braze SDK Ihren angepassten Wrapper verwenden kann, müssen Sie eine angepasste `IInAppMessageViewWrapperFactory` Implementierung bereitstellen, die Ihren angepassten Wrapper zurückgibt. Sie können entweder `IInAppMessageViewWrapperFactory` direkt implementieren oder `BrazeInAppMessageViewWrapperFactory` unterklassifizieren und nur die Methode `createInAppMessageViewWrapper` überschreiben:

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
**Factory bei Braze registrieren**<br>
Sobald Sie die angepasste Wrapper-Factory erstellt haben, registrieren Sie sie mit dem Braze SDK über `BrazeInAppMessageManager`:

```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
```
{% endtab %}
{% tab Java %}
**Factory bei Braze registrieren**<br>
Sobald Sie die angepasste Wrapper-Factory erstellt haben, registrieren Sie sie mit dem Braze SDK über `BrazeInAppMessageManager`:

```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
```
{% endtab %}
{% endtabs %}

### Benutzerdefinierte modale In-App-Nachricht

Ein `BrazeInAppMessageModalView` kann unterteilt werden, um einen `Spinner` zu nutzen, der engagierte Möglichkeiten zur Erfassung wertvoller Nutzer bietet. Das folgende Beispiel zeigt, wie Sie mit Connected-Content angepasste Attribute aus einer dynamischen Liste von Artikeln erfassen können. Besuchen Sie die [`TeamPickerView`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/modal/TeamPickerView.kt) um loszulegen.

{% tabs %}
{% tab Kotlin %}
**Verwendung von `view_type` für das Anzeigeverhalten der Benutzeroberfläche**<br>
Das Objekt `IInAppMessage` verfügt über ein `extras` Wörterbuch, das wir abfragen können, um den Schlüssel `view_type` (falls vorhanden) zu finden und die richtige Art der Ansicht anzuzeigen. Es ist wichtig zu wissen, dass In-App-Nachrichten für jede einzelne Nachricht konfiguriert werden, so dass benutzerdefinierte und standardmäßige modale Ansichten harmonisch zusammenarbeiten können.

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
**Verwendung von `view_type` für das Anzeigeverhalten der Benutzeroberfläche**<br>
Das Objekt `IInAppMessage` verfügt über ein `extras` Wörterbuch, das wir abfragen können, um den Schlüssel `view_type` (falls vorhanden) zu finden und die richtige Art der Ansicht anzuzeigen. Es ist wichtig zu wissen, dass In-App-Nachrichten für jede einzelne Nachricht konfiguriert werden, so dass benutzerdefinierte und standardmäßige modale Ansichten harmonisch zusammenarbeiten können.

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

**Benutzerdefinierte Ansicht überschreiben und bereitstellen**<br>
Stellen Sie ein Layout bereit, das die standardmäßige Modal-In-App-Nachricht nachahmt, aber geben Sie Ihre Ansicht als Root-Element an, und erweitern Sie dann das Layout. 
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
**Ansicht anpassen und erweitern**<br>
Bevor Sie die Komponenten von `Spinner` neu laden, wird die Nachrichten-Variable `inAppMessage` als String ausgegeben. Diese Nachricht muss als Array von Artikeln formatiert werden, um korrekt angezeigt zu werden. Dies kann z. B. mit `String.split(",")` erreicht werden.

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
**Ansicht anpassen und erweitern**<br>
Bevor die Komponenten von `Spinner` neu geladen werden, wird die Nachrichten-Variable `inAppMessage` als _String_ ausgegeben. Diese Nachricht muss als Array von Artikeln formatiert werden, um korrekt angezeigt zu werden. Dies kann z. B. mit `String.split(",")` erreicht werden.

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
**Angepasstes Attribut zuweisen**<br>
Nachdem der Nutzer auf "Senden" geklickt hat, übergeben Sie mit Hilfe der View-Subklasse das Attribut mit dem entsprechend ausgewählten Wert an Braze und beenden die In-App-Nachricht durch den Aufruf von `messageClickableView.performClick()`.

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
**Angepasstes Attribut zuweisen**<br>
Nachdem der Nutzer auf "Senden" geklickt hat, übergeben Sie mit Hilfe der View-Subklasse das Attribut mit dem entsprechend ausgewählten Wert an Braze und beenden die In-App-Nachricht durch den Aufruf von `messageClickableView.performClick()`.

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

### Angepasste In-App-Nachricht des Typs "Full"
Die Implementierung einer vollständig angepassten immersiven (Vollbild) In-App-Nachricht erfordert einen ähnlichen Ansatz, wie er im Abschnitt zur Implementierung einer [angepassten modalen In-App-Nachricht](#custom-modal-in-app-message) beschrieben wurde. In dieser Instanz erweitern Sie jedoch einfach `BrazeInAppMessageFullView` und passen es nach Bedarf an. Denken Sie daran, dass die Ansicht über der UI der Anwendung angezeigt wird, und Ansichten in Android sind standardmäßig transparent. Das bedeutet, dass Sie einen Hintergrund definieren müssen, damit die In-App-Nachricht den dahinter liegenden Inhalt verdeckt. Durch die Erweiterung von `BrazeInAppMessageFullView` wird das Braze SDK das Abfangen von Touch-Events auf der Ansicht übernehmen und die entsprechenden Maßnahmen ergreifen. Wie bei dem Modal-Beispiel können Sie dieses Verhalten für bestimmte Steuerelemente (z. B. `Switch`) außer Kraft setzen, um Nutzerfeedback zu erhalten.

{% tabs %}
{% tab Kotlin %}
**Verwendung von `view_type` für das Anzeigeverhalten der Benutzeroberfläche**<br>
Für unsere neue immersive Anpassung fügen wir einen weiteren `view_type` hinzu. Mit der Methode `createInAppMessageView` fügen Sie eine Option für die "Switches"-UI hinzu:

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
**Verwendung von `view_type` für das Anzeigeverhalten der Benutzeroberfläche**<br>
Für unsere neue immersive Anpassung fügen wir einen weiteren `view_type` hinzu. Mit der Methode `createInAppMessageView` fügen Sie eine Option für die "Switches"-UI hinzu:

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

**Benutzerdefinierte Ansicht überschreiben und bereitstellen**<br>
Stellen Sie ein Layout bereit, das die standardmäßige Modal-In-App-Nachricht nachahmt, aber geben Sie Ihre Ansicht als Root-Element an, und erweitern Sie dann das Layout. 
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
**Ansicht anpassen und erweitern**<br>
Bevor die Komponenten von `RecyclerView` festgelegt werden, wird die Nachrichten-Variable `inAppMessage` als _String_ ausgegeben. Diese Nachricht muss als Array von Artikeln formatiert werden, um korrekt angezeigt zu werden. Dies kann z. B. mit `String.split(",")` erreicht werden. Die Dateien `title` und `subtitle` werden ebenfalls aus dem Bündel `extras` extrahiert.

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
**Ansicht anpassen und erweitern**<br>
Bevor die Komponenten von `RecyclerView` festgelegt werden, wird die Nachrichten-Variable `inAppMessage` als _String_ ausgegeben. Diese Nachricht muss als Array von Artikeln formatiert werden, um korrekt angezeigt zu werden. Dies kann z. B. mit `String.split(",")` erreicht werden. Die Dateien `title` und `subtitle` werden ebenfalls aus dem Bündel `extras` extrahiert.

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
**Angepasstes Attribut zuweisen**<br>
Wenn ein Nutzer einen Switch umschaltet, übergeben Sie mit Hilfe der View-Unterklasse das zugehörige Attribut und den Umschaltstatus an Braze.

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
**Angepasstes Attribut zuweisen**<br>
Wenn ein Nutzer einen Switch umschaltet, übergeben Sie mit Hilfe der View-Unterklasse das zugehörige Attribut und den Umschaltstatus an Braze.

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

#### Touch-Events in der In-App-Nachricht abfangen
![Ein Android Gerät, das Reihen von Einstellungen und Umschaltern anzeigt. Die angepasste Ansicht verwaltet die Buttons. Alle Berührungen außerhalb der Button-Steuerelemente werden von der In-App-Nachricht verwaltet und verwerfen diese.]({% image_buster /assets/img/iam_implementation_guide_android.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
Damit die angepassten Buttons für In-App-Nachricht richtig funktionieren, ist das Abfangen von Berührungen in der App entscheidend. Standardmäßig fügen alle In-App-Nachricht-Ansichten `onClick`-Listener zur Nachricht hinzu, sodass Nutzer Nachrichten ohne Buttons verwerfen können. Wenn Sie angepasste Steuerelemente hinzufügen, die auf Nutzereingaben reagieren sollen (z. B. angepasste Buttons), können Sie wie gewohnt einen `onClick`-Listener in der Ansicht registrieren. Bei Berührungen außerhalb der angepassten Steuerelemente wird die In-App-Nachricht wie gewohnt verworfen, während Berührungen, die von den angepassten Steuerelementen empfangen werden, Ihren `onClick`-Listener aufrufen. 

