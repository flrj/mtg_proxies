import re
from template import *

def create_df_proxy(card_json):
    card_json = card_json["card_faces"]

    for i, card in enumerate(card_json):
        new_keys = ["name", "mana_cost", "type_line", "oracle_text"]

        card_json[i] = {k: card_json[i][k] for k in new_keys}
        card_json[i]["oracle_text"] = re.sub("[\(\[].*?[\)\]]", "", card_json[i]["oracle_text"]).strip()

    # card name 1 and mana cost
    latex_body = "{\\large\\textbf{" + card_json[0]["name"] + "}}"
    latex_body += "\n\\hfill\n"
    latex_body += card_json[0]["mana_cost"].replace("}", "").replace("{", "\\") + "\n"
    
    # type line
    latex_body += "\n" + "\\textbf{" + card_json[0]["type_line"] + "}\n"

    # card text
    latex_body += "\n" + card_json[0]["oracle_text"]

    latex = latex_head + "\n" + latex_body + "\n" + latex_end

    return latex