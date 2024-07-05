# Chess Game

## Overview

This project is a fully functional chess game developed using Python and the Pygame library. The game implements various Object-Oriented Programming (OOP) principles and contains multiple classes to handle different aspects of the game, such as `Move`, `Board`, `Square`, `Piece`, and `Dragger`.

## Features

- **Graphical User Interface (GUI)**: A user-friendly interface developed using Pygame.
- **Drag and Drop**: Intuitive piece movement using drag-and-drop functionality.
- **Move Validation**: Ensures that only legal moves can be made.
- **Different Classes**: OOP concepts are utilized with different classes for handling moves, board, squares, pieces, draggers, etc.

## Classes

### `Move`
Handles the logic for chess moves, including validation and execution.

### `Board`
Represents the chessboard and manages the placement of pieces, move validation, and board state.

### `Square`
Represents each individual square on the chessboard and its properties (e.g., occupied, piece present).

### `Piece`
Represents chess pieces with attributes like type (pawn, knight, etc.), color, and movement logic.

### `Dragger`
Manages the drag-and-drop functionality for moving pieces on the board.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/priyeshj1/chess-game.git
    cd chess-game
    ```

2. **Install the required dependencies**:
    ```sh
    pip install pygame
    ```

## Usage

1. **Run the game**:
    ```sh
    python main.py
    ```

2. **Game Controls**:
    - **Drag and Drop**: Click and hold a piece to drag it to a new square. Release the mouse button to drop the piece.
    - **Restart Game**: Press `R` to restart the game.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
