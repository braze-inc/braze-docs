---
nav_title: Crie seu agente
article_title: Crie seu agente
page_order: 3
description: "Aprenda a projetar um agente Go do BrazeAI Decisioning Studio, incluindo definição de público, dimensões e limitações específicas do Go."
---

# Crie seu agente

> Este artigo aborda como projetar seu agente Decisioning Studio Go, incluindo a definição do seu público, a seleção de dimensões e a compreensão dos recursos e limitações específicos do Go.

Para conceitos básicos sobre agentes de decisão — incluindo métricas de sucesso, dimensões, bancos de ações e restrições — consulte [Projetando agentes de decisão]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/).

## Recursos Go versus Pro

O Decisioning Studio Go é uma plataforma self-service com recursos simplificados em comparação com o Decisioning Studio Pro. Compreender essas diferenças ajuda você a projetar um agente eficaz dentro do escopo do Go.

| Capacidade | Estúdio de Decisão Go | Decisioning Studio Pro |
|-----------|----------------------|------------------------|
| **Métrica de sucesso** | Apenas cliques | Qualquer métrica de negócios (receita, conversões ou ARPU) |
| **Dimensões** | Banco de ação limitada | Dimensões ilimitadas |
| **CEPs suportados** | Braze, SFMC, Klaviyo | Qualquer CEP (nativo e personalizado) |
| **Dados de cliente** | Apenas engajamento | Todos os dados 1P |
| **Configuração** | Autoatendimento | Suporte aos serviços de tomada de decisão por IA |
| **Grupos experimentais** | Ir + Controle aleatório + BAU opcional | Totalmente personalizável |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Projetando seu agente Go

Ao projetar um agente do Decisioning Studio Go, você tomará decisões nas seguintes áreas:

### Etapa 1: Defina seu público

Seu público é o conjunto de clientes com os quais o agente irá realizar o engajamento. No Go, os públicos são definidos no seu CEP:

{% tabs %}
{% tab Braze %}

**Definindo o público no Braze:**

1. Crie um segmento no Braze que defina os clientes que você deseja que o agente tenha como alvo para o direcionamento.
2. Ao configurar seu experimentador no portal Decisioning Studio Go, selecione este segmento como seu público-alvo.

{% alert tip %}
Considere criar um segmento dedicado para o seu experimentador do Decisioning Studio Go, a fim de manter seus testes isolados e mensuráveis.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

**Definindo o público no SFMC:**

1. Configure uma extensão de dados que contenha seu público-alvo.
2. Certifique-se de que esta extensão de dados seja atualizada diariamente com os dados mais recentes de cliente.
3. Faça referência a esta extensão de dados no portal Decisioning Studio Go ao configurar seu experimentador.

{% endtab %}
{% tab Klaviyo %}

**Definindo o público no Klaviyo:**

1. Crie um segmento no Klaviyo que defina seu público-alvo.
2. Ao configurar seu experimentador no portal Decisioning Studio Go, selecione este segmento.

{% endtab %}
{% endtabs %}

### Etapa 2: Selecione suas dimensões

As dimensões são as “alavancas” que o agente pode acionar para personalizar a experiência do cliente. Isso inclui dimensões criativas, como linha de assunto e imagem principal, bem como dimensões relacionadas ao tipo de envio de e-mail, como a frequência dos e-mails ou a hora do dia. 

{% alert note %}
As dimensões específicas disponíveis dependem do seu CEP e de como suas campanhas estão configuradas. Trabalhe com os modelos e o conteúdo que você configurou no seu CEP.
{% endalert %}

### Etapa 3: Configure seu banco de ações

O banco de ações define as opções específicas que o agente pode escolher para cada dimensão. Por exemplo:

- **Modelos de e-mail**: Selecione quais modelos o agente pode usar (eles devem ser configurados primeiro no seu CEP)
- **Assunto**: Defina as variantes da linha de assunto que o agente pode testar
- **Horários de envio**: Especifique os intervalos de tempo que o agente pode escolher

### Etapa 4: Configurar grupos experimentais

O Decisioning Studio Go cria automaticamente grupos de experimentos para medir a performance:

| Grupo | Descrição |
|-------|-------------|
| **Estúdio de Decisão Go** | Clientes que recebem recomendações otimizadas por IA |
| **Controle aleatório** | Clientes que recebem opções selecionadas aleatoriamente (comparação com a linha de base) |
| **Negócios como de costume (opcional)** | Clientes que recebem sua campanha atual (se comparado com a performance atual) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Para uma comparação precisa, certifique-se de que nenhum cliente possa pertencer a mais de um grupo experimental e que os clientes sejam atribuídos aleatoriamente aos grupos, sem preconceitos.
{% endalert %}

## Limitações a considerar

Ao projetar seu agente Go, tenha em mente estas limitações:

- **Apenas cliques**: O Go otimiza as taxas de cliques. Se você precisa otimizar receitas, conversões ou outras métricas de negócios, considere o Decisioning Studio Pro.
- **Dimensões limitadas**: O Go suporta um conjunto predefinido de dimensões. Para dimensões personalizadas ou personalizações complexas, considere o Decisioning Studio Pro.
- **Três CEPs**: O Go integra-se apenas com o Braze, o Salesforce Marketing Cloud e o Klaviyo. Para outras plataformas, considere o Decisioning Studio Pro.

## Melhores práticas

- **Comece de forma simples**: Comece com 2 ou 3 modelos ou variantes de linha de assunto. Isso dá ao agente opções suficientes para aprender, mantendo a experiência gerenciável.
- **Dê tempo ao tempo**: O agente precisa de dados suficientes para aprender. Aguarde pelo menos 2 a 4 semanas antes de tirar conclusões sobre a performance.
- **Mantenha o conteúdo variado**: Certifique-se de que suas opções sejam significativamente diferentes. Testar pequenas variações pode não trazer insights significativos.
- **Monitore regularmente**: Verifique o portal Decisioning Studio Go para monitorar o progresso da experiência e as métricas de engajamento.

## Próximos passos

Depois de projetar seu agente e configurá-lo no portal Decisioning Studio Go, você estará pronto para iniciar:

- [Inicie seu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent/)
