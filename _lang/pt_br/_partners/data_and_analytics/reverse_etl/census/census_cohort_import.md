---
nav_title: Census
article_title: Importação de coortes do Census
description: "Este artigo de referência descreve a funcionalidade de importação de usuários do Census, uma plataforma de integração de dados que permite criar dinamicamente segmentos de usuários direcionados com dados do seu data warehouse na nuvem."
page_type: partner
search_tag: Partner

---

# Importação de coorte do Census

> Este artigo descreve como fazer a importação de coortes de usuários do [Census](https://www.getcensus.com/) para o Braze. Para saber mais sobre a integração da Census, consulte o [artigo principal sobre a Census]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/census/).

## Integração da importação de coortes

### Etapa 1: Criar conexão de serviço Braze

Para integrar o Census na plataforma Census, navegue até a guia **Connections (Conexões)** e selecione **New Destination (Novo destino** ) para criar uma nova conexão de serviço Braze.

No prompt exibido, nomeie essa conexão e forneça o URL do endpoint da Braze, a chave da API REST da Braze e a chave de importação de dados. A chave de importação de dados é necessária para sincronizar coortes e pode ser encontrada no Braze acessando **Partner Integrations** > **Technology Partners** > **Census**.

![]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Etapa 2: Criar uma sincronização do Census

Para sincronizar clientes com o Braze, você deve criar uma sincronização. Aqui, você definirá onde sincronizar os dados e como deseja que os campos sejam mapeados entre as duas plataformas.

1. Navegue até a guia **Syncs (Sincronizações** ) e selecione **New Sync (Nova sincronização**).<br><br> 
2. No criador, selecione o modelo de dados de origem do seu data warehouse.<br><br>
3. Configure o local para onde o modelo será sincronizado. Selecione **Braze** como os destinos e **User & Coorte** como o objeto a ser sincronizado.<br>![No prompt "Select a Destination", "Braze" é selecionado como a conexão e vários objetos são listados.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Selecione a **coluna de origem** que identifica os usuários a serem adicionados a um coorte e selecione **ID de usuário externo** como o **tipo de identificador**.<br><br>
5. No menu suspenso **Nome da coorte**, selecione uma coorte, crie uma coorte ou selecione uma Coluna de origem para preencher o nome da coorte.<br><br>
6. Use o menu suspenso **Quando um registro é removido dos dados de origem** para selecionar o que acontece com os usuários quando eles são removidos do conjunto de dados de origem, como **Não fazer nada** ou **Remover registro correspondente do coorte**.<br><br>
7. Por fim, mapeie os campos de dados do Census para os campos equivalentes do Braze.<br>![Mapeamento do Census]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
8. Confirme os detalhes e crie a sincronização. 

Agora você pode executar sua sincronização!

Durante uma sincronização, todos os campos que você mapear serão primeiro sincronizados com o objeto do usuário para atualizar o que já existe no Braze. Depois disso, o usuário atualizado será adicionado à coorte especificada.

Após a sincronização, é possível criar e adicionar um segmento Braze com um filtro de coorte Census a futuras campanhas Braze e Canvas para direcionamento a esses usuários. 

{% alert note %}
Ao usar a integração do Census e do Braze, o Census enviará apenas os deltas (dados alterados) em cada sincronização para o Braze.
{% endalert %}

{% alert important %}
Somente os usuários que já existem no Braze serão adicionados ou removidos de um coorte. A importação de coorte não criará novos usuários no Braze.
{% endalert %}

## Correspondência de usuários

Os usuários identificados podem ser combinados pelo endereço `external_id` ou `alias`. Os usuários anônimos podem ser combinados pelo site `device_id`. Os usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo endereço `device_id` e devem ser identificados pelo endereço `external_id` ou `alias`.

