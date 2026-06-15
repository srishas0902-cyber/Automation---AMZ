# Amazon Automation Test Suite

Automated test suite for Amazon product search and cart operations, built with **Python + Playwright + pytest-xdist** for true parallel execution.

---

## Features

| Feature | Detail |
|---|---|
| Language | Python 3.10+ |
| Framework | Playwright |
| Test runner | pytest + pytest-xdist |
| Pattern | Page Object Model (POM) |
| Parallelism | 2 workers (TC1 & TC2 simultaneously) |
| Cloud | LambdaTest integration (bonus) |

---

## Project Structure

```
amazon-automation/
├── config/
│   └── settings.py          # All config — local & LambdaTest
├── pages/
│   ├── base_page.py         # Shared helpers
│   ├── search_page.py       # Amazon search / home page
│   └── product_page.py      # Product detail page (PDP)
├── tests/
│   ├── test_iphone.py       # TC1 — iPhone search + cart
│   └── test_galaxy.py       # TC2 — Galaxy search + cart
├── utils/
│   ├── browser_factory.py   # Local & LambdaTest browser creation
│   └── logger.py            # Thread-safe console logger
├── conftest.py              # pytest fixtures
├── pytest.ini               # pytest config (parallel workers set here)
├── requirements.txt
└── .env.example             # Copy to .env and fill in values
```

---

## Quick Start (Local)

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/amazon-automation.git
cd amazon-automation
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install chromium        # Install browser binaries
```

### 4. Configure environment

```bash
cp .env.example .env
# Edit .env if you want to change BROWSER, HEADLESS, etc.
```

### 5. Run the tests (parallel)

```bash
pytest
```

Both test cases run **simultaneously** thanks to `pytest-xdist` (`-n 2` in `pytest.ini`).

### Run a single test

```bash
pytest tests/test_iphone.py -v
pytest tests/test_galaxy.py -v
```

### Run sequentially (no parallelism)

```bash
pytest -n 0
```

### Run in headed mode (watch the browser)

```bash
HEADLESS=false pytest -n 0
```

---

## Expected Console Output

```
[10:22:01.423] [TC1 - iPhone] Navigating to Amazon and searching for 'iPhone'
[10:22:01.431] [TC2 - Galaxy] Navigating to Amazon and searching for 'Samsung Galaxy phone'
[10:22:05.210] [TC1 - iPhone] Clicking first search result
[10:22:05.918] [TC2 - Galaxy] Clicking first search result
[10:22:09.123] [TC1 - iPhone] Product: Apple iPhone 15…
[10:22:09.340] [TC2 - Galaxy] Product: Samsung Galaxy S24…

============================================================
  [TC1 - iPhone] PRICE RETRIEVED: $799.00
============================================================

============================================================
  [TC2 - Galaxy] PRICE RETRIEVED: $699.99
============================================================

[10:22:12.001] [TC1 - iPhone] ✅ Test complete
[10:22:12.445] [TC2 - Galaxy] ✅ Test complete
```

---

## Bonus: LambdaTest Cloud Integration

### 1. Sign up

Create a free account at [lambdatest.com](https://www.lambdatest.com).

### 2. Get credentials

Go to **Profile → Username & Access Keys** and copy your username and access key.

### 3. Update `.env`

```env
USE_LAMBDATEST=true
LT_USERNAME=your_lt_username
LT_ACCESS_KEY=your_lt_access_key
```

### 4. Run on the cloud

```bash
pytest
```

Tests will appear in your LambdaTest dashboard at **Automation → Web Automation**.

> **Tip:** LambdaTest parallel concurrency depends on your plan. Free plans allow 1 concurrent session; upgrade or run `-n 1` if you hit limits.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `playwright install` fails | Run `playwright install --with-deps chromium` |
| Amazon shows CAPTCHA | Set `HEADLESS=false` and `SLOW_MO=500` |
| Price not found | Amazon occasionally A/B tests layouts; re-run |
| LambdaTest auth error | Double-check `LT_USERNAME` and `LT_ACCESS_KEY` in `.env` |

---

## Notes on Amazon Bot Detection

Amazon actively detects automation. The suite mitigates this by:
- Setting a real `User-Agent` header
- Disabling `AutomationControlled` Chromium flag
- Using `domcontentloaded` instead of `networkidle` (faster, less suspicious)

If you encounter CAPTCHAs consistently, run in headed mode first to warm up cookies.
