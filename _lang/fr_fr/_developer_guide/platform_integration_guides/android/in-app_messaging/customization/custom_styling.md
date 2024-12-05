---
nav_title: Style personnalisé
article_title: Style personnalisé de messages in-app pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 2
description: "Cet article de référence décrit les styles de messagerie in-app personnalisés pour votre application Android ou FireOS."
channel:
  - in-app messages

---

# Style personnalisé

> Les éléments de l’IU de Braze sont dotés d’un aspect et d’une convivialité par défaut qui correspondent aux directives de l’IU standard d’Android et offrent une expérience transparente. Cet article de référence décrit les styles de messagerie in-app personnalisés pour votre application Android ou FireOS.

Vous pouvez voir ces styles par défaut dans le fichier [`styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) du SDK Braze :

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

Si vous préférez, vous pouvez écraser ces styles pour créer un aspect et une convivialité qui conviennent mieux à votre application.

Pour remplacer un style, copiez-le dans son intégralité dans le fichier `styles.xml` dans votre projet et apportez des modifications. Le style entier doit être copié sur votre fichier `styles.xml` local pour que tous les attributs soient correctement définis. Notez que ces styles personnalisés sont destinés aux modifications apportées à des éléments individuels de l’IU et non à des modifications globales sur les mises en page. Les modifications au niveau de la disposition doivent être gérées avec des vues personnalisées.

{% alert note %}
Vous pouvez personnaliser certaines couleurs directement dans votre campagne Braze sans modifier le XML. N'oubliez pas que les couleurs définies dans le tableau de bord de Braze remplacent celles que vous avez définies ailleurs.
{% endalert %}

## Police personnalisée

Braze permet de définir une police personnalisée à l'aide du [guide des familles de polices]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization). Pour l’utiliser, remplacez le style du texte du message, des en-têtes et du texte du bouton et utilisez l’attribut `fontFamily` pour indiquer à Braze d’utiliser votre famille de polices personnalisée.

Par exemple, pour mettre à jour la police sur le texte du bouton du message in-app, remplacez le style `Braze.InAppMessage.Button` et faites référence à votre famille de polices personnalisée. La valeur d’attribut doit pointer vers une famille de polices dans votre répertoire `res/font`.

Voici un exemple tronqué avec une famille de polices personnalisées `my_custom_font_family`, référencé sur la dernière ligne :

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Mis à part le style `Braze.InAppMessage.Button` pour le texte du bouton, le style du texte du message est `Braze.InAppMessage.Message` et le style pour les en-têtes de messages est `Braze.InAppMessage.Header`. Si vous souhaitez utiliser votre famille de polices personnalisée pour l’ensemble du texte du message in-app, vous pouvez configurer votre famille de polices sur le style `Braze.InAppMessage`, qui est le style parent pour tous les messages in-app.

{% alert important %}
Comme pour les autres styles personnalisés, le style entier doit être copié sur votre fichier `styles.xml` local pour que tous les attributs soient correctement définis.
{% endalert %}

## Définir une orientation fixe

Pour définir une orientation fixe pour un message in-app, [définissez d'abord un écouteur personnalisé de gestionnaire de messages in-app]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/). Appelez ensuite `setOrientation()` sur l’objet `IInAppMessage` dans la méthode de délégation `beforeInAppMessageDisplayed()` :

{% tabs %}
{% tab JAVA %}
```java
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Set the orientation to portrait
  inAppMessage.setOrientation(Orientation.PORTRAIT);
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  // Set the orientation to portrait
  inAppMessage.orientation = Orientation.PORTRAIT
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

Pour les tablettes, les messages in-app apparaissent dans le style d’orientation préféré de l’utilisateur, quelle que soit l’orientation réelle de l’écran.

