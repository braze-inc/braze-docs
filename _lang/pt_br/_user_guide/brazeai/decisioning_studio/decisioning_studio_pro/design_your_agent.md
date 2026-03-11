---
nav_title: Crie seu agente
article_title: Crie seu agente
page_order: 3
description: "Aprenda a projetar seu agente Decisioning Studio Pro com a equipe de Serviços de Decisão de IA, incluindo definição de público, métricas de sucesso e dimensões."
---

# Crie seu agente

> A primeira etapa da configuração do agente é trabalhar com nossa equipe de Serviços de Decisão de IA para projetar seu agente. Este artigo aborda as principais decisões de design e como definir seu público.

Para conceitos básicos sobre agentes de decisão — incluindo métricas de sucesso, dimensões, bancos de ações e restrições — consulte [Projetando agentes de decisão]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/).

## Principais decisões de design

Trabalhando com a equipe de Serviços de Decisão de IA, você tomará as seguintes decisões:

| Decisão | Descrição | Exemplos |
|----------|-------------|----------|
| **Métrica de sucesso** | O que o agente maximizará ao personalizar o engajamento do cliente? | Receita, LTV, ARPU, conversões, retenção |
| **Público** | Para quem o agente do Decisioning Studio tomará decisões de engajamento do cliente? | Todos os clientes, membros do programa de fidelidade, assinantes em risco |
| **Grupos experimentais** | Como devem ser estruturados os ensaios clínicos randomizados do Decisioning Studio? | Estúdio de Decisão, Controle Aleatório, BAU, Retenção |
| **Dimensões** | Que decisões o agente deve personalizar? | Hora do dia, assunto, frequência, ofertas, canal |
| **Opções** | Com quais opções o agente pode trabalhar? | Modelos específicos, ofertas, janelas de tempo |
| **Restrições** | Que decisões o agente *nunca* deve tomar? | Restrições geográficas, limites orçamentários, regras de elegibilidade |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Cada uma dessas decisões tem implicações sobre o quanto o agente poderá gerar de aumento incremental e com que rapidez. Nossa equipe de Serviços de Decisão por IA trabalhará com você para projetar um agente que gere o máximo valor, respeitando todas as suas regras de negócios.

![Diagrama de tomada de decisão profissional]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Definindo seu público

Os públicos-alvo dos casos de uso são normalmente definidos em uma plataforma de engajamento com clientes (como Braze ou Salesforce Marketing Cloud) e, em seguida, enviados ao agente do Decisioning Studio. O agente divide então os clientes em grupos de tratamento, a fim de realizar ensaios clínicos randomizados.

### Grupos de tratamento

| Grupo | Descrição |
|-------|-------------|
| **Estúdio de Decisões** | Clientes que recebem recomendações otimizadas por IA |
| **Controle aleatório** | Clientes que recebem opções selecionadas aleatoriamente (comparação com a linha de base) |
| **Negócios como de costume (opcional)** | Clientes que recebem a jornada de marketing atual (para comparar com a performance existente) |
| **Holdout (opcional)** | Clientes que não recebem comunicações (para medir o impacto geral da campanha) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Configurando seu público

{% tabs %}
{% tab Braze %}

**Configure o público no Braze:**

1. Crie um segmento para o público que você deseja direcionar.
2. Forneça o ID do segmento à sua equipe de Serviços de Decisão de IA.

{% alert note %}
Para a Braze, podemos incorporar vários segmentos e combiná-los para criar o público. O Decisioning Studio pode incorporar um segmento para uma campanha comparativa Business-as-Usual. Todos esses padrões são aceitáveis.
{% endalert %}

{% endtab %}
{% tab SFMC %}

**Configure o público no Salesforce Marketing Cloud:**

1. Configure uma ou mais extensões de dados SFMC para o seu público e forneça o ID da extensão de dados.
2. Configure o pacote instalado SFMC para integração com a API com as permissões apropriadas exigidas pelo Decisioning Studio.
3. Certifique-se de que essa extensão de dados seja atualizada diariamente, pois o Decisioning Studio irá extrair os dados incrementais mais recentes disponíveis.

Forneça o ID da extensão e a chave de API à equipe de serviços da Braze. Eles ajudarão nas próximas etapas da ingestão dos dados de cliente.

{% endtab %}
{% tab Klaviyo %}

**Defina o público no Klaviyo:**

1. Crie um segmento de público
2. Gere uma chave de API privada e forneça-a à equipe de tomada de decisões da Braze IA.
3. Forneça o ID do segmento e a chave de API à equipe de serviços da Braze.

Consulte a [documentação da Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) para saber mais sobre como realizar essas etapas.

{% endtab %}
{% tab Other Platforms %}

**Google Cloud Storage**

Se o público não estiver armazenado atualmente no Braze, SFMC ou Klaviyo, a melhor etapa é configurar uma exportação automatizada diretamente para um bucket do Google Cloud Services controlado pelo Braze.

Para determinar se isso é viável, consulte a documentação da sua plataforma MarTech. Por exemplo, o mParticle oferece uma [integração nativa com o Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/). Se for esse o caso, podemos fornecer um bucket GCS para exportar os dados do público.

Existem páginas semelhantes para:
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## Recursos profissionais

O Decisioning Studio Pro oferece todo o poder da tomada de decisões com IA:

| Capacidade | Informações |
|------------|---------|
| **Qualquer métrica de sucesso** | Otimize para receita, conversões, ARPU, LTV ou qualquer KPI de negócios |
| **Dimensões ilimitadas** | Personalize a oferta, o canal, o momento, a frequência, a criatividade e muito mais. |
| **Qualquer CEP** | Integrações nativas com Braze, SFMC, Klaviyo + integrações personalizadas para qualquer plataforma |
| **Serviços de tomada de decisão com IA** | Suporte dedicado da equipe de ciência de dados da Braze |
| **Projeto de experimento avançado** | Grupos de tratamento e holdouts totalmente personalizáveis |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Melhores práticas

Algumas práticas recomendadas para projetar agentes do Decisioning Studio:

1. **Maximize a riqueza dos dados**: Quanto mais informações os agentes tiverem sobre seus clientes, melhor será a performance deles.
2. **Diversificar ações**: Quanto mais diversificado for o conjunto de ações que o agente pode realizar, mais ele poderá personalizar sua estratégia para cada usuário.
3. **Minimize as restrições**: Quanto menos restrições houver para seus agentes, melhor. As restrições devem ser projetadas para respeitar as regras de negócios, ao mesmo tempo em que liberam ao máximo a experimentação conduzida pelos agentes.

## Próximos passos

Depois que as principais decisões de design forem tomadas, podemos prosseguir com o lançamento:

- [Inicie seu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)