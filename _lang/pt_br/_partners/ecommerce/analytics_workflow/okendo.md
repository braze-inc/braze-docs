---
nav_title: Okendo
article_title: "Okendo"
description: "Aprenda como integrar Okendo com Braze."
page_type: partner
search_tag: Partner
alias: /partners/okendo/
---

# Okendo

> [Okendo](https://okendo.io/) é uma plataforma unificada de marketing de clientes que fornece ferramentas para cultivar a defesa, escalar o boca a boca e maximizar o valor do tempo de vida para mobilizar seus clientes para um crescimento mais rápido e eficiente.

*Esta integração é mantida pela Okendo.*

## Sobre a integração

A integração do Braze com Okendo funciona em vários produtos na plataforma da Okendo, incluindo Avaliações, Fidelidade, Referências, Pesquisas e Questionários. Okendo envia eventos personalizados e atributos de usuário para o Braze, que podem ser usados para personalizar e disparar mensagens.  

## Pré-requisitos

| Requisito            | Descrição                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Conta Okendo         | Uma conta Okendo é necessária para aproveitar esta parceria.        |
| Chave da API REST do Braze     | Uma chave da API REST da Braze com permissões `users.track`. Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze    | [Sua URL de endpoint REST.]({{site.baseurl}}/api/basics/#endpoints) Seu endpoint depende do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Configurar o Conector Braze no Okendo

1. No Okendo, vá para **Configurações** > **Integrações** > **Email & SMS** > **Braze**
2. Adicione o endpoint da API e a chave da API nas configurações de **Integração**.

### Etapa 2: Configure seu identificador

O campo `external_id` é usado para identificar o usuário associado a cada evento. Ative **Usar ID de Cliente Shopify para identificação de usuário Braze** para associar o campo com IDs de Cliente Shopify. Caso contrário, desative para associá-lo ao endereço de e-mail de cada usuário.

## Sincronizando eventos e atributos do Okendo para o Braze

### Eventos personalizados

{% alert note %}
Para dados de eventos de exemplo, consulte [documentação da Okendo](https://support.okendo.io/en/articles/10396885-getting-started-with-braze-and-okendo#h_679a212e3c).
{% endalert %}

#### Eventos de revisão

- Revisão Okendo Criada
- Solicitação de Revisão Okendo

#### Eventos de referência

- Referência enviada Okendo
- Optou por referências Okendo
- Convite de referência Okendo
- Cupom de referência Okendo recebido
- Cupom de referência Okendo resgatado
- Referência Okendo rejeitada

#### Eventos de fidelidade

- Inscrito no programa de fidelidade Okendo
- Pontos de fidelidade Okendo concedidos
- Pontos de fidelidade Okendo resgatados
- Nível de fidelidade Okendo alterado
- Pontos de fidelidade Okendo ajustados

#### Evento de pesquisa

- Pesquisa Okendo enviada

#### Evento de quiz

- Quiz Okendo enviado

### Atributos personalizados

Okendo envia dados do perfil do usuário como atributos personalizados no Braze, que podem ser usados para criar segmentos de público. Os exemplos incluem:

- Perguntas de perfil feitas em pesquisas e durante a submissão de uma avaliação, como idade, aniversário, tipo de pele e cor do cabelo
- Métricas de avaliação como _Classificação média da avaliação_ e _Sentimento médio da avaliação_
- Métricas de fidelidade, como _Saldo de Pontos_ e _Nível VIP_
- Métricas de referências, como o _Número de Referências Bem-Sucedidas_ e _Receita Total de Referências_  
- Pontuação NPS coletada de uma pesquisa

## Usando Braze com produtos Okendo

Dependendo do produto Okendo, você deve completar etapas adicionais para usar Braze e Okendo juntos. Consulte os seguintes artigos para mais detalhes:

- [Integrando Avaliações com Braze](https://support.okendo.io/en/articles/10509722-integrating-reviews-with-braze#h_09c4575b39)
- [Integrando Fidelidade com Braze](https://support.okendo.io/en/articles/10509615-integrating-loyalty-with-braze#h_47129ea105)
- [Integrando Referências com Braze](https://support.okendo.io/en/articles/10509748-build-a-canvas-in-braze-to-trigger-referral-emails#h_32fb5ba542)
- [Integrando Pesquisas com Braze](https://support.okendo.io/en/articles/11546662-integrating-surveys-with-braze)
- [Integrando Questionários com Braze](https://support.okendo.io/en/articles/10509739-build-a-canvas-in-braze-to-send-quiz-recommendations#h_53748cb121)

{% alert note %}
Para assistência na configuração da integração, entre em contato com a equipe de suporte da Okendo.
{% endalert %}
