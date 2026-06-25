from pygame import *
from tkinter import *
import random


#WINDOW
init()

WIDTH = 700
HEIGHT = 500

window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Catch The Apple - Biology Quiz")

clock = time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)

font.init()
font1 = font.SysFont("Arial",30)


#SCORE
score = 0
apple_count = 0
TOTAL_APPLES = 5


#QUESTIONS
questions = [

{
"question":"What is the powerhouse of the cell?",
"options":["A. Nucleus",
           "B. Mitochondria",
           "C. Ribosome",
           "D. Vacuole"],
"answer":"B"
},

{
"question":"Photosynthesis occurs in ...",
"options":["A. Chloroplast",
           "B. Mitochondria",
           "C. Ribosome",
           "D. Nucleus"],
"answer":"A"
},

{
"question":"Humans have ___ pairs of chromosomes.",
"options":["A. 22",
           "B. 23",
           "C. 24",
           "D. 46"],
"answer":"B"
},

{
"question":"DNA stands for ...",
"options":["A. Dynamic Nuclear Acid",
           "B. Double Nuclear Acid",
           "C. Deoxyribonucleic Acid",
           "D. None"],
"answer":"C"
},

{
"question":"Plants make food by ...",
"options":["A. Respiration",
           "B. Digestion",
           "C. Photosynthesis",
           "D. Fermentation"],
"answer":"C"
}

]


#QUIZ
def ask_question():

    global score

    q = random.choice(questions)
    questions.remove(q)

    root = Tk()
    root.title("Biology Quiz")
    root.geometry("430x260")

    Label(root,
          text=q["question"],
          font=("Arial",12,"bold"),
          wraplength=400).pack(pady=10)

    ans = StringVar()

    for option in q["options"]:
        Radiobutton(root,
                    text=option,
                    variable=ans,
                    value=option[0]).pack(anchor="w")

    def submit():

        global score

        if ans.get() == q["answer"]:
            score += 10

        root.destroy()

    Button(root,
           text="Submit",
           command=submit).pack(pady=10)

    root.mainloop()


#IMAGES
basket = transform.scale(image.load("basket.png"),(100,60))
apple = transform.scale(image.load("apple.png"),(50,50))

win_img = transform.scale(image.load("youwin.png"),(700,500))
lose_img = transform.scale(image.load("youlose.png"),(700,500))
background = transform.scale(
    image.load("background.png"),
    (700, 500)
)


#PLAYER
basket_rect = basket.get_rect()

basket_rect.x = WIDTH//2-50
basket_rect.y = HEIGHT-70

basket_speed = 10


#APPLE
apple_rect = apple.get_rect()

apple_rect.x = random.randint(0, WIDTH-50)
apple_rect.y = -50

apple_speed = 5

run = True
finish = False


#GAME LOOP
while run:

    clock.tick(60)

    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:

        
        keys = key.get_pressed()

        if keys[K_LEFT] and basket_rect.x > 0:
            basket_rect.x -= basket_speed

        if keys[K_RIGHT] and basket_rect.x < WIDTH-100:
            basket_rect.x += basket_speed

        
        apple_rect.y += apple_speed

        
        basket_hitbox = basket_rect.inflate(-80, -50)
        apple_hitbox = apple_rect.inflate(-35, -35)

        
        if basket_hitbox.colliderect(apple_hitbox):
            apple_count += 1
            ask_question()
            apple_speed += 1
            apple_rect.x = random.randint(0, WIDTH - 50)
            apple_rect.y = -50

       
        elif apple_rect.y >= HEIGHT:
            apple_count += 1        
            apple_speed += 1        
            apple_rect.x = random.randint(0, WIDTH - 50)
            apple_rect.y = -50

        
        window.blit(background, (0,0))

        
        window.blit(apple, apple_rect)

        
        window.blit(basket, basket_rect)

        
        score_text = font1.render(
            "Score : " + str(score),
            True,
            BLACK
        )

        window.blit(score_text,(10,10))

       
        left_text = font1.render(
            "Apple : " + str(apple_count) + "/" + str(TOTAL_APPLES),
            True,
            BLACK
        )

        window.blit(left_text,(10,45))

        
        if apple_count >= TOTAL_APPLES:

            finish = True

            if score >= 20:
                window.blit(win_img,(0,0))
            else:
                window.blit(lose_img,(0,0))

    display.update()

quit()

