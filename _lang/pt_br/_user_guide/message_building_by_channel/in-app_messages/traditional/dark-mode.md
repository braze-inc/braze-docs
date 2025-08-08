---
nav_title: Temas do modo escuro
article_title: Modo escuro para mensagens no app
page_order: 5
description: "Este artigo de referência aborda o suporte ao modo escuro das mensagens no app do Braze, incluindo como definir um tema de modo escuro e considerações de compatibilidade."
channel:
  - in-app messages

---

# Temas do modo escuro

> O modo escuro oferece aos usuários a oportunidade de definir uma preferência de cor em todo o sistema (introduzido no [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) e no [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)). Os temas "Escuro" têm o objetivo de economizar a vida útil da bateria e reduzir a tensão nos olhos dos usuários, além de oferecer aos desenvolvedores de apps uma maneira mais fácil de implementar os temas de cores escuras que os usuários preferem.

As mensagens no app do Braze suportam a adição de um tema escuro alternativo para ajudar a fornecer a mensagem com a cor certa aos seus usuários com base na preferência deles, além de ajudar a proporcionar consistência com o design do seu app.

## Como funciona o modo escuro

Os usuários com versões de pelo menos Android 10 ou iOS 13 e posteriores podem ativar ou desativar o modo escuro nas configurações do dispositivo.

Quando o Modo escuro é ativado, os menus e as telas nativas do dispositivo (notificações por push, configurações do dispositivo, etc.) mudam para um cinza escuro. Os aplicativos também podem optar por oferecer suporte ao modo escuro especificando os temas alternativos no código do aplicativo.

## Configuração de um tema do modo escuro

A nova opção Modo escuro, localizada na guia Estilo ao [criar uma mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/), permite adicionar facilmente um tema de cor alternativo para usuários que estão no Modo escuro em seus dispositivos.

![Envio de mensagens pelo usuário entre os estilos Modo Claro e Modo Escuro na guia Estilo ao criar uma mensagem no app.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

Quando essa opção está ativada, você pode escolher cores de tema escuro para sua mensagem no app usando o seletor de cores ou selecionando [Perfis de cores]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) existentes para reutilizar os temas Escuro ou Claro existentes.

{% alert note %}
Você ainda pode usar esse recurso mesmo que seu app não ofereça seu próprio tema escuro. No entanto, os dispositivos que não suportam o modo escuro exibirão o tema claro por padrão. A alteração do tema do dispositivo no Android enquanto uma mensagem no app estiver sendo exibida não alterará o tema usado para essa mensagem no app.
{% endalert %}

### Usando o modo escuro de forma consistente

Para usar o modo escuro em todas as mensagens no app, acesse **Modelos** > **Modelos de mensagens no app**.

A partir daí, selecione [Create Color Profile (Criar perfil de cores]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) ) no menu suspenso. Crie um perfil de cores que se alinhe ao tema do modo escuro. Então, sempre que criar uma versão em modo escuro de uma mensagem no app, você poderá selecionar esse perfil de cor e manter a aparência das mensagens no app consistente.

## Compatibilidade

- Seus usuários devem estar em dispositivos iOS versão 13 ou superior, ou Android versão 10 ou superior.
- Braze iOS SDK v3.21.0+ Braze Android SDK v3.8.0+ é necessário.

{% alert note %}
Os apps do modo escuro foram introduzidos com o Android 10 e o iOS 13. Os usuários que não fizeram upgrade de seus telefones para pelo menos essas versões receberão apenas o tema light. <br><br>As campanhas ainda serão veiculadas para todos os usuários que são elegíveis para o público selecionado, independentemente da configuração do modo escuro ou da versão do sistema operacional dos usuários.
{% endalert %}

## Uso de mensagens no app em HTML

Para criar um tema escuro e claro para mensagens HTML no app, você pode usar o recurso de mídia [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) recurso de mídia CSS para detectar a preferência do usuário.

Por exemplo:

```css
@media (prefers-color-scheme: dark) {
  body {
    background: #333;
    color: white;
  }
}

@media (prefers-color-scheme: light) {
  body {
    background: white;
    color: #555;
  }
}
```

