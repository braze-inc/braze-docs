---
nav_title: Cartões de conteúdo
article_title: Cartões de conteúdo
page_order: 1
layout: dev_guide
guide_top_header: "Cartões de conteúdo"
guide_top_text: "Com os Content Cards, você pode enviar um fluxo dinâmico e altamente direcionado de conteúdo avançado para seus clientes nos aplicativos que eles adoram, sem interromper a experiência deles. <br><br>Os Content Cards são incorporados diretamente ao seu aplicativo ou site, permitindo que você crie caixas de entrada de mensagens e interfaces personalizadas que ampliam o alcance de outros canais, como e-mail ou notificações por push. Além disso, os Content Cards oferecem suporte a recursos mais personalizados, incluindo fixação de cartões, dispensa de cartões, entrega baseada em API, Connected Content, tempos de expiração de cartões personalizados, análise de cartões e fácil coordenação com notificações push. <br><br>**A disponibilidade dos cartões de conteúdo depende de seu pacote Braze. Entre em contato com seu gerente de conta ou gerente de sucesso do cliente para começar."
description: "Esta página de aterrissagem é a página inicial dos Cartões de Conteúdo Braze. Aqui, você encontra artigos sobre como criar um Content Card, como personalizar seus Content Cards, testes, relatórios e muito mais."
channel:
  - content cards
search_rank: 5
guide_featured_title: "Artigos de seção"
guide_featured_list:
- name: Criar um cartão de conteúdo
  link: /docs/user_guide/message_building_by_channel/content_cards/create/
  image: /assets/img/braze_icons/columns-01.svg
- name: Criação de cartões
  link: /docs/user_guide/message_building_by_channel/content_cards/create/card_creation
  image: /assets/img/braze_icons/message-check-circle.svg
- name: Detalhes criativos
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/
  image: /assets/img/braze_icons/brush-02.svg
- name: Testes
  link: /docs/user_guide/message_building_by_channel/content_cards/testing/
  image: /assets/img/braze_icons/beaker-02.svg
- name: Relatórios
  link: /docs/user_guide/message_building_by_channel/content_cards/reporting/
  image: /assets/img/braze_icons/pie-chart-01.svg
- name: Práticas recomendadas
  link: /docs/user_guide/message_building_by_channel/content_cards/best_practices
  image: /assets/img/braze_icons/check-square-broken.svg
---

## [![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} Benefícios do uso de Cartões de Conteúdo

Aqui estão apenas alguns benefícios do uso dos Content Cards em comparação com o fato de os desenvolvedores criarem conteúdo em seu aplicativo:

- **Segmentação e personalização mais fáceis:** Os dados de seus usuários residem no Braze, o que facilita a definição de seu público e a personalização de suas mensagens com os Content Cards.
- **Relatórios centralizados:** A análise do Content Card é rastreada no Braze, para que você tenha uma visão de todas as suas campanhas em um único local.
- **Jornadas do cliente coesas:** Você pode combinar os Content Cards com outros canais no Braze para criar experiências consistentes para o cliente. Um caso de uso popular é enviar uma notificação por push e, em seguida, salvar essa notificação como um Content Card em seu aplicativo para qualquer pessoa que não tenha se envolvido com o push. Se o conteúdo for incorporado diretamente ao seu aplicativo pelos desenvolvedores, ele ficará isolado do restante das mensagens.
- **Não é necessário fazer opt-in:** Semelhante às mensagens in-app, os Content Cards não exigem opt-in ou permissões de seus usuários. Mas, enquanto as mensagens no aplicativo não têm permissão e são de curta duração, os Content Cards não têm permissão e são permanentes. Isso significa que as estratégias de mensagens que combinam mensagens no aplicativo e Cartões de conteúdo atingem um ótimo equilíbrio.
- **Mais controle sobre a experiência de mensagens:** Embora você ainda precise da ajuda de seus desenvolvedores para a configuração inicial dos Content Cards, depois disso, você poderá controlar a mensagem, os destinatários, o tempo e muito mais diretamente do painel do Braze.

### Cartões de conteúdo em números

Como você, o profissional de marketing, está criando os cartões de conteúdo no Braze, pode fazer atualizações de mensagens e receber um retorno sobre o investimento sem precisar reformular completamente seu aplicativo ou site. Aqui estão algumas estatísticas úteis sobre o ROI dos cartões de conteúdo:

- Os cartões de conteúdo são **38 vezes** mais eficazes do que os e-mails para aumentar as vendas em um período de 72 horas.
- O uso de Content Cards em campanhas de registro de fidelidade aumenta as conversões em **5 vezes**.
- O envio de alcance aos usuários por meio de notificações push, mensagens no aplicativo e Content Cards resulta em **6,9 vezes** mais sessões, em comparação com os usuários engajados apenas por meio de push.
- O envio de alcance aos usuários por meio de e-mail, mensagens no aplicativo e Content Cards resulta em um tempo médio de vida do usuário **3,6 vezes** maior, em comparação com os usuários engajados apenas por e-mail.

## Como funciona

O Braze oferece diferentes tipos de Content Card para exibir o Content Card: Clássico, Imagem com legenda ou Imagem. Em sua essência, os Content Cards são, na verdade, uma carga útil de dados, e não a aparência dos dados. 

Agora, vamos nos aprofundar um pouco na parte técnica. Nos bastidores, há três partes principais de um Content Card:

- **Modelo:** Que tipo de dados estão no cartão
- **Ver:** Qual a aparência do cartão
- **Controlador:** Como o usuário interage com o cartão

Para uma implementação padrão, você adiciona o conteúdo do cartão - o modelo - a partir do painel ou por meio de APIs, e a exibição e o controlador são tratados pelo que é chamado de view controller. Um view controller é a "cola" entre o aplicativo geral e a tela.

## Casos de uso

Consulte esta seção para ver alguns casos de uso comuns dos Content Cards.

{% alert tip %}
Para obter mais inspiração, recomendamos que você consulte nosso [Guia de inspiração para cartões de conteúdo](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), que inclui mais de 20 campanhas personalizáveis, inclusive programas de indicação, lançamentos de novos produtos e renovações de assinaturas.
{% endalert %}

{% tabs %}
{% tab Onboarding and next steps %}

À medida que novos usuários exploram seu aplicativo e site, mostre a eles os valores e os benefícios do que você oferece com cartões de conteúdo estrategicamente posicionados. Incentive os usuários a optarem por outros canais de comunicação com um Content Card na sua página inicial e salve as tarefas de integração pendentes em uma guia de integração dedicada, alimentada por Content Cards. Não se esqueça de remover um cartão depois que o usuário concluir a tarefa desejada!

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_onboarding.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Event attendance %}

Exiba os Content Cards na parte superior da página inicial de um usuário para incentivar a participação em eventos, usando a segmentação por local para alcançar os usuários em potencial onde eles estiverem. Convidar os usuários para eventos físicos relevantes faz com que eles se sintam especiais, especialmente com mensagens personalizadas que aproveitam a atividade anterior deles com a sua marca.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_event.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Recommendations %}

Use os dados que você tem sobre o comportamento e as preferências dos usuários para exibir conteúdo relevante em tempo real na página inicial ou na caixa de entrada dos Content Cards e atraí-los de volta à sua oferta de produtos.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_recommendation.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Sales and promotions %}

Aproveite os Content Cards para destacar mensagens promocionais e ofertas não reclamadas diretamente em sua página inicial ou em uma caixa de entrada promocional dedicada. Extraia conteúdo relevante com base nas compras anteriores de cada cliente para oferecer promoções personalizadas que chamem a atenção.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_promo.png %}" style="border:0px">
</div>

{% endtab %}
{% endtabs %}

### Outros casos de uso

Além desses casos de uso principais, nossos clientes usam os Content Cards de muitas maneiras diferentes. O poder dos cartões de conteúdo é sua flexibilidade. Se o caso de uso desejado não for mostrado aqui, você poderá configurar [pares de valores-chave]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) e enviar as cargas para seu aplicativo ou site.

## Cartões de conteúdo em seu aplicativo

Esta seção aborda as maneiras mais comuns de colocar Content Cards no seu aplicativo ou site:

- [Caixa de entrada de mensagens](#message-inbox)
- [Carrossel](#carousel)

A lógica e a implementação desses posicionamentos não são padrão no Braze, portanto, sua equipe de engenharia deve fornecer e dar suporte ao trabalho para alcançar esses casos de uso. Para obter uma visão geral sobre como implementar esses posicionamentos, consulte [Criação de cartão de conteúdo personalizado]({{site.baseurl}}/developer_guide/content_cards/creating_cards/).

\![3 exemplos de cartões de conteúdo, mostrando as diferentes opções de posicionamento: caixa de entrada de mensagens, carrossel e banner.]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Caixa de entrada de mensagens

\![Um exemplo de cartão de conteúdo usando o posicionamento "caixa de entrada de mensagens".]({% image_buster /assets/img_archive/cc_placement_inbox.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Uma caixa de entrada de mensagens (também chamada de centro de notificações ou feed) é um local persistente em seu aplicativo ou site onde você pode exibir Content Cards no formato que preferir. Cada mensagem na caixa de entrada é seu próprio Content Card. 

A caixa de entrada de mensagens é uma implementação padrão com necessidade mínima de desenvolvimento. O Braze fornece um [view controller](#how-it-works) para uma caixa de entrada de mensagens no iOS, Android e na Web para facilitar o processo de criação.

#### Benefícios

- Os usuários podem receber muitos cartões em um só lugar
- Maneira eficiente de trazer à tona informações perdidas ou descartadas em outros canais (especialmente notificações push)
- Não é necessário optar por participar

#### Comportamento

Quando um usuário for elegível para um cartão, ele aparecerá automaticamente em sua caixa de entrada. Os Content Cards são criados para serem visualizados em massa, de modo que os usuários possam visualizar todos os cartões para os quais estão qualificados de uma só vez.

Com a implementação padrão, os Content Cards na caixa de entrada podem ser exibidos como cartões clássicos (contendo um título, texto e uma imagem opcional), somente de imagem ou de imagem com legenda. Você escolhe onde a caixa de entrada de mensagens ficará localizada em seu aplicativo.

Os Content Cards vêm com um estilo padrão, mas você pode escolher uma implementação personalizada para exibir os cartões e o feed de acordo com a aparência do seu aplicativo.

### Carrossel

\![Um exemplo de cartão de conteúdo usando o posicionamento "carrossel".]({% image_buster /assets/img_archive/cc_politer_carousel.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Os carrosséis exibem várias partes de conteúdo em um único espaço que seus clientes podem deslizar para visualizar. Eles podem ser uma apresentação de slides de imagens, texto, vídeo ou uma combinação deles. Essa é uma implementação personalizada e exige um pouco de trabalho de seus desenvolvedores.

#### Benefícios

- Os usuários podem receber muitos cartões em um só lugar
- Forma envolvente de apresentar recomendações

#### Comportamento

Quando um usuário for elegível para um cartão, ele aparecerá em um carrossel na página do seu aplicativo em que o carrossel for adicionado. Os usuários podem deslizar horizontalmente para visualizar cartões adicionais em destaque.

Como essa é uma implementação personalizada, você precisará trabalhar com seus desenvolvedores para criar suas próprias exibições para mostrar os Content Cards. Os cartões padrão clássico, somente de imagem e de imagem com legenda não são compatíveis com essa implementação.

## Integração de cartões de conteúdo

Seus desenvolvedores integrarão os Content Cards quando integrarem o Braze SDK. Para obter mais detalhes sobre como fazer a integração com os Content Cards, consulte os artigos do guia do desenvolvedor para sua plataforma:

- [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web)

## Fontes

<span></span>

[^1]: [8 dicas para tirar o máximo proveito de suas campanhas de retenção de clientes](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Relatório: A diferença do marketing entre canais](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)
