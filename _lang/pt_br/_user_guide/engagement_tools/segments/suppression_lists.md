---
nav_title: Listas de supressão
article_title: Listas de supressão
page_order: 3
page_type: reference
tool: Segments
description: "Esta página aborda como usar listas de supressão para especificar quais usuários nunca devem receber suas mensagens."

---

# Listas de supressão

> As listas de supressão especificam grupos de usuários que nunca receberão mensagens. Os administradores podem criar listas de supressão dinâmicas com filtros de segmento para restringir um grupo de usuários da mesma forma que você faria para a segmentação.

{% alert important %}
As listas de supressão estão atualmente na versão beta. Se estiver interessado em fazer parte dessa versão beta, entre em contato com seu gerente de sucesso do cliente. Durante a versão beta, a funcionalidade pode mudar, e você pode ter até cinco listas de supressão ativas por vez, mas informe seu gerente de sucesso do cliente se precisar de mais.
{% endalert %}

## Por que usar listas de supressão?

As listas de supressão são dinâmicas e se aplicam automaticamente a determinadas formas de envio de mensagens, mas você pode definir exceções para tags selecionadas. Se as tags de exceção selecionadas forem usadas em uma campanha ou Canvas, essa lista de supressão não se aplicará a essa campanha ou Canvas. As mensagens de campanhas ou Canvas com tags de exceção ainda alcançarão todos os usuários da lista de supressão que fazem parte de seus segmentos de direcionamento.

### Envio de mensagens não afetadas por listas de supressão

Como parte da versão beta, as listas de supressão não se aplicarão aos seguintes tipos de mensagens (em outras palavras, os usuários da lista de supressão **ainda receberão** mensagens que pertencem aos seguintes tipos):
- [Feature Flags]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/)
- [E-mails de transação]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/)
- [Campanhas da API]({{site.baseurl}}/api/api_campaigns/)

Não é necessário adicionar uma tag de exceção para nenhum desses casos de uso, pois as listas de supressão automaticamente não se aplicarão a eles. Para excluir um grupo de usuários de uma mensagem dentro desses casos de uso, é necessário criar um segmento de direcionamento que exclua esses usuários.

{% alert important %}
Durante a versão beta, coletamos feedback dos clientes para ajudar a aprimorar nosso produto. Informe ao seu gerente de sucesso do cliente se planeja aplicar listas de supressão a e-mails de transação.
{% endalert %}

### Canais afetados por listas de supressão

As listas de supressão são dinâmicas e serão aplicadas automaticamente a todos os canais a seguir (a menos que a campanha ou o Canva contenha uma tag de exceção): 
- SMS
- E-mail
- Push
- Mensagem no app
- Cartão de conteúdo
- Banner
- SMS/MMS
- Webhook
- WhatsApp
- LINE

Por padrão, as listas de supressão serão aplicadas a qualquer campanha disparada por API e Canvas disparados por API. É possível alterar isso marcando **Não aplicar essa lista de supressão a todas as campanhas disparadas por API e Canvas disparadas por API** na seção **Configurações de exceção**.

![A seção "Configurações de exceção" com uma caixa de seleção para não aplicar a lista de supressão a campanhas e Canvas disparados pela API.]({% image_buster /assets/img/suppression_list_checkbox.png %}){: style="max-width:70%;"}

## Configuração de listas de supressão

Como as listas de supressão podem afetar significativamente o envio de mensagens, somente os administradores podem editar, salvar, ativar e desativar listas de supressão (todos os usuários podem visualizar as listas de supressão).

1. Acesse **Público** > **Listas de supressão**.<br><br>![A página "Suppression Lists" (Listas de supressão) com uma lista de três listas de supressão.]({% image_buster /assets/img/suppression_lists_home.png %})<br><br>
2. Selecione **Criar lista de supressão** e adicione um nome.<br><br>![Uma janela chamada "Create a Suppression List" (Criar uma lista de supressão) com um campo para inserir um nome.]({% image_buster /assets/img/create_suppression_list.png %}){: style="max-width:80%;"}<br><br>
3. Use filtros de segmento para identificar os usuários em suas listas de supressão. Você deve selecionar pelo menos um.

{% alert important %}
Embora o processo de configuração pareça semelhante ao da [criação de segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), uma lista de supressão é um grupo de usuários para os quais **não** se deseja enviar mensagens, independentemente da associação ao segmento.
{% endalert %}

![Um criador de listas de supressão com um filtro para usuários que abriram um e-mail pela última vez há mais de 90 dias.]({% image_buster /assets/img/suppression_list_filters.png %})

{: start="4"}
4\. Determine se deseja ter exceções com base na tag marcando a caixa abaixo do nome do segmento (consulte [Por que usar listas de supressão?](#why-use-suppression-lists) para obter mais informações) e, em seguida, adicione as tags de campanhas ou Canvas que os usuários dessa lista de supressão ainda devem receber. <br><br>Em outras palavras, se você adicionar a tag de exceção "Shipping confirmation" (Confirmação de envio), os usuários da sua lista de supressão serão excluídos de todos os envios de mensagens, exceto aqueles que usam a tag "Shipping confirmation" (Confirmação de envio).<br><br>![A seção "Shipping List Details" (Detalhes da lista de remessa) com uma tag de exceção aplicada chamada "Shipping confirmation" (Confirmação de remessa).]({% image_buster /assets/img/exception_tags.png %})<br><br>
5\. Salve ou ative sua lista de supressão.
- Quando você salvar, sua lista de supressão será salva, mas não será ativada, o que significa que não entrará em vigor. Sua lista de supressão permanecerá inativa até que você a ative, e as listas de supressão inativas não afetarão o envio de mensagens (os usuários não serão excluídos das mensagens).
- Ao ser ativada, sua lista de supressão será salva e entrará em vigor imediatamente, o que significa que os usuários em sua lista de supressão serão imediatamente excluídos de campanhas ou Canvas (exceto os que contêm uma tag de exceção).

{% alert note %}
Somente os administradores podem salvar ou ativar listas de supressão. Você pode ter até cinco listas de supressão ativas por vez na versão beta.
{% endalert %}

Você pode desativar ou arquivar listas de supressão quando não precisar mais delas. 
- Para desativar, selecione uma lista de supressão ativa e selecione **Desativar**. As listas de supressão desativadas podem ser reativadas posteriormente.
- Para arquivar, faça isso na página **Listas de supressão**.

## Uso da lista de supressão

Para verificar se a lista de supressão impediu que um usuário recebesse uma mensagem, use **a Pesquisa de usuários** na etapa do **público-alvo** em sua campanha ou no Canva. Aqui, você poderá ver de qual lista de supressão eles fazem parte.

![Janela "User Lookup" mostrando que um usuário está em uma lista de supressão.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

{% alert tip %}
Você também pode encontrar listas de supressão aplicadas na etapa **Resumo**.
{% endalert %}

Ao criar uma campanha ou um Canva, use a **pesquisa de usuário** na etapa do **público-alvo** para procurar um usuário e, se ele não estiver no público-alvo, você poderá ver a lista de supressão da qual ele faz parte. 

![Janela "User Lookup" mostrando que um usuário está em uma lista de supressão.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

{% tabs local %}
{% tab campanha %}
Se um usuário estiver em uma lista de supressão, ele não receberá uma campanha à qual essa lista de supressão se aplica. Consulte [Mensagens não afetadas por listas de supressão](#messages-not-affected-by-suppression-lists) para saber os casos em que uma lista de supressão não se aplica.

![A seção "Listas de supressão" com uma lista de supressão ativa, chamada "Pontuações baixas de integridade de marketing".]({% image_buster /assets/img/active_suppression_list.png %})
{% endtab %}
{% tab canvas %}
Se um usuário estiver em uma lista de supressão, ele ainda entrará no Canvas, mas não poderá receber etapas de mensagens dentro do Canva. Quando avançarem para uma etapa de Mensagens, eles sairão do Canva. No entanto, um usuário em uma lista de supressão ainda pode receber etapas que não sejam de envio de mensagens antes de uma etapa de mensagem. 

#### Impedindo que segmentos entrem em um Canva

Para que um segmento não seja inserido em **nenhum** canva, você pode configurar as definições de destino do canva para excluir esse segmento seguindo estas etapas:

1. Crie um segmento usando os mesmos filtros e critérios de sua lista de supressão.
2. Na etapa **Alvo**, use o filtro **Inscrição em segmento** para direcionar os usuários que não estão incluídos em seu segmento.

Por exemplo, digamos que você tenha um Canva com uma lista de supressão aplicada. O Canva tem uma etapa de atualização do usuário seguida de uma etapa de mensagem. Nesse cenário, os usuários da lista de supressão entrarão no Canvas, passarão pela etapa de Atualização do usuário (onde o usuário pode ser atualizado, com base em como essa etapa está configurada) e, em seguida, sairão na etapa de Mensagens (momento em que o usuário será incluído na métrica "Saído").
{% endtab %}
{% endtabs %}

