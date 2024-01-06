import time
from turtle import Turtle, Screen
from player_and_bullet import PlayerBullet
from shield import Shield
from enemies_and_bullet import Enemy
from health import Health
from score import Score

is_running = True
screen = Screen()
screen.title("Space Invader Game")
screen.setup(width=1230, height=800)
screen.listen()
screen.tracer(0)

player_and_bullet = PlayerBullet()
player_and_bullet.create_player()


block = Shield()
block.create_blocks()

enemy = Enemy()
enemy.create_enemies()
enemy.create_enemy_bullet()
health = Health()
score = Score()

screen.onkeypress(fun=player_and_bullet.left, key="Left")
screen.onkeypress(fun=player_and_bullet.right, key="Right")
screen.onkeypress(fun=player_and_bullet.create_player_bullet, key="space")


def check_player_bullet_collide_with_enemy():
    for i in enemy.enemies:
        for j in player_and_bullet.bullet_list:
            if i.distance(j) < 30:
                i.reset()
                i.hideturtle()
                i.penup()
                i.goto(1000, 1000)

                j.reset()
                j.hideturtle()
                j.penup()
                j.goto(1000, 1000)
                score.reset_score()

                enemy.enemies.remove(i)

    if len(enemy.enemies) == 0:
        print("Game Over")
        print("All Aliens Destroyed")
        print(f"Your Score {score.SCORES}")
        exit()


def check_enemy_bullet_collide_with_block_and_player():
    flag = False
    x_pos =0
    for i in enemy.enemy_bullet_list:
        for j in block.blocks:
            if i.distance(j) < 40:
                # i.reset()
                # i.hideturtle()
                i.penup()
                i.goto(i.xcor(),-600)

                j.reset()
                j.hideturtle()
                j.penup()
                j.goto(1000, 1000)

                # enemy.enemy_bullet_list.remove(i)
                block.blocks.remove(j)

                flag = True
                x_pos -=20

        if i.distance(player_and_bullet.player) < 20:
            health.reset_health()
            if health.HEALTH == 0:
                print("Game Over")
                exit()

    # if flag == True:
    #     # pass
    #     enemy.create_enemy_bullet_one(x_pos)

while is_running:
    time.sleep(0.3)
    player_and_bullet.move_player_bullet()
    check_player_bullet_collide_with_enemy()
    check_enemy_bullet_collide_with_block_and_player()
    player_and_bullet.boundry_check()
    enemy.move_enemy_bullet()
    enemy.create_enemy_bullet_again()
    enemy.enemy_move()

    screen.update()

screen.exitonclick()
