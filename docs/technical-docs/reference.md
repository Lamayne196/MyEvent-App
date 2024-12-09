---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .label }
[Jane Dane]

{: .no_toc }
# Reference documentation

{: .attention }
> This page collects internal functions, routes with their functions, and APIs (if any).
> 
> See [Uber](https://developer.uber.com/docs/drivers/references/api) or [PayPal](https://developer.paypal.com/api/rest/) for exemplary high-quality API reference documentation.
>
> You may delete this `attention` box.

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Auth Routes

### `login()`

**Route:** `/login`

**Methods:** `GET` `POST`

**Purpose:**  
Verarbeitet die Login-Anfrage eines Nutzers. Überprüft, ob die eingegebene E-Mail und das Passwort mit den in der Firebase-Datenbank gespeicherten Nutzerdaten übereinstimmen. Bei erfolgreicher Anmeldung wird der Nutzer auf das Dashboard weitergeleitet, bei Fehlern wird eine Fehlermeldung angezeigt.

**Sample output:**  
- Erfolgreiche Anmeldung: Weiterleitung zum Dashboard.  
- Fehlermeldung: `Ungültige Anmeldeinformationen.`  

---

### `register()`

**Route:** `/register`

**Methods:** `GET` `POST`

**Purpose:**  
Verarbeitet die Registrierung eines neuen Nutzers. Überprüft, ob die eingegebenen Passwörter übereinstimmen und ob die E-Mail-Adresse bereits vergeben ist. Bei erfolgreicher Registrierung wird der Nutzer in Firebase gespeichert und zur Login-Seite weitergeleitet.

**Sample output:**  
- Erfolgreiche Registrierung: `Benutzer erfolgreich registriert.`  
- Fehlermeldung: `Passwörter stimmen nicht überein.` oder `Benutzername bereits vergeben.`

---

### `logout()`

**Route:** `/logout`

**Methods:** `GET`

**Purpose:**  
Verarbeitet die Abmeldung eines Nutzers. Entfernt den Nutzer aus der Sitzung (Session) und leitet ihn zurück zur Home-Seite.

**Sample output:**  
- Erfolgreiche Abmeldung: `Du hast dich erfolgreich abgemeldet.`  

---

## Additional Notes

- Die Auth-Routen sind in einer separaten `authRoute.py`-Datei definiert und in der Hauptapplikation (`app.py`) über Blueprints registriert.
- **Flask Sessions** werden verwendet, um die Benutzersitzung zu verwalten und die Anmeldeinformationen während der Sitzung zu speichern.
- **Firebase Firestore** wird verwendet, um Nutzerdaten (E-Mail und Passwort) zu speichern und zu validieren.

