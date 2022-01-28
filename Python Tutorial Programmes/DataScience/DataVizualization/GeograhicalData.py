# Many open source python libraries now have been created to represent the geographical maps.
# They are highly customizable and offer a varierty of maps depicting areas in different shapes and colours.

import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # make the map global rather than have it zoom in to
    # the extents of any plotted data

ax.set_extent((60, 150, 55, -25))

ax.stock_img()
ax.coastlines()

ax.tissot(facecolor='purple', alpha=0.8)

plt.show()