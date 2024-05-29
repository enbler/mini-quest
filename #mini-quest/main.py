from pgzero.screen import Screen
import pgzrun
from pgzero.builtins import Actor, mouse

cell = 20
size_w = 30  # Larghezza del campo in celle
size_h = 16  # Altezza del campo in celle
WIDTH = cell * size_w
HEIGHT = cell * size_h

TITLE = "mini-adventure"  # Titolo del tuo progetto
FPS = 30  # Numero di frame per secondo

background = Actor('background')
cell = Actor('platform')
char = Actor('right')
enem = Actor('enemy-r')
goal = Actor('goal')
spike = Actor('spike')

button1 = Actor('button', pos=(210, 300))
button2 = Actor('button', pos=(370, 300))

status = "start"
livello = 1
vite = 3

nemici = []
nemici_volanti = []

current_x = 2
current_y = 2

current_x_enem = 2
current_y_enem = 2

screen: Screen


def get_tables():
    table_1 = [
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 4],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1,
         -1]
    ]

    table_2 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 5, 0, 5, 0, 5, 0, 5, 0, 0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 5, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [1, 1, 5, 1, 0, 5, 0, 0, 0, 3, 0, 0, 0, 5, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1,
         -1]
    ]

    table_3 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 5, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 5, 0, 0, 0, 4],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 5, 5, 5, 1, 0, 0, 1, 0, 5, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1,
         -1]
    ]

    return table_1, table_2, table_3


tables = get_tables()
current_level_table = tables[0]


# SETUP

def crea_nemici():
    global nemici, current_level_table
    # controllo la mappa corrente e se numero == 3 creo un nemico
    for y in range(len(current_level_table)):
        for x in range(len(current_level_table[y])):
            if current_level_table[y][x] == 3:
                # associo al nemico i valori x, y, direzione
                nemico = Actor('enemy-r')  # creao un'istanza della classe Actor (un oggetto)
                nemico.posx = x
                nemico.posy = y
                nemico.direzione = "right"  # o left
                nemici.append(nemico)


def crea_nemici_volanti():
    global nemici_volanti, current_level_table
    # controllo la mappa corrente e se numero == 3 creo un nemico
    for y in range(len(current_level_table)):
        for x in range(len(current_level_table[y])):
            if current_level_table[y][x] == 6:
                # associo al nemico i valori x, y, direzione
                nemico = Actor('nemico-volante-r')  # creao un'istanza della classe Actor (un oggetto)
                nemico.posx = x
                nemico.posy = y
                nemico.direzione = "right"  # o left
                nemici_volanti.append(nemico)


# FUNCTIONS


def map_draw(c_l):
    """
        Draws the map based on the current level table.

        Args:
        c_l (list): A 2D list representing the current level table.

        Returns:
        None: This function does not return any value. It only draws the map on the screen.

        Raises:
        None: This function does not raise any exceptions.


        This function iterates through each row and column of the current level table. If an element in the table is greater than 0, it draws the corresponding object on the screen. The objects are represented by the following values:
            1: A cell
            2: The character
            3: An enemy
            4: The goal
            5: Stalagmite
        note: 0. do not draw

        The function uses the `draw` method of each object to render it on the screen. The `left` and `top` attributes of each object are set based on the position of the corresponding element in the current level table.
    """
    for i in range(len(c_l)):
        for j in range(len(c_l[i])):
            if c_l[i][j] > 0:
                if c_l[i][j] == 1:
                    cell.left = cell.width * j
                    cell.top = cell.height * i
                    cell.draw()
                if c_l[i][j] == 2:
                    char.left = cell.width * j
                    char.top = cell.height * i
                    char.draw()

                if c_l[i][j] == 4:
                    goal.left = cell.width * j
                    goal.top = cell.height * i
                    goal.draw()
                if c_l[i][j] == 5:
                    spike.left = cell.width * j
                    spike.top = cell.height * i
                    spike.draw()


def draw_buttons(text1, text2):
    button1.draw()
    screen.draw.text(f"{text1}", (185, 282), color="white", fontsize=25)
    button2.draw()
    screen.draw.text(f"{text2}", (353, 282), color="white", fontsize=25)


def draw():
    """
        Draws the game screen based on the current level.

        Args:
        None: This function does not require any arguments.

        Returns:
        None: This function does not return any value. It only draws the game screen.

        Raises:
        None: This function does not raise any exceptions.

        This function is responsible for drawing the game screen based on the current level. It first clears the screen with a dark purple color. Then, it checks if the game status is "game". If it is, it draws the background, sets the current level table, and then draws the map on the screen.
    """
    global status, livello, screen, livello, vite, button1, button2, current_level_table

    if status == "game":
        screen.fill("#55158a")
        background.image = "background"
        background.draw()
        map_draw(current_level_table)
        screen.draw.text(f"Livello {livello}", (10, 300), color="white", fontsize=25)
        screen.draw.text(f"Vite {vite}", (100, 300), color="white", fontsize=25)
        for nemico in nemici:
            nemico.left = cell.width * nemico.posx
            nemico.top = cell.height * nemico.posy
            nemico.draw()
        for nemico_volante in nemici_volanti:
            nemico_volante.left = cell.width * nemico_volante.posx
            nemico_volante.top = cell.height * nemico_volante.posy
            nemico_volante.draw()

    elif status == "victory":
        screen.fill("#000000")
        background.image = "vittoria"
        background.draw()
        draw_buttons("Riparti", "Esci")

    elif status == "game_over":
        screen.fill("#000000")
        background.image = "gover"
        background.draw()
        draw_buttons("Riprova", "Esci")

    elif status == "start":
        screen.fill("#000000")
        background.image = "start"
        background.draw()
        draw_buttons("Start", "Esci")


def muovi_char(new_x, new_y):
    global current_x, current_y, livello, current_level_table
    # anche se funziona non si usa chiamare una funzione che ritorna una tabella e agire direttamente perchè non si capisce cosa fa
    # meglio salvarla in una variabile e poi usare quella variabile

    if len(current_level_table[0]) - 1 < new_x < 0:
        # non puoi andare fuori dalla mappa
        return

    if current_level_table[new_y][new_x] == 0:
        current_level_table[current_y][current_x] = 0
        current_level_table[new_y][new_x] = 2
        current_x = new_x
        current_y = new_y


def muovi_enem(old_x, old_y, new_x, new_y):
    global current_level_table
    current_level_table[int(old_y)][int(old_x)] = 0  # imposto a 0 la cella attuale (sfondo)
    current_level_table[int(new_y)][int(new_x)] = 3  # imposto a 3 la cella nuova (nemico)


def my_on_key_up():
    # cercare il primo non zero sopra la cella attuale
    global current_level_table
    max_spostamento = 3
    for i in range(1, 4):
        if current_level_table[current_y - i][current_x] != 0:
            max_spostamento = i - 1
            break

    new_y = current_y - max_spostamento
    if new_y < 0:
        new_y = current_y
    muovi_char(current_x, new_y)


def check_fine():
    global current_x, current_y, status, livello, nemici, nemici_volanti, current_level_table
    if current_level_table[current_y - 1][current_x] == 4 and current_level_table[current_y + 1][current_x] == 4:
        reset(vite, livello + 1)
        return True

    return False


# noinspection DuplicatedCode
def move_enemies():
    global current_x, current_y, status, livello, nemici, vite, current_level_table

    for nemico in nemici:
        # per ogni nermico nella lista nemico

        if (current_level_table[int(nemico.posy)][int(nemico.posx) + 1] == 2 and nemico.direzione == "right") or (
                current_level_table[int(nemico.posy)][int(nemico.posx) - 1] == 2 and nemico.direzione == "left"):
            vite = vite - 1
            current_level_table[current_y][current_x] = 0
            current_level_table[2][2] = 2
            current_y, current_x = 2, 2
            if vite == 0:
                status = "game_over"
            return

        if current_level_table[int(nemico.posy)][int(nemico.posx) + 1] == 0 and not \
                current_level_table[int(nemico.posy) + 1][int(nemico.posx) + 1] == 0 and nemico.direzione == "right":
            muovi_enem(nemico.posx, nemico.posy, nemico.posx + 1, nemico.posy)
            nemico.posx = nemico.posx + 1

        elif current_level_table[int(nemico.posy)][int(nemico.posx) - 1] == 0 and not \
                current_level_table[int(nemico.posy) + 1][int(nemico.posx) - 1] == 0 and nemico.direzione == "left":
            muovi_enem(nemico.posx, nemico.posy, nemico.posx - 1, nemico.posy)
            nemico.posx = nemico.posx - 1

        else:
            # se right -> left e se left -> right

            if nemico.direzione == "right":
                nemico.direzione = "left"
                nemico.image = "enemy-l"
            else:
                nemico.direzione = "right"
                nemico.image = "enemy-r"


# noinspection DuplicatedCode
def move_nemici_volanti():
    global current_x, current_y, status, livello, nemici, vite, current_level_table

    for nemico in nemici_volanti:
        # per ogni nermico nella lista nemico
        # collide con il personaggio
        if (current_level_table[int(nemico.posy)][int(nemico.posx) + 1] == 2 and nemico.direzione == "right") or (
                current_level_table[int(nemico.posy)][int(nemico.posx) - 1] == 2 and nemico.direzione == "left"):
            vite = vite - 1
            current_level_table[current_y][current_x] = 0
            current_level_table[2][2] = 2
            current_y, current_x = 2, 2
            if vite == 0:
                status = "game_over"
            return

        if current_level_table[int(nemico.posy)][int(nemico.posx) + 1] == 0 and nemico.direzione == "right":
            muovi_enem(nemico.posx, nemico.posy, nemico.posx + 1, nemico.posy)
            nemico.posx = nemico.posx + 1

        elif current_level_table[int(nemico.posy)][int(nemico.posx) - 1] == 0 and nemico.direzione == "left":
            muovi_enem(nemico.posx, nemico.posy, nemico.posx - 1, nemico.posy)
            nemico.posx = nemico.posx - 1

        else:
            # se right -> left e se left -> right
            if nemico.direzione == "right":
                nemico.direzione = "left"
                nemico.image = "nemico-volante-l"
            else:
                nemico.direzione = "right"
                nemico.image = "nemico-volante-r"


def check_stalagmite():
    global current_x, current_y, status, livello, nemici, vite, current_level_table
    if current_level_table[current_y + 1][current_x] == 5:
        vite = vite - 1
        current_level_table[current_y][current_x] = 0
        current_level_table[2][2] = 2
        current_y, current_x = 2, 2
        if vite == 0:
            status = "game_over"
        return True

    return False


def check_keyboard(key):
    global current_level_table
    # se sopra e sotto ho una cella vuota -> c'è la gravità
    if current_level_table[current_y + 1][current_x] == 0 and current_level_table[current_y - 1][current_x] == 0:
        muovi_char(current_x, current_y + 1)

    if key == keys.RIGHT or key == keys.D:
        muovi_char(current_x + 1, current_y)
        char.image = "right"

    elif key == keys.LEFT or key == keys.A:
        muovi_char(current_x - 1, current_y)
        char.image = "left"

    elif key == keys.UP and current_level_table[current_y + 1][current_x] == 1:
        my_on_key_up()

    elif key == keys.DOWN and current_level_table[current_y + 1][current_x] == 0:
        muovi_char(current_x, current_y + 1)


def on_key_down(key):
    global current_x, current_y, status, keys, livello, nemici, vite, current_level_table

    move_enemies()

    move_nemici_volanti()

    check_keyboard(key, )

    if check_fine():
        return

    if check_stalagmite():
        return


def check_button_clicked(button_x, button_y, pos_x, pos_y):
    """
    Checks if the given position (pos_x, pos_y) is within the bounds of a button with the given coordinates (button_x, button_y) and width/height of 53/22.

    Args:
    button_x (int): The x-coordinate of the top-left corner of the button.
    button_y (int): The y-coordinate of the top-left corner of the button.
    pos_x (int): The x-coordinate of the position to check.
    pos_y (int): The y-coordinate of the position to check.

    Returns:
    bool: True if the position is within the bounds of the button, False otherwise.
    """
    if button_x < pos_x < button_x + 53 and button_y < pos_y < button_y + 22:
        return True
    else:
        return False


def reset(p_vite, p_livello):
    global status, vite, livello, nemici, nemici_volanti, current_y, current_x, tables, current_level_table

    vite = p_vite
    livello = p_livello

    if livello > 3:
        # vinci dopo 3 livelli
        status = "victory"
        return

    tables = get_tables()
    current_level_table = tables[livello - 1]

    nemici = []
    nemici_volanti = []

    crea_nemici()
    crea_nemici_volanti()

    current_x, current_y = 2, 2


def on_mouse_down(pos, button):
    global status, vite, livello, nemici, nemici_volanti, current_y, current_x

    if button == mouse.LEFT:
        if check_button_clicked(179, 279, pos[0], pos[1]):
            status = "game"
            reset(3, 1)
            return
        if check_button_clicked(335, 281, pos[0], pos[1]):
            exit()


pgzrun.go()
