import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv
import os

load_dotenv()

transactions_collection = os.getenv("FIREBASE_TRANSACTION_COLLECTION")

# Use a service account.
cred = credentials.Certificate('./pessoal-b6cd9-firebase-adminsdk-rxiwm-9cfc742560.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

def save_to_firestore(my_list, collection_name=transactions_collection):
    """
    Save the given list to Firebase Firestore.
    
    Args:
    - my_list (list): The list to save.
    - collection_name (str): The Firestore collection name where the list should be saved. Default is "default_collection".
    """
    firebase_last_transaction = get_last_transaction_firebase()
    collection_ref = db.collection(collection_name)
    for item in my_list:
        if firebase_last_transaction is not None and item["id"] == firebase_last_transaction["id"]:
            break
        item["added_to_notion"] = False
        # You can customize the way you save each item here.
        # For this example, we are saving each item as a document with a single field called "value".
        collection_ref.document(item["id"]).set(item)
        # .add({"value": item})


def get_last_transaction_firebase():
    """
    Get the last transaction from Firebase Firestore.
    
    Returns:
    - last_transaction (dict): The last transaction from Firebase Firestore.
    """
    collection_ref = db.collection(transactions_collection)
    last_transaction = collection_ref.order_by("time", direction=firestore.Query.DESCENDING).limit(1).get()
    if len(last_transaction) == 0:
        return None
    return last_transaction[0].to_dict()

if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5]
    save_to_firestore(test_list)