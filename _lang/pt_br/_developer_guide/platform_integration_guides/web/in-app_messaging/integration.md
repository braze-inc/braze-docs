---
nav_title: Integração
article_title: Integração de mensagem no app para a web
platform: Web
channel: in-app messages
page_order: 0
page_type: reference
description: "Este artigo inclui recursos sobre tipos de mensagem no app e comportamento de mensagem para seu aplicativo web."
search_rank: 2
---

# Integração de mensagem no app

> Este artigo cobre como configurar mensagens no app para o aplicativo web.

[Mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) ajudam você a entregar conteúdo aos seus usuários sem interromper o dia deles com uma notificação por push. Mensagens no app personalizadas e sob medida aprimoram a experiência do usuário e ajudam o público a obter o máximo valor do seu app. Com vários layouts e ferramentas de personalização para escolher, as mensagens no app envolvem seus usuários mais do que nunca.

Confira nossos [estudos de caso](https://www.braze.com/customers) para ver exemplos de mensagens no app.

## Tipos de mensagens no app

Atualmente, a Braze oferece os seguintes tipos de mensagens padrão no app: 

- `Slideup`
- `Modal`
- `Full`
- `HTML`

Cada tipo de mensagem no app é personalizável em termos de conteúdo, imagens, ícones, ações de clique, análise de dados, exibição e entrega.

Todas as mensagens no app herdam seu protótipo de [`InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)que define o comportamento básico e as características de todas as mensagens no app. As subclasses prototípicas são [`SlideUpMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html), [`ModalMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html), [`FullScreenMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html), e [`HtmlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html).

## Comportamentos esperados por tipo de mensagem

É assim que parece para seus usuários abrir um dos nossos tipos padrão de mensagem no app.

{% tabs %}
{% tab Slideup %}

As mensagens no app [`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) têm esse nome porque, nas plataformas móveis, elas  tradicionalmente "deslizam para cima" ou "deslizam para baixo" do topo ou da parte inferior da tela. No Braze Web SDK, essas mensagens são exibidas mais como uma notificação no estilo Growl ou Toast para alinhar com o paradigma dominante da web. Eles cobrem uma pequena parte da tela e fornecem um recurso de envio de mensagens eficaz e não intrusivo.

![Uma mensagem no app que desliza da parte inferior da tela do telefone exibindo "Os seres humanos são complicados. O engajamento personalizado não deveria ser." Em segundo plano, a mesma mensagem no app exibida no canto inferior de uma página da Internet.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

As mensagens no app [`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) aparecem no centro da tela e são emolduradas por um painel translúcido. Úteis para o envio de mensagens mais críticas, eles podem ser capacitados com até dois botões de ação por clique e de análise de dados.

![Uma mensagem modal no app no centro da tela do telefone exibindo "Os seres humanos são complicados. O engajamento personalizado não deveria ser." No plano de fundo, está a mesma mensagem no app exibida no centro de uma página da Internet.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Tela inteira %}

[`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) As mensagens no app são úteis para maximizar o conteúdo e o impacto da sua comunicação com o usuário. Em janelas de navegador estreitas (por exemplo, na web móvel), mensagem no app `full` ocupam toda a janela do navegador. Em janelas de navegador maiores, mensagens no app `full` aparecem de forma semelhante a mensagens no app `modal`. A metade superior de uma mensagem no app `full` contém uma imagem, e a metade inferior permite até oito linhas de texto, bem como até dois botões com ação de clique e habilitados para análise de dados.

![Uma mensagem no app de tela cheia exibida em toda a tela do telefone mostrando: "Os humanos são complicados." O engajamento personalizado não deveria ser." No plano de fundo, está a mesma mensagem no app exibida em grande parte no centro de uma página da Internet.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab HTML personalizado %}

[`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) As mensagens no app são úteis para criar conteúdo totalmente personalizado para o usuário. O conteúdo HTML definido pelo usuário é exibido em um iFrame e pode conter conteúdos avançados, como imagens, fontes, vídeos e elementos interativos, permitindo controle total sobre a aparência e a funcionalidade da mensagem. Esses suportam uma interface JavaScript `brazeBridge` para chamar métodos no Braze Web SDK de dentro do HTML. Para saber mais, consulte nossas [práticas recomendadas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

{% alert important %}

Para ativar mensagens no app HTML através do Web SDK, você **deve** fornecer a opção de inicialização `allowUserSuppliedJavascript` para a Braze, por exemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Isto é por razões de segurança. Mensagens HTML no app podem executar JavaScript, então exigimos que um mantenedor do site as ative.

{% endalert %}

O exemplo a seguir mostra uma mensagem no app HTML paginada:

![Uma mensagem no app em HTML com um carrossel de conteúdo e botões interativos.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}

## Integração

Por padrão, as mensagens no app são exibidas automaticamente como parte de nossas [instruções de integração]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/). ] recomendadas. A personalização adicional pode ser feita seguindo as etapas deste guia.

