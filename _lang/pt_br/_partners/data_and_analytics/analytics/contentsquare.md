---
nav_title: Contentsquare
article_title: Contentsquare
description: "Este artigo de referência descreve a parceria entre o Braze e a Contentsquare, uma plataforma de análise de dados de experiência digital que permite melhorar a relevância e as taxas de conversão de suas campanhas por meio do direcionamento de mensagens com base na experiência digital de seus clientes."
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# Contentsquare

> [A Contentsquare](https://contentsquare.com/) é uma plataforma de análise de dados de experiência digital que ativa uma compreensão sem precedentes da experiência do cliente.

_Essa integração é mantida pela Contentsquare._

## Sobre a integração

A integração entre o Braze e o Contentsquare permite que você envie sinais ao vivo (fraude, sinais de frustração, etc.) como eventos personalizados no Braze. Aproveite os insights da experiência do Contentsquare para melhorar a relevância e as taxas de conversão de suas campanhas, direcionando mensagens com base na experiência digital e na linguagem corporal de seus clientes.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Contentsquare | É necessário ter uma conta no Contentsquare para aproveitar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. Para criar uma nova chave no dashboard do Braze, acesse **Configurações** > **Chaves de API**. |
| Endpoint REST  do Braze | [Seu URL do ponto de extremidade REST]({% image_buster /assets/img/contentsquare_custom_events.png %}). Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Alguns casos de uso comuns do Braze e do Contentsquare incluem:
- Hiperpersonalize as mensagens com base na intenção do cliente, exibindo os dados de experiência do cliente na Braze.
- Redirecione os clientes com base nas características de comportamento digital, hesitações, frustrações e intenções demonstradas por eles.
- Identifique experiências ruins no Contentsquare e recupere clientes com mensagens direcionadas e ofertas de retenção.
- Recupere clientes em risco enviando mensagens mais relevantes e empáticas no momento e local certos.

## Integração

Para integrar o Contentsquare ao Braze, você deve solicitar a instalação de uma integração "Live Signals" no catálogo de integração do Contentsquare:

1. No Contentsquare, clique em **Console** no menu **Settings (Configurações** ). Isso o redirecionará para o projeto em que está trabalhando no momento. 
2. Na página **Projetos**, acesse a guia **Integrações** e clique no botão **\+ Adicionar integração**.
3. No catálogo de integrações, localize a integração **Live Signals** e clique em **Add** (Adicionar). A equipe da Contentsquare entrará em contato para configurar o snippet de código para enviar sinais em tempo real para a Braze.
4. O Contentsquare agora processará sua integração. O texto do indicador será atualizado após a conclusão da integração.

Para saber mais, consulte [Solicitar uma integração da Contentsquare](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186).

## Usando essa integração

Quando a integração estiver concluída, os eventos personalizados do Contentsquare estarão disponíveis para uso em suas campanhas e Canvas. Você pode verificar quais eventos estão sendo enviados ao Braze em **Data Settings** > **Custom Events** (Configurações de dados > Eventos personalizados).

![Dados de sinais ao vivo do Contentsquare na guia Eventos personalizados do Braze]({% image_buster /assets/img/contentsquare_custom_events.png %})


