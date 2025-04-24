---
nav_title: Gerações Anteriores
article_title: Gerações Anteriores de Mensagens no App
page_order: 20
page_type: reference
description: "Este artigo revisa informações anteriores sobre mensagens no app no Braze."
channel: in-app messages
noindex: true
hidden : true
---

# Gerações anteriores de mensagem no app

{% alert important %}
Esta página revisa informações anteriores sobre nossas mensagens no app. Para ver as informações mais atualizadas sobre nossa geração atual de mensagem no app, consulte nossa documentação atual de [mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/).
{% endalert %}

## Universal

Isso revisará informações anteriores sobre nossas mensagens no app. Para ver as informações mais atualizadas sobre nossa geração atual de mensagem no app, consulte nossa [documentação de visão geral de mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/).

{% details Tela cheia %}
Estes são os mais envolventes, mas também os mais intrusivos, pois cobrem toda a tela do seu usuário. São ótimos para exibir imagens grandes e ricas, e podem ser úteis para transmitir informações muito importantes, como novos recursos cruciais e promoções que estão expirando. Como são mais disruptivos para a experiência do usuário, use-os com moderação para conteúdo de alta prioridade.

![Mensagem em tela cheia]({% image_buster /assets/img_archive/braze_fullscreen.png %}){: style="max-width:80%;"}

**Recursos Personalizáveis**

- Texto de cabeçalho e corpo
- Uma imagem grande
- Até dois botões de call to action com comportamento ao clicar e deep linking separados
- Cores diferentes para o texto do cabeçalho e do corpo, botões e fundo
- Pares chave-valor

{% enddetails %}
{% details  Modal %}
Essas mensagens não são tão intrusivas quanto as mensagens em tela cheia, pois ainda permitem que os usuários vejam parte da interface do usuário do seu app. Como ainda contêm botões e imagens, as mensagens modais podem ser uma opção melhor do que os slideups se você deseja uma campanha mais interativa e visual. Estes são ótimos para conteúdo de prioridade média, como atualizações de app e ofertas e eventos não urgentes.

![Mensagem Modal]({% image_buster /assets/img_archive/braze_modal.png %}){: style="max-width:80%;"}

**Recursos Personalizáveis**

- Texto de cabeçalho e corpo
- Uma imagem ou ícone de emblema personalizável
- Até dois botões de call to action com comportamento ao clicar e deep linking separados
- Cores diferentes para o texto do cabeçalho e do corpo, botões e fundo
- Pares chave-valor

{% enddetails %}

{% details Slideup Tradicional %}
Estas são as mensagens menos intrusivas, embora possam ser mais ou menos chamativas dependendo do seu uso de cores e ícones de emblema. Este pode ser o formato de mensagem a ser usado ao integrar novos usuários e direcioná-los para recursos específicos no app, pois eles não pausam a experiência do app e permitem uma exploração contínua.

![Mensagem slideup]({% image_buster /assets/img_archive/stopwatch_slideup_IAM.gif %}){: style="max-width:50%;"}

**Recursos Personalizáveis**

- Texto do corpo
- Uma imagem ou ícone de emblema personalizável
- Cores diferentes para o fundo, texto e ícone do slideup
- Comportamento de fechamento de mensagem
- Posição do slideup (parte superior ou inferior da tela do app)
- Pares chave-valor

{% enddetails %}

<br>

## Web

Isso revisará informações anteriores sobre mensagens no app mais personalizadas. Para ver as informações mais atualizadas sobre nossa geração atual de mensagem no app, consulte nossa [documentação de personalização]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/).

{% details Mensagem de captura de e-mail %}
Mensagens de captura de e-mail permitem que você solicite facilmente aos usuários do seu site que enviem seu endereço de e-mail, após o qual ele estará disponível no sistema Braze para uso em todas as suas campanhas de envio de mensagens.

![Mensagem de captura de e-mail]({% image_buster /assets/img_archive/web-email-capture.png %}){: style="max-width:60%;"}

>  Para ativar mensagens no app de captura de e-mail através do Web SDK, você deve fornecer a opção de inicialização `allowUserSuppliedJavascript` para a Braze, por exemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Isso ocorre por motivos de segurança, pois as mensagens HTML no app podem executar JavaScript, portanto, exigimos que um mantenedor de site as ative.

**Recursos Personalizáveis**

- Texto do cabeçalho, corpo e botão de envio
- Uma imagem opcional
- Um link opcional para os "Termos de Serviço"
- Cores diferentes para o texto do cabeçalho e do corpo, botões e fundo
- Pares chave-valor

{% enddetails %}

{% details Mensagem HTML Personalizada %}

Embora as mensagens in-app prontas para uso da Braze possam ser personalizadas de várias maneiras, você pode obter ainda mais controle sobre a aparência e a sensação de suas campanhas usando mensagens projetadas e construídas com HTML, CSS e JavaScript. Com uma composição simples, você pode desbloquear funcionalidades personalizadas e branding para atender a qualquer uma de suas necessidades. Mensagens no app em HTML permitem maior controle sobre a aparência e a sensação de uma mensagem, e tudo o que é compatível com HTML5 também é compatível com a Braze.

**Ponte JavaScript (appboyBridge)**

As mensagens em HTML no app suportam uma interface de "ponte" JavaScript para o Braze Web SDK, permitindo que você dispare ações personalizadas do Braze quando os usuários clicam em elementos com links ou interajam de outra forma com seu conteúdo. Os seguintes métodos JavaScript são suportados nas mensagens no app em HTML da Braze:

{% multi_lang_include archive/appboyBridge.md platform="web" %}

Além disso, para rastreamento de análise de dados, qualquer `<a>` ou `<button>` elementos no seu HTML registrarão automaticamente uma ação de "clique" na campanha associada à mensagem no app. Para registrar um "clique no botão" em vez de um "clique no corpo", forneça um valor da string de consulta de abButtonId no href do seu link (por exemplo, `<a href="http://mysite.com?abButtonId=0">click me</a>`), ou forneça um id no elemento HTML (por exemplo, `<a id="0" href="http://mysite.com">click me</a>`). Observe que os únicos IDs de botões atualmente aceitos são "0" e "1". Um link com um id de botão de 0 será representado como "Botão 1" no dashboard, enquanto um link com um id de botão de 1 será representado como "Botão 2."

>  Para ativar mensagens no app HTML através do Web SDK, você deve fornecer a opção de inicialização `allowUserSuppliedJavascript` para a Braze, por exemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Isso ocorre por motivos de segurança, pois as mensagens HTML no app podem executar JavaScript, portanto, exigimos que um mantenedor de site as ative.

{% enddetails %}

{% details Modelos de Mensagem no App em HTML %}

Nós projetamos um conjunto de modelos de mensagens no app em HTML5 para ajudar você a dar os primeiros passos. Confira nosso [repositório GitHub](https://github.com/braze-inc/in-app-message-templates) que contém instruções detalhadas sobre como usar e personalizar esses modelos para suas necessidades.

**Recursos Personalizáveis**

- Fontes
- Estilos
- Imagens + Vídeos
- Comportamentos ao clicar
- Componentes Interativos

{% enddetails %}

<br>

## Especificações

Isso revisará informações anteriores sobre nossas especificações criativas de mensagens no app. Para ver as informações mais atualizadas sobre nossa geração atual de mensagens no app, consulte nossa [documentação de especificações criativas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Limites de caracteres e imagens

Para todos os tipos de mensagem no app listados na tabela a seguir, aplicam-se as seguintes diretrizes adicionais:

- **Tamanho de imagem recomendado:** 500 KB 
- **Tamanho máximo da imagem:** 5 MB
- **Tipos de arquivos suportados:** PNG, JPEG, GIF

| Tipo                               | Proporção de Aspecto | Contagem Máxima de Caracteres |
| :--------------------------------- | :----------: | :-----------------: |
| Retrato em Tela Cheia (Apenas Imagem)  |    10:16     |         240         |
| Retrato em Tela Cheia (Com Texto)   |     5:4      |         240         |
| Paisagem Tela Cheia (Com Texto)  |     16:5     |         240         |
| Tela cheia de paisagem (somente imagem) |    16:10     |         240         |
| Slideup                            |     1:1      |         140         |
| Modal (apenas imagem)                 |     1:1      |         140         |
| Modal (Com Texto)                  |    29:10     |         140         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Manter os tamanhos dos arquivos de mensagem no app pequenos

A Braze recomenda que você mantenha suas imagens e arquivos HTML zipados o menor possível por várias razões:

- Mensagens HTML e imagens menores serão baixadas mais rapidamente e exibidas de forma mais rápida e confiável para seus clientes.
- Cargas úteis menores de HTML e imagens também manterão os custos de dados do seu cliente baixos. As mensagens in-app da Braze são baixadas em segundo plano no início da sessão para que possam ser acionadas em tempo real com base em qualquer critério que você selecionar. Como resultado, se você tiver 10 mensagens HTML no app de 1 MB cada, seus clientes incorrerão em 10 MB de cobranças de dados, mesmo que nunca tenham acionado todas essas mensagens. Isso pode se acumular rapidamente ao longo do tempo, mesmo que as mensagens no-app sejam armazenadas em cache e não sejam baixadas novamente de sessão para sessão.

As seguintes estratégias são úteis para manter o tamanho dos arquivos baixo:

- Referencie fontes incorporadas no seu aplicativo ou site para personalizar suas mensagens HTML no aplicativo em vez de incluir os arquivos de fontes na sua pasta ZIP de ativos HTML.
- Não pode haver nenhum CSS ou JavaScript extra ou duplicado nos ZIPs do ativos de HTML.
- Use [ImageOptim][25] em todas as imagens para comprimir as imagens ao seu tamanho mínimo possível sem redução na qualidade.

### especificações do iPhone 5

![Especificações do iPhone 5][18]

### especificações do iPhone 6

![Especificações do iPhone 6][19]


[18]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_05.png %}

[19]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_06.png %}

[25]: https://imageoptim.com/
