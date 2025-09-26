---
nav_title: Importação de coorte de pilha
article_title: Importação de coorte de pilha
description: "Este artigo de referência detalha a integração entre o Braze e a Heap, uma plataforma de insights digitais, que permite a importação de dados da Heap para o Braze, a criação de coortes de usuários e a exportação de dados do Braze para a Heap para criar segmentos."
alias: /partners/heap_cohort_import/
page_type: partner
search_tag: Partner

---

# Importação de coorte de pilha

> O[Heap](https://heap.io/), uma plataforma de insights digitais, concentra-se nas oportunidades de sua experiência digital que mais afetam seus negócios, eliminando o atrito, encantando os clientes e acelerando a receita.

A integração entre o Braze e o Heap ativa a [importação de dados do Heap para o Braze](#data-import-integration), a criação de coortes de usuários e a [exportação de dados do Braze para o Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/) para criar segmentos.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Heap | É necessário ter uma conta [Heap](https://heap.io/about) para aproveitar essa parceria. |
| Chave de importação de dados do Braze | Isso pode ser capturado no dashboard da Braze, em **Integração com parceiros** > **Parceiros de tecnologia**. Em seguida, selecione **Heap**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância. |
| Braze Currents | Para exportar dados do Braze para o Heap, você precisará ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) ativado na sua conta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso
- Reengaje os usuários que abandonaram um funil: dispare envios de mensagens de reengajamento quando os usuários abandonarem o funil de compra ou de inscrição.
- Personalize a experiência do teste: Identifique os pontos de atrito na sua experiência de avaliação e envie lembretes com o tempo certo para reengajar os usuários durante uma avaliação e ajudá-los a obter valor.
- Aumente o engajamento em anúncios e ofertas: direcione promoções, atualizações e anúncios de novos serviços para os públicos relevantes.

## Integração de importação de dados

Use a integração Heap to Braze para sincronizar automaticamente os coortes definidos no Heap to Braze.

### Etapa 1: Obter a chave de importação de dados do Braze

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Heap**. 

Nessa página, você pode encontrar sua chave de importação de dados e um endpoint REST. Anote esses dois valores e forneça-os ao seu gerente de conta Heap para concluir a configuração da integração.

![]({% image_buster /assets/img/heap/heap2.png %}){: style="max-width:90%;"}

### Etapa 2: Segmentar usuários importados no Braze

Na Braze, navegue até **Segmentos**, dê um nome ao seu segmento da coorte da Heap e selecione **Coortes do Heap** como filtro. Aqui você pode escolher qual coorte do Heap deseja incluir. Depois que seu segmento de coorte Heap for criado, você poderá selecioná-lo como um filtro de público ao criar uma campanha ou um Canva.

![No criador de segmentos do Braze, o filtro de atribuições do usuário "Heap cohort" está definido como "includes" e "Heap Test Cohort".]({% image_buster /assets/img/heap/heap1.png %}){: style="max-width:90%;"}

### Usando essa integração

Para usar seu segmento do Heap, crie uma campanha da Braze ou um canva e selecione o segmento como seu público-alvo.

![No criador de campanhas do Braze, na etapa de direcionamento, o filtro "Target users by segment" está definido como "Heap cohort".]({% image_buster /assets/img/heap/heap3.png %}){: style="max-width:90%;"}

{% alert important %}
Somente os usuários que já existem no Braze serão adicionados ou removidos de um coorte. A importação de coorte não criará novos usuários no Braze.
{% endalert %}

## Detalhes da integração

A estrutura de carga útil para dados exportados é a mesma que a estrutura de carga útil para conectores HTTP personalizados, que pode ser visualizada no [repositório de exemplos para conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).

## Correspondência de usuários

Os usuários identificados podem ser combinados pelo endereço `external_id` ou `alias`. Os usuários anônimos podem ser combinados pelo site `device_id`. Os usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo endereço `device_id` e devem ser identificados pelo endereço `external_id` ou `alias`.

