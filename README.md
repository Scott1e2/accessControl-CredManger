# accessControl-CredManger
putting together some ideas from an old project that was very IAM heavy



# initialize the Access Control Dashboard and Credential Manager Tool (version 1)

## Overview
This project provides two tools to enhance security posture:
1. **Access Control Dashboard**: Monitors user roles and permissions, ensuring that high-risk roles like admin accounts are configured securely with MFA and other access controls.
2. **Credential Manager Tool**: Manages credential lifecycle policies, ensuring password strength, preventing password reuse, and alerting users before credential expiration.

## Features
### Access Control Dashboard
- **High-Risk Role Detection**: Identifies users with roles that require multi-factor authentication (MFA).
- **Periodic Access Review**: Configured to run access control checks at a defined frequency.
- **Logging and Alerts**: Logs detected issues and generates alerts for critical findings.

### Credential Manager Tool
- **Password Policy Enforcement**: Ensures passwords meet minimum strength requirements.
- **Password Reuse Detection**: Detects reused passwords across accounts.
- **Credential Expiration Management**: Tracks expiration and alerts users in advance of expiration deadlines.

## Installation
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repository/access-control-credential-manager-tool.git
    cd access-control-credential-manager-tool
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configuration**:
   - Open `config.json` to set up user roles, high-risk role definitions, MFA requirements, credential expiration policies, and password strength settings.
   - Adjust thresholds, review frequency, and password settings as necessary.

## Usage
1. **Run the Access Control Dashboard**:
    ```bash
    python access_control_dashboard.py
    ```
   - Scans user permissions, logs any high-risk role issues, and alerts if critical issues are found.

2. **Run the Credential Manager Tool**:
    ```bash
    python credential_manager.py
    ```
   - Checks for password policy violations, expiration, and reuse issues, logging and alerting as configured.

## Configuration File (`config.json`)
The configuration file allows customization for both tools. Key fields include:
- **Access Control Settings**:
  - `"mfa_required_roles"`: Specifies roles requiring MFA.
  - `"high_risk_roles"`: Defines roles considered high risk.
  - `"review_frequency"`: Sets the frequency for access reviews.

- **Credential Manager Settings**:
  - `"credential_expiration_days"`: Defines the number of days before a credential expires.
  - `"alert_before_expiration_days"`: Number of days before expiration to send alerts.
  - `"allowed_password_strength"`: Configures password requirements (length, uppercase, digits, special characters).

## Example Configuration
```json
{
    "access_control": {
        "mfa_required_roles": ["admin", "superuser"],
        "high_risk_roles": ["admin", "root"],
        "review_frequency": "monthly"
    },
    "credential_manager": {
        "credential_expiration_days": 90,
        "password_reuse_check": true,
        "weak_password_check": true,
        "alert_before_expiration_days": 14,
        "allowed_password_strength": {
            "min_length": 8,
            "requires_uppercase": true,
            "requires_digit": true,
            "requires_special": true
        }
    }
}
```

## License
This project is licensed under the MIT License.

## Support
For issues or suggestions, please open an issue on the GitHub repository.
