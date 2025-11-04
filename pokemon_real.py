import re

def is_pokemon_real(pokemon_name):
    partner_flag = False

    if partner_flag == False:
        cleaned_name = re.sub(r"[~`!@#$%^&*()_+{}\[\]|\\:;\"'<,>.?/]", "", pokemon_name)
        partner_flag = True

    else:
        print(f'{cleaned_name} is not a real Pokemon name, Please try again.')
        return None



def link_pokemon(pokemon_name):
    partner = pb.pokemon(cleaned_name)
    if partner_flag == True & partner == pokemon_name:
        response = ""
        response += f"Name: {partner.name}\n"
        response += f"Height: {partner.height}\n"
        response += f"Weight: {partner.weight}\n"
        response += f"Types: {partner.types}\n"
        return response
    else:
        print(f'{cleaned_name} is not a real Pokemon name, Please try again.')
        return None
    
