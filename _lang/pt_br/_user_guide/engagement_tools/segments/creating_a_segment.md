---
nav_title: Criação de um segmento
article_title: Criação de um segmento
page_order: 0
page_type: tutorial
description: "Este artigo explica como configurar e criar um segmento usando a Braze."
tool: Segments
search_rank: 3
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %}](https://learning.braze.com/segmentation-course) ){: style="float:right;width:120px;border:0;" class="noimgborder"}Criando um segmento

> A segmentação permite o direcionamento de usuários com base em suas características e ações demográficas, comportamentais ou técnicas. O uso criativo e inteligente da segmentação e da automação do envio de mensagens ativa a capacitação para mover seus usuários do primeiro contato para o cliente de longo prazo. Os segmentos são atualizados em tempo real à medida que os dados mudam, e você pode criar quantos segmentos forem necessários para fins de direcionamento e envio de mensagens.

## Etapa 1: Navegue até a seção de segmentos

Acesse **Público** > **Segmentos**.

## Etapa 2: Dê um nome ao seu segmento

Selecione **Create Segment (Criar segmento** ) para começar a criar seu segmento. Nomeie seu segmento descrevendo o tipo de usuário que pretende filtrar. Isso o ajudará a identificar o segmento quando quiser direcioná-lo para suas campanhas ou Canvas. Títulos vagos de segmentos podem ser confusos.

Como opção, você também pode fazer o seguinte:
- Adicione uma descrição ao segmento para fornecer mais detalhes sobre a intenção desse público e deixe notas para que outros membros da equipe possam consultá-las.
- Adicione uma [equipe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) ao seu segmento.
- Adicione [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) ao seu segmento para maior organização.

![Crie um modal de segmento em que o segmento seja chamado de "Lapsed Users" (Usuários que perderam a validade) com a descrição do segmento como "This is our main Lapsed User segment to target non-actives within the past fourteen days." (Este é o nosso principal segmento de usuários que perderam a validade para direcionamento de não ativos nos últimos 14 dias) com dois botões: Cancelar e criar segmento.]({% image_buster /assets/img_archive/segment_app_selection.png %}){: style="max-width:80%;"}

## Etapa 3: Escolha seu app ou plataforma

Escolha quais aplicativos ou plataformas deseja direcionar, selecionando **Usuários de todos os aplicativos** (padrão) ou **Usuários de aplicativos específicos**. Se você escolher **Usuários de todos os apps**, o segmento incluirá todos os usuários, independentemente de qualquer sessão ou dados do app. Se você escolher **Usuários de aplicativos específicos**, poderá selecionar quais apps ou plataformas deseja incluir no seu segmento.

Por exemplo, se quiser enviar uma mensagem no app somente para dispositivos iOS, selecione seu app iOS. Isso garantirá que os usuários que possam usar tanto um dispositivo iOS quanto um Android recebam a mensagem apenas em seu dispositivo iOS. Na lista de aplicativos específicos, a opção **Usuários de nenhum** aplicativo permite incluir usuários sem sessões e sem dados de aplicativos (normalmente criados por meio da importação de usuários ou da API REST).

![Painel Detalhes do segmento com a opção "Usuários de todos os apps" selecionada na seção Apps usados.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## Etapa 4: Adicione filtros ao seu segmento

Adicione pelo menos um filtro ao seu segmento. Você pode combinar quantos filtros quiser para tornar sua segmentação mais específica.

{% alert note %}
O Braze não gera perfis para os usuários até que eles tenham usado o aplicativo pela primeira vez, portanto, não é possível fazer o direcionamento para usuários que ainda não abriram o aplicativo.
{% endalert %}

#### Grupos de filtros

Os filtros são organizados em grupos de filtros. Todo filtro deve fazer parte de um grupo de filtros que tenha no mínimo um filtro. Um segmento pode ter vários grupos de filtros. Para adicionar um, selecione **Adicionar grupo de filtros**. Edite o nome do grupo de filtros selecionando o ícone que aparece quando você passa o mouse ao lado dele.

![Grupo de filtros com um ícone de edição ao lado de seu nome.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

Selecione os ícones ao lado de cada filtro para recolher o editor de filtros ou duplicar filtros individuais. Depois de duplicar um filtro, você pode ajustar seus valores em cada menu suspenso.

#### Lógica de segmentação usando AND e OR

Em um grupo de filtros, os filtros podem ser unidos por "AND" ou "OR". Entre os grupos de filtros, os grupos podem ser unidos por "E" ou "OU". Ao usar grupos de filtros, você pode criar uma lógica de segmentação, como:
- (A E B E C) OU (C E E E F)
- (A OU B OU C) E (C OU D OU F)

Selecionar "OR" para seus filtros significa que seu segmento conterá usuários que satisfaçam qualquer combinação de um, alguns ou todos esses filtros. A seleção de "AND" significa que os usuários que não passarem por esse filtro não serão incluídos no seu segmento.

{% alert tip %}
Ao selecionar "OU" para filtros que incluem um filtro negativo (como "não está" em um grupo de inscrições), lembre-se de que os usuários só precisam atender a um dos filtros "OU" para serem incluídos no segmento. Para aplicar o filtro negativo independentemente dos outros filtros, use um [grupo de exclusão](#exclusion).
{% endalert %}

#### Operadores de filtro

Dependendo do filtro específico selecionado, você terá diferentes operadores para identificar os valores do filtro. Para se aprofundar nos operadores disponíveis para diferentes tipos de atributos personalizados, consulte [Armazenamento de atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes). Observe que, ao usar o operador "is any of", o número máximo de itens que você pode incluir nesse campo é 256.

{% alert note %}
O Braze não gera perfis para os usuários até que eles tenham usado o aplicativo pela primeira vez, portanto, não é possível fazer o direcionamento para usuários que ainda não abriram o aplicativo.
{% endalert %}

![Grupos de filtros de segmentação com o operador AND.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

{% alert important %}
Os segmentos que já usam o filtro **Inscrição em segmento** não podem ser incluídos ou aninhados em outros segmentos. Isso evita um ciclo em que o Segmento A inclui o Segmento B, que, por sua vez, tenta incluir o Segmento A novamente. Se isso acontecesse, o segmento continuaria fazendo referência a si mesmo, tornando impossível calcular quem realmente pertence a ele.

Além disso, o aninhamento de segmentos como esse aumenta a complexidade e pode tornar as coisas mais lentas. Em vez disso, recrie o segmento que está tentando incluir usando os mesmos filtros.
{% endalert %}

#### Grupos de exclusão (opcional) {#exclusion}

Ao criar um segmento, você pode aplicar um ou vários grupos de exclusão. Os grupos de exclusão contêm critérios que identificam os usuários a serem excluídos do seu segmento e sempre serão conectados aos seus grupos de filtros com um operador "AND NOT".

Os grupos de exclusão substituem os critérios de segmento. Se um usuário se enquadrar nos critérios do grupo de exclusão, ele não fará parte do seu segmento, mesmo que atenda aos critérios dos grupos de filtros.

Crie um grupo de exclusão adicionando filtros como você faria para grupos de filtros. A estatística _Estimated Reachable Users (Usuários alcançáveis estimados_ ) em um grupo de exclusão mostra o número estimado de usuários restantes em seu segmento após a aplicação dos critérios de exclusão.

Os usuários excluídos não serão contados como parte da estatística _Total de usuários acessíveis_ do seu segmento.

![Um grupo de exclusão com dois filtros.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

#### Segmentos de teste

Depois de adicionar apps e filtros ao seu segmento, você pode testar se o segmento está configurado conforme o esperado, procurando um usuário para confirmar se ele corresponde aos critérios do segmento. Para fazer isso, pesquise o endereço `external_id` ou `braze_id` de um usuário na seção **User Lookup**.

![Seção User Lookup com um campo de pesquisa.]({% image_buster /assets/img_archive/user_lookup.png %})

A pesquisa de usuário está disponível quando:
- Criação de um segmento
- Configuração de uma campanha ou público do Canvas
- Configuração de uma etapa de jornadas do público

Quando um usuário corresponder aos critérios de segmento, filtro e app, um alerta indicará isso.

![Uma pesquisa de usuário de "testuser" dispara um alerta dizendo: "testuser corresponde a todos os segmentos, filtros e apps.]({% image_buster /assets/img_archive/user_lookup_match.png %})

Quando um usuário não corresponde a parte ou a todos os critérios de segmento, filtro ou app, os critérios ausentes são listados para fins de solução de problemas.

![Uma pesquisa de usuário com um alerta informando: "test1 não corresponde aos seguintes critérios de direcionamento:" e exibe os critérios ausentes.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

#### Segmentos de usuário único

É possível criar segmentos de usuários únicos (ou segmentos de um punhado de usuários) usando atribuições exclusivas que identificam os usuários, como um nome de usuário ou um ID de usuário.

No entanto, as estatísticas de segmentação ou a prévia podem não mostrar esse usuário individual porque as estatísticas de segmento são calculadas com base em uma amostra aleatória com um intervalo de confiança de 95% de que o resultado está dentro de +/- 1%. Quanto maior for a sua base de usuários, maior será a probabilidade de que o tamanho do seu segmento seja uma estimativa aproximada. Para ter certeza de que seu segmento contém o único usuário que está sendo direcionado, selecione **Calculate exact statistics (Calcular estatísticas exatas**). Isso calculará o número exato de usuários em seu segmento com mais de 99,999% de precisão.

O Braze tem filtros de teste para direcionamento a usuários específicos por ID de usuário ou endereço de e-mail.

## Etapa 5: Salve seu segmento

Selecione **Salvar**. Agora você está pronto para começar a enviar mensagens aos seus usuários!

## Medição do tamanho do segmento

Para saber como monitorar a associação e o tamanho do seu segmento, consulte [Medição do tamanho do segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/).

## Arquivamento de segmentos

Se não precisar mais de um segmento específico ou desejar retirá-lo, você poderá arquivá-lo acessando a página **Segmentos** e selecionando **Arquivar** no menu da linha desse segmento.

{% alert warning %}
Ao arquivar um segmento, todas as campanhas ou Canvas que o utilizarem (mesmo que o segmento seja usado apenas em um único componente do Canvas) também serão arquivados. Isso também inclui segmentos aninhados em que ambos os segmentos e quaisquer campanhas ou telas que os utilizem também serão arquivados.
<br><br>
Você receberá um aviso listando quais campanhas e telas estão prestes a ser arquivadas ao arquivar o segmento associado.
{% endalert %}

Você pode desarquivar o segmento navegando até ele na página **Segments (Segmentos** ) e selecionando **Unarchive (Desarquivar)**.

## Comportamento de direcionamento quando os usuários têm vários dispositivos

Os usuários têm mais de um dispositivo se registrarem a mesma conta em vários dispositivos. É possível verificar se há vários dispositivos na seção **Dispositivos recentes** de um [perfil de usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/).

Ao segmentar com filtros dependentes do dispositivo (modelo do dispositivo, sistema operacional do dispositivo e versão do app), seu segmento conterá todos os usuários que correspondem aos critérios do filtro. Esses usuários receberão uma mensagem em todos os seus dispositivos, incluindo aqueles que talvez não atendam aos seus critérios de filtragem. Por exemplo, digamos que o usuário A tenha dois dispositivos: O dispositivo 1 é o OS 13.0 e o dispositivo 2 é o OS 10.0. Se um segmento direcionar usuários com OS 10.0, esse usuário fará parte desse segmento e receberá mensagens em ambos os dispositivos.

### Notificações por push

É possível especificar que apenas uma notificação por push seja enviada a cada usuário. Ao [criar a mensagem]({{ssite.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#step-4-compose-your-push-message), selecione **Enviar apenas para o último dispositivo usado pelo usuário** em **Configurações adicionais**.

!["Addional settings" (Configurações adicionais) com uma caixa de seleção para enviar apenas para o último dispositivo usado pelo usuário.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### Considerações

- **O envio de mensagens pode exceder o tamanho do público.** Quando alguns usuários têm mais de um dispositivo, cada dispositivo pode receber uma mensagem. Isso causa um número maior de envios de mensagens do que os usuários do seu segmento.
- **A associação de segmento de um usuário pode não ter a aparência esperada.**
    - Um usuário pode ser direcionado em seu dispositivo atual com base em atribuições associadas a um dispositivo diferente. Se não esperava que um usuário recebesse uma mensagem, verifique se há vários dispositivos no perfil do usuário.
    - Um usuário pode ter estado em seu segmento-alvo no momento do envio, mas, devido a comportamentos associados a qualquer um de seus dispositivos, pode não fazer parte desse segmento posteriormente. Isso pode fazer com que um usuário receba uma campanha ou um canva, mesmo que não corresponda aos critérios do filtro. <br><br>Por exemplo, um usuário poderia receber uma mensagem direcionando os usuários com uma versão mais recente do app do OS 10.0, mesmo que eles tenham atualmente o OS 13.0. Nesse caso, o usuário tinha o OS 10.0 quando a mensagem foi enviada e depois fez upgrade para o OS 13.0.<br><br> Da mesma forma, se um usuário usar posteriormente um dispositivo com uma versão diferente do app, seu perfil de usuário será atualizado com uma nova versão mais recente do app. Isso pode fazer com que pareça que o usuário não deveria ter se qualificado para a mensagem, mesmo que tenha se qualificado quando ela foi enviada.


