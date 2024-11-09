
# access_control_dashboard.py - Access Control Dashboard Tool

import json
import logging
from logging_config import setup_logging

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Initialize logging
setup_logging("access_control_dashboard.log")
logger = logging.getLogger(__name__)

# Sample user roles and permissions data (in production, this would come from an external source)
USER_ROLES = {
    "user1": ["user"],
    "user2": ["admin", "user"],
    "user3": ["superuser", "admin"],
    "user4": ["guest"],
    "user5": ["user", "manager"]
}

# Function to check for high-risk configurations
def check_high_risk_roles(user_roles):
    issues = []
    for user, roles in user_roles.items():
        for role in roles:
            if role in config["access_control"]["high_risk_roles"] and "mfa" not in roles:
                issues.append(f"User {user} has high-risk role {role} without MFA enabled.")
    return issues

# Function to log issues and send alerts if needed
def log_and_alert_issues(issues):
    for issue in issues:
        logger.warning(issue)

    # Send alert if critical issues found (placeholder)
    if issues:
        print("[ALERT] High-risk configurations detected.")

# Main function to run access control checks
def run_access_control_dashboard():
    logger.info("Starting Access Control Dashboard checks...")
    high_risk_issues = check_high_risk_roles(USER_ROLES)
    log_and_alert_issues(high_risk_issues)

if __name__ == "__main__":
    run_access_control_dashboard()
