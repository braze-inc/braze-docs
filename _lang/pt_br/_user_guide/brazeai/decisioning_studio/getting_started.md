---
nav_title: Primeiros passos
article_title: Introdução ao Decisioning Studio
layout: dev_guide
guide_top_header: "Introdução ao Decisioning Studio"
guide_top_text: "Antes de criar um agente de decisão, use estes artigos para orientar seu planejamento e compreensão do Decisioning Studio."
page_order: 0
search_rank: 2
page_type: landing
description: "Esta seção fornece uma introdução ao Decisioning Studio e como você pode usá-lo para projetar e implantar agentes de decisão que otimizam qualquer métrica de negócios."

guide_featured_title: "Artigos de seção"
guide_featured_list:
  - name: Preparando suas Fontes de Dados
    link: /docs/user_guide/brazeai/decisioning_studio/preparing_your_data_sources/
    image: /assets/img/braze_icons/database-01.svg
  - name: Preparando sua Orquestração
    link: /docs/user_guide/brazeai/decisioning_studio/preparing_your_orchestration/
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: Projetando Agentes de Decisão
    link: /docs/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/
    image: /assets/img/braze_icons/settings-01.svg

guide_menu_title: "Additional resources"
guide_menu_list:
  - name: Sobre o Decisioning Studio
    link: /docs/user_guide/brazeai/decisioning_studio/about/
    image: /assets/img/braze_icons/info-circle.svg
  - name: Perguntas Frequentes sobre o Decisioning Studio
    link: /docs/user_guide/brazeai/decisioning_studio/faq/
    image: /assets/img/braze_icons/annotation-question.svg
---

# Introdução ao Decisioning Studio

> Esta referência fornece uma visão geral das etapas envolvidas na configuração do Decisioning Studio, incluindo a conexão de fontes de dados, a configuração da orquestração e o projeto do agente de decisão.

O BrazeAI Decisioning Studio™ permite que você projete e implemente agentes de decisão que otimizam qualquer métrica de negócios. Um agente de decisão é uma configuração personalizada feita sob medida para atender a uma meta comercial específica.

Para isso, você deve conectar fontes de dados, configurar a orquestração e projetar seus agentes de decisão.

{% alert tip %}
Para os clientes do Decisioning Studio Pro, a equipe do IA Expert Services o ajudará a configurar o Decisioning Studio para obter a performance ideal.
{% endalert %}

## Configuração do Decisioning Studio

Para configurar o Decisioning Studio, você deve concluir as seguintes etapas:

### Etapa 1: Conectar fontes de dados

Conecte os perfis dos clientes e os dados de engajamento para que os agentes de decisão que você criar entendam quem é cada cliente e como eles se comportam.

Normalmente, você só precisa conectar suas fontes de dados uma vez, durante a configuração inicial do Decisioning Studio. Se você expandir seus casos de uso posteriormente, talvez seja necessário adicionar novas fontes de dados.

{% alert tip %}
Todos os dados já existentes na [Braze Data Platform]({{site.baseurl}}/user_guide/data/braze_data_platform) estão automaticamente disponíveis para o Decisioning Studio.
{% endalert %}

Para obter orientações detalhadas, consulte a documentação de seu nível do Decisioning Studio:
- [Acessar o Decisioning Studio: Conectar fontes de dados]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Decisioning Studio Pro: Conectar fontes de dados]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/connect_data_sources/)

### Etapa 2: Configurar a orquestração

Integre o Decisioning Studio à sua plataforma de engajamento com clientes (CEP) para permitir que seus agentes orquestrem ações. O CEP é a plataforma usada para oferecer experiências personalizadas aos seus clientes com base nas decisões do agente.

Em geral, você precisa configurar essa orquestração apenas uma vez.

Para obter orientações detalhadas, consulte a documentação de seu nível do Decisioning Studio:
- [Acessar o Decisioning Studio: Configurar a orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)
- [Decisioning Studio Pro: Configurar a orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

### Etapa 3: Projete seus agentes

Configure seus agentes de tomada de decisão para definir quais resultados você deseja maximizar e quais ações o agente pode tomar para alcançá-los. Consulte [Projetando agentes de decisão]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/) para obter orientações detalhadas sobre o projeto de agentes.

Para obter orientações específicas de nível:
- [Acessar o Decisioning Studio: Crie seu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
- [Decisioning Studio Pro: Crie seu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

{% alert tip %}
Para os clientes do Decisioning Studio Pro, a equipe do IA Decisioning Services o ajudará a projetar e lançar seus agentes de decisão.
{% endalert %}

### Etapa 4: Inicie seu agente de decisão

Inicie seu agente de tomada de decisões e permita que ele aprenda e otimize continuamente seus resultados comerciais.

Para obter orientações detalhadas, consulte a documentação de seu nível do Decisioning Studio:
- [Acessar o Decisioning Studio: Lance seu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent/)
- [Decisioning Studio Pro: Lance seu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)

## Próximos passos

Agora que você tem uma compreensão básica dos principais conceitos do Decisioning Studio, pode começar a projetar seu agente de decisão.

- [Projetando agentes de decisão]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/)
