import pygame, sys
from game import Game
from button import Button
from colors import Colors

pygame.init()

screen = pygame.display.set_mode((570,630))

background = pygame.image.load("assets/mybackground.png")

# font template
def main_font(size):
    return pygame.font.Font("assets/font/font.ttf", size)

basic_font = pygame.font.Font('assets/font/Pixellari.ttf', 30)
game_over_font1 = pygame.font.Font('assets/font/Pixellari.ttf', 40)
game_over_font2 = pygame.font.Font('assets/font/Pixellari.ttf', 20)

def main_menu():
    while True:
        pygame.mixer.music.stop()
        screen.blit(background, (-70, -90))
        pygame.display.set_caption("Tetris main menu screen")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        judul_game = main_font(35).render("TETRIS IN PYTHON", True, "white")
        judul_game_rect = judul_game.get_rect(center = (283 , 80))

        tombol_mulai = Button(image = pygame.image.load("assets/newewewbutton.png"), pos = (285, 280), 
                            text_input = "Mulai", font = main_font(30), base_color = "#a2fab4", ganti_warna = "White")
        tombol_kredit = Button(image = pygame.image.load("assets/newewewbutton.png"), pos = (285, 400), 
                            text_input = "Kredit", font = main_font(30), base_color = "#faf7a2", ganti_warna = "White")
        tombol_keluar = Button(image = pygame.image.load("assets/newewewbutton.png"), pos = (285 , 520), 
                            text_input = "Keluar", font = main_font(30), base_color = "#faa2a2", ganti_warna = "White")

        screen.blit(judul_game, judul_game_rect)

        for button in [tombol_mulai, tombol_kredit, tombol_keluar]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tombol_mulai.checkForInput(MENU_MOUSE_POS):
                    tutor()
                if tombol_kredit.checkForInput(MENU_MOUSE_POS):
                    kredit()
                if tombol_keluar.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def tutor():
    while True:
        screen.fill(Colors.warna_bg)
        pygame.display.set_caption("Tutorial screen")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # judul main screen "tutorial"
        who_made = main_font(26).render("ini tutor mainnya yee", True, "#F5F5DC")
        who_rect = who_made.get_rect(center = (285, 40))
        straight_line = main_font(22).render("_________________________", True, "#F5F5DC")
        straight_rect = straight_line.get_rect(center = (285, 70))

        # template untuk teks tutorial
        tutor1 = main_font(20).render("panah atas :", True, "#E6E6FA")
        tutor1_rect = tutor1.get_rect(center = (130, 120))
        tutor2 = main_font(20).render("panah bawah :", True, "#E6E6FA")
        tutor2_rect = tutor2.get_rect(center = (140, 200))
        tutor3 = main_font(20).render("panah kiri :", True, "#E6E6FA")
        tutor3_rect = tutor3.get_rect(center = (130, 280))
        tutor4 = main_font(20).render("panah kanan :", True, "#E6E6FA")
        tutor4_rect = tutor4.get_rect(center = (140, 360))
        # template untuk penjelasan tutorial
        penjelasan1 = main_font(20).render("memutar balok", True, "#E6E6FA")
        penjelasan1_rect = penjelasan1.get_rect(center = (140, 150))
        penjelasan2 = main_font(20).render("menurunkan balok 1 grid", True, "#E6E6FA")
        penjelasan2_rect = penjelasan2.get_rect(center = (240, 230))
        penjelasan3 = main_font(20).render("menggeser balok ke kiri", True, "#E6E6FA")
        penjelasan3_rect = penjelasan3.get_rect(center = (240, 310))
        penjelasan4 = main_font(20).render("menggeser balok ke kanan", True, "#E6E6FA")
        penjelasan4_rect = penjelasan4.get_rect(center = (250, 390))

        # nampilin teks tutorial
        screen.blit(who_made, who_rect)
        screen.blit(straight_line, straight_rect)
        screen.blit(tutor1, tutor1_rect)
        screen.blit(tutor2, tutor2_rect)
        screen.blit(tutor3, tutor3_rect)
        screen.blit(tutor4, tutor4_rect)
        # nampilin penjelasan dari tutorial
        screen.blit(penjelasan1, penjelasan1_rect)
        screen.blit(penjelasan2, penjelasan2_rect)
        screen.blit(penjelasan3, penjelasan3_rect)
        screen.blit(penjelasan4, penjelasan4_rect)

        tombol_main = Button(image = pygame.image.load("assets/tutor pe button.png"), pos = (425, 550), 
                            text_input = "gaskenn!!", font = main_font(25), base_color = "white", ganti_warna = "#a2fab4")
        tombol_kembali = Button(image = pygame.image.load("assets/tutor pe button.png"), pos = (145, 550), 
                            text_input = "gajadi ah", font = main_font(25), base_color = "white", ganti_warna = "#faa2a2")

        for button in [tombol_main, tombol_kembali]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tombol_main.checkForInput(MENU_MOUSE_POS):
                    play()
                if tombol_kembali.checkForInput(MENU_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def play():
    while True:
        skor = basic_font.render("Skor Anda", True, Colors.white)

        balok_lanjutan = basic_font.render("Balok Selanjutnya", True, Colors.white)

        game_over1 = game_over_font1.render("GAME OVER", True, Colors.white)
        game_over2 = game_over_font2.render("press space to play again", True, Colors.white)

        # besar persegi pada tampilan UI
        next_rect = pygame.Rect(320, 60, 240, 150)
        score_rect = pygame.Rect(320, 270, 240, 60)

        pygame.display.set_caption("Python Tetris by anak tektel")

        clock = pygame.time.Clock()

        game = Game()

        GAME_UPADTE = pygame.USEREVENT
        pygame.time.set_timer(GAME_UPADTE, 200) # cepat berjalannya game, perhitungannya 1/milidetik

        # Game loop
        while True: # ketika gamenya berjalan maka syntax dibawah akan berjalan
            posisi_tombol_menu = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and game.game_over == True:
                        game.game_over = False
                        game.reset()
                    if event.key == pygame.K_LEFT and game.game_over == False:
                        game.move_left()
                    if event.key == pygame.K_RIGHT and game.game_over == False:
                        game.move_right()
                    if event.key == pygame.K_DOWN and game.game_over == False:
                        game.move_down()
                        game.update_score(0, 1)
                    if event.key == pygame.K_UP and game.game_over == False:
                        game.rotate()
                if event.type == GAME_UPADTE and game.game_over == False:
                    game.move_down()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if  tombol_menu.checkForInput(posisi_tombol_menu):
                        main_menu()

            tombol_menu = Button(image = None, pos = (440, 590), text_input = "Menu Utama", font = main_font(23), base_color = "white", ganti_warna="Green")

            #skor record
            score_value_surface = basic_font.render(str(game.score), True, Colors.white)

            # posisi/letak text
            screen.fill(Colors.warna_bg)

            screen.blit(skor, (325, 230, 50, 50))
            screen.blit(balok_lanjutan, (325, 15, 40, 40))

            tombol_menu.changeColor(posisi_tombol_menu)
            tombol_menu.update(screen)


            if game.game_over == False:
                pygame.mixer.music.load("assets/sound effects/gameoversfx.ogg")
                pygame.mixer.music.play(0)

            if game.game_over == True:
                screen.blit(game_over1, (330, 440, 40, 40))
                screen.blit(game_over2, (330, 475, 40, 40))



            # nyambung dengan besar persegi, ini untuk warna dan besar sudutnya
            pygame.draw.rect(screen, Colors.warna_persegi, score_rect, 0, 10)
            screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery)) # letak skor
            pygame.draw.rect(screen, Colors.warna_persegi, next_rect, 0, 10)
            game.draw(screen)

            pygame.display.update()
            clock.tick(60) # berapa fps(frame per second)/ frame yang terjadi dalam satu detik

def kredit():
    while True:
        posisi_kredit_kembali = pygame.mouse.get_pos()
        pygame.display.set_caption("Credits...")

        screen.fill(Colors.warna_bg)

        # teks buat kredit
        who_made = main_font(22).render("Made by anak tektel 47-01", True, "#F5F5DC")
        who_rect = who_made.get_rect(center = (285, 40))

        straight_line = main_font(22).render("_________________________", True, "#F5F5DC")
        straight_rect = straight_line.get_rect(center = (285, 70))

        person1 = main_font(20).render("A. Kiflan Jiyaad Mafazi. A", True, "white")
        person1_rect = person1.get_rect(center = (272, 120))
        person2 = main_font(20).render("Alya Khalisa Nadira", True, "white")
        person2_rect = person2.get_rect(center = (202, 150))
        person3 = main_font(20).render("Hariro Imka Harahap", True, "white")
        person3_rect = person3.get_rect(center = (202, 180))

        # nampilin teks di kredit
        screen.blit(who_made, who_rect)
        screen.blit(straight_line, straight_rect)
        screen.blit(person1, person1_rect)
        screen.blit(person2, person2_rect)
        screen.blit(person3, person3_rect)

        kredit_kembali = Button(image = None, pos = (100, 580), text_input = "Kembali", font = main_font(23), base_color = "white", ganti_warna="Green")

        kredit_kembali.changeColor(posisi_kredit_kembali)
        kredit_kembali.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if kredit_kembali.checkForInput(posisi_kredit_kembali):
                    main_menu()

        pygame.display.update()

main_menu()