The latest release is available for download at: https://github.com/andywalden/esm_o365_cfg/releases/latest

Usage Example 
----------------------------------------------------
- Note the change of status after a number is entered.
******************************************************

    ============================================================
    This script will enable or disable Office 365 subscriptions.
    ============================================================
    Please enter the required data.

    The Tenant ID is listed under Azure Active Directory | Properties and labeled "Directory ID".
    Example: cb6997bf-4029-455f-9f7a-e76fee8881da

    Enter Tenant ID: cb6997bf-4029-455f-9f7a-e76fee8881da

    The Client Key is available after app registration and labeled "Application ID"App Registrations | <ESM App Name> | Application ID
    Example: 553dd2ba-251b-47d5-893d-2f7ab26adf19

    Enter Client Key: 975403d8-b1d3-49a7-ad4d-ead9c6d9c3a7

    The Secret Key is accessible only one time after the App has been registered:
    Example: D8perHbL9gAqx4vx5YbuffCDsvz2Pbdswey72FYRDNk=

    Enter Secret Key: XN7714rvZlRvoJ2scJ2y4ehNbEyUvgmoJ9Kq7qsikCg=

    Enter 1-5 to enable/disable subscriptions or 0 to exit
    1. Audit.AzureActiveDirectory: disabled
    2. Audit.Exchange: disabled
    3. Audit.General: disabled
    4. Audit.SharePoint: disabled
    5. DLP.All: enabled
    Enter 0-5: 1

    Enter 1-5 to enable/disable subscriptions or 0 to exit
    1. Audit.AzureActiveDirectory: enabled
    2. Audit.Exchange: disabled
    3. Audit.General: disabled
    4. Audit.SharePoint: disabled
    5. DLP.All: enabled
    Enter 0-5: 5

    Enter 1-5 to enable/disable subscriptions or 0 to exit
    1. Audit.AzureActiveDirectory: enabled
    2. Audit.Exchange: disabled
    3. Audit.General: disabled
    4. Audit.SharePoint: disabled
    5. DLP.All: disabled
    Enter 0-5: 3

    Enter 1-5 to enable/disable subscriptions or 0 to exit
    1. Audit.AzureActiveDirectory: enabled
    2. Audit.Exchange: disabled
    3. Audit.General: enabled
    4. Audit.SharePoint: disabled
    5. DLP.All: disabled
    Enter 0-5: 0
