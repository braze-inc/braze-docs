{% multi_lang_include developer_guide/prerequisites/android.md %}

## Uso de fontes personalizadas

### Etapa 1: Criar uma família de fontes

A seguir, um exemplo de definição de família de fontes personalizada usando o [guia de família de fontes](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html#font-family). Para este exemplo, usamos a [fonte Bungee Shade](https://fonts.google.com/specimen/Bungee+Shade).

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

Depois de armazenar a definição da família de fontes em `/res/font/bungee_font_family.xml`, podemos fazer referência a ela em XML como `@font/bungee_font_family`.

### Etapa 2: Faça referência à sua família de fontes

Agora que a família de fontes foi criada, você pode substituir os padrões de estilo do Braze em seu site `styles.xml` para incluir referências à família de fontes.

Por exemplo, a seguinte substituição de estilos usaria a família de fontes `bungee` para todas as mensagens no app do Braze.

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
Os atributos de estilo `android:fontFamily` e `fontFamily` devem ser definidos para manter a compatibilidade em todas as versões do SDK.
{% endalert %}
