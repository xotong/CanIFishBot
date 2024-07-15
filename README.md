# CanIFish? Bot🎣🌦️‼️

CanIFishBot is a Telegram bot that allows fellow Anglers in Singapore to check on the weather conditions before heading out for their fishing journey.

## Features

Here are the main features of CanIFishBot:

- `/start` - Start the bot
- `/help` - Get help
- `/ystd_rainfall` - Get yesterday's total rainfall data by area
- `/today_rainfall` - Get today's total rainfall data by area
- `/2hr_forecast` - Get 2-hour weather forecast
- `/24hr_forecast` - Get 24-hour weather forecast
- `/tides` - Get tides data

## Prerequisites

Make sure you have the following prerequisites before running the bot:

- Python 3.9 or higher
- Docker (if you prefer running the bot in a container)

## Installation

### Clone the Repository

First, clone the repository:

```bash
git clone https://github.com/yourusername/CanIFishBot.git
cd CanIFishBot
```

### Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root directory to store the following environment variables:

- `TELE_CHANNEL_ID`: Obtain this from BotFather in Telegram
- `VISUALCROSSING_KEY`: Obtain this from VisualCrossing website after signing up

Example `.env` file:

```env
TELE_CHANNEL_ID=your_telegram_channel_id
VISUALCROSSING_KEY=your_visualcrossing_key
```

## Running the Bot

### Running Locally

To run the bot locally, use the following command:

```bash
python app/app.py
```

### Running with Docker

To run the bot using Docker, use the following commands:

```bash
docker build -t canifishbot:latest .
docker run --env-file .env canifishbot:latest
```

## Security

We have implemented several security measures, including:

- GitHub Actions for continuous integration and security scanning
- Tools used: CodeQL, OSV-Scanner, and Trivy

## Documentation

For more detailed documentation, visit [pytba.readthedocs.io](https://pytba.readthedocs.io/en/latest/index.html).

## Contributing

We welcome contributions to CanIFishBot! Here are some guidelines:

1. Fork the repository and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. Ensure the test suite passes.
4. Make sure your code lints.
5. Create a pull request and describe your changes.

## Contact

For support or collaboration, you can contact me via Telegram: [@XotOng](https://t.me/XotOng)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
