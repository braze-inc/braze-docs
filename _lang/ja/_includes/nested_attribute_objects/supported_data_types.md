## サポートされるデータ型

以下のデータタイプがサポートされている：

<table>
  <thead>
    <tr>
      <th>データ型</th>
      <th>説明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>数値</td>
      <td>のような数値である。 <code>1</code> または <code>5.5</code>.</td>
    </tr>
    <tr>
      <td>string</td>
      <td>のようなテキスト値である。 <code>"Hello"</code> または <code>"The Hobbit"</code>.</td>
    </tr>
    <tr>
      <td>ブール値</td>
      <td>と評価される値。 <code>true</code> または <code>false</code>.</td>
    </tr>
    <tr>
      <td>配列</td>
      <td>のような値のリストである。 <code>["red", "blue", "green"]</code>.</td>
    </tr>
    <tr>
      <td>時刻</td>
      <td>
        日付と時刻の比較に使われるタイムスタンプ値。階層化された時間カスタム属性をフィルターする際に、選択することができる：<br><br>
        <ul>
          <li><strong>年中無休</strong>：比較のために月と日だけをチェックする。 <code>03-15</code>.</li>
          <li><strong>時間</strong>:次のように、年を含む完全なタイムスタンプを比較する。 <code>2023-03-15T12:00:00Z</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>オブジェクト</td>
      <td>キーと値のペアを持つ構造化された値。 <code>{"author": "Tolkien"}</code>.</td>
    </tr>
    <tr>
      <td>オブジェクト配列</td>
      <td>
        などのオブジェクトのリストである。 <code>[{"title": "The Hobbit"}, {"title": "Dune"}]</code>.
        詳細は以下を参照のこと。 
        <a href="{{site.baseurl}}/array_of_objects/">オブジェクトの配列</a>。
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
