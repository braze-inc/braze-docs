---
nav_title: Braze Pilot
page_order: 10.5
layout: dev_guide
guide_top_header: "Braze Pilot"
guide_top_text: "Braze Pilot é um aplicativo móvel projetado para se conectar perfeitamente ao seu painel do Braze. Isso permite que você lance campanhas e Canvases para o aplicativo, trazendo mensagens do Braze à vida no seu próprio telefone. O Braze Pilot inclui uma biblioteca de simulações de aplicativos para marcas fictícias representando diferentes indústrias, permitindo que você experimente como suas mensagens podem parecer do ponto de vista de seus clientes."
description: "Confira as diferentes maneiras de usar o Braze para lançar mensagens do painel do Braze para o seu telefone."

guide_featured_title: "Artigos de seção"
guide_featured_list:
  - name: Introdução ao Braze Pilot
    link: /docs/user_guide/getting_started/braze_pilot/getting_started/
    image: /assets/img/braze_icons/brush-02.svg
  - name: Dicionário de Dados
    link: /docs/user_guide/getting_started/braze_pilot/data_dictionary/
    image: /assets/img/braze_icons/book-closed.svg
  - name: Deep links
    link: /docs/user_guide/getting_started/braze_pilot/deep_links/
    image: /assets/img/braze_icons/link-03.svg

---

## Simulações de aplicativos do Pilot

O núcleo do Braze Pilot é sua biblioteca de simulações de aplicativos. Cada aplicativo é uma simulação realista de uma marca fictícia específica do setor, instrumentada para registrar uma rica variedade de eventos e atributos que criam oportunidades infinitas para impulsionar casos de uso comuns do Braze.

{% tabs local %}
{% tab Fitness %}

### Steppington

Steppington é um aplicativo de fitness com treinos, metas de exercícios e um serviço premium Steppington+. Oferece vários lugares para demonstrar [Cartões de Conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), uma seção que pode ser revelada com [feature flags]({{site.baseurl}}/developer_guide/feature_flags), e uma robusta biblioteca de registro de eventos personalizados que torna possível ilustrar muitas jornadas de clientes para esta indústria.

![A página inicial do Steppington com ícones para treinamento de maratona, yoga, ciclismo e pesos.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### Pants Labyrinth

PantsLabyrinth é um aplicativo de eCommerce que vende (você adivinhou) calças! O aplicativo PantsLabyrinth inclui uma experiência completa de checkout de carrinho de compras, um recurso de lista de desejos opcional que pode ser ativado com uma feature flag, e muitas oportunidades para piadas sutis com amigos do Reino Unido.

![Uma página de produto para PantsLabyrinth com opções para adicionar jeans ao carrinho.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon 

MovieCanon é um serviço de streaming perfeitamente projetado para ilustrar casos de uso comuns do Braze em torno do engajamento de conteúdo. 

![O aplicativo MovieCanon com diferentes thrillers para assistir.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## Como o Pilot se conecta ao seu painel do Braze

O SDK do Braze é um pacote de código que coleta dados de seus usuários uma vez que está integrado ao seu aplicativo ou site. Quando você conecta o Pilot ao seu dashboard, você inicializa essa conexão entre o aplicativo Pilot no seu telefone e o SDK Braze, e estabelece uma conexão única com sua instância Braze ao fornecer ao Pilot seu identificador de chave de API para seu dashboard.

![A primeira etapa de configurar o Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Depois que o Pilot se conecta ao seu dashboard Braze, o SDK Braze funciona no aplicativo exatamente como funcionará uma vez que você integre o SDK com seu próprio aplicativo ou site. Isso significa que o Braze irá:

- Armazenar dados sobre a atividade do usuário no Pilot, incluindo dados personalizados específicos das marcas fictícias no aplicativo.
- Coletar automaticamente dados de sessão, informações do dispositivo e tokens de push.
- Potencializar notificações por push, mensagens no aplicativo e canais de mensagens de Cartão de Conteúdo que requerem integração de SDK para funcionar.

Para mais informações sobre o SDK Braze, confira [Integração]({{site.baseurl}}/user_guide/getting_started/integration).

![A pilha de engajamento do cliente Braze, que inclui integrações, APIs, SDKs para ingestão de dados, classificação, orquestração, personalização e ação com canais de mensagens para um loop de feedback interativo com seus clientes.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Perfis de usuário no Braze

Cada pedaço de dado enviado ao Braze é armazenado em um perfil de usuário dedicado a um usuário específico do seu aplicativo ou site. Uma vez que você conecta o Pilot ao seu dashboard Braze, o Braze começará a registrar dados sobre você como usuário do Pilot. Existem dois tipos de usuários que podem ser criados para você através dessa conexão: anônimo e identificado.

### Anônimo 

Esse status de conexão representa a experiência de um convidado do seu aplicativo ou site que ainda não fez login. Se você inicializar o Pilot como um usuário anônimo, o Braze cria um [perfil de usuário anônimo]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users) para você e registra dados sobre sua atividade lá. Usuários anônimos ainda podem ser segmentados em campanhas, mas você não poderá consultar seu perfil de usuário diretamente no seu dashboard Braze.

### Identificado

Esse status de conexão significa que o Braze reconhece seu perfil de usuário através de um identificador único atribuído a você, conhecido como identificador externo. Você pode procurar por esse identificador externo na página **Pesquisa de Usuário** do seu dashboard para localizar seu perfil de usuário, que armazenará todos os atributos e eventos do usuário registrados a partir do Pilot com base na sua atividade no aplicativo.

![Um exemplo de um perfil de usuário Braze para o usuário "torchie-208117".]({% image_buster /assets/img/braze_pilot/user_profile.png %})

### Tipo de conexão

Para verificar que tipo de conexão você tem, você pode verificar o status da conexão no canto superior direito da sua tela.

{% tabs local %}
{% tab Anonymous user  %}

**Anônimo** indica que você está registrando dados como um usuário anônimo.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_anonymous.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Identified user %}

Se você estiver registrando dados como um usuário identificado, um ícone de usuário será exibido ao lado do seu ID externo.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_identified_user.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Not connected %}

**Não conectado** indica que você ainda não inicializou a conexão do SDK Braze com o Pilot.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_not_connected.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Campanhas e canvas

Campanhas e Canvas são a forma de envio de mensagens aos seus usuários. 

- As campanhas são melhores para mensagens únicas enviadas a um segmento específico de mensagens em vários canais. 
- As telas são fluxos de trabalho de campanha avançados que permitem automatizar e orquestrar jornadas personalizadas de clientes em vários canais. Em um Canva, você pode configurar lógica de ramificação, postergações, pontos de decisão e eventos de conversão para orientar os clientes em uma série de interações. Os canvases ajudam a garantir uma comunicação consistente e contínua em diferentes pontos de contato, aumentando as chances de engajamento e conversão do cliente.

## Canais de envio de mensagens suportados

O Braze Pilot atualmente suporta [mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about), que aparecem no seu app, entregando mensagens oportunas enquanto o usuário está ativamente engajado.

![Uma mensagem no app no aplicativo MovieCanon "Aproveitando o MovieCanon? Indique seus amigos!" com uma opção para inserir seu endereço de e-mail para enviar uma referência.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}