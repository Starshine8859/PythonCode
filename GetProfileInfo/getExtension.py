import os
import json

def list_profiles(base_path):
    """Detect all Chrome user profile directories"""
    profiles = []
    if not os.path.exists(base_path):
        print(f"Chrome base path does not exist: {base_path}")
        return profiles

    for entry in os.listdir(base_path):
        entry_path = os.path.join(base_path, entry)
        if os.path.isdir(entry_path) and (
            entry == "Default" or entry.startswith("Profile")
        ):
            profiles.append(entry)
    return profiles


def get_profile_name(profile_dir):
    """Read the profile display name from the Preferences file"""
    prefs_path = os.path.join(profile_dir, "Preferences")
    if not os.path.exists(prefs_path):
        return "Unknown"
    try:
        with open(prefs_path, "r", encoding="utf-8") as f:
            prefs = json.load(f)
        return prefs.get("profile", {}).get("name", "Unknown")
    except Exception as e:
        print(f"Error reading Preferences in {profile_dir}: {e}")
        return "Unknown"


def list_extensions_for_profile(profile_name, base_path):
    """List extensions installed in a specific Chrome profile"""
    extensions_path = os.path.join(base_path, profile_name, "Extensions")
    extensions = []

    if not os.path.exists(extensions_path):
        return []

    for ext_id in os.listdir(extensions_path):
        ext_dir = os.path.join(extensions_path, ext_id)
        if os.path.isdir(ext_dir):
            versions = os.listdir(ext_dir)
            if versions:
                latest_version = sorted(versions)[-1]
                manifest_path = os.path.join(ext_dir, latest_version, "manifest.json")
                if os.path.exists(manifest_path):
                    try:
                        with open(manifest_path, "r", encoding="utf-8") as f:
                            manifest = json.load(f)
                        extensions.append(
                            {
                                "id": ext_id,
                                "name": manifest.get("name", "Unknown"),
                                "version": manifest.get("version", "Unknown"),
                                "description": manifest.get("description", ""),
                            }
                        )
                    except Exception as e:
                        print(f"Error reading {manifest_path}: {e}")
    return extensions


# -------- Main Program --------

# Set the base path to Chrome's user data directory
# Adjust path if using Mac or Linux
base_path = os.path.expanduser(
    "~/AppData/Local/Google/Chrome/User Data"
)  # For Windows
# base_path = os.path.expanduser("~/.config/google-chrome")  # For Linux
# base_path = os.path.expanduser("~/Library/Application Support/Google/Chrome")  # macOS

profiles = list_profiles(base_path)

for profile in profiles:
    profile_dir = os.path.join(base_path, profile)
    profile_display_name = get_profile_name(profile_dir)
    print(f"\nExtensions in profile: {profile} (Name: {profile_display_name})")
    
    exts = list_extensions_for_profile(profile, base_path)
    if not exts:
        print("- No extensions found")
    else:
        for ext in exts:
            print(f"- {ext['name']} ({ext['id']}) v{ext['version']}")
