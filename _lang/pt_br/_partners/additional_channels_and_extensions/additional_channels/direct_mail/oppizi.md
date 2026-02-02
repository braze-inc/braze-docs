---
nav_title: Oppizi
article_title: Oppizi 
alias: /partners/oppizi/
description: "Este artigo de referência descreve a parceria entre a Braze e a Oppizi."
page_type: partner
search_tag: Partner
---

# Oppizi

> [Oppizi](https://www.oppizi.com/) é o líder global em marketing offline, fornecendo uma solução completa para empresas realizarem campanhas de mala direta e distribuição de panfletos mensuráveis e direcionadas.

_Esta integração é mantida pela Oppizi._

## Pré-requisitos

| Requisito                    | Descrição                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------- |
| Conta da Oppizi                 | Uma conta ativa da Oppizi é necessária para usar esta integração.                 |
| Chave de API da Oppizi                 | Encontrada na sua conta da Oppizi em **Integrações** > **Braze**.                |
| ID do fluxo de trabalho de mala direta da Oppizi | Crie um fluxo de trabalho na Oppizi na página **Fluxo de Trabalho de Mala Direta** para obter um ID. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Com a integração da Oppizi, você pode:

* **Enviar postais de mala direta automatizados** usando gatilhos da Braze conectados ao webhook da Oppizi e fluxos de trabalho de mala direta.
* **Configurar limites, ondas e limites** nos fluxos de trabalho de mala direta da Oppizi para controlar o envio de suas campanhas.
* **Projetar postais profissionais** com a ferramenta de design integrada da Oppizi—sem experiência em design necessária.
* **Rastrear o desempenho da campanha** em tempo real com o dashboard da Oppizi.

## Integração

### Etapa 1: Gere sua chave de API da Oppizi 

Para usar seu modelo de webhook na Braze, você primeiro precisará gerar sua chave de API da Oppizi.

1. Faça login na Oppizi.
2. Acesse **Integrações** > **Braze**.
3. Gere sua chave de API.

Você pode gerenciar, revogar e criar suas chaves a partir desta página conforme necessário.

### Etapa 2: Crie um modelo de webhook Braze

Em seguida, crie um modelo de webhook para Oppizi no Braze para usar em campanhas futuras ou Canvases.

1. No Braze, acesse **Templates** > **Webhook templates**.

No seu modelo de webhook, preencha os seguintes campos:

- **Webhook URL:** ```https://webhooks.oppizi.com/events```
- **Corpo da solicitação:** **Texto bruto**

Para o método de solicitação e cabeçalhos, a Oppizi requer um método HTTP juntamente com os seguintes cabeçalhos HTTP a serem incluídos no modelo. Preencha os seguintes campos:

- **Método HTTP:** POST
- **Cabeçalhos de solicitação:**
  - **Autorização:** `Bearer <oppiziAPIKey>`
  - **Content-Type:** `application/json`

![Um exemplo do cabeçalho de webhook da Oppizi no Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_headers.png %})

Para o **Corpo da Solicitação**, você deve incluir o campo **oppiziWorkflowID**. Este ID é gerado quando um fluxo de trabalho é criado na Oppiz e é necessário para especificar a qual fluxo de trabalho de mala direta seus destinatários devem ser adicionados. Cada fluxo de trabalho de mala direta na Oppizi tem um ID exclusivo, então, se você criar um modelo de webhook da Oppizi no Braze, certifique-se de sempre atualizar o ID do fluxo de trabalho para o correto.

{% alert note %}
Verifique se os atributos personalizados necessários estão configurados na sua conta Braze para os endereços postais dos seus destinatários, pois estes são necessários para o envio de mala direta.
{% endalert %}

![Um exemplo de um modelo de webhook da Oppizi no Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_example.png %})

O seguinte é um exemplo de corpo de solicitação:

{% raw %}
```json
{
    "event" : "workflow.addRecipient",
    "oppiziWorkflowID" : "<oppiziWorkflowID>",
    "requestType" : "live",
    "recipient" : {
        "recipientID" : "{{${braze_id}}}",
        "firstName" : "{{${first_name}}}",
        "lastName" : "{{${last_name}}}",
        "address1" : "{{custom_attribute.${address1}}}",
        "address2" : "{{custom_attribute.${address2}}}",
        "city" : "{{custom_attribute.${city}}}",
        "country" : "{{${country}}}",
        "zipCode" : "{{custom_attribute.${zipCode}}}",
        "state" : "{{custom_attribute.${state}}}"
    }
}
```
{% endraw %}

### Etapa 3: Crie um Fluxo de Trabalho de Mala Direta na Oppizi

1. Na Oppizi, acesse **Fluxo de Trabalho de Mala Direta** > **Criar fluxo de trabalho**
2. Configure os detalhes do fluxo de trabalho, incluindo limites, ondas, formato do cartão postal e arte.
3. Na seção de detalhes do webhook, você encontrará um corpo de solicitação pronto para uso, incluindo seu ID de fluxo de trabalho, que pode colar diretamente no Braze.

### Etapa 4: Prévia e teste sua solicitação no Braze

Após adicionar seu corpo de solicitação com o ID de fluxo de trabalho da Oppizi, execute um teste para confirmar que sua configuração está funcionando como esperado.

Para executar o teste, atualize `requestType` de `live` para `test` no corpo da solicitação. Nota que este passo é crucial para evitar adicionar destinatários de teste ao seu público de mala direta.

Depois de terminar os testes, atualize `requestType` de volta para `live` e salve seu Canva. Agora, você está pronto para lançar suas campanhas automatizadas de mala direta.
