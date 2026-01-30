import json
import os
import shutil

# Load links from links.json
with open('links.json', 'r') as f:
    links_data = json.load(f)

# Webpage shown during redirect process
template = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Bitte warten | Please wait</title>
    <meta name="robots" content="noindex, nofollow">
    <link rel="canonical" href="{url}">
    <meta http-equiv="refresh" content="0; url={url}">
    <script>window.location.replace("{url}")</script>
</head>
<body>
    <p>Sie werden zu <a href="{url}">{url}</a> weitergeleitet...</p>
    <p>You are being redirected to <a href="{url}">{url}</a>...</p>
</body>
</html>
"""

# Process each link entry
for entry in links_data:
    destination_url = entry['url']
    aliases = entry['aliases']
    
    for slug in aliases:
        # Clean the slug (remove spaces/special characters)
        slug = slug.strip().lower()
        
        # Create a directory for the alias
        os.makedirs(slug, exist_ok=True)
        
        # Write the redirect file
        with open(os.path.join(slug, 'index.html'), 'w') as f:
            f.write(template.format(url=destination_url))
        
        print(f"Created redirect: /{slug} -> {destination_url}")

print("\nAll aliases generated!")
