---
nav_title: Braze Docs スタイルガイド
article_title: Braze Docs スタイルガイド
description: "Braze Docs のライティングスタイルガイドです。"
page_order: 0
noindex: true
---

# Braze Docs スタイルガイド

## ライティングスタイルガイド

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

### 一般的なガイドライン {#general-guidelines}

#### ボイスとトーン {#voice-and-tone}

Braze のブランドボイスは、スマートで、会話的で、率直です。テクノロジーのバズワードが飛び交う世界において、私たちは人間の声を届けます。カスタマーエンゲージメントに関心のあるすべての人に明確さとガイダンスを提供し、専門用語を避けて、わかりやすく力強い簡潔な言葉を使います。

ライティングと編集においてこのブランドボイスを統一するために、3つのボイスガイドラインを使用します。**わかりやすく、力を与え、**そして**人間らしく**。

##### わかりやすく

文章を明確に構成し、読者が必要な情報を見つけやすくします。

* 複雑なことをシンプルに説明します。
* 簡潔にします。
* 機能やアクションには一貫した言葉を使います。

###### ガイドライン

✅ ビジュアルを使って複雑なテーマをわかりやすくします。<br>
**例:** [ユーザープロファイルのライフサイクルの記事]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)にあるユーザープロファイルのライフサイクル画像は、難しい概念をわかりやすく説明するのに役立ちます。

✅ 明確な情報の階層構造を作ります。<br>
**例:** 「これは Braze Docs でコンテンツがどのように管理されるかの概要です。特定のトピックについて詳しく知りたい場合は、ナビゲーションから専用のトピックページを選択してください。」

✅ 可能であれば、専門用語や略語を徹底的に排除します。排除できない場合は、定義を記載します。<br>
**例:** 「Short Messaging Service (SMS) は、短いテキストメッセージの送受信に使用されます。」

##### 力を与える

ライティングで解決しようとしている問題は何ですか？コンテンツを作成する際は、常にその問題を念頭に置いてください。

* 「なぜ」と「どのように」を説明し、ユーザーが自信を持ってアクションを起こせるようにします。
* メリットを説明する際は具体的にし、何ができて何ができないかを明確にします。
* 実用的なアドバイスと誠実な励ましを提供します。

###### ガイドライン

✅ ハッピーパスを見つけやすくします。<br>
**例:** 「Canvas を停止すると、以下が適用されます。1. ユーザーは Canvas に入れなくなります。2. フロー内のどこにいるかに関係なく、それ以上のメッセージは送信されません。3. **例外:** メールの Canvas はすぐには停止しません。」

✅ ユーザーの作業を簡素化または向上させる例、ユースケース、テンプレートを提供します。<br>
**例:** 「`IInAppMessageManagerListener` には、メッセージ自体またはボタンのいずれかのクリックに対するデリゲートメソッドも含まれています。一般的なユースケースは、ボタンまたはメッセージがクリックされたときにメッセージをインターセプトして、さらに処理を行うことです。」

##### 人間らしく

情報提供のためのライティングは本質的に無味乾燥になりがちです。読者にはコンテンツに集中してほしいのであって、伝え方に注目してほしいわけではありません。それでも、読者が消費している情報を処理しやすく、知識を内面化しやすいように書くことはできます。人間らしく、個性を出し、記憶に残るようにしましょう。

* フォーマルなトーンではなく、会話的なトーンを目指します。
* ユーザーに焦点を当て、その状況や感情の状態を尊重します。
* マシンの状態ではなく、人間の体験を積極的に中心に据えます。

###### ガイドライン

✅ ブランドのトーンとアセットを思慮深く適用します。<br>
**例:** 「Braze との統合は価値のあるプロセスです。でも、あなたは賢い方です。ここにいるのですから。明らかに、それはもうご存知ですよね。」

✅ ビジュアルコンテンツと言語コンテンツの両方に[アクセシビリティのベストプラクティス](#accessibility)を適用します。<br>
**例:** 「out-of-the-box」のような慣用句を「default」に置き換えると、英語を第二言語とする方にとってテキストがよりアクセシブルになります。

✅ ユーザージャーニー全体を通じて一貫したサポートを提供します。<br>
**例:** Diátaxis フレームワークを使用して、さまざまなタイミングでさまざまなユーザーのニーズに応えていることを確認します。

#### アクセシビリティ {#accessibility}

Braze はインクルーシブな体験の提供を目指しています。以下のガイドラインを使用して、アクセシビリティのニーズを持つ[10億人](https://www.who.int/en/news-room/fact-sheets/detail/disability-and-health)の方々が学習コンテンツにアクセスできるようにしてください。

##### 全般

* 偏見のある言葉や差別的な言葉を避けます。詳しくは、[インクルーシブな言葉遣い](#inclusive-language)のセクションを参照してください。
* [スクリーンリーダー](https://support.apple.com/guide/mac-help/use-accessibility-features-mh35884/mac)を使用してコンテンツをテストします。
* UI 要素でアンパサンドが使用されている場合を除き、「and」の代わりに[アンパサンド](#ampersands) (&) を使用しないでください。

##### 言語とフォーマット

* [プレーンランゲージ](https://www.plainlanguage.gov/guidelines/)を使用します。
* セクションの冒頭に最も重要な情報を配置します。ジャーナリズムの[逆ピラミッド](https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism))モデルを使用します。
* テキストの壁を分割して、読者が情報をスキャンしやすくします。段落、[リスト](#lists)、[コールアウト](#callouts-and-alerts)、[画像](#figures-and-other-images)を使用して読みやすさを向上させます。
* [短い文と段落を書きます](https://www.usability.gov/how-to-and-tools/methods/writing-for-the-web.html)。一般的なルールとして、1文あたり20語以内、1段落あたり5文以内を目指します。
* ラテン語の略語やフレーズは翻訳が難しいため、使用を避けます。代わりに、シンプルな単語やフレーズを使用します。

##### 見出し

* ユニークで、説明的で、明確な[見出しとタイトル](#headings-and-titles)を使用します。
* ページタイトルには h1 を使用します。
* 見出しレベルをスキップしないでください。h3 は h2 の後に続く必要があります。

##### リンク

* 「詳しくはこちら」、「ここ」、「このドキュメント」のようなリンクテキストを使用しないでください。避けるべきフレーズについては、[リンクの書き方](#writing-links)のセクションを参照してください。
* 文中で2つのリンクを連続して配置することを避けます。リンクの間に文字や単語を入れて区切ります。
* [ファイルダウンロード用のリンク](#links-for-file-download)は、リンクをクリックするとファイルがダウンロードされることと、ファイルタイプ（PDF、CSV など）を示す必要があります。
* コンテキストから明確でない場合、同じドキュメント内のセクションへのリンクには、そのアクションを示す[標準的なフレーズ](#structuring-links)を使用する必要があります。

##### 画像、動画、GIF

* 画像に表示されている情報を要約する[代替テキスト](#alt-text)をすべての画像に提供します。
* 情報を表示する唯一の方法として画像を使用しないでください。画像に表示されている手順、コンテンツ、その他の詳細は、常に周囲のテキストでも提供します。
* ターミナル出力、コードサンプル、テキストの画像を使用しないでください。代わりに、実際のテキストを使用します。
* 動画コンテンツにはキャプションを提供します。
* 動画や GIF で点滅する要素を使用しないでください。

##### テーブル {#tables-1}

* テーブルの目的を説明する導入文を必ず使用します。
* リスト、特に手順リストの途中にテーブルを配置することを避けます。

#### グローバルオーディエンス {#global-audience}

学習コンテンツはアメリカ英語で書きます。ただし、Braze はグローバルブランドであるため、グローバルオーディエンスに向けて書きます。英語が母国語でない顧客にもライティングが理解されるように、以下のガイドラインを使用してください。

1. **ローカライゼーションを念頭に置いて書きます：**
  * [日付と時刻](#dates-and-times)を曖昧でない形式でフォーマットします。
  * 画像にテキストオーバーレイを配置しないでください。このテキストは翻訳できません。
  * [スラングや慣用句](#slang-and-idioms)を避けます。
  * コンテキストを提供します。読者があなたの話していることを知っていると仮定しないでください。
2. **短く正確な文を書きます：**
  * [プレーンランゲージ](https://www.plainlanguage.gov/guidelines/)を使用します。
  * [略語](#abbreviations)を定義します。
  * [曖昧な代名詞](#ambiguous-pronouns)を避けます。代名詞が曖昧になる可能性がある場合は、適切な名詞に置き換えます。
3. **一貫性を保ちます：**
  * 概念に対して、大文字・小文字やテキストフォーマットを含め、すべての言及で同じ用語を使用します。
  * 主語 + 動詞 + 目的語の語順で文を書きます。
  * 指示が条件の充足に依存する場合は、条件節を先に配置します。詳しくは、[節の順序](#clause-order)を参照してください。
4. **インクルーシブにします：**
  * [インクルーシブな言葉遣い](#inclusive-language)を使用します。
  * 多様な[例の名前](#example-names)を使用します。
  * 文化固有のユーモアを避けます。

#### インクルーシブな言葉遣い {#inclusive-language}

私たちは B2B 企業かもしれませんが、私たちの活動の中心には人がいます。そして私たちはグローバルブランドです。コンテンツで人に言及する際は、常にインクルーシブで思いやりのある表現を心がけます。迷った場合は、このセクションまたは [The Diversity Style Guide](https://www.diversitystyleguide.com/) を参照してください。

##### 年齢

ライティングに関連がない限り、対象者の年齢に言及しないでください。対象者やオーディエンスを説明するために「若い」や「年配の」などの修飾語を使用しないでください。

年齢層を表す場合は、「youth」の代わりに「Generation Z」のように、説明的かつ具体的にします。「college-age」のような曖昧な表現ではなく、「college students」と言えるときはそちらを使用してください。

##### 色

絶対に必要な場合を除き、ライティングに色の用語を含めることを避けます。必要な場合は、説明テキストを含めてください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">✅ **Save** を押します。</td><td style="width: 50%;">緑色の Save アイコンを押します。</td></tr>
<tr><td style="width: 50%;">緑色のチェックマークアイコンを押します。</td><td style="width: 50%;">赤い Cancel ボタンの横にある緑色のアイコンを押します。</td></tr>
<tr><td style="width: 50%;">緑色のアイコンを押します。</td><td style="width: 50%;"></td></tr>
</tbody>
</table>
{:/}

インタラクティブ要素の唯一のインジケーターとして色に依存しないでください。たとえば、ホバー時にリンクに下線を引いたり、必須フィールドにアスタリスクを付けたりします。

「良い」と「悪い」（または、より一般的には「推奨」と「非推奨」）のインジケーターとして緑と赤だけに依存することを避けます。赤/緑の色覚異常は最も一般的なタイプの色覚異常です。推奨と非推奨を伝えるために色を使用する場合は、同じポイントを伝えるための他のテキストやシンボルも必ず含めてください。

##### 見下すような言葉遣い {#condescending-language}

読者が従うべき指示や手順を書く際は、以下のような単語やフレーズの使用を避けてください：

* simple（「キャンペーンの作成は simple です。」のように）
* simply（「...simply X を Y に追加します」のように）
* just（「...just X をインストールします」のように）
* 「It's easy」

手順や指示に困難を感じている人にとって、あなたのカジュアルな表現は見下しているように感じられる可能性があります。また、自分にはスキルが足りないと解釈する人をドキュメントから意図せず排除してしまう可能性もあります。

##### 顧客とクライアント

企業ユーザーとその消費者に言及する際は、以下の用語を適切に使用してください：

* **Customers（顧客）：** 私たちが協力するブランドです。顧客を「clients」と呼ばないでください。
 * **Company users（企業ユーザー）：** ドキュメントのコンテキストで、プラットフォームのユーザーとマーケティングメッセージを受け取るエンドユーザーを区別することが重要な場合は、「company users」を使用します。
* **Consumers（消費者）：** 私たちが協力するブランドの顧客です。
* **Users（ユーザー）：** 一般的に、「user」メトリクスに依存する特定の統計（「user retention」など）に使用されます。コンテンツで「users」に言及する際は、まずより具体的にすることを目指します。shoppers、consumers、patients、players などを考えてください。

##### 部門とチーム

部門やチームの名前は大文字にします。「team」や「department」は大文字にしないでください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Marketing, Business Intelligence Product team</td><td style="width: 50%;">marketing, business intelligence Product Team</td></tr>
<tr><td style="width: 50%;">Revenue department</td><td style="width: 50%;">Revenue Department</td></tr>
</tbody>
</table>
{:/}

##### 障害

ライティングに特に関連がない限り、人の障害に言及しないでください。言及する場合は、思いやりを持ち、対象者がアイデンティティファーストまたはパーソンファーストの言葉遣いのどちらを好むか確認してください。障害のある対象者に言及する際は、「handicapped」のような用語を使用しないでください。

差別的な言葉遣いには、「crazy」、「insane」、「blind to」または「blind eye to」、「cripple」、「dumb」などの単語やフレーズが含まれます。コンテキストに応じて代替の単語を選択してください。

##### 病気

病気を説明する際は、「suffer」、「struggle」、「victim」のような言葉を避けます。中立的で事実に基づいた表現を目指します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">She was diagnosed with cancer.</td></tr>
<tr><td style="width: 100%;">They're living with HIV.</td></tr>
<tr><td style="width: 100%;">He recovered from his stroke.</td></tr>
</tbody>
</table>
{:/}


##### コンテンツにおけるインクルーシビティ

多様なコミュニティを強調し、代表します。顧客、スピーカー、業界の専門家、Braze チームメンバーを含める際は、思いやりを持ちインクルーシブにしてください。

##### 役職

役職に関しては、AP スタイルから外れます。すべてのケースで、特定の人物に言及する際は役職を大文字にします。

###### 会社名付きの役職

正式な役職が人名の前後に来る場合は大文字にします。3つの形式でフォーマットします：

1. **[正式な役職]** at **[会社名]** + **[フルネーム]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Creative Director at PantsLabyrinth David Bowie</td><td style="width: 50%;">creative director at PantsLabyrinth David Bowie</td></tr>
</tbody>
</table>
{:/}

{: start="2"}
2. **[フルネーム]** + コンマ + **[正式な役職]** at **[会社名]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">David Bowie, Creative Director at PantsLabyrinth</td><td style="width: 50%;">David Bowie, creative director at PantsLabyrinth</td></tr>
</tbody>
</table>
{:/}

{: start="3"}
3. **[会社名]** + **[正式な役職]** + **[フルネーム]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">PantsLabyrinth Creative Director David Bowie</td><td style="width: 50%;">PantsLabyrinth creative director David Bowie</td></tr>
</tbody>
</table>
{:/}

###### 会社名なしの役職

正式な役職で特定の人物に言及する場合は、正式な役職と名前を以下のように大文字にします：

1. **[正式な役職]** + **[フルネーム]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">CEO Robin Fenty</td><td style="width: 50%;">Chief executive officer Robyn Fenty</td></tr>
</tbody>
</table>
{:/}

{: start="2"}
2. **[正式な役職]** + コンマ + **[フルネーム]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">SVP, Product, Robin Fenty</td><td style="width: 50%;">senior vice president, product, Robyn Fenty</td></tr>
</tbody>
</table>
{:/}

###### その他

正式な役職は「at [会社名]」です。Founder と Cofounder は「of [会社名]」です。正式な役職や職業が単独で使用される場合は、大文字にする必要はありません。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">I wrote to their chief data officer.</td><td style="width: 50%;">I wrote to their Chief Data Officer</td></tr>
<tr><td style="width: 50%;">We spoke with several business intelligence analysts.</td><td style="width: 50%;">We spoke with several Business Intelligence Analysts.</td></tr>
<tr><td style="width: 50%;">Contact your Braze account manager.</td><td style="width: 50%;">I wrote to their Chief Data Officer Contact your Braze Account Manager.</td></tr>
</tbody>
</table>
{:/}

性別が既に確立されていない限り、ジェンダーニュートラルな役職を使用してください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">salesperson</td><td style="width: 50%;">salesman/saleswoman</td></tr>
</tbody>
</table>
{:/}

本人がそのように自分の役職を呼んでいる場合は、VP や SVP のように適切に略します。テキストスペースが限られている場合は、標準的な略語（VP、SVP、Sr.、Jr.）が許容されます。

##### ジェンダー

人のジェンダーについて仮定しないでください。コンテンツに登場する対象者に、どのように自認しているか確認してください。

コミュニティのメンバーに言及する際、「queer」は許容されます。「Gay」は許容されません。人々のグループを「LGBTQ」と呼ぶことができます。個人を表すためにこれを使用しないでください。

コンテンツでグループの人々に呼びかける際は、オーディエンスにジェンダーを付けることを避けてください（例：「OK, ladies!」）。代わりにジェンダーニュートラルな表現を使用してください（例：「Let's dig in, everyone!」）。

「They/them/theirs」は、すべてのコンテンツで単数または複数の代名詞として常に使用できます。

##### メンタルヘルス

メンタルヘルスと精神疾患は幅広い状態をカバーします。ライティングに関連がない限り、人のメンタルヘルスに言及しないでください。スティグマを助長する言葉やフレーズを避けます。医学用語を口語的に使用しないでください（例：「The depressing state of things...」）。

##### 名前

人物に初めて言及する際は、ファーストネームとフルネームを使用します。それ以降は、ファーストネームまたはラストネームのいずれかを使用して言及します。

##### 代名詞

代名詞の適切な使用については、言語と文法セクションの[代名詞](#pronouns)を参照してください。

##### 人種、宗教、民族

ライティングに関連がない限り、人の人種、宗教、民族に言及しないでください。人種や民族が関係するライティングでは、対象者にどのように自認しているか確認してください。

二重の遺産や宗教を示すためにハイフンを使用しないでください。代わりにスペースを使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Muslim American</td><td style="width: 50%;">Muslim-American</td></tr>
<tr><td style="width: 50%;">Cuban American</td><td style="width: 50%;">Cuban-american</td></tr>
</tbody>
</table>
{:/}

民族、国籍、民族集団、部族の固有名詞は大文字にします。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Cambodian</td><td style="width: 50%;">cambodian</td></tr>
<tr><td style="width: 50%;">Black Americans</td><td style="width: 50%;">black Americans</td></tr>
</tbody>
</table>
{:/}

宗教や宗教用語の名前は大文字にします。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Bahá'í Faith</td><td style="width: 50%;">bahá'í faith</td></tr>
<tr><td style="width: 50%;">Buddhist</td><td style="width: 50%;">buddhist</td></tr>
</tbody>
</table>
{:/}

African American Vernacular English に属する言葉やフレーズを流用しないでください（on fleek、bae、lit、woke）。

先住民族に固有の言葉やフレーズを流用しないでください（例：spirit animal、powwow）。

#### サードパーティのソース {#third-party-sources}

著作権を侵害する可能性があるため、他のサイトからコンテンツをコピーしないでください。コンテンツにはテキストと画像の両方が含まれます。

サードパーティのサイトをコピーまたは引用する代わりに、コンテンツを言い換えるか、詳細についてサードパーティのサイトへのリンクを提供してください。詳しくは、[他のサイトへのリンク](#links-to-other-sites)を参照してください。

### 言語と文法 {#language-and-grammar}

合意された文法と表記法に従うことで、ライティングを明確で一貫性のあるものに保つことができます。このセクションでは、特に指定がない限り、テクニカルドキュメントで従うべき内容を説明します。

#### 略語 {#abbreviations}

頭字語、イニシャリズム、短縮語などの略語は、明確さ、ボイス、SEO を損なう可能性があります。

一部の略語は広く理解されていますが、あまり知られていないものや、特定の顧客グループにのみ馴染みのあるものもあります。最善の判断を使用し、一般的なルールとして、[American Heritage Dictionary](https://ahdictionary.com/) に掲載されている略語であれば、展開しなくても問題ありません。

略語がよく知られていない場合は、最初の言及時に展開し、その後にかっこで略語を記載します。以降のすべての言及では、略語を使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>一般的でない略語は最初の言及時に展開する</em></th><th style="width: 50%;">非推奨：<em>一般的な略語を展開する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Top-level domain (TLD)</td><td style="width: 50%;">Portable Document Format (PDF)</td></tr>
<tr><td style="width: 50%;">Universally unique identifier (UUID)</td><td style="width: 50%;">Universal Serial Bus (USB)</td></tr>
</tbody>
</table>
{:/}


略語を複数形にする際は通常の単語と同様に扱い、アポストロフィを付けないでください。たとえば、APIs や SDKs のようにします。冠詞（a または an）の使い分けも同様で、略語の発音を確認してください。略語が母音の音で始まる場合は「an」を使用し、子音の音で始まる場合は「a」を使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">推奨：<em>略語のスペルではなく、発音に基づいて冠詞を使用する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">an ISP</td></tr>
<tr><td style="width: 100%;">a DLL</td></tr>
<tr><td style="width: 100%;">an HTML site</td></tr>
<tr><td style="width: 100%;">a CSV file</td></tr>
</tbody>
</table>
{:/}

#### 能動態 {#active-voice}

Braze では可能な限り能動態を使用します。能動態は私たちのゴールドスタンダードです。受動態では、誰が、または何が特定のアクションを実行しているかを判断するのが難しくなる場合があるため、避けてください。

文が受動態かどうかを確認するには、動詞の後に「by somebody」を挿入してみてください。文が意味をなす場合、受動態である可能性が高いです。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>能動態を使用する</em></th><th style="width: 50%;">非推奨：<em>可能であれば受動態を使用しない</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Braze connects consumers to the brands they love.</td><td style="width: 50%;">Consumers are connected to the brands they love.</td></tr>
<tr><td style="width: 50%;">Braze requires employees to keep their addresses up to date.</td><td style="width: 50%;">Employees are required to keep their addresses up to date.</td></tr>
<tr><td style="width: 50%;">Company administrators can configure authentication requirements for signing into Braze.</td><td style="width: 50%;">Authentication requirements for signing into Braze can be configured by company administrators.</td></tr>
</tbody>
</table>
{:/}

##### 例外

以下のケースでは受動態を使用しても問題ありません：

* 主語を目立たなくするため（一般的に、読者を非難することを避けるため）：
  - **推奨：** Two errors were found in the email.
  - **非推奨：** You created two errors in the email.
* アクションの責任者が誰かを知ることが重要でない場合：
  - **推奨：** This article was last updated in December 2020.

#### 冠詞 {#articles}

ライティングを明確にし、翻訳を支援するために、冠詞「a」、「an」、「the」を使用します。特定の単数名詞または複数名詞の前には「the」を使用し、不特定の単数名詞の前には「a」または「an」を使用します。

「a」と「an」のどちらを使用するかを判断するには、後に続く単語の発音を確認します。子音の音の前には「a」を使用し、母音の音の前には「an」を使用します。同じガイドラインが[略語](#abbreviations)にも適用されます。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">推奨：<em>先行する単語の発音に基づいて冠詞を使用する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">an hour</td></tr>
<tr><td style="width: 100%;">a minute</td></tr>
<tr><td style="width: 100%;">an FAQ article</td></tr>
<tr><td style="width: 100%;">a LAB course</td></tr>
</tbody>
</table>
{:/}

#### 代名詞 {#pronouns}

##### 人称代名詞

可能な限り二人称代名詞（you）を使用します。

外部向けのライティングでは、Braze の顧客を「user」と呼ばず、「you」を使用して読者に直接語りかけます。顧客の顧客に言及するには、「your consumers」を使用するか、ユーザー統計に関連する状況では「your users」を使用します。

以下のケースを除き、一人称代名詞（I、we、us、our）を避けます：

* FAQ のエントリ。たとえば、「How do I reset my password?」。
* 組織としての Braze に言及するために「we」を使用する場合。
 * 「we」が誰を指しているか不明確な場合は、まず Braze を名前で呼び、その後の言及で「we」を使用します。

##### ジェンダーニュートラルな代名詞

対象者が使用する代名詞を使用します。不確かな場合は、単数代名詞として「they」、「them」、「their」を使用します。単数の「they」の代替として「he/she」や「(s)he」を使用しないでください。

性別付きの代名詞（he/she、him/her、his/hers）は、言及している人が実際にその性別である場合にのみ使用します。

##### 曖昧な代名詞 {#ambiguous-pronouns}

代名詞は名詞の代わりをします。代名詞が指す単語は先行詞と呼ばれます。指示や学習教材を書く際は、代名詞とその先行詞の間の参照を明確にしてください。意味を明確にするために主語を繰り返す必要がある場合があります。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>代名詞が先行詞を明確に参照していることを確認する</em></th><th style="width: 50%;">非推奨：<em>曖昧な代名詞参照を使用する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">If you type text in the field, the text doesn't change.</td><td style="width: 50%;">If you type text in the field, it doesn't change.</td></tr>
<tr><td style="width: 50%;">She told Sarah that Sarah's answer was incorrect.</td><td style="width: 50%;">She told Sarah that her answer was incorrect.</td></tr>
<tr><td style="width: 50%;">You can't edit an archived campaign. Unarchive a campaign to edit it.</td><td style="width: 50%;">You can't edit an archived campaign. Unarchive it to edit it.</td></tr>
</tbody>
</table>
{:/}

##### 任意の代名詞

ライティングにさらなる明確さを加え、ローカライゼーションを支援するために、「that」、「which」、「who」などの代名詞を使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>「that」、「which」、「who」を使用してさらなる明確さを加える</em></th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Right-click the link that you want to open.</td><td style="width: 50%;">Right-click the link you want to open.</td></tr>
<tr><td style="width: 50%;">From here, you can choose which Tinyclues cohort that you want to include.</td><td style="width: 50%;">From here, you can choose a Tinyclues cohort you want to include.</td></tr>
</tbody>
</table>
{:/}

#### 大文字と小文字 {#capitalization}

不必要な大文字化を避けます。ほとんどの場合、センテンスケースを使用します。タイトルケースは固有名詞や機能名にのみ使用してください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>ウェブサイトの URL やメールアドレスには小文字を使用する</em></th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">www.braze.com/docs</td><td style="width: 50%;">www.Braze.com/docs</td></tr>
<tr><td style="width: 50%;">sample@email.com</td><td style="width: 50%;">SAMPLE@EMAIL.COM</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>方角は小文字を使用する</em></th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">north, south, east, west</td><td style="width: 50%;">North, South, East, West</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>特定の地域は大文字にし、略称の地域はすべて大文字にする</em></th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">the Northwest</td><td style="width: 50%;">the northwest</td></tr>
<tr><td style="width: 50%;">Southern Connecticut</td><td style="width: 50%;">southern Connecticut</td></tr>
<tr><td style="width: 50%;">Eastern Europe</td><td style="width: 50%;">eastern Europe</td></tr>
<tr><td style="width: 50%;">APAC, EMEA</td><td style="width: 50%;">Apac, emea</td></tr>
</tbody>
</table>
{:/}

##### ブランドと製品

ブランドや製品に言及する際は、そのブランドが使用する大文字・小文字を使用します。ほとんどの場合、ブランド名（Grindr、Walmart）と製品名（Benchmarks、Looker Blocks）は大文字にします。eBay や iTunes のように、最初の単語がブランドのスタイル化された名前である場合は、小文字で文を始めても問題ありません。

インターキャップについては、常に印刷物でブランドが好む使用法を参照してください（OkCupid、YouTube）。ロゴやグラフィックデザインの処理にのみ表示されるインターキャップは使用しないでください（Amazon）。

#### 節の順序 {#clause-order}

特定の状況で読者に何かをするよう伝えたい場合は、指示を提供する前に状況を述べるようにします。これにより、状況が該当しない場合、読者は指示をスキップできます。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">For troubleshooting steps, see Campaign FAQs.</td><td style="width: 50%;">See Campaign FAQs for troubleshooting steps.</td></tr>
<tr><td style="width: 50%;">To archive your campaign, click the gear icon and select Archive.</td><td style="width: 50%;">Click the gear icon and select Archive to archive your campaign.</td></tr>
</tbody>
</table>
{:/}

#### 結合形 {#combining-forms}

フレーズが名詞の前の形容詞として使用される場合は、結合形を[ハイフン](#hyphens)でつなぎます。

**例：** A one-of-a-kind item

#### 短縮形 {#contractions}

短縮形は、単語やフレーズの短縮版です。親しみやすくカジュアルなトーンを保つために短縮形を使用します。ただし、名詞と動詞の短縮形や二重短縮形、または2つの短縮形の組み合わせは使用しないでください。これらは文の流れと一貫性を損なう可能性があります。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>短縮形を使用する</em></th><th style="width: 50%;">非推奨：<em>名詞と動詞の短縮形を使用する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">If you're an admin, you can manage your company's contact information.</td><td style="width: 50%;">Braze'll now support Shoptify integration.</td></tr>
<tr><td style="width: 50%;">You can't edit an archived campaign.</td><td style="width: 50%;">You mightn't've seen the restricted upload size.</td></tr>
</tbody>
</table>
{:/}

#### 懸垂修飾語と誤配置修飾語 {#dangling-and-misplaced-modifiers}

修飾語は、他の単語やフレーズを修飾する単語やフレーズです。懸垂修飾語は、文中のどの主語も修飾しません。誤配置修飾語は、修飾する対象の主語から離れた場所に配置されます。基本的に、懸垂修飾語と誤配置修飾語は、文の間違った部分に接続することで混乱を引き起こす可能性があります。

能動態で書くことで、懸垂修飾語と誤配置修飾語の使用を防ぐことができます。明確に修飾する修飾語を使用してください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>文を短く簡潔に保つ。能動態を使用する。</em></th><th style="width: 50%;">非推奨：<em>混乱を引き起こす可能性のある修飾語を含む長い文を使用する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Customers must set up their SAML settings.</td><td style="width: 50%;">You may have test messages on your campaigns that can be deleted.</td></tr>
<tr><td style="width: 50%;">Make sure to save your campaign drafts.</td><td style="width: 50%;">On the way home, Sarah found a gold man's stopwatch.</td></tr>
</tbody>
</table>
{:/}

#### 前置詞 {#prepositions}

読みやすさが向上する場合は、前置詞で文を終えても問題ありません。前置詞または前置詞句は、文中で最も意味のある場所に配置します。困った場合は、文を声に出して読んで、自然に聞こえるか確認してください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Each option corresponds to the priority the notification appears in.</td><td style="width: 50%;">Each option corresponds to the priority in which the notification appears.</td></tr>
<tr><td style="width: 50%;">For details, see the SDK documentation for the platform you're working with.</td><td style="width: 50%;">For details, see the SDK documentation for the platform with which you're working.</td></tr>
</tbody>
</table>
{:/}

#### 現在時制 {#present-tense}

未来時制の代わりに現在時制を使用します。現在時制は即時性を伝え、自信を示します。特にユーザーアクションの結果に言及する際は、「will」や仮定の「would」の使用を避けてください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Archived subscription groups cannot be edited and no longer appear in segment filters.</td><td style="width: 50%;">Archived subscription groups cannot be edited and will no longer appear in segment filters.</td></tr>
<tr><td style="width: 50%;">Using a short code is the most reliable number type for including links.</td><td style="width: 50%;">Using a short code would be the most reliable number type for including links.</td></tr>
</tbody>
</table>
{:/}

実際に未来について話している場合にのみ未来時制を使用します。[将来の機能](#describing-limitations)を予測することは避けてください。

#### 不適切な言葉 {#profanity}

PG レベルに保ちます。これは道徳の問題というよりも、不適切な言葉は私たちのような幅広い国際的なオーディエンスにとって分裂的で不快になり得るという事実に関係しています。また、不適切な言葉が中途半端なライティングの隠れ蓑になることもあります。それは私たちのスタイルではありません。

#### かっこ内の複数形 {#plurals-in-parentheses}

かっこ内の複数形を使用しないでください。代わりに、単語の複数形または単数形を使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Customize your campaign with the following filters.</td><td style="width: 50%;">Customize your campaign with the following filter(s).</td></tr>
</tbody>
</table>
{:/}

#### 二人称と一人称 {#second-person-and-first-person}

指示では一人称ではなく二人称を使用します。「we」ではなく「you」を使います。

読者がアクションを実行する人として扱います。会話的なトーンを心がけてください。ほとんどの読者は、サポートエージェントにすぐにアクセスできないときにドキュメントを参照します。記事が読者に直接語りかけているように感じさせてください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">If you want to add a variant...</td><td style="width: 50%;">If we want to add a variant...</td></tr>
</tbody>
</table>
{:/}

読者に何かをするよう伝える場合は、「you」を省略して命令形を使用できます。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Upload the CSV file.</td><td style="width: 50%;">You can upload the CSV file.</td></tr>
<tr><td style="width: 50%;">Select Submit.</td><td style="width: 50%;">You'll need to select Submit.</td></tr>
</tbody>
</table>
{:/}

二人称を使用する際は、ドキュメントのオーディエンスが誰であるかを把握し、誰に話しかけているかについて一貫性を保ってください。

#### スラングと慣用句 {#slang-and-idioms}

私たちは率直な集団です。特定のオーディエンスにのみ通じるトレンディなスラングや慣用句の使用を避けてください。これにより、素材がすぐに古くなり、コンテンツのローカライゼーションが困難になる可能性もあります。

#### スペル {#spelling}

イギリス英語と異なる単語にはアメリカ英語のスペルを使用します。単語のスペルがわからない場合は、まず[用語集](#glossary)を参照してください。用語集に掲載されていない場合は、[Merriam-Webster's Collegiate Dictionary](https://www.merriam-webster.com/) を参照してください。

アクセント付きの単語や特殊文字を含む単語については、辞書のスペルに正しく従ってください。場合によっては、これらのアクセントを意図せず省略すると、別の単語になることがあります。たとえば、「resume」は停止後に再開することを意味しますが、「résumé」は資格の概要です。

### 句読点 {#punctuation}

#### アンパサンド {#ampersands}

ユーザーインターフェイスを直接参照している場合を除き、テキストや見出しで「and」の代わりにアンパサンド (&) を使用しないでください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Drag-And-Drop Editor</td><td style="width: 50%;">Drag & Drop Editor</td></tr>
<tr><td style="width: 50%;">SMS and MMS</td><td style="width: 50%;">SMS & MMS</td></tr>
</tbody>
</table>
{:/}

#### アポストロフィ {#apostrophes}

アポストロフィは、名詞を所有格にするために最もよく使用されます。

* S で終わる単数名詞の場合、アポストロフィの後にもう1つの S を付けても問題ありません。
 * **例：** Chris's, business's, alias's
* S で終わる複数名詞の場合、アポストロフィを追加しますが、追加の S は付けません。
 * **例：** users'

#### コロン {#colons}

リストや例の前の導入フレーズの末尾にコロンを使用します。導入文は、単独で完全な文として成立する必要があります。これはアクセシビリティとローカライゼーションの両方の目的のためであり、文の断片は翻訳が困難です。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">The general structure is as follows:</td><td style="width: 50%;">The general structure is:</td></tr>
</tbody>
</table>
{:/}

コロンの前のテキストが太字の場合は、コロンも太字にします。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>Scheduled:</strong> Time-based entry.</td><td style="width: 50%;"><strong>Scheduled</strong>: Time-based entry.</td></tr>
</tbody>
</table>
{:/}

コロンの前のテキストがコードテキストの場合、コード要素の一部でない限り、コロンをコードテキストに含めないでください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>user_alias_label</code>: A common label to group user aliases with.</td><td style="width: 50%;"><code>user_alias_label:</code> A common label to group user aliases with.</td></tr>
</tbody>
</table>
{:/}

コロンを使用して、文中の2つの関連するフレーズをつなぐこともできます。ただし、この用途でのコロンの使用は控えめにしてください。一般的に、2つの文の方が読みやすいです。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Coming up next week: we're going on a tour of the West Village.</td></tr>
</tbody>
</table>
{:/}


#### コンマ {#commas}

Braze では、指示や学習コンテンツを書く際にオックスフォードコンマ（シリアルコンマ）を使用します。シリーズの項目を区切るために、最後の接続詞の前にコンマを使用します。

導入フレーズの後にコンマを使用します。

等位接続詞（「and」、「but」、「or」、「yet」、「so」などの単語）が2つの独立節を区切る場合、最初の節の後、接続詞の前にコンマを配置します。ただし、両方の節が短い場合、このコンマは必要ありません。

たとえば、以下は2つの独立節です：

* 「All fields are optional.」
* 「You must specify at least one field.」

等位接続詞「but」を使用した文は「All fields are optional, but you must specify at least one field.」となります。

独立節と従属節が同じ文で使用される場合、それらを区切るためにコンマを使用しないでください。コンマの配置なしに文が誤解される可能性がある場合にのみ、このシナリオでコンマを使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Push subscriptions states are filters and can allow users to edit notification preferences.</td><td style="width: 50%;">Push subscriptions states are filters, and can allow users to edit notification preferences.</td></tr>
</tbody>
</table>
{:/}

#### ダッシュ {#dashes}

##### em ダッシュ

文中でダッシュを使用して別の考えや中断を示す場合は、em ダッシュ（—）を使用します。em ダッシュの前後にスペースを入れないでください。コンマやかっこで十分な場合は、em ダッシュを使用しないでください。

em ダッシュの入力方法については、お使いのオペレーティングシステムを参照してください：

* **macOS：** Option + Shift + Hyphen を押します。
* **Windows：** Num Lock をオンにし、左 Alt キーを押しながらテンキーで 0151 と入力します。

##### en ダッシュ {#en-dash}

数値の範囲、マイナス記号、または負の数を示すには、en ダッシュ（–）を使用します。マイナス記号として使用する場合を除き、en ダッシュの前後にスペースを入れないでください。ハイフン（-）を使用しないでください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>数値の範囲には en ダッシュを使用する</em></th><th style="width: 50%;">非推奨：<em>ハイフンを使用する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">2018–2021</td><td style="width: 50%;">2018-2021</td></tr>
</tbody>
</table>
{:/}

時間の範囲には en ダッシュを使用しないでください。詳しくは、[日付と時刻](#dates-and-times)のセクションを参照してください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>マイナス記号には en ダッシュを使用し、en ダッシュの前後にスペースを入れる</em></th><th style="width: 50%;">非推奨：<em>ハイフンを使用する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">15 – 5 = 10</td><td style="width: 50%;">15-5=10</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>負の数には en ダッシュを使用する</em></th><th style="width: 50%;">非推奨：<em>ハイフンを使用する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">–30</td><td style="width: 50%;">-30</td></tr>
</tbody>
</table>
{:/}

en ダッシュの入力方法については、お使いのオペレーティングシステムを参照してください：

* **macOS：** Option + Hyphen を押します。
* **Windows：** Num Lock をオンにし、左 Alt キーを押しながらテンキーで 0150 と入力します。

#### 省略記号 {#ellipses}

省略記号は、1つ以上の単語の省略を示す3つのピリオド（...）の連続です。一般的に、指示や学習コンテンツを書く際は、可能な限り省略記号の使用を避けてください。

#### 感嘆符 {#exclamation-points}

カジュアルなトーンのために感嘆符を控えめに使用できます。ただし、テキスト全体で感嘆符を過度に使用することは避けてください。代わりに、[アラート](#callouts-and-alerts)の使用を検討してください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>リマインダーや紹介のカジュアルなトーンに感嘆符を使用する</em></th><th style="width: 50%;">非推奨：<em>読者への警告や注意を示すために感嘆符を使用する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Be sure to save your changes before leaving the page!</td><td style="width: 50%;">Users must receive one or more messages from a step to be counted as a unique recipient!</td></tr>
</tbody>
</table>
{:/}

#### ハイフン {#hyphens}

ハイフンは、フレーズ内の単語をリンクすることで、読者が文をより明確に理解するのに役立ちます。正しく使用するためのガイドラインをいくつか紹介します。

読者が主語をより明確に理解するのに役立つ複合修飾語にはハイフンを使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">real-time data streaming</td></tr>
</tbody>
</table>
{:/}

修飾語と主語の間にスペースを入れて、フレーズをリンクするためにハイフンを使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">All-in-one solutions</td></tr>
</tbody>
</table>
{:/}

主語を修飾するフレーズにはハイフンを使用します。フレーズが主語そのものである場合は、ハイフンを使用する必要はありません。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">It was a well-known fact.</td><td style="width: 50%;">That fact is well-known</td></tr>
</tbody>
</table>
{:/}

文中で一時停止を作るために、em ダッシュの代わりにハイフンを使用しないでください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">...third-party integrations—such as Slack—and automate...</td><td style="width: 50%;">...third-party integrations-such as Slack-and automate...</td></tr>
</tbody>
</table>
{:/}

副詞の後にハイフンを使用しないでください。単語を分けたままにします。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Hastily made</td><td style="width: 50%;">Hastily-made</td></tr>
</tbody>
</table>
{:/}

#### かっこ {#parentheses}

かっこは控えめに使用します。重要な情報をかっこ内に入れないでください。一部の読者はかっこ内のコンテンツをスキップします。

重要度の低い括弧書きについては、かっこを削除するように文を書き直すことを検討してください。たとえば、コンマ、ダッシュ、セミコロンを使用してフレーズや文を区切るか、新しい文を追加できます。

かっこがより大きな文の一部である場合は、かっこの外側にピリオドを配置します。かっこが完全な文を含む場合は、内側にピリオドを配置します。

**関連セクション：** [かっこ内の複数形](#plurals-in-parentheses)

#### ピリオド {#periods}

文を終えるためにピリオドを使用します。見出し、小見出し、UI 要素を終えるためにピリオドを使用しないでください。

リスト項目でピリオドを使用するタイミングのガイドラインについては、[リスト](#lists)を参照してください。

#### セミコロン {#semicolons}

セミコロンは、より長く複雑な文を分割するのに最適です。トピックが密接に関連する2つの独立節を区切るためにセミコロンを使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">推奨：<em>関連する2つの独立節を持つ文を分割するためにセミコロンを使用する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">The cat slept through the storm; the dog cowered under the bed.</td></tr>
</tbody>
</table>
{:/}

リスト項目の1つ（またはそれ以上）にコンマが含まれている場合、セミコロンを使用してリスト項目を区切ることができます。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">推奨：<em>より長い文を分割するためにセミコロンを使用する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Jane Lang, our moderator; Simon Mayer, CEO and Cofounder of PantsLabyrinth; and Kara Seberg, CMO of Yachtr.</td></tr>
</tbody>
</table>
{:/}

#### スラッシュ {#slashes}

スラッシュには、バックスラッシュ（\\）とフォワードスラッシュ（/）の2種類があります。代替の単語や例を示すためにスラッシュを使用しないでください（「and/or」）。

ファイルパスや URL では必要に応じてスラッシュを使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>ファイルパスにはスラッシュを使用する</em></th><th style="width: 50%;">非推奨：<em>代替を区切るためにスラッシュを使用する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/campaigns/data_series</code></td><td style="width: 50%;">you/your customers</td></tr>
</tbody>
</table>
{:/}

#### 引用符 {#quotation-marks}

引用符には、ストレート（" "）とカーリー（" "）の2種類があります。ピリオドとコンマは引用符の内側に配置します。例外は、引用符が文字列などの正確な情報を含む場合です。テキストフィールドに特定の文字列を入力するようユーザーに指示する際は、引用符を使用します。

{% alert note %}

検索構文を説明する際、引用符は正確なテキストの検索を示すためによく使用されます。この場合、テキスト文字列の周りにブラケットを使用し、検索構文で必要な引用符を使用します。たとえば：<br><br>

*["test segment"] のように、任意の単語やフレーズを引用符で囲むと、その正確な単語やフレーズのみを含む結果が表示されます。*

{% endalert %}

コード例ではストレート引用符を使用する必要があります。テキスト内のコードのフォーマットについて詳しくは、[テキスト内のコード](#code-in-text)を参照してください。

### テクニカルドキュメント {#technical-documentation}

#### API エンドポイント {#api-endpoints}

一般的に、API エンドポイントのドキュメントは、このスタイルガイドのガイドラインに従う必要があります。ただし、このドキュメントに記載されている異なるコンテンツガイドラインが必要なニッチなトピックがある場合があります。エンドポイントのフォーマットと参照方法について詳しくは、[API エンドポイントドキュメントガイドライン]({{site.baseurl}}/contributing/style_guide/api_endpoint_guidelines/)を参照してください。

#### 保証を避ける {#avoid-guarantees}

ドキュメントでは、法的な影響を及ぼす可能性のあるコミットメントを行うことを控える必要があります。「guarantee」や「ensure」のような断定的な用語の使用を避けてください。代わりに、「Designed to」や「Intended to」のような前向きな表現を使用して、製品の機能と意図を正確に伝えます。

#### UI とのインタラクションの説明 {#describing-interactions-with-the-ui}

UI 要素に言及する際は、UI に表示されている大文字・小文字に合わせます。ただし、ラベルがすべて大文字の場合は、センテンスケースを使用します（例外：AND や OR オペレーターのような短いラベル）。

読者に UI とのインタラクションを指示する際は、インタラクションする UI 要素を太字にします。ユーザーがフィールドに入力する文字列には、引用符を使用します。

UI とのインタラクションを説明する際に使用する動詞のガイダンスについては、以下のテーブルを参照してください：

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 20%;">
<col style="width: 40%;">
<col style="width: 40%;">
</colgroup>
<thead>
<tr><th>動詞</th><th>使用法</th><th>例</th></tr>
</thead>
<tbody>
<tr><td>Open</td><td><ul><li>アプリを開く</li><li>ファイルやフォルダーを開く</li></ul></td><td><ul><li>Open Droidboy.</li><li>Open the braze.xml file.</li></ul></td></tr>
<tr><td>Close</td><td><ul><li>アプリを閉じる</li><li>ファイルやフォルダーを閉じる</li></ul></td><td><ul><li>Close Droidboy.</li><li>Close the braze.xml file.</li></ul></td></tr>
<tr><td>Go to</td><td><ul><li>UI の特定のページに移動する（タブ、ページ、セクション）</li><li>ウェブページに移動する</li></ul></td><td><ul><li>Go to the <strong>Segments</strong> page, and click…</li><li>Go to example.com to sign up.</li></ul></td></tr>
<tr><td>&gt;</td><td>すべてのステップが同じタイプの場合に、一連のステップに従います。</td><td>Go to <strong>Segments</strong> &gt; <strong>Segment Insights</strong>.</td></tr>
<tr><td>Choose</td><td>主観的、戦略的、オープンエンド、または複雑な決定を行います。</td><td>Choose a campaign strategy.</td></tr>
<tr><td>Select</td><td><ul><li>チェックボックスを選択する</li><li>ドロップダウンから項目を選択する</li><li>タブを選択する</li><li>シンプルな決定を行う</li></ul></td><td><ul><li>Select <strong>Show Password</strong>.</li><li>Select a data type from the dropdown.</li><li>On the <strong>Manage Settings</strong> page, select the <strong>Custom Events</strong> tab.</li><li>Select an image.</li></ul></td></tr>
<tr><td>Clear</td><td>チェックボックスの選択を解除します。</td><td>Clear the <strong>Show Password</strong> checkbox.</td></tr>
<tr><td>Select</td><td>UI の要素を選択します。</td><td>Add a custom attribute and select <strong>Save</strong>.</td></tr>
<tr><td>Turn on</td><td>トグルオプションを有効にします。</td><td>Turn on the <strong>List-Unsubscribe header</strong>.</td></tr>
<tr><td>Turn off</td><td>トグルオプションを無効にします。</td><td>Turn off <strong>Inline CSS on New Emails by Default</strong>.</td></tr>
<tr><td>Enter</td><td>値を入力します。</td><td><ul><li>In the text field, enter the name of your custom attribute.</li><li>Enter "Braze" as the source name.</li></ul></td></tr>
</tbody>
</table>
{:/}

#### 制限事項の説明 {#describing-limitations}

製品の制限事項について、歪曲や操作なしに率直に書きます。読者は操作されたり、騙されたりすることに強く反応し、これはドキュメントの実用的な真実の源としての有効性を損ないます。顧客は、Braze を正常に使用できるように、構築しているシステムの制限を理解するためにドキュメントに依存しています。

同時に、制限事項を適切でポジティブなコンテキストでフレーミングすることで、製品開発の意図性をサポートします。

* ソフトリミット（たとえば、API レート制限）がある場合は、**デフォルトの制限**または**初期割り当て**について話すことで制限をフレーミングします。
* ソフトリミットを回避するための意味のある道筋を提供します。必要に応じて、これらの回避策の例を提供します。
 * たとえば、Braze はオンボーディング中にサイジングエクササイズを使用して、データポイントなどが同様の規模の他のビジネスでどのように使用されているかを顧客が理解できるようにします。データポイントについて議論する際は、同時にサイジングエクササイズについて話すことが適切です。
* 緩和策としてではなく、ポジティブな方法で前進の道筋を説明する方が良いです。
 * たとえば、「Braze does not allow customers to do this on their own. The Support team must activate this feature for you.」と言う代わりに、「To activate this feature, contact the Support team.」と言います。
* ソフトリミットを回避するために同じ定型句に過度に依存しないでください。ユーザーが「Talk to your customer service representative」を何度も読むと、そのアドバイスは意味をなさなくなります。
* ハードリミットがある場合は、この制限の背後にある理由を説明するようにします。
 * たとえば：「There is a limit of 200 active, action-based in-app message campaigns per app group to optimize the speed of message delivery and to prevent timeouts. …The average Braze customer has a total of 26 campaigns active at once—so it's unlikely that this limitation impacts you.」
* 現在の制限を説明する方法として、[計画された機能や将来の機能](#future-features)を説明しないでください。
* カスタムデータに関する制限に言及する際は、「limits」の代わりに「capacity」という用語を使用します。
 * たとえば：By default, you can have 20 segmentable event properties per workspace. Contact your Braze アカウントマネージャー to increase your capacity.

#### 将来の機能 {#future-features}

将来の機能への言及や、将来サポートされる可能性があるという示唆を避けてください。

ライティングを特定の時点に固定する単語やフレーズを使用しないでください。コンテンツがすぐに古くなります。製品が現在どのように機能するかに焦点を当て、何が変わったかには焦点を当てないでください（リリースノートなどの時間に焦点を当てたコンテンツを除く）。

具体的には、Google の[開発者ドキュメントスタイルガイド](https://developers.google.com/style/timeless-documentation)から取った以下の単語やフレーズを避けてください：

* as of this writing
* currently
* does not yet
* eventually
* future, in the future
* latest
* new, newer
* now
* old, older
* presently, at present
* soon

#### 機能の廃止 {#features-deprecations}

機能の廃止に関する情報を含める前に、読者が機能の廃止を予想できる一般的な時間枠（たとえば、2025年後半）を把握していることを確認してください。

一般的な時間枠が決まったら、機能の廃止を早期に伝えます。読者が何を期待すべきかを明確に理解できるように、廃止について明確に書きます。

読者に恐怖、不確実性、疑念を抱かせるようなフレーズを使用しないでください。廃止される機能の代替となるものや代替ソリューションなど、明確な前進の道筋を提供します。

#### 一般的 vs 具体的 {#general-vs-specific}

ベストプラクティスとして、一般的に適用可能な方法で機能を説明する記事を書きます。特定のケースや例外についてより詳細が必要な場合は、この例外を概説する別のセクション（またはコンテンツがウェブ記事の長さ、約500語の場合は別の記事）を作成します。一般的な記事から具体的な記事へのクロスリファレンスを作成して、ユーザーがこれらの概念を結びつけるのを助けます。

異なるチャネルや機能のために重複した繰り返しのコンテンツを作成することを避けます。繰り返しが必要な場合は、`includes` ファイルやその他の[再利用可能なコンテンツのベストプラクティス]({{site.baseurl}}/contributing/content_management/reusing_content)を使用します。

**例として：** Braze の顧客の一般的なユースケースは、以前にメッセージングとインタラクションしたユーザーをリターゲティングすることです。ユーザーのリターゲティングは、キャンペーン、キャンバス、ランディングページ、セグメントなど、多くのエンゲージメントツールを通じて行うことができます。ユーザーのリターゲティングは、WhatsApp、SMS、コンテンツカード、メール、プッシュ通知など、多くのチャネルを通じて行うことができます。多くの場合、顧客は以前使用したチャネルとは別のチャネルを通じてユーザーを再エンゲージしようとします。
各エンゲージメントツールと各チャネルに1つの記事を作成する代わりに、ユーザーのリターゲティング戦略を説明し、利用可能なすべてのオプションを概説する単一の記事を作成します。特定のチャネル/ツールに特別な考慮事項がある場合は、それらの考慮事項を概説する別の記事を作成し、そのドキュメントセクション内に配置します。一般的な記事と具体的な記事の間にクロスリファレンスを作成します。

#### メタデータと YAML {#metadata-and-yaml}

Braze ドキュメントの記事には、検索とインデックスの目的で特定のメタデータが必要です。必要なメタデータについては、GitHub ページの [YAML and Metadata Layouts](https://github.com/braze-inc/braze-docs/wiki/YAML-%26-Metadata-Layouts) を参照してください。

#### 命名規則 {#naming-conventions}

記事やファイル名を命名する際は、タイトルに一般的なトピックを説明するようにします。特に記事タイトルでは、読者が容易に理解できるキーワードと簡潔な説明を常に含めてください。

ファイル名については、名前を簡潔に保ち、冠詞（a、an、the）の使用を避けます。各単語をアンダースコア（_）で区切ります。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Targeting users</td></tr>
<tr><td style="width: 100%;">Creating an email campaign</td></tr>
<tr><td style="width: 100%;">API errors and responses</td></tr>
<tr><td style="width: 100%;">sms_historical_performance.png</td></tr>
<tr><td style="width: 100%;">push_notification_test.png</td></tr>
</tbody>
</table>
{:/}

一般的に、記事や画像ファイルについては、参照される記事やファイルと同じスペルと大文字・小文字を使用します。記事タイトルのスタイリングのガイドラインについては、[見出しとタイトル](#headings-and-titles)を参照してください。

特定のファイルに言及する際は、ファイル名と同じスペルとコードフォントを使用します。フォーマットの詳細については、GitHub ページの [Special Formatting](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting) を参照してください。

#### 手順と指示 {#procedures-and-instructions}

このセクションでは、Braze ダッシュボードの手順の指示を書く際に留意すべきガイドラインを説明します。

一般的なガイドライン：

* **適切なトーンを使用します。** 指示については、ライティングを短く、要点を押さえ、タスク指向に保ちます。ライティングが簡素で無味乾燥である必要はありませんが、直接的であるべきです。タスクやサブタスクを紹介する際は、よりカジュアルなトーンを使用してバリエーションを加えることができます。トーンをカジュアルに保つために「please」の使用を避けます。短縮形を積極的に使用して、トーンを親しみやすく保ちます。
* **並列の見出しフォーマットに従います。** 見出しの1つのフォーマットを選び、それに従います。コンテンツをスキャンしやすく予測可能に保ちます。タスクベースの見出しやページタイトルには、命令形の動詞を優先します（たとえば、「Create an email campaign」）。

指示の前に：

* **導入と前提条件を使用します。** いきなりステップに入らないでください。代わりに、記事やセクションが何をカバーしているかのコンテキストを提供し、読者が指示をスキャンする前に知っておく必要がある情報を提供します。前提条件は、「Prerequisites」という見出しで記事の上部にリストされていることを確認してください。このセクションのテーブルヘッダーは「Requirements」とします。「Requirements」は、Braze、サードパーティプロバイダー、またはパートナーからの要件を述べるために使用できる用語です。
* **手順の最初から始めます。** 読者が前のステップを完了した後にこのページに到達したと仮定しないでください。タスクの指示が前のタスクの続きである場合は、読者が手順のどこにいるか、このステップの前に何を完了する必要があるかの概要を提供します。前のステップへのリンクを含めます。

指示の書き方：

* **アクション可能な言葉を使用します。** 製品ができることではなく、ユーザーができることを中心にドキュメントを構成します。「This feature [does xyz]」のような言葉を避けます。代わりに、「Use this feature to [do xyz]」の観点で考えます。
* **必要に応じてロケーションステップを提供します。** 「On the **Settings** page, select **Edit**.」のような簡潔なフレーズで、読者が正しい場所を見ていることを確認します。それだけでは十分に明確でない場合は、導入ステップを提供します。たとえば、「Go to **Manage Settings** and select the **Settings** tab.」
* **条件文を前置きします。** [条件節](#clause-order)を先に配置します。条件付きの指示については、ステップの前に「if」を付けて、条件が該当しない場合に読者がステップをスキップできるようにします。たとえば、「If you need X, then do A > B > C.」
* **タスクの順序を強化します。** 一連のステップ内の進行には、「When you've」または「After you've」というフレーズを使用します。タスク間の進行には、セクションの冒頭に「Now that you've」または「After you've」を使用します。「Once you've」というフレーズは、「once」のその特定の使用法が翻訳しにくいため、避けてください。

#### タブ {#tabs}

タブは、グループ化された情報を整理する方法として、テクニカルドキュメントで使用できます。

タブとは、ワークフローの概要を示したり、グループ化された情報を整理したりするために、指示を書く際に使用できる要素を指します。これはテーブルやリストに似ていますが、情報はパネルにグループ化されます。

重複を避けたり、読者にワークフローを視覚化したりするために、情報をグループ化できる場合はタブの使用を検討してください。タブには並列の情報が含まれていることを確認し、読者がワークフローの順次ステップに従う必要がある場合には使用しないでください。

たとえば、タブを使用して異なるプログラミング言語のコード例を表示できます。この場合、読者は記事をスクロールする代わりに、タブラベルに基づいて例を切り替えます。

フォーマットの詳細については、GitHub ページの [Special Formatting](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting) を参照してください。あるいは、[リスト](#lists)や[テーブル](#tables-1)を使用して情報を整理することもできます。

### フォーマットと整理 {#formatting-and-organizing}

#### 住所 {#addresses}

数字の後にストリート名を以下のように使用します：

*330 W. 34th St.*

完全な住所を表示するには、数字の後にストリート名、続いて市、州、郵便番号を使用します。州と郵便番号の間にコンマは不要です。

*330 W. 34th St., New York, NY 10001*

#### ボタンラベル {#buttons-labels}

ボタンラベルは明確で予測可能であるべきです。ユーザーはボタンを選択した際にどのアクションが発生するかを知っている必要があります。ボタンラベルにはセンテンスケースを使用し、強い動詞で始めます。動詞が何を指しているか不明確な場合は、[動詞] + [名詞] のフォーマットを使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Sign up</td><td style="width: 50%;">Sign Up</td></tr>
<tr><td style="width: 50%;">Log in</td><td style="width: 50%;">Log In</td></tr>
<tr><td style="width: 50%;">Subscribe</td><td style="width: 50%;">SUBSCRIBE</td></tr>
<tr><td style="width: 50%;">Learn more</td><td style="width: 50%;">More</td></tr>
</tbody>
</table>
{:/}

「a」、「an」、「the」などの不要な単語や冠詞を省略します。

#### コールアウトとアラート {#callouts-and-alerts}

アラート（コールアウトとも呼ばれます）は、読者にとって有用な情報に注意を引くために使用されます。ドキュメントで使用される4つのアラートタイプがあります：

* Important
* Note
* Tip
* Warning

記事全体でアラートを控えめに使用します。詳しくは、[アラートのベストプラクティス]({{site.baseurl}}/contributing/style_guide/alerts/)を参照してください。

#### テキスト内のコード {#code-in-text}

文中でコードフォントを使用してテキストをフォーマットすべきシナリオがいくつかあります。コードフォントにすべき項目の不完全なリストを以下に示します：

* 属性名と値
* API リクエストパラメーター
* ファイル名
* ファイルパス
* メソッド、変数、パラメーター名
* HTML および XML 要素名
* HTTP ステータスコード
* ターミナルへのテキスト入力

Braze ドキュメントでインラインコードテキストを作成するには、テキストをバッククォート（`）で囲みます。

#### コードサンプル {#code-samples}

コードサンプルとは、サンプルコードスニペットを表示するコードテキストのブロックを指します。アクセシビリティの目的で、可能な限り説明文でコードサンプルを紹介してください。

コードサンプルが読みやすいことを確認するために、インデントレベルごとに2つのスペースで各行をインデントします。コードサンプルのフォーマットに問題がある場合は、[JSON Formatter](https://jsonformatter.org/json-pretty-print) などのプリティプリントフォーマッターを使用してコードを整形してみてください。

Braze ドキュメントでコードブロックを作成するには、[Code Snippet Test](https://github.com/braze-inc/braze-docs/blob/develop/_docs/_home/styling_test_page.md#code-snippet-test) を参照してください。コードブロックでは、適切な構文ハイライトを確保するために言語タイプを指定する必要があることを覚えておいてください。

#### 日付と時刻 {#dates-and-times}

月と曜日はスペルアウトします。可能な限り略語を避けます。月の略語が必要な場合は、以下のみを略します：

* Jan.
* Feb.
* Aug.
* Sept.
* Oct.
* Nov.
* Dec.

日付と年を区切るために[コンマ](#commas)を使用します。曜日を日付と一緒に使用する場合は、月の前に追加します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">推奨：<em>推奨される日付フォーマットを使用する。</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">September 2021</td></tr>
<tr><td style="width: 100%;">September 15, 2021</td></tr>
<tr><td style="width: 100%;">Wednesday, September 15, 2021</td></tr>
</tbody>
</table>
{:/}

日付の範囲には、[en ダッシュ](#en-dash)を使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">2010–2021</td></tr>
</tbody>
</table>
{:/}

日付の範囲には en ダッシュを使用します。

数字の後にスペースを入れ、その後に時間帯（am または pm）を付けて数字を使用します。正時の場合は分を省略します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>am または pm 付きの数字を使用する。</em></th><th style="width: 50%;">非推奨：<em>正時に分を使用する（範囲の場合を除く）。</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">12 pm</td><td style="width: 50%;">12:00 P.M.</td></tr>
</tbody>
</table>
{:/}

時間の範囲には、en ダッシュを使用して区切ります。en ダッシュの前後にスペースを入れないでください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">推奨：<em>時間の範囲には en ダッシュを使用する。</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">12:45–2:30 pm</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">推奨：<em>時間の範囲には分を使用する。</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">8:00 am–2:30 pm</td></tr>
</tbody>
</table>
{:/}

他のタイムゾーンの関係者が含まれる場合（ウェビナー、ミーティング、イベントなど）の参考として、以下のようにタイムゾーンを示します：

* Eastern Standard Time: EST
* Central Standard Time: CST
* Mountain Standard Time: MST
* Pacific Standard Time: PST
* Greenwich Mean Time: GMT
* Coordinated Universal Time: UTC
* Central European Time: CET
* Eastern Europe Time: EET
* Western Europe Time: WET
* Singapore Time: SGT
* China Standard Time: CST

#### 絵文字 {#emojis}

私たちはカジュアルな集団ですが、学習コンテンツでの絵文字の使用は避けてください。絵文字はさまざまな方法で解釈される可能性があり、プロフェッショナルでない印象を与えることがよくあります。

以下のシナリオは例外です：

* テーブルで ✅ と ❌ を使用して、サポートされているコンテンツとサポートされていないコンテンツ、または推奨と非推奨を示す場合
* キャンペーンまたは Canvas メッセージのサンプルコピーで使用する場合

#### 例の名前 {#example-names}

実名、メールアドレス、その他の個人を特定できる情報（PII）を使用しないでください。代わりに、架空の例や[プレースホルダーテキスト](#placeholder-text)を使用します。

ライティングに名前を含める必要がある場合は、Wikipedia の [Unisex names](https://en.wikipedia.org/wiki/Unisex_name) のリストを参照してください。可能な限り代名詞「they」、「their」、「theirs」を使用し、特定の性別に限定された例の使用を避けてください。

##### 例のメールアドレス

一般的なメールアドレスには「name@example.com」のフォーマットを使用します。「name」を例の名前に置き換えます。たとえば：

* alex@example.com
* lee@example.com
* yuri@example.com

#### 図とその他の画像 {#figures-and-other-images}

図や画像を作成する際は、[画像コピースタイルガイド]({{site.baseurl}}/contributing/style_guide/image_style_guide/)を参照してください。図や画像に個人を特定できる情報（PII）を含めないでください。

##### 代替テキスト {#alt-text}

画像には常に代替テキストを含めてください。スクリーンリーダーは、視覚障害のある方に画像を説明するために代替テキストを読み上げます。そのため、代替テキストは画像に描かれているすべての重要な情報を伝える必要があります。
代替テキストを書く際は、以下のガイドラインを使用してください：

* [プレーンランゲージ](https://www.plainlanguage.gov/guidelines/)を使用します。
* 完全な文で書き、センテンスケースを使用します。
* 不要な単語を省略します。
* 「image of」や「picture of」を含めないでください。画像を参照していることは既に理解されています。
* 特殊文字を含めないでください。たとえば、アンパサンド（&）の代わりに「and」と書きます。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Custom Events settings page in the Braze dashboard with Add Report highlighted.</td><td style="width: 50%;">A screenshot of the Manage Settings > Custom Events page in the Braze dashboard with the option to add a report highlighted.</td></tr>
</tbody>
</table>
{:/}

画像がテキストで説明されている内容に冗長なビジュアルコンポーネントを追加している場合は、代替タグを明示的に空（alt=""）にします。

すべての画像に代替テキストを追加しても、ウェブページのコンテンツが自動的にナビゲートしやすく消費しやすくなるわけではありません。冗長なビジュアルは、視覚情報が理解しやすく記憶しやすいため、目の見えるユーザーにとって強力です。ただし、冗長な画像を説明する代替テキストは、画像を見ることができないユーザーにとっては不要な場合があります。スクリーンリーダーのユーザーは、すべてのページ要素に等しい注意を払って、それが自分のタスクに有用かどうかを判断する必要があるためです。

##### 例の会社名

可能であれば、FakeBrandz の会社名の1つを使用するために、[dashboard-06](https://dashboard-06.braze.com/) からスクリーンショットを撮ります。

#### ファイルタイプとファイル名 {#file-types-and-filenames}

ファイルタイプに言及する際は、タイプの標準名を使用します。ファイルタイプが頭字語の場合は、すべて大文字でファイルタイプを参照します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>ファイルタイプの標準名を使用する</em></th><th style="width: 50%;">非推奨：<em>ファイル拡張子を使用する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">CSV</td><td style="width: 50%;">.csv</td></tr>
<tr><td style="width: 50%;">executable file</td><td style="width: 50%;">.exe</td></tr>
<tr><td style="width: 50%;">GIF</td><td style="width: 50%;">.gif</td></tr>
<tr><td style="width: 50%;">JAR</td><td style="width: 50%;">.jar</td></tr>
<tr><td style="width: 50%;">JPEG</td><td style="width: 50%;">.jpg, .jpeg</td></tr>
<tr><td style="width: 50%;">JSON</td><td style="width: 50%;">.json</td></tr>
<tr><td style="width: 50%;">PDF</td><td style="width: 50%;">.pdf</td></tr>
<tr><td style="width: 50%;">PNG</td><td style="width: 50%;">.png</td></tr>
<tr><td style="width: 50%;">Python file</td><td style="width: 50%;">.py</td></tr>
<tr><td style="width: 50%;">Bash file</td><td style="width: 50%;">.sh</td></tr>
<tr><td style="width: 50%;">text file</td><td style="width: 50%;">.txt</td></tr>
<tr><td style="width: 50%;">YAML</td><td style="width: 50%;">.yaml</td></tr>
<tr><td style="width: 50%;">ZIP</td><td style="width: 50%;">.zip</td></tr>
</tbody>
</table>
{:/}

ファイルの名前に言及する際は、ファイル名をコードテキストとしてフォーマットします。詳しくは、[テキスト内のコード](#code-in-text)のセクションを参照してください。

Braze ドキュメントで記事や画像ファイルなどのファイルに名前を付ける際は、すべて小文字を使用し、ハイフンではなくアンダースコアで単語を区切ります。詳しくは、GitHub の [Creating Files and Folders](https://github.com/braze-inc/braze-docs/wiki/Creating-Files-&-Folders) を参照してください。

#### 脚注 {#footnotes}

脚注は、追加情報を提供する注釈であり、通常はページの末尾に配置されます。テキストのフォーマットの関係上、脚注はほとんどのユースケースに最適ではありません。以下は、脚注と他の帰属方法のどちらを使用するかを説明しています：

* ソースに帰属させる必要がある統計やその他の密な情報のリストを提示する場合は、脚注を使用します。
* 1つまたは2つの情報を提示する場合は、リンクまたはアラートを使用します。
* テーブル内の項目に追加情報を提供する必要がある場合は、テーブル項目の横にアスタリスク（*）記号を使用し、テーブルの後に情報を提示します。

#### 指示内のテキストフォーマット {#formatting-text-in-instructions}

一貫したテキストフォーマットを使用して、読者が情報を見つけて解釈するのを助けます。このセクションでは、指示内でさまざまなテキスト要素を説明または参照する際に使用するフォーマットのガイドラインを提供します。

このセクションでは、以下の要素を説明します：

* [ボタン](#buttons)
* [チェックボックス](#checkboxes)
* [コマンドラインのコマンドとオプション](#command-line-commands-and-options)
* [ダイアログボックス](#dialog-boxes-(modals))
* [エラーメッセージ](#error-messages)
* [フィルターとオペレーター名](#filter-and-operator-names)
* [フォルダーとファイル名](#folder-and-filenames)
* [キー名と組み合わせ](#key-names-and-combinations)
* [メトリクス](#metrics)
* [ページ](#pages)
* [権限名](#permission-names)
* [タブ](#tabs-1)
* [テキスト入力](#text-input)

##### ボタン {#buttons}

ボタンに言及する際は、ボタンラベルに太字テキストを使用します。ほとんどの場合、UI の大文字・小文字に合わせます。ラベルがすべて大文字のボタン（OK ボタンを除く）の場合は、代わりにセンテンスケースを使用します。

ボタンを参照するには、ボタンのラベルのみを使用します。ボタンを「the [label] button」として参照しないでください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Select <strong>Add Languages</strong>.</td><td style="width: 50%;">Select the <strong>Add Language</strong>s button. <br><br> Select "Add Languages".</td></tr>
</tbody>
</table>
{:/}

ラベルがコロンまたは省略記号で終わる場合は、末尾の句読点を省略します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Select <strong>Save as</strong></td><td style="width: 50%;">Select <strong>Save as…</strong></td></tr>
</tbody>
</table>
{:/}

ボタンがアイコンの場合は、ツールチップに表示されるボタンの名前を含めます。アイコン付きのボタンにツールチップが含まれていない場合は、ツールチップの追加をリクエストしてください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Select ➕ <strong>Add</strong>.</td><td style="width: 50%;">Select the ➕ icon.</td></tr>
</tbody>
</table>
{:/}

##### チェックボックス {#checkboxes}

チェックボックスに言及する際は、チェックボックスラベルに太字テキストを使用します。明確さが必要でない限り、「checkbox」という単語を含めないでください。「check/uncheck」ではなく「select/clear」を優先します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Select <strong>Send campaign to users in their local time zone</strong>.</td><td style="width: 50%;">Check <strong>Send campaign to users in their local time zone</strong>.</td></tr>
<tr><td style="width: 50%;">Clear the <strong>Exit</strong> checkbox.</td><td style="width: 50%;">Uncheck the <strong>Exit</strong> checkbox.</td></tr>
</tbody>
</table>
{:/}

##### コマンドラインのコマンドとオプション {#command-line-commands-and-options}

コマンドラインのコマンドやオプションに言及する際は、コードフォーマットを使用します。表示されている通り、または入力する必要がある通りの大文字・小文字に合わせます。

##### ダイアログボックス（モーダル） {#dialog-boxes-(modals)}

明確さが必要でない限り、ダイアログボックスを名前で参照することを避けます。代わりに、読者が何をする必要があるかを説明します。ダイアログボックスに言及する場合は、ダイアログボックスの名前に太字テキストを使用し、UI の大文字・小文字に合わせます。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Select <strong>Upload</strong> then select a file to upload.</td><td style="width: 50%;">Select <strong>Upload</strong> and use the <strong>File Upload</strong> dialog box to select a file to upload.</td></tr>
</tbody>
</table>
{:/}

##### エラーメッセージ {#error-messages}

読者が遭遇する可能性のあるエラーメッセージに言及する際は、エラーメッセージを引用符で囲みます。長いエラーメッセージの場合は、ブロック引用を使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">"Push Bounced: MismatchSenderId"</td><td style="width: 50%;"><em>Push Bounced: MismatchSenderID</em><br><br><code>Push Bounced: MismatchSenderID</code></td></tr>
</tbody>
</table>
{:/}

##### フィルターとオペレーター名 {#filter-and-operator-names}

セグメントやダッシュボードの他の領域のフィルターとオペレーターの名前に言及する際は、コードテキストを使用します。`OR` や `AND` オペレーターなど、すべて大文字の要素を含め、UI の大文字・小文字に合わせます。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Select the <code>First Used App</code> filter and…</td><td style="width: 50%;">Select the <strong>First Used App</strong> filter and…</td></tr>
<tr><td style="width: 50%;">Combine filters with the <code>OR</code> operator.</td><td style="width: 50%;">Combine filters with the "OR" operator.</td></tr>
</tbody>
</table>
{:/}

##### フォルダーとファイル名 {#folder-and-filenames}

フォルダー名とファイル名に言及する際は、コードテキストを使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Open the <code>braze.xml</code> file.</td><td style="width: 50%;">Open the <strong>braze.xml</strong> file.</td></tr>
</tbody>
</table>
{:/}

##### キー名と組み合わせ {#key-names-and-combinations}

キー名やキーの組み合わせに言及する際は、[HTML `<kbd>` タグ](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd)を使用します。これは、キーボード、音声入力、その他のテキスト入力デバイスからのテキストユーザー入力を示します。カスタム HTML をサポートしないエディターで作業している場合は、代わりに[コードテキスト](#code-in-text)を使用します。

Command、Control、Option、Shift などのキーの名前はスペルアウトします。これらのキーにシンボルを使用しないでください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Press <strong>Option</strong>.</td><td style="width: 50%;">Press ⌥.</td></tr>
</tbody>
</table>
{:/}

キーの組み合わせには、キーの間にプラス（+）記号を使用しますが、特別なフォーマットからプラスを省略します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Press <strong>Option + F12</strong>.</td><td style="width: 50%;">Press ⌥ + F12.</td></tr>
</tbody>
</table>
{:/}

たとえば、Braze ドキュメントではキーボードタグは以下のように表示されます：
コマンドを停止するには、**Control + C** を押します。

##### メトリクス {#metrics}

テーブルや用語集エントリでメトリクスに言及する際は、特別なフォーマットなしでイニシャルキャップを使用します。文中でメトリクスに言及する際は、イニシャルキャップとイタリック体を使用します（*Machine Opens* など）。

##### ページ

一般的なウェブページ、または Braze ダッシュボードの特定のページに言及する際は、「page」という用語を使用します。ページ名に言及する際は、「the [label] page」のフォーマットを使用し、ページの名前を太字にします。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Go to the Segments page.</td><td style="width: 50%;">Go to the "Segments" page.</td></tr>
</tbody>
</table>
{:/}

##### 権限名 {#permission-names}

ダッシュボード内のユーザー権限の名前に言及する際は、権限名を引用符で囲みます。

{% alert note %}

現在、ダッシュボードのフォーマットに合わせてタイトルケースを使用しています。UI 内の権限名を、私たちの基準に合わせてセンテンスケースに更新する計画があります。

{% endalert %}

##### タブ {#tabs-1}

タブに言及する際は、「the [label] tab」のフォーマットを使用し、タブの名前を太字にします。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Go to the <strong>Manage Settings</strong> page and select the <strong>Tags</strong> tab.</td><td style="width: 50%;">Go to the "Manage Settings" page and select the "Tags" tab.</td></tr>
</tbody>
</table>
{:/}

##### テキスト入力 {#text-input}

読者に特定の文字列を入力するよう指示する際は、テキストを引用符で囲みます。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">In the <strong>Name</strong> field, enter "Lapsing Users"</td><td style="width: 50%;">In the <strong>Name</strong> field, enter <code>Lapsing Users</code>.</td></tr>
</tbody>
</table>
{:/}

#### よくある質問（FAQ） {#frequently-asked-questions-faqs}

FAQ は、人々が最も知りたい、または知る必要がある情報から始めて順序付けし、複数のカテゴリがある場合は問題カテゴリごとに整理します。

各 FAQ について、まず質問に直接回答し、その後詳細に入ります。一般的な検索クエリやユーザーの語彙に一致する実際の質問を使用します。これにより、FAQ の検索性が向上します。関連記事、サポートへの連絡方法、教材（ハウツーガイド、チュートリアルなど）など、ユーザーが役立つと思われるリソースへのリンクを含めます。

#### 地理 {#geography}

##### 都市

コピーの最初の言及ではすべての都市名をスペルアウトします。その後は、NYC や LA のようなよく知られた都市名を略しても問題ありません。

**最初の言及：** San Francisco
**2回目の言及：** SF

London や Tokyo のようなよく知られた都市の場合は、州、県、国をコンマで続けずに紹介しても問題ありません。

オーディエンスにとって馴染みのない都市や町の場合は、州、県、国を含めます。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Biloxi, Mississippi</td></tr>
<tr><td style="width: 100%;">New Bedford, MA</td></tr>
<tr><td style="width: 100%;">Antwerp, Belgium</td></tr>
</tbody>
</table>
{:/}

##### 国

すべての国名を大文字にします。国名を略す場合は、最初の言及でフルスペルを記載し、以降はイニシャルを使用します。

**最初の言及：** United States
**2回目の言及：** US

略された国名の間にピリオドを入れないでください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">UK</td><td style="width: 50%;">U.K.</td></tr>
<tr><td style="width: 50%;">Washington, DC</td><td style="width: 50%;">Washington, D.C.</td></tr>
</tbody>
</table>
{:/}

##### 地域

地域とそれを修飾する方角の両方を大文字にします。

**例：** Northern California, Eastern Europe

特定の地域や場所を表す固有名詞を大文字にします。

**例：** West Midlands, South America, South Chicago

##### 州と県

すべての州と県を大文字にします。

**例：** New York, Quebec

#### 見出しとタイトル {#headings-and-titles}

記事の見出しとタイトルには、センテンスケースの大文字化を使用します。見出しとタイトルを書く際は説明的にし、記事タイプに基づいてコンテンツの主な目的に焦点を当てます。「and」の代わりにアンパサンドを使用しないでください。

記事タイトルについては、可能な限り動名詞（*-ing* で終わる動詞）ではなく命令形の動詞を優先します。記事タイトルは簡潔に保ち、コンテンツに適切であることを確認します。たとえば、SMS メッセージに関するリファレンス記事のタイトルは「About SMS」とすることができます。

記事の見出しについては、見出しタイトル全体で簡潔かつ一貫性を保ちます。たとえば、記事の Heading 1 スタイルが各ステップを定義する場合（例：**Step 1: Create a new push campaign**）、記事の見出し全体でこのフォーマットを一貫して維持します。

Braze Docs でのスタイリングのヘルプについては、Contributing ページの [Styling examples]({{site.baseurl}}/contributing/styling_examples/?tab=markdown) を参照してください。

##### 数字付きサブタスク

順序付きステップを説明するヘッダーには、サブタスクヘッダーに数字を使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Step 2: Create an SMS campaign <br><br> Step 2.1: Compose your message <br><br> Step 2.2: Schedule the delivery</td><td style="width: 50%;">Step 2: Create an SMS campaign <br><br> Step 2a: Compose your message <br><br> Step 2b: Schedule the delivery</td></tr>
</tbody>
</table>
{:/}

#### 導入文 {#introductions}

導入文は、ユーザーが以下を確認するためのクイックチェックとして機能します：

* 正しいドキュメントにいるか？これは自分に関連があるか？
* このドキュメントを読む時間を投資すれば何を学べるか？
* SMS、メール、IAM などの明確な統合またはセットアップジャーニーに従っていると感じるか（次にどのドキュメントに行くべきかを明示していなくても）？

以下は導入文の一般的なガイドラインです。よりニッチなユースケースについては、セクション固有のガイドラインを参照してください。

* 導入文は1〜5文の範囲で記述できます
* 導入文はドキュメントのコンテンツの概要を提供するか、トピックの導入となるべきです
* ブロック引用を使用します
* 導入文は記事の H1 ヘッダーの下に配置します

##### パートナー

パートナーの概要と簡潔な会社説明を含めます。また、パートナーサイトへのリンクも含めます。

##### API

導入文には「Use this endpoint...」の文のみを含めます。API エンドポイントをできるだけナビゲートしやすく保ちたいと考えています。API エンドポイントの構造とフォーマットについて詳しくは、[API エンドポイントドキュメントガイドライン]({{site.baseurl}}/contributing/style_guide/api_endpoint_guidelines/)を参照してください。

##### ユーザーガイドと開発者ガイド

導入段落は、以下の2つの方法のいずれかで書く必要があります：

1. トピックの導入段落またはオープナーとして
2. 記事の内容の説明として。これは多くの場合「This reference article....」のようになります。

ユーザーガイドと開発者ガイドのステップでは、ユーザーはカスタマージャーニー全体を通じてナビゲーションからの手がかりに大きく依存していますが、冗長な場合もありますが、ドキュメントの価値を冒頭で明示的に述べることが役立ちます。

たとえば、ユーザーが開発者ガイドを通じて Unity を統合している場合、「Integration」というタイトルのこのページは、導入文を含めなければ十分な情報とは言えません。

#### リスト {#lists}

リストは、関連する情報をフォーマットするのに最適です。1つの項目のみを表示するためにリストを使用しないでください。単一の項目を周囲のテキストから区別したい場合は、他のフォーマットを使用してください。

リストには、箇条書き、文字付き、番号付きの3種類があります。コロンまたはピリオドで終わる導入の完全な文を含めます。

* 箇条書きリストは、特定の順序である必要のない情報を整理します。
* 文字付きリストは、相互に排他的なオプションを定義するために使用されます。
* 番号付きリストは、順序付きステップのシーケンスを示します。

可能であれば、すべてのリスト項目に同じ構文を使用します。

リスト項目の大文字化については、各リスト項目を大文字で始めます。リスト項目の末尾の句読点については、以下のシナリオでは末尾の句読点を使用しないでください：

* リスト項目が単一の単語または不完全な文の場合
* リスト項目に動詞が含まれていない場合
* リスト項目がコードフォントの場合
* リスト項目がリンクまたはドキュメントタイトルの場合

#### メディアフォーマット {#media-formatting}

このセクションには、コンテンツ内の画像と GIF のフォーマットに関する一般的なガイドラインが含まれています。スクリーンショットの例を含む詳細については、[画像コピースタイルガイド]({{site.baseurl}}/contributing/style_guide/image_style_guide/)を参照してください。

| **推奨** | {::nomarkdown}<ul><li>言及する機能やコンポーネントにタイトにクロップします。</li><li>高品質のスクリーンショットを撮ります。できればレティナモニター（MacBook ディスプレイ）で撮影します。</li><li>インタラクションやワークフローの GIF を作成します。</li><li>ユーザーは GIF を一時停止したりスクラブしたりして詳細を確認できないことに留意してください。</li><li>画像をオプティマイザー（ImageOptim、TinyPNG、Ezgif）で処理してファイルサイズを削減します。</li><li>アクセシビリティのために要素間のコントラストを高くすることを目指します。</li><li>個別のピクセル値ではなく、高さのパーセンテージで画像をリサイズします。</li></ul>{:/} |
| **非推奨** | {::nomarkdown}<ul><li>ダッシュボードのヘッダーやサイドバーを含めないでください。これらは簡単な文で説明できます。</li><li>ダッシュボード全体を含めないでください。</li><li>個人を特定できる情報を含めないでください（ぼかしている場合やデモユーザーの場合を除く）。</li><li>ブラウザフレーム（URL フィールド、ブックマーク、タブなど）を含めないでください。</li><li>テクノロジーパートナーのダッシュボードを含めないでください。</li><li>画像にボーダーやドロップシャドウを追加しないでください。</li></ul>{:/} |

#### 数字 {#numbers}

数字で文を始めないでください。例外は年を参照する場合です（例：「2019 was one for the books」）。

9までの数字はスペルアウトします。測定単位や10以上の数字には数字を使用します。3桁を超える数字にはコンマを使用します。大きな数字は書き出します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">1,000</td><td style="width: 50%;">1000</td></tr>
<tr><td style="width: 50%;">200,000</td><td style="width: 50%;">200000</td></tr>
<tr><td style="width: 50%;">1,000,000</td><td style="width: 50%;">1000000</td></tr>
<tr><td style="width: 50%;">9 billion</td><td style="width: 50%;">9000000000</td></tr>
<tr><td style="width: 50%;">5 MB</td><td style="width: 50%;">five MB</td></tr>
</tbody>
</table>
{:/}

##### 通貨

通貨記号を金額の前に使用するか、スペルアウト（pesos、euros、pounds など）して、常にどの通貨を指しているかを示します。

セントの数がゼロより大きい金額には小数を使用します。3桁を超える金額にはコンマを使用します。金額に「.00」を含めないでください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">US $20</td><td style="width: 50%;">$20</td></tr>
</tbody>
</table>
{:/}

##### 電話番号

電話番号を参照する際は、数字の間にハイフンを入れます。市外局番をかっこ内に入れないでください。

国コード付きの電話番号をフォーマットする際は、国コードの前にプラス記号（+）を使用し、市外局番をかっこ内に入れます。

国コード付きの番号は以下のように提供します：+1 (504) 327-7269

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">123-456-7890</td><td style="width: 50%;">(123)-456-7890</td></tr>
<tr><td style="width: 50%;">+1 (123) 456-7890</td><td style="width: 50%;">1 234-567-9012</td></tr>
</tbody>
</table>
{:/}

##### 分数

分数はスペルアウトし、分子と分母の間にハイフンを使用します。スラッシュで区切った数字を使用しないでください。

分数を小数で表す必要がある場合は、1未満の分数には小数点の前にゼロを追加します。

評価システムを分数で表す場合は、数字を使用してランキングをスペルアウトします。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">0.5</td><td style="width: 50%;">1/2</td></tr>
<tr><td style="width: 50%;">one-third</td><td style="width: 50%;">one third</td></tr>
<tr><td style="width: 50%;">9 out of 10</td><td style="width: 50%;">nine out of ten</td></tr>
</tbody>
</table>
{:/}

##### パーセンテージ

数字とパーセント記号（%）の間にスペースを入れずに使用します。ただし、パーセントが文の先頭にある場合は、パーセンテージ全体（数字とパーセント）をスペルアウトします。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">10%</td><td style="width: 50%;">10 %</td></tr>
<tr><td style="width: 50%;">Twenty percent of company users are...</td><td style="width: 50%;">20% of company users are...</td></tr>
</tbody>
</table>
{:/}

##### 範囲

数字の範囲を示すにはハイフンを使用します。範囲内の数字を区切るために en ダッシュを使用しないでください。

単位付きの数字の範囲については、数字の後に測定単位を繰り返します。これには名詞の繰り返しは含まれません。混乱を避けるために、範囲内の数字の間に「to」という単語を使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">5 to 100</td><td style="width: 50%;">5–100</td></tr>
<tr><td style="width: 50%;">-10°C to 50°C</td><td style="width: 50%;">-10°C-50°C Don't</td></tr>
</tbody>
</table>
{:/}

#### プレースホルダーテキスト {#placeholder-text}

プレースホルダーテキストは、読者が関連する値を提供すべき場所を示すために使用します。プレースホルダーテキストは、表現されているコンテンツを示す必要があります。たとえば、*YOUR_API_KEY* は読者の API キーを示します。

##### プレースホルダーの書き方

プレースホルダーテキストを作成する際は、以下のガイドラインを参照してください：

| ガイドライン | 例 |
| :---- | :---- |
| 大文字を使用し、単語をアンダースコア（_）で区切ります。 | `PLACEHOLDER_VARIABLE` |
| インラインプレースホルダーテキストにはイタリック体を使用します。 | *`PLACEHOLDER_VARIABLE`* |
| API コードブロックのプレースホルダーテキスト（イタリック体を使用できない場合）には、プレースホルダーを波かっこ（{}）で囲みます。 | `<string name="com_appboy_api_key">{YOUR_APP_IDENTIFIER_API_KEY}</string>` |
| Liquid コードブロックのプレースホルダーテキスト（イタリック体を使用できない場合）には、大文字を使用します。 | `{% raw %}{%- connected_content YOUR-API-URL :save items -%}{% endraw %}` |
| 簡潔さのために明確さを犠牲にしないでください。プレースホルダーを表すために必要な数の単語を使用します。 | **推奨：** `CAMPAIGN_NAME` <br> **非推奨：** _`NAME`_|

##### プレースホルダーの使用

プレースホルダーを紹介または説明する際は、以下のガイドラインを参照してください：

| ガイドライン | 例 |
| :---- | :---- |
| プレースホルダーの直後にプレースホルダーを説明します。 | Replace `<YOUR_APP_IDENTIFIER_API_KEY>` with your [App Identifier API Key]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key), which you can find on the **Settings** page. |
| 2つ以上のプレースホルダーを一度に説明するには、箇条書きリストを使用します。各プレースホルダーをコード内に表示される順序でリストします。 | Replace the following: {::nomarkdown}<ul><li><code>PLACEHOLDER_VARIABLE</code>: a description of what the placeholder represents</li><li><code>PLACEHOLDER_VARIABLE</code>: a description of what the placeholder represents</li></ul>{:/} |
| テキストまたはコードに表示されているのと同じフォーマットでプレースホルダーを参照します。 | `target <YOUR_APP_TARGET> do pod 'Appboy-iOS-SDK' end` <br><br> Replace `<YOUR_APP_TARGET>` with the name of your target app. |

#### 製品 {#products}

Braze とその機能に言及する際は、完全な製品名と機能名を使用し、UI に従って大文字にします。テンプレートや一般的な機能は大文字にしないでください。製品名とそのスペルのリストについては、[用語集](#glossary)を参照してください。

以下のケースを除き、製品名や機能名を略さないでください：

* UI に合わせるため
* 限られたスペースの制約を満たすため

製品名や機能名を動詞として使用しないでください。

Braze の後にアポストロフィを使用しないでください（例：「Braze's」）。不自然に聞こえます。代わりに、前置詞（「to, of, from」）の後に会社名を続けて所有格を形成します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">The newest product update from Braze</td><td style="width: 50%;">Braze's newest product update</td></tr>
<tr><td style="width: 50%;">That's one of the defining features of Braze.</td><td style="width: 50%;">That's one of Braze's defining features</td></tr>
</tbody>
</table>
{:/}

「Braze」は「we/our/ours」として参照します。「it/its/they/their」は使用しないでください。

#### テーブル {#tables}

テーブルを使用すると、情報を整理して表示するのに役立ちます。明確で説明的なヘッダーと、それぞれの列と行に関連するデータがあることを確認してください。

テーブルの目的を説明する導入文を必ず使用します。番号付き手順の途中にテーブルを使用することを避けます。代わりに、リストの使用を検討してください。

#### 測定単位 {#units-of-measurement}

HTML と Markdown では、測定単位を指定する際に数字と単位の間にノーブレークスペース（&nbsp）を使用します。これには、距離、ピクセル、ポイント、重量、温度の度数（度と測定単位の間）などのほとんどの測定単位が含まれます。

通貨、パーセント、角度の度数については、数字と単位の間にスペースを入れないでください。

単位付きの数字の範囲については、各数字に対して単位を繰り返します。同様に、レートについては、スラッシュ（/）の代わりに「per」を使用します。

### リンク {#linking}

#### クロスリファレンスリンク {#cross-reference-links}

クロスリファレンスを使用して、ユーザーを追加のリソースに案内します。Braze ドキュメントでは、他の Braze ドキュメントにリンクするためにサイトルート相対 URL を使用します（「www.braze.com/docs」を「{{site.baseurl}}」に置き換えます）。

特定のページ内で同じドキュメントへの複数のリンクを追加することを避けてください。リンク疲れを引き起こす可能性があります。別のページの特定のセクションにリンクしている場合や、リンク元のページが長い場合は、重複リンクは適度であれば問題ありません。

#### 動画の埋め込み {#embedding-videos}

画像と同様に、動画を使用して学習教材にバリエーションを作ります。ほとんどの人はメディアの組み合わせで最もよく学ぶため、動画に含めるコンテンツは記事やレッスンでもカバーされていることを確認してください。

Braze ドキュメントに動画を埋め込むには、[Embedded Video Test]({{site.baseurl}}/home/styling_test_page/#embedded-video-test) を参照してください。

#### リンクターゲットとしての見出し {#headings-as-link-targets}

Braze ドキュメントでは、見出しに対してアンカーが自動的に作成されます。ただし、以下の場合はカスタムアンカーを見出しに追加することをお勧めします：

* 自動生成されたアンカーが非常に長い場合。
* 見出しが頻繁にリンクされる可能性がある場合。カスタムアンカーを追加すると、見出しテキストが後で変更された場合にリンクが壊れる可能性が低くなります。

Braze ドキュメントで見出しにアンカーを追加するには、[Custom Anchors]({{site.baseurl}}/home/styling_test_page/#custom-header-anchor) を参照してください。

#### リンクテキスト {#link-text}

効果的なリンクテキストは、コンテンツの検索性、発見性、アクセシビリティの向上に役立ちます。

##### リンクの構造 {#structuring-links}

リンクを書く際は、以下のフォーマットのいずれかを使用します：

* リンクテキストをリンク先のタイトルまたは見出しに一致させます。
* リンク先の説明をリンクテキストとして使用します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>リンクテキストをリンク先のタイトルまたは見出しに一致させる。</em></th><th style="width: 50%;">推奨：<em>リンク先の説明をリンクテキストとして使用する。</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Get started with the Braze <a href="{{site.baseurl}}/user_guide/getting_started/web_sdk/">Web SDK</a>.</td><td style="width: 50%;">To find out your specific cluster or endpoint, <a href="{{site.baseurl}}/braze_support/">contact Support</a>.</td></tr>
<tr><td style="width: 50%;">For more information, see <a href="{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/">Aborting Liquid Messages</a>.</td><td style="width: 50%;">When in doubt, you can always <a href="{{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password">reset your password</a>.</td></tr>
</tbody>
</table>
{:/}

良いリンクテキストを作成するために、文を言い換える必要がある場合があります。

同じページのセクションにリンクする場合は、そのアクションを示す標準的なフレーズを使用します。たとえば：

* On this page, see [heading].
* In this document, refer to [heading].
* For more information, refer to the section [heading].

##### リンクの書き方 {#writing-links}

リンクテキストを書く際は、以下のガイドラインを適用してください：

* 関連するキーワードにリンクを配置します。
* 読者を別の記事に参照する完全な文を書いている場合は、「For more information, see」または「For more information about [topic], see」というフレーズを使用します。
* ヘルプテキストが複数の概念を扱っており、それぞれが独自のヘルプドキュメントにリンクできる場合にのみ、「Learn more…」の文を追加します。この場合、最も適切なリンクを選び、「Learn more…」でコンテキストを提供します。
* カジュアルなトーンを保つために、リンクテキストの紹介に「please」を使用しないでください。たとえば、「Please refer to」、「Please see」、「Please contact」というフレーズを避けます。
* 周囲のテキストなしでも意味が通じる、ユニークで説明的なリンクテキストを書きます。[Nielsen Norman Group](https://www.nngroup.com/articles/link-promise/#links-should-stand-alone)（NN/g）の調査によると、読者はページ上の目立つ情報をスキャンするため、リンクが単独で意味をなすようにしてください。
* リンクテキストに以下の単語やフレーズを使用しないでください。アクセシビリティとスキャン性に悪影響を及ぼします。
 * Learn more（単独で）
 * Click here
 * here
 * this document
 * this article

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>周囲のテキストなしでもリンクテキストが意味をなすようにする</em></th><th style="width: 50%;">非推奨：<em>曖昧または説明的でないリンクテキストを使用する</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">For more information on importing customer data, see <a href="{{site.baseurl}}">User Import</a>.</td><td style="width: 50%;">For more information, <a href="{{site.baseurl}}">click here</a>.</td></tr>
<tr><td style="width: 50%;">This feature connects to the <a href="{{site.baseurl}}">Track users</a> endpoint.</td><td style="width: 50%;">See <a href="{{site.baseurl}}">this article</a>.</td></tr>
<tr><td style="width: 50%;">Learn more about <a href="{{site.baseurl}}">what's new in Android SDK 16.0.0</a>.</td><td style="width: 50%;">Follow the instructions <a href="{{site.baseurl}}">here</a>.</td></tr>
<tr><td style="width: 50%;">Learn more about the <a href="https://www.braze.com/product">Braze platform</a>.</td><td style="width: 50%;">For steps, refer to <a href="{{site.baseurl}}">this document</a>. <a href="{{site.baseurl}}">Learn more</a>.</td></tr>
<tr><td style="width: 50%;">Storefront API keys are unique per Hydrogen storefront, but their permission scopes are shared by all Hydrogen storefronts. Learn more about <a href="{{site.baseurl}}">Storefront API tokens.</a></td><td style="width: 50%;"><a href="{{site.baseurl}}">Storefront API tokens</a> are unique per <a href="{{site.baseurl}}">Hydrogen storefront</a>, but their <a href="{{site.baseurl}}">permission scopes</a> are shared across all Hydrogen storefronts.</td></tr>
</tbody>
</table>
{:/}

#### エンドポイントへのリンク {#links-for-endpoints}

エンドポイントの記事を参照する際は、コンテキスト外でも意味が通じる[意味のあるリンクテキスト](https://docs.google.com/document/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.79ujl0qtumog)を使用してください。エンドポイントのパスをリンクとして使用する場合は、パスがエンドポイントの機能を明確に伝えない可能性があるため、周囲のテキストで詳細を提供してください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨</th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Delete user profiles using the Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user endpoint</a>.</td><td style="width: 50%;">Delete user profiles using the Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user</a> endpoint.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code> endpoint</a></td><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a> endpoint</td></tr>
</tbody>
</table>
{:/}

#### ファイルダウンロード用のリンク {#links-for-file-download}

リンクがファイルをダウンロードする場合は、リンクテキストでそれを明確にし、ファイルタイプを記載します。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">推奨：<em>リンクテキストが選択するとファイルがダウンロードされることを伝えるようにする</em></th><th style="width: 50%;">非推奨</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">For tips, download the <a href="{{site.baseurl}}">Regex Cheat Sheet PDF</a>.</td><td style="width: 50%;">Check out our <a href="{{site.baseurl}}">RegEx Cheat Sheet</a>.</td></tr>
<tr><td style="width: 50%;">For more information, download the <a href="{{site.baseurl}}">Success and Support Services Handbook PDF</a>.</td><td style="width: 50%;"><a href="{{site.baseurl}}">Success and Support Services Handbook</a></td></tr>
</tbody>
</table>
{:/}

#### 他のサイトへのリンク {#links-to-other-sites}

一般的なルールとして、簡潔な説明でカバーできる場合は、別のサイトにリンクしないでください。別のサイトのコンテンツがいつ変更されるかを追跡することはできません。

外部サイトにリンクする場合は、リンク先のサイトが高品質で、信頼性があり、評判の良いものであることを確認してください。可能であれば、ページ上の最も関連性の高い見出しにリンクします。

外部リンクアイコンを使用して、リンクが別のドメインに移動することを示します。Braze ドキュメントでは、これは外部リンクに自動的に適用されます。

#### 画像の URL {#urls-for-images}

Braze ドキュメントでは、画像にリンクするためにサイトルート相対 URL を使用します。詳しくは、[Adding and Editing Images](https://github.com/braze-inc/braze-docs/wiki/Editing-Content#adding-and-editing-images) を参照してください。

### 用語集 {#glossary}

⚠️ = 注意して使用、関連する注記を参照
⛔️ = 使用しない

#### 数字

**24/7**
名詞の前の修飾語として使用する場合のみハイフンでつなぎます（24-7）。

**2D / two-dimensional**

**3D / three-dimensional**

#### A

**A/B testing**

⚠️ **abort**
特定の名前のプロセスを参照する場合を除き、使用を避けてください。代わりに、「stop」、「exit」、「cancel」、「end」などの単語を使用します。

**action buttons**

**action-based delivery**
大文字の UI 要素を参照する場合を除き、小文字。

⛔️ **ad hoc**
使用しないでください。「one-time」または類似の表現を使用します。

**AI**
最初の言及の後は「artificial intelligence」よりも優先されます。

**AI item recommendation**

**Alloys / Braze Alloys**
常に大文字。

**alphanumeric**
ハイフンなし。

**always-on**

**am**
時刻に使用する場合は小文字（例：「10 am」）。[pm](#glossary) も参照。

**Amazon S3**

**Amazon Web Services (AWS)**
常に大文字。最初の言及でスペルアウトし、その後は略語を使用して問題ありません。

**AMP for Email / Braze AMP for Email**

**Android**

**API / Application Programming Interface**
最初の言及でスペルアウトし、その後は略語を使用して問題ありません。

**API key**

**APNs / Apple Push Notification service**

**⛔️ app group**
使用しないでください。App group はワークスペースに名前が変更されました。

**Apple iOS platform**

**AppleWatch**

**.avro**

#### B

**behavior, behaviors**

**Benchmarks**

**beta**

**BI Insights**

**bingeing**

**Binge-watch**

**Bonfire / Bonfire community / Braze Bonfire community**
最初の言及では「Braze Bonfire community」を使用し、その後は「Bonfire」または「Bonfire community」のみで問題ありません。

**boolean**

⛔️ **blacklist**
使用しないでください。代わりに「blocklist」または「denylist」を使用します。これらの単語の動詞形については、問題のある用語を削除するように文を書き直すことを検討してください。たとえば：

>✅ **推奨：** To block an existing property from being used in new messages, select **Manage Properties**. <br>
>⛔️ **非推奨：** To blocklist an existing property, select **Manage Properties**.

**Braze-to-Braze webhook**

**Business Intelligence (BI)**
最初の言及でスペルアウトし、その後は略語を使用して問題ありません。

#### C

**California Consumer Privacy Act (CCPA)**
最初の言及でスペルアウトし、その後は略語を使用して問題ありません。[CCPA compliance (noun) / CCPA-compliant (adjective)](#ccpa-compliance) も参照。

**can**
オプションのアクションまたは結果を参照するために「can」を使用します。たとえば：

> ✅ **推奨：** You can also upload and update user profiles with CSV files.
> ✅ **推奨：** The import process can take a few minutes.

指示に「can」を使用しないでください。代わりに、命令形の動詞を優先します。例については、[二人称と一人称](#second-person-and-first-person)を参照してください。

**Canvas**
常に大文字。複数形は「Canvases」。

**Canvas Flow**
オリジナルの Canvas エディターと Canvas Flow を区別する場合に使用します。それ以外の場合は「Canvas」を使用します。

**campaign**
大文字の UI 要素を参照する場合を除き、小文字。

**capacity**
「limit」の代わりに、カスタムデータの制限に言及する際に使用します。

**catalog**
大文字の UI 要素を参照する場合を除き、小文字。

**CCPA compliance (noun) / CCPA-compliant (adjective)** {#ccpa-compliance}

**CEO, CFO, CMO, COO, CTO**

**churn**
顧客の離脱や損失を指すために使用します。

**churn prediction**
UI を参照する場合を除き、小文字。

**checkbox**

**Check-in (noun) / check in (verb)**

**City x City**

**Cofounder**

**Content Cards / Braze Content Cards**

**Content Blocks**

**control group**

**conversion**

**conversion group analysis**
小文字。

**Cordova**

**Currents / Braze Currents**
常に大文字。

**CRM / customer relationship management**
最初の言及でスペルアウトし、その後は略語を使用して問題ありません。

**cross-channel messaging / cross-channel personalization**

**C-suite**

**CSV / comma-separated values**

**custom attributes**
大文字の UI 要素を参照する場合を除き、小文字。

**custom events**
大文字の UI 要素を参照する場合を除き、小文字。

**customer attributes**

**customer behavior**

**customer data platform (CDP)**
小文字。

**customer engagement**

**customer events**

**customer journey**

**customer permissions**

**customer retention**

#### D

**Dark Mode theme / Dark Mode Preview / dark mode concept**

**dashboard / Braze dashboard**
プラットフォームとしての Braze を指すために使用します。小文字を使用します（Dashboard ではなく dashboard）。

**data-driven (adjective)**

**data privacy**

**data sheet**

**data streaming**

**DAU / Daily Active Users**

**Decision Splits**

**deep linking**

**Delay Messages**

**Downtime**

**drag and drop (verb) / drag-and-drop (adjective)** {#drag-and-drop}
ファイルをアップロードゾーンにドラッグする場合に使用します。

**Drag-And-Drop Editor**
UI の機能を参照する場合はタイトルケースを使用します。それ以外の場合は小文字（drag-and-drop editor）を使用します。顧客がエディターで要素を[ドラッグ＆ドロップ](#drag-and-drop)する方法を参照する場合は動詞を使用します。

**drill down (verb) / drilldown (noun or adjective)**
データとそこから生成されるレポートに関するコンテンツで使用します。

**DTC / direct to consumer**

**dynamic content**

#### E

**early access**

⛔️ **e.g.**
使用しないでください。「for example,」、「such as」、「like」、または類似のフレーズを使用します。

**eBook**

**eCommerce**
「ecommerce」や「e-commerce」ではありません。

**ecosystem**

**email**
「Email」や「e-mail」ではありません。

**email deliverability**

**email reputation**

**EMEA (Europe, Middle East, and Asia)**

**emoji**
単数形と複数形が同じ。

**end user (noun) / end-user (adjective)**
「end users」よりも「your users」を優先します。

⚠️ **ensure**
機能が何をするかについて話す際は使用を避けてください。詳しくは、[保証を避ける](#avoid-guarantees)を参照してください。

**ESP / email service provider**

**event prediction**

**event properties / custom event properties**
大文字の UI 要素を参照する場合を除き、小文字。

**exception events**

**extract**
圧縮フォルダーからファイルを抽出することを指すには、「unzip」の代わりに「extract」を使用します。

**external ID**
「External ID」ではありません。コードスニペットを参照する場合は、external_id を使用します。

#### F

**Facebook**

**FCM / Firebase Cloud Messaging**

**Firebrand / Firebrands**

**Forge [YEAR]**

**frequency capping**

**Fullscreen**
形容詞として使用する場合（例：「Fullscreen in-app messages」）、ハイフンなしで表記します。

#### G

**GDPR / General Data Protection Regulation**
最初の言及でスペルアウトし、その後は略語を使用して問題ありません。

**GDPR compliance (noun) / GDPR-compliant (adjective)**

**geofence**

**GIF**

**GitHub**
「Github」や「github」ではありません。

**Google / google-able**

#### H

**High-performance**

**High-Value Actions**

**HQ / headquarters**

**HTML Email Editor**

**HTTP**

#### I

⛔️ **i.e.**
使用しないでください。「that is」または類似のフレーズを使用します。

**in-app messages**

**in-browser message (IBM)**

**infographic**

**install attribution**

**integer**

**Intelligence Suite**
タイトルケースを使用します。

**Intelligent Channel**
タイトルケースを使用します。

**Intelligent Selection**
タイトルケースを使用します。

**Intelligent Timing**
タイトルケースを使用します。

⛔️ **Internet of things**
使用しないでください。

**iOS**

**IP warming**

**iPad**

**iPhone**

**IT**

#### J

**JavaScript**

**JPEG / JPG**

**JSON / JavaScript Object Notation**

#### K

**Keynote (program) / keynote (noun)**

**kick off (verb) / kickoff (noun)**

⚠️ **kill**
特定の名前のプロセスを参照する場合を除き、使用を避けてください。代わりに、「stop」、「exit」、「cancel」、「end」などの単語を使用します。

**KPI / key performance indicator**

#### L

**landing page**

**lifecycle**

**Lift-rate**

**LinkedIn**

**Liquid**
常に大文字。

**Live Preview**

**long term (noun) / long-term (adjective)**

**LTV / Lifetime Value**

#### M

**marketing technology**
「martech」よりも優先されます。

**MAU / Monthly Active Users**

**maximum**
「max」ではありません。

**media library**
大文字の UI 要素を参照する場合を除き、小文字。

**Microsoft**

**Microsoft Azure**

**ML / machine learning**

**mobile marketing**

**mobile marketing automation**

**mobile moment**

**mobile phone**

**multichannel campaign**
大文字の UI 要素を参照する場合を除き、小文字。ハイフンなし。

**multi-language support**

**multivariate testing**

#### N

**N/A**
「NA」ではありません。テーブルで、特定のセルに該当しない列または行のコンテンツを示すために必要に応じて「N/A」を使用します。インラインテキストでは、明確さのためにスペルアウトした「not available」または「not applicable」を優先します。

⚠️ **new**
製品ドキュメントや学習教材での使用を避けてください。コンテンツがすぐに古くなる可能性があります。詳しくは、[将来の機能](#describing-limitations)を参照してください。

**NRT / near real-time (adjective) / near real time (noun)**

**NYC / New York City**

#### O

**on demand**

**onboarding**

**once**
アクションを1回実行することを指すために使用します。「after」や「when」の代わりに「once」を使用しないでください。

**open rate (OR)**

**opt-in prompt**

**orchestration**

**OS / Operating System**

**OTT / Over-the-top media services**

⛔️ **out-of-the-box**
使用しないでください。代わりに「default」のような代替を使用します。

#### P

**partner, partners, partnership**

**persona (singular) / personas (plural)**

**personalization**

**personally identifiable information (PII)**

**Personalized Path**
タイトルケースを使用します。

**Personalized Variant**
タイトルケースを使用します。

**PhD / PhDs**

**pm**
時刻に使用する場合は小文字（例：「10 pm」）。[am](#glossary) も参照。

**preceding**

**prediction**
「Braze」が先行する場合を除き、小文字。たとえば「A Braze Prediction is…」。

**predictive analytics**

**Predictive Churn**
タイトルケースを使用します。Predictive Churn は製品名であり、顧客は[解約予測](#glossary)を作成します。

**Predictive Events**
タイトルケースを使用します。

**Predictive Purchases**
タイトルケースを使用します。Predictive Purchases は製品名であり、顧客は[購入予測](#glossary)を作成します。

**Predictive Suite**
タイトルケースを使用します。

**preference center**
大文字の UI 要素を参照する場合を除き、小文字。

**priming for location**

**priming for push**

**promotion code**
大文字の UI 要素を参照する場合を除き、小文字。「promo code」は使用しないでください。

**purchase prediction**
大文字の UI 要素を参照する場合を除き、小文字。

**purchase properties**
大文字の UI 要素を参照する場合を除き、小文字。

**push action buttons**

**Push Max**
タイトルケースを使用します。

**push notification**

**Push Stories**
タイトルケースを使用します。

#### Q

**Q&A**

⛔️ **QA (quality assurance)**
略語を動詞として使用しないでください。代わりに「perform quality assurance」と書き直します。

**quiet hours**
文頭では「Quiet hours」、文中では「quiet hours」を使用します。ブランド機能ではないため、タイトルケース「Quiet Hours」は使用しないでください。

⚠️ **quick / quickly**
使用を避けてください。あなたにとって速いことが、他の人にとっても速いとは限りません。関連するガイドラインについては、[見下すような言葉遣い](#condescending-language)を参照してください。

#### R

**rate limiting**

**real time (noun) / real-time (adjective)**

**re-engagement**

⚠️ **regular expression / regex**
略語の「regex」よりもスペルアウトした版を優先します。「RegEx」は使用しないでください。

**relationship marketing**

**retargeting**

**retention**

**rich push**

**right-click**

**right-swipe**

**ROI / return on investment**

#### S

**Sage AI by Braze™**

⛔️ **sanity check**
使用しないでください。代わりに「quick check」や「preliminary check」のような用語を使用します。あるいは、「Let's check to make sure everything is working」のようなフレーズでチェックイン指示を導入します。

**scheduled delivery**
大文字の UI 要素を参照する場合を除き、小文字。

**screencap**

**screengrab**

**SDK / Software Developer Kit**

**segment (audience)**

**Segment Extensions**
タイトルケースを使用します。

**Segment Insights**
タイトルケースを使用します。

**Segmentation**

**selection**
カタログ内の機能として。大文字の UI 要素を参照する場合を除き、小文字。

**SF / San Francisco**

**Silicon Valley**

**silo, silos, siloed**

**simple survey**

**slideshow**

**Smartphone**

**Smartwatch**

**SMS**

**software as a service (SaaS)**
最初の言及でスペルアウトし、その後は略語を使用して問題ありません。

**spam testing**

**SQL / structured query language**

**SQL Segment Extensions**
タイトルケースを使用します。

**stickiness**

**streaming**

**string**
非技術的なオーディエンスの場合は、文字列を「alphanumeric characters」を含むテキストとして定義します。技術的なオーディエンスの場合は、この用語を定義しなくても問題ありません。

**subscription group**

**sunset, sunsetting**

#### T

**targeted response**

⚠️ **terminate**
特定の名前のプロセスを参照する場合を除き、使用を避けてください。代わりに、「stop」、「exit」、「cancel」、「end」などの単語を使用します。

**third-party**

**time zone**
「timezone」ではありません。

**timestamp**

**touchscreen**

**triggered message**

**Twitter**

#### U

**UK / United Kingdom**

⛔️ **unzip**
使用しないでください。代わりに「extract」を使用します。

**URL**
個々の文字 U-R-L として発音されるため、「an URL」ではなく「a URL」と書きます。すべて大文字を使用します。複数形は URLs。

**US / USA**
ピリオドなし。

**use cases**

**user attributes / default user attributes**
Braze が自動的にキャプチャするユーザーデータを指すために使用します。

**user profile**

**username**

⚠️ **utilize**
「use」を意味する場合は「utilize」を使用しないでください。「utilize」は、本来の意図された目的を超えて何かが使用されることを指すために使用します。

#### V

**variant**

⛔️ **via**
使用しないでください。代わりに「through」や「by means of」、「by way of」のようなフレーズを使用します。

⛔️ **vice versa**
使用しないでください。代わりに「conversely」や「the other way around」のようなフレーズを使用します。

**view-only**

⚠️ **vs.**
「versus」の略語として「vs.」を使用しないでください。代わりに、単語をスペルアウトします。

#### W

**web messaging**

**web push**

**webhook**

**webinar**

**whitelabel**

⛔️ **whitelist**
UI を参照する場合を除き、使用しないでください。代わりに「allowlist」または「safelist」を使用します。これらの単語の動詞形については、問題のある用語を削除するように文を書き直すことを検討してください。例については、[blacklist](#glossary) を参照してください。

⚠️ **Wi-Fi**
「WiFi」、「wi-fi」、「wifi」は使用しないでください。

**will**
「will」や「would」の使用を避けてください。[現在時制](#present-tense)を参照してください。

**Winning Path**
タイトルケースを使用します。

**Winning Variant**
タイトルケースを使用します。

⛔️ **wizard**
使用しないでください。代わりに「composer」を使用します。

**WordPress**

**workspace**

**www**

#### Y

**YAML**
ファイルタイプを参照するためにファイル拡張子を使用しないでください。たとえば、「.yaml file」ではなく「YAML file」を使用します。

**YouTube**

#### Z

**zip code**

**zip file / zipped files**

**ZIP**
ファイルタイプを参照するためにファイル拡張子を使用しないでください。たとえば、「.zip file」ではなく「ZIP file」を使用します。