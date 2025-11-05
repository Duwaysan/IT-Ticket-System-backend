
---

# ⭐ **Backend README**

This repository contains the Django REST API for Wasil, an internal support ticket system used to streamline communication between employees and managers.

---

## Related Repositories
[Frontend](https://github.com/Duwaysan/IT-Ticket-System-frontend)

[Backend (This repo)](https://github.com/Duwaysan/IT-Ticket-System-backend)


## API Base URL

http://localhost:8000

## Tech Stack

- Django & Django REST Framework

- SQLite (development) / PostgreSQL (production planned)

- JWT Authentication (SimpleJWT)

- CORS-enabled API


--- 
## Entity Relationship Diagram

![ERD](./assets/ERD.png)



## Routing Table - Backend Routing


<h2>Profile</h2>
<table border="1">
    <tr><th>HTTP Verb</th>      <th>Path</th>             <th>Action</th>     <th>Description</th>                 </tr>
    <tr><td>GET</td>            <td>/login</td>         <td>show</td>      <td>log into profile</td>            </tr>
    <tr><td>POST</td>           <td>/signup</td>         <td>create</td>     <td>Create a new profile</td>         </tr>
</table>



<hr>
<br>
<br>


<h2>Ticket</h2>
<table border="1">
    <tr><th>HTTP Verb</th>      <th>Path</th>             <th>Action</th>     <th>Description</th>                 </tr>
    <tr><td>GET</td>            <td>profiles/profile_id/tickets</td>         <td>show</td>      <td>Show all ticket </td>            </tr>
    <tr><td>POST</td>           <td>profiles/profile_id/tickets</td>         <td>create</td>     <td>Create a new ticket</td>         </tr>
    <tr><td>GET</td>            <td>tickets/ticket_id</td>         <td>show</td>      <td>Show ticket detail</td>            </tr>
    <tr><td>PUT</td>            <td>/tickets/:id</td>         <td>update</td>     <td>Update a ticket</td>         </tr>
    <tr><td>DELETE</td>         <td>/tickets/:id</td>     <td>delete</td>    <td>Remove a ticket</td>            </tr>
</table>

<hr>
<br>
<br>

<h2>Message</h2>
<table border="1">
    <tr><th>HTTP Verb</th>      <th>Path</th>             <th>Action</th>     <th>Description</th>                 </tr>
    <tr><td>GET</td>            <td>/tickets/:ticket_id/messages</td>         <td>show</td>      <td>Show all messages</td>            </tr>
    <tr><td>POST</td>           <td>/tickets/:ticket_id/messages</td>         <td>create</td>     <td>Create a new message</td>         </tr>
    <tr><td>PUT</td>            <td>/tickets/:ticket_id/messages/:message_id</td>         <td>update</td>     <td>Update a message</td>         </tr>
    <tr><td>DELETE</td>         <td>/tickets/:ticket_id/messages/:message_id</td>     <td>delete</td>    <td>Remove a message</td>            </tr>
</table>

```bash
git clone https://github.com/Duwaysan/IT-Ticket-System-backend
cd IT-Ticket-System-backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## IceBox (Future Enhancements)

- AI ticket suggestions to propose solutions automatically

- Email/SMS alerts when a ticket is updated

- Ticket performance dashboard (reporting & metrics)

- File attachment support

- Multi-department workflow handling


---

