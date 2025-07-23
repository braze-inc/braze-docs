---
nav_title: Sobre Cartões de Conteúdo
article_title: Sobre Cartões de Conteúdo
page_order: 0
description: "Este artigo de referência fornece uma visão geral do canal de cartão de conteúdo da Braze e casos de uso comuns."
channel:
  - content cards
search_rank: 4
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} Sobre Cartões de Conteúdo

> Os cartões de conteúdo são incorporados diretamente ao seu app ou site para que você possa engajar os usuários com uma experiência que pareça natural e perfeita. Eles oferecem mais controle sobre a experiência do app ou do site e permitem criar caixas de entrada de mensagens, carrosséis e banners, além de ampliar o alcance de outros canais (como e-mail ou notificações por push).

Os Cartões de Conteúdo são um recurso adicional e devem ser adquiridos. Para começar com os Cartões de Conteúdo, entre em contato com seu gerente de sucesso do cliente da Braze ou com nossa equipe de suporte.

{% alert note %}
Se você estiver usando nossa ferramenta de feed de notícias, recomendamos que você mude para o nosso canal de envio de mensagens Content Cards—é mais flexível, personalizável e confiável. O Feed de notícias também está sendo descontinuado. Veja nosso [Guia de Migração]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) ou entre em contato com seu gerente de conta da Braze para saber mais.
{% endalert %}

## Benefícios do uso de cartões de conteúdo

Aqui estão apenas alguns benefícios do uso de cartões de conteúdo em comparação com o fato de seus desenvolvedores criarem conteúdo em seu app:

- **Segmentação e personalização mais fáceis:** Seus dados de usuários vivem na Braze, facilitando a definição do seu público e a personalização de suas mensagens com Content Cards.
- **Relatórios centralizados:** A análise de dados do cartão de conteúdo é rastreada no Braze, para que você tenha insight sobre todas as suas campanhas em um único local.
- **Jornadas coesas do cliente:** Você pode combinar Cartões de Conteúdo com outros canais no Braze para criar experiências consistentes para os clientes. Um caso de uso popular é enviar uma notificação por push, depois salvar essa notificação como um cartão de conteúdo no seu app para qualquer pessoa que não interagiu com o push. Se o conteúdo for incorporado diretamente ao app pelos desenvolvedores, ele ficará isolado do restante das mensagens.
- **Não há necessidade de aceitação:** Semelhante às mensagens no app, os Cartões de Conteúdo não requerem aceitação ou permissões dos seus usuários. Mas, enquanto as mensagens no app não têm permissão e são de curta duração, os cartões de conteúdo não têm permissão e são permanentes. Isso significa que as estratégias de envio de mensagens que combinam mensagens no app e cartões de conteúdo atingem um ótimo equilíbrio.
- **Mais controle sobre a experiência de mensagens:** Embora ainda seja necessário que seus desenvolvedores ajudem na configuração inicial dos cartões de conteúdo, depois disso, você poderá controlar a mensagem, os destinatários, o tempo e muito mais diretamente do seu dashboard do Braze.

### Cartões de Conteúdo pelos números

Como você, o profissional de marketing, está criando os cartões de conteúdo no Braze, pode fazer atualizações de mensagens e receber um retorno sobre o investimento sem precisar reformular completamente seu app ou site. Aqui estão algumas estatísticas úteis sobre o ROI dos cartões de conteúdo:

- Os cartões de conteúdo são **38x** mais eficazes do que os e-mails para aumentar as vendas em um período de 72 horas.[^1]
- Usar Cartões de Conteúdo em campanhas de inscrição de fidelidade aumenta as conversões em **5X**.[^1]
- O envio de alcance aos usuários por meio de notificações por push, mensagens no app e cartões de conteúdo resulta em **6,9 vezes** mais sessões, em comparação com usuários engajados apenas por push.[^2]
- O envio de e-mail, mensagens no app e cartões de conteúdo para os usuários resulta em um tempo médio de vida **3,6 vezes** maior, em comparação com os usuários engajados apenas por e-mail.[^2]

## Como funciona?

No seu núcleo, os cartões de conteúdo são na verdade uma carga útil de dados, não como os dados se parecem. A Braze fornece visualizações de modelo (banner, modal, imagem legendada) para exibir os dados do cartão de conteúdo, que é, em última análise, a aparência da sua mensagem.

Agora vamos ficar um pouco técnicos. Nos bastidores, há três partes principais de um cartão de conteúdo:

- **Modelo:** Que tipo de dados vive no cartão
- **Visualizar:** Como é o cartão
- **Controlador:** Como o usuário interage com o cartão

Para uma implementação padrão, você adiciona o conteúdo do cartão - o modelo - a partir do dashboard ou por meio de APIs, e a visualização e o controlador são tratados pelo que é chamado de view controller. Um controlador de visualização é a "cola" entre o aplicativo geral e a tela.

## Casos de uso

Consulte esta seção para ver alguns casos de uso comuns de cartões de conteúdo.

{% alert tip %}
Para obter mais inspiração, recomendamos que você consulte nosso [Guia de inspiração de cartões de conteúdo](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide), que inclui mais de 20 campanhas personalizáveis, inclusive programas de indicação, lançamentos de novos produtos e renovações de inscrição.
{% endalert %}

{% tabs %}
{% tab integração e próximos passos %}

À medida que novos usuários exploram seu app e site, mostre a eles os valores e os benefícios do que você oferece com cartões de conteúdo estrategicamente posicionados. Incentive os usuários a aceitar outros canais de comunicação com um cartão de conteúdo em sua página inicial e salve as tarefas de integração pendentes em uma guia de integração dedicada, alimentada por cartões de conteúdo. Não se esqueça de remover um cartão depois que o usuário concluir a tarefa desejada!

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_onboarding.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Participação no evento %}

Exiba os cartões de conteúdo na parte superior da página inicial do usuário para incentivar a participação em eventos, usando o direcionamento local para alcançar os usuários em potencial onde eles estiverem. Convidar usuários para eventos físicos relevantes faz com que se sintam especiais, especialmente com envio de mensagens personalizadas que aproveitam suas atividades anteriores com sua marca.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_event.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Recomendações %}

Use os dados que você tem sobre comportamentos e preferências dos usuários para exibir conteúdo relevante em tempo real a partir da página inicial ou dos Cartões de Conteúdo da caixa de entrada e atraí-los de volta para sua oferta de produtos.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_recommendation.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Vendas e promoções %}

Aproveite os Cartões de Conteúdo para destacar mensagens promocionais e ofertas não reivindicadas diretamente na sua página inicial ou em uma caixa de entrada promocional dedicada. Puxe conteúdo relevante com base nas compras anteriores de cada cliente para oferecer promoções personalizadas que chamem a atenção.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_promo.png %}" style="border:0px">
</div>

{% endtab %}
{% endtabs %}

### Outros casos de uso

Fora desses principais casos de uso, nossos clientes usam os Cartões de Conteúdo de muitas maneiras diferentes. O poder dos Cartões de Conteúdo é a sua flexibilidade. Se o caso de uso desejado não for mostrado aqui, você poderá configurar [pares de valores-chave]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) e enviar as cargas úteis para seu app ou site.

## posicionamentos de cartão de conteúdo

Esta seção aborda as três maneiras mais comuns de colocar cartões de conteúdo no seu app ou site:

- [Caixa de entrada de mensagens](#message-inbox)
- [Carrossel](#carousel)
- [Banner](#banner)

A lógica e a implementação desses posicionamentos não são padrão no Braze, portanto, sua equipe de engenharia deve fornecer e apoiar o trabalho para alcançar esses casos de uso. Para obter uma visão geral sobre como implementar esses posicionamentos, consulte [Criação de cartão de conteúdo personalizado]({{site.baseurl}}/developer_guide/content_cards/creating_cards/).

![3 exemplos de cartões de conteúdo de conteúdo, mostrando as diferentes opções de posicionamento: caixa de entrada de mensagens, carrossel e banner.]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Caixa de entrada de mensagens

![Um exemplo de cartão de conteúdo usando o posicionamento da "caixa de entrada de mensagens".]({% image_buster /assets/img_archive/cc_placement_inbox.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Uma caixa de entrada de mensagens (também chamada de central de notificações ou feed) é um local persistente em seu app ou site onde você pode exibir Cartões de Conteúdo no formato que preferir. Cada mensagem na caixa de entrada é seu próprio cartão de conteúdo. 

A caixa de entrada de mensagens é uma implementação padrão com necessidade mínima de desenvolvimento. O Braze fornece um [view controller](#how-it-works) para uma caixa de entrada de mensagens no iOS, no Android e na Internet para facilitar o processo de criação.

#### Benefícios

- Os usuários podem receber muitos cartões em um só lugar
- Maneira eficiente de trazer à tona informações perdidas ou descartadas em outros canais (especialmente notificações por push)
- Nenhuma aceitação necessária

#### Comportamento

Quando um usuário é elegível para um cartão, ele aparecerá automaticamente na sua caixa de entrada. Os cartões de conteúdo são criados para serem visualizados em massa, para que os usuários possam visualizar todos os cartões para os quais são elegíveis de uma só vez.

Com a implementação padrão, os cartões de conteúdo na caixa de entrada podem aparecer como clássicos (contendo um título, texto e uma imagem opcional), apenas imagem ou cartões de imagem legendados. Você escolhe onde a caixa de entrada de mensagens estará localizada no seu app.

Os Cartões de Conteúdo vêm com um estilo padrão, mas você pode escolher uma implementação personalizada para exibir os cartões e o feed de acordo com a aparência do seu app.

### Carrossel

![Um exemplo de cartão de conteúdo usando o posicionamento "carrossel".]({% image_buster /assets/img_archive/cc_politer_carousel.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Os carrosséis exibem várias peças de conteúdo em um único espaço que seus clientes podem deslizar para ver. Eles podem ser uma apresentação de slides de imagens, texto, vídeo ou uma combinação deles. Esta é uma implementação personalizada e requer um pouco de trabalho dos seus desenvolvedores.

#### Benefícios

- Os usuários podem receber muitos cartões em um só lugar
- Maneira envolvente de apresentar recomendações

#### Comportamento

Quando um usuário é elegível para um cartão, ele aparecerá em um carrossel em qualquer página do seu app em que o carrossel for adicionado. Os usuários podem deslizar horizontalmente para ver cartões adicionais em destaque.

Como esta é uma implementação personalizada, você precisará trabalhar com seus desenvolvedores para criar suas próprias visualizações para exibir os Cartões de Conteúdo. Os cartões padrão clássico, somente de imagem e de imagem com legenda não são compatíveis com essa implementação.

### Banner

![Um exemplo de cartão de conteúdo de banner.]({% image_buster /assets/img_archive/cc_placement_banner.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

Os Cartões de Conteúdo podem aparecer como um banner dinâmico que é exibido de forma persistente na sua página inicial ou no topo de outras páginas designadas.

#### Benefícios

- Permanece na página ao contrário de uma mensagem no app, então você tem mais tempo para alcançar seu público
- Ótima maneira de exibir novo conteúdo em um local de destaque na sua página inicial

#### Comportamento

Os usuários podem visualizar e interagir com o conteúdo mais relevante para o qual são elegíveis. Como esta é uma implementação personalizada, você precisará trabalhar com seus desenvolvedores para personalizar as visualizações para exibir os Cartões de Conteúdo.

## Integrando Cartões de Conteúdo

Seus desenvolvedores irão integrar os Cartões de Conteúdo quando integrarem o SDK da Braze. Para mais detalhes sobre como integrar com os cartões de conteúdo, consulte os artigos do guia do desenvolvedor para sua plataforma:

- []({{site.baseurl}}/developer_guide/platforms/swift/content_cards/ "Guia de Integração de Cartão de Conteúdo do iOS")
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/ "Guia de Integração do Cartão de Conteúdo do Android")
- []({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/ "Guia de Integração de Cartão de Conteúdo da Web")

## Fontes

<span></span>

[^1]: [Dicas para aproveitar ao máximo suas campanhas de retenção de clientes](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [Relatório: A Diferença do Marketing Multicanal](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)