# Snake_Game

Ce projet est un jeu du serpent développé en utilisant la bibliothèque Tkinter de Python pour l'interface graphique et PIL pour le traitement des images, ainsi Random pour le traitement des chiffres en aléatoires.
Prérequis

    Python 3.x
    Bibliothèque Tkinter
    Bibliothèque PIL (Pillow)

Vous pouvez installer les bibliothèques nécessaires en utilisant pip :
Fichiers

    snake_game.py : Le script principal pour exécuter le jeu du serpent.
    BGSNAKE.jpg : Image de fond pour le jeu.

Exécuter le jeu

Fonctionnalités
Menu Principal

    Jouer : Commencez le jeu.
    Options : Personnalisez la couleur du serpent.
    Quitter : Quittez le jeu.

Menu des Niveaux

    Facile : Commencez le jeu avec un niveau de difficulté facile.
    Moyen : Commencez le jeu avec un niveau de difficulté moyen.
    Difficile : Commencez le jeu avec un niveau de difficulté difficile.
    Retour : Retournez au menu principal.

Menu Options

    Couleur du Serpent : Choisissez la couleur du serpent.
    Retour : Enregistrez les options et retournez au menu principal.

Contrôles en Jeu

    Flèches directionnelles : Contrôlez la direction du serpent.
    Barre d'espace : Mettez le jeu en pause et reprenez-le.
    Retour au Menu : Retournez au menu principal pendant le jeu.

Écran de Fin de Partie

    Rejouer : Redémarrez le jeu.
    Quitter : Quittez le jeu.

Aperçu du Code

La classe principale SnakeGame initialise la fenêtre du jeu, gère les entrées de l'utilisateur, met à jour l'état du jeu et gère la boucle principale du jeu.
Méthodes

    __init__(self, root) : Initialise la fenêtre du jeu et configure le menu principal.
    set_background_color(self, color) : Définit la couleur de fond de la fenêtre du jeu.
    main_menu(self) : Affiche le menu principal.
    level_menu(self) : Affiche le menu de sélection des niveaux.
    options_menu(self) : Affiche le menu des options.
    choose_snake_color(self) : Ouvre un sélecteur de couleur pour choisir la couleur du serpent.
    save_options(self) : Enregistre les options sélectionnées et retourne au menu principal.
    clear_widgets(self) : Supprime tous les widgets de la fenêtre.
    start_game(self, speed) : Démarre le jeu avec la vitesse spécifiée.
    draw(self) : Dessine le serpent et la pomme sur le canvas.
    update(self) : Met à jour l'état du jeu.
    update_apple_position(self) : Met à jour la position de la pomme.
    random_coord(self, max_value) : Génère une coordonnée aléatoire pour la pomme.
    move(self) : Déplace le serpent et met à jour l'état du jeu.
    start_game_loop(self) : Démarre la boucle du jeu.
    toggle_pause(self, event=None) : Active ou désactive la pause du jeu.
    left(self, event), right(self, event), up(self, event), down(self, event) : Gère le changement de direction du serpent.
    back_to_menu(self) : Retourne au menu principal.
    game_over(self) : Affiche l'écran de fin de partie.

Personnalisation

Vous pouvez personnaliser l'image de fond en remplaçant BGSNAKE.jpg par une autre image. Assurez-vous que la nouvelle image porte le même nom ou mettez à jour l'attribut self.bg_image_path dans la classe SnakeGame.
Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

Amusez-vous bien en jouant au Jeu du Serpent !


#SnakyWaveGAMES
