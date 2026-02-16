---
nav_title: Conectar fontes de dados
article_title: Conectar fontes de dados
page_order: 1
description: "Saiba como o BrazeAI Decisioning Studio Acessa os dados de seus clientes por meio de sua plataforma de engajamento com clientes."
---

# Conectar fontes de dados

> O BrazeAI Decisioning Studio™ Acessa os dados de seus clientes por meio de sua plataforma de engajamento com clientes (CEP). Este artigo explica quais dados são usados e como a conexão funciona.

## Como o Acessar acessa os dados de clientes

Ao contrário do Decisioning Studio Pro, que suporta integrações diretas de dados com várias fontes, o Decisioning Studio Acessa os dados de clientes por meio do CEP. Isso significa que:

- **Os dados do público** são extraídos diretamente de segmentos ou listas definidas em seu CEP (Braze, Salesforce Marketing Cloud ou Klaviyo) e só podem incluir determinadas atribuições predefinidas (não dados 1P)
- **Os dados de engajamento** (aberturas, cliques, envios) são capturados por meio de consultas automatizadas ou integrações nativas com seu CEP
- **Não** é necessária **nenhuma configuração adicional de pipeline de dados** além do que você configura em seu CEP

## Padrões de integração suportados

O Decisioning Studio Acessa os seguintes CEPs para acesso a dados:

| CEP | Fonte do público | Dados de engajamento |
|-----|-----------------|-----------------|
| **Braze** | Segmentos | Exportação de Braze Currents |
| **Salesforce Marketing Cloud** | Extensões de dados | Automação de consultas de SQL |
| **Klaviyo** | Segmentos | Integração de API nativa |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Requisitos de dados do CEP

{% tabs %}
{% tab Braze %}

### Requisitos de dados do Braze

Para as integrações do Braze, o Decisioning Studio Acessar requer:

1. **Braze Currents**: Você deve ter o Braze Currents ativado e configurado para exportar dados de engajamento para o Decisioning Studio Acessar. Isso permite que o agente aprenda com as respostas do cliente.

2. **Acesso ao segmento**: A chave de API criada deve ter permissões para acessar segmentos que definem seu público-alvo.

3. **Dados de perfil de usuários**: Todos os atributos de perfil de usuário ou atributos personalizados que você deseja que o agente considere devem estar acessíveis por meio da API do Braze.

{% alert important %}
Certifique-se de que sua exportação do Braze Currents inclua dados de todas as campanhas com as quais você deseja comparar (incluindo campanhas BAU).
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### Requisitos de dados SFMC

Para integrações com o Salesforce Marketing Cloud, o Decisioning Studio Acessar requer:

1. **Extensões de dados**: Seu público deve ser definido em uma extensão de dados que o Decisioning Studio Acessar. Use o SubscriberKey como o identificador principal do usuário.
2. **Acesso a eventos de rastreamento**: Desde que o pacote de aplicativos instalado ofereça suporte à configuração automatizada de ponta a ponta, nenhuma configuração adicional será necessária. 

As extensões de dados e as consultas de SQL são configuradas como parte da [configuração da orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/).

{% endtab %}
{% tab Klaviyo %}

### Requisitos de dados do Klaviyo

Para integrações com a Klaviyo, o Decisioning Studio Acessar requer:

1. **Acesso ao segmento**: Seu público deve ser definido como um segmento da Klaviyo que a chave de API pode acessar.
2. **Dados do perfil**: A chave de API deve ter acesso completo aos perfis para ler as atribuições do cliente.
3. **Acesso às métricas**: A chave de acesso completo à API deve ter acesso total a métricas e eventos para capturar dados de engajamento.

{% endtab %}
{% endtabs %}

## Melhores práticas

- **Mantenha os dados atualizados**: Certifique-se de que seus segmentos de público e dados de clientes sejam atualizados regularmente (no mínimo, diariamente) para que o agente trabalhe com informações atuais.
- **Inclua atribuições relevantes**: Pense nas características do cliente que podem influenciar a repercussão das mensagens - dados demográficos, histórico de engajamento, comportamento de compra e estágio do ciclo de vida são sinais valiosos.

## Próximos passos

Agora que você entende como o Acessa se conecta aos dados, prossiga para configurar sua integração com o CEP:

- [Configurar a orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)

