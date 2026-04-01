# Test Coverage Analysis

## Current State: Zero Test Coverage

The codebase has **6 Python modules** (~250 lines of code) with no tests, no test framework, and no coverage tooling.

---

## Priority Areas for Test Improvement

### 1. `golge_ticaret.py` — CRITICAL (Trading Engine)

The core business logic module. Needs:

- **SMA calculation tests** — Verify average calculation from candlestick data
- **Buy signal logic** — Buy triggers when `anlik_fiyat <= sma_15 * 0.999` and USDT > 0
- **Sell signal logic** — Sell triggers when `anlik_fiyat >= son_alim_fiyati * 1.001` and SOL > 0
- **Portfolio state management** — Correct balance updates after buy/sell
- **Edge cases** — Empty `kapanislar` list (division by zero, line 27), zero `son_alim_fiyati`
- **Profit/loss calculation** — Line 60 hardcodes `100.0` as initial balance

**Recommended refactor**: Extract pure functions from the infinite loop:
- `calculate_sma(closing_prices) -> float`
- `should_buy(price, sma, kasa) -> bool`
- `should_sell(price, kasa) -> bool`
- `execute_buy(price, kasa) -> dict`
- `execute_sell(price, kasa) -> dict`

### 2. `ticaret_beyni.py` — HIGH (Market Intelligence)

- **Price parsing** — Extract price from Binance JSON response
- **Profit calculation** — `amount_in_sol * sol_price`
- **Error handling** — Non-200 API status codes

### 3. `sensor.py` — MEDIUM (Balance Monitor)

- **Lamport-to-SOL conversion** — `lamports / 1_000_000_000`
- **Missing env var** — Guard when `TWIN_PUBLIC_KEY` is unset
- **Balance detection** — `sol_balance > 0` vs waiting branch

### 4. `kimlik.py` — MEDIUM (Identity Creation)

- **Keypair generation** — Valid Solana keypair produced
- **Base58 encoding** — Round-trip encode/decode of private key
- **File output** — `.env` written with correct format (mock file I/O)

### 5. `uyanis.py` — LOW (Initialization)

- **Connection success/failure paths** — Mock `is_connected()`

### 6. `airdrop.py` — LOW (Devnet Airdrop)

- **Parameterized wallet key** — Currently hardcoded
- **Success/failure paths** — Mock airdrop request

---

## Bugs & Risks Found

| Issue | File | Line | Severity |
|-------|------|------|----------|
| Division by zero if `grafik_verisi` is empty | `golge_ticaret.py` | 27 | **High** |
| Profit calc hardcodes initial balance as 100 | `golge_ticaret.py` | 60 | Medium |
| Global mutable state (`kasa` dict) | `golge_ticaret.py` | 6-10 | Medium |
| Hardcoded wallet public key | `airdrop.py` | 9 | Low |
| No `requirements.txt` | — | — | Medium |

---

## Recommended Test Infrastructure

1. **`pytest` + `pytest-asyncio`** — async test support
2. **`pytest-cov`** — coverage reporting
3. **`aioresponses`** — mock `aiohttp` calls (Binance API)
4. **`unittest.mock`** — mock Solana RPC calls
5. **`requirements.txt`** and **`requirements-dev.txt`**
6. **`pyproject.toml`** with pytest configuration
