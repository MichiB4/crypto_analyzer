# crypto_analyzer
A simple Python application that fetches real-time cryptocurrency prices and creates interactive candlestick charts for technical analysis. For the HSG course "Programming with Advanced Computer Languages"

**Inspired by ChatGPT**

## Table of Contents
- [What This Program Does](#what-this-program-does)
- [Programming Language](#programming-language)
- [Features](#features)
- [Installation & Setup](#installation--setup)
- [How to Run the Program](#how-to-run-the-program)
- [Step-by-Step Usage Guide](#step-by-step-usage-guide)
- [Code Quality Features](#code-quality-features)
- [Supported Cryptocurrencies](#supported-cryptocurrencies)
- [Error Handling](#error-handling)
- [Troubleshooting](#troubleshooting)

# What This Program Does

This tool helps you analyze cryptocurrency market data.

It allows you to:

- **Fetch current prices** – Gets the latest USD prices for popular cryptocurrencies  
- **Display price information** – Shows a formatted table with current market values  
- **Create visual charts** – Generates candlestick charts to help analyze price movements  
- **Support multiple timeframes** – View data for 1 day, 7 days, 30 days, or 90 days  

Perfect for:

Students learning about financial data, cryptocurrency enthusiasts, or anyone interested in market analysis.

---

## Programming Language

**Python 3.7+**  
This program is written entirely in Python and uses popular data science libraries.

---

## Features

- Real-time data from CoinGecko API (free, no API key required)  
- Interactive menu system for easy navigation  
- Professional candlestick charts with green/red color coding  
- Multiple time periods (1, 7, 14, 30, 90 days)  
- Error handling for network issues and invalid inputs  
- Clean, readable code following Python best practices  
- Input validation to prevent crashes  

---

## Installation & Setup

### Step 1: Install Python

Make sure you have Python 3.7 or newer installed on your computer.

- **Windows/Mac**: Download from [python.org](https://www.python.org)
- **Linux**: Usually pre-installed, or use:

```bash
sudo apt install python3
```

---

### Step 2: Install Required Libraries

Open your terminal or command prompt and run:

```bash
pip install requests pandas matplotlib mplfinance
```

**What each library does:**

- `requests` – Downloads data from the internet  
- `pandas` – Handles data tables and calculations  
- `matplotlib` – Creates charts and graphs  
- `mplfinance` – Specialized library for financial candlestick charts  

---

### Step 3: Get the Code

#### Option A: For Jupyter Notebook (.ipynb)

- Download the `.ipynb` file to your computer  
- No additional setup needed  

#### Option B: For Python Script (.py)

- Save the provided Python code as `crypto_analyzer.py` on your computer  

---

## How to Run the Program

### Method 1: Jupyter Notebook (Recommended for `.ipynb` files)

1. Install Jupyter:
```bash
pip install jupyter
```

2. Open terminal/command prompt in the folder containing your notebook  
3. Run:
```bash
jupyter notebook
```

4. Click on your `.ipynb` file in the browser  
5. Run all cells:
   - Click “Cell” → “Run All”  
   - Or use `Shift + Enter` to run individual cells  

**Benefits of Jupyter:**
- Interactive execution – run code step by step  
- See outputs immediately below each cell  
- Perfect for data analysis and visualization  
- Easy to modify and experiment with the code  

---

### Method 2: Command Line (for `.py` files)

1. Open terminal/command prompt  
2. Navigate to the folder containing `crypto_analyzer.py`  
3. Run:
```bash
python crypto_analyzer.py
```

---

### Method 3: Python IDE

1. Open the file in any Python IDE (e.g., PyCharm, VS Code, IDLE)  
2. Click the “Run” button or press `F5`  

---

## Step-by-Step Usage Guide

### What You'll See When You Run the Program:

#### 1. **Current Prices Display**
```
===== Crypto Data =====
Prices as of 2025-05-25 14:30:15

Name          Symbol    Price
Bitcoin       BTC       $67,234.50
Ethereum      ETH       $3,845.20
XRP           XRP       $0.52
...
```

#### 2. **Cryptocurrency Selection Menu**
```
Select a cryptocurrency:

  1. Bitcoin (BTC)
  2. Ethereum (ETH)
  3. XRP (XRP)
  4. Binance Coin (BNB)
  5. Solana (SOL)
  ...

Enter choice [1-10]:
```
**What to do:** Type a number (1-10) and press Enter

#### 3. **Time Period Selection**
```
Select historical data period (days):

  1. 1
  2. 7
  3. 14
  4. 30
  5. 90

Enter choice [1-5]:
```
**What to do:** Choose how many days of price history you want to see

#### 4. **Chart Display**
A candlestick chart window will open showing:
- **Green candles** = Price went up that day
- **Red candles** = Price went down that day
- **X-axis** = Time (dates or hours)
- **Y-axis** = Price in USD

---

## Code Quality Features

This program demonstrates following coding practices:

### **Function Design**
- Each function has a single, defined purpose
- Descriptive function and variable names
- Type hints for better code documentation

### **Error Handling**
- Network connection failures are caught and handled
- Invalid user inputs are validated
- API errors are managed
- Program exits cleanly with error messages

### **Input Validation**
- Menu selections are validated (must be numbers in valid range)
- Non-integer inputs are handled without crashing
- Empty or invalid API responses are checked

### **Documentation**
- Detailed docstrings explain what each function does
- Comments explain complex logic
- Clear variable names that explain their purpose

### **Separation of Concerns**
- Data fetching is separate from data display
- Chart creation is isolated from user interaction
- Each function handles one specific task

---

## Error Handling

The program handles these common issues:

### **Network Problems**
- **Issue:** No internet connection
- **Response:** "Error fetching current prices: [connection details]"
- **Action:** Check your internet and try again

### **Invalid Menu Selections**
- **Issue:** User enters letters instead of numbers
- **Response:** "Invalid input; please enter a number."
- **Action:** Program asks again without crashing

### **API Issues**
- **Issue:** CoinGecko API is down or returns no data
- **Response:** "No historical data returned."
- **Action:** Program exits with explanation

### **Out of Range Selections**
- **Issue:** User enters number outside valid range
- **Response:** "Please enter a number between 1 and [max]."
- **Action:** Program prompts again

---

## Troubleshooting

### **"Module not found" error**
```bash
pip install --upgrade pip
pip install requests pandas matplotlib mplfinance
```

### **Charts not displaying**
- Make sure you have a graphical interface (not running on a server)
- On Linux, you might need: `sudo apt install python3-tk`

### **Slow performance**
- This is normal (the program downloads data from the internet)
- Wait a few seconds for charts to load

### **API rate limits**
- CoinGecko allows many free requests per minute
- If you get rate limited, wait a minute and try again

---

## Learning Opportunities

This code demonstrates several programming concepts like:
- **API integration** - How to fetch data from web services
- **Data manipulation** - Using pandas for data processing
- **Error handling** - Failure management
- **User interaction** - Menu systems and input validation
- **Data visualization** - Creating professional charts
- **Code organization** - Maintainable code structure

---

## Credits
- Inspired by ChatGPT
- Data provided by [CoinGecko API](https://www.coingecko.com/en/api)
- Inspired by modern financial analysis tools
- Built with coding best practices in mind



