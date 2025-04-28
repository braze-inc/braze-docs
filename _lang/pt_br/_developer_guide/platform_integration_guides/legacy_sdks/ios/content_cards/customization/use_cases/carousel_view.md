---
nav_title: Visualização em carrossel
article_title: Visualização de carrossel de cartão de conteúdo para iOS
platform: iOS
page_order: 5
description: "Este artigo aborda como implementar um caso de uso de visualização de carrossel de cartão de conteúdo para aplicativos iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Caso de uso: Visualização do carrossel

![Exemplo de app de notícias mostrando o carrossel de cartões de conteúdo em um artigo.]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Esta seção aborda como implementar um feed de carrossel com vários cartões, em que o usuário pode deslizar horizontalmente para ver os cartões adicionais em destaque. Para integrar uma exibição de carrossel, você precisará usar uma implementação de cartão de conteúdo totalmente personalizado - a fase de "execução" da [abordagem crawl, walk, run]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches).

Com essa abordagem, você não usará as exibições do Braze e a lógica padrão, mas, em vez disso, exibirá os cartões de conteúdo de maneira totalmente personalizada, usando suas próprias exibições preenchidas com dados dos modelos do Braze.

Em termos de nível de esforço de desenvolvimento, as principais diferenças entre a implementação básica e a implementação do carrossel incluem:

- Criando suas próprias visualizações
- Registro da análise de dados do cartão de conteúdo
- Introdução de lógica adicional no lado do cliente para determinar quantos e quais cartões serão exibidos no carrossel

## Implementação

### Etapa 1: Criar um controlador de visualizações personalizado

Para criar o carrossel de cartões de conteúdo, crie seu próprio controlador de visualização personalizado (como `UICollectionViewController`) e [assine as atualizações de dados]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/#getting-the-data). Note que você não poderá estender ou criar uma subclasse do nosso `ABKContentCardTableViewController` padrão, pois ele só é capaz de lidar com nossos tipos de cartão de conteúdo padrão.

### Etapa 2: Implementar análise de dados

Ao criar um controlador de visualização totalmente personalizado, as impressões, os cliques e os descartes de cartão de conteúdo não são registrados automaticamente. É necessário implementar os respectivos métodos de análise de dados para garantir que as impressões, os eventos de demissão e os cliques sejam registrados corretamente na análise do dashboard do Braze.

Para obter informações sobre os métodos de análise de dados, consulte [Métodos de cartão]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/#card-methods). 

{% alert note %}
A mesma página também detalha as diferentes propriedades herdadas de nossa classe genérica de modelo de cartão de conteúdo, que podem ser úteis durante a implementação da visualização.
{% endalert %}

### Etapa 3: Criar um observador de cartão de conteúdo

Crie um [observador de cartão de]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/#step-2-set-up-a-content-card-listener) conteúdo que seja responsável por lidar com a chegada de cartões de conteúdo e implemente a lógica condicional para exibir um número específico de cartões no carrossel a qualquer momento. Por padrão, os cartões de conteúdo são classificados por data de criação (o mais recente primeiro), e o usuário vê todos os cartões para os quais é elegível.

Dito isso, você pode solicitar e aplicar lógica de exibição adicional de várias maneiras. Por exemplo, você pode selecionar os cinco primeiros objetos do cartão de conteúdo do vetor ou introduzir pares de valores-chave (a propriedade `extras` no modelo de dados) para criar uma lógica condicional.

Se estiver implementando um carrossel como um feed secundário de cartões de conteúdo, consulte [Uso de vários feeds de cartão de conteúdo]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/) para garantir que você classifique os cartões no feed correto com base em pares de valores-chave.

{% alert important %}
É importante garantir que as equipes de marketing e de desenvolvimento coordenem os pares de valores-chave que serão usados (por exemplo, `feed_type = brand_homepage`), pois todos os pares de valores-chave que os profissionais de marketing inserirem no dashboard do Braze devem corresponder exatamente aos pares de valores-chave que os desenvolvedores criam na lógica do app.
{% endalert %}

Para obter a documentação do desenvolvedor específica do iOS sobre a classe, os métodos e as atribuições dos cartões de conteúdo, consulte a referência de classe do iOS [`ABKContentCard`.](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html)

## Considerações

- Ao usar exibições totalmente personalizadas, você não poderá estender ou criar subclasses dos métodos usados em `ABKContentCardsController`. Em vez disso, você mesmo precisará integrar os métodos e as propriedades do modelo de dados.
- A lógica e a implementação da visualização de carrossel não são um tipo padrão de cartão de conteúdo no Braze e, portanto, a lógica para alcançar o caso de uso deve ser fornecida e suportada pela sua equipe de desenvolvimento.
- Você precisará implementar a lógica do lado do cliente para exibir um número específico de cartões no carrossel a qualquer momento.

