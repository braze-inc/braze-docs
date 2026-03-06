---
nav_title: Configurar orquestração
article_title: Configurar orquestração
page_order: 2
description: "Aprenda como configurar a orquestração para agentes do Decisioning Studio Pro para ativar comunicações personalizadas."
toc_headers: h2
---

# Configurar orquestração

> Os agentes de decisão precisam se conectar a uma Plataforma de Engajamento com Clientes (CEP) para orquestrar comunicações uma vez que tenham ingerido dados de cliente e personalizado em um nível 1:1. Este artigo explica como configurar a integração para cada CEP suportado.

## CEPs suportados

O Decisioning Studio Pro suporta as seguintes Plataformas de Engajamento com Clientes:

| CEP | Tipo de integração | Complexidade de configuração |
|-----|-----------------|------------------|
| **Braze** | Integração de API nativa | Baixa (recomendado) |
| **Salesforce Marketing Cloud** | Eventos de API nativa + Jornadas | Média |
| **Klaviyo** | Eventos de API nativa + Fluxos | Média |
| **Outros CEPs** | Personalizado (arquivo de recomendação) | Alta |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Selecione seu CEP abaixo para começar com a configuração da integração.

{% tabs %}
{% tab Braze %}

## Configurando a integração do Braze

Siga estas etapas para integrar um agente do Decisioning Studio do Braze com as capacidades de orquestração do Braze (a equipe de serviços do Braze estará disponível para ajudar):

### Etapa 1: Crie uma chave de API

Acessar **Configurações** > **Chaves de API**, em seguida, crie uma nova chave com as seguintes permissões:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Etapa 2: Configurar campanhas acionadas por API

Configurar uma campanha acionada por API para cada modelo base com propriedades de acionamento de API para todas as dimensões otimizadas.

Um modelo base é qualquer modelo que o Agente de Decisão pode usar para orquestrar mensagens. Um Agente de Decisão pode ter 1 modelo base ou múltiplos, caso em que escolher o modelo base certo para cada cliente será uma das decisões que o agente personaliza.

### Etapa 3: Configurar re-elegibilidade

Garantir que todas as campanhas acionadas por API permitam que os usuários se tornem re-elegíveis em até 15 minutos.

![Diagrama do Pro de Decisão]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Embora o agente do Estúdio de Decisão nunca envie a mesma campanha mais de uma vez por dia, você vai querer ter a capacidade de enviar as mesmas campanhas várias vezes em um dia para fins de teste.
{% endalert %}

### Etapa 4: Adicionar marcadores dinâmicos

Esses servem como marcadores dinâmicos para decisões que o agente do Estúdio de Decisão está otimizando.

#### Exemplo 1: Campanha de e-mail

Suponha que o agente do Estúdio de Decisão esteja otimizando uma campanha de e-mail. Isso pode ser configurado assim:

![Diagrama do Pro de Decisão]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

Supondo que o agente esteja otimizando a escolha de modelos e a mensagem de Chamada para Ação (CTA), então uma campanha acionada por API deve ser criada para cada modelo, e a seção de CTA de um modelo pode parecer assim:

![Diagrama do Pro de Decisão]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### Exemplo 2: Campanha Push

Suponha que um agente do Estúdio de Decisão esteja otimizando a mensagem de uma campanha Push. Isso pode ser configurado assim:

![Diagrama do Pro de Decisão]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Diagrama do Pro de Decisão]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

Resultando na seguinte mensagem:

![Diagrama do Pro de Decisão]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Exemplo 3: Campanha de SMS

Suponha que o agente do Estúdio de Decisão esteja otimizando campos em uma campanha de SMS. Isso pode ser configurado assim:

![Diagrama do Pro de Decisão]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Diagrama do Pro de Decisão]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

Resultando na seguinte mensagem:

![Diagrama do Pro de Decisão]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configurando a integração do SFMC

O Decisioning Studio Pro suporta integração nativa com o Salesforce Marketing Cloud. O Decisioning Studio dispara eventos da API em uma jornada com os dados necessários para preencher elementos dinâmicos.

A configuração da orquestração para o SFMC é semelhante tanto para o Decisioning Studio Pro quanto para o Decisioning Studio Go. Para etapas detalhadas para configurar a integração do SFMC, siga as [instruções do SFMC]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) na documentação do Decisioning Studio Go.

{% endtab %}
{% tab Klaviyo %}

## Configurando a integração do Klaviyo

O Decisioning Studio Pro suporta integração nativa com o Klaviyo. O Decisioning Studio dispara eventos da API em um fluxo com os dados necessários para preencher elementos dinâmicos.

A configuração da orquestração para o Klaviyo é semelhante tanto para o Decisioning Studio Pro quanto para o Decisioning Studio Go. Para etapas detalhadas para configurar a integração do Klaviyo, siga as [instruções do Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) na documentação do Decisioning Studio Go.

{% endtab %}
{% tab Other CEPs %}

## Configurando outras integrações de CEP

O Decisioning Studio pode se integrar com qualquer plataforma de engajamento com clientes. No entanto, isso pode exigir algum trabalho de engenharia personalizado da sua equipe, uma vez que o Decisioning Studio não pode disparar comunicações diretamente.

Neste cenário, o agente entregará um "arquivo de recomendação." Este arquivo contém linhas para cada cliente, com colunas que indicam todas as decisões personalizadas para aquele cliente.

Por exemplo, o seguinte arquivo de recomendação:

![Diagrama do Pro de Decisão]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

Pode ser usado para otimizar uma campanha de e-mail que se parece com o seguinte:

![Diagrama do Pro de Decisão]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## Próximos passos

Após configurar a orquestração, prossiga para projetar seu agente:

- [Crie seu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

