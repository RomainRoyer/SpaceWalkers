import pygame
import random

# initialisation de Pygame
pygame.init()

# définition de la fenêtre de jeu
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Jeu de quiz QCM sur la chimie")

# définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# définition des polices de caractères
FONT_LARGE = pygame.font.Font(None, 50)
FONT_MEDIUM = pygame.font.Font(None, 30)
FONT_SMALL = pygame.font.Font(None, 20)

# définition des questions et des réponses
questions = [
    {
        "question": "Quel est le symbole chimique de l'eau ?",
        "options": ["H2O", "CO2", "O2", "N2"],
        "answer": "H2O"
    },
    {
        "question": "Quel est l'élément chimique de symbole C ?",
        "options": ["Carbone", "Cuivre", "Calcium", "Chlore"],
        "answer": "Carbone"
    },
    {
        "question": "Quel est le gaz le plus abondant dans l'atmosphère terrestre ?",
        "options": ["Azote", "Oxygène", "Argon", "Dioxyde de carbone"],
        "answer": "Azote"
    }
]

player_names = []
num_players = 0

# initialize scores for each player to zero
scores = [0 for _ in range(num_players)]




# définition des variables du jeu
score = [0, 0, 0, 0]  # score de chaque joueur
current_player = 0  # joueur actuel
current_question = 0  # question actuelle
level = 1  # niveau actuel

# initialisation du jeu
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Quiz chimie")

def draw_question():
    font = pygame.font.Font(None, 36)
    question_text = font.render("Quel est le symbole chimique du carbone?", True, WHITE)
    question_rect = question_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/3))
    screen.blit(question_text, question_rect)

def draw_options():
    font = pygame.font.Font(None, 36)
    option_a = font.render("A: Car", True, WHITE)
    option_a_rect = option_a.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    screen.blit(option_a, option_a_rect)

    option_b = font.render("B: Oxygen", True, WHITE)
    option_b_rect = option_b.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 50))
    screen.blit(option_b, option_b_rect)

    option_c = font.render("C: Nitrogen", True, WHITE)
    option_c_rect = option_c.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 100))
    screen.blit(option_c, option_c_rect)

def draw_score():
    font = pygame.font.Font(None, 30)
    player_scores = [f"Player {i+1}: {scores[i]}" for i in range(num_players)]
    score_text = font.render(" | ".join(player_scores), True, WHITE)
    score_rect = score_text.get_rect(topright=(WINDOW_WIDTH - 10, 10))
    screen.blit(score_text, score_rect)


while num_players < 1 or num_players > 4:
    try:
        num_players = int(input("Enter number of players (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")

for i in range(num_players):
    player_name = input(f"Enter name for player {i+1}: ")
    player_names.append(player_name)

num_options = 4  # Replace 4 with the actual number of options

# Rest of your code
options = ["Option 1", "Option 2", "Option 3", "Option 4"]  # Replace with your actual options

num_options = len(options)


# Define the rectangle coordinates for each option
option_rects = []
for i in range(num_options):
    option_rects.append(pygame.Rect(50, 250 + i * 50, 500, 50))

def check_answer(answer_index):
    if isinstance(current_question, dict) and isinstance(answer_index, int):
        if current_question["answer_index"] == answer_index:
            print("Réponse correcte!")
            scores[current_player] += 1
    else:
        print("Réponse incorrecte!")


    # Passe à la question suivante
    current_question_index += 1
    if current_question_index >= len(questions):
        print("Le jeu est terminé!")
    else:
        current_question = questions[current_question_index]

        # Dessine la nouvelle question et options
        draw_question()
        draw_options()
        draw_score()


# boucle principale du jeu
running = True
while running:
    scores = [0] * num_players
    # traitement des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_1:
                # traitement de la réponse 1
                check_answer(0)
            elif event.key == pygame.K_2:
                # traitement de la réponse 2
                check_answer(1)
            elif event.key == pygame.K_3:
                # traitement de la réponse 3
                check_answer(2)
            elif event.key == pygame.K_4:
                # traitement de la réponse 4
                check_answer(3)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # traitement du clic gauche de la souris
                for i, option_rect in enumerate(option_rects):
                    if option_rect.collidepoint(event.pos):
                        check_answer(i)

    # mise à jour de l'affichage

    screen.fill(BLACK)
    draw_question()
    draw_options()
    draw_score()
    pygame.display.flip()


# fermeture de Pygame
pygame.quit()

                           
