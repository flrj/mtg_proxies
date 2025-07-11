latex_head = """\\documentclass[8pt]{extarticle}
\\usepackage{geometry}
\\usepackage{graphicx}
\\usepackage[frame, a4, center]{crop}

\\geometry{
	paperwidth=63mm,
	paperheight=88mm,
	margin=5mm
}

\\setlength{\\parindent}{0cm}

\\input{mana_icons/mana_commands.tex}

\\begin{document}"""

latex_end = "\\end{document}"""

def concat_card_face(card_json):
    # card name and mana cost
    latex_body = "{\\large\\textbf{" + card_json["name"] + "}}"
    if card_json["mana_cost"] != "":
        latex_body += "\n\\hfill\n"
        latex_body += card_json["mana_cost"].replace("}", "").replace("{", "\\").replace("/", "")
    latex_body += "\n"
    
    # type line
    latex_body += "\n" + "\\textbf{" + card_json["type_line"] + "}\n"

    # card text
    latex_body += "\n" + card_json["oracle_text"].replace("}", "").replace("{", "\\").replace("/", "") + "\n"
    
    # bottom line, e.g. power/toughness
    print(card_json.keys())
    if "power" in card_json.keys() and "toughness" in card_json.keys():
        print("is creature")
        latex_body += "\n\\hfill" + card_json["power"] + "/" + card_json["toughness"] + "\n"
    if "loyalty" in card_json.keys():
        print("is planeswalker")
        latex_body += "\n\\hfill" + card_json["loyalty"] + "\n"
    if "defense" in card_json.keys():
        print("is siege")
        latex_body += "\n\\hfill" + card_json["defense"] + "\n"

    return latex_body