import argparse
import requests
import os
from df_cards import create_df_proxy

def main(args):
    # Access the user input
    card_set = args.set.lower()
    card_nr = args.nr
    card_lang = args.lang

    if card_lang == None:
        card_lang = "en"

    card_lang = card_lang.lower()

    # Print the user input
    print(f"set: {card_set}")
    print(f"number: {card_nr}")
    print(f"language: {card_lang}")

    scryfall_url = f"https://api.scryfall.com/cards/{card_set}/{card_nr}/{card_lang}"
    response = requests.get(scryfall_url)
    card_json = response.json()

    filename = "".join(card_json["name"].title().split()).replace("//", "_").replace(",", "").replace("'", "")
    print(f"filename: {filename}")

    # double faced card to .tex format
    if "card_faces" in card_json:
        print("double face card detected")
        proxy_text = create_df_proxy(card_json)
    else:
        print("not yet possible")

    # write to .tex file
    with open("tex_files/" + filename + ".tex", "w") as tex_file:
        tex_file.write(proxy_text)

    os.system(f"pdflatex -output-directory=pdf_files tex_files/{filename}.tex")

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="A simple script to fetch card data and set up double face card proxies.")

    # Add an argument for user input
    parser.add_argument("--set", type=str, required=True, help="3-5 digit set code")
    parser.add_argument("--nr", type=int, required=True, help="collector number")
    parser.add_argument("--lang", type=str, required=False, help="language of the card")

    # Parse the arguments
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args)