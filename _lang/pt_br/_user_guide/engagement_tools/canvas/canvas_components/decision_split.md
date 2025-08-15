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

![Uma etapa de divisão de decisão chamada "Push enabled?" para usuários que não estão habilitados para push e usuários que estão habilitados para push.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

Este componente pode ser usado para criar ramificações de canva com base em se um usuário corresponde a uma consulta.

## Criar uma divisão de decisão 

Para criar uma divisão de decisão em seu fluxo de trabalho, adicione uma etapa do canva. Em seguida, arraste e solte o componente da barra lateral ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Divisão de decisão**.

### Defina sua divisão

Como você quer dividir seus usuários? Você pode usar [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/) e filtros para desenhar a linha. Essencialmente, você está criando uma `true` ou `false` consulta que avaliará seus usuários e, em seguida, os direcionará para uma etapa ou outra. Você deve usar pelo menos um segmento ou um filtro. Você não precisa usar ambos, um segmento e um filtro.

![Uma etapa de divisão de decisão com o filtro "Capacitação ativada é verdadeira" selecionado.]({% image_buster /assets/img/define-split-2.png %}){: style="max-width:90%;"}

{% alert note %}
Por padrão, os segmentos e filtros de uma etapa de divisão de decisão são verificados logo após o recebimento de uma etapa anterior, a menos que você adicione uma postergação.
{% endalert %} 

## Use sua divisão

Usar uma divisão de decisão pode ajudá-lo a distinguir caminhos para seus usuários com base em seu segmento ou seus atributos, até mesmo se eles usam certos canais de envio de mensagens para receber suas mensagens!

Digamos que você está criando um fluxo de integração. Você pode começar com um e-mail de boas-vindas ao se inscrever. Então, dois dias depois, você quer enviar uma push mensagem, mas apenas para usuários que estão push habilitados. Depois disso, todos os usuários recebem outro e-mail três dias após se inscreverem. Você também pode usar sua divisão de decisão para enviar uma mensagem no app para usuários que não têm push ativado para incentivá-los a ativar o push.

Se não houver uma etapa seguindo uma das jornadas, os usuários que seguirem essa jornada sairão do canva. 

![Uma etapa de divisão de decisão chamada "Push enabled?" para usuários que não estão habilitados para capacitação e para aqueles que estão. Os usuários que não estiverem ativados para push terão uma postergação de três dias e receberão uma mensagem de e-mail. Os usuários que estiverem habilitados para push terão um atraso de 1 dia, receberão uma notificação por push seguida de uma postergação de 2 dias e, em seguida, receberão o mesmo envio de e-mail que os usuários que não estiverem habilitados para push.]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## Análise de dados

Consulte a tabela a seguir para descrições de análise de dados para esta etapa:

| Métrica | Descrição |
|---|---|
| _Entraram_ | O total de vezes que a etapa foi inserida. Se o seu canva tiver re-eligibilidade e um usuário entrar em uma divisão de decisão etapa duas vezes, duas entradas serão registradas. |
| _Sim_ | O número de entradas que atenderam aos critérios especificados e seguiram pelo "sim" jornada. |
| _Não_ | O número de entradas que não atenderam aos critérios especificados e seguiram pela "jornada" "não". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

