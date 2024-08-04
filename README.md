# PokePic - Pokémon Artwork Generator

PokePic is a web application that allows users to generate Pokémon artwork using the OpenAI API. Users can input a Pokémon name, and the app will create realistic, colorful artwork of the specified Pokémon. The application also features a gallery of generated images and a leaderboard displaying the most generated Pokémon.

## Features

- **Random Pokémon Generation**: Generate random Pokémon artwork.
- **Search by Name**: Enter a Pokémon name to generate its artwork.
- **Artwork Gallery**: View previously generated artworks.
- **Leaderboard**: See the most generated Pokémon.

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip

### Clone the Repository

```bash
git clone https://github.com/eileenpaula/PokeAPI_Artwork.git
cd PokeAPI_Artwork
```

### Install Dependencies

Use the following command to install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

#### Generating Artwork with `pokeapi-artwork.py`

Run the script to generate artwork interactively:

```bash
python pokeapi-artwork.py
```

#### Running the Web Application (`app.py`)

To start the Flask application, run:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`.

### Application Endpoints

- **Home Page**: `http://127.0.0.1:5000/` - Generate Pokémon artwork.
- **Gallery**: `http://127.0.0.1:5000/gallery` - View the gallery of generated artworks.

## Project Structure

- `pokeapi-artwork.py`: Script for generating Pokémon artwork using the OpenAI API in a command-line interface.
- `app.py`: The main Flask application file for the web interface.
- `templates/`: Directory containing HTML templates.
- `static/`: Directory containing static files like CSS and JavaScript.
- `requirements.txt`: Python dependencies.

## Dependencies

The project relies on the following dependencies:

- `click==8.1.3`
- `email_validator==2.0.0.post2`
- `Flask==2.3.2`
- `flask_behind_proxy==0.1.1`
- `flask_sqlalchemy==3.0.5`
- `Flask-WTF==1.1.1`
- `GitPython==3.1.31`
- `itsdangerous==2.1.2`
- `Jinja2==3.1.2`
- `MarkupSafe==2.1.3`
- `pycodestyle`
- `pytest`
- `Werkzeug==2.3.6`

## Acknowledgements

- Thanks to OpenAI for providing the API for generating artwork.
- Pokémon data is provided by [PokeAPI](https://pokeapi.co/).
