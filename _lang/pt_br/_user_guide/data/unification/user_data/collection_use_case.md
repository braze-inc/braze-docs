---
nav_title: Caso de uso da coleção
article_title: Caso de uso da coleção
page_order: 3
page_type: reference
description: "Este artigo de referência aborda um caso de uso de coleta de dados do usuário sobre como um aplicativo de compartilhamento de carona pode decidir quais dados do usuário coletar."

---

# Caso de uso da coleção

> Este artigo aborda um caso de uso de coleta de dados do usuário sobre como um aplicativo de compartilhamento de carona pode decidir quais dados do usuário coletar.

Digamos que um aplicativo de táxi ou de compartilhamento de carona, chamado StyleRyde, queira decidir quais dados de usuário coletar. As perguntas e o processo de brainstorming a seguir são um ótimo modelo a ser seguido pelas equipes de marketing e desenvolvimento. Ao final desse exercício, ambas as equipes devem ter uma sólida compreensão de quais eventos e atributos personalizados fazem sentido coletar para ajudar a atingir a meta.

## Pergunta de caso 1: Qual é o objetivo?

O objetivo da StyleRyde é simples: eles querem que os usuários chamem táxis por meio de seu aplicativo.

## Pergunta de caso 2: Quais são as etapas para atingir essa meta após a instalação do aplicativo?

1. A StyleRyde precisa que os usuários iniciem o processo de registro e preencham suas informações pessoais.
2. A StyleRyde precisa que os usuários concluam e verifiquem o processo de registro inserindo um código no aplicativo que recebem por SMS.
3. O StyleRyde precisa que os usuários tentem chamar um táxi.
4. O StyleRyde precisa estar disponível quando os usuários chamam um táxi.

Essas ações poderiam então ser marcadas como os seguintes eventos personalizados:

- Início do registro
- Registro concluído
- Chamadas de táxi bem-sucedidas
- Chamadas de táxi malsucedidas

Depois de implementar os eventos, o StyleRyde pode executar campanhas que incluem o seguinte:

1. Envie mensagens aos usuários que iniciaram o registro, mas não o concluíram dentro de um determinado período de tempo.
2. Envie mensagens de parabéns aos usuários que concluíram o registro.
3. Envie desculpas e crédito promocional aos usuários que tiveram chamadas de táxi malsucedidas, que não foram seguidas por uma chamada de táxi bem-sucedida dentro de um determinado período de tempo.
4. Envie promoções aos usuários avançados com muitas chamadas de táxi bem-sucedidas para agradecê-los por sua fidelidade.

## Pergunta de caso 3: Que outras informações do usuário poderíamos coletar e usar para informar nossas mensagens?

- Se os usuários têm algum crédito promocional?
- A classificação média que os usuários dão aos seus motoristas?
- Códigos promocionais exclusivos para usuários?

Essas características poderiam então ser marcadas como os seguintes atributos personalizados:

- Saldo de crédito promocional (tipo decimal)
- Classificação média do motorista (tipo inteiro)
- Código promocional exclusivo (tipo de cadeia de caracteres)

Esses atributos permitem o envio de campanhas para usuários como:

1. Lembrar aos usuários que não usaram o aplicativo em sete dias e que têm crédito promocional em suas contas que devem retornar ao aplicativo e usar o crédito.
2. Usar nossos modelos de mensagem e [recursos de personalização]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/#personalized-messaging) para arrastar o atributo de código promocional exclusivo para as mensagens direcionadas aos usuários.

{% alert important %}
O Braze banirá ou bloqueará usuários ("usuários fictícios") com mais de 5.000.000 de sessões e não mais ingerirá seus eventos de SDK porque eles geralmente são o resultado de uma integração incorreta. Se você perceber que isso aconteceu com um usuário legítimo, entre em contato com o gerente da sua conta Braze.
{% endalert %}

