---
nav_title: Monitoramento de localização
article_title: Monitoramento de localização
page_order: 0
page_type: reference
description: "Este artigo de referência explica como usar o monitoramento de localização e o direcionamento de localização em seus apps e quais parceiros oferecem suporte ao rastreamento de localização."
tool: Location
search_rank: 2
---

# monitoramento de localização

> A coleta de local captura o local mais recente do usuário quando o app foi aberto usando dados de localização GPS. É possível usar essas informações para segmentar dados com base nos usuários que estavam em um local definido.

## Ativação do monitoramento de localização

Para ativar a coleta de locais em seu app, consulte o guia do desenvolvedor da plataforma que está usando:

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=web)

Em geral, os apps móveis usam o chip GPS do dispositivo e outros sistemas (como o monitoramento de localização por Wi-Fi) para rastrear o local do usuário. Os apps da Web usarão o WPS (Wi-Fi Positioning System) para rastrear os locais do usuário. Todas essas plataformas exigirão que os usuários aceitem o monitoramento de localização. A precisão dos seus dados de monitoramento de localização pode ser afetada pelo fato de os usuários terem ou não o Wi-Fi ativado em seus dispositivos. Os usuários de Android também podem escolher diferentes modos de local - os usuários que estão no modo "Economia de bateria" ou "Somente dispositivo" podem ter dados imprecisos.

### Local do usuário do SDK por endereço IP

A partir de 26 de novembro de 2024, o Braze detectará os locais dos usuários do país geolocalizado usando o endereço IP do início da primeira sessão do SDK. 

Antes disso, o Braze usava o código do país da localização do dispositivo durante a criação do usuário do SDK e na duração da primeira sessão. Somente após o processamento do início da primeira sessão, o endereço IP seria usado para definir o país mais confiável do usuário. Isso significa que o país do usuário foi definido com maior precisão apenas a partir da segunda sessão, somente depois que o início da primeira sessão foi processado.

Agora, o Braze usará o endereço IP para definir o valor do país nos perfis de usuário criados por meio do SDK, e essa configuração de país baseada em IP estará disponível durante e após a primeira sessão.

## Direcionamento do local

Usando dados e segmentos de monitoramento de localização, é possível configurar campanhas e estratégias baseadas no local. Por exemplo, talvez você queira executar uma campanha promocional para usuários que moram em uma determinada região ou excluir usuários de uma região com regulamentos mais rígidos.

Consulte [Direcionamento de local]({{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/) para obter mais informações sobre como criar um segmento de local.

## Definição da atribuição do local padrão

Você também pode usar o [endpoint`users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) em nossa API para atualizar o [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object/) atribuição padrão. Um exemplo é:

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

A combinação do suporte a beacon ou geofence existente com nossos recursos de direcionamento e envio de mensagens fornece mais informações sobre as ações físicas dos usuários para que você possa enviar mensagens de acordo com elas. Você pode aproveitar o monitoramento de localização com alguns de nossos parceiros: 

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

## Perguntas frequentes

### Quando o Braze coleta dados de local?

A Braze só coleta o local quando o aplicativo está aberto em primeiro plano. Como resultado, nosso filtro `Most Recent Location` direciona os usuários com base no local em que eles abriram o aplicativo pela última vez (também chamado de início da sessão).

Você também deve ter em mente as seguintes nuances:

- Se a localização estiver desativada, o filtro `Most Recent Location` mostrará o último local registrado.
- Se um usuário já teve um local armazenado em seu perfil, ele se qualificará para o filtro `Location Available`, mesmo que tenha feito a aceitação do monitoramento de localização desde então.

### Qual é a diferença entre os filtros Localidade mais recente do dispositivo e Local mais recente?

O `Most Recent Device Locale` vem das configurações do dispositivo do usuário. Por exemplo, para os usuários do iPhone, isso aparece no dispositivo em **Settings** > **General** > **Language & Region**. Esse filtro é usado para capturar a formatação regional e de idioma, como datas e endereços, e é independente do filtro `Most Recent Location`.

O endereço `Most Recent Location` é o último local GPS conhecido do dispositivo. Isso é atualizado no início da sessão e é armazenado no perfil do usuário.

### Se um usuário aceitar o monitoramento de localização, seus dados de localização antigos serão removidos da Braze?

Não. Se um usuário já teve um local armazenado em seu perfil, esses dados não serão removidos automaticamente se ele aceitar o monitoramento de localização posteriormente.

