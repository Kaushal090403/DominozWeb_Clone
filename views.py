from django.shortcuts import render
import folium


def locate(request):
    lat_lng = [19.0178, 72.8478]

    # Create a Figure object with specific width and height
    f = folium.Figure(width=500, height=500)

    # Create a Map object centered at lat_lng with zoom level 16
    th = folium.Map(location=lat_lng, zoom_start=16)

    # Add a Marker at lat_lng with a tooltip
    folium.Marker(lat_lng, tooltip="Dadar").add_to(th)

    # Add the Map object to the Figure object
    th.add_to(f)

    # Get the HTML representation of the Figure object
    map_html = f._repr_html_()

    return render(request, "locate.html", {"map_html": map_html})
