---
nav_title: Casos de uso
article_title: Casos de uso da transformação de dados Braze
page_order: 2
page_type: reference
description: "Este artigo de referência fornece alguns casos de uso da transformação de dados do Braze."
---

# Casos de uso de transformação de dados

> Considere os seguintes casos de uso possíveis para a transformação de dados da Braze e uma combinação de webhooks das plataformas externas de exemplo.

## Geração de leads

Você hospeda um formulário Typeform de geração de leads em seu site. Quando novos usuários preenchem esse formulário, você pode:
- Crie novos usuários no Braze.
- Adicione-os a uma de suas listas de e-mail do Braze.
- Sincronize algumas de suas respostas como atributos personalizados no Braze, pois suas respostas são dados primários valiosos que podem alimentar experiências de mensagens personalizadas para uso futuro.

## Abertura de tickets de serviço

Quando os clientes abrem tickets de atendimento ao cliente em uma plataforma como a Zendesk, você pode:
- Escreva um evento personalizado no Braze quando um ticket do Zendesk for criado.
- Escreva um evento personalizado com propriedades de evento no Braze quando uma classificação CSAT negativa for fornecida ao Zendesk.

## Integração com o Braze

O Braze tem uma integração com a [Iterate]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/surveys/iterate/), uma plataforma de insights e pesquisas com clientes. Com a Transformação de dados, é possível salvar várias respostas de pesquisa em um atributo personalizado aninhado, em vez da integração existente que salva vários atributos personalizados.

## Exemplo de código de transformação

Considere este exemplo de carga útil da Typeform, uma plataforma de pesquisa, que é enviada sempre que uma resposta de pesquisa é recebida.

![]({% image_buster /assets/img/data_transformation/data_transformation2.png %})

{% tabs local %}
{% tab Transformação básica %}

Este exemplo usa as respostas da pesquisa como atribuições e grava um evento para indicar que a pesquisa foi concluída:

```
return {
  "attributes": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_rating": payload.form_response.answers[1].number
    }
  ],
  "events": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
}
```

{% endtab %}
{% tab Transformação avançada %}

Vamos continuar com o exemplo de transformação básica e introduzir uma declaração `if` para categorizar o usuário em uma das respostas.

```
let nps_category;
let nps_number = payload.form_response.answers[1].number;
if (nps_number < 7) {
  nps_category = "Detractor";
} else if (nps_number == 7 || nps_number == 8) {
  nps_category = "Passive";
} else if (nps_number > 8) {
  nps_category = "Promoter";
}

return {
  "attributes": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_NPS_category": nps_category
    }
  ],
  "events": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
};
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/data_transformation/data_transformation2.png %}