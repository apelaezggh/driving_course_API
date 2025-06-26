#!/usr/bin/env python3
import requests
import time
import json

# Configuration
API_BASE_URL = "http://localhost:8000"
TEST_EMAIL = "testingworkapg@gmail.com"
TEST_PASSWORD = "password123"

def test_refresh_token():
    print("Testing refresh token functionality...")
    
    # Step 1: Login to get access token and refresh token
    print("\n1. Logging in...")
    login_data = {
        "username": TEST_EMAIL,
        "password": TEST_PASSWORD
    }
    
    login_response = requests.post(
        f"{API_BASE_URL}/token",
        data=login_data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    
    if login_response.status_code != 200:
        print(f"Login failed: {login_response.status_code}")
        print(login_response.text)
        return
    
    login_data = login_response.json()
    access_token = login_data["access_token"]
    refresh_token = login_data["refresh_token"]
    
    print(f"Login successful!")
    print(f"Access token: {access_token[:50]}...")
    print(f"Refresh token: {refresh_token[:50]}...")
    
    # Step 2: Test that access token works
    print("\n2. Testing access token...")
    headers = {"Authorization": f"Bearer {access_token}"}
    me_response = requests.get(f"{API_BASE_URL}/users/me", headers=headers)
    
    if me_response.status_code == 200:
        print("Access token is valid!")
    else:
        print(f"Access token failed: {me_response.status_code}")
        print(me_response.text)
        return
    
    # Step 3: Wait for token to expire (1 minute)
    print("\n3. Waiting for access token to expire (1 minute)...")
    time.sleep(65)  # Wait 65 seconds to ensure token expires
    
    # Step 4: Test that access token is expired
    print("\n4. Testing expired access token...")
    me_response = requests.get(f"{API_BASE_URL}/users/me", headers=headers)
    
    if me_response.status_code == 401:
        print("Access token is expired (expected)!")
    else:
        print(f"Access token still valid: {me_response.status_code}")
        print("Token might not have expired yet, waiting a bit more...")
        time.sleep(30)
        me_response = requests.get(f"{API_BASE_URL}/users/me", headers=headers)
        if me_response.status_code == 401:
            print("Access token is now expired!")
        else:
            print(f"Access token still valid after additional wait: {me_response.status_code}")
            return
    
    # Step 5: Test refresh token
    print("\n5. Testing refresh token...")
    refresh_data = {"refresh_token": refresh_token}
    refresh_response = requests.post(f"{API_BASE_URL}/refresh", json=refresh_data)
    
    if refresh_response.status_code == 200:
        print("Refresh token worked!")
        new_tokens = refresh_response.json()
        new_access_token = new_tokens["access_token"]
        new_refresh_token = new_tokens["refresh_token"]
        
        print(f"New access token: {new_access_token[:50]}...")
        print(f"New refresh token: {new_refresh_token[:50]}...")
        
        # Step 6: Test new access token
        print("\n6. Testing new access token...")
        new_headers = {"Authorization": f"Bearer {new_access_token}"}
        me_response = requests.get(f"{API_BASE_URL}/users/me", headers=new_headers)
        
        if me_response.status_code == 200:
            print("New access token works!")
            print("✅ Refresh token test PASSED!")
        else:
            print(f"New access token failed: {me_response.status_code}")
            print(me_response.text)
            print("❌ Refresh token test FAILED!")
    else:
        print(f"Refresh token failed: {refresh_response.status_code}")
        print(refresh_response.text)
        print("❌ Refresh token test FAILED!")

if __name__ == "__main__":
    test_refresh_token() 