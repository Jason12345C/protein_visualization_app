import requests
from bs4 import BeautifulSoup

def get_data(doc_url):
    # Fetch the document content
    response = requests.get(doc_url)
    response.raise_for_status()  # Raise an error if the request fails
    
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the table element
    table = soup.find("table")
    if not table:
        raise ValueError("Table not found in the document")

    data = []
    
    # Iterate over table rows (skip header)
    for row in table.find_all("tr")[1:]:  # Skip header row
        cells = row.find_all("td")
        if len(cells) == 3:
            x = cells[0].text.strip()
            char = cells[1].text.strip()
            y = cells[2].text.strip()
            data.append((int(x), char, int(y)))
    
    return data

def decode(doc_url)
    data = decode(doc_url)


    # Find grid size
    max_x = max(data, key=lambda x: x[0])[0] + 1
    max_y = max(data, key=lambda x: x[2])[2] + 1

    # Initialize the grid with spaces
    grid = [[' ' for _ in range(max_x)] for _ in range(max_y)]

    # Populate the grid based on data
    for x, symbol, y in data:
        grid[y][x] = symbol  # Ensure correct positioning

    # Print the grid
    for row in grid:
        print(''.join(row))