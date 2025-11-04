---
nav_title: Typeform
article_title: Typeform
description: "Este artigo descreve a parceria entre a Braze e a Typeform, uma ferramenta fácil de usar para coletar dados, feedback e muito mais."
alias: /partners/typeform/
page_type: partner
search_tag: Partner
---

# Typeform

> [O Typeform](https://www.typeform.com/) é uma ferramenta fácil de usar para coletar dados, feedback e muito mais.

Ao integrar a Braze e a Typeform, você pode:

- Atualizar os perfis de usuários no Braze com os dados coletados da resposta do Typeform
- Disparar o envio de mensagens na Braze com base no engajamento de um usuário com um typeform
- Personalize o envio de mensagens do Braze com base nas respostas do usuário no Typeform

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Typeform | É necessário ter uma conta Typeform com acesso a webhooks para aproveitar essa parceria. |
| Transformação de dados do Braze | É necessário um [URL de transformação de dados]({{site.baseurl}}/data_transformation/) para receber dados do Typeform. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: configure a transformação de dados da Braze para aceitar os webhooks do Typeform {#step-1}

{% multi_lang_include create_transformation.md location="typeform" %}

### Etapa 2: Configurar webhooks do Typeform

Siga as etapas na [documentação de webhooks do Typeform](https://www.typeform.com/help/a/webhooks-360029573471/) para configurar um webhook.

Na etapa 4, adicione seu URL do webhook de transformação de dados como o **URL de destino**.

![]({% image_buster /assets/img/typeform/typeform_add_webhook.png %}){: style="max-width:50%" }

Envie um evento de teste para sua transformação de dados clicando em **Exibir entregas** e, em seguida, em **Enviar solicitação de teste**.

![]({% image_buster /assets/img/typeform/typeform_test_request.png %})

### Etapa 3: Escreva o código de transformação para aceitar seus eventos Typeform escolhidos

Nesta etapa, você transformará a carga útil do webhook que será enviada do Typeform em um valor de retorno de objeto JavaScript.

1. Atualize sua transformação de dados e verifique se você pode ver a carga útil do teste Typeform nos **detalhes do webhook**.
2. Atualize seu código de transformação de dados para dar suporte aos eventos do Typeform escolhidos.
3. Clique em **Validate (Validar)** para retornar uma prévia da saída de seu código e verificar se é uma solicitação `/users/track` aceitável.
4. Salve e ative sua transformação de dados.

![]({% image_buster /assets/img/typeform/typeform_test_result.png %})

#### Formato do corpo da solicitação

Este valor de retorno deve aderir ao formato do corpo da solicitação da Braze `/users/track`:

- O código de transformação é aceito na linguagem de programação JavaScript. Todo fluxo de controle JavaScript padrão, como a lógica if/else, é suportado.
- O código de transformação acessa o corpo da solicitação do webhook através da variável carga útil. Esta variável é um objeto populado pela análise do corpo da solicitação JSON.
- Qualquer recurso aceito em nosso `/users/track` endpoint é aceito, incluindo:
    - Objetos de atributos de usuário, objetos de eventos e objetos de compra
    - Atributos aninhados e propriedades de evento personalizado aninhadas
    - Atualizações do grupo de inscrições
    - Endereço de e-mail como identificador

## Exemplo de carga útil do webhook do Typeform

```json
Content-Type: application/json

{
  "event_id": "01HC3PTZN05GJWT0QDXXB2QV8F",
  "event_type": "form_response",
  "form_response": {
    "form_id": "uaIA4a7Y",
    "token": "7pctqdoqxg41to97pctqdibhqn6hqvto",
    "landed_at": "2023-10-06T23:57:52Z",
    "submitted_at": "2023-10-06T23:58:18Z",
    "hidden": { 
		"user_id": "hidden_value" 
    },
    "definition": {
      "id": "uaIA4a7Y",
      "title": "Project Feedback Survey",
      "fields": [
        {
          "id": "G0IbXtfvsfjV",
          "ref": "814b9fc2-e6d2-4672-accf-22f754b84f20",
          "type": "email",
          "title": "Please provide your email",
          "properties": {}
        },
        {
          "id": "lg82q3t0rK03",
          "ref": "e1503b62-0241-4269-9902-5c539abf305e",
          "type": "short_text",
          "title": "What was your role in the project?",
          "properties": {}
        },
        {
          "id": "UXftY0tSmuDV",
          "ref": "5b839dbb-566b-47de-a47e-b0914d9ccf7c",
          "type": "opinion_scale",
          "title": "How would you rate the overall performance of the team?",
          "properties": {}
        },
        {
          "id": "fE17bXVUEB4E",
          "ref": "fd6be99d-1ed1-4a4d-b811-f6ecdd8fa9b6",
          "type": "yes_no",
          "title": "Did the project meet its intended outcomes?",
          "properties": {}
        },
        {
          "id": "NmVOQFuI0vv9",
          "ref": "cd2b4176-db9a-49bb-a918-4463720bbc79",
          "type": "multiple_choice",
          "title": "Which area of the project do you think went well?",
          "properties": {},
          "choices": [
            {
              "id": "RvV3LaMEQ2eK",
              "ref": "2d5e0913-afe9-491c-b31c-0648dd397d56",
              "label": "Communication"
            },
            {
              "id": "7iXmfpPMeQvz",
              "ref": "7a7749d2-5cd6-4bf7-9726-65c7ab11ec83",
              "label": "Planning"
            },
            {
              "id": "1No85DZlvP6f",
              "ref": "d7b7304a-776b-4630-8bee-7dc7ef9c9404",
              "label": "Execution"
            },
            {
              "id": "ruMnsZWjyalW",
              "ref": "41dc926a-85af-4625-8a61-725fda35afda",
              "label": "Problem Solving"
            },
            {
              "id": "CexnFN3roprG",
              "ref": "cfdd2da4-8c57-4ff1-b4c0-1a5262e2ff84",
              "label": "Other"
            }
          ]
        },
        {
          "id": "ZJop9pvoObzk",
          "ref": "ce903cda-7e27-4b4c-9fa8-0623c47c61b4",
          "type": "multiple_choice",
          "title": "Which area of the project do you think could be improved?",
          "properties": {},
          "choices": [
            {
              "id": "YQLArFf0Wks5",
              "ref": "09fa30c7-7bdc-4753-971e-0d922638d023",
              "label": "Communication"
            },
            {
              "id": "iGjaELgfnChw",
              "ref": "61820c89-3426-464d-b031-c06de5125fd5",
              "label": "Planning"
            },
            {
              "id": "2EyI5tozFxro",
              "ref": "c35f71b2-2a6d-4488-a1ba-87c2e711ce19",
              "label": "Execution"
            },
            {
              "id": "VGtsIHBLAhME",
              "ref": "6c171a9a-9324-4f7d-adb9-290bd701efe9",
              "label": "Problem Solving"
            },
            {
              "id": "lVdV7MIL1anS",
              "ref": "faba551f-4e6b-4377-9f74-11ca4fcc8ed5",
              "label": "Other"
            }
          ]
        },
        {
          "id": "hcCNsLUHGXgv",
          "ref": "d1ae8537-0d5a-4ca8-bb6b-f8057f04d7e2",
          "type": "opinion_scale",
          "title": "How satisfied were you with the level of communication during the project?",
          "properties": {}
        },
        {
          "id": "dBqPlgeKejN2",
          "ref": "e2c884c1-0d92-4f18-9833-79dff0b3eef2",
          "type": "nps",
          "title": "How likely are you to recommend Braze for customer engagement services?",
          "properties": {}
        },
        {
          "id": "vLdpFmCmulF5",
          "ref": "a86e48ec-6d10-49fc-ac03-4ac1aad4bfec",
          "type": "dropdown",
          "title": "In which country was the project executed?",
          "properties": {}
        }
      ],
      "endings": [
        {
          "id": "LUpVm67y72vb",
          "ref": "30c03bdf-80b3-45f5-8307-df8ca49046b1",
          "title": "Thank you for taking the time to complete our survey!",
          "type": "thankyou_screen",
          "properties": {
            "button_text": "Create a typeform",
            "show_button": true,
            "share_icons": true,
            "button_mode": "default_redirect"
          }
        }
      ]
    },
    "answers": [
      {
        "type": "email",
        "email": "typeformintegration@example.com",
        "field": {
          "id": "G0IbXtfvsfjV",
          "type": "email",
          "ref": "814b9fc2-e6d2-4672-accf-22f754b84f20"
        }
      },
      {
        "type": "text",
        "text": "Project",
        "field": {
          "id": "lg82q3t0rK03",
          "type": "short_text",
          "ref": "e1503b62-0241-4269-9902-5c539abf305e"
        }
      },
      {
        "type": "number",
        "number": 9,
        "field": {
          "id": "UXftY0tSmuDV",
          "type": "opinion_scale",
          "ref": "5b839dbb-566b-47de-a47e-b0914d9ccf7c"
        }
      },
      {
        "type": "boolean",
        "boolean": true,
        "field": {
          "id": "fE17bXVUEB4E",
          "type": "yes_no",
          "ref": "fd6be99d-1ed1-4a4d-b811-f6ecdd8fa9b6"
        }
      },
      {
        "type": "choice",
        "choice": {
          "id": "ruMnsZWjyalW",
          "label": "Problem Solving",
          "ref": "41dc926a-85af-4625-8a61-725fda35afda"
        },
        "field": {
          "id": "NmVOQFuI0vv9",
          "type": "multiple_choice",
          "ref": "cd2b4176-db9a-49bb-a918-4463720bbc79"
        }
      },
      {
        "type": "choice",
        "choice": {
          "id": "lVdV7MIL1anS",
          "label": "Other",
          "ref": "faba551f-4e6b-4377-9f74-11ca4fcc8ed5"
        },
        "field": {
          "id": "ZJop9pvoObzk",
          "type": "multiple_choice",
          "ref": "ce903cda-7e27-4b4c-9fa8-0623c47c61b4"
        }
      },
      {
        "type": "number",
        "number": 8,
        "field": {
          "id": "hcCNsLUHGXgv",
          "type": "opinion_scale",
          "ref": "d1ae8537-0d5a-4ca8-bb6b-f8057f04d7e2"
        }
      },
      {
        "type": "number",
        "number": 6,
        "field": {
          "id": "dBqPlgeKejN2",
          "type": "nps",
          "ref": "e2c884c1-0d92-4f18-9833-79dff0b3eef2"
        }
      },
      {
        "type": "choice",
        "choice": {
          "id": "KESjdqLseWmC",
          "label": "Brazil",
          "ref": "250210d9-33f6-4734-8ec6-06005a8ef66d"
        },
        "field": {
          "id": "vLdpFmCmulF5",
          "type": "dropdown",
          "ref": "a86e48ec-6d10-49fc-ac03-4ac1aad4bfec"
        }
      }
    ],
    "ending": {
      "id": "LUpVm67y72vb",
      "ref": "30c03bdf-80b3-45f5-8307-df8ca49046b1"
    }
  }
}
```

## Casos de uso de transformação de dados

Veja a seguir os modelos de exemplo criados usando nossa [carga útil de webhook do Typeform](#example-typeform-webhook-payload). Esses modelos podem ser usados como ponto de partida. Você pode começar do zero ou excluir componentes específicos conforme achar necessário.

Nesses modelos de exemplo, estamos registrando um evento personalizado no perfil da Braze. O título do Typeform será passado como o nome do evento personalizado, e os resultados do Typeform serão passados como propriedades do evento. Esses modelos de exemplo não levam em conta os tipos de pergunta Calendly, File Upload ou Payment no Typeform.

### Caso de uso: Envio de e-mail como identificador

Neste modelo de exemplo, estamos usando um endereço de e-mail (capturado de uma pergunta de endereço de e-mail dentro do formulário) como identificador.

{% alert note %}
Se você pretende usar um endereço de e-mail como identificador, consulte nossas [perguntas frequentes]({{site.baseurl}}/api/endpoints/user_data/post_user_track#frequently-asked-questions) sobre o endpoint `/users/track` para obter mais informações sobre o comportamento esperado.
{% endalert %}

{% tabs local %}
{% tab Entrada %}

```javascript
/* In the Typeform webhook payload each question is stored as a “title” within each object of the “fields” array. Our code defines a “title” variable where we store the value of each field title. */
const titles = payload.form_response.definition.fields.map(field => field.title);

/* The answers array is saved to a “tfAnswers” variable so this can be iterated through */
const tfAnswers = payload.form_response.answers;

/* The value of a response will change based on the type of question, to account for this we have created a function that iterates through the answers, determines what the answer type is and then, based on the type, adds the associated response to an extractedValues array. */
const extractValues = (tfAnswers) => {
	const extractedValues = [];

	tfAnswers.forEach((tfAnswer) => {
		let result = null;

		if (tfAnswer.type === 'choices') {
			if (tfAnswer.choices) {
				// Multiple choices
				let labels = tfAnswer.choices.labels || [];
				if (tfAnswer.choices.other) {
					labels.push(tfAnswer.choices.other);
				}
				result = labels;
			}
		} else if (tfAnswer.type === 'choice' && Object.keys(tfAnswer.choice).length > 1) {
			// Single choice
			result = tfAnswer.choice && tfAnswer.choice.other ?
				tfAnswer.choice.other.toString() :
				tfAnswer.choice.label.toString();
		} else if (tfAnswer.type === 'dropdown') {
			// Dropdown
			result = tfAnswer.text;
		} else {
			// For other types, use the type-specific value
			result = tfAnswer[tfAnswer.type];
		}

		extractedValues.push(result);
	});

	return extractedValues;
};

/* We use the above defined function, passing it the “tfAnswers” variable that holds the answers portion of the Typeform webhook payload and save the output to a ”values” variable */
const values = extractValues(tfAnswers);

/* Finally, the values within the previously assigned “titles” variable and “values” variable are paired together in an object as the values to a “question” key and “answer” key in a “responses” array of objects variable. */
const results = titles.map((title, index) => {
	return {
		question: title,
		answer: values[index],
	};
});

/* The code defines a variable, "brazecall", to build a /users/track request. Within the request, the typeform title is populated as the event name, and our “results” variable (where all of our question/answer pairs are stored), is assigned as the event’s properties. */
let brazecall = {
	"events": [{
		"email": payload.form_response.answers.find(answer => answer.type === 'email').email,
		"name": payload.form_response.definition.title,
		"time": new Date().toISOString(),
		"properties": {
			"responses": results
		}
	}]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return “brazecall” to create an output
return brazecall;
```

{% endtab %}
{% tab Saída %}

```json
{
  "events": [
    {
      "email": "an_account@example.com",
      "name": "Project Feedback Survey",
      "time": "2023-10-17T18:21:39.527Z",
      "properties": {
        "responses": [
          {
            "question": "Please provide your email",
            "answer": "an_account@example.com"
          },
          {
            "question": "What was your role in the project?",
            "answer": "Lorem ipsum dolor"
          },
          {
            "question": "How would you rate the overall performance of the team?",
            "answer": 5
          },
          {
            "question": "Did the project meet its intended outcomes?",
            "answer": true
          },
          {
            "question": "If you answered \"No\" to the previous question, please explain why. If you answered \"Yes\", skip this question.",
            "answer": "Lorem ipsum dolor"
          },
          {
            "question": "Which area of the project do you think went well?",
            "answer": "Communication"
          },
          {
            "question": "Which area of the project do you think could be improved?",
            "answer": "Communication"
          },
          {
            "question": "How satisfied were you with the level of communication during the project?",
            "answer": 5
          },
          {
            "question": "How likely are you to recommend Braze for customer engagement services?",
            "answer": 5
          },
          {
            "question": "In which country was the project executed?",
            "answer": "United States"
          }
        ]
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### Caso de uso: Uso do identificador passado em campos ocultos

Você pode usar o Typeform Hidden Fields para passar dados na carga útil do webhook do Typeform, como o ID de um usuário, sem precisar passar essas informações na resposta do Typeform.

Neste modelo de exemplo, usamos um campo oculto "user_id" e o passamos para a carga útil da solicitação `/users/track` como `external_id`. Embora estejamos usando "user_id", os campos podem ser modificados para atender às suas necessidades.

{% tabs local %}
{% tab Entrada %}

```javascript
/* In the Typeform webhook payload each question is stored as a “title” within each object of the “fields” array. Our code defines a “title” variable where we store the value of each field title. */
const titles = payload.form_response.definition.fields.map(field => field.title);

/* The answers array is saved to a “tfAnswers” variable so this can be iterated through */
const tfAnswers = payload.form_response.answers;

/* The value of a response will change based on the type of question, to account for this we have created a function that iterates through the answers, determines what the answer type is and then, based on the type, adds the associated response to an extractedValues array. */
const extractValues = (tfAnswers) => {
	const extractedValues = [];

	tfAnswers.forEach((tfAnswer) => {
		let result = null;

		if (tfAnswer.type === 'choices') {
			if (tfAnswer.choices) {
				// Multiple choices
				let labels = tfAnswer.choices.labels || [];
				if (tfAnswer.choices.other) {
					labels.push(tfAnswer.choices.other);
				}
				result = labels;
			}
		} else if (tfAnswer.type === 'choice' && Object.keys(tfAnswer.choice).length > 1) {
			// Single choice
			result = tfAnswer.choice && tfAnswer.choice.other ?
				tfAnswer.choice.other.toString() :
				tfAnswer.choice.label.toString();
		} else if (tfAnswer.type === 'dropdown') {
			// Dropdown
			result = tfAnswer.text;
		} else {
			// For other types, use the type-specific value
			result = tfAnswer[tfAnswer.type];
		}

		extractedValues.push(result);
	});

	return extractedValues;
};

/* We use the above defined function, passing it the “tfAnswers” variable that holds the answers portion of the Typeform webhook payload and save the output to a ”values” variable */
const values = extractValues(tfAnswers);

/* Finally, the values within the previously assigned “titles” variable and “values” variable are paired together in an object as the values to a “question” key and “answer” key in a “responses” array of objects variable. */
const results = titles.map((title, index) => {
	return {
		question: title,
		answer: values[index],
	};
});

/* The code defines a variable, "brazecall", to build a /users/track request. Within the request, the typeform title is populated as the event name, and our “results” variable (where all of our question/answer pairs are stored), is assigned as the event’s properties. */
let brazecall = {
	"events": [{
		"external_id": payload.form_response.hidden.user_id,
		"name": payload.form_response.definition.title,
		"time": new Date().toISOString(),
		"properties": {
			"responses": results
		}
	}]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return “brazecall” to create an output
return brazecall;
```

{% endtab %}
{% tab Saída %}

```json
{
  "events": [
    {
      "external_id": "hidden_value",
      "name": "Project Feedback Survey",
      "time": "2023-10-17T18:27:22.209Z",
      "properties": {
        "responses": [
          {
            "question": "Please provide your email",
            "answer": "an_account@example.com"
          },
          {
            "question": "What was your role in the project?",
            "answer": "Lorem ipsum dolor"
          },
          {
            "question": "How would you rate the overall performance of the team?",
            "answer": 5
          },
          {
            "question": "Did the project meet its intended outcomes?",
            "answer": true
          },
          {
            "question": "If you answered \"No\" to the previous question, please explain why. If you answered \"Yes\", skip this question.",
            "answer": "Lorem ipsum dolor"
          },
          {
            "question": "Which area of the project do you think went well?",
            "answer": "Communication"
          },
          {
            "question": "Which area of the project do you think could be improved?",
            "answer": "Communication"
          },
          {
            "question": "How satisfied were you with the level of communication during the project?",
            "answer": 5
          },
          {
            "question": "How likely are you to recommend Braze for customer engagement services?",
            "answer": 5
          },
          {
            "question": "In which country was the project executed?",
            "answer": "United States"
          }
        ]
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### Etapa 4: Publique seu webhook do Typeform

Depois de escrever a transformação de dados, clique em **Validate (Validar)** para verificar se o código da transformação de dados está formatado corretamente e se funcionará conforme o esperado. Em seguida, salve e ative sua transformação de dados.

Uma vez ativados, os dados de eventos personalizados serão registrados no perfil do usuário quando ele preencher o formulário.

![]({% image_buster /assets/img/typeform/typeform_custom_event.png %})

## Monitoramento e solução de problemas

Consulte a seção [Monitoramento da transformação]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#step-5-monitor-your-transformation) para obter mais informações sobre monitoramento e solução de problemas da transformação.