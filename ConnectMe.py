import requests
import json
import re

def fetch_facebook_profile(phone_or_email):
    url = f"https://graph.facebook.com/v9.0/{phone_or_email}?fields=id,name&access_token=your_facebook_access_token"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"https://facebook.com/{data['id']}" if 'id' in data else None, data['name'] if 'name' in data else None
    except Exception as e:
        print(f"Facebook API error: {e}")
    return None, None

def fetch_twitter_profile(phone_or_email):
    url = f"https://api.twitter.com/2/users/by?usernames={phone_or_email}"
    headers = {"Authorization": "Bearer your_twitter_bearer_token"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data['data']:
                return f"https://twitter.com/{data['data'][0]['username']}", data['data'][0]['name']
    except Exception as e:
        print(f"Twitter API error: {e}")
    return None, None

def fetch_instagram_profile(phone_or_email):
    url = f"https://www.instagram.com/{phone_or_email}/?__a=1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"https://www.instagram.com/{phone_or_email}/", data['graphql']['user']['full_name']
    except Exception as e:
        print(f"Instagram API error: {e}")
    return None, None

def fetch_social_profiles(phone_or_email):
    social_profiles = {
        "facebook": None,
        "twitter": None,
        "instagram": None,
        "name": None
    }
    
    if re.match(r"^[+]*[0-9]+$", phone_or_email):
        social_profiles["facebook"], social_profiles["facebook_name"] = fetch_facebook_profile(phone_or_email)
        social_profiles["twitter"], social_profiles["twitter_name"] = fetch_twitter_profile(phone_or_email)
        social_profiles["instagram"], social_profiles["instagram_name"] = fetch_instagram_profile(phone_or_email)
    elif re.match(r"[^@]+@[^@]+\.[^@]+", phone_or_email):
        social_profiles["facebook"], social_profiles["facebook_name"] = fetch_facebook_profile(phone_or_email)
        social_profiles["twitter"], social_profiles["twitter_name"] = fetch_twitter_profile(phone_or_email)
        social_profiles["instagram"], social_profiles["instagram_name"] = fetch_instagram_profile(phone_or_email)
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
    print(f"📘 Facebook: https://facebook.com/Omar.Hany.850")
    print(f"📷 Instagram: https://instagram.com/omar.hany.850")
