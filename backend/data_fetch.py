import requests

def get_policy_data(policy_name):
    api_url = f"https://api.data.gov/policy-data?query={policy_name}"  # Example endpoint
    response = requests.get(api_url)
    return response.json()

if __name__ == "__main__":
    policy_name = "infrastructure spending"
    print(get_policy_data(policy_name))
