---
nav_title: Noções básicas de campanha
article_title: Noções básicas de campanha
page_order: 1
page_type: reference
description: "Este artigo de referência aborda os conceitos básicos de campanhas, incluindo várias perguntas que você deve fazer a si mesmo ao configurar suas primeiras campanhas."
tool: Campaigns

---

# Noções básicas de campanhas

> Este artigo de referência aborda os conceitos básicos de campanhas, incluindo várias perguntas que você deve fazer a si mesmo ao configurar suas primeiras campanhas.

## Compreensão da estrutura da campanha

Antes de começar com os detalhes mais minuciosos da configuração de campanhas, vamos identificar os principais detalhes para entender como as campanhas funcionam em diferentes canais de envio de mensagens.

As campanhas são uma etapa de mensagem única para se conectar aos seus usuários nos canais, ou mais comumente chamados de canais de envio de mensagens. Esses canais de envio de mensagens incluem cartões de conteúdo, e-mail, mensagens no app, push, SMS e MMS e webhooks. Ao entender onde seus clientes residem, você pode aproveitar os canais de envio de mensagens apropriados para se comunicar.

## Criação da jornada do cliente

Como as campanhas podem ser criadas de forma exclusiva, dependendo do canal de envio de mensagens, você pode usar esses cinco Ws da visualização para ajudar a identificar e conceituar suas estratégias e metas de engajamento do cliente.

### O "quê": Dê um nome à sua campanha

> O que você está tentando ajudar o usuário a fazer ou entender?

Nunca subestime o poder do nome. O Braze foi criado para a colaboração, portanto, este é um excelente momento para se preparar para a comunicação de metas com a sua equipe. Para saber mais sobre as jornadas do cliente, confira nosso curso do Braze Learning [Mapeamento dos ciclos de vida do usuário](https://learning.braze.com/mapping-customer-lifecycles)!

### O "quando": Criar condições iniciais

> Quando o cliente encontrará essa campanha? 

Os usuários podem entrar em sua campanha de três maneiras: em uma data e hora definidas (programada), quando realizam uma ação específica (baseada em ação) ou quando fazem algo que dispara uma chamada de API (acionada por API). 

A entrega programada envolve o ajuste de suas campanhas para envio em um horário específico e, opcionalmente, para uma cadência especificada. As campanhas baseadas em ações respondem a comportamentos específicos dos clientes à medida que eles ocorrem em tempo real. Isso pode incluir a realização de uma compra ou a interação com outra campanha. As campanhas acionadas por API podem ser configuradas para determinar as principais ações do cliente em sua plataforma que, quando realizadas, dispararão uma chamada de API para o Braze e enviarão suas campanhas.

### O "quem": Selecione um público de entrada

> Quem você está tentando alcançar? 

É possível usar [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments) predefinidos para direcionar os usuários com base em suas características e ações demográficas, comportamentais ou técnicas. Adicione mais filtros ao criar sua campanha para personalizar ainda mais seu segmento. Somente os usuários que correspondem a esses critérios de público-alvo podem entrar na jornada. Confira esta tabela para obter um resumo rápido dos tipos de filtros disponíveis.

| Filtrar | Descrição |
|---|---|
| Dados personalizados | Segmente os usuários com base em eventos e atribuições definidas por você. Pode usar recursos específicos de seu produto. |
| Atividade do usuário | Segmentar os clientes com base em suas ações e compras. |
| Redirecionamento | Segmente os clientes que foram enviados, receberam ou interagiram com campanhas anteriores. |
| Atividade de marketing | Segmente os clientes com base em comportamentos universais, como o último engajamento ou campanhas recebidas. |
| Atributos do usuário | Segmentar os clientes por seus atributos e características constantes. |
| Instalar atribuição | Segmente os clientes por sua primeira fonte, grupo de anúncios, campanha ou anúncio. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### O "porquê": Identificar eventos de conversão

> Por que você está criando essa campanha? 

É sempre importante ter uma meta definida em mente, e as campanhas o ajudam a entender sua performance em relação aos KPIs, como engajamento em sessões, compras e eventos personalizados. A seleção de pelo menos um [evento de conversão]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/) permitirá que você entenda a performance de sua campanha.

### O "onde": Encontrar meu público

> Onde posso alcançar melhor meu público?

É aqui que determinamos quais canais de envio de mensagens fazem mais sentido para a jornada do usuário. O ideal é alcançar os usuários onde eles estão mais ativos.

### O "como": Crie a experiência

> Como faço para criar minha campanha depois de identificar os cinco Ws?

Considere a possibilidade de configurar variantes e Testes A/B à medida que você se tornar mais experiente na criação de campanhas. Note que as campanhas suportam até oito variantes com um grupo de controle. Use a análise de dados de sua campanha para fazer escolhas informadas à medida que cria sua campanha, ajustando qualquer coisa, desde seu público segmentado até o conteúdo real do envio de mensagens.

