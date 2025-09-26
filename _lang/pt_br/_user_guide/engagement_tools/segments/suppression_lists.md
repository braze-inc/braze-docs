---
nav_title: Listas de supressão
article_title: Listas de supressão
page_order: 2.5
page_type: reference
tool: Segments
description: "Esta página cobre como usar listas de supressão para especificar quais usuários nunca devem receber suas mensagens."

---

# Listas de supressão

> As listas de supressão especificam grupos de usuários que nunca receberão mensagens. Os administradores podem criar listas de supressão dinâmicas com filtros de segmento para restringir um grupo de usuários da mesma forma que você faria para a segmentação.

{% alert important %}
Listas de supressão estão atualmente em beta. Se estiver interessado em fazer parte dessa versão beta, entre em contato com seu gerente de sucesso do cliente. Durante a beta, a funcionalidade pode mudar, e você pode ter até cinco listas de supressão ativas ao mesmo tempo, mas avise seu gerente de sucesso do cliente se precisar de mais.
{% endalert %}

## Como funciona?

As listas de supressão são dinâmicas e se aplicam automaticamente a determinadas formas de envio de mensagens, mas você pode definir exceções para tags selecionadas. Se as tags de exceção selecionadas forem usadas em uma campanha ou Canvas, essa lista de supressão não se aplicará a essa campanha ou Canvas. As mensagens de campanhas ou Canvas com tags de exceção ainda alcançarão todos os usuários da lista de supressão que fazem parte de seus segmentos de direcionamento.

### Envio de mensagens não afetadas por listas de supressão

Como parte da beta, listas de supressão não se aplicarão aos seguintes tipos de mensagens (em outras palavras, usuários da lista de supressão **ainda** receberão mensagens que pertencem ao seguinte):
- Feature Flags
- Casos de uso transacionais
- Campanhas da API
- Campanhas disparadas por API
- Canvases acionados por API
- Campanhas acionadas pela API Braze (`/messages` e `/send`)

Não é necessário adicionar uma tag de exceção para nenhum desses casos de uso, pois as listas de supressão automaticamente não se aplicarão a eles. Para excluir um grupo de usuários de uma mensagem dentro desses casos de uso, é necessário criar um segmento de direcionamento que exclua esses usuários.

{% alert important %}
Durante a beta, coletamos feedback dos clientes para ajudar a melhorar nosso produto. Diga ao seu gerente de sucesso do cliente se você planeja aplicar listas de supressão a casos de uso transacionais.
{% endalert %}

### Canais afetados por listas de supressão

Listas de supressão são dinâmicas e se aplicarão automaticamente a todos os seguintes canais (a menos que a campanha ou Canvas contenha uma tag de exceção): 
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

## Configuração de listas de supressão

Como as listas de supressão podem afetar significativamente o envio de mensagens, somente os administradores podem editar, salvar, ativar e desativar listas de supressão (todos os usuários podem visualizar as listas de supressão).

1. Acesse **Público** > **Listas de supressão**.<br><br>![A página "Listas de Supressão" com uma lista de três listas de supressão.][1]<br><br>
2. Selecione **Criar lista de supressão** e adicione um nome.<br><br>![Uma janela chamada "Criar uma Lista de Supressão" com um campo para inserir um nome.][2]{: style="max-width:80%;"}<br><br>
3. Use filtros de segmento para identificar os usuários em suas listas de supressão. Você deve selecionar pelo menos um.

{% alert important %}
Embora o processo de configuração pareça semelhante à [criação de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), uma lista de supressão é um grupo de usuários que você **não** deseja enviar mensagens, independentemente da associação ao segmento.
{% endalert %}

![Um construtor de lista de supressão com um filtro para usuários que abriram um e-mail pela última vez há mais de 90 dias.][3]

{: start="4"}
4\. Determine se deseja ter exceções com base na tag marcando a caixa abaixo do nome do seu segmento (consulte [Como funciona](#how-it-works) para obter mais informações) e, em seguida, adicione as tags de campanhas ou Canvas que os usuários nessa lista de supressão ainda devem receber. <br><br>Em outras palavras, se você adicionar a tag de exceção "Shipping confirmation" (Confirmação de envio), os usuários da sua lista de supressão serão excluídos de todos os envios de mensagens, exceto aqueles que usam a tag "Shipping confirmation" (Confirmação de envio).<br><br>![A seção "Detalhes da Lista de Envio" com uma tag de exceção aplicada chamada "Confirmação de envio".][4]<br><br>
5\. Salve ou ative sua lista de supressão.
- Quando você salva, sua lista de supressão será salva, mas não será ativada, o que significa que não entrará em vigor. Sua lista de supressão permanecerá inativa até que você a ative, e listas de supressão inativas não impactarão o envio de mensagens (usuários não serão excluídos das mensagens).
- Quando você ativa, sua lista de supressão será salva e entrará em vigor imediatamente, o que significa que usuários em sua lista de supressão serão imediatamente excluídos de campanhas ou Canvases (exceto aqueles que contêm uma tag de exceção).

{% alert note %}
Apenas administradores podem salvar ou ativar listas de supressão. Você pode ter até cinco listas de supressão ativas ao mesmo tempo na versão beta.
{% endalert %}

Você pode desativar ou arquivar listas de supressão quando não precisar mais delas. 
- Para desativar, selecione uma lista de supressão ativa e selecione **Desativar**. Listas de supressão desativadas podem ser reativadas mais tarde.
- Para arquivar, faça isso a partir da página **Listas de Supressão**.

## Uso da lista de supressão

### Para campanhas

![A seção "Listas de Supressão" com uma lista de supressão ativa, chamada "Baixas pontuações de integridade de marketing".][5]

Se um usuário estiver em uma lista de supressão, ele não receberá uma campanha à qual essa lista de supressão se aplica. Consulte [Mensagens não afetadas por listas de supressão](#messages-not-affected-by-suppression-lists) para saber os casos em que uma lista de supressão não se aplica.

#### Verificação de quais listas de supressão são aplicadas

Para verificar o uso da lista de supressão em uma campanha, acesse a seção **Lista de supressão** na página **Público-alvo** para ver quais listas de supressão estão sendo aplicadas a essa campanha.

### Para telas

Se um usuário estiver em uma lista de supressão, ele ainda entrará no Canvas, mas não poderá receber etapas de mensagens dentro do Canva. Quando avançarem para uma etapa de Mensagens, eles sairão do Canva. No entanto, um usuário em uma lista de supressão ainda pode receber etapas que não sejam de envio de mensagens antes de uma etapa de mensagem. 

#### Impedindo que segmentos entrem em um Canva

Para que um segmento não seja inserido em **nenhum** canva, você pode configurar as definições de destino do canva para excluir esse segmento seguindo estas etapas:

1. Crie um segmento usando os mesmos filtros e critérios de sua lista de supressões.
2. Na etapa **Alvo**, use o filtro **Inscrição em segmento** para direcionar os usuários que não estão incluídos em seu segmento.

Por exemplo, digamos que você tenha um Canva com uma lista de supressão aplicada. O Canva tem uma etapa de atualização do usuário seguida de uma etapa de mensagem. Nesse cenário, os usuários da lista de supressão entrarão no Canvas, passarão pela etapa de Atualização do usuário (onde o usuário pode ser atualizado, com base em como essa etapa está configurada) e, em seguida, sairão na etapa de Mensagens (momento em que o usuário será incluído na métrica "Saído"). 

#### Verificação de quais listas de supressão são aplicadas

Para verificar o uso da lista de supressão em um canvas, acesse a seção **Lista de supressão** na página **Público-alvo** para ver quais listas de supressão estão sendo aplicadas a esse canvas. Você também pode visualizar as listas de supressão aplicadas na etapa **Resumo**.

[1]: {% image_buster /assets/img/suppression_lists_home.png %}
[2]: {% image_buster /assets/img/create_suppression_list.png %}
[3]: {% image_buster /assets/img/suppression_list_filters.png %}
[4]: {% image_buster /assets/img/exception_tags.png %}
[5]: {% image_buster /assets/img/active_suppression_list.png %}
