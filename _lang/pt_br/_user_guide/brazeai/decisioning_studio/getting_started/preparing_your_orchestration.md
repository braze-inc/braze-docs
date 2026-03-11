---
nav_title: Preparando sua orquestração
article_title: Preparando sua orquestração
page_order: 3
page_type: reference
description: "Este artigo de referência explica o que você precisa preparar antes de configurar a orquestração para o BrazeAI Decisioning Studio, incluindo a escolha da sua plataforma de engajamento com clientes (CEP) e a coleta das credenciais e ativos necessários."
---

# Preparando sua orquestração

> Este artigo de referência explica o que você precisa preparar antes de configurar a orquestração para o BrazeAI Decisioning Studio™, incluindo a escolha da sua plataforma de engajamento com clientes (CEP) e a coleta das credenciais e ativos necessários.

## O que é orquestração?

A orquestração é a conexão entre o Decisioning Studio e sua plataforma de engajamento com clientes (CEP). Uma vez que seu agente de decisão determina a ação ideal para cada cliente, a orquestração executa essas decisões acionando comunicações personalizadas através da sua CEP.

Pense assim:

- **Decisioning Studio** decide *o que* enviar e *quando* enviar
- **Sua CEP** cuida de *como* enviar

## Escolhendo sua CEP

O primeiro passo é determinar qual plataforma de engajamento com clientes você usará com o Decisioning Studio. Sua escolha afeta a complexidade da configuração e os recursos disponíveis.

### CEPs suportadas

| CEP | Decisioning Studio Go | Decisioning Studio Pro | Tipo de integração |
|-----|:---------------------:|:----------------------:|------------------|
| **Braze** | ✓ | ✓ | Integração de API nativa (recomendada) |
| **Salesforce Marketing Cloud** | ✓ | ✓ | Eventos de API + Journey Builder |
| **Klaviyo** | ✓ | ✓ | Eventos de API + Fluxos |
| **Outros CEPs** | — | ✓ | Personalizado (arquivo de recomendação) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert tip %}
Se você já está usando o Braze como seu CEP, recomendamos usar a integração nativa do Braze para a experiência de configuração mais suave.
{% endalert %}

## O que você precisará preparar

Antes de configurar a orquestração, reúna os seguintes itens com base no seu CEP escolhido.

{% tabs %}
{% tab Braze %}

| Item | Descrição |
|------|-------------|
| **Chave da API REST** | Uma nova chave de API com permissões para dados de usuários, mensagens, campanhas, Canvas, segmentos e modelos. |
| **URL do painel do Braze** | A URL da sua instância do Braze (por exemplo, `https://dashboard-01.braze.com`). |
| **ID do App** | A chave de API associada ao app que você deseja rastrear (encontrada em **Configurações** > **Configurações do App**). |
| **Nome e endereço de exibição do e-mail** | As informações do remetente a serem usadas em suas campanhas (encontradas em **Configurações** > **Preferências de E-mail**). |
| **Modelos base** | Os modelos de mensagem que seu agente usará para a orquestração. Você criará campanhas acionadas por API para cada modelo. |
| **ID do usuário teste** | Um ID de usuário para testar a integração antes do lançamento. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Item | Descrição |
|------|-------------|
| **Credenciais do pacote do App** | ID do cliente, segredo do cliente, URI base de autenticação, URI base REST e URI base SOAP de um pacote instalado com integração de API de servidor para servidor. |
| **Permissões da API** | Escopos para canais, ativos, automações, jornadas, contatos, extensões de dados e eventos de rastreamento. |
| **Extensões de dados** | Você precisará de extensões de dados para dados de assinantes, dados de engajamento e recomendações. |
| **Modelos de e-mail** | Os modelos que você deseja que o Decisioning Studio use, com IDs de modelo para cada um. |
| **Acesso ao Journey Builder** | Acesso para criar e ativar jornadas de múltiplas etapas com fontes de entrada de eventos da API. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Klaviyo %}

| Item | Descrição |
|------|-------------|
| **Chave de API privada** | Uma nova chave de API com permissões de acesso total para eventos, fluxos, listas, métricas, perfis e modelos. |
| **Modelos de e-mail** | Os modelos que você deseja que o Decisioning Studio use. Os modelos devem estar associados a um fluxo (você pode criar um fluxo de espaço reservado para esse propósito). |
| **Informações do remetente** | O nome do remetente e o endereço de e-mail a serem usados em suas campanhas. |
| **Acesso ao fluxo** | Acesso para criar e ativar fluxos com gatilhos de métricas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Other CEPs %}

{% alert note %}
Integrações de CEP personalizadas estão disponíveis apenas com o Decisioning Studio Pro.
{% endalert %}

Se você estiver usando um CEP diferente de Braze, SFMC ou Klaviyo, o Decisioning Studio Pro pode integrar por meio de uma abordagem de arquivo de recomendação:

| Item | Descrição |
|------|-------------|
| **Capacidade de ingestão de dados** | Seu CEP deve ser capaz de ingerir arquivos de recomendação (normalmente CSV ou JSON) contendo decisões personalizadas para cada cliente. |
| **Suporte a conteúdo dinâmico** | Suas campanhas devem suportar o preenchimento de campos dinamicamente com base em dados de recomendação. |
| **Recursos de engenharia personalizados** | Sua equipe precisará construir a integração para ler arquivos de recomendação e disparar comunicações. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

## Planejando suas campanhas

Antes de configurar a orquestração, considere os seguintes detalhes:

### Modelos base

Um modelo base é qualquer modelo de mensagem que seu agente de decisão pode usar. Considere:

- **Quantos modelos?** Seu agente pode trabalhar com um modelo ou vários. Se forem vários, o agente pode personalizar qual modelo cada cliente recebe.
- **Quais canais?** E-mail, push, SMS ou uma combinação. Cada canal pode exigir modelos e campanhas separados.
- **Quais elementos dinâmicos?** Identifique quais partes da sua mensagem o agente irá personalizar (linhas de assunto, CTAs, ofertas, timing, etc.). Esses se tornarão propriedades de disparo da API ou espaços reservados dinâmicos.

### Configurações de re-eligibilidade

Suas campanhas devem permitir que os usuários recebam mensagens várias vezes:

- Para testes, você vai querer enviar a mesma campanha para o mesmo usuário repetidamente
- Em produção, o agente pode determinar que a mesma campanha é ideal para um usuário em dias consecutivos

{% alert note %}
Ao configurar a re-eligibilidade para testes, os agentes do Decisioning Studio são projetados para respeitar os limites de frequência e não enviar a mesma campanha para um usuário mais de uma vez por dia em produção.
{% endalert %}

### Propriedades do gatilho da API

Para integrações com o Braze, planeje quais dimensões seu agente irá otimizar. Essas se tornam propriedades do gatilho da API que passam valores dinâmicos para suas campanhas:

| Exemplo de dimensão | Propriedade do gatilho da API |
|-------------------|---------------------|
| Linha de assunto | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Chamada para ação | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Oferta | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Valor do desconto | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Melhores práticas

Mantenha essas melhores práticas em mente ao se preparar para a orquestração:

1. **Comece simples.** Comece com um canal e um ou dois modelos. Você pode expandir depois, à medida que aprende o que funciona.
2. **Teste minuciosamente.** Antes de lançar, teste sua integração com um pequeno conjunto de usuários para verificar se o conteúdo dinâmico é preenchido corretamente.
3. **Documente sua configuração.** Mantenha um registro dos IDs das campanhas, IDs dos modelos, chaves da API e outros identificadores. Você precisará referenciar esses no portal do Decisioning Studio.
4. **Coordene com sua equipe.** A configuração de orquestração pode envolver equipes de marketing, engenharia e dados. Certifique-se de que todos entendam seu papel no processo.
5. **Planeje os dados de feedback.** A orquestração não se trata apenas de enviar mensagens—também envolve coletar os dados de engajamento e conversão que ajudam seu agente a aprender. Veja [Preparando suas fontes de dados]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/preparing_your_data_sources/) para mais detalhes.

## Próximos passos

Uma vez que você tenha reunido suas credenciais e planejado suas campanhas, você está pronto para configurar a orquestração:

- [Estúdio de Decisão Go: Configure a orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)
- [Estúdio de Decisão Pro: Configure a orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

