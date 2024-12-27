import re
from template import *

def create_df_proxy(card_json):
    card_json = card_json["card_faces"]

    for i, card in enumerate(card_json):
        #new_keys = ["name", "mana_cost", "type_line", "oracle_text"]

        #card_json[i] = {k: card_json[i][k] for k in new_keys}
        card_json[i]["oracle_text"] = re.sub("[\(\[].*?[\)\]]", "", card_json[i]["oracle_text"]).strip()
        card_json[i]["oracle_text"] = card_json[i]["oracle_text"].replace("\n", "\n\n")

    latex_body = concat_card_face(card_json[0])
    latex_body += "\n\\vfill\n\\hrule\n\\vfill\n\n"
    latex_body += concat_card_face(card_json[1])

    latex = latex_head + "\n" + latex_body + "\n" + latex_end

    return latex