# PII Detection Bot

## Overview

The PII Detection Bot is a sophisticated Python-based tool designed to identify and report Personally Identifiable Information (PII) within Hack Club Bank's open-source repositories. Its primary goal is to enhance privacy and security by automatically scanning issues and pull requests for sensitive information that should not be publicly accessible. By leveraging advanced natural language processing (NLP) techniques, this bot ensures that contributors' and users' personal data remain protected, aligning with the best practices for data privacy.

## Features

- **Automated Scanning**: Scans all issues and pull requests in specified GitHub repositories for potential PII.
- **NLP Powered**: Utilizes the Spacy NLP library to accurately identify various types of PII, including names, organizations, locations, dates, and more.
- **Secure Authentication**: Accesses GitHub repositories securely using OAuth tokens, ensuring that the bot's operations are both safe and compliant with GitHub's API usage policies.
- **Environment Variable Integration**: Leverages environment variables for secure token management, preventing sensitive information from being hard-coded into the script.
- **Customizable PII Entities**: Offers the flexibility to define and modify the types of PII the bot is on the lookout for, making it adaptable to different privacy requirements.
- **Detailed Reporting**: Provides detailed logs of detected PII instances, including the type of data found and the exact location within the repository, facilitating quick and efficient remediation.

## How It Works

1. **Initialization**: The bot starts by loading necessary dependencies, including the Spacy NLP library for PII detection and the `dotenv` package for environment variable management.
2. **Authentication**: Utilizes a GitHub OAuth token stored as an environment variable to securely authenticate with the GitHub API.
3. **Scanning Process**: The bot fetches issues and pull requests from the specified repository and scans each item's description for PII using the Spacy NLP library.
4. **Detection and Reporting**: Upon detecting PII, the bot constructs a detailed report indicating the type of PII found, its location, and provides a direct link to the issue or pull request for further action.

## Setup and Configuration

1. **Environment Setup**: Ensure Python 3.6+ is installed along with the `requests`, `json`, `spacy`, and `python-dotenv` packages.
2. **Spacy Model**: Download the Spacy NLP model with `python -m spacy download en_core_web_sm`.
3. **Environment Variables**: Create a `.env` file in the root directory and add your GitHub OAuth token as `GITHUB_TOKEN=your_token_here`.
4. **Running the Bot**: Execute the script with `python pii.py` to start scanning for PII in the configured repository.

## Contribution Guidelines

Contributions are welcome! If you're looking to contribute, please follow these steps:

- **Fork the Repository**: Start by forking the repository to your GitHub account.
- **Create a New Branch**: Make your changes in a new branch named after the feature or fix you're working on.
- **Submit a Pull Request**: Once you've made your changes, submit a pull request for review.

Please ensure your contributions adhere to the project's coding standards and are accompanied by appropriate tests (if applicable).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- The Hack Club Bank team for their commitment to open-source and privacy.
- The contributors and maintainers of the Spacy NLP library.
- All contributors to this project, whose efforts continue to improve privacy and security for the community.