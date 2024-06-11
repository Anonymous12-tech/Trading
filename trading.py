import yfinance as yf
import matplotlib.pyplot as plt

# List of 25 famous companies and their stock symbols
companies = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Google': 'GOOGL',
    'Facebook': 'META',
    'Tesla': 'TSLA',
    'Berkshire Hathaway': 'BRK-B',
    'Johnson & Johnson': 'JNJ',
    'Walmart': 'WMT',
    'JPMorgan Chase': 'JPM',
    'Visa': 'V',
    'Procter & Gamble': 'PG',
    'Mastercard': 'MA',
    'UnitedHealth': 'UNH',
    'NVIDIA': 'NVDA',
    'Home Depot': 'HD',
    'Disney': 'DIS',
    'PayPal': 'PYPL',
    'Intel': 'INTC',
    'Netflix': 'NFLX',
    'Coca-Cola': 'KO',
    'PepsiCo': 'PEP',
    'AbbVie': 'ABBV',
    'Adobe': 'ADBE',
    'Cisco': 'CSCO',
    'Tata Steel':'TATASTEEL.NS'
}

def display_menu():
    print("Select a company to view its current stock information:")
    for i, company in enumerate(companies.keys(), start=1):
        print(f"{i}. {company}")

def get_stock_info(symbol):
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1d")
        current_price = hist['Close'].iloc[-1] if not hist.empty else 'N/A'
        info = stock.info
        return {
            'Current Price': current_price,
            'Market Cap': info.get('marketCap', 'N/A'),
            '52 Week High': info.get('fiftyTwoWeekHigh', 'N/A'),
            '52 Week Low': info.get('fiftyTwoWeekLow', 'N/A'),
            'Volume': info.get('volume', 'N/A')
        }
    except Exception as e:
        print(f"Error retrieving data for {symbol}: {e}")
        return {
            'Current Price': 'N/A',
            'Market Cap': 'N/A',
            '52 Week High': 'N/A',
            '52 Week Low': 'N/A',
            'Volume': 'N/A'
        }

def plot_stock_history(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="max")  # 1 year history
    plt.figure(figsize=(10, 5))
    plt.plot(hist.index, hist['Close'], label='Close Price')
    plt.title(f'Stock Price History for {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter the number of the company (1-26): "))
            if 1 <= choice <= 26:
                company_name = list(companies.keys())[choice - 1]
                symbol = companies[company_name]
                info = get_stock_info(symbol)
                print(f"\nStock information for {company_name} ({symbol}):")
                for key, value in info.items():
                    print(f"{key}: {value}")

                # Plot the stock history
                plot_stock_history(symbol)
                break
            else:
                print("Invalid choice. Please select a number between 1 and 26.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 26.")

if __name__ == "__main__":
    main()
