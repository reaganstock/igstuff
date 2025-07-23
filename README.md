# Instagram Automation System

An automated system for managing Instagram accounts with features for authentication, SMS verification, batch processing, direct messaging, and more.

## Features

- Automated Instagram account login and verification
- SMS verification integration via SMS PVA (see `smspva.md`)
- Batch account processing (`ig_auth_batch.py`, `new_file.py`)
- Direct messaging to users from CSV (`instagramdms.py`)
- Human-like behavior simulation with random delays
- Comprehensive error handling and logging

## Requirements

- Python 3.8+
- Playwright (`pip install playwright`)
- NST Browser API key (will be prompted at runtime)
- SMSPVA API key (will be prompted at runtime)

## Installation

1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd instagram-automation
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

> Note: API keys are not read from a `.env` file—each script will prompt you for your NST Browser and/or SMSPVA API key at runtime.

## Usage

### NST Browser setup & configuration

1. Configure your account updates, posts, and follow list in `instagram_config.json`.
2. Run the setup and automation flows:
   ```bash
   python ig_setup.py
   ```
   You will be prompted for your NST Browser profile ID and API key.

### Batch login & verification

```bash
python ig_auth_batch.py
```

This script reads `accounts.txt` and `profile_ids.txt`, prompts for your NST Browser and SMSPVA API keys, and handles login and verification for multiple accounts.

### Send Direct Messages

```bash
python instagramdms.py
```

Follow the prompts to enter your CSV file path, username and message column names, NST Browser profile ID, and API key.

### Account creation & alternate batch flow

```bash
python new_file.py
```

Processes lines in `accounts.txt` (username:password:email:email_password[:year]) and `profile_ids.txt` to launch parallel login attempts.

### Single-account testing flow

```bash
python test.py
```

Prompts for API key and runs the recovery or login test sequence.

### Codegen & tracing helper

```bash
python codegen_nst.py [--codegen]
```

Launches or connects to NST Browser profiles and optionally starts Playwright codegen or tracing.

## Project Structure

- `ig_setup.py`          – Setup, session loading, delete/update content, create posts, follow users
- `ig_auth.py`           – Core Instagram authentication logic
- `ig_auth_batch.py`     – Batch login and SMS verification using SMS PVA
- `new_file.py`          – Alternate batch login flow (`InstagramAccount.from_line`)
- `instagram_login.py`   – Sync/async login manager with logging placeholders
- `instagramdms.py`      – CSV-based direct messaging automation
- `test.py`              – Single-account test and recovery flow
- `codegen_nst.py`       – Helper for Playwright codegen and tracing
- `smspva.md`            – SMS PVA API reference documentation
- `instagram_config.json`– Example configuration for `ig_setup.py`
- `requirements.txt`     – Python dependencies

## Security Notes

- Do not commit files containing secrets or API keys.
- Use secure storage for credentials if automating in production.
- Implement proper rate limiting to avoid service bans.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
