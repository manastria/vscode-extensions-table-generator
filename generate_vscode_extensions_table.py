import requests

def get_extension_details(extension_id):
    url = 'https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery'
    headers = {
        'Accept': 'application/json; charset=utf-8; api-version=7.2-preview.1'
    }
    body = {
        "filters": [
            {
                "criteria": [
                    {
                        "filterType": 7,  # Filter by extension name
                        "value": extension_id
                    }
                ],
                "pageNumber": 1,
                "pageSize": 1,
                "sortBy": 0,
                "sortOrder": 0
            }
        ],
        "assetTypes": [],
        "flags": 0x1 | 0x2 | 0x4 | 0x8 | 0x10 | 0x20 | 0x40 | 0x80 | 0x100 | 0x200 | 0x1000 | 0x8000
    }

    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()
    return response.json()

def generate_markdown_table(extension_ids):
    table_header = """
| Unique Identifier | Marketplace Link | VSCode Install Link | Short Description |
| ----------------- | ---------------- | ------------------- | ----------------- |
"""
    table_rows = []

    for extension_id in extension_ids:
        extension_details = get_extension_details(extension_id)
        extension_info = extension_details['results'][0]['extensions'][0]
        extension_name = extension_info['extensionName']
        display_name = extension_info['displayName']
        short_description = extension_info['shortDescription']
        marketplace_link = f"https://marketplace.visualstudio.com/items?itemName={extension_id}"
        vscode_install_link = f"vscode:extension/{extension_id}"

        row = f"| {extension_id} | [{display_name}]({marketplace_link}) | [{extension_name}]({vscode_install_link}) | {short_description} |"
        table_rows.append(row)

    return table_header + "\n".join(table_rows)

# List of Unique Identifiers
extension_ids = ['eamodio.gitlens', 'donjayamanne.githistory', 'mhutchie.git-graph']

# Generate the Markdown table
markdown_table = generate_markdown_table(extension_ids)

# Write the table to a file
with open('extensions_table.md', 'w', encoding='utf-8') as file:
    file.write(markdown_table)
