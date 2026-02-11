{% multi_lang_include developer_guide/prerequisites/web.md %}

## Estilos personalizados

Os elementos da interface do usuário do Braze vêm com uma aparência padrão que cria uma experiência neutra de mensagens no app e visa à consistência com outras plataformas móveis do Braze. Os estilos padrão do Braze são definidos em CSS no SDK do Braze. 

### Definição de um estilo padrão

Ao substituir estilos selecionados em seu aplicativo, você pode personalizar nossos tipos de mensagem no app padrão com suas próprias imagens de fundo, famílias de fontes, estilos, tamanhos, animações e muito mais. 

Na instância do app a seguir, há um exemplo de substituição que fará com que os cabeçalhos de uma mensagem no app apareçam em itálico:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

Consulte os [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) para saber mais.

### Personalização do z-index

Por padrão, as mensagens no app são exibidas usando `z-index: 9001`. Isso pode ser configurado usando a [opção de inicialização](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `inAppMessageZIndex `, caso seu site estilize elementos com valores mais altos do que esse.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
Esse recurso está disponível apenas para o Web Braze SDK v3.3.0 e posterior.
{% endalert %}

## Personalização do envio de mensagens

Por padrão, quando uma mensagem no app estiver sendo exibida, pressionar o botão de escape ou clicar no fundo acinzentado da página descartará a mensagem. Configure a [opção de inicialização](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `requireExplicitInAppMessageDismissal` para `true` para evitar esse comportamento e exigir um clique explícito no botão para descartar as mensagens. 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

## Abrir links em uma nova guia

Para configurar os links das mensagens no app para abrirem em uma nova guia, defina a opção `openInAppMessagesInNewTab` como `true` para forçar todos os links de cliques em mensagens no app a abrirem em uma nova guia ou janela.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```
