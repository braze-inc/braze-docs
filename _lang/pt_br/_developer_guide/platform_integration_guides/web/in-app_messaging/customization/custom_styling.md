---
nav_title: Estilo Personalizado
article_title: Mensagens no app com estilo personalizado para a Internet
platform: Web
channel: in-app messages
page_order: 1
page_type: reference
description: "Este artigo aborda o estilo personalizado de mensagens no app para seu aplicativo da Web."

---

# Estilo personalizado

> Os elementos da interface do usuário do Braze vêm com uma aparência padrão que cria uma experiência neutra de mensagens no app e visa à consistência com outras plataformas móveis do Braze. Os estilos padrão da Braze são definidos em CSS no SDK da Braze. 

Ao substituir estilos selecionados em seu aplicativo, você pode personalizar nossos tipos de mensagem no app padrão com suas próprias imagens de fundo, famílias de fontes, estilos, tamanhos, animações e muito mais. 

Na instância do app a seguir, há um exemplo de substituição que fará com que os cabeçalhos de uma mensagem no app apareçam em itálico:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

Consulte os [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) para saber mais.

## Z-index padrão de mensagens no app

Por padrão, as mensagens no app são exibidas usando `z-index: 9001`. Isso pode ser configurado usando a [opção de inicialização](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `inAppMessageZIndex `, caso seu site estilize elementos com valores mais altos do que esse.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
Essa opção foi introduzida no Web SDK v3.3.0. Para usar essa opção, é necessário fazer upgrade nos SDKs mais antigos.
{% endalert %}

