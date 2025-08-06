---
nav_title: Datadog
article_title: "Datadog"
description: "Este artigo de referência descreve a parceria com a Braze e a Datadog, um serviço de observabilidade para aplicativos em escala de nuvem, fornecendo monitoramento de servidores, bancos de dados, ferramentas e serviços por meio de uma plataforma de análise de dados baseada em SaaS."
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [O Datadog](https://www.datadoghq.com/) é um serviço de observabilidade para aplicativos em escala de nuvem, que fornece monitoramento de servidores, bancos de dados, ferramentas e serviços por meio de uma plataforma de análise de dados baseada em SaaS.

A integração entre o Braze e o Datadog permite que os clientes coletem dados do Braze no Datadog e criem alertas sobre os dados que enviamos. Por exemplo, configurar um monitor e um alerta se sua campanha de mensagens semanais enviar um volume anormalmente baixo de mensagens ou se uma etapa do Canva que normalmente envia apenas algumas mensagens por dia começar a enviar milhares. 

## Pré-requisitos 

| Requisito | Descrição |
|---|---|
| Conta do Datadog | É necessário ter uma conta da Datalog para usar a parceria. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Gerar a chave do Datadog

Na Datadog, você precisará criar uma [chave de API](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys). Para adicionar uma chave de API, navegue até **Configurações da organização** > **Chaves de API** > **Nova chave**.

### Etapa 2: Adicionar chave ao Braze

No dashboard da Braze, navegue até **Integração com parceiros** > **Parceiros de tecnologia** e, em seguida, pesquise **Datadog**. Na página de parceiro da Datadog, forneça a chave de API da Datadog. Isso criará uma conexão para permitir que o Braze envie dados para o Datadog.

## Eventos do Braze

Depois que a conexão for integrada, a Braze enviará os seguintes eventos à Datadog:

- `braze.messaging.sent` - A contagem de envios

Cada um desses eventos terá metadados na forma de tags do Datadog para fornecer informações como:

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (se disponível)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (se disponível)

Esses eventos e tags podem ser monitorados na página **Explorador de métricas** (Metrics Explorer). Essas métricas são registradas como [distribuições](https://docs.datadoghq.com/metrics/distributions/) para o DataDog. Dada a natureza das métricas e a imprecisão das agregações e rollups da DataDog, o Braze não tenta novamente erros de rede intermitentes ou outros erros da API da DataDog que possam ser encontrados durante a transmissão. Isso significa que essas contagens métricas podem diferir ligeiramente das contagens vistas no dashboard do Braze e/ou no Currents.

![]({% image_buster /assets/img/datadog.png %})

