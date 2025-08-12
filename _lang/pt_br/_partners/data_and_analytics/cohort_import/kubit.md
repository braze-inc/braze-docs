---
nav_title: Kubit
article_title: Importação do coorte Kubit
description: "Este artigo de referência descreve a funcionalidade de importação de coortes do Kubit, uma plataforma de análise de dados sem código e de autoatendimento que oferece insights instantâneos sobre o produto, permitindo a importação de coortes de usuários do Kubit e seu direcionamento no envio de mensagens do Braze."
page_type: partner
search_tag: Partner
---

# Importação do coorte Kubit

> Este artigo descreve como fazer a importação de coortes de usuários do [Kubit](https://kubit.ai/) para o Braze. Para saber mais sobre a integração do Kubit e suas outras funcionalidades, consulte o [artigo principal do Kubit]({{site.baseurl}}/partners/data_and_analytics/analytics/kubit/).

## Integração de importação de dados

### Etapa 1: Obter a chave de importação de dados do Braze

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Kubit**. Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. 

Após a geração, você pode criar outra chave ou invalidar uma existente. A chave de importação de dados e o ponto de extremidade REST são usados na próxima etapa ao configurar um postback no dashboard do Kubit.

![A página do parceiro de tecnologia Kubit no Braze.]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### Etapa 2: Configurar o Braze no Kubit

Forneça a chave de importação de dados do Braze e o ponto de extremidade Braze REST ao seu contato de suporte do Kubit. Eles configurarão a integração do lado deles e o informarão quando a integração estiver ativa.  

### Etapa 3: Importar coortes para Braze

#### Criar um coorte no Kubit
[Crie um coorte](https://www.kubit.ai/doc/fundamentals#cohort) no Kubit e defina os critérios de seus usuários-alvo.<br><br>![]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### Importação de usuários para o Braze
Depois de salvar sua coorte, você poderá importá-la para o Braze para ser usada nos segmentos da Braze. Esses segmentos podem então ser usados para criar campanhas de e-mail ou push e Canvas direcionados.

Para fazer isso, navegue até o coorte existente e, em **Controle de coorte**, selecione **Importar para o Braze**.

![]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

Em seguida, selecione a cadência de importação desejada. As importações únicas permitem que você importe uma vez agora. As importações agendadas permitem que você importe diariamente, semanalmente ou mensalmente em um horário específico. Note que cada coorte só pode ter uma programação de importação ativa. 

![]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

{% alert important %}
Somente os usuários que já existem no Braze serão adicionados ou removidos de um coorte. A importação de coorte não criará novos usuários no Braze.
{% endalert %}

#### Verificar o status da importação
Após a conclusão de uma importação, uma notificação por e-mail será enviada aos destinatários especificados na programação da importação. Você também pode verificar o status de importação de um coorte em **Schedule (Programação** ) no Kubit. O histórico do agendamento exibirá o tempo de execução de cada importação, o resultado e o número total de usuários no coorte que foram importados para o Braze.<br><br>![]({% image_buster /assets/img/kubit/import_history.png %})<br><br>Você pode disparar manualmente uma importação clicando no ícone **Importar para o Braze** para esse agendamento de importação.

### Etapa 4: Criar segmentos do Braze com coortes do Kubit
Depois de importar coortes para o Braze, você pode usá-los como filtros para criar segmentos do Braze e incluí-los em campanhas ou canvas do Braze. Visite nossa documentação de segmentos para saber mais sobre [como criar segmentos Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment).

![No criador de segmentos da Braze, o atributo de usuário "Kubit cohorts" é definido como "includes_value" e mostra uma lista de coortes disponíveis.]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

## Correspondência de usuários

Os usuários identificados podem ser combinados pelo endereço `external_id` ou `alias`. Os usuários anônimos podem ser combinados pelo site `device_id`. Os usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo endereço `device_id` e devem ser identificados pelo endereço `external_id` ou `alias`.