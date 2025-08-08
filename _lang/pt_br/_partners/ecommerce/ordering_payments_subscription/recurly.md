---
nav_title: Recurly
article_title: Recurly
description: "A Recurly é a principal plataforma de gerenciamento e faturamento de inscrições para marcas diretas ao consumidor que buscam aumentar suas inscrições e receitas recorrentes."
alias: /partners/recurly/
page_type: partner
search_tag: partner
---

# Recurly

> A [Recurly](https://recurly.com/) é uma plataforma de gerenciamento de inscrições e faturamento. A plataforma integrada da Recurly simplifica a automação do ciclo de vida da inscrição em escala, ativando as equipes para gerenciar e otimizar a experiência do inscrito - desde o teste de novos planos, ofertas e promoções até o gerenciamento de métodos de pagamento, integrações e insights.

_Essa integração é mantida pelo Recurly._

## Sobre a integração

A integração entre a Recurly e a Braze simplifica o processo de compartilhamento de dados de inscrição com a Braze, pois permite a comunicação direcionada com os clientes.

- Use os eventos do ciclo de vida da inscrição da Recurly (como renovações, pausas ou cancelamentos de inscrição) na Braze para disparar campanhas e comunicações personalizadas.
- Aproveite os dados de inscrição do Recurly (por exemplo, planos de inscrição, complementos ou status) para criar e gerenciar usuários, segmentos e canvas do Braze para executar campanhas e comunicações específicas do coorte.
- Envie dados da Recurly diretamente para a Braze para ter acesso a mais casos de uso de envio de mensagens e diminuir os custos indiretos de desenvolvimento.

Consulte a [documentação da Recurly](https://docs.recurly.com/docs/braze-integration) para saber mais sobre como usar a Recurly com a Braze.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Recurly | Para aproveitar essa parceria, é necessário ter um plano de inscrição Elite [Recurly](https://recurly.com/) com a capacitação do recurso Braze. A ativação de faturas de crédito na sua plataforma da Recurly também é necessária.|
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. Como a Recurly usa apenas o endpoint `users.track`, recomendamos o provisionamento de uma chave específica da Recurly somente com essa permissão. |
| Ponto de extremidade REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância. |

## Integração

Antes de começar, verifique se você tem contas ativas na Braze e na Recurly.

### Conectar o Recurly ao Braze

1. No Recurly, acesse **Integrações** > **Braze**. Ao navegar pela primeira vez na página de configuração da integração do Braze no Recurly, a interface solicitará que você conecte os dois sistemas.

2. Forneça as seguintes credenciais:

- **URL da instância:** O endpoint Braze REST da instância para a qual você está provisionado.
- **Chave de API (identificador):** A chave da API REST da Braze que a Recurly deve usar ao enviar solicitações à Braze.

Lembre-se de copiar o URL de sua instância do Braze. Por exemplo, seu URL pode ter a seguinte aparência: 

```
<https://dashboard-03.braze.com/dashboard/app_usage?locale=en>
```

{:start="3"}
3\. Depois de inserir suas credenciais, clique em **Connect (Conectar**).

## Usando essa integração

### Identificadores suportados

A Recurly usa o endereço `account_code` de uma conta como `external_id` na Braze. Por isso, o `account_code` das suas contas da Recurly deve corresponder ao `external_id` do seu usuário da Braze.

### Eventos personalizados

Para um engajamento eficaz do cliente, você deve [configurar eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) no Braze para receber eventos disparados pelo Recurly. Inclua cada evento da Recurly para obter uma integração completa dos dados. Esses eventos também podem ser rastreados na [análise de dados do Braze]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics). Uma vez configurados, esses eventos personalizados podem ser usados para segmentar usuários ou personalizar o envio de mensagens. 

| Evento personalizado Braze| Evento da Recurly |
| ----------- | ----------- |
| Nova inscrição na Recurly              | Disparado quando uma inscrição é criada                            |
| Inscrição renovada na Recurly          | Disparado quando uma inscrição é renovada                                |
| Inscrição atualizada na Recurly          | Disparado quando as atribuições de uma inscrição mudam (mudança de plano, mudança de preço ou mudança de quantidade) |
| Recurly cancelada na inscrição         | Disparado quando uma inscrição é cancelada                           |
| Inscrição reativada na Recurly      | Disparado quando uma assinatura cancelada é reativada               |
| Inscrição pausada na Recurly           | Disparado quando uma inscrição é definida para ser pausada                   |
| Inscrição retomada na Recurly          | Disparado quando a pausa de uma inscrição é removida                              |
| Inscrição expirada na Recurly          | Disparado quando uma inscrição expira                               |
| Fatura criada na Recurly               | Disparado quando uma fatura é criada                                |
| Pagamento bem-sucedido do Recurly            | Disparado quando uma fatura é coletada com sucesso                 |
| Reembolso emitido na Recurly                 | Disparado quando um reembolso é emitido                                   |
| Pagamento recorrente com falha na Recurly      | Disparado quando uma fatura falha para uma renovação de inscrição          |

### Loteamento e limite de frequência

Como a Recurly usa o endpoint `/users/track` da Braze, a integração está sujeita aos limites de frequência padrão de 50.000 solicitações por minuto da Braze.

O Recurly agrupa determinados eventos do ciclo de vida da inscrição como chamadas únicas de API para o Braze para reduzir o número de chamadas feitas.

- A criação de várias inscrições ao mesmo tempo é agrupada e enviada ao Braze como uma única solicitação.
- Quando várias inscrições são renovadas ao mesmo tempo para uma conta, todas essas renovações são agrupadas em uma única solicitação.
- Os eventos do ciclo de vida da inscrição no mesmo modelo são enviados como uma única solicitação. Por exemplo, uma fatura recém-criada com um pagamento enviaria uma única solicitação de API com os eventos personalizados `Recurly Invoice Created` e `Recurly Successful Payment`.

Os lotes são enviados à Braze em grupos de até 75 eventos por vez. Por exemplo, se 100 inscrições fossem criadas de uma vez, a Recurly faria duas solicitações de API para a Braze. Consulte [como agrupar solicitações de rastreamento de usuários em lote]({{site.baseurl}}/api/api_limits/#batch-user-track) para obter detalhes.


