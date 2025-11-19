# Implementation examples

> This optional and advanced implementation guide covers in-app message code considerations, three custom use cases built by our team, and accompanying code snippets. Visit our Braze Demo repository [here](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Note that this implementation guide is centered around a Kotlin implementation, but Java snippets are provided for those interested. Looking for HTML implementations? Take a look at our [HTML template repository](https://github.com/braze-inc/in-app-message-templates)!

## Code considerations

The following guide offers an optional custom developer integration to use in addition to default in-app messages. Custom view components and factories are included as needed with each use case, offering examples to extend functionality and natively customize the look and feel of your in-app messages. There are, in some instances, multiple ways to achieve similar results. The optimal implementation will depend on the specific use case.

### Custom factories

The Braze SDK allows developers to override a number of defaults through custom factory objects. These can be registered with the Braze SDK as needed to achieve the desired results. In most cases, however, if you decide to override a factory, you will need to either explicitly defer to the default or reimplement the functionality provided by the Braze default. The following code snippet illustrates how to supply custom implementations of the `IInAppMessageViewFactory` and the `IInAppMessageViewWrapperFactory` interfaces. After you have a solid understanding of the concepts behind overriding our default factories, check out our [use cases](#sample-use-cases) to get started implementing custom in-app messaging functionality.

{% tabs %}
{% tab Kotlin %}
**In-app message types**<br>

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
**In-app message types**<br> 

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

## Use cases

We've provided three use cases below. Each use case has code snippets and a look into how in-app messages may look and be used in the Braze dashboard:
- [Implementation examples](#implementation-examples)
  - [Code considerations](#code-considerations)
    - [Custom factories](#custom-factories)
  - [Use cases](#use-cases)
    - [Custom slide-up in-app message](#custom-slide-up-in-app-message)
      - [Custom view wrapper](#custom-view-wrapper)
    - [Custom modal in-app message](#custom-modal-in-app-message)
    - [Custom full in-app message](#custom-full-in-app-message)
      - [Intercepting in-app message touches](#intercepting-in-app-message-touches)

### Custom slide-up in-app message

While building out your slide-up in-app message, you may notice you aren't able to modify the placement of the message using default methods. Modification like this is made possible by subclassing the `DefaultInAppMessageViewWrapper` class to adjust the layout parameters. You can adjust the final position on the screen by overriding the `getLayoutParams` method returning the modified `LayoutParams` with your own custom positioning values. Visit the [CustomSlideUpInAppMessageViewWrapper](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/slideup/CustomSlideUpInAppMessageViewWrapper.kt) to get started.

#### Custom view wrapper<br><br>

{% tabs %}
{% tab Kotlin %}
**Override and return custom layout parameters**<br>
Within the `getLayoutParams` method, you can use the superclass method to access the original `LayoutParameters` for the in-app message. Then, you can adjust the position by adding or subtracting as desired.

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
**Override and return custom layout parameters**<br>
Within the `getLayoutParams` method, you can use the superclass method to access the original `LayoutParameters` for the in-app message. Then, you can adjust the position by adding or subtracting as desired.

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
**Supply a custom factory to return your custom wrapper**<br>
In order for the Braze SDK to use your custom wrapper, you also need to supply a custom `IInAppMessageViewWrapperFactory` implementation that returns your custom wrapper. You can either implement the `IInAppMessageViewWrapperFactory` directly, or subclass `BrazeInAppMessageViewWrapperFactory` and only override the `createInAppMessageViewWrapper` method:

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
**Supply a custom factory to return your custom wrapper**<br>
In order for the Braze SDK to use your custom wrapper, you need to supply a custom `IInAppMessageViewWrapperFactory` implementation that returns your custom wrapper. You can either implement the `IInAppMessageViewWrapperFactory` directly, or subclass `BrazeInAppMessageViewWrapperFactory` and only override the `createInAppMessageViewWrapper` method:

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
**Register your factory with Braze**<br>
Once you've created your custom wrapper factory, register it with the Braze SDK via the `BrazeInAppMessageManager`:

```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
```
{% endtab %}
{% tab Java %}
**Register your factory with Braze**<br>
Once you've created your custom wrapper factory, register it with the Braze SDK via the `BrazeInAppMessageManager`:

```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
```
{% endtab %}
{% endtabs %}

### Custom modal in-app message

A `BrazeInAppMessageModalView` can be subclassed to leverage a `Spinner` offering engaging ways to collect valuable user attributes. The following example shows how you can use Connected Content to capture custom attributes from a dynamic list of items. Visit the [`TeamPickerView`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/inapp/modal/TeamPickerView.kt) to get started.

{% tabs %}
{% tab Kotlin %}
**Using `view_type` for UI display behavior**<br>
The `IInAppMessage` object has an `extras` dictionary that we can query to find the `view_type` key (if any) and display the correct type of view. It's important to note that in-app messages are configured on a per-message basis, so custom and default modal views can work harmoniously.

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
**Using `view_type` for UI display behavior**<br>
The `IInAppMessage` object has an `extras` dictionary that we can query to find the `view_type` key (if any) and display the correct type of view. It's important to note that in-app messages are configured on a per-message basis, so custom and default modal views can work harmoniously.

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

**Override and provide custom view**<br>
Provide a layout that mimics the standard modal in-app message, but supply your view as the root element, and then inflate that layout 
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
**Inflate and customize the view**<br>
Before reloading the `Spinner` components, the `inAppMessage` message variable is output as a string. This message must be formatted as an array of items to be displayed correctly. As an example, this can be achieved using `String.split(",")`.

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
**Inflate and customize the view**<br>
Before reloading the `Spinner` components, the `inAppMessage` message variable is output as a _String_. This message must be formatted as an array of items to be displayed correctly. As an example, this can be achieved using `String.split(",")`.

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
**Assign custom attribute**<br>
Using the view subclass, after a user presses submit, pass the attribute with its corresponding selected value to Braze and dismiss the in-app message by calling `messageClickableView.performClick()`.

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
**Assign custom attribute**<br>
Using the view subclass, after a user presses submit, pass the attribute with its corresponding selected value to Braze and dismiss the in-app message by calling `messageClickableView.performClick()`.

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

### Custom full in-app message
Implementing a fully custom immersive (full screen) in-app message involves a similar approach outlined in the section for implementing a [customized modal in-app message](#custom-modal-in-app-message). In this instance, however, simply extend `BrazeInAppMessageFullView` and customize as needed. Remember that the view will be displayed over the application UI, and views in Android by default are transparent. This means you will need to define a background such that the in-app message obscures the content behind it. By extending `BrazeInAppMessageFullView`, the Braze SDK will handle intercepting touch events on the view and take the appropriate action. Like with the modal example, you can override this behavior for certain controls (like `Switch` controls) to collect feedback from the user.

{% tabs %}
{% tab Kotlin %}
**Using `view_type` for UI display behavior**<br>
We will add another `view_type` extra for our new immersive customization. Revisiting the `createInAppMessageView` method, add a option for the "switches" UI:

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
**Using `view_type` for UI display behavior**<br>
We will add another `view_type` extra for our new immersive customization. Revisiting the `createInAppMessageView` method, add a option for the "switches" UI:

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

**Override and provide custom view**<br>
Provide a layout that mimics the standard modal in-app message, but supply your view as the root element, and then inflate that layout 
```xml
<?xml version="1.0" encoding="utf-8"?>
<com.braze.advancedsamples.immersive.CustomImmersiveInAppMessage
        xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
        android:layout_height="wrap_content">
    <!-- giving the parent layout a white background color will obscure the app behind the IAM. You could also do this within your custom view -->
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
**Inflate and customize the view**<br>
Before setting the options for the `RecyclerView` component, the `inAppMessage` message variable is output as a _String_. This message must be formatted as an array of items to be displayed correctly. As an example, this can be achieved using `String.split(",")`. The `title` and `subtitle` are also extracted from the `extras` bundle.

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
**Inflate and customize the view**<br>
Before setting the options for the `RecyclerView` component, the `inAppMessage` message variable is output as a _String_. This message must be formatted as an array of items to be displayed correctly. As an example, this can be achieved using `String.split(",")`. The `title` and `subtitle` are also extracted from the `extras` bundle.

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
**Assign custom attribute**<br>
Using the view subclass, after a user toggles one of the switches, pass the associated attribute and the toggle status to Braze.

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
**Assign custom attribute**<br>
Using the view subclass, after a user toggles one of the switches, pass the associated attribute and the toggle status to Braze.

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

#### Intercepting in-app message touches
![An android device displaying rows of settings and toggles. The custom view handles the buttons, and any touches outside of the button controls are handled by the in-app message and will dismiss it.]({% image_buster /assets/img/iam_implementation_guide_android.png %}){: style="float:right;max-width:30%;margin-left:10px;border:0"}
Intercepting in-app message touches is crucial in making the custom full in-app message buttons function correctly. By default, all in-app message views add `onClick` listeners onto the message, so users can dismiss messages without buttons. When you add custom controls that should respond to user input (like custom buttons), you can register an `onClick` listener with the view as normal. Any touches outside of the custom controls will dismiss the in-app message as usual, while touches received by the custom controls will invoke your `onClick` listener. 

