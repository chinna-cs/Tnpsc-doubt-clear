print("Vanakkam Ma! Naan TNPSC AI Assistant!")

while True:
    doubt = input("\nUngal Doubt Enna Ma? (velila vara 'exit' nu type pannunga): ")

    if doubt.lower() == 'exit':
        print("Okay Ma! Padichittu topper agunga! All the best Ma!")
        break

    if doubt.strip() == "":
        print("Ma, doubt-a type pannave illa ma!")
        continue

    print(f"\nSuper Ma! Ungal Doubt: {doubt}")
    print("Ithukku answer naan kathukittu varen Ma...")

    # Intha idathula than neenga AI answer-a add pannanum
    # Ippo naan sample answer potruken
    print(f"'{doubt}' - ithu pathi naan thedivittu ungalukku solluren Ma!")
