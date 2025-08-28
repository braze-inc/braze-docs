---
nav_title: Optilyz
article_title: Optilyz
description: "Este artigo de referência descreve a parceria entre a Braze e a optilyz, que permite executar campanhas de mala direta mais sustentáveis, lucrativas e centradas no cliente."
alias: /partners/optilyz/
page_type: partner
search_tag: Partner

---

# Optilyz

> A [optilyz](https://optilyz.com) é uma plataforma de automação de mala direta que permite executar campanhas de mala direta mais sustentáveis, lucrativas e centradas no cliente. 

_Essa integração é mantida pela Optilyz._

## Sobre a integração

Use a integração entre a optilyz e a Braze para enviar mala direta a seus clientes, como cartas, cartões postais e self-mailers.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
|Conta Optilyz | Uma conta da optilyz é necessária para usar essa parceria. |
| Chave de API da optilyz<br><br>`<OPTILYZ_API_KEY>`| Seu gerente de sucesso do cliente da optilyz fornecerá sua chave de API da optilyz.<br><br>Essa chave de API permitirá que você conecte suas contas da Braze e da optilyz. |
| ID de automação Optilyz<br><br>`<OPTILYZ_AUTOMATION_ID>` | A ID de automação pode ser encontrada em uma caixa no cabeçalho da página.<br><br>Depois de criar o cadastro na optilyz, você poderá navegar até a automação para a qual deseja enviar dados.<br>A automação deve ser ativada primeiro. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Casos de uso

Operar a mala direta como um canal digital significa afastar-se das correspondências em massa e aproveitar o canal como parte de suas jornadas (digitais) do cliente. Os benefícios de uma abordagem moderna à mala direta são:
- Aumento das taxas de conversão por meio de maior relevância, casos de uso adicionais, Testes A/B mais fáceis e efeitos entre canais
- Menos esforço por meio da automação e de uma solução de ponta a ponta
- Redução de custos por meio de contratos-quadro e transparência de custos

## Integração

Para integrar com a optilyz, use a [API da optilyz](https://www.optilyz.com/doc/api/) para enviar dados do destinatário para o webhook da Braze.

### Etapa 1: Crie seu modelo de webhook do Braze

Para criar um modelo de webhook Optilyz para ser usado em futuras campanhas ou Canvas, navegue até **Modelos** > **Modelos de webhook** na plataforma Braze. 

Se você quiser criar uma campanha única de webhook Optilyz ou usar um modelo existente, selecione **Webhook** no Braze ao criar uma nova campanha.

Em seu novo modelo de webhook, preencha os seguintes campos:
- **URL do webhook**: o URL do webhook é exclusivo para cada cliente, e o gerente de sucesso do cliente da optilyz o fornecerá a você.
- **Corpo da solicitação**: Texto bruto

#### Cabeçalhos de solicitação e método

A optilyz também requer um cabeçalho HTTP para autorização e um método HTTP. Os dados a seguir já estarão incluídos no modelo como par de valor-chave, mas, na guia **Settings** (Configurações), substitua `<OPTILYZ_API_KEY>` pela sua chave de API da optilyz. Essa chave deve incluir um ":" logo após a chave e ser codificada em base 64. 

- **Método HTTP**: POST
- **Cabeçalhos de solicitação**:
  - **Autorização**: {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![Os cabeçalhos de solicitação e o método HTTP mostrados no construtor de webhooks do Braze.]({% image_buster /assets/img/optilyz/optilyz_settings.png %}){: style="max-width:50%"}

#### Corpo da solicitação

No corpo da solicitação a seguir, você pode usar qualquer tag de personalização Liquid e criar um modelo de solicitação personalizado de acordo com a [documentação da API](https://www.optilyz.com/doc/api/) da optilyz.

O campo `variation` é opcional e pode definir qual projeto dentro da automação deve ser usado. Se uma variação for omitida, a optilyz atribuirá uma das variações definidas de forma aleatória.

{% raw %}
```json
{
    "address": {
        "title": "{{custom_attribute.${salutation}}}",
        "firstName": "{{${first_name}}}",
        "lastName": "{{${last_name}}}",
        "street": "{{custom_attribute.${street}}}",
        "houseNumber": "{{custom_attribute.${houseNumber}}}",
        "address2": "{{custom_attribute.${address2}}}",
        "zipCode": "{{custom_attribute.${zipCode}}}",
        "city": "{{custom_attribute.${city}}}",
        "country": "{{custom_attribute.${country}}}"
    },
    "variation": {{custom_attribute.${designVariation}}}
}
```
{% endraw %}

![Uma imagem do código do corpo da solicitação e do URL do webhook mostrados na guia de composição do criador de webhooks do Braze.]({% image_buster /assets/img/optilyz/optilyz_compose.png %})

### Etapa 2: veja uma prévia da sua solicitação

Em seguida, faça uma prévia da solicitação no painel **Preview (Prévia** ) ou navegue até a guia **Test (Teste** ), onde é possível selecionar um usuário aleatório, um usuário existente ou personalizar o seu próprio usuário para testar o webhook. Lembre-se de salvar seu modelo antes de sair da página!

![Diferentes campos de teste disponíveis na guia teste do construtor de webhooks do Braze.]({% image_buster /assets/img/optilyz/optilyz_testing.png %})

{% alert important %}
Lembre-se de salvar seu modelo antes de sair da página! <br>Os modelos de webhook atualizados podem ser encontrados na lista **Modelos de webhook salvos** ao criar uma nova [campanha de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}


