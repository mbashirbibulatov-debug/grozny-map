import folium



locations = [
    {
        "name": "Грозный-Сити",
        "coords": [43.3151, 45.6941],
        "type": "Развлечения",
        "color": "blue"
    },
    {
        "name": "Мечеть Сердце Чечни ",
        "coords": [43.3177, 45.6949],
        "type": "Культура",
        "color": "green"
    },
    {
        "name": "ТЦ Грозный Молл",
        "coords": [43.3160, 45.6910],
        "type": "Магазин",
        "color": "red",
    }
]


my_map = folium.Map(location=[43.3151, 45.6941], zoom_start=15, tiles='Cartodb Positron')



for place in locations:
    folium.Marker(
        location=place["coords"],
        popup=f"Объект: {place['name']}\nТип: {place['type']}",
        icon=folium.Icon(color=place["color"], icon='info-sign')
    ).add_to (my_map)



my_map.save("/Users/muhammad/Desktop/index.html")


print(f"Готово! Мухаммад, я обработал объектов: {len(locations)}") 












