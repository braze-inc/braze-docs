---
nav_title: Links profundos de navegação
article_title: Navegação por deep linking no Braze Pilot
page_order: 4
page_type: reference
description: "Este artigo de referência aborda brevemente as etapas de integração exigidas de seus engenheiros ou desenvolvedores."
---

# Links profundos de navegação no Braze Pilot

> O Braze Pilot oferece suporte a deep linking do envio de mensagens no Braze para partes específicas do aplicativo Pilot. Isso permite que você crie casos de uso de engajamento, conduzindo os usuários a várias partes do aplicativo Pilot. Também é possível usar parâmetros opcionais de deep linking para personalizar o conteúdo de determinadas páginas do app para o usuário. Para saber mais sobre deep linking, consulte [Deep linking para conteúdo in-app]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

## Geral

Esses são os deep links para as principais páginas de navegação no aplicativo Pilot. 

| Tela | Deep linking |
| --- | --- |
| Projetos | `braze-pilot://navigation/projects` |
| Dados de registro | `braze-pilot://navigation/logdata` |
| Configuração | `braze-pilot://navigation/setup` |
| Alterar idioma | `braze-pilot://navigation/selectlanguage` |
| Câmera | `braze-pilot://navigation/camera` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Steppington

Estes são os deep linkings para o app da marca fictícia Steppington na Pilot.

### Exemplo de deep linking

`braze-pilot://navigation/steppington/workout?title=Running&icon=HEART_DETAILS&image=https://picsum.photos/400&info=This%20workout%20is%20awesome%21&workout=5k%20Run&calories=600&length=25&workout_info_left_text=Road%20Run&workout_info_left_icon=RUNNING_HOME&workout_info_center_text=120%20BPM&workout_info_center_icon=HEART_DETAILS&workout_info_right_text=25%3A00&workout_info_right_icon=TIMER_DETAILS`

### Deep linking sem parâmetros

| Tela | Deep linking |
| --- | --- |
| Tela de respingo | `braze-pilot://navigation/steppington/splash` |
| Início | `braze-pilot://navigation/steppington/home` |
| Steppington+ página | `braze-pilot://navigation/steppington/plus` |
| Tela de metas | `braze-pilot://navigation/steppington/goals` |
| Tela Alterar metas | `braze-pilot://navigation/steppington/changegoals` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Deep linking com parâmetros

| Tela | Deep linking |
| --- | --- |
| Treino | `braze-pilot://navigation/steppington/workout` |
| Treino ativo | `braze-pilot://navigation/steppington/activeworkout` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Parâmetros aceitos

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 22%;
}
th:nth-child(2), td:nth-child(2) {
    width: 30%;
}
th:nth-child(3), td:nth-child(3) {
    width: 8%;
}
th:nth-child(4), td:nth-child(4) {
    width: 13%;
}
th:nth-child(5), td:nth-child(5) {
    width: 10%;
}
th:nth-child(6), td:nth-child(6) {
    width: 30%;
}
</style>

<table>
    <thead>
        <tr>
            <th>Parâmetro</th>
            <th>Descrição</th>
            <th>Obrigatória</th>
            <th>Padrão (se não for especificado)</th>
            <th>Tipo</th>
            <th>Exemplo</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>title</code></td>
            <td>O título a ser usado na parte superior da tela.</td>
            <td>Sim</td>
            <td></td>
            <td>String</td>
            <td>Executando</td>
        </tr>
        <tr>
            <td><code>icon</code></td>
            <td>Uma string que representa o ícone a ser usado.</td>
            <td>Não</td>
            <td><code>RUNNING_HOME</code></td>
            <td>String</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>O URL da imagem do item.</td>
            <td>Sim</td>
            <td></td>
            <td>String</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>info</code></td>
            <td>Informações sobre o exercício a serem colocadas sobre o botão de início do exercício.</td>
            <td>Sim</td>
            <td></td>
            <td>String</td>
            <td>This%20workout%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>workout</code></td>
            <td>O nome do exercício. Enviado no <code>st_completed_class</code> evento.</td>
            <td>Sim</td>
            <td></td>
            <td>Número</td>
            <td>5k%20Run</td>
        </tr>
        <tr>
            <td><code>calories</code></td>
            <td>O número de calorias a ser mostrado na tela do exercício ativo. Enviado no <code>st_completed_class</code> evento.</td>
            <td>Não</td>
            <td>Número aleatório entre 500 e 1.250</td>
            <td>Número</td>
            <td>600</td>
        </tr>
        <tr>
            <td><code>length</code></td>
            <td>A duração do exercício. Enviado no <code>st_completed_class</code> evento.</td>
            <td>Não</td>
            <td></td>
            <td>Número</td>
            <td>25</td>
        </tr>
        <tr>
            <td><code>workout_info_left_text</code></td>
            <td>O texto a ser usado no cartão esquerdo na tela de exercício ativa.</td>
            <td>Não</td>
            <td></td>
            <td>String</td>
            <td>Road%20Run</td>
        </tr>
        <tr>
            <td><code>workout_info_left_icon</code></td>
            <td>O ícone a ser usado no cartão esquerdo na tela de exercício ativo.</td>
            <td>Não</td>
            <td></td>
            <td>String</td>
            <td>RUNNING_HOME</td>
        </tr>
        <tr>
            <td><code>workout_info_center_text</code></td>
            <td>O texto a ser usado no cartão central na tela de exercícios ativos.</td>
            <td>Não</td>
            <td></td>
            <td>String</td>
            <td>120%20BPM</td>
        </tr>
        <tr>
            <td><code>workout_info_center_icon</code></td>
            <td>O ícone a ser usado no cartão central na tela de exercícios ativos.</td>
            <td>Não</td>
            <td></td>
            <td>String</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>workout_info_right_text</code></td>
            <td>O texto a ser usado no cartão direito na tela de exercício ativa.</td>
            <td>Não</td>
            <td></td>
            <td>String</td>
            <td>25%3A00</td>
        </tr>
        <tr>
            <td><code>workout_info_right_icon</code></td>
            <td>O ícone a ser usado no cartão direito na tela do exercício ativo.</td>
            <td>Não</td>
            <td></td>
            <td>String</td>
            <td>TIMER_DETAILS</td>
        </tr>
    </tbody>
</table>

##### Opções de ícones

| Ícone | Imagem |
| --- | --- |
| `RUNNING_HOME` | ![Um ícone dos tênis de corrida.]({% image_buster /assets/img/braze_pilot/running_home_icon.png %}){:style="max-width:30%"} |
| `HEART_DETAILS` | ![Um ícone de coração.]({% image_buster /assets/img/braze_pilot/heart_details_icon.png %}){:style="max-width:30%"} |
| `TIMER_DETAILS` | ![Um ícone de cronômetro.]({% image_buster /assets/img/braze_pilot/timer_details_icon.png %}){:style="max-width:30%"} |
| `YOGA_HOME` | ![Um ícone de uma pessoa em uma pose de ioga.]({% image_buster /assets/img/braze_pilot/yoga_home_icon.png %}){:style="max-width:30%"} |
| `BICYCLE_HOME` | ![Um ícone da bicicleta.]({% image_buster /assets/img/braze_pilot/bicycle_home_icon.png %}){:style="max-width:30%"} |
| `DUMBBELL_HOME` | ![Um ícone de haltere.]({% image_buster /assets/img/braze_pilot/dumbbell_home_icon.png %}){:style="max-width:30%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Pants Labyrinth

Estes são os deep linkings para o app da marca fictícia PantsLabyrinth na Pilot.

### Exemplo de deep linking

`braze-pilot://navigation/pantslabyrinth/itemdetails?name=Jeans&price=85&image=https://picsum.photos/400&description=This%20item%20is%20awesome%21&quantity=2&size=Large&colors=%230000FF,%23FF0000&color_strings=White,Blue&selected_color=1`

### Deep linking sem parâmetros

| Tela | Deep linking |
| --- | --- |
| Tela de respingo | `braze-pilot://navigation/pantslabyrinth/splash` |
| Tela de boas-vindas | `braze-pilot://navigation/pantslabyrinth/welcome` |
| Tela de listagem | `braze-pilot://navigation/pantslabyrinth/listing` |
| Página do carrinho | `braze-pilot://navigation/pantslabyrinth/cart` |
| Página da lista de desejos | `braze-pilot://navigation/pantslabyrinth/wishlist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Deep linking com parâmetros

| Tela | Deep linking |
| --- | --- |
| Página de detalhes do item | `braze-pilot://navigation/pantslabyrinth/itemdetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Parâmetros aceitos

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 20%;
}
th:nth-child(2), td:nth-child(2) {
    width: 30%;
}
th:nth-child(3), td:nth-child(3) {
    width: 8%;
}
th:nth-child(4), td:nth-child(4) {
    width: 13%;
}
th:nth-child(5), td:nth-child(5) {
    width: 10%;
}
th:nth-child(6), td:nth-child(6) {
    width: 30%;
}
</style>

<table>
    <thead>
        <tr>
            <th>Parâmetro</th>
            <th>Descrição</th>
            <th>Obrigatória</th>
            <th>Padrão (se não for especificado)</th>
            <th>Tipo</th>
            <th>Exemplo</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>name</code></td>
            <td>O nome do item.</td>
            <td>Sim</td>
            <td></td>
            <td>String</td>
            <td>Jeans</td>
        </tr>
        <tr>
            <td><code>price</code></td>
            <td>O preço do item.</td>
            <td>Sim</td>
            <td></td>
            <td>String</td>
            <td>85</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>O URL da imagem do item.</td>
            <td>Sim</td>
            <td></td>
            <td>String</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>description</code></td>
            <td>A descrição do item.</td>
            <td>Sim</td>
            <td></td>
            <td>String</td>
            <td>This%20item%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>quantity</code></td>
            <td>A quantidade do item.</td>
            <td>Não</td>
            <td>1</td>
            <td>Número</td>
            <td>2</td>
        </tr>
        <tr>
            <td><code>size</code></td>
            <td>Uma string que representa o tamanho do item.</td>
            <td>Não</td>
            <td>M</td>
            <td>String</td>
            <td>Grande</td>
        </tr>
        <tr>
            <td><code>colors</code></td>
            <td>Uma lista de cores hexadecimais separadas por vírgulas. Essas são as cores disponíveis para o item.</td>
            <td>Não</td>
            <td>%23000000</td>
            <td>String</td>
            <td>%230000FF,%23FF0000</td>
        </tr>
        <tr>
            <td><code>color_strings</code></td>
            <td>Uma lista das strings de cores separadas por vírgulas. Representa as cores no texto.</td>
            <td>Não</td>
            <td>Preto</td>
            <td>String</td>
            <td>Azul, vermelho</td>
        </tr>
        <tr>
            <td><code>selected_color</code></td>
            <td>O índice selecionado da cor a ser selecionada no seletor de cores quando o usuário chegar à tela. Se nenhum valor for usado, ele terá a primeira cor selecionada.</td>
            <td>Não</td>
            <td>0</td>
            <td>Número</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

## MovieCanon

Estes são os deep linkings para o app da marca fictícia Steppington na Pilot.

### Exemplo de deep linking

`braze-pilot://navigation/moviecannon/moviedetails?id=1&title=Jaws&thumbnail=https://picsum.photos/400&video=0&description=This%20video%20is%20awesome%21`

### Deep linking sem parâmetros

| Tela | Deep linking |
| --- | --- |
| Tela de respingo | `braze-pilot://navigation/moviecannon/splash` |
| Tela de boas-vindas | `braze-pilot://navigation/moviecannon/welcome` |
| Página de listagem de filmes | `braze-pilot://navigation/moviecannon/moviecannon` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Deep linking com parâmetros

| Tela | Deep linking |
| --- | --- |
| Página de detalhes do filme | `braze-pilot://navigation/moviecannon/moviedetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Parâmetros aceitos

| Parâmetro | Descrição | Obrigatória | Tipo | Exemplo |
| --- | --- | --- | --- | --- |
| `id` | A identificação do filme. | Sim | Número | 1 |
| `title` | O título do filme. | Sim | String | Tubarão |
| `thumbnail` | O URL da Web da miniatura a ser exibida antes do filme. | Sim | String | `https://picsum.photos/400` |
| `video` | O índice na lista de vídeos a serem exibidos. | Não | Número | 0 |
| `description` | A descrição do vídeo. | Sim | String | `This%20video%20is%20awesome%21` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
