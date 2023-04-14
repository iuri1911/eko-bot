# Eko Bot: Multipurpose GPT-Powered Chatbot

![Eko Bot Banner](https://media.discordapp.net/attachments/1096154265745096736/1096530263250583682/image.png)

*The image above shows the bot responding to a question about a recent event, which was added to its database.*

## About the Project

Eko Bot is a powerful and versatile chatbot developed in Python, capable of extracting and assimilating information from APIs, chat services, and cloud storage services like Google Drive and OneDrive. By combining the power of GPT and vector databases, Eko Bot can provide context-aware and meaningful responses based on the integrated data sources. Integrated with Discord, Eko Bot utilizes Llama Index to generate responses based on the content of the text file and other data sources.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Structure](#structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

1. Clone the repository:
```shell
git clone https://github.com/iuri1911/eko-bot.git
```

2. Install the required dependencies using Poetry:
```shell
poetry install

```

3. Create a `.env` file in the project root with the following environment variables:
```makefile
GPT_API_KEY=<your_gpt_api_key>
DISCORD_BOT_TOKEN=<your_discord_bot_token>
```

## Usage

1. Run the bot using Poetry:
```makefile
poetry run python bot.py
```

2. The bot will now be active on your Discord server. You can ask the bot a question using the `!ask` command followed by your question:
```makefile
!ask What is the capital of France?
```


## Structure

- `context_data/data/data.txt`: The source text file containing the data used by the chatbot to generate responses.
- `.env`: A file containing the required environment variables.
- `bot.py`: The main Python script that contains the code for the Discord bot and Llama Index integration.
- `index.json`: A file containing the vectorized output of the `data.txt` file.
- `pyproject.toml`: The configuration file for the project, containing metadata, dependencies, and build information.

## Credits

This project was developed by Iuri Ribeiro. You can find him on most social media platforms as [@iuri1911](https://www.linkedin.com/in/iuri1911/).
