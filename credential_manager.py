
# credential_manager.py - Credential Manager Tool

import json
import logging
from datetime import datetime, timedelta

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("credential_manager")

# Sample credential data (in production, this would connect to a user directory)
USER_CREDENTIALS = {
    "user1": {"password": "StrongPass#1", "last_updated": "2023-06-01"},
    "user2": {"password": "WeakPass", "last_updated": "2024-02-01"},
    "user3": {"password": "Password123!", "last_updated": "2023-12-15"},
    "user4": {"password": "StrongPass#2", "last_updated": "2024-04-01"},
    "user5": {"password": "StrongPass#1", "last_updated": "2024-03-01"}  # Reused password
}

# Check if password meets policy requirements
def check_password_strength(password):
    policy = config["credential_manager"]["allowed_password_strength"]
    if len(password) < policy["min_length"]:
        return False
    if policy["requires_uppercase"] and not any(char.isupper() for char in password):
        return False
    if policy["requires_digit"] and not any(char.isdigit() for char in password):
        return False
    if policy["requires_special"] and not any(char in "!@#$%^&*()-_=+{}[];:'",.<>?/`~" for char in password):
        return False
    return True

# Function to check for reused passwords
def check_password_reuse():
    passwords_seen = set()
    reuse_issues = []
    for user, credentials in USER_CREDENTIALS.items():
        if credentials["password"] in passwords_seen:
            reuse_issues.append(f"Password reused by {user}.")
        else:
            passwords_seen.add(credentials["password"])
    return reuse_issues

# Function to check credential expiration and strength
def check_credential_policies():
    issues = []
    expiration_days = config["credential_manager"]["credential_expiration_days"]
    alert_days = config["credential_manager"]["alert_before_expiration_days"]
    
    for user, credentials in USER_CREDENTIALS.items():
        last_updated = datetime.strptime(credentials["last_updated"], "%Y-%m-%d")
        expiration_date = last_updated + timedelta(days=expiration_days)
        days_until_expiration = (expiration_date - datetime.now()).days

        # Check expiration
        if days_until_expiration <= alert_days:
            issues.append(f"Credential for {user} will expire in {days_until_expiration} days.")
        
        # Check password strength
        if not check_password_strength(credentials["password"]):
            issues.append(f"Password for {user} does not meet strength requirements.")
    
    return issues

# Main function to run credential checks
def run_credential_manager():
    logger.info("Starting Credential Manager checks...")
    reuse_issues = check_password_reuse()
    policy_issues = check_credential_policies()
    all_issues = reuse_issues + policy_issues
    
    for issue in all_issues:
        logger.warning(issue)

    if all_issues:
        print("[ALERT] Credential policy issues detected.")

if __name__ == "__main__":
    run_credential_manager()
