---
nav_title: Integração
article_title: Visão geral das mensagens no app para iOS
platform: Swift
page_order: 0
description: "Este artigo aborda os tipos de mensagens no app do iOS, os comportamentos esperados e vários casos de uso para o Swift SDK."
channel:
  - in-app messages

---

# Integração de mensagens no app

> [As mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) ajudam a levar o conteúdo ao usuário sem interromper o dia dele com uma notificação por push. Mensagens no app personalizadas e sob medida aprimoram a experiência do usuário e ajudam o público a obter o máximo valor do seu app. Com uma variedade de layouts e ferramentas de personalização para escolher, as mensagens no app engajam seus usuários mais do que nunca.

Confira nossos [estudos de caso](https://www.braze.com/customers) para ver exemplos de mensagens no app.

## Tipos de mensagens no app

Atualmente, a Braze oferece os seguintes tipos de mensagens padrão no app: 

- Slideup
- Modal
- Imagem Modal
- Completo
- Imagem completa
- HTML personalizado
- Controle

Cada tipo de mensagem no app é altamente personalizável em termos de conteúdo, imagens, ícones, ações de clique, análise de dados, exibição e entrega.

Para obter uma lista completa das propriedades e do uso das mensagens no app, consulte a [documentação da classe `InAppMessage`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

Todas as mensagens no app são tipos enumerados de `Braze.InAppMessage`, que define o comportamento básico e as características de todas as mensagens no app. Cada tipo de mensagem no app e seus detalhes correspondentes estão listados nas guias abaixo.

### Comportamentos esperados por tipos de mensagens

É assim que seus usuários abrem um dos nossos tipos de mensagem no app padrão.

{% tabs %}
{% tab Slideup %}

[`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct) As mensagens no app são assim chamadas porque "deslizam para cima" ou "deslizam para baixo" a partir da parte superior ou inferior da tela. Eles cobrem uma pequena parte da tela e fornecem um recurso de envio de mensagens eficaz e não intrusivo.

![Uma mensagem no app em slideup na parte inferior e superior da tela do telefone.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endtab %}
{% tab Modal %}

[`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct) As mensagens no app aparecem no centro da tela e são emolduradas por um painel translúcido. Úteis para o envio de mensagens mais críticas, eles podem ser equipados com até dois botões ativados por análise de dados.

![Uma mensagem modal no app no centro da tela do telefone.]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Imagem de modal %}

[`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct) As mensagens no app aparecem no centro da tela e são emolduradas por um painel translúcido. Essas mensagens são semelhantes ao tipo `Modal`, mas sem cabeçalho ou texto de mensagem. Úteis para o envio de mensagens mais críticas, eles podem ser equipados com até dois botões ativados por análise de dados.

![Uma mensagem no app com imagem modal no centro da tela do telefone.]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Tela cheia %}

[`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct) As mensagens no app são úteis para maximizar o conteúdo e o impacto da sua comunicação com o usuário. A metade superior de uma mensagem no app `Full` contém uma imagem, e a metade inferior exibe texto e até dois botões de análise de dados.

![Uma mensagem no app em tela cheia exibida em toda a tela do telefone.]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Imagem em tela inteira %}

[`Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct) As mensagens no app são semelhantes às mensagens no app `Full`, exceto pelo fato de não terem cabeçalho ou texto de mensagem. Esse tipo de mensagem é útil para maximizar o conteúdo e o impacto da sua comunicação com o usuário. Uma mensagem no app `Full Image` contém uma imagem que abrange toda a tela, com a opção de exibir até dois botões de análise de dados ativados.

![Uma mensagem no app com imagem em tela cheia exibida em toda a tela do telefone.]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab HTML personalizado %}

[`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct) As mensagens no app são úteis para criar conteúdo totalmente personalizado para o usuário. HTML definido pelo usuário O conteúdo completo da mensagem no app é exibido em `WKWebView`e pode, opcionalmente, conter outros conteúdos avançados, como imagens e fontes, permitindo controle total sobre a aparência e a funcionalidade da mensagem. <br><br>As mensagens no app do iOS suportam uma interface JavaScript `brazeBridge` para chamar métodos no Braze Web SDK a partir do seu HTML; consulte nossas [práticas recomendadas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) para obter mais detalhes.

O exemplo a seguir mostra uma mensagem no app paginada em HTML Full:

![Uma mensagem no app em HTML com um carrossel de conteúdo e botões interativos.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

Note que atualmente não oferecemos suporte à exibição de mensagens no app em HTML personalizado em um iFrame nas plataformas iOS e Android.

{% endtab %}
{% tab Controle %}

[`Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct) As mensagens no app não contêm um componente de interface do usuário e são usadas principalmente para fins de análise de dados. Esse tipo é usado para verificar o recebimento de uma mensagem no app enviada a um grupo de controle.

Para obter mais detalhes sobre a seleção inteligente e os grupos de controle, consulte [Seleção inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

{% endtab %}
{% endtabs %}


{% alert important %}
A integração padrão do SDK inclui etapas que ativam mensagens no app, incluindo suporte a GIFs. Para saber mais sobre o suporte a GIFs, consulte este [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support).
{% endalert %}


