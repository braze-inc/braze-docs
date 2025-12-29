---
nav_title: Piloto de brasagem
page_order: 10.5
layout: dev_guide
guide_top_header: "Piloto de brasagem"
guide_top_text: "O Braze Pilot é um aplicativo móvel projetado para se conectar perfeitamente ao seu painel de controle Braze. Isso permite que você lance campanhas e Canvases no aplicativo, dando vida às mensagens do Braze em seu próprio telefone. O Braze Pilot inclui uma biblioteca de simulações de aplicativos para marcas fictícias que representam diferentes setores, permitindo que você experimente como suas mensagens podem parecer do ponto de vista de seus clientes."
description: "Confira as diferentes maneiras de usar o Braze para enviar mensagens do painel do Braze para o seu telefone."

guide_featured_title: "Artigos de seção"
guide_featured_list:
  - name: Primeiros passos com o Braze Pilot
    link: /docs/user_guide/getting_started/braze_pilot/getting_started/
    image: /assets/img/braze_icons/brush-02.svg
  - name: Dicionário de dados
    link: /docs/user_guide/getting_started/braze_pilot/data_dictionary/
    image: /assets/img/braze_icons/book-closed.svg
  - name: Links profundos
    link: /docs/user_guide/getting_started/braze_pilot/deep_links/
    image: /assets/img/braze_icons/link-03.svg

---

## Simulações de aplicativos piloto

O núcleo do Braze Pilot é sua biblioteca de simulações de aplicativos. Cada aplicativo é uma simulação realista de uma marca fictícia específica do setor, instrumentada para registrar uma rica variedade de eventos e atributos que criam infinitas oportunidades para potencializar os casos de uso comuns do Braze.

{% tabs local %}
{% tab Fitness %}

### Steppington

O Steppington é um aplicativo de condicionamento físico com exercícios, metas de exercícios e um serviço premium Steppington+. Ele oferece vários locais para demonstrar [os Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), uma seção que pode ser revelada com [sinalizadores de recursos]({{site.baseurl}}/developer_guide/feature_flags) e uma biblioteca robusta de registro de eventos personalizados que possibilitam ilustrar muitas jornadas de clientes para esse setor.

Página inicial da Steppington com ícones para treinamento de maratona, ioga, ciclismo e pesos.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### PantsLabyrinth

O PantsLabyrinth é um aplicativo de comércio eletrônico que vende (você adivinhou) calças! O aplicativo PantsLabyrinth inclui uma experiência completa de checkout com carrinho de compras, um recurso opcional de lista de desejos que pode ser ativado com um sinalizador de recurso e muitas oportunidades para piadas maliciosas com amigos do Reino Unido.

Uma página de produto da PantsLabyrinth com opções para adicionar jeans ao carrinho.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon 

O MovieCanon é um serviço de streaming perfeitamente projetado para ilustrar casos de uso comuns do Braze em relação ao envolvimento com o conteúdo. 

\![O aplicativo MovieCanon com diferentes thrillers para assistir.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## Como o Pilot se conecta ao seu painel de controle do Braze

O Braze SDK é um pacote de código que coleta dados dos seus usuários depois de integrado ao seu aplicativo ou site. Ao conectar o Pilot ao seu painel, você inicializa essa conexão entre o aplicativo Pilot no seu telefone e o SDK do Braze e estabelece uma conexão exclusiva com sua instância do Braze, fornecendo ao Pilot o identificador da chave da API do seu painel.

\![A primeira etapa da configuração do Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Depois que o Pilot se conectar ao seu painel do Braze, o SDK do Braze funcionará no aplicativo da mesma forma que quando você integrar o SDK ao seu próprio aplicativo ou site. Isso significa que o Braze irá:

- Armazene dados sobre a atividade do usuário no Pilot, incluindo dados personalizados específicos das marcas fictícias no aplicativo.
- Colete automaticamente dados da sessão, informações do dispositivo e tokens de envio.
- Notificações push de energia, mensagens no aplicativo e canais de mensagens do Content Card que exigem integração com o SDK para funcionar.

Para saber mais sobre o Braze SDK, confira [Integração]({{site.baseurl}}/user_guide/getting_started/integration).

A pilha de envolvimento do cliente Braze, que inclui integrações, APIs, SDKs para ingestão de dados, classificação, orquestração, personalização e ação com canais de mensagens para um ciclo de feedback interativo com seus clientes.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Perfis de usuário no Braze

Cada dado enviado ao Braze é armazenado em um perfil de usuário dedicado a um usuário específico do seu aplicativo ou site. Depois de conectar a Pilot ao seu painel do Braze, o Braze começará a registrar dados sobre você como usuário da Pilot. Há dois tipos de usuários que podem ser criados para você por meio dessa conexão: anônimos e identificados.

### Anônimo 

Esse status de conexão representa a experiência de um convidado do seu aplicativo ou site que ainda não fez login. Se você inicializar o Pilot como um usuário anônimo, o Braze criará um [perfil de usuário anônimo]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users) para você e registrará dados sobre sua atividade nesse perfil. Os usuários anônimos ainda podem ser direcionados com campanhas, mas você não poderá procurar o perfil de usuário deles diretamente no painel do Braze.

### Identificado

Esse status de conexão significa que a Braze reconhece seu perfil de usuário por meio de um identificador exclusivo atribuído a você, conhecido como identificador externo. Você pode pesquisar esse identificador externo na página **User Search (Pesquisa de usuário** ) do seu painel para localizar seu perfil de usuário, que armazenará todos os atributos de usuário e eventos registrados no Pilot com base em sua atividade no aplicativo.

\![Um exemplo de um perfil de usuário do Braze para o usuário "torchie-208117".]({% image_buster /assets/img/braze_pilot/user_profile.png %})

### Tipo de conexão

Para verificar que tipo de conexão você tem, verifique o status da conexão no canto superior direito da tela.

{% tabs local %}
{% tab Anonymous user  %}

**Anonymous** indica que você está registrando dados como um usuário anônimo.

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

Se você estiver registrando dados como um usuário identificado, um ícone de usuário será exibido ao lado da sua ID externa.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_identified_user.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Not connected %}

**Não conectado** indica que você ainda não inicializou a conexão do Braze SDK com o Pilot.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_not_connected.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Campanhas e telas

Campanhas e Canvases são a forma de enviar mensagens aos seus usuários. 

- As campanhas são melhores para mensagens únicas enviadas a um segmento de público específico em vários canais. 
- Canvases são fluxos de trabalho de campanha avançados que permitem automatizar e orquestrar jornadas personalizadas de clientes em vários canais. Em um Canvas, você pode configurar a lógica de ramificação, atrasos, pontos de decisão e eventos de conversão para orientar os clientes por meio de uma série de interações. As telas ajudam a garantir uma comunicação consistente e contínua em diferentes pontos de contato, aumentando as chances de envolvimento e conversão do cliente.

## Canais de mensagens compatíveis

Atualmente, o Braze Pilot oferece suporte a [mensagens no aplicativo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about), que aparecem no seu aplicativo, fornecendo mensagens oportunas enquanto o usuário está ativamente envolvido.

\![Uma mensagem no aplicativo MovieCanon "Está gostando do MovieCanon? Indique seus amigos!" com uma opção para inserir seu endereço de e-mail para enviar uma indicação.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}