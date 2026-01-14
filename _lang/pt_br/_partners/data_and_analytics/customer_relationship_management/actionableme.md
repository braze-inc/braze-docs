---
nav_title: actionable.me
article_title: actionable.me
description: "Este artigo de referência descreve a parceria entre a Braze e a actionable.me, uma solução proprietária de software e processos, que permite aproveitar ao máximo seu investimento na Braze imediatamente."
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> [actionable.me](https://actionable.me), construído pela equipe da Massive Rocket, uma agência de dados e CRM, é uma abordagem padronizada e automatizada para executar programas de CRM, fornecendo ferramentas e processos projetados para levar os clientes da Braze a obter valor de forma rápida, consistente e previsível. 

_Essa integração é mantida por actionable.me._

## Sobre a integração

A integração entre a Braze e a actionable.me permite implantar um serviço para monitorar seu progresso na utilização da Braze. Por meio de uma combinação de ferramentas e processos, eles irão rapidamente avaliar a performance do seu CRM, identificar novas oportunidades e fornecer recomendações sobre como melhorar o desempenho.

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
| Conta actionable.me | Uma conta actionable.me é necessária para aproveitar esta parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com as permissões listadas na próxima seção.<br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Para integrar a Braze e a actionable.me, a plataforma actionable.me deve ser configurada, e é preciso criar uma chave de API da Braze na Braze e configurá-la no dashboard da actionable.me.

### Etapa 1: Crie sua chave de API da Braze

Na Braze, navegue para **Configurações** > **Chaves de API**. Selecione **Criar nova chave de API** e confirme se as seguintes permissões foram adicionadas:

- `campaigns.list`
- `campaigns.data_series`
- `campaigns.details`
- `sends.data_series`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `events.list`
- `canvas.list`
- `canvas.data_series`
- `canvas.details`
- `canvas.data_summary`
- `kpi.mau.data_series`
- `kpi.dau.data_series`
- `kpi.new_users.data_series`
- `kpi.uninstalls.data_series`

### Etapa 2: Forneça informações para a equipe actionable.me

Para concluir a integração, forneça a chave da API REST e o [URL do endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) para sua equipe de operações da actionable.me. Em seguida, a actionable.me estabelece a conexão e avisa quando a configuração fica pronta. Ela também entrará em contato para começar a compartilhar insights.

![A página actionable.me "add platform" (adicionar plataforma) que a equipe de operações actionable.me configurará.]({% image_buster /assets/img/actionableme/image2.png %})

## Solução de problemas

Entre em contato com a equipe da actionable.me ou da Massive Rocket obter mais ajuda: [info@massiverocket.com](mailto:info@massiverocket.com)


