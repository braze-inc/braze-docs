---
nav_title: Conectar fontes de dados
article_title: Conectar fontes de dados
page_order: 1
description: "Saiba como o BrazeAI Decisioning Studio Go se conecta aos seus dados de cliente através da sua Plataforma de Engajamento com Clientes."
---

# Conectar fontes de dados

> O BrazeAI Decisioning Studio™ Go se conecta aos seus dados de cliente através da sua Plataforma de Engajamento com Clientes (CEP). Este artigo explica quais dados são utilizados e como a conexão funciona.

## Como o Go acessa os dados de cliente

Diferente do Decisioning Studio Pro, que suporta integrações diretas de dados com várias fontes, o Decisioning Studio Go acessa os dados de cliente através do seu CEP. Isso significa:

- **Os dados do público** são extraídos diretamente de segmentos ou listas definidos no seu CEP (Braze, Salesforce Marketing Cloud ou Klaviyo) e podem incluir apenas certos atributos pré-definidos (não dados 1P)
- **Os dados de engajamento** (aberturas, cliques, envios) são capturados através de consultas automatizadas ou integrações nativas com seu CEP
- **Nenhuma configuração adicional de pipeline de dados** é necessária além do que você configura no seu CEP

## Padrões de integração suportados

O Decisioning Studio Go suporta os seguintes CEPs para acesso a dados:

| CEP | Fonte de Público | Dados de engajamento |
|-----|-----------------|-----------------|
| **Braze** | Segmentos | Exportação do Braze Currents |
| **Salesforce Marketing Cloud** | Extensões de Dados | Automação de Consulta SQL |
| **Klaviyo** | Segmentos | Integração nativa de API |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Requisitos de dados por CEP

{% tabs %}
{% tab Braze %}

### requisitos de dados do Braze

Para integrações do Braze, o Decisioning Studio Go requer:

1. **Braze Currents**: Você deve ter o Braze Currents habilitado e configurado para exportar dados de engajamento para o Decisioning Studio Go. Isso permite que o agente aprenda com as respostas dos clientes.

2. **Acesso a segmentos**: A chave de API que você criar deve ter permissões para acessar segmentos que definem seu público-alvo.

3. **Dados do perfil do usuário**: Quaisquer atributos de perfil de usuário ou atributos personalizados que você deseja que o agente considere devem ser acessíveis através da API do Braze.

{% alert important %}
Certifique-se de que sua exportação do Braze Currents inclua dados de quaisquer campanhas que você deseja comparar (incluindo campanhas BAU).
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### requisitos de dados do SFMC

Para integrações do Salesforce Marketing Cloud, o Decisioning Studio Go requer:

1. **Data Extensions**: Seu público deve ser definido em uma Data Extension que o Decisioning Studio Go possa acessar. Use o SubscriberKey como o identificador principal do usuário.
2. **Acesso a eventos de rastreamento**: Desde que o Pacote de Aplicativo Instalado suporte configuração automatizada de ponta a ponta, nenhuma configuração adicional é necessária. 

As extensões de dados e consultas de SQL são configuradas como parte da [configuração de orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/).

{% endtab %}
{% tab Klaviyo %}

### requisitos de dados do Klaviyo

Para integrações do Klaviyo, o Decisioning Studio Go requer:

1. **Acesso a segmentos**: Seu público deve ser definido como um segmento Klaviyo que a chave de API pode acessar.
2. **Dados do perfil**: A chave de API deve ter Acesso Total a Perfis para ler os atributos do cliente.
3. **Acesso a métricas**: A chave de API deve ter Acesso Total a Métricas e Eventos para capturar dados de engajamento.

{% endtab %}
{% endtabs %}

## Melhores práticas

- **Mantenha os dados atualizados**: Certifique-se de que seus segmentos de público e dados de cliente sejam atualizados regularmente (no mínimo, diariamente) para que o agente trabalhe com informações atuais.
- **Inclua atributos relevantes**: Pense sobre quais características do cliente podem influenciar quais mensagens ressoam—demografia, histórico de engajamento, comportamento de compra e estágio do ciclo de vida são todos sinais valiosos.

## Próximos passos

Agora que você entende como o Go se conecta aos dados, prossiga para configurar sua integração CEP:

- [Configurar orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)

