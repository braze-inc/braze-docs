---
nav_title: Talon.One
article_title: Talon.One
alias: /partners/talonone/
description: "Este artigo de referência descreve a parceria entre a Braze e a Talon.One, um mecanismo de promoção que permite lançar campanhas contextuais individualizadas de cupom, indicação, desconto e fidelidade de forma rápida e eficiente."
page_type: partner
search_tag: Partner

---

# Talon.One

> A [Talon.One](https://talon.one/) fornece incentivos personalizados para o seu CRM de marketing para mobile e permite lançar campanhas contextuais individualizadas de cupom, indicação, desconto e fidelidade de forma rápida e eficiente.

_Esta integração é mantida por Talon.One._

## Sobre a integração

A integração entre Braze e Talon.One pode ajudar a levar seu programa de fidelidade ou de cupons para o próximo nível, enviando códigos gerados pelo Talon.One para seu público por meio do Braze Connected Content.


## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
|Conta Talon.One | É necessário ter uma conta no site Talon.One para aproveitar essa parceria. |
|Talon.One chave de API | Em Talon.One, em **Configurações** > **Configurações do desenvolvedor**, crie uma chave de API de terceiros do Braze para a integração. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert warning %}
A Talon.One **_requer_** um limite de frequência máximo de 2.500 mensagens por minuto. Esse limite de frequência pode ser [modificado]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting) no dashboard da Braze.
{% endalert %}

## Integração

1. Visite a [documentação do siteTalon.One ](https://docs.talon.one/docs/dev/technology-partners/braze) para obter orientação sobre como configurar sua integração, como usar o endpoint de cupom da API Talon.One e onde encontrar os modelos de Connected Content necessários para suas mensagens do Braze.
2. Para aproveitar os outros recursos que a Talon.One oferece, como pontos de fidelidade e indicações, visite os artigos a seguir:
  - [Adicionar pontos de fidelidade pela Braze](https://docs.talon.one/docs/dev/technology-partners/braze/adding-loyalty-points-braze)
  - [Obter um registro de fidelidade na Braze](https://docs.talon.one/docs/dev/technology-partners/braze/receiving-loyalty-ledger-braze)
  - [Criar cupons via Braze](https://docs.talon.one/docs/dev/technology-partners/braze/creating-coupons-braze)
  - [Criar indicações via Braze](https://docs.talon.one/docs/dev/technology-partners/braze/creating-referrals-braze)
  - [Criar uma promoção de aniversário via Braze](https://docs.talon.one/docs/dev/technology-partners/braze/bday-promotion-braze)

