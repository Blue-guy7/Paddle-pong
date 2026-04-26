# Pong Game

A classic Pong game implementation using Python's Turtle graphics library. Experience the nostalgic arcade game with smooth gameplay, responsive controls, and score tracking.

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Game Features

• **Classic Pong gameplay** with two paddles and a bouncing ball
• **Responsive controls** for both players
• **Real-time score tracking** with automatic game-over detection
• **Dynamic ball physics** with wall bouncing and paddle collision
• **Speed acceleration** as the game progresses
• **Clean, retro-style graphics** with a black background and white elements

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Turtle graphics library (included with Python)

### Run the Source Code
```bash
git clone https://github.com/Blue-guy7/Paddle-pong.git
cd Paddle-pong
python main.py
```

## 🚀 Play the Game

* **Play in Browser:** (https://ball-game--nilangshugangul.replit.app/) *(Zero setup required)*
* **Download Desktop Version:**(https://github.com/Blue-guy7/Paddle-pong/releases/tag/v1.0.0) *(Standalone .exe for Windows)*
  
## How to Play

### Controls

**Left Player:**
• `W` - Move paddle up
• `S` - Move paddle down

**Right Player:**
• `↑` (Up Arrow) - Move paddle up  
• `↓` (Down Arrow) - Move paddle down

### Game Rules

• Each player controls a paddle to hit the ball back and forth
• Score a point when the ball passes your opponent's paddle
• First player to reach **10 points** wins the game
• Ball speed increases slightly after each paddle hit
• Game ends automatically when a player reaches the winning score

## Project Structure

```
Paddle-pong/
│
├── main.py          # Main game loop and setup
├── ball.py          # Ball class with physics and movement
├── paddlef.py       # Paddle class with controls
├── scoreboard.py    # Score tracking and game-over logic
└── README.md        # Project documentation
```

## Technical Details

### Classes Overview

• **Ball**: Handles ball movement, collision detection, and physics
• **Paddle**: Manages paddle positioning and movement controls  
• **Scoreboard**: Tracks and displays scores, handles game-over conditions

### Key Features Implementation

• **Collision Detection**: Uses distance calculation between ball and paddles
• **Ball Physics**: Implements realistic bouncing off walls and paddles
• **Random Start**: Ball begins each round with a random direction
• **Smooth Animation**: Uses screen.tracer(0) and screen.update() for fluid motion

## Customization

You can easily customize the game by modifying these parameters in `main.py`:

• **Screen size**: Change `screen.setup(1000,600)` values
• **Ball speed**: Modify the `ball.forward(8)` value
• **Paddle speed**: Adjust the `45` value in `Up()` and `Down()` methods
• **Winning score**: Change the `10` in `game_over()` method
• **Colors**: Modify color values in each class

## Known Issues

• Speed acceleration could make the game too fast in extended play

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

• Inspired by the original Pong arcade game by Atari
• Built with Python's Turtle graphics for educational purposes

---

**Enjoy the game!** Click anywhere on the game window to exit when finished.
