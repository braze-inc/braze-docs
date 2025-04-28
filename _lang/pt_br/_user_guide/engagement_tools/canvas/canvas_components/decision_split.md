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

![][1]{: style="float:right;max-width:20%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

## Criar uma divisão de decisão 

Para criar uma divisão de decisão no seu fluxo de trabalho, primeiro adicione uma etapa ao seu canva. Arraste e solte o componente da barra lateral ou clique no <i class="fas fa-plus-circle"></i> botão de mais na parte inferior de uma etapa e selecione **divisão de decisão**.

### Defina sua divisão

Como você quer dividir seus usuários? Você pode usar [segmentos][5] e filtros para traçar a LINE. Essencialmente, você está criando uma `true` ou `false` consulta que avaliará seus usuários e, em seguida, os direcionará para uma etapa ou outra. Você deve usar pelo menos um segmento ou um filtro. Você não precisa usar ambos, um segmento e um filtro.

![][2]{: style="max-width:90%;"}

{% alert note %}
Por padrão, segmentos e filtros para um componente de divisão de decisão são verificados logo após receber uma etapa anterior, a menos que você adicione uma postergação.
{% endalert %} 

## Use sua divisão

Usar uma divisão de decisão pode ajudá-lo a distinguir caminhos para seus usuários com base em seu segmento ou seus atributos, até mesmo se eles usam certos canais de envio de mensagens para receber suas mensagens!

Digamos que você está criando um fluxo de integração. Você pode começar com um e-mail de boas-vindas ao se inscrever. Então, dois dias depois, você quer enviar uma push mensagem, mas apenas para usuários que estão push habilitados. Depois disso, todos os usuários recebem outro e-mail três dias após se inscreverem. Você também pode usar sua divisão de decisão para enviar uma mensagem no app para usuários que não têm push ativado para incentivá-los a ativar o push.

![][3]{: style="max-width:60%;"}

Se não houver uma etapa seguindo uma das jornadas, os usuários que seguirem essa jornada sairão do canva. 

{% alert important %}
Uma divisão de decisão não pode ter etapas irmãs completas. Em outras palavras, você não pode criar uma etapa completa que se ramifique em uma etapa de filtro e uma etapa completa. Essa restrição existe porque, se houvesse um ramo com uma etapa de filtro e uma etapa completa, não seria claro qual ramo os usuários seguiriam.
<br>
Uma etapa de filtro só pode se conectar a uma próxima etapa.
{% endalert %}

## Análise de dados

Consulte a tabela a seguir para descrições de análise de dados para esta etapa:

| Métrica | Descrição |
|---|---|
| Entraram | O total de vezes que a etapa foi inserida. Se o seu canva tiver re-eligibilidade e um usuário entrar em uma divisão de decisão etapa duas vezes, duas entradas serão registradas. |
| Sim | O número de entradas que atenderam aos critérios especificados e seguiram pelo "sim" jornada. |
| Não | O número de entradas que não atenderam aos critérios especificados e seguiram pela "jornada" "não". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[1]: {% image_buster /assets/img/decision-split-1.png %}
[2]: {% image_buster /assets/img/define-split-2.png %}
[3]: {% image_buster /assets/img/use-split-onboarding-3.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/
