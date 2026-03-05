---
nav_title: Crie seu agente
article_title: Crie seu agente
page_order: 3
description: "Saiba como projetar um agente do BrazeAI Decisioning Studio Acessar, incluindo a definição do público, as dimensões e as limitações específicas do Acessar."
---

# Crie seu agente

> Este artigo aborda como projetar seu agente do Decisioning Studio Acessar, incluindo a definição de seu público, a seleção de dimensões e a compreensão das capacidades e limitações específicas do Acessar.

Para conhecer os conceitos básicos sobre agentes de decisão - incluindo métricas de sucesso, dimensões, bancos de ações e restrições - consulte [Projetando agentes de decisão]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/).

## Recursos do Acessar versus Pro

O Decisioning Studio Acessar é uma plataforma de autoatendimento com recursos simplificados em comparação com o Decisioning Studio Pro. Compreender essas diferenças o ajuda a projetar um agente eficaz dentro do escopo do Acessar.

| Capacidade | Acessar o Decisioning Studio | Decisioning Studio Pro |
|-----------|----------------------|------------------------|
| **Métrica de sucesso** | Somente cliques | Qualquer métrica de negócios (receita, conversões ou ARPU) |
| **Dimensões** | Banco de ações limitado | Dimensões ilimitadas |
| **CEPs apoiados** | Braze, SFMC | Qualquer CEP (nativo e personalizado) |
| **Dados de cliente** | Somente engajamento | Todos os dados 1P |
| **Configuração** | Autoatendimento | Suporte aos serviços de tomada de decisão por IA |
| **Grupos de experimentos** | Acessar + controle aleatório + BAU opcional | Totalmente personalizável |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Projetando seu agente Acessado

Ao projetar um agente do Decisioning Studio Acessar, você tomará decisões nas seguintes áreas:

### Etapa 1: Defina seu público

Seu público é o conjunto de clientes com os quais o agente se engajará. No Acessar, os públicos são definidos em seu CEP:

{% tabs %}
{% tab Braze %}

**Definição de público no Braze:**

1. Crie um segmento no Braze que defina os clientes que você deseja que o agente direcione.
2. Ao configurar seu experimentador no portal do Decisioning Studio Acessar, selecione esse segmento como seu público-alvo.

{% alert tip %}
Considere criar um segmento dedicado para seu experimentador do Decisioning Studio Acessar para manter seus testes isolados e mensuráveis.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

**Definição de público na SFMC:**

1. Configure uma extensão de dados que contenha seu público-alvo.
2. Certifique-se de que essa extensão de dados seja atualizada diariamente com os dados mais recentes dos clientes.
3. Faça referência a essa extensão de dados no portal do Decisioning Studio Acessar ao configurar seu experimentador.

{% endtab %}
{% endtabs %}

### Etapa 2: Selecione suas dimensões

As dimensões são as "alavancas" que o agente pode acionar para personalizar a experiência do cliente. Isso inclui dimensões criativas, como linha de assunto e imagem de herói, bem como dimensões de tipo de envio, como a frequência de e-mails ou a hora do dia. 

{% alert note %}
As dimensões específicas disponíveis dependem de seu CEP e de como suas campanhas estão configuradas. Trabalhe com os modelos e o conteúdo que você configurou em seu CEP.
{% endalert %}

### Etapa 3: Configure seu banco de ações

O banco de ações define as opções específicas que o agente pode escolher para cada dimensão. Por exemplo:

- **Modelos de e-mail**: Selecione quais modelos o agente pode usar (eles devem ser configurados em seu CEP primeiro)
- **Linhas de assunto**: Defina as variantes de linha de assunto que o agente pode testar
- **Horário de envio**: Especifique as janelas de tempo que o agente pode escolher

### Etapa 4: Configurar grupos de experimentos

O Decisioning Studio Acess cria automaticamente grupos de experimentos para medir a performance:

| Grupo | Descrição |
|-------|-------------|
| **Acessar o Decisioning Studio** | Clientes que recebem recomendações otimizadas por IA |
| **Controle aleatório** | Clientes que recebem opções selecionadas aleatoriamente (comparação de linha de base) |
| **Negócios como de costume (opcional)** | Currents que recebem sua campanha existente (se estiver comparando com a performance atual) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Para obter uma comparação precisa, certifique-se de que nenhum cliente possa pertencer a mais de um grupo de experimento e que os clientes sejam atribuídos aleatoriamente aos grupos, sem viés.
{% endalert %}

## Limitações a serem consideradas

Ao projetar seu agente Acessar, tenha em mente essas limitações:

- **Somente cliques**: O Acessar otimiza as taxas de cliques. Se você precisar otimizar a receita, as conversões ou outras métricas de negócios, considere o Decisioning Studio Pro.
- **Dimensões limitadas**: O Acessar oferece suporte a um conjunto predefinido de dimensões. Para dimensões personalizadas ou personalização complexa, considere o Decisioning Studio Pro.
- **Dois CEPs**: O Acessar só se integra ao Braze e ao Salesforce Marketing Cloud. Para outras plataformas, considere o Decisioning Studio Pro.

## Melhores práticas

- **Comece de forma simples**: Comece com dois ou três modelos ou variantes de linha de assunto. Isso dá ao agente opções suficientes para aprender e, ao mesmo tempo, mantém o experimento gerenciável.
- **Dê tempo ao tempo**: O agente precisa de dados suficientes para aprender. Aguarde pelo menos 2 a 4 semanas antes de tirar conclusões sobre o desempenho.
- **Mantenha o conteúdo variado**: Certifique-se de que suas opções sejam significativamente diferentes. O teste de pequenas variações pode não produzir insights significativos.
- **Monitore regularmente**: Acesse o portal do Decisioning Studio Acessar para monitorar o progresso do experimento e as métricas de engajamento.

## Próximos passos

Depois de projetar seu agente e configurá-lo no portal do Decisioning Studio Acessar, você estará pronto para iniciar:

- [Lance seu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent/)
