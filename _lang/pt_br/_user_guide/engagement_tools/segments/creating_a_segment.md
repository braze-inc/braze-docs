---
nav_title: Criação de um segmento
article_title: Criação de um segmento
page_order: 1
page_type: tutorial
description: "Este artigo explica como configurar e criar um segmento usando a Braze."
tool: Segments
search_rank: 3
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %}](https://learning.braze.com/segmentation-course) ){: style="float:right;width:120px;border:0;" class="noimgborder"}Criando um segmento

> A segmentação permite o direcionamento de usuários com base em suas características e ações demográficas, comportamentais ou técnicas. O uso criativo e inteligente da segmentação e da automação do envio de mensagens ativa a capacitação para mover seus usuários do primeiro contato para o cliente de longo prazo. Os segmentos são atualizados em tempo real à medida que os dados mudam, e você pode criar quantos segmentos forem necessários para fins de direcionamento e envio de mensagens.

## Etapa 1: Navegue até a seção de segmentos

Acesse **Público** > **Segmentos**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar **os Segmentos** em **Engajamento**.
{% endalert %}

## Etapa 2: Dê um nome ao seu segmento

Selecione **Create Segment (Criar segmento** ) para começar a criar seu segmento. Nomeie seu segmento descrevendo o tipo de usuário que pretende filtrar. Isso o ajudará a identificar o segmento quando quiser direcioná-lo para suas campanhas ou Canvas. Títulos vagos de segmentos podem ser confusos.

Como opção, você também pode fazer o seguinte:
- Adicione uma descrição ao segmento para fornecer mais detalhes sobre a intenção desse público e deixe notas para que outros membros da equipe possam consultá-las.
- Adicione uma [equipe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) ao seu segmento.
- Adicione [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) ao seu segmento para maior organização.

![Crie um modal de segmento em que o segmento seja chamado de "Lapsed Users" (Usuários que perderam a validade) com a descrição do segmento como "This is our main Lapsed User segment to target non-actives within the past fourteen days." (Este é o nosso principal segmento de usuários que perderam a validade para direcionamento de não ativos nos últimos 14 dias) com dois botões: Cancelar e criar segmento.][2]{: style="max-width:70%;"}

## Etapa 3: Escolha seu app ou plataforma

Escolha quais aplicativos ou plataformas deseja direcionar, selecionando **Usuários de todos os aplicativos** (padrão) ou **Usuários de aplicativos específicos**. Se você escolher **Usuários de todos os apps**, o segmento incluirá todos os usuários, independentemente de qualquer sessão ou dados do app. Se você escolher **Usuários de aplicativos específicos**, poderá selecionar quais apps ou plataformas deseja incluir no seu segmento.

Por exemplo, se quiser enviar uma mensagem no app somente para dispositivos iOS, selecione seu app iOS. Isso garantirá que os usuários que possam usar tanto um dispositivo iOS quanto um Android recebam a mensagem apenas em seu dispositivo iOS. Na lista de aplicativos específicos, a opção **Usuários de nenhum** aplicativo permite incluir usuários sem sessões e sem dados de aplicativos (normalmente criados por meio da importação de usuários ou da API REST).

![Painel Segment Details (Detalhes do segmento) com a opção "Users from all apps" (Usuários de todos os aplicativos) selecionada na seção Apps Used (Aplicativos usados).][5]{: style="max-width:70%;"}

## Etapa 4: Adicione filtros ao seu segmento

Adicione pelo menos um filtro ao seu segmento. Você pode combinar quantos filtros quiser para tornar sua segmentação mais específica.

{% alert note %}
O Braze não gera perfis para os usuários até que eles tenham usado o aplicativo pela primeira vez, portanto, não é possível fazer o direcionamento para usuários que ainda não abriram o aplicativo.
{% endalert %}

#### Grupos de filtros

Os filtros são organizados em grupos de filtros. Todo filtro deve fazer parte de um grupo de filtros que tenha no mínimo um filtro. Um segmento pode ter vários grupos de filtros. Para adicionar um, selecione **Adicionar grupo de filtros**. Edite o nome do grupo de filtros selecionando o ícone que aparece quando você passa o mouse ao lado dele.

![Grupo de filtros com um ícone de edição ao lado do nome.][14]{: style="max-width:70%;"}

Selecione os ícones ao lado de cada filtro para recolher o editor de filtros, duplicar o filtro ou remover o filtro. Depois de duplicar um filtro, você pode ajustar seus valores em cada menu suspenso.

Você também pode usar o ícone em cada grupo de filtros para duplicar esse grupo de filtros e os filtros contidos nele ou excluir esse grupo de filtros do seu segmento.

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

![Grupos de filtros do segmentador com o operador AND.][9]{: style="max-width:70%;"}

{% alert important %}
Os segmentos que já usam o filtro **Inscrição em segmento** não podem ser incluídos ou aninhados em outros segmentos.
{% endalert %}

#### Grupos de exclusão (opcional) {#exclusion}

Ao criar um segmento, você pode aplicar um ou vários grupos de exclusão. Os grupos de exclusão contêm critérios que identificam os usuários a serem excluídos do seu segmento e sempre serão conectados aos seus grupos de filtros com um operador "AND NOT".

Os grupos de exclusão substituem os critérios de segmento. Se um usuário se enquadrar nos critérios do grupo de exclusão, ele não fará parte do seu segmento, mesmo que atenda aos critérios dos grupos de filtros.

Crie um grupo de exclusão adicionando filtros como você faria para grupos de filtros. A estatística _Estimated Reachable Users (Usuários alcançáveis estimados_ ) em um grupo de exclusão mostra o número estimado de usuários restantes em seu segmento após a aplicação dos critérios de exclusão.

Os usuários excluídos não serão contados como parte da estatística _Total de usuários acessíveis_ do seu segmento.

![Um grupo de exclusão com dois filtros.][12]{: style="max-width:70%;"}

#### Segmentos de teste

Depois de adicionar apps e filtros ao seu segmento, você pode testar se o segmento está configurado conforme o esperado, procurando um usuário para confirmar se ele corresponde aos critérios do segmento. Para fazer isso, pesquise o endereço `external_id` ou `braze_id` de um usuário na seção **User Lookup**.

![Seção "Pesquisa de usuário" com um campo de pesquisa.][6]{: style="max-width:80%;"}

A pesquisa de usuário está disponível quando:
- Criação de um segmento
- Configuração de uma campanha ou público do Canvas
- Configuração de uma etapa de jornadas do público

Quando um usuário corresponder aos critérios de segmento, filtro e app, um alerta indicará isso.

![Uma pesquisa de usuário "user007" dispara um alerta informando: "user007 corresponde a todos os segmentos, filtros e apps.][7]{: style=" max-width:80%;"}

Quando um usuário não corresponde a parte ou a todos os critérios de segmento, filtro ou app, os critérios ausentes são listados para fins de solução de problemas.

![Uma pesquisa de usuário de "user1234" dispara um alerta dizendo: "user1234 não corresponde aos seguintes critérios de direcionamento:" e exibe dois critérios ausentes: uma posse maior que um ano e hoje ser um aniversário.][8]{: style=" max-width:80%;"}

#### Segmentos de usuário único

É possível criar segmentos de usuários únicos (ou segmentos de um punhado de usuários) usando atribuições exclusivas que identificam os usuários, como um nome de usuário ou um ID de usuário.

No entanto, as estatísticas de segmentação ou a prévia podem não mostrar esse usuário individual porque as estatísticas de segmento são calculadas com base em uma amostra aleatória com um intervalo de confiança de 95% de que o resultado está dentro de +/- 1%. Quanto maior for a sua base de usuários, maior será a probabilidade de que o tamanho do seu segmento seja uma estimativa aproximada. Para ter certeza de que seu segmento contém o único usuário que está sendo direcionado, selecione **Calculate exact statistics (Calcular estatísticas exatas**). Isso calculará o número exato de usuários em seu segmento com mais de 99,999% de precisão.

O Braze tem filtros de teste para direcionamento a usuários específicos por ID de usuário ou endereço de e-mail.

### Etapa 5: Salve seu segmento

Selecione **Salvar**. Agora você está pronto para começar a enviar mensagens aos seus usuários!

## Cálculo de associação de segmentos {#segment-membership-calculation}

O Braze atualiza a associação do segmento do usuário à medida que os dados são enviados de volta aos nossos servidores e processados, normalmente de forma instantânea. A associação de segmento de um usuário não será alterada até que a sessão seja processada. Por exemplo, um usuário que cair em um segmento de usuário expirado quando a sessão for iniciada será imediatamente removido do segmento de usuário expirado quando a sessão for processada.

### Cálculo do total de usuários acessíveis

Cada segmento exibe o número total de usuários que são membros desse segmento. Ao filtrar **Usuários de todos os apps**, ele também exibe todos os diferentes canais disponíveis para se comunicar com esses usuários, como web push ou e-mail. É possível que o número total de usuários seja diferente do número de usuários alcançáveis por cada canal.

![Uma tabela que exibe o total de usuários acessíveis, divididos por usuários acessíveis por e-mail, envio de e-mail para iOS, envio de e-mail para Android, envio de e-mail pela Web, envio de e-mail para Kindle e envio de e-mail para Android China.][10]

Para que um usuário seja listado como acessível por meio de um determinado canal, ele deve ter ambos:
* Um endereço de e-mail válido ou um token por push associado ao seu perfil; e
* Aceitação ou assinatura do seu app.

Um único usuário pode pertencer a diferentes grupos de usuários acessíveis. Por exemplo, um usuário pode ter um endereço de e-mail válido e um token por push válido para Android e ter aceitação em ambos, mas não ter um token por push para iOS associado. A diferença entre o total de usuários alcançáveis e a soma dos diferentes canais é o número de usuários que se qualificaram para o segmento, mas não são alcançáveis por meio desses canais de comunicação.

### Estatísticas para o tamanho do segmento

A Braze fornece as seguintes estatísticas sobre o tamanho do segmento. Todas as estatísticas estimadas estão dentro de 1% acima ou abaixo do valor real, e a associação exata do segmento sempre será calculada antes que um segmento seja afetado por uma mensagem enviada em uma campanha ou Canva.

#### Filtrar estatísticas

Para cada grupo de filtros, é possível visualizar os usuários alcançáveis estimados. Selecione **Expandir estatísticas extras do funil** para ver um detalhamento entre os canais.

![Um grupo de filtros com um filtro para um gênero que não seja desconhecido.][4]{: style="max-width:80%;"}

#### Estatísticas do segmento

Para um segmento inteiro, é possível visualizar os usuários alcançáveis estimados, bem como as contagens de usuários estimadas para cada canal, na parte inferior da página. Também é possível visualizar uma contagem exata de usuários acessíveis (tanto para o segmento como um todo quanto para cada canal) selecionando **Calcular estatísticas exatas**.

Note que:
- O cálculo de estatísticas exatas pode levar alguns minutos para ser executado. Essa função calcula apenas as estatísticas exatas no nível do segmento, não no nível do filtro ou do grupo de filtros.
- Em segmentos grandes, é normal haver uma pequena variação, mesmo ao calcular estatísticas exatas. Espera-se que a precisão desse recurso seja de 99,999% ou mais.

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

![][13]{: style="max-width:60%;"}

### Considerações

- **O envio de mensagens pode exceder o tamanho do público.** Quando alguns usuários têm mais de um dispositivo, cada dispositivo pode receber uma mensagem. Isso causa um número maior de envios de mensagens do que os usuários do seu segmento.
- **A associação de segmento de um usuário pode não ter a aparência esperada.**
    - Um usuário pode ser direcionado em seu dispositivo atual com base em atribuições associadas a um dispositivo diferente. Se não esperava que um usuário recebesse uma mensagem, verifique se há vários dispositivos no perfil do usuário.
    - Um usuário pode ter estado em seu segmento-alvo no momento do envio, mas, devido a comportamentos associados a qualquer um de seus dispositivos, pode não fazer parte desse segmento posteriormente. Isso pode fazer com que um usuário receba uma campanha ou um canva, mesmo que não corresponda aos critérios do filtro. <br><br>Por exemplo, um usuário poderia receber uma mensagem direcionando os usuários com uma versão mais recente do app do OS 10.0, mesmo que eles tenham atualmente o OS 13.0. Nesse caso, o usuário tinha o OS 10.0 quando a mensagem foi enviada e depois fez upgrade para o OS 13.0.<br><br> Da mesma forma, se um usuário usar posteriormente um dispositivo com uma versão diferente do app, seu perfil de usuário será atualizado com uma nova versão mais recente do app. Isso pode fazer com que pareça que o usuário não deveria ter se qualificado para a mensagem, mesmo que tenha se qualificado quando ela foi enviada.


[1]: {% image_buster /assets/img_archive/Segment1.png %}
[2]: {% image_buster /assets/img_archive/Segment2.png %}
[3]: {% image_buster /assets/img_archive/segment_step4.png %}
[4]: {% image_buster /assets/img_archive/segment_filter_stats.png %}
[5]: {% image_buster /assets/img_archive/segment_app_selection.png %}
[6]: {% image_buster /assets/img_archive/user_lookup.png %}
[7]: {% image_buster /assets/img_archive/user_lookup_match.png %}
[8]: {% image_buster /assets/img_archive/user_lookup_nomatch.png %}
[9]: {% image_buster /assets/img_archive/segmenter_filter_groups.png %}
[10]: {% image_buster /assets/img_archive/segmenter_reachable_users.png %}
[11]: {% image_buster /assets/img_archive/segmenter_and_or.png %}
[12]: {% image_buster /assets/img_archive/segmenter_exclusion_groups.png %}
[13]: {% image_buster /assets/img_archive/send_to_last_device.png %}
[14]: {% image_buster /assets/img_archive/edit_filter_group_name.png %}