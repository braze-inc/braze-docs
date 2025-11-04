---
nav_title: Temas do modo escuro
article_title: Modo escuro para mensagens no aplicativo
page_order: 5
description: "Este artigo de referência aborda o suporte ao modo escuro da mensagem in-app do Braze, incluindo como definir um tema de modo escuro e considerações de compatibilidade."
channel:
  - in-app messages

---

# Temas do Modo escuro

> O Modo escuro oferece aos usuários a oportunidade de definir uma preferência de cor em todo o sistema (introduzido no [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) e no [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)). Os temas "escuros" destinam-se a conservar a vida útil da bateria e a reduzir a pressão sobre os olhos dos usuários, além de oferecer aos desenvolvedores de aplicativos uma maneira mais fácil de implementar os temas de cores escuras preferidos pelos usuários.

As mensagens in-app do Braze suportam a adição de um tema escuro alternativo para ajudar a fornecer a mensagem com a cor certa aos seus usuários com base na preferência deles, além de ajudar a manter a consistência com o design do seu aplicativo.

## Como funciona o Modo escuro

Os usuários com versões de pelo menos Android 10 ou iOS 13 e posteriores podem ativar ou desativar o Modo escuro nas configurações do dispositivo.

Quando o Modo escuro estiver ativado, os menus e as telas nativas do dispositivo (notificações por push, configurações do dispositivo etc.) mudarão para um cinza escuro. Os aplicativos também podem optar por oferecer suporte ao modo escuro, especificando os temas alternativos no código do aplicativo.

## Configuração de um tema do Modo escuro

A nova opção Dark Mode (Modo escuro), localizada na guia Style (Estilo) ao [criar uma mensagem no aplicativo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/), permite adicionar facilmente um tema de cor alternativo para usuários que estão no Modo escuro em seus dispositivos.

O usuário alternava entre os estilos Modo claro e Modo escuro na guia Estilo ao criar uma mensagem no aplicativo.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

Quando essa opção está ativada, você pode escolher cores de tema escuro para sua mensagem no aplicativo usando o seletor de cores ou selecionando [Perfis de cores]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) existentes para reutilizar os temas Escuro ou Claro existentes.

{% alert note %}
Você ainda pode usar esse recurso mesmo que seu aplicativo não ofereça seu próprio tema escuro. No entanto, os dispositivos que não suportam o Modo escuro exibirão o tema Claro por padrão. Alterar o tema do dispositivo no Android enquanto uma mensagem no aplicativo estiver sendo exibida não alterará o tema usado para essa mensagem no aplicativo.
{% endalert %}

### Uso consistente do modo escuro

Para usar o Modo escuro em todas as mensagens no aplicativo, vá para **Modelos** > **Modelos de mensagens no aplicativo**.

A partir daí, selecione [Create Color Profile (Criar perfil de cores]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) ) no menu suspenso. Crie um perfil de cores que se alinhe ao tema do Modo escuro. Então, sempre que você criar uma versão Dark Mode de uma mensagem in-app, poderá selecionar esse Color Profile e manter a aparência de suas mensagens in-app consistente.

## Compatibilidade

- Seus usuários devem estar em dispositivos iOS versão 13 ou superior, ou em dispositivos Android versão 10 ou superior.
- Braze iOS SDK v3.21.0+ Braze Android SDK v3.8.0+ é necessário.

{% alert note %}
Os aplicativos do Modo escuro foram introduzidos no Android 10 e no iOS 13. Os usuários que não atualizaram seus telefones para pelo menos essas versões receberão apenas o tema light. <br><br>As campanhas ainda serão veiculadas para todos os usuários qualificados para o público-alvo selecionado, independentemente da configuração do Modo escuro ou da versão do sistema operacional dos usuários.
{% endalert %}

## Uso de mensagens HTML no aplicativo

Para criar um tema escuro e claro para mensagens HTML no aplicativo, você pode usar o recurso de mídia [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) recurso de mídia CSS para detectar a preferência do usuário.

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

