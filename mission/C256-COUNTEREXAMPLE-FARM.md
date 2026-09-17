# CEREBRON OMEGA — COLLATZ COUNTEREXAMPLE FARM — CHECKPOINT 2026-09-17

MISSION: falsify the current H-COUPLING / H-LOG / small-h program. Do not prove by search; use finite computation only to kill false universal claims.

Claims under attack:
1. any proposed monotone potential on (u,r,h);
2. any statement small h => large r without precise quantifiers;
3. any claim that exceptional 3-adic valuations are globally rare;
4. any collective H-LOG upper bound stronger than termwise h>=5;
5. any LOWER>UPPER collision claim;
6. any arithmetic-compression transformation used by other farms.

Exact constraints to preserve while generating examples:
- 3^u t - 1 = 4^r h;
- 2^{u_next} t_next - 1 = 3^r h;
- h odd, h≡5 mod6;
- H-COUPLING: 2^{u_next+2r_next}h_next-3^{u_next+r}h=3^{u_next}-2^{u_next};
- h≡-4^{-r} mod 3^u.

Search priorities: u=1, r=1, h=5,11,17; exceptional valuations; imprimitive words; adjacent-run compatibility; cases that maximize H-LOG contribution.

ARITHMETIC COMPRESSION RED TEAM: verify every claimed reduction. Attack factorization, caching, recurrence indexing, modular pruning, log approximations, precision and hidden recomputation. An optimization without exact equivalence is REJECTED.

Output: CLAIM / ATTACK / COUNTEREXAMPLE OR NO COUNTEREXAMPLE FOUND / UNIVERSAL STATUS / CORRECTION / NEXT ATTACK. Absence of counterexample is not proof.