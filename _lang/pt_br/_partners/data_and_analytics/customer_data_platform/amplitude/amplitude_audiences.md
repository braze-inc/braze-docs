---
nav_title: Amplitude
article_title: Amplitude
page_order: 0
alias: /partners/amplitude_recommend/
description: "Este artigo de referência descreve a parceria entre a Braze e a Amplitude, uma plataforma de análise de dados e business intelligence de produtos."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Curso do Braze Learning ]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude

> A [Amplitude](https://amplitude.com/) é uma plataforma de análise de dados e business intelligence de produtos.

A integração bidirecional entre o Braze e o Amplitude permite a [importação de coortes]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/), características de usuários e eventos do Amplitude para o Braze, bem como a criação de segmentos que podem direcionar os usuários em futuras campanhas ou canvas. Você também pode aproveitar o Braze Currents para [exportar seus eventos do Braze para o Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/#data-export-integration) para realizar análises mais profundas de seus dados de produto e marketing.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta de Amplitude | É necessário ter uma [conta da Amplitude](https://amplitude.com/) para usar essa parceria. |
| Currents | Para exportar dados de volta para o Amplitude, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado em sua conta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Escolha uma integração 

A Amplitude e a Braze oferecem dois métodos de integração diferentes. Leia a documentação a seguir para decidir quais métodos atenderão às suas necessidades:

- Transmissão do evento do Braze: Uma integração que permite que você encaminhe dados brutos de eventos do Amplitude diretamente para o Braze.
- [Importação de coorte]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/): Uma integração que lhe permite encaminhar coortes do Amplitude para o Braze.

## Transmissão de eventos do Braze

### Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Chave da API REST do Braze | Uma chave da API REST do Braze com todas as permissões.<br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze | [URL de seu endpoint REST][1]. Seu endpoint dependerá do URL do Braze para sua instância. |
| Identificador do app Braze | O identificador do app que receberá eventos do Amplitude. Isso pode ser encontrado em **Dashboard da Braze > Console de desenvolvedor > Configurações**. |

### Configuração da Amplitude

1. Na Amplitude, navegue até **Data Destinations** (Destinos de dados) e procure "Braze - Event Stream" (Braze – Fluxo de eventos).
2. Digite um nome de sincronização e clique em **Create Sync (Criar sincronização**).
3. Clique em **Editar** e forneça seu ponto de extremidade da API REST do Braze, a chave da API REST e o identificador do app Braze.
4. Use o filtro de eventos de envio para selecionar os eventos a serem enviados. Você pode enviar todos os eventos, mas a Amplitude recomenda escolher os mais importantes. 
5. Quando terminar, ative o destino e salve. 

Consulte [Braze Event Streaming](https://www.docs.developers.amplitude.com/data/destinations/braze/) para saber mais sobre essa integração.

## Sincronize as características e os cálculos do usuário

Use públicos para enviar propriedades e cálculos do usuário para o Braze como atributos personalizados. Você poderá sincronizar as propriedades do usuário ou as propriedades computadas dos usuários que estiveram ativos nos últimos 90 dias.

Quando a propriedade de um usuário ou um cálculo for atualizado, o Amplitude atualizará um atributo personalizado no Braze com o mesmo nome da propriedade ou do cálculo do usuário.

A característica do usuário e as sincronizações de computação criarão novos usuários para identificadores de usuário que ainda não existem no Braze. Os cálculos e as características do usuário só podem ser sincronizados usando identificadores de usuário. Um identificador de usuário pode ser qualquer um dos seguintes:
- ID externo
- ID da Braze
- Alias de usuário
- Endereço de e-mail

Consulte a documentação do Amplitude para saber mais sobre a [sincronização de propriedades, recomendações e coortes com destinos de terceiros](https://help.amplitude.com/hc/en-us/articles/360060055531).

#### Como sincronizar as propriedades e os cálculos do usuário

Nos públicos da Amplitude, selecione **Syncs > Create Sync** (Sincronizações > Criar sincronização).

![]({% image_buster /assets/img/amplitude11.png %})

Em seguida, escolha sincronizar uma propriedade, um cálculo, um coorte ou uma recomendação de usuário. 

{% tabs %}
{% tab Sincronização de propriedades do usuário %}

Selecione **User Property** (Propriedade do usuário) e, em seguida, a propriedade do usuário que deseja sincronizar.

![]({% image_buster /assets/img/amplitude7.png %})

Em seguida, selecione um destino para sincronizar a propriedade do usuário.

![]({% image_buster /assets/img/amplitude8.png %})

Por fim, defina a frequência de sua sincronização.

![Defina sua cadência como uma sincronização única ou uma sincronização programada.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab Computação de sincronização %}

Selecione **Computation** (Cálculo) e, em seguida, o cálculo que deseja sincronizar.

![]({% image_buster /assets/img/amplitude10.png %})

Em seguida, selecione um destino para sincronizar seu cálculo.

![]({% image_buster /assets/img/amplitude8.png %})

Por fim, defina a frequência de sua sincronização.

![Defina sua cadência como uma sincronização única ou uma sincronização programada.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## Pontos de extremidade da API do perfil de usuário do Amplitude

Para verificar alguns dos endpoints comuns da API do Amplitude que podem ser usados com o conteúdo conectado, consulte nossa [documentação específica da API da Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_user_profile_api/).
