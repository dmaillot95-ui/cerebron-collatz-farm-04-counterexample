# CEREBRON OMEGA — COLLATZ FARM 04 COUNTEREXAMPLE — C256+

MISSION
Falsifier agressivement les verrous actuels sans confondre réfutation d'une méthode avec réfutation de Collatz.

CHECKPOINT
Map accélérée impaire: T(x)=(3x+1)/2^{v2(3x+1)}.
Mot de valuations a_0,...,a_{n-1}; A_k=sum_{i<k} a_i.
Formule exacte: 2^{A_k}x_k=3^k x_0+C_k, C_0=0, C_{k+1}=3C_k+2^{A_k}.
Mots mécaniques/quasi critiques: A_k=floor(k log_2(3)+theta) ou variantes équilibrées.
Verrou courant: compatibilité simultanée fenêtre réelle first-return + cylindre 2-adique + endpoint 3-adique + structure Sturmienne.
CYCLES OPEN.

OBJECTIFS
1. Chercher des familles arbitrairement longues qui satisfont toute sous-collection des contraintes mais cassent la conclusion attendue.
2. Construire des contre-exemples aux lemmes trop forts: contraction uniforme, gap d'arc uniforme, résidu normalisé uniformément positif, obstruction CRT locale, etc.
3. Identifier précisément la première hypothèse qui échoue dans chaque argument.
4. Tester les mots floor/ceil one-crossing et leurs phases theta.
5. Séparer: contre-exemple fini; famille infinie prouvée; heuristique; simple anomalie numérique.
6. Ne jamais annoncer un cycle Collatz sans vérification exacte intégrale complète.

SORTIE ATTENDUE
Chaque rôle doit retourner: CLAIM ATTAQUÉ; CONSTRUCTION; CALCUL/ARGUMENT; STATUT PROUVÉ/HYPOTHÈSE/INCONNU; IMPACT SUR LE PROGRAMME.
