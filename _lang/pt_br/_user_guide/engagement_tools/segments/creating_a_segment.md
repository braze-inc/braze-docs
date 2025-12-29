---
nav_title: Criação de um segmento
article_title: Criação de um segmento
page_order: 0
page_type: tutorial
description: "Este artigo explica como configurar e criar um segmento usando o Braze."
tool: Segments
search_rank: 3
---

# [![Curso de aprendizado do Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"} Criando um segmento

> A segmentação permite que você direcione os usuários com base em suas características e ações demográficas, comportamentais ou técnicas. O uso criativo e inteligente da segmentação e da automação de mensagens permite que você mova seus usuários do primeiro contato para o cliente de longo prazo. Os segmentos são atualizados em tempo real à medida que os dados são alterados, e você pode criar quantos segmentos forem necessários para fins de segmentação e envio de mensagens.

## Etapa 1: Navegue até a seção de segmentos

Vá para **Audience** > **Segments**( **Público** > **Segmentos**).

## Etapa 2: Dê um nome ao seu segmento

Selecione **Create Segment (Criar segmento** ) para começar a criar seu segmento. Nomeie seu segmento descrevendo o tipo de usuário que pretende filtrar. Isso o ajudará a identificar o segmento quando quiser direcioná-lo para suas campanhas ou Canvases. Títulos vagos de segmentos podem ser confusos.

Opcionalmente, você pode fazer o seguinte:
- Adicione uma descrição ao segmento para fornecer mais detalhes sobre a intenção desse público e deixe anotações para que outros membros da equipe possam consultar.
- Adicione uma [equipe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) ao seu segmento.
- Adicione [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) ao seu segmento para maior organização.

Crie um modal de segmento em que o segmento seja chamado de "Lapsed Users" (Usuários inativos) com a descrição do segmento como "This is our main Lapsed User segment to target non-actives within the past fourteen days." (Este é o nosso principal segmento de usuários inativos para direcionar os não ativos nos últimos 14 dias) com dois botões: Cancel e Create Segment.]({% image_buster /assets/img_archive/segment_app_selection.png %}){: style="max-width:80%;"}

## Etapa 3: Escolha seu aplicativo ou plataforma

Escolha quais aplicativos ou plataformas você deseja segmentar selecionando **Usuários de todos os aplicativos** (padrão) ou **Usuários de aplicativos específicos**. **Usuários de aplicativos específicos** tem como alvo usuários com pelo menos uma sessão nos aplicativos especificados.

Por exemplo, se você quiser enviar uma mensagem in-app somente para dispositivos iOS, selecione seu aplicativo iOS. Isso garantirá que os usuários que possam usar tanto um dispositivo iOS quanto um Android recebam a mensagem apenas no dispositivo iOS. Na lista de aplicativos específicos, a opção **Usuários de nenhum** aplicativo permite incluir usuários sem sessões e sem dados de aplicativos (normalmente criados por meio de importação de usuário ou API REST).

Painel Segment Details (Detalhes do segmento) com a opção "Users from all apps" (Usuários de todos os aplicativos) selecionada na seção Apps Used (Aplicativos usados).]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## Etapa 4: Adicione filtros ao seu segmento

Adicione pelo menos um filtro ao seu segmento. Você pode combinar quantos filtros quiser para tornar sua segmentação mais específica. 

{% alert note %}
O Braze não gera perfis para os usuários até que eles tenham usado o aplicativo pela primeira vez, portanto, você não pode segmentar usuários que ainda não abriram seu aplicativo.
{% endalert %}

#### Grupos de filtros

Os filtros são organizados em grupos de filtros. Todo filtro deve fazer parte de um grupo de filtros que tenha no mínimo um filtro. Um segmento pode ter vários grupos de filtros. Para adicionar um, selecione **Adicionar grupo de filtros**. Edite o nome do grupo de filtros selecionando o ícone que aparece quando você passa o mouse ao lado dele.

Grupo de filtros com um ícone de edição ao lado de seu nome.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

Selecione os ícones ao lado de cada filtro para recolher o editor de filtros ou duplicar filtros individuais. Depois de duplicar um filtro, você pode ajustar seus valores em cada menu suspenso.

#### Lógica de segmentação usando AND e OR

Em um grupo de filtros, os filtros podem ser unidos por "AND" ou "OR". Entre os grupos de filtros, os grupos podem ser unidos por "E" ou "OU". Ao usar grupos de filtros, você pode criar uma lógica de segmentação, como:
- (A E B E C) OU (C E E E E F)
- (A OU B OU C) E (C OU D OU F)

Selecionar "OR" para seus filtros significa que seu segmento conterá usuários que satisfaçam qualquer combinação de um, alguns ou todos esses filtros. Selecionar "AND" significa que os usuários que não passarem nesse filtro não serão incluídos no seu segmento.

{% alert tip %}
Ao selecionar "OU" para filtros que incluem um filtro negativo (como "não está" em um grupo de assinatura), lembre-se de que os usuários só precisam atender a um dos filtros "OU" para serem incluídos no segmento. Para aplicar o filtro negativo independentemente dos outros filtros, use um [grupo de exclusão](#exclusion).
{% endalert %}

{% details When to avoid the OR operator %}

Pode haver situações de direcionamento de usuários em que o uso do operador `OR` deve ser evitado. O operador `OR` cria uma declaração que é avaliada como verdadeira se um usuário atender aos critérios de um ou mais filtros em uma declaração. Por exemplo, se você quiser criar um segmento de usuários que pertençam a "Foodies", mas não pertençam a "Non-foodies" ou "Candy-lovers", o operador `OR` funcionaria aqui.

Grupo de filtro para usuários no segmento "foodies" e não nos segmentos "non-foodies" ou "candy-lovers".]({% image_buster /assets/img_archive/or_operator_segment.png %})

No entanto, se o seu objetivo for segmentar os usuários que pertencem ao segmento "Foodies" e não estão em nenhum dos segmentos "Non-foodies" e "Candy-lovers", use o operador `AND`. Dessa forma, os usuários que recebem a campanha ou o Canvas estão no segmento pretendido ("foodies") e não nos outros segmentos ("Non-foodies" e "Candy-lovers") ao mesmo tempo. 

Os seguintes critérios de direcionamento negativo não devem ser usados com o operador `OR` quando dois ou mais filtros estiverem fazendo referência ao mesmo atributo:

- `not included`
- `is not`
- `does not equal`
- `does not match regex`

Se `not included`, `is not`, `does not equal`, ou `does not match regex` forem usados com o operador `OR` duas ou mais vezes em uma declaração, os usuários com todos os valores do atributo relevante serão direcionados.

{% enddetails %}

#### Operadores de filtro

Dependendo do filtro específico selecionado, você terá diferentes operadores para identificar os valores do filtro. Para se aprofundar nos operadores disponíveis para diferentes tipos de atributos personalizados, consulte [Armazenamento de atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes). Observe que, ao usar o operador "is any of", o número máximo de itens que você pode incluir nesse campo é 256.

{% alert note %}
O Braze não gera perfis para os usuários até que eles tenham usado o aplicativo pela primeira vez, portanto, você não pode segmentar usuários que ainda não abriram seu aplicativo.
{% endalert %}

\![Grupos de filtros do segmentador com o operador AND.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

{% alert important %}
Os segmentos que já usam o filtro **Segment Membership** não podem ser incluídos ou aninhados em outros segmentos. Isso evita um ciclo em que o Segmento A inclui o Segmento B, que, por sua vez, tenta incluir o Segmento A novamente. Se isso acontecesse, o segmento continuaria fazendo referência a si mesmo, tornando impossível calcular quem realmente pertence a ele.

Além disso, o aninhamento de segmentos como esse aumenta a complexidade e pode tornar as coisas mais lentas. Em vez disso, recrie o segmento que está tentando incluir usando os mesmos filtros.
{% endalert %}

#### Grupos de exclusão (opcional) {#exclusion}

Ao criar um segmento, você pode aplicar um ou vários grupos de exclusão. Os grupos de exclusão contêm critérios que identificam os usuários a serem excluídos do seu segmento e sempre serão conectados aos seus grupos de filtros com um operador "AND NOT".

Os grupos de exclusão substituem os critérios de segmento. Se um usuário se enquadrar nos critérios do grupo de exclusão, ele não fará parte do seu segmento, mesmo que atenda aos critérios dos grupos de filtros.

Crie um grupo de exclusão adicionando filtros como você faria para grupos de filtros. A estatística _Estimated Reachable Users (Usuários alcançáveis estimados_ ) em um grupo de exclusão mostra o número estimado de usuários restantes em seu segmento após a aplicação dos critérios de exclusão.

Os usuários excluídos não serão contados como parte da estatística _Total de usuários acessíveis_ do seu segmento.

\![Um grupo de exclusão com dois filtros.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

#### Visualização de estatísticas do funil

Selecione **View funnel statistics (Exibir estatísticas do funil** ) para exibir as estatísticas desse grupo de filtros e ver como cada filtro adicionado afeta as estatísticas do segmento. Você verá uma contagem estimada e uma porcentagem de usuários que são direcionados por todos os filtros até esse ponto. Depois que as estatísticas forem exibidas para um grupo de filtros, elas serão atualizadas automaticamente sempre que você alterar os filtros. Essas estatísticas são estimadas e podem levar algum tempo para serem geradas.

Lembre-se de que, se você usar AND entre os filtros, as estatísticas do funil diminuirão; se você usar OR entre os filtros, as estatísticas do funil aumentarão.

\![Dois filtros com estatísticas de funil de segmento.]({% image_buster /assets/img_archive/segment_funnel_statistics.png %})

Ao adicionar filtros que documentam o fluxo do usuário, você pode ver os pontos em que os usuários caem. Por exemplo, se você for um aplicativo de rede social e quiser ver onde pode estar perdendo usuários durante o processo de integração, talvez queira adicionar filtros de dados personalizados para inscrição, adição de amigos e envio da primeira mensagem. Se você descobrir que 85% dos usuários estão se inscrevendo e adicionando amigos, mas apenas 45% enviaram a primeira mensagem, saberá que deve se concentrar em incentivar mais envios de mensagens durante suas campanhas de integração e marketing.

#### Segmentos de teste

Depois de adicionar aplicativos e filtros ao seu segmento, você pode testar se o segmento está configurado conforme o esperado, procurando um usuário para confirmar se ele corresponde aos critérios do segmento. Para isso, procure o endereço `external_id` ou `braze_id` de um usuário na seção **User Lookup**. Observe que não é possível pesquisar por endereço de e-mail no **User Lookup**.

\![Seção User Lookup com um campo de pesquisa.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%;"}

A pesquisa de usuário está disponível quando:
- Criação de um segmento
- Configuração de uma campanha ou público-alvo do Canvas
- Configuração de uma etapa do Audience Paths

Quando um usuário corresponder aos critérios de segmento, filtro e aplicativo, um alerta indicará isso.

Uma pesquisa de usuário de "testuser" aciona um alerta informando: "testuser corresponde a todos os segmentos, filtros e aplicativos.]({% image_buster /assets/img_archive/user_lookup_match.png %})

Quando um usuário não corresponde a parte ou a todos os critérios de segmento, filtro ou aplicativo, os critérios ausentes são listados para fins de solução de problemas.

\![Uma pesquisa de usuário com um alerta informando "test1 não corresponde aos seguintes critérios de direcionamento:" e exibe os critérios ausentes.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

#### Segmentos de usuário único

É possível criar segmentos de usuários individuais (ou segmentos de alguns usuários) usando atributos exclusivos que identificam os usuários, como um nome de usuário ou um ID de usuário.

No entanto, as estatísticas de segmentação ou a visualização podem não mostrar esse usuário individual porque as estatísticas de segmento são calculadas com base em uma amostra aleatória com um intervalo de confiança de 95% de que o resultado está dentro de +/- 1%. Quanto maior for a sua base de usuários, maior será a probabilidade de que o tamanho do seu segmento seja uma estimativa aproximada. Para ter certeza de que seu segmento contém o único usuário que você está segmentando, selecione **Calculate exact statistics (Calcular estatísticas exatas**). Isso calculará o número exato de usuários em seu segmento com mais de 99,999% de precisão.

O Braze tem filtros de teste para direcionar usuários específicos por ID de usuário ou endereço de e-mail.

## Etapa 5: Salve seu segmento

Selecione **Salvar**. Agora você está pronto para começar a enviar mensagens aos seus usuários!

## Medição do tamanho do segmento

Para saber como monitorar a associação e o tamanho do seu segmento, consulte [Medição do tamanho do segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/).

## Segmentos de arquivamento

Se você não precisar mais de um segmento específico ou não quiser retirá-lo, poderá arquivá-lo acessando a página **Segments (Segmentos** ) e selecionando **Archive (Arquivar** ) no menu da linha desse segmento.

{% alert warning %}
Quando você arquivar um segmento, todas as campanhas ou Canvases que o utilizarem (mesmo que o segmento seja usado apenas em um único componente do Canvas) também serão arquivados. Isso também inclui segmentos aninhados em que ambos os segmentos e quaisquer campanhas ou Canvases que os utilizem também serão arquivados.
<br><br>
Você receberá um aviso listando quais campanhas e Canvases estão prestes a ser arquivadas ao arquivar o segmento associado.
{% endalert %}

Você pode desarquivar o segmento navegando até ele na página **Segments (Segmentos** ) e selecionando **Unarchive (Desarquivar**).

## Comportamento de segmentação quando os usuários têm vários dispositivos

Os usuários têm mais de um dispositivo se fizerem login na mesma conta em vários dispositivos. É possível verificar se há vários dispositivos na seção **Recent Devices (Dispositivos recentes** ) de um [perfil de usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/).

Ao segmentar com filtros dependentes do dispositivo (modelo do dispositivo, sistema operacional do dispositivo e versão do aplicativo), seu segmento conterá todos os usuários que correspondem aos critérios do filtro. Esses usuários receberão uma mensagem em todos os seus dispositivos, incluindo aqueles que talvez não atendam aos critérios do filtro. Por exemplo, digamos que o usuário A tenha dois dispositivos: O dispositivo 1 é o OS 13.0 e o dispositivo 2 é o OS 10.0. Se um segmento tiver como alvo usuários com OS 10.0, esse usuário fará parte desse segmento e receberá mensagens em ambos os dispositivos.

### Notificações push

Você pode especificar que apenas uma notificação push seja enviada a cada usuário. Ao [redigir sua mensagem]({{ssite.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#step-4-compose-your-push-message), selecione **Enviar somente para o último dispositivo usado pelo usuário** em **Configurações adicionais**.

\!["Configurações adicionais" com uma caixa de seleção para enviar apenas para o último dispositivo usado pelo usuário.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### Considerações

- **As mensagens enviadas podem exceder o tamanho do público.** Quando alguns usuários têm mais de um dispositivo, cada dispositivo pode receber uma mensagem. Isso causa um número maior de envios de mensagens do que os usuários do seu segmento.
- **A associação de segmento de um usuário pode não ter a aparência esperada.**
    - Um usuário pode ser direcionado em seu dispositivo atual com base em atributos associados a um dispositivo diferente. Se você não esperava que um usuário recebesse uma mensagem, verifique se há vários dispositivos no perfil do usuário.
    - Um usuário pode ter estado em seu segmento-alvo no momento do envio, mas, devido a comportamentos associados a qualquer um de seus dispositivos, pode não fazer parte desse segmento posteriormente. Isso pode fazer com que um usuário receba uma campanha ou um Canvas mesmo que não corresponda aos critérios do filtro. <br><br>Por exemplo, um usuário pode receber uma mensagem direcionada a usuários com uma versão mais recente do aplicativo do OS 10.0, mesmo que ele tenha atualmente o OS 13.0. Nesse caso, o usuário tinha o OS 10.0 quando a mensagem foi enviada e depois fez o upgrade para o OS 13.0.<br><br> Da mesma forma, se um usuário usar posteriormente um dispositivo com uma versão diferente do aplicativo, seu perfil de usuário será atualizado com uma nova versão mais recente do aplicativo. Isso pode fazer com que pareça que o usuário não deveria ter se qualificado para a mensagem, mesmo que tenha se qualificado quando ela foi enviada.


