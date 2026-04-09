# calculateur.py


def calculer_moyenne(notes):
    """Calcule la moyenne d'une liste de notes."""
    if not notes:
        return 0
    return sum(notes) / len(notes)

def mention(moyenne):
    """Retourne la mention selon la moyenne."""
    if moyenne >= 16:
        return "Très bien"
    elif moyenne >= 14:
        return "Bien"
    elif moyenne >= 12:
        return "Assez bien"
    elif moyenne >= 10:
        return "Passable"
    else:
        return "Insuffisant"