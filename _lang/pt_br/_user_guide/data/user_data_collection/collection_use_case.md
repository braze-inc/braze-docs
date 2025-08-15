---
nav_title: Caso de uso da coleção
article_title: Caso de uso da coleção
page_order: 3
page_type: reference
description: "Este artigo de referência cobre um caso de uso de coleta de dados de usuários sobre como uma viagem por aplicativo pode decidir quais dados de usuários coletar."

---

# Caso de uso da coleção

> Este artigo aborda um caso de uso de coleta de dados de usuários sobre como uma viagem por aplicativo pode decidir quais dados de usuários coletar.

Vamos supor que um táxi ou aplicativo de viagem por aplicativo, chamado StyleRyde, queira decidir quais dados de usuários coletar. As seguintes perguntas e o processo de brainstorming são um ótimo modelo para suas equipes de marketing e desenvolvimento seguirem. Até o final deste exercício, ambas as equipes devem ter uma compreensão sólida sobre quais eventos e atributos personalizados fazem sentido coletar para ajudar a alcançar seu objetivo.

## Caso questão 1: Qual é o objetivo?

O objetivo do StyleRyde é simples, pois eles querem que os usuários chamem corridas de táxi através de seu app.

## Caso questão 2: Quais são os passos para alcançar esse objetivo após a instalação do app?

1. StyleRyde precisa que os usuários comecem o processo de registro e preencham suas informações pessoais.
2. StyleRyde precisa que os usuários completem e verifiquem o processo de registro inserindo um código no app que recebem por SMS.
3. StyleRyde precisa que os usuários tentem chamar um táxi.
4. StyleRyde precisa estar disponível quando os usuários chamam um táxi.

Essas ações poderiam então ser marcadas como os seguintes eventos personalizados:

- Início do registro
- Registro concluído
- Chamadas de táxi bem-sucedidas
- Chamadas de táxi malsucedidas

Após implementar os eventos, StyleRyde pode executar campanhas incluindo o seguinte:

1. Envio de mensagens aos usuários que iniciaram o registro, mas não o concluíram dentro de um determinado período de tempo.
2. Envie mensagens de parabéns aos usuários que concluíram o registro.
3. Envie desculpas e crédito promocional aos usuários que tiveram chamadas de táxi malsucedidas, que não foram seguidas por uma chamada de táxi bem-sucedida dentro de um determinado período de tempo.
4. Envie promoções aos usuários avançados com muitas chamadas de táxi bem-sucedidas para agradecê-los pela fidelidade.

## Caso questão 3: Que outras informações do usuário poderíamos coletar e usar para informar nosso envio de mensagens?

- Os usuários têm algum crédito promocional?
- A avaliação média que os usuários dão aos seus motoristas?
- Códigos promocionais exclusivos para usuários?

Essas características poderiam então ser marcadas como os seguintes atributos personalizados:

- Saldo de crédito promocional (tipo decimal)
- Classificação média do motorista (tipo inteiro)
- Código promocional exclusivo (tipo string)

Esses atributos permitem que você envie campanhas para usuários, como:

1. Lembrando os usuários que não usaram o app nos últimos sete dias e têm crédito promocional em sua conta para retornar ao app e usar o crédito.
2. Usar nossos modelos de mensagens e [recursos de personalização]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/#personalized-messaging) para arrastar o atributo de código promocional exclusivo para o envio de mensagens direcionadas aos usuários.

{% alert important %}
Braze irá banir ou bloquear usuários ("usuários fictícios") com mais de 5.000.000 sessões e não irá mais ingerir seus eventos SDK porque geralmente são o resultado de uma má integração. Se você descobrir que isso aconteceu com um usuário legítimo, entre em contato com o gerente da sua conta Braze.
{% endalert %}

