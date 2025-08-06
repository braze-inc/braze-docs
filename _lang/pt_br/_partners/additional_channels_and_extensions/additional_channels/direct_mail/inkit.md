---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "Este artigo de referência descreve a parceria entre a Braze e a Inkit, que permite a você economizar tempo e esforço com a automatização de campanhas de mala direta e recuperação de clientes offline."
page_type: partner
search_tag: Partner

---

# Inkit

> A [Inkit](https://www.inkit.com) e a Braze ajudam organizações a gerar e distribuir documentos de forma segura, tanto em meio digital quanto por mala direta.

_Essa integração é mantida pela Inkit._

## Sobre a integração

A integração entre o Braze e o Inkit permite gerar documentos e enviá-los por mala direta aos usuários do Braze com webhooks do Braze.

## Pré-requisitos

|Requisito| Descrição|
| ---| ---|
|Conta da Inkit | É necessário ter uma [conta Inkit](https://www.inkit.com/) para aproveitar essa parceria. |
| Chave de API da Inkit<br><br>`<INKIT_API_TOKEN>` | Essa chave pode ser encontrada no [dashboard da Inkit](https://app.inkit.io/#/account/integrations), na guia **Desenvolvimento**, e ativará a conexão das contas Braze e Inkit.|
| ID de modelo da Inkit<br><br>`<INKIT_TEMPLATE_ID>` | Depois de criar um modelo, você pode copiar o ID do modelo da guia **Modelos** para usá-lo em seu modelo no Braze.<br><br>Por exemplo, você pode criar um modelo chamado `invoice_template` no ambiente da Inkit com o ID de modelo `tmpl_3bDScFl9cwr3OAVR1RSdEC`.
| Cabeçalho HTTP | O cabeçalho HTTP faz parte da solicitação da API que você envia da Braze para a Inkit. Nele, você incluirá sua chave de API da Inkit para autenticar e autorizar chamadas para a API da Inkit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integração

### Etapa 1: crie um modelo da Inkit

Na plataforma da Inkit, crie um modelo para ser usado na sua campanha da Braze em HTML, Word, PowerPoint, Excel ou PDF. Consulte [a documentação do Inkit](https://docs.inkit.com/docs/create-a-template) para saber mais.

### Etapa 2: Crie seu modelo de webhook do Braze

Para criar um modelo de webhook Inkit a ser usado em futuras campanhas ou Canvas, navegue até **Modelos** > **Modelos de webhook** na plataforma Braze. 

Se você quiser criar uma campanha única de webhook Inkit ou usar um modelo existente, selecione **Webhook** no Braze ao criar uma nova campanha.

![Uma seleção de modelos de webhook predefinidos disponíveis na guia Modelos de webhook da seção Modelos e mídias.]({% image_buster /assets/img/inkit-webhook-template.png %})

Depois de selecionar o modelo de webhook da Inkit, você verá o seguinte:
- **URL do webhook**: Em branco
- **Corpo da solicitação**: Texto bruto

No campo de URL do webhook, você precisará [criar](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event) e inserir um URL do webhook da Inkit.

![O código do corpo da solicitação e o URL do webhook são mostrados na guia do criador de webhooks do Braze.]({% image_buster /assets/img/inkit-integration.png %})

#### Cabeçalhos e método da solicitação

A Inkit requer um `HTTP Header` para autorização que inclua sua chave de API da Inkit codificada em base 64. O seguinte já estará incluído no modelo como um par de valores-chave, mas na guia **Settings (Configurações)**, você deve substituir o `<INKIT_API_TOKEN>` pela sua chave de API do Inkit.

{% raw %}
- **Método HTTP**: POST
- **Cabeçalho da solicitação**:
  - **Autorização**: Básico `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Content-Type**: application/json
{% endraw %}

#### Corpo da solicitação

Certifique-se de que seu Liquid corresponda aos atributos personalizados adequados associados aos seguintes campos obrigatórios e opcionais. Você também pode adicionar campos de dados personalizados a qualquer solicitação.

```json
{% raw %}{
  "api_token": "<INKIT_API_TOKEN>",
  "template_id": "<INKIT_TEMPLATE_ID>",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "company": "{{custom_attribute.${company_name}}}",
  "phone" : "{{${phone_number}}}",
  "address_line_1": "{{custom_attribute.${address}}}",
  "address_line_2": "{{custom_attribute.${address2}}}",
  "address_city": "{{${city}}}",
  "address_state": "{{custom_attribute.${state}}}",
  "address_zip": "{{custom_attribute.${zip}}}",
  "address_country": "{{${country}}}",
  "source" : "Braze"
}{% endraw %}
```

### Etapa 3: veja uma prévia da sua solicitação

Seu texto bruto será automaticamente destacado se for uma tag Braze aplicável. As tags `street`, `unit`, `state` e `zip` devem ser configuradas como [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes) para enviar esse Webhook.

Pré-visualize a solicitação no painel **Preview (Pré-visualização** ) ou navegue até a guia **Test (Teste** ), onde é possível selecionar um usuário aleatório, um usuário existente ou personalizar o seu próprio usuário para testar o webhook.

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Modelos de webhook salvos** ao criar uma nova [campanha de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}


