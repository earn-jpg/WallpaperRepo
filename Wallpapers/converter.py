# your link goes here
link = "https://github.com/earn-jpg/WallpaperRepo/blob/main/Wallpapers/walpappre%20(1).jpg"

# note: this will break if a repo/organization or subfolder is named "blob" -- would be ideal to use a fancy regex
# to be more precise here
print(link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/"))

# example output link:
# https://raw.githubusercontent.com/earn-jpg/WallpaperRepo/Wallpapers/walpappre%20(1).jpg

