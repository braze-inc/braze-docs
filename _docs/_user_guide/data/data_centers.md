---
nav_title: Data Centers
article_title: Data Centers
page_order: 0.1
page_type: reference
description: "This reference article covers information about data centers, including where they're located and how to sign up for region-specific data centers."
---

# Data centers

> Braze data centers are built to provide you with options on where your users' data is processed and stored. This allows you to effectively manage your risks related to data sovereignty, flexibility, and management. When you select a Braze data center, you can be certain that our platform meets or exceeds all local requirements in data management.

## How it works

Braze operates several data centers located in different regions around the world. These data centers allow our services to be reliable and scalable. This geographical distribution helps to minimize latency, which is the time it takes for data to travel between the server and the user. 

This also means that when a user interacts with your app or website, their requests are directed to the nearest data center, optimizing performance and reducing load times. By connecting to the nearest data center, your users can experience fast load times, which is especially important for real-time messaging and user engagement.

Let's say you have a mobile app that sends push notifications to users. If a user in Melbourne receives a notification, the request to send that notification is routed to the nearest data center in Australia. In the event the mobile app experiences a surge in users during a promotional event, Braze has a scalable infrastructure with multiple data centers that can handle the increased demand.

## List of data centers

Refer to the following table for a list of available data centers.

<style>
table th:nth-child(1) {
    width: 10%;
}
table th:nth-child(2) {
    width: 33%;
}
table th:nth-child(3) {
    width: 33%;
}
table th:nth-child(4) {
    width: 24%;
}
table td {
    word-break: break-word;
}
</style>
<table>
  <thead>
    <tr>
      <th>Data center region</th>
      <th>Dashboard URL</th>
      <th>REST endpoint</th>
      <th>SDK endpoint</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Australia</b></td>
      <td><code>https://dashboard.au-01.braze.com</code></td>
      <td><code>https://rest.au-01.braze.com</code></td>
      <td><code>sdk.au-01.braze.com</code></td>
    </tr>
    <tr>
      <td><b>Europe</b></td>
      <td>
        <ul>
          <li><code>https://dashboard-01.braze.eu</code></li>
          <li><code>https://dashboard-02.braze.eu</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>https://rest.fra-01.braze.eu</code></li>
          <li><code>https://rest.fra-02.braze.eu</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>sdk.fra-01.braze.eu</code></li>
          <li><code>sdk.fra-02.braze.eu</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>US</b></td>
      <td>
        <ul>
          <li><code>https://dashboard-01.braze.com</code></li>
          <li><code>https://dashboard-02.braze.com</code></li>
          <li><code>https://dashboard-03.braze.com</code></li>
          <li><code>https://dashboard-04.braze.com</code></li>
          <li><code>https://dashboard-05.braze.com</code></li>
          <li><code>https://dashboard-06.braze.com</code></li>
          <li><code>https://dashboard-07.braze.com</code></li>
          <li><code>https://dashboard-08.braze.com</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>https://rest.iad-01.braze.com</code></li>
          <li><code>https://rest.iad-02.braze.com</code></li>
          <li><code>https://rest.iad-03.braze.com</code></li>
          <li><code>https://rest.iad-04.braze.com</code></li>
          <li><code>https://rest.iad-05.braze.com</code></li>
          <li><code>https://rest.iad-06.braze.com</code></li>
          <li><code>https://rest.iad-07.braze.com</code></li>
          <li><code>https://rest.iad-08.braze.com</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>sdk.iad-01.braze.com</code></li>
          <li><code>sdk.iad-02.braze.com</code></li>
          <li><code>sdk.iad-03.braze.com</code></li>
          <li><code>sdk.iad-04.braze.com</code></li>
          <li><code>sdk.iad-05.braze.com</code></li>
          <li><code>sdk.iad-06.braze.com</code></li>
          <li><code>sdk.iad-07.braze.com</code></li>
          <li><code>sdk.iad-08.braze.com</code></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Signing up for region-specific data centers

When you set up your Braze account, you can sign up for region-specific data centers. Contact your account manager for information and recommendations on which data centers work best for you based on your users' geographical regions.
