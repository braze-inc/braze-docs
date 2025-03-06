---
nav_title: Parceiros disponíveis
article_title: Parceiros Currents disponíveis
page_order: 2
page_type: reference
description: "Este artigo de referência descreve os parceiros de dados que você pode usar para se integrar ao Braze Currents e seus casos de uso."
tool: Currents

---

# Parceiros disponíveis

> Esta página lista os parceiros de dados com os quais você pode se integrar ao Braze Currents e descreve seus casos de uso. 

{% alert note %}
As convenções de nomes para eventos que fluem para um parceiro do Braze podem não corresponder a outros parceiros. Por exemplo, o evento de abertura de e-mail Currents no Segment é `Email Opened`, enquanto no Mixpanel é `Email Open`.
{% endalert %}

## Armazenamento de data warehouse
[![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/introduction-to-data-warehouses){: style="float:right;width:120px;border:0;" class="noimgborder"}
O armazenamento de data warehouse oferece uma fonte de coleta para todas as informações enviadas pelo Currents. Esses parceiros podem atuar como armazéns (para armazenamento de arquivos simples) ou ser usados para alimentar ferramentas de business intelligence, algoritmos de machine learning, obter insights sobre o desempenho do marketing e muito mais.

* [Amazon S3][1]
* [Google Cloud Storage][2]
* [Armazenamento de Blob do Microsoft Azure][3]

Estamos tão confiantes no poder do Currents e dos data warehouses juntos que [nós mesmos os usamos]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/)!

## Dados de cliente

Essas plataformas de dados do cliente coletam e encaminham informações de várias fontes para uma variedade de outros locais para capacitá-lo a utilizar os dados do Braze da melhor maneira possível.

* [mParticle][6]
* [Segmento][7]
* [Tealium][8]
* [Treasure Data][10]
* [RudderStack][9]
* [Adobe][12]

## Análise de dados comportamentais

Esses parceiros são especializados em análise de dados de produtos e business intelligence e podem ajudá-lo a interagir com seus usuários com base em suas ações.

* [Amplitude][4]

* [Mixpanel][5]

* [Heap][11]



[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/google_cloud_storage_for_currents/
[3]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/microsoft_azure_blob_storage_for_currents/
[4]: {{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/
[5]: {{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/
[6]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/
[7]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/
[8]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents#tealium-for-currents
[9]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack_for_currents/
[10]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/treasure_data/treasure_data_for_currents/
[11]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/
[12]: {{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/adobe_for_currents/