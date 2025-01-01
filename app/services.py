import requests
import random
from flask import current_app
from app.utils import round_money, round_cpm

class MonetagService:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {current_app.config['BEARER_TOKEN']}"
        }
        self.base_url = current_app.config['BASE_URL']
        self.site_id = current_app.config['SITE_ID']

    def create_zone(self):
        title = f"Zone {random.randint(1000, 9999)}"
        url = f"{self.base_url}/sites/{self.site_id}/zones/"
        
        response = requests.post(url, headers=self.headers, json={"title": title})
        data = response.json()
        
        return {
            "zone_id": data["id"],
            "title": data["title"],
            "tag_url": data["tag_url"]
        }

    def get_stats(self, date_range):
        url = f"{self.base_url}/stats/"
        params = {"date": date_range}
        
        response = requests.get(url, headers=self.headers, params=params)
        data = response.json()
        
        return {
            "money": round_money(data["money"]),
            "cpm": round_cpm(data["cpm"])
        }

