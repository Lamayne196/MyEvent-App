---
title: Design Decisions
nav_order: 3
---

{: .label }
[65Coders]

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Firebase vs. SQL Database for Data Management

### Meta

Status  
: **Entschieden**

Aktualisiert  
: 19-Nov-2024

### Problemstellung

Wir mussten entscheiden, ob wir die Daten unserer Anwendung (z. B. Events, Nutzer, RSVP-Zähler) mit Firebase Firestore oder einer SQL-Datenbank (z. B. SQLite, MySQL) verwalten.  

Die Kernanforderungen waren:  
1. Echtzeit-Datenaktualisierungen für die RSVP-Funktionalität.  
2. Skalierbarkeit, um mit wachsenden Datenmengen umgehen zu können.  
3. Eine einfache Integration mit unserem Flask-Backend.  

Zusätzlich wollten wir neue Technologien ausprobieren, da Firebase für uns neu ist. Unser Ziel war es, unser Wissen zu erweitern und praktische Erfahrungen mit modernen Technologien zu sammeln.

### Entscheidung

Wir haben uns für **Firebase Firestore** entschieden.  

Firebase überzeugt durch seine integrierten Echtzeit-Funktionen und die einfache Integration mit Flask über Bibliotheken wie `pyrebase` und `firebase-admin`. Darüber hinaus bietet Firebase integrierte Authentifizierungs- und Cloud-Storage-Dienste, wodurch der Entwicklungsaufwand reduziert wird.  

Diese Entscheidung bietet uns auch die Möglichkeit, eine neue Technologie zu erlernen und unser Wissen im Bereich moderner Datenbanken zu erweitern.  

*Entscheidung getroffen von:* Lamine Touré (Backend Lead), Veysel Sam (Frontend Lead).

### Betrachtete Optionen

Wir haben zwei Alternativen betrachtet:

+ Firebase Firestore  
+ SQL-Datenbank (SQLite oder MySQL)

| Kriterium                  | Firebase Firestore      | SQL-Datenbank         |
| -------------------------- | ----------------------- | --------------------- |
| **Echtzeit-Aktualisierungen** | ✔️ Eingebaute Unterstützung | ❌ Zusätzliche Konfiguration erforderlich |
| **Integration**            | ✔️ Einfach mit Flask-SDKs | ❌ Manuelle Einrichtung notwendig |
| **Skalierbarkeit**         | ✔️ Kein manuelles Skalieren erforderlich | ❌ Manuelles Skalieren nötig |
| **Benutzerfreundlichkeit** | ✔️ Minimaler Aufwand    | ❌ Komplexe Schema- und Migrationserstellung |
| **Kosten**                 | ❔ Kostenlose Stufe verfügbar | ✔️ Meist kostenlos mit SQLite |
| **Lernmöglichkeit**        | ✔️ Neue Technologie, die wir erlernen möchten | ❌ Bereits bekannt, bietet wenig Lernpotenzial |

---

## 02: Backend Framework - Flask

### Meta

Status  
: **Entschieden**

Aktualisiert  
: 19-Nov-2024

### Problemstellung

Für die Entwicklung des Backends gab es keine Wahl, da der Kursplan die Verwendung von Flask vorgab.  

Obwohl alternative Frameworks wie Django für größere Projekte besser geeignet sein könnten, war Flask für die Kursanforderungen optimal, da es leicht und schnell zu lernen ist. 

### Entscheidung

Wir verwenden **Flask** als Backend-Framework.  

Die Entscheidung basiert auf den Vorgaben des Lehrplans. Flask bietet jedoch auch praktische Vorteile für kleine Projekte wie unser MVP (Minimum Viable Product). Es ist flexibel, erfordert wenig Einrichtung und erlaubt eine einfache Integration mit Firebase.

*Entscheidung getroffen von:* Lehrplananforderung.

### Betrachtete Optionen

Flask war die einzige Option im Rahmen des Kurses. Django oder andere Frameworks wurden nicht in Betracht gezogen.

| Kriterium                  | Flask                  |
| -------------------------- | ---------------------- |
| **Vorgabe durch Lehrplan** | ✔️ Erfüllt            |
| **Flexibilität**           | ✔️ Hochgradig anpassbar |
| **Einfachheit**            | ✔️ Einfach für Einsteiger |
| **Integration mit Firebase** | ✔️ Einfach           |

---

## 03: Frontend Framework - Bootstrap vs. Custom CSS

### Meta

Status  
: **Entschieden**

Aktualisiert  
: 19-Nov-2024

### Problemstellung

Für das Frontend mussten wir entscheiden, ob wir ein vorgefertigtes CSS-Framework wie Bootstrap nutzen oder eigene CSS-Stile entwickeln. Die Hauptüberlegungen umfassten die einfache Erstellung responsiver Designs, die Entwicklungsgeschwindigkeit und die allgemeine Optik der Anwendung.

### Entscheidung

Wir haben uns für **Bootstrap** als primäres CSS-Framework entschieden.  

Bootstraps responsives Grid-System und vorgefertigte Komponenten ermöglichten es uns, schnell eine Oberfläche zu gestalten, die auf verschiedenen Bildschirmgrößen funktioniert. Durch Bootstrap wurde sichergestellt, dass das UI konsistent ist, ohne dass viel Zeit in die Entwicklung von individuellen Stilen investiert werden musste.  

*Entscheidung getroffen von:* Veysel Sam (Frontend Lead).

### Betrachtete Optionen

Wir haben zwei Alternativen betrachtet:

+ Bootstrap  
+ Eigenes CSS  

| Kriterium                  | Bootstrap              | Eigenes CSS          |
| -------------------------- | ---------------------- | ------------------- |
| **Responsivität**          | ✔️ Eingebautes Grid-System | ❌ Manuelle Implementierung erforderlich |
| **Entwicklungsgeschwindigkeit** | ✔️ Schnell mit vorgefertigten Komponenten | ❌ Langsamer durch individuelle Kodierung |
| **Design-Konsistenz**      | ✔️ Hoch                | ❔ Hängt von den Fähigkeiten des Entwicklers ab |
| **Anpassbarkeit**          | ❔ Eingeschränkt durch Framework | ✔️ Vollständig anpassbar |

---

### Zusammenfassung der Entscheidungen

1. **Datenbank**: Firebase Firestore für Echtzeit-Updates, Skalierbarkeit und Lernmöglichkeiten mit neuen Technologien.  
2. **Backend-Framework**: Flask, wie durch den Lehrplan vorgegeben.  
3. **Frontend-Styling**: Bootstrap für schnelle Entwicklung und konsistente Responsivität.

Jede Entscheidung wurde getroffen, um das Ziel zu erreichen, ein funktionales, skalierbares und benutzerfreundliches MVP innerhalb der Projektzeit zu erstellen.
