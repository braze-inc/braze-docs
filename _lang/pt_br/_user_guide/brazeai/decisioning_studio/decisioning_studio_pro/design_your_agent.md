---
nav_title: Crie seu agente
article_title: Crie seu agente
page_order: 3
description: "Saiba como projetar seu agente do Decisioning Studio Pro com a equipe do IA Decisioning Services, incluindo definição de público, métricas de sucesso e dimensões."
---

# Crie seu agente

> A primeira etapa da configuração do agente é trabalhar com nossa equipe de IA Decisioning Services para projetar seu agente. Este artigo aborda as principais decisões de design e como definir seu público.

Para conhecer os conceitos básicos sobre agentes de decisão - incluindo métricas de sucesso, dimensões, bancos de ações e restrições - consulte [Projetando agentes de decisão]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/).

## Principais decisões de design

Trabalhando com a equipe de IA Decisioning Services, você tomará as seguintes decisões:

| Decisão | Descrição | Exemplos |
|----------|-------------|----------|
| **Métrica de sucesso** | O que o agente maximizará ao personalizar o engajamento do cliente? | Receita, LTV, ARPU, conversões, retenção |
| **Público** | Para quem o agente do Decisioning Studio tomará as decisões de engajamento do cliente? | Todos os clientes, membros de fidelidade, assinantes em risco |
| **Grupos de experimentos** | Como devem ser estruturados os estudos controlados randomizados do Decisioning Studio? | Estúdio de tomada de decisão, controle aleatório, BAU, retenção |
| **Dimensões** | Quais decisões o agente deve personalizar? | Hora do dia, linha de assunto, frequência, ofertas, canal |
| **Opções** | Quais são as opções que o agente tem para trabalhar? | Modelos específicos, ofertas, janelas de tempo |
| **Restrições** | Que decisões o agente *nunca* deve tomar? | Restrições geográficas, limites orçamentários, regras de elegibilidade |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Cada uma dessas decisões tem implicações sobre a quantidade de aumento incremental que o agente pode ser capaz de gerar e com que rapidez. Nossa equipe de IA Decisioning Services trabalhará com você para projetar um agente que gere o máximo de valor, respeitando todas as suas regras de negócios.

![Diagrama Pro de tomada de decisão]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Definição de seu público

Os públicos dos casos de uso são normalmente definidos em uma plataforma de engajamento com clientes (como a Braze ou a Salesforce Marketing Cloud) e, em seguida, enviados para o agente do Decisioning Studio. Em seguida, o agente divide os clientes em grupos de tratamento para realizar estudos controlados e randomizados.

### Grupos de tratamento

| Grupo | Descrição |
|-------|-------------|
| **Estúdio de tomada de decisões** | Clientes que recebem recomendações otimizadas por IA |
| **Controle aleatório** | Clientes que recebem opções selecionadas aleatoriamente (comparação de linha de base) |
| **Negócios como de costume (opcional)** | Clientes que recebem a jornada de marketing atual (para comparação com a performance existente) |
| **Retenção (opcional)** | Clientes que não recebem comunicações (para medir o impacto geral da campanha) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Configuração de seu público

{% tabs %}
{% tab Braze %}

**Configurar o público no Braze:**

1. Crie um segmento para seu público que você gostaria de direcionar.
2. Forneça o ID do segmento à sua equipe de IA Decisioning Services.

{% alert note %}
No Braze, podemos ingerir vários segmentos e combiná-los para criar o público. O Decisioning Studio pode ingerir um segmento para uma campanha de comparador Business-as-Usual. Todos esses padrões são aceitáveis.
{% endalert %}

{% endtab %}
{% tab SFMC %}

**Configure o público no Salesforce Marketing Cloud:**

1. Configure uma extensão de dados SFMC para seu público e forneça a ID da extensão de dados
2. Configure o SFMC Installed Package para a integração da API com as permissões apropriadas exigidas pelo Decisioning Studio
3. Certifique-se de que essa extensão de dados seja atualizada diariamente, pois o Decisioning Studio extrairá os dados incrementais mais recentes disponíveis

Forneça o ID da extensão e a chave de API para a equipe de serviços do Braze. Eles ajudarão nas próximas etapas da ingestão de dados de clientes.

{% endtab %}
{% tab Klaviyo %}

**Definir o público no Klaviyo:**

1. Criar um segmento de público
2. Gere uma chave de API privada e forneça-a à equipe do Braze IA Decisioning
3. Forneça o ID do segmento e a chave de API para a equipe de serviços do Braze

Consulte a [documentação do Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) para saber mais sobre como realizar essas etapas.

{% endtab %}
{% tab Other Platforms %}

**Google Cloud Storage**

Se o público não estiver armazenado no Braze, SFMC ou Klaviyo, a próxima melhor etapa é configurar uma exportação automatizada diretamente para um bucket do Google Cloud Services controlado pelo Braze.

Para determinar se isso é viável, consulte a documentação de sua plataforma MarTech. Por exemplo, o mParticle oferece uma [integração nativa com o Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/). Se esse for o caso, podemos fornecer um bucket GCS para exportar os dados do público.

Há páginas semelhantes para:
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Plataforma de experiência da Adobe](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## Recursos profissionais

O Decisioning Studio Pro oferece todo o poder de decisão da IA:

| Capacidade | Informações |
|------------|---------|
| **Qualquer métrica de sucesso** | Otimize a receita, as conversões, o ARPU, o LTV ou qualquer KPI da empresa |
| **Dimensões ilimitadas** | Personalize a oferta, o canal, o momento, a frequência, o criativo e muito mais |
| **Qualquer CEP** | Integrações nativas com Braze, SFMC, Klaviyo + integrações personalizadas para qualquer plataforma |
| **Serviços de decisão de IA** | Suporte dedicado da equipe de ciência de dados da Braze |
| **Projeto avançado de experimentos** | Grupos de tratamento e holdouts totalmente personalizáveis |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Melhores práticas

Algumas práticas recomendadas para projetar agentes do Decisioning Studio:

1. **Maximizar a riqueza de dados**: Quanto mais informações os agentes tiverem sobre seus clientes, melhor será a performance deles.
2. **Diversificar as ações**: Quanto mais diversificado for o conjunto de ações que o agente puder realizar, mais ele poderá personalizar sua estratégia para cada usuário.
3. **Minimizar as restrições**: Quanto menos restrições forem impostas a seus agentes, melhor. As restrições devem ser projetadas para respeitar as regras comerciais e, ao mesmo tempo, liberar ao máximo a experimentação conduzida pelo agente.

## Próximos passos

Quando as principais decisões de design forem tomadas, poderemos prosseguir com o lançamento:

- [Lance seu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)