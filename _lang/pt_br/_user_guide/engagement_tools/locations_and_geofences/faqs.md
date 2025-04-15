---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre locais e geofences
page_order: 4
page_type: FAQ
description: "Este artigo de referência aborda algumas perguntas frequentes sobre o uso de monitoramento de localização e geofences."
tool: Location

---

# Perguntas frequentes

> Esta página fornece respostas a perguntas frequentes sobre locais e geofences.

## monitoramento de localização

### Quando o Braze coleta dados de local?

A Braze só coleta o local quando o aplicativo está aberto em primeiro plano. Como resultado, nosso filtro `Most Recent Location` direciona os usuários com base no local em que eles abriram o aplicativo pela última vez (também chamado de início da sessão).

Você também deve ter em mente as seguintes nuances:

- Se a localização estiver desativada, o filtro `Most Recent Location` mostrará o último local registrado.
- Se um usuário já teve um local armazenado em seu perfil, ele se qualificará para o filtro `Location Available`, mesmo que tenha feito a aceitação do monitoramento de localização desde então.

### Qual é a diferença entre os filtros Localidade mais recente do dispositivo e Local mais recente?

O `Most Recent Device Locale` vem das configurações do dispositivo do usuário. Por exemplo, para os usuários do iPhone, isso aparece no dispositivo em **Settings** > **General** > **Language & Region**. Esse filtro é usado para capturar a formatação regional e de idioma, como datas e endereços, e é independente do filtro `Most Recent Location`.

O endereço `Most Recent Location` é o último local GPS conhecido do dispositivo. Isso é atualizado no início da sessão e é armazenado no perfil do usuário.

### Se um usuário aceitar o monitoramento de localização, seus dados de localização antigos serão removidos da Braze?

Não! Se um usuário já teve um local armazenado em seu perfil, esses dados não serão removidos automaticamente se ele aceitar o monitoramento de localização posteriormente.

## Geofences

### Qual é a diferença entre geofences e monitoramento de localização?

Na Braze, uma geofence é um conceito diferente do monitoramento de localização. Os geofences são usados como disparadores para determinadas ações. Um geofence é um limite virtual estabelecido em um local geográfico. Quando um usuário entra ou sai desse limite, ele pode disparar uma ação específica, como o envio de uma mensagem.

O monitoramento de localização é usado para coletar e armazenar os dados de localização mais recentes de um usuário. Esses dados podem ser usados para segmentar usuários com base no filtro `Most Recent Location`. Por exemplo, é possível usar o filtro `Most Recent Location` para direcionamento a uma região específica do seu público, como o envio de mensagens a usuários localizados em Nova York.

### Qual é a precisão das geofences do Braze?

As geofences do Braze usam uma combinação de todos os provedores de localização disponíveis em um dispositivo para triangular a localização do usuário. Isso inclui Wi-Fi, GPS e torres de celular.

A precisão típica está na faixa de 20 a 50 m e a melhor precisão será na faixa de 5 a 10 m. Em áreas rurais, a precisão pode se degradar significativamente, podendo chegar a vários quilômetros. Braze recomenda a criação de geofences com raios maiores em locais rurais.

Para saber mais sobre a precisão das geofences, consulte a documentação do [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing) e do [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW1).

### Como o geofences afeta a duração da bateria?

Nossa solução de geofencing usa o serviço de sistema de geofence nativo no iOS e no Android e é ajustada para negociar de forma inteligente a precisão e a energia, garantindo a melhor duração de bateria da categoria e melhorias no desempenho à medida que o serviço subjacente é aprimorado.

### Quando as geofences estão ativas?

As geofences da Braze funcionam em todas as horas do dia, mesmo quando seu app está fechado. Eles se tornam ativos assim que são definidos e feitos upload no dashboard da Braze. No entanto, as geofences não podem funcionar se um usuário tiver desativado o monitoramento de localização.

Para que as geofences funcionem, os usuários devem ter os serviços de localização ativados no dispositivo e devem ter concedido permissão ao app para acessar o local. Se um usuário tiver desativado o monitoramento de localização, seu app não conseguirá detectar quando ele entrar ou sair de uma geofence.

### Os dados de geofence são armazenados nos perfis de usuários?

Não, a Braze não armazena dados de geofence nos perfis de usuários. As geofences são monitoradas pelos serviços de local da Apple e do Google, e o Braze só é notificado quando um usuário dispara uma geofence. Nesse ponto, processamos todas as campanhas de disparo associadas.

### Posso configurar uma geofence dentro de uma geofence?

Como prática recomendada, evite configurar geofences entre si, pois isso pode causar problemas com o disparo de notificações.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
