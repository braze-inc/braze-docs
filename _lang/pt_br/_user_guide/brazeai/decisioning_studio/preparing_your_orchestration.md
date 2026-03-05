---
nav_title: Preparando sua orquestração
article_title: Preparando sua orquestração
page_order: 5
page_type: reference
description: "Este artigo de referência explica o que você precisa preparar antes de configurar a orquestração para o BrazeAI Decisioning Studio, incluindo a escolha do CEP e a coleta das credenciais e dos ativos necessários."
---

# Preparando sua orquestração

> Este artigo de referência explica o que você precisa preparar antes de configurar a orquestração para o BrazeAI Decisioning Studio™, incluindo a escolha de sua plataforma de engajamento com clientes (CEP) e a coleta das credenciais e ativos necessários.

## O que é orquestração?

A orquestração é a conexão entre o Decisioning Studio e sua plataforma de engajamento com clientes (CEP). Depois que seu agente de decisão determina a ação ideal para cada cliente, a orquestração executa essas decisões disparando comunicações personalizadas por meio de seu CEP.

Pense da seguinte forma:

- **O Decisioning Studio** decide *o que* enviar e *quando* enviar
- **Seu CEP** controla *como* enviá-lo

## Escolhendo seu CEP

A primeira etapa é determinar qual plataforma de engajamento com clientes você usará com o Decisioning Studio. Sua escolha afeta a complexidade da configuração e os recursos disponíveis.

### CEPs com suporte

| CEP | Acessar o Decisioning Studio | Decisioning Studio Pro | Tipo de integração |
|-----|:---------------------:|:----------------------:|------------------|
| **Braze** | ✓ | ✓ | Integração com API nativa (recomendado) |
| **Salesforce Marketing Cloud** | ✓ | ✓ | Eventos da API + Journey Builder |
| **Klaviyo** | ✓ | ✓ | Eventos da API + fluxos |
| **Outros CEPs** | - | ✓ | Personalizado (arquivo de recomendação) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert tip %}
Se já estiver usando o Braze como CEP, recomendamos usar a integração nativa do Braze para obter uma experiência de configuração mais tranquila.
{% endalert %}

## O que você precisa para se preparar

Antes de configurar a orquestração, reúna os seguintes itens com base no CEP escolhido.

{% tabs %}
{% tab Braze %}

| Item | Descrição |
|------|-------------|
| **Chave da API REST** | Uma nova chave de API com permissões para dados de usuários, mensagens, campanhas, Canvas, segmentos e modelos. |
| **URL do dashboard do Braze** | Seu URL da instância do Braze (por exemplo, `https://dashboard-01.braze.com`). |
| **ID do app** | A chave de API associada ao app que deseja rastrear (encontrada em **Configurações** > **Configurações do app**). |
| **Nome e endereço de exibição do e-mail** | As informações do remetente a serem usadas em suas campanhas (encontradas em **Configurações** > **Preferências de e-mail**). |
| **Modelos básicos** | Os modelos de mensagens que seu agente usará para orquestração. Você criará campanhas disparadas pela API para cada modelo. |
| **ID do usuário de teste** | Um ID de usuário para testar a integração antes do lançamento. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Item | Descrição |
|------|-------------|
| **Credenciais do pacote do app** | ID do cliente, segredo do cliente, URI de base de autenticação, URI de base REST e URI de base SOAP de um pacote instalado com integração de API de servidor para servidor. |
| **Permissões da API** | Escopos para canais, ativos, automações, jornadas, contatos, extensões de dados e eventos de rastreamento. |
| **Extensões de dados** | Você precisará de extensões de dados para dados de assinantes, dados de engajamento e recomendações. |
| **Modelos de e-mail** | Os modelos que você deseja que o Decisioning Studio use, com IDs de modelo para cada um. |
| **Acesso ao Journey Builder** | Acesso para criar e ativar jornadas de várias etapas com fontes de entrada de eventos da API. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Klaviyo %}

| Item | Descrição |
|------|-------------|
| **Chave de API privada** | Uma nova chave de acesso completo à API com permissões de acesso para eventos, fluxos, listas, métricas, perfis e modelos. |
| **Modelos de e-mail** | Os modelos que você deseja que o Decisioning Studio use. Os modelos devem ser associados a um fluxo (você pode criar um fluxo de espaço reservado para essa finalidade). |
| **Informações do remetente** | O nome do remetente e o endereço de e-mail a serem usados em suas campanhas. |
| **Acesso ao fluxo** | Acesso para criar e ativar fluxos com disparadores de métricas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Other CEPs %}

{% alert note %}
As integrações personalizadas do CEP só estão disponíveis com o Decisioning Studio Pro.
{% endalert %}

Se estiver usando um CEP diferente do Braze, SFMC ou Klaviyo, o Decisioning Studio Pro pode se integrar por meio de uma abordagem de arquivo de recomendação:

| Item | Descrição |
|------|-------------|
| **Capacidade de ingestão de dados** | Seu CEP deve ser capaz de ingerir arquivos de recomendação (normalmente CSV ou JSON) contendo decisões personalizadas para cada cliente. |
| **Suporte a conteúdo dinâmico** | Suas campanhas devem suportar o preenchimento dinâmico de campos com base em dados de recomendação. |
| **Recursos de engenharia personalizados** | Sua equipe precisará criar a integração para ler arquivos de recomendação e disparar comunicações. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

## Planejando suas campanhas

Antes de configurar a orquestração, considere os seguintes detalhes:

### Modelos básicos

Um modelo básico é qualquer modelo de mensagem que seu agente de decisão possa usar. Considere:

- **Quantos modelos?** Seu agente pode trabalhar com um ou vários modelos. Se forem múltiplos, o agente poderá personalizar o modelo que cada cliente receberá.
- **Quais canais?** Envio de e-mail, push, SMS ou uma combinação. Cada canal pode exigir modelos e campanhas separados.
- **Quais são os elementos dinâmicos?** Identifique quais partes de sua mensagem o agente personalizará (linhas de assunto, CTAs, ofertas, tempo, etc.). Eles se tornarão propriedades de disparo da API ou espaços reservados dinâmicos.

### Configurações de reelegibilidade

Suas campanhas devem permitir que os usuários recebam mensagens várias vezes:

- Para testes, envie a mesma campanha para o mesmo usuário repetidamente
- Na produção, o agente pode determinar que a mesma campanha é ideal para um usuário em dias consecutivos

{% alert note %}
Ao configurar a reelegibilidade para testes, os agentes do Decisioning Studio são projetados para respeitar os limites de frequência e não enviarão a mesma campanha a um usuário mais de uma vez por dia na produção.
{% endalert %}

### Propriedades do disparador da API

Para integrações do Braze, planeje quais dimensões seu agente otimizará. Elas se tornam propriedades de disparo da API que passam valores dinâmicos para suas campanhas:

| Exemplo de dimensão | Propriedade de disparo da API |
|-------------------|---------------------|
| Linha de assunto | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Chamada para ação | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Oferta | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Valor do desconto | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Melhores práticas

Tenha em mente essas práticas recomendadas ao se preparar para a orquestração:

1. **Comece de forma simples.** Comece com um canal e um ou dois modelos. Você pode expandir posteriormente à medida que aprender o que funciona.
2. **Faça um teste completo.** Antes do lançamento, teste sua integração com um pequeno conjunto de usuários para verificar se o conteúdo dinâmico é preenchido corretamente.
3. **Documente sua configuração.** Mantenha o controle de IDs de campanha, IDs de modelo, chaves de API e outros identificadores. Você precisará fazer referência a eles no portal do Decisioning Studio.
4. **Coordene com sua equipe.** A configuração da orquestração pode envolver as equipes de marketing, engenharia e dados. Certifique-se de que todos entendam sua função no processo.
5. **Planeje os dados de feedback.** A orquestração não se refere apenas ao envio de mensagens, mas também à coleta de dados de engajamento e conversão que ajudam seu agente a aprender. Consulte [Preparação de suas fontes de dados]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/preparing_your_data_sources/) para obter mais detalhes.

## Próximos passos

Depois de reunir suas credenciais e planejar suas campanhas, você estará pronto para configurar a orquestração:

- [Acessar o Decisioning Studio: Configurar a orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)
- [Decisioning Studio Pro: Configurar a orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)
