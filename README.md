# Instagram Automation System

An automated system for managing Instagram accounts with features for authentication, SMS verification, and batch processing.

## Features

- Automated Instagram account login
- SMS verification integration via SMS PVA
- Batch account processing
- Proxy support
- Human-like behavior simulation
- Comprehensive error handling and logging

## Requirements

- Python 3.8+
- Playwright
- NST Browser API key
- SMS PVA API key

## Installation

1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd instagram-automation
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file with:
   ```text
   NST_BROWSER_API_KEY=your_api_key_here
   SMSPVA_API_KEY=your_api_key_here
   ```

## Usage

1. Configure account settings in `instagram_config.json` for the NST-based workflows.

2. **Batch processing (modern):**
   ```bash
   python new_file.py
   ```
   - Expects `accounts.txt` (username:password:email:email_password[:year]) and `profile_ids.txt` in the project root.

3. **Legacy batch processing:**
   ```bash
   python ig_auth_batch.py
   ```
   - Uses `accounts.txt` and `profile_ids.txt` as well.

4. **Single account testing:**
   ```bash
   python test.py
   ```

## Project Structure

- `new_file.py`: Batch login handler reading `accounts.txt` and `profile_ids.txt`.
- `ig_auth.py`: Core authentication logic for small batches.
- `ig_auth_batch.py`: Legacy batch account processing.
- `ig_setup.py`: Initial setup and configuration for NST Browser.
- `instagram_login.py`: Playwright sync/async Instagram login template.
- `instagramdms.py`: Direct messaging functionality via CSV input.
- `codegen_nst.py`: Helpers for launching and tracing NST Browser sessions.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

## Security Notes

- Never commit `.env` file or any files containing sensitive information.
- Store API keys and credentials securely.
- Use proxy servers when possible.
- Implement proper rate limiting.

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
