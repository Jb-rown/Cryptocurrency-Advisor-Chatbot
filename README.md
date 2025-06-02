# CryptoBuddy: Cryptocurrency Advisor Chatbot

**CryptoBuddy** is a rule-based Python chatbot designed to provide cryptocurrency investment advice based on **profitability** (price trends, market cap) and **sustainability** (energy use, sustainability score). It uses a predefined dataset for core data and integrates real-time price trends and market cap data from the [CoinGecko API](https://www.coingecko.com/en/api/documentation). The chatbot offers a friendly, emoji-rich interface and includes an ethics disclaimer to promote responsible investing.

This project was developed as part of a Week 1 Assignment with the theme: *“Your First AI-Powered Financial Sidekick!”* 🌟 Built by a team of five, it combines modular code, API integration, and basic NLP for a robust user experience.

## Table of Contents
- [CryptoBuddy: Cryptocurrency Advisor Chatbot](#cryptobuddy-cryptocurrency-advisor-chatbot)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Project Structure](#project-structure)
    - [Key Files](#key-files)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Example Interaction](#example-interaction)
    - [Supported Queries](#supported-queries)
    - [Test Coverage](#test-coverage)
  - [Contributing](#contributing)

## Features
- **Investment Advice**: Recommends cryptocurrencies based on:
  - **Profitability**: Prioritizes coins with rising price trends and high market cap.
  - **Sustainability**: Highlights coins with low energy use and high sustainability scores (>7/10).
- **Real-Time Data**: Fetches price trends and market cap from CoinGecko API, with in-memory caching to optimize performance.
- **Conversational Interface**: Supports queries like:
  - “Which crypto is trending?”
  - “What’s the most sustainable coin?”
  - “Compare Bitcoin and Cardano.”
  - “Tell me a fun fact about Ethereum.”
- **Fun Facts & Motivation**: Provides crypto facts and motivational quotes.
- **Ethics Disclaimer**: Includes a warning: “Crypto is risky—always do your own research!”
- **Modular Design**: Organized code structure for maintainability and scalability.

## Project Structure
```
Crypto-advisor-chatbot/
├── chatbot.py           # Core chatbot logic with API integration
├── requirements.txt         # Project dependencies        
└── README.md              # documentation
```

### Key Files
- **chatbot.py**: Implements the `CryptoBuddy` class, handling user queries, recommendations, and real-time data integration
## Installation
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd CryptoBuddyProject
   ```
2. **Install Dependencies**:
   Ensure Python 3.8+ is installed, then install required packages:
   ```bash
   pip install -r requirements.txt
   ```
   Dependencies include:
   - `requests==2.31.0` (for API calls)
   - `nltk==3.8.1` (for NLP processing)
3. **Download NLTK Data**:
   Run the following in a Python shell to download NLTK resources:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```
4. **Run the Chatbot**:
   ```bash
   python run.py
   ```

## Usage
Start the chatbot by running:
```bash
python run.py
```
or directly:
```bash
python chatbot.py
```

### Example Interaction
```
👋 Hey there! I'm *CryptoBuddy*, your friendly crypto sidekick!
Ask me about trends, sustainability, coin comparisons, or cool crypto facts.
📢 Disclaimer: Crypto is risky—always do your own research!

🤖 You can ask me:
- What's the most sustainable coin?
- Which crypto is trending? (uses real-time data)
- Tell me a fun fact about Bitcoin.
- Compare Bitcoin and Cardano. (uses real-time data for trends and market cap)
- List all cryptos. (real-time data where available)
- Give me some motivation!
- Type 'exit' to quit.

You: Which crypto is trending?
CryptoBuddy: 📈 These cryptos are trending up (based on real-time data): Bitcoin, Cardano

You: What's the most sustainable coin?
CryptoBuddy: 🌱 Cardano is the most eco-friendly choice with a sustainability score of 8.0/10!

You: Compare Bitcoin and Ethereum
CryptoBuddy: 📊 Comparing Bitcoin vs Ethereum (real-time data where available):
  Price Trend: Bitcoin: rising | Ethereum: stable
  Market Cap: Bitcoin: high | Ethereum: high
  Energy Use: Bitcoin: high | Ethereum: medium
  Sustainability Score: Bitcoin: 0.3 | Ethereum: 0.6

You: Tell me a fun fact about Cardano
CryptoBuddy: 💡 Fun Fact about Cardano: Cardano uses a proof-of-stake model called Ouroboros, making it eco-friendly.

You: exit
CryptoBuddy: 👋 Bye for now! Stay smart with your investments!
```

### Supported Queries
- **Trending**: “Which crypto is trending?” (uses real-time price trends)
- **Sustainability**: “What’s the most sustainable coin?”
- **Investment**: “What should I buy?” or “What’s good for long-term growth?”
- **Comparison**: “Compare Bitcoin and Cardano” (real-time trends and market cap)
- **Facts**: “Tell me about Ethereum” or “Fun fact about Bitcoin”
- **List**: “List all cryptos” (real-time data where available)
- **Motivation**: “Give me some motivation”
- **Help**: “help” to see available commands




### Test Coverage
- **Chatbot Logic**: Tests recommendation logic for profitability and sustainability.
- **Data Processing**: Validates static data loading and API responses.
- **Edge Cases**: Checks handling of invalid queries and API failures.

## Contributing
1. Fork the repository and create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
2. Make changes and commit with descriptive messages (e.g., “Add API caching to data_processor.py”).
3. Push to your branch and create a pull request:
   ```bash
   git push origin feature/your-feature
   ```
4. The group admin will review and merge pull requests.

