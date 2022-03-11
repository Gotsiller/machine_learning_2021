# machine_learning_2021

## Datensets:

#### White Wine Quality
  - Url: https://www.openml.org/d/40498
  - Size: 4898 instances (small)
  - Dimension: 12 features (low)
  - Missing Values: 0
  - Attribute Types: numeric / ratio quantities
  - Task: classification

#### Internet Usage
  - https://www.openml.org/d/372
  - 10108 instance (big enough?)
  - 72 features (high dimension)
  - 46 classes -> unfortunately classification again, not sure if this is a problem
  - 2699 missing values, all in one features
  - **Remark:** I think the column for `Actual_Time` and `who` are interchanged. If this is true, this would be a regression dataset.


## Git Crashkurs

#### Clone Repository:
  1. Git auf eurem Rechner installieren: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
  1. Sicherstellen dass ein SSH key auf GitHub festgelegt ist.
    - Anleitung: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
    - Alternativ sollte auch HTTPS möglich sein oder der GitHub Desktop Client
  1. Im Repository auf das grüne "Code" Feld klicken und SSH URL kopieren.
  1. Lokal in den Ordner gehen wo ihr das Projekt speichern wollt und eine Kommandozeile öffnen.
  1. Zum Clonen folgenden Befehl eingeben: `git clone <die kopierte SSH URL>`
  1. Jetzt solltet ihr das Repo auf eurem lokalen Rechner haben


#### Push/Pull
Bevor ihr an dem Repo arbeitet, solltet ihr immer einen Pull ausführen um sicher zu gehen, dass ihr auf der aktuellen Version arbeitet und um später merge Konflikte zu vermeiden.
  1. Kommandozeile im Repository öffnen
  1. Befehl `git pull` ausführen
  1. Euer GitHub Passwort angeben falls ihr danach gefragt werdet.

Wenn ihr etwas verändert habt und eure Arbeit hochladen wollt, macht ihr folgendes:
  1. Kommandozeile im Repository öffnen
  1. Alle eure Änderungen für den Commit stagen mit: `git add -A`
    - hier könnte man auch nur einzelne Dateien hinzufügen falls man das will
  1. Die hinzugefügten Änderungen in einem Commit verpacken: `git commit -m "Das ist eure commit message"`
  1. Euren Commit in das online Repository pushen: `git push`
  1. Euer GitHub Passwort angeben falls ihr danach gefragt werdet.
  1. Jetzt sind eure Änderungen online und über euren Commit kann jeder sehen was ihr verändert habt.


#### Status und Log
Die Status und Log funktionen können verwendet werden um einen Überblick über euer lokales Repo zu bekommen.

Mit `git status` bekommt ihr Infos darüber was lokal verändert wurde und was sich aktuell in der staging area (also bereit zum commiten) befindet.

Mit `git log` bekommt ihr die commit history. Dort seht ihr was die letzten commits waren, ob ihr auf dem aktuellen stand seid und ob eure Änderungen korrekt commited wurden.
