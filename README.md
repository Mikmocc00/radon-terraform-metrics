# Terraform HCL Metrics — IaC Defect Prediction

Questa libreria estrae metriche statiche da script Terraform (HCL2) per supportare l'addestramento di modelli di **within-repo IaC defect prediction**. Le metriche catturano la complessità del grafo delle dipendenze, l'uso di costrutti logici avanzati (anti-pattern in linguaggi dichiarativi) e il grado di accoppiamento dell'infrastruttura.

---

## Metriche disponibili

### 1. `AvgDependenciesPerResource`
**Tipo:** `float`  
Calcola il numero medio di dipendenze esplicite (`depends_on`) per singola risorsa.  
**Perché è importante:** Terraform gestisce nativamente l'ordine di creazione tramite dipendenze implicite. L'uso frequente di `depends_on` forza il grafo di esecuzione, indicando configurazioni "fragili" dove l'infrastruttura non riesce a passarsi le variabili correttamente. Valori alti sono predittori di fallimenti durante il `terraform apply` o di colli di bottiglia nelle performance.

---

### 2. `AvgResourceSize`
**Tipo:** `float`  
Calcola la dimensione media (in numero di attributi/chiavi) per blocco `resource`.  
**Perché è importante:** Una risorsa con troppi attributi è complessa da configurare e mantenere (es. una `aws_instance` con decine di parametri di rete, storage e provisioning). Modelli ML usano questa metrica per identificare risorse "monolitiche" inclini a errori di configurazione.

---

### 3. `DependencyGraphDensity`
**Tipo:** `float`  
Calcola la densità del grafo delle dipendenze: rapporto tra il numero totale di archi (dipendenze implicite + esplicite) e il numero massimo possibile di archi tra le risorse presenti.  
**Perché è importante:** Misura quanto l'infrastruttura è interconnessa. Una densità troppo elevata (tight coupling) significa che una modifica a una risorsa ha un'alta probabilità di innescare effetti a cascata (o distruzioni/ricreazioni non volute) su tutto lo stack.

---

### 4. `ExplicitDependencies` / `NumDependencies`
**Tipo:** `int`  
Conta il numero totale di blocchi o link `depends_on` nel codice.  
**Perché è importante:** Come per `AvgDependenciesPerResource`, un alto numero assoluto denota un intervento manuale massiccio sull'ordine di esecuzione, spesso sintomo di workaround architetturali e technical debt.

---

### 5. `ImplicitDependencies`
**Tipo:** `int`  
Conta le dipendenze derivate da interpolazioni (es. `aws_vpc.main.id`).  
**Perché è importante:** Le dipendenze implicite sono il modo "giusto" di usare Terraform. Tuttavia, un numero estremamente elevato contribuisce ad aumentare la complessità globale del grafo, rendendo il refactoring pericoloso.

---

### 6. `MaxDependencyChainLength`
**Tipo:** `int`  
Calcola la lunghezza del percorso più lungo (longest path) nel grafo aciclico diretto (DAG) delle dipendenze.  
**Perché è importante:** Catene lunghe aumentano il tempo di esecuzione e la probabilità che un timeout o un fallimento temporaneo a metà catena faccia fallire l'intera pipeline di deploy. È una misura diretta del rischio di "deployment failure".

---

### 7. `ModuleFanIn`
**Tipo:** `int`  
Conta le chiamate ai moduli (es. `module.xxx`).  
**Perché è importante:** Misura l'uso della modularizzazione. Sebbene i moduli riducano la duplicazione, un Fan-In eccessivo senza una corretta astrazione crea "black box" difficili da debuggare quando Terraform restituisce errori su risorse annidate.

---

### 8. `ModuleReuseCount`
**Tipo:** `int`  
Conta quante volte la stessa `source` di un modulo viene riutilizzata all'interno dello script.  
**Perché è importante:** Un alto riutilizzo è positivo per la standardizzazione, ma se la configurazione del modulo non è flessibile, può introdurre difetti logici. È utile ai modelli ML per capire se il file agisce come "orchestratore" di moduli standard.

---

### 9. `NumConditionals`
**Tipo:** `int`  
Conta l'utilizzo dell'operatore ternario (es. `condizione ? vero : falso`).  
**Perché è importante:** HCL non è nato per la logica complessa. I condizionali rendono l'IaC molto meno leggibile e sono tra le principali fonti di bug logici, specialmente quando usati per bypassare o spegnere intere risorse in ambienti diversi.

---

### 10. `NumDataSources`
**Tipo:** `int`  
Conta i blocchi `data`.  
**Perché è importante:** I data source legano l'esecuzione dello script allo stato attuale del cloud provider. Molti data source aumentano la probabilità di fallimenti durante il `terraform plan` causati da problemi di rete, permessi IAM mancanti o risorse esterne eliminate.

---

### 11. `NumDynamicBlocks`
**Tipo:** `int`  
Conta i blocchi `dynamic`.  
**Perché è importante:** I blocchi dinamici generano codice in base a variabili complesse (es. mappe o liste). Sono notoriamente difficili da leggere e testare. Il loro abuso è un forte segnale di over-engineering e correla fortemente con difetti di sintassi ed esecuzione.

---

### 12. `NumLocals`
**Tipo:** `int`  
Conta il numero di variabili locali definite in blocchi `locals`.  
**Perché è importante:** I `locals` aiutano la pulizia del codice, ma un numero spropositato indica trasformazioni di dati complesse che avvengono direttamente nell'HCL (anti-pattern) anziché a monte.

---

### 13. `NumLoops`
**Tipo:** `int`  
Conta le iterazioni dichiarate tramite `count` o `for_each`.  
**Perché è importante:** Creare risorse in loop è potente, ma gestire gli indici (specie con `count`) è pericoloso. Se un elemento viene rimosso da una lista usata con `count`, Terraform ricreerà o distruggerà le risorse successive sfasando gli indici. È uno dei difetti IaC più distruttivi.

---

### 14. `NumModules` / `NumResources` / `NumProviders`
**Tipo:** `int`  
Volume totale di blocchi `module`, `resource` e `provider`.  
**Perché è importante:** Metriche di dimensionalità di base (l'equivalente delle Lines of Code). Spazi di lavoro troppo grandi e non frammentati hanno fisiologicamente una probabilità maggiore di contenere bug.

---

### 15. `NumOutputs` / `NumVariables`
**Tipo:** `int`  
Volume dei blocchi di input/output.  
**Perché è importante:** Rappresentano l'interfaccia (API) dello script Terraform. Un'interfaccia molto larga aumenta l'accoppiamento con tool di CI/CD o moduli genitore, aumentando la superficie di regressione.

---

### 16. `NumProvisioners` / `ProvisionersPerResource`
**Tipo:** `int` / `float`  
Conta i blocchi `provisioner` (es. `local-exec`, `remote-exec`) e la loro densità per risorsa.  
**Perché è importante:** I provisioner sono considerati un'ultima risorsa da HashiCorp (un *anti-pattern* ufficiale). Inseriscono comportamenti imperativi in un tool dichiarativo. Non sono idempotenti e spesso non tracciati nello state file. È la metrica predittiva più forte per fallimenti di apply non riproducibili.
> **Valore ideale:** `0`.

---

### 17. `ResourceDensity`
**Tipo:** `float`  
Rapporto tra il numero di risorse e le righe di codice (LOC).  
**Perché è importante:** Valuta la formattazione e la "densità" d'informazione. File molto densi sono difficili da ispezionare durante una Code Review.

---

### 18. `ResourceTypeDiversity`
**Tipo:** `int`  
Conta il numero di tipologie uniche di risorse (es. `aws_vpc`, `aws_instance`, `aws_s3_bucket`).  
**Perché è importante:** Un file che gestisce 20 tipi di risorse diverse sta probabilmente violando il principio di singola responsabilità (es. mischiando Network, Compute e IAM). Predice difetti architetturali e di design.

---

### 19. `ResourcesPerProvider`
**Tipo:** `float`  
Numero medio di risorse per blocco provider.  
**Perché è importante:** Script multi-cloud o multi-account (con molti alias di provider) sono complessi. Se ci sono troppe risorse da mappare a provider diversi, il rischio di associare una risorsa alla region o all'account sbagliato cresce notevolmente.

---

### 20. `VariableDefaultRatio`
**Tipo:** `float`  
Percentuale di variabili che dichiarano un valore di `default`.  
**Perché è importante:** Variabili senza default sono obbligatorie. Se usate male, bloccano l'esecuzione di Terraform in ambienti CI/CD non interattivi richiedendo input manuale. Un ratio basso indica uno script poco portabile o difficile da testare.

---

### 21. `VariableReferenceCount`
**Tipo:** `float`  
Media dei riferimenti (es. `var.nome_variabile`) per ogni variabile dichiarata.  
**Perché è importante:** Se una variabile è referenziata 50 volte, il suo impatto (blast radius) è enorme: un input sbagliato comprometterà buona parte dell'infrastruttura. Valori troppo bassi possono indicare variabili "orfane" (dichiarate ma non usate).

---

### 22. `VariablesPerResource`
**Tipo:** `float`  
Rapporto tra variabili e risorse.  
**Perché è importante:** Moduli con troppe variabili per risorsa sono considerati over-ingegnerizzati (es. un modulo che cerca di esporre ogni singolo parametro AWS all'utente). Questo riduce il valore dell'astrazione e aumenta gli errori di configurazione "lato utente".

## Metriche Composte (Composite Metrics)

Questa sezione include metriche avanzate calcolate combinando le metriche di base. Forniscono insight di alto livello sulla qualità del codice, sul debito tecnico e sul rischio di deployment.

### 23. `AvgBlockVerbosity`
**Tipo:** `float`  
Calcola la verbosità media del codice per ogni blocco risorsa.
$$\frac{\text{Total Tokens}}{\text{Total Resources}}$$
**Perché è importante:** Indica la "pesantezza" testuale delle risorse. File con una verbosità anomala contengono spesso stringhe hardcodate lunghissime (es. script `user_data` in linea) o documentazione mista a codice, rendendo l'analisi visiva difficile.

---

### 24. `ChangeAmplification`
**Tipo:** `float`  
Misura l'effetto a cascata ("blast radius") potenziale di una modifica.
$$\text{AvgDependenciesPerResource} \times \text{VariableReferenceCount}$$
**Perché è importante:** Moltiplica quanto le risorse sono dipendenti l'una dall'altra per quanto le variabili sono referenziate in giro. Un valore alto significa che cambiare un singolo input (es. una variabile d'ambiente) causerà la ricalcolazione del plan per moltissime risorse connesse.

---

### 25. `ComplexityScore`
**Tipo:** `float`  
Punteggio di complessità strutturale del manifest.
$$\frac{\text{Dynamic Blocks} + \text{Conditionals} + \text{Provisioners}}{\text{Total Resources}}$$
**Perché è importante:** Aggrega gli elementi più imperativi, complessi e imprevedibili di Terraform. Risorse che necessitano di blocchi dinamici, logica condizionale e provisioner sono statisticamente la fonte primaria di fallimenti o drift di stato in produzione.

---

### 26. `ConfigStress`
**Tipo:** `float`  
Valuta lo "stress" cognitivo e tecnico della configurazione.
$$\text{KeyDensity} \times \text{AvgResourceSize} \times \text{ResourceDensity}$$
**Perché è importante:** Identifica script che sono densi di logica, con risorse enormi e tantissime chiavi configurate. Questi file sono i colli di bottiglia del repository: difficili da refactorizzare e proni a typo o misconfigurazioni silenti.

---

### 27. `CouplingPressure`
**Tipo:** `float`  
Misura la pressione imposta dai legami esterni e interni sulle risorse.
$$\frac{\text{VarRefs} + \text{ImplicitDeps} + \text{ModuleFanIn}}{\text{Total Resources}}$$
**Perché è importante:** Un file con alta "pressione" non è autonomo. Dipende fortemente da input esterni (variabili), output di altre risorse (dipendenze implicite) e astrazioni esterne (moduli). Rompere uno qualsiasi di questi contratti causa il fallimento del manifest.

---

### 28. `CouplingScore`
**Tipo:** `float`  
Rapporto globale di accoppiamento normalizzato per riga di codice.
$$\frac{\text{Implicit Refs} + \text{Modules}}{\text{LOC}}$$
**Perché è importante:** Fornisce una metrica densa di quanto il file sia "cablato" verso l'esterno rispetto alla sua lunghezza effettiva. Utile per paragonare il livello di accoppiamento tra script piccoli e script molto lunghi.

---

### 29. `DynamicComplexity`
**Tipo:** `float`  
Valuta l'impatto dei comportamenti dinamici sulle dimensioni delle risorse.
$$(\text{DynamicBlocks} + \text{Conditionals} + \text{Loops}) \times \text{AvgResourceSize}$$
**Perché è importante:** Un loop (`for_each`) applicato su una risorsa enorme e complessa è infinitamente più rischioso di un loop applicato su una risorsa banale (es. un `random_id`). Questa metrica amplifica il rischio dinamico in base al "peso" della risorsa manipolata.

---

### 30. `KeyDensity`
**Tipo:** `float`  
Calcola il numero medio di chiavi (attributi) assegnate per risorsa.
$$\frac{\text{Total Keys}}{\text{Total Resources}}$$
**Perché è importante:** Complementare alla dimensione della risorsa, indica quante configurazioni esplicite sono fornite rispetto ai valori di default del provider. Una densità estrema può indicare micro-management dell'infrastruttura.

---

### 31. `ModularityScore`
**Tipo:** `float`  
Indica il grado di astrazione e riutilizzo.
$$\frac{\text{Locals} + \text{Modules}}{\text{Total Resources}}$$
**Perché è importante:** Valori alti denotano un forte uso di variabili calcolate (`locals`) e moduli esterni. Se il valore è eccessivo, il file è solo uno stub incomprensibile (over-engineering), se è troppo basso manca di standardizzazione (under-engineering).

---

### 32. `ProvisionerRisk`
**Tipo:** `float`  
Calcola il rischio catastrofico associato all'uso di script imperativi.
$$\text{NumProvisioners} \times \text{ProvPerResource} \times \text{ComplexityScore}$$
**Perché è importante:** I provisioner (`local-exec`, `remote-exec`) aggirano lo stato dichiarativo di Terraform. Moltiplicare la loro presenza per la complessità generale del file isola le "bombe a orologeria" del repository, dove script bash fallaci possono corrompere il deployment.

---

### 33. `ResourceSprawl`
**Tipo:** `float`  
Indica la dispersione e ripetizione architetturale.
$$\frac{\text{Total Resources}}{\text{Unique Resource Types}}$$
**Perché è importante:** Se ho 50 risorse ma appartengono a un solo tipo (es. 50 record DNS dichiarati a mano), ho uno sprawl altissimo. Questo segnala codice "copia-incolla" che andrebbe ottimizzato usando i loop (`for_each`), riducendo la possibilità di errori manuali.

---

### 34. `VocabularyRichness`
**Tipo:** `float`  
Misura la diversità dei token usando l'entropia di Shannon normalizzata.
$$\frac{\text{Shannon Entropy}}{\log_2(\text{Tokens})}$$
**Perché è importante:** È una metrica NLP prestata al codice. Un vocabolario troppo "ricco" (alta entropia) in un linguaggio dichiarativo significa che lo sviluppatore sta usando naming conventions incoerenti, nomi di risorse disomogenei e descrizioni non standardizzate.

---

## Riepilogo Completo (Metriche Base + Composte)

| Metrica | Focus ML | Segnale critico |
| :--- | :--- | :--- |
| `AvgDependenciesPerResource` | Complessità DAG | Valore alto → Uso anomalo di `depends_on`, ordine forzato |
| `AvgResourceSize` | Complessità | Valore alto → Risorse monolitiche e over-configurate |
| `DependencyGraphDensity` | Architettura | Valore alto → Tight coupling, alto rischio di rollback a cascata |
| `Explicit/Implicit/Total Dependencies`| Complessità DAG | Valori alti → Fragilità delle connessioni infrastrutturali |
| `MaxDependencyChainLength` | Stabilità Apply | Valore alto → Alto rischio di timeout e fallimenti a catena |
| `ModuleFanIn` / `ModuleReuseCount` | Astrazione | Valori alti → Rischio "Black box", difficile da debuggare |
| `NumConditionals` | Logica / Qualità | Valore alto → Codice illeggibile, bug logici, anti-pattern |
| `NumDataSources` | Affidabilità | Valore alto → Rischio legami ambientali non risolvibili |
| `NumDynamicBlocks` | Logica / Qualità | Valore alto → Over-engineering, difficile predirne l'output |
| `NumLoops` (`count`/`for_each`) | Stabilità State | Valore alto → Rischio massiccio distruzione/ricreazione imprevista |
| `NumProvisioners` / `ProvPerResource` | Affidabilità | > 0 → Forte anti-pattern, deploy imperativi e non idempotenti |
| `NumResources` / `Providers` / `Modules`| Dimensione | Valori alti → Complessità globale, difficile manutenzione |
| `ResourceDensity` | Leggibilità | Valori anomali → Difficoltà in Code Review |
| `ResourceTypeDiversity` | Architettura | Valore alto → Violazione della Separation of Concerns |
| `VariableDefaultRatio` | Usabilità CI/CD | Valore basso → Rischio di prompt bloccanti, difficile testabilità |
| `VariableReferenceCount` | Blast Radius | Valore alto → Un errore di input propaga difetti ovunque |
| **`AvgBlockVerbosity`** | Leggibilità | Valore alto → Hardcoding testuale estremo (es. inline scripts) |
| **`ChangeAmplification`** | Blast Radius | Valore alto → Propagazione massiccia di ricalcoli in fase di plan |
| **`ComplexityScore`** | Stabilità | Valore alto → Alta concentrazione di logica imperativa in HCL |
| **`ConfigStress`** | Manutenibilità | Valore alto → File troppo densi e incomprensibili human-readable |
| **`CouplingPressure/Score`** | Accoppiamento | Valore alto → Risorse dipendenti in modo insicuro da input esterni |
| **`DynamicComplexity`** | Prevedibilità | Valore alto → Rischio di state desync fatali su risorse pesanti |
| **`KeyDensity`** | Micro-management| Valore alto → Eccesso di parametri espliciti a discapito dei default |
| **`ModularityScore`** | Architettura | Valori estremi → Over-engineering o codice completamente flat |
| **`ProvisionerRisk`** | Pericolo Critico | Valore alto → Script fallaci bypassano l'idempotenza di Terraform |
| **`ResourceSprawl`** | DRY Principle | Valore alto → Assenza di loop e presenza di copia-incolla manuale |
| **`VocabularyRichness`** | Standardizzazione| Valore alto → Naming conventions caotiche, "magic strings" |