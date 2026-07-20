from services.opportunity_scanner import OpportunityScanner


scanner = OpportunityScanner()


resultado = scanner.scan()


print("\n==============================")
print("OPORTUNIDADES ENCONTRADAS")
print("==============================\n")


if not resultado:

    print("Nenhuma oportunidade encontrada")



for item in resultado:

    print("------------------------------")

    print("BETANO:")

    print(item["betano"])


    print("\nSOFASCORE:")

    print(item["sofa"])


    print("\nSCORE:")

    print(item["score"])