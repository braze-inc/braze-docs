---
nav_title: Rastreamento de localização
article_title: Rastreamento de localização
page_order: 0
page_type: reference
description: "Este artigo de referência explica como usar o rastreamento de localização e a segmentação por localização em seus aplicativos e quais parceiros oferecem suporte ao rastreamento de localização."
tool: Location
search_rank: 2
---

# Rastreamento de localização

> A coleta de localização captura a localização mais recente de um usuário quando o aplicativo foi aberto usando dados de localização GPS. Você pode usar essas informações para segmentar dados com base nos usuários que estavam em um local definido.

## Ativação do rastreamento de localização

Para ativar a coleta de localização em seu aplicativo, consulte o guia do desenvolvedor da plataforma que você está usando:

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=web)

Em geral, os aplicativos móveis usarão o chip de GPS do dispositivo e outros sistemas (como o escaneamento de Wi-Fi) para rastrear a localização do usuário. Os aplicativos da Web usarão o WPS (Wi-Fi Positioning System) para rastrear a localização do usuário. Todas essas plataformas exigirão que os usuários aceitem o rastreamento de localização. A precisão dos seus dados de rastreamento de localização pode ser afetada pelo fato de os usuários terem ou não o Wi-Fi ativado em seus dispositivos. Os usuários do Android também podem escolher diferentes modos de localização - os usuários que estão no modo "Economia de bateria" ou "Somente dispositivo" podem ter dados imprecisos.

### Localização do usuário do SDK por endereço IP

A partir de 26 de novembro de 2024, o Braze detectará as localizações dos usuários do país geolocalizado usando o endereço IP do início da primeira sessão do SDK. 

Antes disso, o Braze usava o código do país da localidade do dispositivo durante a criação do usuário do SDK e a duração da primeira sessão. Somente após o processamento do início da primeira sessão, o endereço IP seria usado para definir o país mais confiável do usuário. Isso significa que o país do usuário foi definido com maior precisão apenas a partir da segunda sessão, somente depois que o início da primeira sessão foi processado.

Agora, o Braze usará o endereço IP para definir o valor do país nos perfis de usuário criados por meio do SDK, e essa configuração de país baseada em IP estará disponível durante e após a primeira sessão.

## Direcionamento de localização

Usando dados e segmentos de rastreamento de localização, você pode configurar campanhas e estratégias baseadas em localização. Por exemplo, você pode querer executar uma campanha promocional para usuários que moram em uma determinada região ou excluir usuários de uma região que tenha regulamentações mais rígidas.

Consulte [Segmentação por local]({{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/) para obter mais informações sobre como criar um segmento de local.

## Definição difícil do atributo de local padrão

Você também pode usar o [ponto de extremidade`users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) em nossa API para atualizar o atributo [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object/) atributo padrão. Um exemplo é:

```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [ 
 	{
 	  "external_id" : "XXX",
 	  "current_location" : {"longitude":-0.118092, "latitude": 51.509865}
      }
   ]
}
```

## Suporte de parceria para beacon e geofence

A combinação do suporte a beacon ou geofence existente com nossos recursos de segmentação e mensagens fornece mais informações sobre as ações físicas dos usuários para que você possa enviar mensagens de acordo com elas. Você pode aproveitar o rastreamento de localização com alguns de nossos parceiros: 

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infilhão]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

## Perguntas frequentes

### Quando o Braze coleta dados de localização?

O Braze só coleta a localização quando o aplicativo está aberto em primeiro plano. Como resultado, nosso filtro `Most Recent Location` tem como alvo os usuários com base no local em que eles abriram o aplicativo pela última vez (também conhecido como início da sessão).

Você também deve ter em mente as seguintes nuances:

- Se a localização estiver desativada, o filtro `Most Recent Location` mostrará a última localização registrada.
- Se um usuário já teve uma localização armazenada em seu perfil, ele se qualificará para o filtro `Location Available`, mesmo que tenha optado por não rastrear a localização desde então.

### Qual é a diferença entre os filtros Most Recent Device Locale e Most Recent Location?

O `Most Recent Device Locale` vem das configurações do dispositivo do usuário. Por exemplo, para os usuários do iPhone, isso aparece no dispositivo em **Ajustes** > **Geral** > **Idioma & Região**. Esse filtro é usado para capturar a formatação regional e de idioma, como datas e endereços, e é independente do filtro `Most Recent Location`.

O endereço `Most Recent Location` é a última localização GPS conhecida do dispositivo. Isso é atualizado no início da sessão e é armazenado no perfil do usuário.

### Se um usuário optar por sair do rastreamento de localização, seus dados de localização antigos serão removidos do Braze?

Não. Se um usuário já teve uma localização armazenada em seu perfil, esses dados não serão removidos automaticamente se ele optar por desativar o rastreamento de localização posteriormente.

