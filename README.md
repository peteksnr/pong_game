# Pong Game 🏓

A simple Pong-style game built with Python's `turtle` module. Two paddles bounce a ball back and forth—earn points when your opponent misses the ball.

## 🎯 Features
- Two paddles (left & right) controlled by keyboard
- Ball with collision detection (paddles & walls)
- Score tracking for both players
- Adjustable ball speed/direction
- Classic Pong rules

## 🕹️ Controls
- **Right Paddle:**
  - **Up Arrow** — Move paddle up
  - **Down Arrow** — Move paddle down
- **Left Paddle:**
  - **W** — Move paddle up
  - **S** — Move paddle down

## 📂 Project Structure
```
.
├── main.py          # Entry point: sets up game screen, paddles, ball, scoreboard
├── paddle.py        # Paddle class: movement methods
├── ball.py          # Ball class: movement & collision behavior
├── scoreboard.py    # Scoreboard class: tracks and displays scores
```
> Game ends when you decide—keep playing as long as you want.

## 🧰 Requirements
- **Python 3.8+**
- Uses only Python’s built-in `turtle` module

## 🚀 Run Locally
1. Make sure all `.py` files are in the same directory.
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # macOS/Linux
   source venv/bin/activate
   # Windows
   .\venv\Scripts\Activate.ps1
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## ⚙️ How It Works
1. `main.py` sets up the screen and creates **Paddle** objects for both players, a **Ball**, and a **Scoreboard**.
2. The game loop:
   - Moves the ball automatically.
   - Detects collisions with walls (bounce vertically) and paddles (bounce horizontally).
   - Awards points when the ball passes a paddle.
   - Resets ball position and speed after a point.
3. `paddle.py` controls paddle movement within boundaries.
4. `ball.py` controls speed, bounce logic, and reset.
5. `scoreboard.py` displays the scores for both players.

## 🎨 Customization
- **Ball speed:** Change the ball’s movement speed in `ball.py`.
- **Paddle size:** Adjust `stretch_wid` in `paddle.py`.
- **Winning condition:** You can stop the game after a set score.

## 🧪 Common Issues & Fixes
- **Paddles moving off-screen** → Ensure boundary checks exist in `paddle.py`.
- **Ball moving too fast/slow** → Adjust `move_speed` in `ball.py`.
- **Keys not working** → Ensure `screen.listen()` and `screen.onkey()` calls exist.

