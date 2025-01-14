---
nav_title: Visão geral
article_title: Visão geral das mensagens no app para iOS
platform: iOS
page_order: 0
description: "Este artigo de referência aborda os tipos de mensagens no app do iOS, os comportamentos esperados e vários casos de uso."
channel:
  - in-app messages
search_rank: 4
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Mensagem no app

[As mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) ajudam a levar o conteúdo ao usuário sem interromper o dia dele com uma notificação por push. Mensagens no app personalizadas e sob medida aprimoram a experiência do usuário e ajudam o público a obter o máximo valor do seu app. Com uma variedade de layouts e ferramentas de personalização para escolher, as mensagens no app engajam seus usuários mais do que nunca.

Confira nossos [estudos de caso](https://www.braze.com/customers) para ver exemplos de mensagens no app.

## Tipos de mensagens no app

Atualmente, a Braze oferece os seguintes tipos de mensagens padrão no app: 

- `Slideup`
- `Modal`
- `Full`
- `HTML Full`

Cada tipo de mensagem no app é altamente personalizável em termos de conteúdo, imagens, ícones, ações de clique, análise de dados, exibição e entrega.

Todas as mensagens no app são subclasses do `ABKInAppMessage`, que define o comportamento básico e as características de todas as mensagens no app. As estruturas de classe das mensagens no app são as seguintes:

![Um gráfico que mostra que a classe ABKInAppMessage é a classe raiz da ABKInAppMessageSlideup, ABKInAppMessageImmersive e ABKInAppMessageHTML. O ABKInAppMessage inclui propriedades personalizáveis, como mensagem, extras, duração, ação ao clicar, URI, ação de dispensa, orientação do ícone e alinhamento do texto. O ABKInAppMessageSlideup inclui propriedades personalizáveis, como chevron e âncora deslizante. O ABKInAppMessageImmersive inclui propriedades personalizáveis, como cabeçalho, botão Fechar, quadro e botões de mensagem no app. O ABKInAppMessageHTML permite registrar manualmente os cliques no botão de mensagem no app em HTML.]({% image_buster /assets/img_archive/ABKInAppMessage-models.png %})

{% alert important %}
Por padrão, as mensagens no app são ativadas após a conclusão da integração padrão do SDK, incluindo o suporte a GIF.
<br><br>
Note que a integração do `SDWebImage` é necessária se você planeja usar nossa Braze UI para exibir imagens em mensagens no app do iOS ou em cartões de conteúdo.
{% endalert %}

### Comportamentos esperados por tipos de mensagens

É assim que seus usuários abrem um dos nossos tipos de mensagem no app padrão.

{% tabs %}
{% tab Slideup %}

[`Slideup`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html) As mensagens no app são assim chamadas porque "deslizam para cima" ou "deslizam para baixo" a partir da parte superior ou inferior da tela. Eles cobrem uma pequena parte da tela e fornecem um recurso de envio de mensagens eficaz e não intrusivo.

![Uma mensagem no app que desliza da parte inferior da tela do telefone exibindo "Os seres humanos são complicados. O engajamento personalizado não deveria ser." Em segundo plano, a mesma mensagem no app exibida no canto inferior de uma página da Internet.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}


{% endtab %}
{% tab Modal %}

As mensagens no app [`Modal`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html) aparecem no centro da tela e são emolduradas por um painel translúcido. Úteis para o envio de mensagens mais críticas, eles podem ser capacitados com até dois botões de ação por clique e de análise de dados.

![Uma mensagem modal no app no centro da tela do telefone exibindo "Os seres humanos são complicados. O engajamento personalizado não deveria ser." No plano de fundo, está a mesma mensagem no app exibida no centro de uma página da Internet.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Tela inteira %}

[`Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html) As mensagens no app são úteis para maximizar o conteúdo e o impacto da sua comunicação com o usuário. A metade superior de uma mensagem no app `full` contém uma imagem, e a metade inferior exibe texto e até dois botões de ação de clique e de análise de dados.

![Uma mensagem no app, em tela inteira, exibida em toda a tela do telefone, que diz: "Os seres humanos são complicados. O engajamento personalizado não deveria ser." No plano de fundo, está a mesma mensagem no app exibida em grande parte no centro de uma página da Internet.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab HTML personalizado %}

[`HTML Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html) As mensagens no app são úteis para criar conteúdo totalmente personalizado para o usuário. HTML definido pelo usuário O conteúdo completo da mensagem no app é exibido em `WKWebView`e pode, opcionalmente, conter outros conteúdos avançados, como imagens e fontes, permitindo controle total sobre a aparência e a funcionalidade da mensagem. <br><br>As mensagens no app do iOS suportam uma interface JavaScript `brazeBridge` para chamar métodos no Braze Web SDK a partir do seu HTML; consulte nossas [práticas recomendadas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/) para obter mais detalhes.

O exemplo a seguir mostra uma mensagem no app paginada em HTML Full:

![Uma mensagem no app em HTML com um carrossel de conteúdo e botões interativos.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

O conteúdo completo da mensagem no app é exibido em `WKWebView` e pode, opcionalmente, conter outros conteúdos avançados, como imagens e fontes, permitindo controle total sobre a aparência e a funcionalidade da mensagem. Note que atualmente não oferecemos suporte à exibição de mensagens no app em HTML personalizado em um iFrame nas plataformas iOS e Android.

{% alert note %}
A partir da versão 3.19.0 do SDK do iOS, os seguintes métodos JavaScript são no-ops em mensagens HTML no app: `alert`, `confirm`, `prompt`.
{% endalert %}

{% endtab %}
{% endtabs %}

