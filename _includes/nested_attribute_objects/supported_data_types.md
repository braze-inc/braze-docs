## Supported data types

The following data types are supported:

<table>
  <thead>
    <tr>
      <th>Data Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Number</td>
      <td>A numeric value, such as <code>1</code> or <code>5.5</code>.</td>
    </tr>
    <tr>
      <td>String</td>
      <td>A text value, such as <code>"Hello"</code> or <code>"The Hobbit"</code>.</td>
    </tr>
    <tr>
      <td>Boolean</td>
      <td>A value that evaluates to either <code>true</code> or <code>false</code>.</td>
    </tr>
    <tr>
      <td>Array</td>
      <td>A list of values, such as <code>["red", "blue", "green"]</code>.</td>
    </tr>
    <tr>
      <td>Time</td>
      <td>
        A timestamp value used for date and time comparisons. When filtering a nested time custom attribute, you can choose:<br><br>
        <ul>
          <li><strong>Day of Year</strong>: Checks only the month and day for comparison, such as <code>03-15</code>.</li>
          <li><strong>Time</strong>: Compares the full timestamp, including the year, such as <code>2023-03-15T12:00:00Z</code>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Object</td>
      <td>A structured value with key–value pairs, such as <code>{"author": "Tolkien"}</code>.</td>
    </tr>
    <tr>
      <td>Array of objects</td>
      <td>
        A list of objects, such as <code>[{"title": "The Hobbit"}, {"title": "Dune"}]</code>. 
        For more information, refer to 
        <a href="{{site.baseurl}}/array_of_objects/">Arrays of objects</a>.
      </td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
