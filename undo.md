"restore vs reset" 

## git restore
- Annule les modifications d'un fichier non commité
- Ne touche PAS à l'historique des commits
- Exemple : git restore fichier.txt

## git reset
- Annule des commits déjà faits
- Modifie l'historique
- Exemple : git reset --soft HEAD~1 (garde les modifs)
- Exemple : git reset --hard HEAD~1 (supprime les modifs)"