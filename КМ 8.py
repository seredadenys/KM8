import requests
dog_ceo_resp = requests.get("https://dog.ceo/api/breeds/image/random")
dog_ceo_data = dog_ceo_resp.json()
image_url = dog_ceo_data["message"]
breed_info = image_url.split("/")[4]

if "-" in breed_info:
    main_breed, sub_breed = breed_info.split("-")
    breed_query = f"{sub_breed} {main_breed}".lower()
    breed_name = f"{sub_breed.title()} {main_breed.title()}"
else:
    breed_query = breed_info.lower()
    breed_name = breed_info.title()
headers = {"x-api-key": "DEMO-API-KEY"} 
search_url = f"https://api.thedogapi.com/v1/breeds/search?q={breed_query}"
search_resp = requests.get(search_url, headers=headers)
search_data = search_resp.json()
print("Зображення:", image_url)
print("Порода:", breed_name)
if search_data:
    description = search_data[0].get("temperament", "Опису немає.")
    print("Опис:", description)
else:
    print("Опис: Інформація про породу не знайдена.")