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
```
NST_BROWSER_API_KEY=your_api_key_here
SMSPVA_API_KEY=your_api_key_here
```

## Usage

1. Configure account settings in `instagram_config.json`
2. Run batch processing:
```bash
python ig_auth_batch.py
```

3. For single account testing:
```bash
python test.py
```

## Project Structure

- `ig_auth.py`: Core authentication logic
- `ig_auth_batch.py`: Batch account processing
- `ig_setup.py`: Initial setup and configuration
- `instagram_login.py`: Login handling
- `instagramdms.py`: Direct messaging functionality

## Security Notes

- Never commit `.env` file or any files containing sensitive information
- Store API keys and credentials securely
- Use proxy servers when possible
- Implement proper rate limiting

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
