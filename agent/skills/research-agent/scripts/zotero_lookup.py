import sqlite3
import sys
import os

DB_PATH = "/Users/rishabhpatra/Zotero/zotero.sqlite"
STORAGE_ROOT = "/Users/rishabhpatra/Zotero/storage/"

def lookup_paper(query):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # SQL to find the paper, its storage key, and its collection
    sql = """
    SELECT 
        items.key, 
        idv.value as title,
        c.collectionName,
        ia.path
    FROM items
    JOIN itemData id ON items.itemID = id.itemID
    JOIN itemDataValues idv ON id.valueID = idv.valueID
    LEFT JOIN itemAttachments ia ON items.itemID = ia.parentItemID
    LEFT JOIN collectionItems ci ON items.itemID = ci.itemID
    LEFT JOIN collections c ON ci.collectionID = c.collectionID
    WHERE idv.value LIKE ? 
    AND ia.path IS NOT NULL
    LIMIT 5;
    """
    
    search = f"%{query}%"
    cursor.execute(sql, (search,))
    results = cursor.fetchall()
    
    if not results:
        print(f"No papers found matching: {query}")
        return

    print(f"\nFound {len(results)} matching papers:\n")
    for key, title, collection, pdf_path in results:
        # Zotero paths are often "storage:filename.pdf"
        clean_pdf = pdf_path.replace("storage:", "") if pdf_path else "No PDF found"
        full_folder_path = os.path.join(STORAGE_ROOT, key)
        
        print(f"TITLE: {title}")
        print(f"COLLECTION: {collection if collection else 'Root'}")
        print(f"FOLDER KEY: {key}")
        print(f"FULL PATH: {full_folder_path}/{clean_pdf}")
        print("-" * 30)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python zotero_lookup.py 'Paper Title Keywords'")
    else:
        lookup_paper(" ".join(sys.argv[1:]))
