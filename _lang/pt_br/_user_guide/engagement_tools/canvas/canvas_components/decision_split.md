---
nav_title: Divisão de decisão 
article_title: Divisão de decisão 
alias: /decision_split/
page_order: 2
page_type: reference
description: "Este artigo de referência cobre como criar e usar divisões de decisão no seu canva."
tool: Canvas

---

# Divisão de decisão 

> O componente de divisão de decisão no canva permite que você ofereça experiências personalizadas e em tempo real para seus usuários.



Este componente pode ser usado para criar ramificações de canva com base em se um usuário corresponde a uma consulta.

## Criar uma divisão de decisão 

 

### Defina sua divisão

Como você quer dividir seus usuários?  Essencialmente, você está criando uma `true` ou `false` consulta que avaliará seus usuários e, em seguida, os direcionará para uma etapa ou outra. Você deve usar pelo menos um segmento ou um filtro. Você não precisa usar ambos, um segmento e um filtro.



{% alert note %}

{% endalert %} 

## Use sua divisão

Usar uma divisão de decisão pode ajudá-lo a distinguir caminhos para seus usuários com base em seu segmento ou seus atributos, até mesmo se eles usam certos canais de envio de mensagens para receber suas mensagens!

Digamos que você está criando um fluxo de integração. Você pode começar com um e-mail de boas-vindas ao se inscrever. Então, dois dias depois, você quer enviar uma push mensagem, mas apenas para usuários que estão push habilitados. Depois disso, todos os usuários recebem outro e-mail três dias após se inscreverem. Você também pode usar sua divisão de decisão para enviar uma mensagem no app para usuários que não têm push ativado para incentivá-los a ativar o push.

Se não houver uma etapa seguindo uma das jornadas, os usuários que seguirem essa jornada sairão do canva. 

  

## Análise de dados

Consulte a tabela a seguir para descrições de análise de dados para esta etapa:

| Métrica | Descrição |
|---|---|
|  | O total de vezes que a etapa foi inserida. Se o seu canva tiver re-eligibilidade e um usuário entrar em uma divisão de decisão etapa duas vezes, duas entradas serão registradas. |
|  | O número de entradas que atenderam aos critérios especificados e seguiram pelo "sim" jornada. |
|  | O número de entradas que não atenderam aos critérios especificados e seguiram pela "jornada" "não". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

