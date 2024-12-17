import requests
import json
import re

def fetch_facebook_profile(phone_or_email):
    url = f"https://graph.facebook.com/v9.0/{phone_or_email}?fields=id,name,picture&access_token=your_facebook_access_token"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"https://facebook.com/{data['id']}"
    except Exception as e:
        print(f"Facebook API error: {e}")
    return None

def fetch_twitter_profile(phone_or_email):
    url = f"https://twitter.com/{phone_or_email}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return url
    except Exception as e:
        print(f"Twitter API error: {e}")
    return None

def fetch_instagram_profile(phone_or_email):
    url = f"https://www.instagram.com/{phone_or_email}/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return url
    except Exception as e:
        print(f"Instagram API error: {e}")
    return None

def fetch_social_profiles(phone_or_email):
    social_profiles = {
        "facebook": None,
        "twitter": None,
        "instagram": None,
    }
    
    # Check if input is phone or email
    if re.match(r"^[+]*[0-9]+$", phone_or_email):
        # Fetch social profiles using phone number
        social_profiles["facebook"] = fetch_facebook_profile(phone_or_email)
        social_profiles["twitter"] = fetch_twitter_profile(phone_or_email)
        social_profiles["instagram"] = fetch_instagram_profile(phone_or_email)
    elif re.match(r"[^@]+@[^@]+\.[^@]+", phone_or_email):
        # Fetch social profiles using email
        social_profiles["facebook"] = fetch_facebook_profile(phone_or_email)
        social_profiles["twitter"] = fetch_twitter_profile(phone_or_email)
        social_profiles["instagram"] = fetch_instagram_profile(phone_or_email)
    else:
        print("Invalid phone number or email.")
    
    return social_profiles

if __name__ == "__main__":
    print("Welcome to ConnectMe 👋")
    print("Helping you find social profiles effortlessly... 📱")
    
    phone_or_email = input("Enter the phone number or email to fetch profiles: ")
    profiles = fetch_social_profiles(phone_or_email)
    
    print("\nResults:")
    print(json.dumps(profiles, indent=4))
    
    print("\nFollow me on:")
    print(f"📘 Facebook: https://facebook.com/yourusername")
    print(f"📷 Instagram: https://instagram.com/yourusername")
