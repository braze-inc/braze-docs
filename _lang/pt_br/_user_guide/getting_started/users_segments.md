---
nav_title: Usuários e segmentos
article_title: "Primeiros passos: Usuários e segmentos"
page_order: 2
page_type: reference
description: "Este artigo fornece uma visão geral dos usuários e segmentos, descrevendo sua importância e como eles podem ser aproveitados para envolver seu público."

---

# Primeiros passos: Usuários e segmentos

Entender seus usuários e segmentá-los de forma eficaz é fundamental para enviar campanhas de marketing personalizadas e direcionadas. Este artigo fornece uma visão geral dos usuários e segmentos, descrevendo sua importância e como eles podem ser aproveitados para envolver seu público.

## Usuários

No Braze, as informações sobre o seu público são armazenadas em perfis de usuário. Um [perfil de usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) é uma coleção abrangente de informações e atributos que descrevem um consumidor individual. Ele serve como um repositório central para armazenar e gerenciar dados relacionados ao comportamento, às preferências e aos detalhes demográficos dos usuários.

### Partes de um perfil de usuário

Ao entender os perfis dos usuários, você pode obter insights sobre o seu público e interagir com eles de forma personalizada e direcionada. O perfil de um usuário contém muitas informações, mas aqui estão algumas das partes principais:

- **Identificador de usuário:** Cada perfil de usuário é identificado exclusivamente por um ID de usuário, chamado `external_id`. Esse identificador permite que o Braze rastreie e associe os dados do usuário em diferentes canais e dispositivos, fornecendo uma visão unificada das interações de cada usuário com a sua marca. [Os perfis de usuários anônimos]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) (usuários que visitam seu site ou aplicativo sem fazer login) não têm um `external_id`, mas podem receber [aliases de usuário]({{site.baseurl}}/user_guide/data/user_data_collection/anonymous_users/#assigning-user-aliases) como um identificador alternativo.
- [Atributos](#attributes)**:** Essas são informações específicas sobre o usuário, como nome, idade, local ou qualquer outra informação demográfica. Você pode usar esses atributos para segmentar seu público e personalizar suas mensagens.
- [Eventos](#events)**:** Essas são ações que o usuário realiza, como fazer uma compra, clicar em um link ou abrir um aplicativo. O Braze rastreia esses eventos para ajudá-lo a entender o comportamento e o envolvimento do usuário. Da mesma forma que os atributos, você também pode usar eventos para segmentar e personalizar.
- **Compras:** Essa seção registra o histórico de compras do usuário. Isso é fundamental para entender os hábitos e as preferências de compra do usuário.
- **Dispositivos:** Essa seção lista os dispositivos que o usuário usou para interagir com a sua marca. Pode incluir dispositivos móveis, navegadores da Web e dispositivos conectados (como wearables e smart TVs).
- **Compromisso:** Essa seção contém informações sobre as interações do usuário com as mensagens que você envia a ele, a quais segmentos ele pertence, o status da assinatura e muito mais.
- **Histórico de mensagens:** Esse é um registro de todas as mensagens que foram enviadas ao usuário pelo respectivo canal de mensagens (como e-mail ou push).

{% alert tip %}
Os SDKs da plataforma Braze coletam automaticamente 27 atributos e eventos diferentes. Usando esses eventos e atributos padrão, você pode criar segmentos assim que integrar o SDK.
{% endalert %}

### Atributos

Os atributos são características ou propriedades específicas associadas a um usuário. Esses atributos ajudam a segmentar e direcionar os usuários com base em suas características e interesses exclusivos. Há dois tipos de atributos no Braze: atributos padrão e atributos personalizados.

#### Atributos padrão

Atributos padrão são atributos predefinidos que você pode rastrear com o Braze depois de integrar o SDK ao seu aplicativo. São partes comuns de informações do usuário que a maioria dos aplicativos consideraria úteis, como dados demográficos e do dispositivo. Os exemplos incluem:

- Primeiro nome
- Sobrenome
- E-mail
- Gênero
- Data de nascimento
- País
- Cidade
- Último aplicativo usado
- Idioma
- Fuso horário

#### Atributos personalizados

[Atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) são atributos que você define com base em suas necessidades comerciais específicas. Eles permitem que você rastreie informações exclusivas do seu aplicativo ou negócio. 

Por exemplo, um aplicativo de streaming de música pode rastrear atributos personalizados como:

- Gênero favorito
- Número de músicas tocadas
- Assinante Premium (Sim/Não)
- Artista favorito

Um aplicativo de varejo, por outro lado, pode rastrear atributos personalizados como:

- Tamanho de roupa preferido
- Marca favorita
- Número de compras
- Membro do programa de fidelidade (Sim/Não)

Os atributos personalizados lhe dão a flexibilidade de coletar e analisar os dados mais relevantes para sua empresa. No entanto, eles exigem uma configuração adicional.

Os atributos padrão e personalizados podem ser usados para segmentar seu público e personalizar suas mensagens de marketing. Por exemplo, você pode enviar uma oferta especial para usuários de uma determinada cidade (atributo padrão) que tenham feito mais de 10 compras (atributo personalizado).

### Eventos

Os eventos representam ações ou comportamentos específicos realizados pelos usuários em seu aplicativo ou site. Exemplos de eventos podem incluir lançamentos de aplicativos, compras, visualizações de conteúdo ou qualquer outra ação. Ao rastrear e analisar esses eventos, você pode obter insights sobre o comportamento do usuário e os padrões de envolvimento.

#### Eventos padrão

[Os eventos padrão]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/events#standard-events) são eventos predefinidos que o Braze rastreia automaticamente depois que o SDK é integrado ao seu aplicativo ou site. Alguns exemplos de eventos padrão incluem:

- **Início da sessão:** Esse evento é acionado quando um usuário abre o aplicativo.
- **Fim da sessão:** Esse evento é acionado quando um usuário fecha o aplicativo.
- **Compra:** Esse evento é acionado quando um usuário faz uma compra no aplicativo.
- **Clique na notificação por push:** Esse evento é acionado quando um usuário clica em uma notificação por push.

#### Eventos personalizados

[Eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) são eventos que você define com base nas ações específicas que deseja rastrear em seu aplicativo ou site. Por exemplo, um aplicativo de streaming de música pode rastrear eventos personalizados como:

- Música tocada
- Lista de reprodução criada
- Anúncio pulado

Um aplicativo de condicionamento físico, por outro lado, pode rastrear eventos personalizados, como:

- Início do treino
- Treino concluído
- Estabelecimento de recorde pessoal

Os eventos personalizados oferecem a flexibilidade de rastrear as ações mais relevantes para o seu aplicativo e negócio. Entretanto, assim como os atributos personalizados, eles exigem configuração adicional.

### Pontos de dados

O Braze usa pontos de dados para ajudá-lo a definir as informações mais impactantes para sua empresa. Os pontos de dados são uma parte crucial da operação do Braze e são usados para faturamento, preços e, o mais importante, para personalizar e otimizar suas campanhas de marketing.

Os pontos de dados são consumidos quando os dados do perfil de um usuário são atualizados ou quando ele executa ações específicas. Essas ações podem incluir iniciar uma sessão, encerrar uma sessão, registrar um evento personalizado ou fazer uma compra. É importante observar que nem todos os dados coletados pelo Braze contam como pontos de dados. Por exemplo, os dados e eventos coletados por padrão pelos Serviços Braze, como tokens push, informações do dispositivo e todos os eventos de rastreamento de engajamento de campanha, como aberturas de e-mail e cliques em notificações push, não são contados como pontos de dados.

Ao considerar cuidadosamente quais informações devem ser rastreadas como pontos de dados, você estará direcionando os dados de maior impacto para a experiência dos seus usuários. Seu gerente de conta Braze ajudará a recomendar as práticas recomendadas de dados para atender às suas necessidades.

Acesse nosso artigo específico para saber mais sobre [pontos de dados]({{site.baseurl}}/user_guide/data/data_points/).

## Segmentos

[A segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments) permite que você direcione os usuários com base em suas características e ações demográficas, comportamentais, sociais ou técnicas (ou seja, atributos e eventos). O uso criativo e inteligente da segmentação e da automação de mensagens permite que você mova perfeitamente seus usuários pela jornada do ciclo de vida do cliente.

Dicas para trabalhar com segmentos:

- Os segmentos no Braze são dinâmicos: os usuários estão sempre entrando e saindo dos segmentos, pois nem sempre se encaixam nos critérios. Os usuários que se enquadram nos critérios de um segmento no momento do envio serão os destinatários dessa campanha ou Canvas.
    - Se quiser que seu segmento seja estático, você pode usar Segment Extensions (Extensões de segmento). As Extensões de Segmento (com a [regeneração desativada]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#extension-regeneration)) representam seu público-alvo como um único instantâneo no tempo.
- Você não está limitado a usar um filtro de cada vez. Crie segmentos granulares com ajuste fino, colocando vários filtros em camadas.
- Você pode usar as ações ou não ações dos seus usuários para entender como alcançá-los onde eles querem se envolver com você. Essas ações podem ser eventos personalizados, envolvimento com uma campanha ou Canvas existente ou até mesmo uma mensagem específica em um Canvas.

### Caso de uso

Suponha que você administre uma loja de roupas on-line e tenha configurado um fluxo de mensagens para enviar uma série de e-mails aos usuários que adicionaram um item ao carrinho, mas não concluíram a compra. Esse fluxo de carrinho abandonado pode incluir um e-mail de lembrete inicial, um e-mail de acompanhamento oferecendo um desconto e um e-mail de lembrete final.

\![]({% image_buster /assets/img/getting_started/segment_example.png %}){: style="max-width:70%" }

Você poderia criar um segmento de usuários que acionaram o evento personalizado "Item adicionado ao carrinho", mas não acionaram o evento personalizado "Compra concluída". Em seguida, nesse segmento, você poderia identificar ainda mais os usuários que abriram o e-mail de lembrete inicial (envolvimento com uma mensagem específica), mas não fizeram uma compra.

\![]({% image_buster /assets/img/getting_started/segment_example_breakdown.png %})

Esse segmento poderia ser alvo de uma campanha mais agressiva para tentar converter esses usuários em compradores. Por exemplo, você pode enviar a eles uma oferta especial ou uma recomendação personalizada com base nos itens do carrinho.

Esse é apenas um exemplo de como você pode usar ações e inações do usuário, eventos personalizados e dados de envolvimento para criar segmentos e adaptar suas estratégias de marketing no Braze.

