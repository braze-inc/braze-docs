{% multi_lang_include developer_guide/prerequisites/android.md %}

## Using custom fonts

### Step 1: Create a font family

The following is an example custom font family definition using the [font family guide](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html#font-family). For this example, we use the [Bungee Shade font](https://fonts.google.com/specimen/Bungee+Shade).

```html
<?xml version="1.0" encoding="utf-8"?>
<font-family xmlns:android="http://schemas.android.com/apk/res/android"
             xmlns:app="http://schemas.android.com/apk/res-auto">

  <!--Note: You must declare both sets of attributes
      so that your fonts load on devices running Android 8.0 (API level 26) or lower.
      See https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html -->

  <font android:fontStyle="normal"
        android:fontWeight="400"
        android:font="@font/bungeeshade"

        app:fontStyle="normal"
        app:fontWeight="400"
        app:font="@font/bungeeshade"/>
</font-family>
```

After storing the font family definition in `/res/font/bungee_font_family.xml`, we can refer to it in XML as `@font/bungee_font_family`.

### Step 2: Reference your font family

Now that the font family is created, you can override Braze style defaults in your `styles.xml` to include references to the font family.

For example, the following styles override would use the `bungee` font family for all Braze in-app messages.

```html
<style name="Braze.InAppMessage">
  <item name="android:fontFamily">@font/bungee_font_family</item>
  <item name="fontFamily">@font/bungee_font_family</item>
</style>

<style name="Braze.Cards">
  <item name="android:fontFamily">@font/another_custom_font_family</item>
  <item name="fontFamily">@font/another_custom_font_family</item>
</style>
```

{% alert warning %}
Both `android:fontFamily` and `fontFamily` style attributes must be set to maintain compatibility across all SDK versions.
{% endalert %}
