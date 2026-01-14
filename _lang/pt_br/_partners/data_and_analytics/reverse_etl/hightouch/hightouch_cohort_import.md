---
nav_title: Importação do coorte Hightouch
article_title: Importação do coorte Hightouch
description: "Este artigo de referência descreve a funcionalidade de importação de coorte da Hightouch, uma plataforma para sincronizar os dados de seus clientes de seu data warehouse com ferramentas de negócios."
page_type: partner
search_tag: Partner

---
# Importação do coorte Hightouch

> Este artigo descreve como fazer a importação de coortes de usuários do [Hightouch](https://hightouch.io) para o Braze para que você possa enviar campanhas direcionadas com base em dados que podem existir apenas em seu data warehouse. Para saber mais sobre a integração do Hightouch e suas outras funcionalidades, consulte o [artigo principal sobre o Hightouch]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch/).

## Integração de importação de dados

### Etapa 1: Obter a chave de importação de dados do Braze
Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Hightouch**. 

Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente.<br><br>![]({% image_buster /assets/img/hightouch/data_import_key.png %}){: style="max-width:90%;"} 

### Etapa 2: Adicionar coortes do Braze como um destino no Hightouch
Navegue até a página **Destino** em seu espaço de trabalho Hightouch, procure por **Braze Coortes** e clique em **Continuar**. Agora copie seu endpoint REST e a chave de importação de dados e clique em **Continue** (Continuar).<br><br>![]({% image_buster /assets/img/hightouch/cohort1.png %}){: style="max-width:90%;"}

### Etapa 3: Sincronizar um modelo (ou público) no Braze Coortes
Na Hightouch, usando seu [modelo](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) ou [público](https://hightouch.io/docs/audiences/usage/) criado, crie uma nova sincronização. Em seguida, selecione o destino das coortes da Braze que você criou na etapa anterior. Por fim, na configuração de destino das coortes da Braze, selecione o identificador que deseja comparar e decida se quer ou não que a Hightouch crie uma nova coorte da Braze ou atualize uma já existente.<br><br>![]({% image_buster /assets/img/hightouch/cohort2.png %}){: style="max-width:90%;"}

{% alert important %}
Somente os usuários que já existem no Braze serão adicionados ou removidos de um coorte. A importação de coorte não criará novos usuários no Braze.
{% endalert %}

### Etapa 4: Criar um segmento Braze a partir do público personalizado Hightouch
No Braze, navegue até **Segments (Segmentos**), crie um novo segmento e selecione **Hightouch Cohorts (Coortes Hightouch)** como seu filtro. Aqui você pode escolher qual coorte da Hightouch deseja incluir. Depois que seu segmento de coorte do Hightouch for criado, você poderá selecioná-lo como um filtro de público ao criar uma campanha ou uma tela.<br><br>![]({% image_buster /assets/img/hightouch/cohort3.png %}){: style="max-width:90%;"}

### Usando essa integração
Para usar seu segmento da Hightouch, crie uma campanha da Braze ou um canva e selecione o segmento como seu público-alvo.<br><br>![]({% image_buster /assets/img/hightouch/cohort4.png %}){: style="max-width:90%;"}

## Correspondência de usuários

Os usuários identificados podem ser combinados pelo endereço `external_id` ou `alias`. Os usuários anônimos podem ser combinados pelo site `device_id`. Os usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo endereço `device_id` e devem ser identificados pelo endereço `external_id` ou `alias`.

